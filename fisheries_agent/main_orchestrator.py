import os
import re
import json
import shutil
from datetime import datetime
import yaml
from pathlib import Path
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

from utils import brain_index, docx_io, gitsync, icm_data, icm_integration, icm_seed, pdf_ingest, project_memory
from utils.runner import find_rscript, new_run_dir, run_command, run_r_template, run_shell, truncate
from utils.safety import (
    SafetyError, clamp_iterations, parse_zi_formula, project_roots, resolve_in_roots,
    validate_columns, validate_csv, validate_method, validate_prefix_columns,
)

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
MANIFEST_PATH = BASE_DIR / "project_manifest.yaml"

load_dotenv(ENV_PATH)

# Override with OPENROUTER_MODEL in .env; pick a tool-capable model from openrouter.ai/models.
MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.5")
# Cheaper model for simple lookups (project files, brain search). Set OPENROUTER_FAST_MODEL=off to always use MODEL.
FAST_MODEL = os.getenv("OPENROUTER_FAST_MODEL", "anthropic/claude-haiku-4.5")

# Requests that run, plan, interpret or compare go to the main model; plain lookups go to the fast one.
HEAVY_REQUEST = re.compile(
    r"\b(re-?run|run (the|a|an|my|this|that|it)|fit|analy[sz]e|analysis|plan|design|compare|interpret|"
    r"recommend|write|draft|summar(y|ize|ise)|review|synthesi[sz]e|literature|simulate|why|should|how (do|should|would|can))\b", re.I)

def pick_model(user_prompt: str) -> str:
    if FAST_MODEL.lower() in ("", "off", "none") or FAST_MODEL == MODEL:
        return MODEL
    return MODEL if HEAVY_REQUEST.search(user_prompt) else FAST_MODEL

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
    """Stub-first search of the Obsidian vault via the local index (concepts, then source excerpts)."""
    return truncate(brain_index.search_brain(keyword))

def read_brain_source(source_id: str, query: str = ""):
    """Reads the most relevant passages of one vault source document."""
    return truncate(brain_index.read_source(source_id, query))

READABLE_SUFFIXES = {".docx", ".txt", ".md", ".csv", ".tsv", ".log", ".r", ".rmd", ".qmd", ".json", ".yaml", ".yml", ".out", ".html"}
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
    if target.suffix.lower() == ".docx":
        try:
            text = docx_io.read_docx(target)
        except Exception as e:
            return f"Error: could not read Word file ({e})."
    elif target.suffix.lower() not in READABLE_SUFFIXES:
        return f"Error: files of type '{target.suffix}' cannot be read as text."
    else:
        text = target.read_text(encoding="utf-8", errors="replace")
    project_memory.record_file(project_name, root, target.relative_to(root).as_posix(), text)
    return truncate(text)

WRITABLE_SUFFIXES = {".r", ".rmd", ".qmd", ".md", ".txt", ".csv", ".yaml", ".yml", ".json", ".docx"}
MAX_WRITE_CHARS = 200_000

def write_project_file(project_name: str, file_path: str, content: str, overwrite: bool = False):
    """Creates (or, with overwrite, replaces) a text file such as an R script inside a registered project."""
    root = _project_root(project_name)
    target = resolve_in_roots(str(root / file_path), [root])
    rel = target.relative_to(root)
    if any(part.startswith(".") for part in rel.parts):
        return "Error: hidden files and folders cannot be written."
    if target.suffix.lower() not in WRITABLE_SUFFIXES:
        return f"Error: files of type '{target.suffix}' cannot be written. Allowed: {', '.join(sorted(WRITABLE_SUFFIXES))}."
    if len(content) > MAX_WRITE_CHARS:
        return f"Error: content is too large ({len(content)} characters)."
    if target.exists() and not overwrite:
        return f"Error: '{rel.as_posix()}' already exists. Choose a new name, or call again with overwrite=true if the user wants it replaced."
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.suffix.lower() == ".docx":
        try:
            docx_io.write_docx(target, content)
        except Exception as e:
            return f"Error: could not write Word file ({e})."
    else:
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    project_memory.record_file(project_name, root, rel.as_posix(), content)
    return f"Wrote {rel.as_posix()} ({len(content)} characters) in project '{project_name}'."

