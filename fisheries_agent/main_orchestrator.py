import os
import json
import shutil
from datetime import datetime
import yaml
from pathlib import Path
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

from utils import gitsync
from utils.runner import find_rscript, new_run_dir, run_command, run_r_template, truncate
from utils.safety import (
    SafetyError, clamp_iterations, parse_zi_formula, project_roots, resolve_in_roots,
    validate_columns, validate_csv, validate_method, validate_prefix_columns,
)

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
MANIFEST_PATH = BASE_DIR / "project_manifest.yaml"
BRAIN_SOURCES_DIR = BASE_DIR / "00_Fisheries_Brain" / "01_Sources"

load_dotenv(ENV_PATH)

# Override with OPENROUTER_MODEL in .env; pick a tool-capable model from openrouter.ai/models.
MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.5")

_client = None

def get_client():
    """Creates the OpenRouter client on first use so a missing key gives a clear error."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.startswith("your_"):
            raise RuntimeError(
                f"OPENROUTER_API_KEY is not set. Add it to {ENV_PATH} (see .env.template)."
            )
        _client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    return _client

def load_manifest():
    """Loads the scientist's specific RProject infrastructure map."""
    if not MANIFEST_PATH.exists():
        print("⚠️ Warning: project_manifest.yaml not found. Run setup_onboarding.py first.")
        return {}
    with open(MANIFEST_PATH, "r") as f:
        return yaml.safe_load(f) or {}

# =====================================================================
# --- TOOLS (all execution goes through utils.runner / utils.safety) ---
# =====================================================================

def search_fisheries_brain(keyword: str):
    """Scans the Obsidian 01_Sources folder markdown files for literature context."""
    context_snippets = []
    if not BRAIN_SOURCES_DIR.exists():
        return "Fisheries brain sources directory missing."

    for md_file in BRAIN_SOURCES_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if keyword.lower() in content.lower():
            context_snippets.append(f"--- Source: {md_file.name} ---\n{content[:1500]}\n")

    if not context_snippets:
        return f"No direct matches found in literature for keyword: '{keyword}'."
    return "\n".join(context_snippets[:3])

READABLE_SUFFIXES = {".txt", ".md", ".csv", ".tsv", ".log", ".r", ".rmd", ".qmd", ".json", ".yaml", ".yml", ".out", ".html"}
MAX_LISTED_FILES = 200

def _project_root(project_name: str) -> Path:
    project = load_manifest().get("projects", {}).get(project_name)
    if not project:
        raise SafetyError(f"Project '{project_name}' is not recognized in the system manifest.")
    return Path(project["project_path"]).resolve()

def list_project_files(project_name: str, subfolder: str = ""):
    """Lists files in a registered project, newest first (read-only)."""
    root = _project_root(project_name)
    base = resolve_in_roots(str(root / subfolder), [root])
    if not base.is_dir():
        return f"Error: '{subfolder}' is not a folder in project '{project_name}'."
    found = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):
                continue
            full = Path(dirpath) / name
            try:
                found.append((full.stat().st_mtime, full.relative_to(root).as_posix()))
            except (OSError, ValueError):
                continue
    found.sort(reverse=True)
    lines = [f"{datetime.fromtimestamp(m):%Y-%m-%d %H:%M}  {rel}" for m, rel in found[:MAX_LISTED_FILES]]
    note = f"\n(showing {len(lines)} of {len(found)} files, newest first)" if found else "No files found."
    return "\n".join(lines) + note

def read_project_file(project_name: str, file_path: str):
    """Reads a text-based file (results, logs, scripts, small tables) from a registered project."""
    root = _project_root(project_name)
    target = resolve_in_roots(str(root / file_path), [root])
    if not target.is_file() or target.name.startswith("."):
        return f"Error: '{file_path}' not found in project '{project_name}'."
    if target.suffix.lower() not in READABLE_SUFFIXES:
        return f"Error: files of type '{target.suffix}' cannot be read as text."
    return truncate(target.read_text(encoding="utf-8", errors="replace"))

def _result_text(ok: bool, out: str, run_dir, output_name="output.txt") -> str:
    if run_dir and output_name and (Path(run_dir) / output_name).is_file():
        out = (Path(run_dir) / output_name).read_text(encoding="utf-8", errors="replace")
    status = "Succeeded" if ok else "Failed"
    where = f"\nFiles saved in: {run_dir}" if run_dir else ""
    return f"{status}.{where}\n{truncate(out)}"

