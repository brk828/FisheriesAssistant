import os
import json
import shutil
import yaml
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

from utils.runner import find_rscript, new_run_dir, run_command, run_r_template, truncate
from utils.safety import (
    SafetyError, clamp_iterations, parse_zi_formula, project_roots, resolve_in_roots,
    validate_columns, validate_csv, validate_method, validate_prefix_columns,
)

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
MANIFEST_PATH = BASE_DIR / "project_manifest.yaml"
BRAIN_SOURCES_DIR = BASE_DIR / "00_Fisheries_Brain" / "01_Sources"
MODEL = "anthropic/claude-3.5-sonnet"

load_dotenv(ENV_PATH)

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
            "description": "Searches Obsidian literature summaries for biological or methodology guidelines.",
            "parameters": {"type": "object", "properties": {"keyword": {"type": "string"}}, "required": ["keyword"]}
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
    "run_project_pipeline": run_project_pipeline,
    "run_zero_inflated_model": run_zero_inflated_model,
    "run_nimble_mark_recapture": run_nimble_mark_recapture,
    "run_multivariate_exploration": run_multivariate_exploration
}

# Read-only lookups run without a prompt; everything else needs the user's approval.
NO_CONFIRMATION_NEEDED = {"search_fisheries_brain"}

def confirm_run(function_name: str, function_args: dict) -> bool:
    print(f"\n🔔 The agent wants to run: {function_name}")
    for key, value in function_args.items():
        print(f"     {key}: {value}")
    answer = input("   Approve this run? (y/n): ").strip().lower()
    return answer in ("y", "yes")

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

    print(f"🔄 Running: {function_name}...")
    try:
        return function_to_call(**function_args)
    except SafetyError as e:
        return f"Rejected: {e}"
    except TypeError as e:
        return f"Error: bad tool arguments ({e})."

# =====================================================================
# --- ORCHESTRATION ENGINE LOOP ---
# =====================================================================

def ask_orchestrator(user_prompt: str, manifest: dict):
    manifest_context = yaml.dump(manifest, default_flow_style=False)

    system_prompt = f"""You are the Master Fisheries Orchestrator Agent.
You run locally on this machine and manage a suite of specialized analysis tools and an Obsidian vault context window.
Maintain formatting and stylistic habits that mirror the scientist's noted documentation habits.
Every analysis run is shown to the user for approval before it executes.

Here is the current scientist's machine layout and project structure configuration:
{manifest_context}"""

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

    client = get_client()
    response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools, tool_choice="auto")

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            tool_output = execute_tool_call(tool_call.function.name, tool_call.function.arguments)
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_call.function.name,
                "content": tool_output,
            })

        second_response = client.chat.completions.create(model=MODEL, messages=messages)
        return second_response.choices[0].message.content

    return response_message.content

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
