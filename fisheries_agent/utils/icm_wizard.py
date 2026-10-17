"""Interactive flow for creating a new ICM project workspace.

Run from fisheries_agent:
    python -m utils.icm_wizard

Steps: one-time user working profile (brain_meta/user_profile.md), one flat questionnaire, a suggested project type
with its fixed folder tree for approval, git and ignore options, then the workspace is written under the projects
root from onboarding. The LLM only writes the project-specific routing text; the tree is deterministic.
"""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

from utils import icm_git, icm_scaffold

HERE = Path(__file__).resolve().parent.parent
MANIFEST_PATH = HERE / "project_manifest.yaml"
PROFILE_PATH = icm_scaffold.PROFILE_PATH

PROFILE_QUESTIONS = [
    ("tools", "Preferred tools and packages (e.g. R with Quarto, FSA, RMark, nimble)"),
    ("style", "Coding and documentation style (e.g. tidyverse, commented scripts, Quarto reports)"),
    ("units", "Naming, units and conventions you always use"),
    ("citations", "Citation style (e.g. AFS, APA, source id plus year)"),
    ("workflow", "How you like to work with the agent (e.g. plan, approve, then run; ask before installing packages)"),
]

PROJECT_QUESTIONS = [
    ("goal", "One sentence: what is this project for?"),
    ("species", "Target species and region"),
    ("data", "Data you have or expect (types, sources, rough size)"),
    ("analyses", "Analyses wanted (e.g. mark-recapture, CPUE, growth, occupancy)"),
    ("deliverables", "Deliverables (e.g. report, manuscript, dashboard)"),
]


def projects_root() -> Path:
    """Projects root collected during onboarding."""
    if MANIFEST_PATH.is_file():
        root = ((yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}).get("global_settings") or {}).get("r_projects_root")
        if root:
            return Path(root)
    raise RuntimeError("No projects root found. Run setup_onboarding.py first.")


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    return input(f"{prompt}{suffix}: ").strip() or default


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    ans = input(f"{prompt} ({'Y/n' if default else 'y/N'}): ").strip().lower()
    return default if not ans else ans.startswith("y")


def collect_profile() -> str:
    """Asks the profile questions once and stores them as the canonical profile text."""
    print("\nI have not recorded how you work yet. These answers go into every project's AGENTS.md (Enter to skip any).")
    lines = []
    for key, q in PROFILE_QUESTIONS:
        ans = ask(q)
        if ans:
            lines.append(f"- **{key.capitalize()}:** {ans}")
    text = "\n".join(lines)
    if text:
        PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        PROFILE_PATH.write_text(text + "\n", encoding="utf-8")
    return text


def make_llm():
    """Returns llm(prompt) -> str using OpenRouter, or None when no key is configured."""
    load_dotenv(HERE / ".env")
    key = os.getenv("OPENROUTER_API_KEY")
    if not key or key.startswith("your_"):
        return None
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
    model = os.getenv("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.5")

    def llm(prompt: str) -> str:
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
        return (r.choices[0].message.content or "").strip()
    return llm


def routing_prompt(name: str, ptype: dict, answers: dict) -> str:
    stages = "\n".join(f"- {s['slug']}: {s['purpose']}" for s in ptype["stages"])
    facts = "\n".join(f"- {k}: {v}" for k, v in answers.items() if v)
    return (
        "Write the project-specific routing section of an AGENTS.md file for a fisheries research project. "
        "Markdown, under 250 words, starting with a '## Project' heading. Say what the project is, which stage handles "
        "which kind of request (use only the stage folders listed), where large data lives (data/, referenced through "
        "data/manifest.yaml, never loaded as context), and any constraints implied by the answers. Do not describe the "
        "user's general working style (a separate section covers it). Do not invent facts beyond the answers.\n\n"
        f"Project name: {name}\nType: {ptype['title']}\nStages:\n{stages}\nAnswers:\n{facts}\n")


def write_routing(llm, name: str, ptype: dict, answers: dict):
    """LLM-written routing text, or None (the scaffold falls back to its plain default)."""
    if llm is None:
        return None
    try:
        text = llm(routing_prompt(name, ptype, answers))
    except Exception as e:
        print(f"Could not generate routing text ({e}); using the default.")
        return None
    return text or None


def ask_git() -> dict:
    if not ask_yes_no("Should this project be a git repository?"):
        return icm_git.settings(False)
    print(f"Large files stay out of git. Default ignored types: {', '.join(icm_git.DEFAULT_IGNORE_TYPES)}; folders: {', '.join(icm_git.DEFAULT_IGNORE_PATHS)}.")
    extra_types = [t.strip() for t in ask("Other file types to ignore (comma-separated, e.g. *.tif)").split(",") if t.strip()]
    extra_paths = [t.strip() for t in ask("Other folders or files to ignore (comma-separated)").split(",") if t.strip()]
    mb = ask("Ignore any file larger than how many MB?", str(icm_git.DEFAULT_MAX_FILE_MB))
    try:
        mb = float(mb)
    except ValueError:
        mb = icm_git.DEFAULT_MAX_FILE_MB
    return icm_git.settings(True, icm_git.DEFAULT_IGNORE_TYPES + extra_types, icm_git.DEFAULT_IGNORE_PATHS + extra_paths, mb)


def choose_type(answers: dict) -> str:
    types = icm_scaffold.load_types()
    ranked = icm_scaffold.suggest_type(" ".join(str(v) for v in answers.values())) or []
    ordered = ranked + [k for k in types if k not in ranked]
    print("\nSuggested project type" + (" (best match first):" if ranked else " (no strong match; pick one):"))
    for i, k in enumerate(ordered, 1):
        print(f"  {i}. {types[k]['title']} ({k})" + ("  <- suggested" if ranked and i == 1 else ""))
    pick = ask("Choose a number", "1")
    try:
        return ordered[int(pick) - 1]
    except (ValueError, IndexError):
        return ordered[0]


def show_tree(type_key: str, folder: str) -> None:
    ptype = icm_scaffold.load_types()[type_key]
    print(f"\n{folder}/\n  AGENTS.md\n  CONTEXT.md\n  _config/\n  stages/")
    for s in ptype["stages"]:
        print(f"    {s['slug']}/   {s['purpose']}")
    print("  skills/ shared/ data/ (not versioned)")


def run(llm=None, root: Path = None) -> Path:
    root = root or projects_root()
    if not PROFILE_PATH.is_file() or not PROFILE_PATH.read_text(encoding="utf-8").strip():
        collect_profile()
    print("\n--- New ICM project ---")
    name = ask("Project name")
    if not name:
        raise SystemExit("A project name is required.")
    answers = {k: ask(q) for k, q in PROJECT_QUESTIONS}
    type_key = choose_type({"name": name, **answers})
    folder = icm_scaffold.folder_name(name)
    folder = ask("Folder name", folder)
    if not folder.endswith(icm_scaffold.SUFFIX):
        folder += icm_scaffold.SUFFIX
    show_tree(type_key, folder)
    git_cfg = ask_git()
    if not ask_yes_no(f"\nCreate {root / folder}?", True):
        raise SystemExit("Cancelled; nothing was written.")
    ptype = icm_scaffold.load_types()[type_key]
    routing = write_routing(llm if llm is not None else make_llm(), name, ptype, answers)
    dest = icm_scaffold.scaffold(root, folder, name, type_key, answers, git_cfg, routing)
    print(f"Created {dest}")
    if git_cfg["enabled"]:
        print("Git repository initialized; large files and data/ are ignored.")
    return dest


if __name__ == "__main__":
    run()