def run_project_pipeline(project_name: str, script_name: str):
    """Runs an .R, .Rmd or .qmd file inside a registered project folder."""
    manifest = load_manifest()
    project = manifest.get("projects", {}).get(project_name)
    if not project:
        return f"Error: Project '{project_name}' is not recognized in the system manifest."

    root = Path(project["project_path"]).resolve()
    target = resolve_in_roots(str(root / script_name), [root])
    if not target.is_file():
        return f"Error: Script '{script_name}' not found in project '{project_name}'."

    suffix = target.suffix.lower()
    rscript = find_rscript()
    if suffix == ".r":
        if not rscript:
            return "Error: Rscript was not found."
        cmd = [rscript, "--vanilla", str(target)]
    elif suffix == ".rmd":
        if not rscript:
            return "Error: Rscript was not found."
        cmd = [rscript, "--vanilla", "-e", "rmarkdown::render(commandArgs(TRUE)[1])", str(target)]
    elif suffix == ".qmd":
        quarto = shutil.which("quarto")
        if not quarto:
            return "Error: Quarto was not found on PATH."
        cmd = [quarto, "render", str(target)]
    else:
        return "Error: Only .R, .Rmd and .qmd files can be run."

    run_dir = new_run_dir(f"pipeline_{project_name}")
    ok, out = run_command(cmd, cwd=root, log_dir=run_dir)
    return _result_text(ok, out, run_dir, output_name=None)

def run_zero_inflated_model(csv_path: str, response_var: str, predictor_vars: list, zero_inflation_formula: str = "~1"):
    """Fits a zero-inflated negative binomial model with glmmTMB."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    validate_columns(csv_file, [response_var, *predictor_vars])
    zi = parse_zi_formula(zero_inflation_formula, csv_file)
    ok, out, run_dir = run_r_template("zinb.R", csv_file, [response_var, ",".join(predictor_vars), zi], "zinb")
    return _result_text(ok, out, run_dir)

def run_nimble_mark_recapture(csv_path: str, capture_history_col: str, iterations: int = 10000):
    """Runs a Cormack-Jolly-Seber MCMC with NIMBLE."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    prefix = validate_prefix_columns(csv_file, capture_history_col)
    ok, out, run_dir = run_r_template("cjs.R", csv_file, [prefix, clamp_iterations(iterations)], "cjs")
    return _result_text(ok, out, run_dir)

def run_multivariate_exploration(csv_path: str, method: str = "PCA"):
    """Draws a PCA, MDS or heatmap plot with vegan."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    ok, out, run_dir = run_r_template("explore.R", csv_file, [validate_method(method)], "explore")
    return _result_text(ok, out, run_dir)

# =====================================================================
# --- OPENROUTER TOOL SCHEMAS ---
# =====================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_fisheries_brain",
            "description": "Searches the Obsidian literature reference for general fisheries science, methods and guidance. Use ONLY for general fisheries questions or when planning a new analysis. NEVER use it to answer questions about the user's own project results or data; use list_project_files and read_project_file for those.",
            "parameters": {"type": "object", "properties": {"keyword": {"type": "string"}}, "required": ["keyword"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_project_files",
            "description": "Lists files in one of the user's registered projects, newest first. Use first for any question about a project's existing results, outputs, data or scripts.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "subfolder": {"type": "string", "description": "Optional folder relative to the project root"}},
                "required": ["project_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_project_file",
            "description": "Reads a text file (results, logs, scripts, csv, md, qmd) from a registered project to report what a past run produced.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "file_path": {"type": "string", "description": "Path relative to the project folder"}},
                "required": ["project_name", "file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_project_pipeline",
            "description": "Runs an existing .R, .Rmd or .qmd script inside one of the user's registered projects.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "script_name": {"type": "string", "description": "Path relative to the project folder"}},
                "required": ["project_name", "script_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_zero_inflated_model",
            "description": "Fits zero-inflated negative binomial models via glmmTMB.",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_path": {"type": "string"}, "response_var": {"type": "string"},
                    "predictor_vars": {"type": "array", "items": {"type": "string"}},
                    "zero_inflation_formula": {"type": "string", "description": "e.g. '~1' or '~ depth + gear'"}
                },
                "required": ["csv_path", "response_var", "predictor_vars"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_nimble_mark_recapture",
            "description": "Launches a Bayesian NIMBLE MCMC analysis for tag resight metric histories.",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_path": {"type": "string"},
                    "capture_history_col": {"type": "string", "description": "Column-name prefix shared by the occasion columns"},
                    "iterations": {"type": "integer"}
                },
                "required": ["csv_path", "capture_history_col"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_multivariate_exploration",
            "description": "Generates PCA, MDS, or Heatmap plots using R vegan.",
            "parameters": {
                "type": "object",
                "properties": {"csv_path": {"type": "string"}, "method": {"type": "string", "enum": ["PCA", "MDS", "HEATMAP"]}},
                "required": ["csv_path", "method"]
            }
        }
    }
]

available_functions = {
    "search_fisheries_brain": search_fisheries_brain,
    "list_project_files": list_project_files,
    "read_project_file": read_project_file,
    "run_project_pipeline": run_project_pipeline,
    "run_zero_inflated_model": run_zero_inflated_model,
    "run_nimble_mark_recapture": run_nimble_mark_recapture,
    "run_multivariate_exploration": run_multivariate_exploration
}

# Read-only lookups run without a prompt; everything else needs the user's approval.
NO_CONFIRMATION_NEEDED = {"search_fisheries_brain", "list_project_files", "read_project_file"}

def confirm_run(function_name: str, function_args: dict) -> bool:
    print(f"\n🔔 The agent wants to run: {function_name}")
    for key, value in function_args.items():
        print(f"     {key}: {value}")
    answer = input("   Approve this run? (y/n): ").strip().lower()
    return answer in ("y", "yes")

# Tools that can create or modify files inside a project folder.
PROJECT_WRITING_TOOLS = {"run_project_pipeline"}

def _git_root_for_call(function_name: str, function_args: dict):
    if function_name not in PROJECT_WRITING_TOOLS:
        return None
    try:
        root = _project_root(function_args.get("project_name", ""))
    except SafetyError:
        return None
    return root if gitsync.is_git_project(root) else None

def _git_followup(root: Path, before: dict, label: str) -> str:
    summary = gitsync.commit_changes(root, before, f"Fisheries agent: {label}")
    print(f"\n📦 {root.name}: {summary}")
    if summary.startswith("Git: committed"):
        answer = input("   Sync this project now (git pull --rebase, then push)? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            summary += "\n" + gitsync.sync(root)
            print(f"   {summary.splitlines()[-1]}")
        else:
            summary += "\nThe user chose not to sync yet."
    return summary

def execute_tool_call(function_name: str, raw_arguments: str) -> str:
    function_to_call = available_functions.get(function_name)
    if not function_to_call:
        return f"Error: unknown tool '{function_name}'."
    try:
        function_args = json.loads(raw_arguments or "{}")
    except json.JSONDecodeError:
        return "Error: tool arguments were not valid JSON."

    if function_name not in NO_CONFIRMATION_NEEDED and not confirm_run(function_name, function_args):
        return "The user declined this run. Do not retry; ask what they would like to change."

    git_root = _git_root_for_call(function_name, function_args)
    before = gitsync.snapshot(git_root) if git_root else None

    print(f"🔄 Running: {function_name}...")
    try:
        result = function_to_call(**function_args)
        if git_root:
            label = f"{function_name} {function_args.get('script_name', '')}".strip()
            result += "\n\n" + _git_followup(git_root, before, label)
        return result
    except SafetyError as e:
        return f"Rejected: {e}"
    except TypeError as e:
        return f"Error: bad tool arguments ({e})."

# =====================================================================
# --- ORCHESTRATION ENGINE LOOP ---
# =====================================================================

MAX_TOOL_ROUNDS = 6

def ask_orchestrator(user_prompt: str, manifest: dict):
    manifest_context = yaml.dump(manifest, default_flow_style=False)

    system_prompt = f"""You are the Master Fisheries Orchestrator Agent.