def _project_for_path(path: Path):
    """Finds the registered project whose folder contains path, as (name, root) or (None, None)."""
    for name, info in load_manifest().get("projects", {}).items():
        root = Path(info["project_path"]).resolve()
        if Path(path).resolve().is_relative_to(root):
            return name, root
    return None, None

def _record_model_run(csv_file: Path, tool: str, label: str, ok: bool, run_dir) -> None:
    name, root = _project_for_path(csv_file)
    if name:
        project_memory.record_run(name, root, tool, ok, label, run_dir, [csv_file.relative_to(root).as_posix()])

def _workspace(project_name: str):
    return icm_integration.workspace_of(load_manifest().get("projects", {}).get(project_name))

def get_project_context(project_name: str, stage: str = ""):
    """Returns the ICM layers (when the project has a workspace) plus remembered notes, key files and recent runs (read-only)."""
    memory = project_memory.context(project_name, _project_root(project_name))
    ws = _workspace(project_name)
    return icm_integration.layered_context(ws, stage) + "\n\n" + memory if ws else memory

def validate_project(project_name: str, full_data_check: bool = False):
    """Checks a project's ICM workspace against the conventions and its linked data against the manifest (read-only)."""
    ws = _workspace(project_name)
    if not ws:
        return f"Project '{project_name}' has no ICM workspace. Offer restructure_project or create_icm_project."
    return icm_integration.validate_workspace(ws, full_data_check)

def refresh_project_references(project_name: str, apply: bool = False):
    """Compares copied reference notes with the brain; with apply=true, updates the changed ones."""
    ws = _workspace(project_name)
    if not ws:
        return f"Project '{project_name}' has no ICM workspace."
    changes = icm_seed.refresh(ws, apply=apply)
    if not changes:
        return "All copied reference notes match the brain."
    lines = "\n".join(f"- {folder}: {sid} {status}" for folder, sid, status in changes)
    return lines + ("\nApplied." if apply else "\nNot applied; call again with apply=true to update.")

def _flow_result(run_flow):
    try:
        return run_flow()
    except SystemExit as e:
        return f"Cancelled: {e}" if e.code not in (None, 0) else "Cancelled."
    except (RuntimeError, ValueError, FileExistsError) as e:
        return f"Error: {e}"

def create_icm_project():
    """Runs the interactive new-project flow, then registers the workspace in the manifest."""
    from utils import icm_wizard
    def flow():
        dest = icm_wizard.run()
        return f"Created ICM project '{icm_integration.register_workspace(dest)}' at {dest} and registered it."
    return _flow_result(flow)

def restructure_project(project_name: str):
    """Runs the interactive restructure flow for a registered project into a new _icm folder; the original is untouched."""
    from utils import icm_restructure
    source = _project_root(project_name)
    def flow():
        dest = icm_restructure.run(source)
        name = icm_integration.register_workspace(dest, original=project_name)
        return f"Restructured '{project_name}' into '{name}' at {dest}; the original was not changed."
    return _flow_result(flow)

def get_latest_results(project_name: str, kind: str = "results"):
    """Finds and reads the newest results (or script/data) file of a project in one step."""
    if kind not in ("results", "script", "data", "any"):
        kind = "results"
    root = _project_root(project_name)
    candidates = project_memory.latest_candidates(project_name, root, kind)
    last_run = project_memory.latest_run_dir_output(project_name) if kind == "results" else None
    parts = []
    if candidates:
        rel, mtime = candidates[0]
        text = read_project_file(project_name, rel)
        parts.append(f"Newest {kind} file: {rel} (modified {datetime.fromtimestamp(mtime):%Y-%m-%d %H:%M})\n{text}")
        others = [f"{datetime.fromtimestamp(m):%Y-%m-%d %H:%M}  {r}" for r, m in candidates[1:6]]
        if others:
            parts.append("Other recent candidates (read with read_project_file):\n" + "\n".join(others))
    else:
        parts.append(f"No {kind} files found in project '{project_name}'. Try list_project_files.")
    if last_run:
        parts.append(f"Last recorded run: {last_run['when']} {last_run['tool']} {last_run.get('label', '')} "
                     f"({'ok' if last_run.get('ok') else 'failed'}); its saved files are in runs/{last_run['run_dir']}.")
    return "\n\n".join(parts)