You run locally on this machine and manage a suite of specialized analysis tools and an Obsidian vault context window.
Maintain formatting and stylistic habits that mirror the scientist's noted documentation habits.
Every analysis run is shown to the user for approval before it executes.

How to choose tools:
- Questions about a specific project's own results, data, outputs or scripts (e.g. "what were the results of the last model run for project X"): go straight to the project. Call list_project_files (newest first), then read_project_file on the relevant results/log/report files. Do NOT call search_fisheries_brain for these.
- General fisheries science, methods, or deciding how to approach a NEW analysis: use search_fisheries_brain as a reference.
- Only use the brain alongside project files if the user asks to interpret results against the literature.
- If you cannot find the requested results, say what you looked at instead of guessing.

Here is the current scientist's machine layout and project structure configuration:
{manifest_context}"""

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

    client = get_client()
    for _ in range(MAX_TOOL_ROUNDS):
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools, tool_choice="auto")
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        if not tool_calls:
            return response_message.content

        messages.append(response_message)
        for tool_call in tool_calls:
            tool_output = execute_tool_call(tool_call.function.name, tool_call.function.arguments)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_call.function.name,
                "content": tool_output,
            })

    final = client.chat.completions.create(model=MODEL, messages=messages)
    return final.choices[0].message.content

if __name__ == "__main__":
    manifest = load_manifest()
    if not manifest:
        print("❌ Cannot start orchestrator without a valid project_manifest.yaml file.")
        exit(1)

    print("\n⚓ Master Fisheries Orchestrator Core Fully Loaded & Online ⚓")
    print("-----------------------------------------------------------------")

    while True:
        try:
            cmd = input("\n🐟 Master Command: ")
            if cmd.lower() == 'exit':
                break
            if not cmd.strip():
                continue
            print(f"\n🤖 Agent Response:\n{ask_orchestrator(cmd, manifest)}")
        except KeyboardInterrupt:
            break
        except RuntimeError as e:
            print(f"❌ {e}")
        except OpenAIError as e:
            print(f"❌ OpenRouter request failed: {e}\n   If the model was not found, set OPENROUTER_MODEL in .env (see openrouter.ai/models).")