def remember_project_fact(project_name: str, fact: str = "", pin_file: str = ""):
    """Stores a short fact and/or pins an important file in a project's memory."""
    root = _project_root(project_name)
    out = []
    if fact:
        out.append(project_memory.add_note(project_name, root, fact))
    if pin_file:
        target = resolve_in_roots(str(root / pin_file), [root])
        if not target.is_file():
            out.append(f"Error: '{pin_file}' not found in project '{project_name}'.")
        else:
            project_memory.record_file(project_name, root, target.relative_to(root).as_posix(), pin=True)
            out.append(f"Pinned {pin_file}.")
    return "\n".join(out) or "Nothing to remember."

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

    ws = icm_integration.workspace_of(project)
    stale = icm_data.warnings(ws) if ws else []
    if stale:
        print("\n⚠️ Linked data differs from the workspace manifest:\n" + "\n".join(f"   - {w}" for w in stale))
        if input("   Run anyway? (y/n): ").strip().lower() not in ("y", "yes"):
            return "Not run: linked data changed or is missing:\n" + "\n".join(stale) + "\nAsk the user whether to accept the changes (python -m utils.icm_data <workspace> --accept) or fix the files."

    run_dir = new_run_dir(f"pipeline_{project_name}")
    before = project_memory.scan(root)
    ok, out = run_command(cmd, cwd=root, log_dir=run_dir)
    after = project_memory.scan(root)
    changed = sorted((r for r, m in after.items() if before.get(r) != m), key=lambda r: -after[r])
    project_memory.record_run(project_name, root, "run_project_pipeline", ok, script_name, run_dir, changed)
    for rel in changed[:5]:
        if project_memory.classify(rel) == "results":
            project_memory.record_file(project_name, root, rel)
    return _result_text(ok, out, run_dir, output_name=None)

def run_shell_command(project_name: str, command: str, subfolder: str = "", timeout_seconds: int = 300):
    """Runs a shell command inside a registered project folder. The user approves every command first."""
    root = _project_root(project_name)
    cwd = resolve_in_roots(str(root / subfolder), [root])
    if not cwd.is_dir():
        return f"Error: '{subfolder}' is not a folder in project '{project_name}'."
    if not command.strip():
        return "Error: empty command."
    ok, out = run_shell(command, cwd, max(1, min(int(timeout_seconds), 1800)))
    return _result_text(ok, out, None)

def run_zero_inflated_model(csv_path: str, response_var: str, predictor_vars: list, zero_inflation_formula: str = "~1"):
    """Fits a zero-inflated negative binomial model with glmmTMB."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    validate_columns(csv_file, [response_var, *predictor_vars])
    zi = parse_zi_formula(zero_inflation_formula, csv_file)
    ok, out, run_dir = run_r_template("zinb.R", csv_file, [response_var, ",".join(predictor_vars), zi], "zinb")
    _record_model_run(csv_file, "run_zero_inflated_model", f"{response_var} ~ {' + '.join(predictor_vars)}", ok, run_dir)
    return _result_text(ok, out, run_dir)

def run_nimble_mark_recapture(csv_path: str, capture_history_col: str, iterations: int = 10000):
    """Runs a Cormack-Jolly-Seber MCMC with NIMBLE."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    prefix = validate_prefix_columns(csv_file, capture_history_col)
    ok, out, run_dir = run_r_template("cjs.R", csv_file, [prefix, clamp_iterations(iterations)], "cjs")
    _record_model_run(csv_file, "run_nimble_mark_recapture", f"CJS on {capture_history_col}", ok, run_dir)
    return _result_text(ok, out, run_dir)

def run_multivariate_exploration(csv_path: str, method: str = "PCA"):
    """Draws a PCA, MDS or heatmap plot with vegan."""
    csv_file = validate_csv(csv_path, project_roots(load_manifest()))
    ok, out, run_dir = run_r_template("explore.R", csv_file, [validate_method(method)], "explore")
    _record_model_run(csv_file, "run_multivariate_exploration", method, ok, run_dir)
    return _result_text(ok, out, run_dir)

# =====================================================================
# --- OPENROUTER TOOL SCHEMAS ---
# =====================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_fisheries_brain",
            "description": "Searches the Obsidian literature vault, concept notes first (summary, related concepts, source ids), then source excerpts. Pass a few specific keywords (species, place, method), not a full sentence. To go deeper, search a Related concept's name. Use ONLY for general fisheries questions or when planning a new analysis. NEVER use it to answer questions about the user's own project results or data; use list_project_files and read_project_file for those.",
            "parameters": {"type": "object", "properties": {"keyword": {"type": "string"}}, "required": ["keyword"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_brain_source",
            "description": "Reads the most relevant passages of one vault source document by its id (as listed in search_fisheries_brain results), preceded by a ready-made citation line. Also accepts a concept name from the search results and then returns that concept's summary, related concepts and cited sources. Use only after a search points to a specific source or concept.",
            "parameters": {
                "type": "object",
                "properties": {"source_id": {"type": "string"}, "query": {"type": "string", "description": "Optional keywords to pick the passages"}},
                "required": ["source_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_project_context",
            "description": "Returns what is known about a registered project: for ICM workspaces its AGENTS.md and CONTEXT.md (plus one stage contract when stage is given), then remembered notes, key/pinned files and recent runs. Call this FIRST for any question about a project; load a stage only when working on that stage.",
            "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "stage": {"type": "string", "description": "Optional stage folder name, e.g. 03-analysis"}}, "required": ["project_name"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "validate_project",
            "description": "Validates a project's ICM workspace (structure, stage contracts, skill citations) and checks that linked data files still match the workspace manifest. Use for 'validate project X'.",
            "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "full_data_check": {"type": "boolean", "description": "Recompute hashes of every linked file"}}, "required": ["project_name"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "refresh_project_references",
            "description": "Checks whether reference notes copied into a project's ICM workspace have changed in the Fisheries Brain. Without apply it only reports; with apply=true (needs user approval) it updates them. Use for 'refresh project references'.",
            "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "apply": {"type": "boolean"}}, "required": ["project_name"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_icm_project",
            "description": "Starts the interactive new-project flow (questions, project type, folder tree, git options, optional brain seeding) in the user's terminal and registers the resulting ICM workspace. Takes no arguments; the user answers the questions directly. Use for 'create a project'.",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "restructure_project",
            "description": "Starts the interactive flow that restructures an existing registered project into a new ICM workspace folder (name plus _icm). The original is never modified. The user answers the questions directly. Use for 'restructure project X'.",
            "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}}, "required": ["project_name"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_latest_results",
            "description": "One-step lookup: finds and reads the newest results file of a project (or kind='script' or 'data'), and lists other recent candidates. Use for 'latest/most recent results' questions instead of list_project_files plus read_project_file.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "kind": {"type": "string", "enum": ["results", "script", "data", "any"]}},
                "required": ["project_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "remember_project_fact",
            "description": "Saves a short durable fact about a project (e.g. a convention, an excluded site) and/or pins an important file so future requests find it fast. Use when the user asks you to remember something or says a file is important.",
            "parameters": {
                "type": "object",
                "properties": {"project_name": {"type": "string"}, "fact": {"type": "string"}, "pin_file": {"type": "string", "description": "Path relative to the project folder"}},
                "required": ["project_name"]
            }
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
            "name": "write_project_file",
            "description": "Creates a text file (e.g. a new .R, .Rmd, .qmd script, .md or .csv) inside a registered project. The user must approve each write. Refuses to replace an existing file unless overwrite is true. Use this to save scripts you have written; then offer to run them with run_project_pipeline.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string"},
                    "file_path": {"type": "string", "description": "Path relative to the project folder, e.g. scripts/model.R"},
                    "content": {"type": "string", "description": "Full file contents"},
                    "overwrite": {"type": "boolean"}
                },
                "required": ["project_name", "file_path", "content"]
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
            "name": "run_shell_command",
            "description": "Runs a bash command inside a registered project folder, for tasks the other tools cannot do (installing a package, converting a file, listing or moving files, running git, running an R or Python script). The user sees the exact command and must approve it. Prefer the dedicated tools when they fit. One focused command per call; never use sudo or touch paths outside the project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_name": {"type": "string"},
                    "command": {"type": "string"},
                    "subfolder": {"type": "string", "description": "Working folder relative to the project root."},
                    "timeout_seconds": {"type": "integer"}
                },
                "required": ["project_name", "command"]
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
    "read_brain_source": read_brain_source,
    "get_project_context": get_project_context,
    "get_latest_results": get_latest_results,
    "validate_project": validate_project,
    "refresh_project_references": refresh_project_references,
    "create_icm_project": create_icm_project,
    "restructure_project": restructure_project,
    "remember_project_fact": remember_project_fact,
    "list_project_files": list_project_files,
    "read_project_file": read_project_file,
    "write_project_file": write_project_file,
    "run_project_pipeline": run_project_pipeline,
    "run_shell_command": run_shell_command,
    "run_zero_inflated_model": run_zero_inflated_model,
    "run_nimble_mark_recapture": run_nimble_mark_recapture,
    "run_multivariate_exploration": run_multivariate_exploration
}

# Read-only lookups run without a prompt; everything else needs the user's approval.
NO_CONFIRMATION_NEEDED = {
    "search_fisheries_brain", "read_brain_source", "list_project_files", "read_project_file",
    "get_project_context", "get_latest_results", "remember_project_fact", "validate_project", "refresh_project_references",
}

def needs_confirmation(function_name: str, function_args: dict) -> bool:
    if function_name == "refresh_project_references":
        return bool(function_args.get("apply"))
    return function_name not in NO_CONFIRMATION_NEEDED

def confirm_run(function_name: str, function_args: dict) -> bool:
    print(f"\n🔔 The agent wants to run: {function_name}")
    for key, value in function_args.items():
        print(f"     {key}: {value}")
    answer = input("   Approve this run? (y/n): ").strip().lower()
    return answer in ("y", "yes")

# Tools that can create or modify files inside a project folder.
PROJECT_WRITING_TOOLS = {"run_project_pipeline", "write_project_file", "run_shell_command"}

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

    if needs_confirmation(function_name, function_args) and not confirm_run(function_name, function_args):
        return "The user declined this run. Do not retry; ask what they would like to change."

    git_root = _git_root_for_call(function_name, function_args)
    before = gitsync.snapshot(git_root) if git_root else None

    print(f"🔄 Running: {function_name}...")
    try:
        result = function_to_call(**function_args)
        if git_root:
            label = f"{function_name} {function_args.get('script_name') or function_args.get('file_path', '')}".strip()
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

# Conversation memory: each turn is the list of messages from one user prompt to its final answer.
HISTORY_CHAR_BUDGET = 40000      # ~10k tokens of remembered conversation
RECENT_TURNS_KEPT_FULL = 2       # newer turns keep full tool output; older ones are compacted
COMPACT_TOOL_CHARS = 600

history = []                     # list of turns (each a list of message dicts)
last_prompt_tokens = None

def _msg_chars(msg: dict) -> int:
    return len(json.dumps(msg, default=str))

def _history_chars() -> int:
    return sum(_msg_chars(m) for turn in history for m in turn)

SESSION_NOTES_CHARS = 1600
session_notes = []               # one short line per dropped turn, so old context is not lost entirely

def _note_dropped_turn(turn: list) -> None:
    question = (turn[0].get("content") or "").strip().replace("\n", " ")[:160]
    answer = next((m.get("content") for m in reversed(turn) if m.get("role") == "assistant" and m.get("content")), "")
    session_notes.append(f"- Q: {question} | A: {answer.strip().replace(chr(10), ' ')[:240]}")
    while len(session_notes) > 1 and sum(len(n) for n in session_notes) > SESSION_NOTES_CHARS:
        session_notes.pop(0)

def _compact_turn(turn: list) -> list:
    out = []
    for m in turn:
        if m.get("role") == "tool" and len(m.get("content") or "") > COMPACT_TOOL_CHARS:
            m = {**m, "content": m["content"][:COMPACT_TOOL_CHARS] + "\n...[older tool output trimmed; re-run the tool if you need it again]"}
        out.append(m)
    return out

def trim_history():
    """Compacts old tool output first, then drops the oldest whole turns while over budget."""
    for i in range(len(history) - RECENT_TURNS_KEPT_FULL):
        history[i] = _compact_turn(history[i])
    while len(history) > 1 and _history_chars() > HISTORY_CHAR_BUDGET:
        _note_dropped_turn(history.pop(0))

def clear_history():
    global last_prompt_tokens
    history.clear()
    session_notes.clear()
    last_prompt_tokens = None

def context_status() -> str:
    used = _history_chars()
    pct = min(100, round(100 * used / HISTORY_CHAR_BUDGET))
    bar = "#" * (pct // 10) + "-" * (10 - pct // 10)
    api = f", last request {last_prompt_tokens} tokens" if last_prompt_tokens else ""
    return f"🧠 Memory: {len(history)} turn(s), ~{used // 4} tokens [{bar}] {pct}% of budget{api}. Type 'clear' to reset."

def _assistant_dict(message) -> dict:
    d = {"role": "assistant", "content": message.content or ""}
    if message.tool_calls:
        d["tool_calls"] = [
            {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
            for tc in message.tool_calls
        ]
    return d

def _complete(client, messages, model=MODEL, **kwargs):
    global last_prompt_tokens
    response = client.chat.completions.create(model=model, messages=messages, **kwargs)
    usage = getattr(response, "usage", None)
    if usage and getattr(usage, "prompt_tokens", None):
        last_prompt_tokens = usage.prompt_tokens
    return response.choices[0].message

def compact_manifest(manifest: dict) -> str:
    """Only what the model needs: project names, paths and style. File lists come from the file tools and project memory."""
    slim = {"projects": {
        name: {k: info[k] for k in ("project_path", "primary_format", "documentation_habit", "icm_workspace") if k in info}
        for name, info in (manifest.get("projects") or {}).items()
    }}
    return yaml.dump(slim, default_flow_style=False)

def _system_messages(system_prompt: str, model: str) -> list:
    """The prompt is identical between requests, so Anthropic models can cache it (and the tool list before it)."""
    content = system_prompt
    if model.startswith("anthropic/"):
        content = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
    msgs = [{"role": "system", "content": content}]
    if session_notes:
        msgs.append({"role": "system", "content": "Earlier in this session (older turns dropped from memory):\n" + "\n".join(session_notes)})
    return msgs

def ask_orchestrator(user_prompt: str, manifest: dict):
    manifest_context = compact_manifest(manifest)
    model = pick_model(user_prompt)
    print(f"🧭 Model: {model}")

    system_prompt = f"""You are the Master Fisheries Orchestrator Agent.
You run locally on this machine and manage a suite of specialized analysis tools and an Obsidian vault context window.
Maintain formatting and stylistic habits that mirror the scientist's noted documentation habits.
Every analysis run is shown to the user for approval before it executes.

How to choose tools:
- Questions about a specific project's own results, data, outputs or scripts (e.g. "what were the results of the last model run for project X"): go straight to the project. Call get_project_context first (remembered key files, notes, recent runs). For "latest/most recent results" call get_latest_results. Use list_project_files and read_project_file for anything else, and remember_project_fact when the user says something should be remembered or a file is important. Do NOT call search_fisheries_brain for these.
- Projects with an icm_workspace are ICM workspaces: get_project_context returns their AGENTS.md and CONTEXT.md; follow them, and pass stage to load one stage contract when working on that stage. Use validate_project, refresh_project_references (report first, apply only if the user wants), create_icm_project and restructure_project when the user asks to validate, refresh, create or restructure a project. The last two are interactive: the user answers in the terminal, so just call them without asking the questions yourself.
- General fisheries science, methods, or deciding how to approach a NEW analysis: use search_fisheries_brain as a reference.
- Only use the brain alongside project files if the user asks to interpret results against the literature.
- Literature answers: no preamble or commentary between tool calls; search once, read at most 3-4 of the most relevant sources, then write the answer. Every paragraph that uses vault material must carry inline citations, using the "Inline:" form each source line gives (for example (Smith 1993)), and the answer must finish with a References list made of the full citation lines the tools gave you (without the "Inline:" part), keeping the bracketed source id in each. Never invent an author or year. A line marked "(no author recorded)" starts with the title: check the passage you read for a named author or agency and use it if present, otherwise cite by a short form of the title, e.g. (Lake Mohave Population Survey 1996); "n.d." means no year is known. Say which statements come from the vault and which are your general knowledge.
- If you cannot find the requested results, say what you looked at instead of guessing.
- This is an ongoing conversation. Follow-up questions ("the parameter estimates", "that model") refer to the project, files and results already discussed; reuse them instead of asking the user to repeat. Older tool output may be trimmed, so re-read the file if you need exact numbers. Only ask for clarification if the earlier conversation really doesn't settle it.

Here is the current scientist's machine layout and project structure configuration:
{manifest_context}"""

    turn = [{"role": "user", "content": user_prompt}]
    base = _system_messages(system_prompt, model) + [m for t in history for m in t]
    client = get_client()
    answer = None

    for _ in range(MAX_TOOL_ROUNDS):
        message = _complete(client, base + turn, model, tools=tools, tool_choice="auto")
        turn.append(_assistant_dict(message))
        if not message.tool_calls:
            answer = message.content
            break
        for tool_call in message.tool_calls:
            output = execute_tool_call(tool_call.function.name, tool_call.function.arguments)
            turn.append({"tool_call_id": tool_call.id, "role": "tool", "name": tool_call.function.name, "content": output})

    if answer is None:
        message = _complete(client, base + turn, model)
        turn.append({"role": "assistant", "content": message.content or ""})
        answer = message.content

    history.append(turn)
    trim_history()
    return answer

HELP_TEXT = """Commands at this prompt:
  help      show this list
  clear     reset conversation memory
  ingest    review PDFs waiting in 00_Fisheries_Brain/pdfs_to_process (checked every minute)
  exit      quit

Maintenance (run in a separate terminal from this folder):
  python -m utils.brain_index "razorback sucker"        try a brain search without the agent
  python -m utils.brain_enrich                          rebuild source titles and species aliases (local)
  python -m utils.brain_enrich titles-llm --limit 20    LLM titles for untitled sources (asks first)
  python -m utils.brain_index rebuild                   force a full brain index rebuild
Edit brain_meta/aliases.yaml to fix species name aliases."""

if __name__ == "__main__":
    manifest = load_manifest()
    if not manifest:
        print("❌ Cannot start orchestrator without a valid project_manifest.yaml file.")
        exit(1)

    print("\n⚓ Master Fisheries Orchestrator Core Fully Loaded & Online ⚓")
    print("-----------------------------------------------------------------")
    print(HELP_TEXT)
    print("-----------------------------------------------------------------")

    # Checks pdfs_to_process/ once a minute; PDFs are only added after the user confirms the cost estimate.
    pdf_watcher = pdf_ingest.PdfWatcher(interval=60)
    pdf_watcher.start()

    while True:
        try:
            cmd = input("\n🐟 Master Command: ")
            if cmd.lower() == 'exit':
                break
            if cmd.strip().lower() in ('ingest', '/ingest') or pdf_watcher.pending():
                pdf_watcher.offer(manual=cmd.strip().lower() in ('ingest', '/ingest'))
                if cmd.strip().lower() in ('ingest', '/ingest', ''):
                    continue
            if cmd.strip().lower() in ('help', '/help', '?'):
                print(HELP_TEXT)
                continue
            if cmd.strip().lower() in ('clear', '/clear'):
                clear_history()
                print("🧹 Conversation memory cleared.")
                continue
            if not cmd.strip():
                continue
            print(f"\n🤖 Agent Response:\n{ask_orchestrator(cmd, manifest)}")
            print(f"\n{context_status()}")
        except KeyboardInterrupt:
            break
        except RuntimeError as e:
            print(f"❌ {e}")
        except OpenAIError as e:
            print(f"❌ OpenRouter request failed: {e}\n   If the model was not found, set OPENROUTER_MODEL in .env (see openrouter.ai/models).")
