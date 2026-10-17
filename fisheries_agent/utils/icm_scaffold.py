"""Writes ICM workspaces from the fixed stage trees in icm_templates/project_types.yaml.

The tree (stages, folders, contracts) is deterministic. Project-specific routing text and skills are supplied by
the caller (LLM-written); a plain fallback routing section is generated when none is given.
Never overwrites an existing folder.
"""
import hashlib
import re
from pathlib import Path

import yaml

from utils import icm_git

HERE = Path(__file__).resolve().parent.parent
TYPES_PATH = HERE / "icm_templates" / "project_types.yaml"
PROFILE_PATH = HERE / "brain_meta" / "user_profile.md"
SUFFIX = "_icm"
MAX_NAME = 40
PROFILE_BEGIN = "<!-- BEGIN USER PROFILE sha256={sha} -->"
PROFILE_END = "<!-- END USER PROFILE -->"
ROUTING_BEGIN = "<!-- BEGIN PROJECT ROUTING -->"
ROUTING_END = "<!-- END PROJECT ROUTING -->"
PROFILE_PLACEHOLDER = "_No user profile has been recorded yet. Add one at brain_meta/user_profile.md and run a refresh._"


def load_types() -> dict:
    return yaml.safe_load(TYPES_PATH.read_text(encoding="utf-8"))


def suggest_type(text: str) -> list:
    """Project types ranked by how many of their suggest_if keywords appear in the text."""
    low = text.lower()
    scored = [(sum(k in low for k in t.get("suggest_if", [])), key) for key, t in load_types().items()]
    return [k for n, k in sorted(scored, key=lambda x: (-x[0], x[1])) if n]


def folder_name(project_name: str, existing_folder: str = None) -> str:
    """Restructured projects keep the original folder name; new ones get a sanitized, shortened name."""
    if existing_folder:
        return existing_folder + SUFFIX
    words = re.sub(r"[^A-Za-z0-9]+", " ", project_name).split()
    name = ""
    for w in words:
        nxt = (name + "_" + w) if name else w
        if len(nxt) > MAX_NAME:
            break
        name = nxt
    return (name or "Project") + SUFFIX


def profile_block(text: str = None) -> str:
    if text is None:
        text = PROFILE_PATH.read_text(encoding="utf-8").strip() if PROFILE_PATH.is_file() else PROFILE_PLACEHOLDER
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    return f"{PROFILE_BEGIN.format(sha=sha)}\n{text}\n{PROFILE_END}"


def _row(cells) -> str:
    return "| " + " | ".join(str(c) for c in cells) + " |"


def _table(header, rows) -> str:
    return "\n".join([_row(header), _row(["---"] * len(header))] + [_row(r) for r in rows])


def stage_context(stage: dict) -> str:
    parts = [f"# {stage['title']}", "", stage["purpose"], ""]
    parts += ["## Inputs", "", _table(["Source", "File/Location", "Section/Scope", "Why"], stage.get("inputs") or [["None", "-", "-", "Starting stage"]]), ""]
    parts += ["## Process", ""] + [f"{i}. {s}" for i, s in enumerate(stage["process"], 1)] + [""]
    if stage.get("checkpoint"):
        parts += ["## Checkpoints", "", _table(["After Step", "Agent Presents", "Human Decides"], [stage["checkpoint"]]), ""]
    if stage.get("audit"):
        parts += ["## Audit", "", _table(["Check", "Pass Condition"], stage["audit"]), ""]
    parts += ["## Outputs", "", _table(["Artifact", "Location", "Format"], stage["outputs"]), ""]
    return "\n".join(parts)


def root_context(name: str, ptype: dict) -> str:
    rows = [[s["title"], f"`stages/{s['slug']}/CONTEXT.md`", s["purpose"]] for s in ptype["stages"]]
    return (f"# {name}\n\n{ptype['title']}.\n\n## Task Routing\n\n"
            + _table(["Task Type", "Go To", "Description"], rows)
            + "\n\n## Shared Resources\n\n"
            + _table(["Resource", "Location", "Contains"], [
                ["Sources", "`shared/sources.md`", "Canonical bibliography for this project"],
                ["Data", "`data/manifest.yaml`", "Large and linked files (not versioned); never load these as context"],
                ["Skills", "`skills/`", "Project skills, each with its own references"],
            ]) + "\n")


def default_routing(name: str, ptype: dict) -> str:
    lines = [f"## Project: {name}", "", f"Type: {ptype['title']}.", "",
             "Read `CONTEXT.md` first, then only the stage `CONTEXT.md` for the current task. Each stage reads the previous stage's `output/` folder; edited outputs are used as left by the user. Plan, get approval, then run. Large data lives in `data/` and is referenced through `data/manifest.yaml`, never loaded into context.", ""]
    return "\n".join(lines)


def agents_md(name: str, ptype: dict, routing: str = None, profile: str = None) -> str:
    routing = (routing or default_routing(name, ptype)).strip()
    return (f"# AGENTS.md: {name}\n\n## How I work\n\n{profile_block(profile)}\n\n"
            f"{ROUTING_BEGIN}\n{routing}\n{ROUTING_END}\n")


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def scaffold(projects_root, folder: str, project_name: str, type_key: str, answers: dict = None,
             git_cfg: dict = None, routing: str = None, profile: str = None, legacy: dict = None) -> Path:
    """Creates the workspace under projects_root/folder. Raises FileExistsError rather than overwrite."""
    types = load_types()
    if type_key not in types:
        raise ValueError(f"Unknown project type '{type_key}'. Choose from: {', '.join(types)}")
    ptype = types[type_key]
    dest = Path(projects_root) / folder
    if dest.exists():
        raise FileExistsError(f"{dest} already exists; choose another name or remove it first.")
    dest.mkdir(parents=True)

    _write(dest / "AGENTS.md", agents_md(project_name, ptype, routing, profile))
    _write(dest / "CONTEXT.md", root_context(project_name, ptype))
    _write(dest / "_config" / "project.yaml", yaml.safe_dump({
        "name": project_name, "type": type_key, "folder": folder,
        "answers": answers or {}, "git": git_cfg or icm_git.settings(False),
        **({"legacy": legacy} if legacy else {})}, sort_keys=False))
    for s in ptype["stages"]:
        base = dest / "stages" / s["slug"]
        _write(base / "CONTEXT.md", stage_context(s))
        _write(base / "references" / ".gitkeep", "")
        _write(base / "output" / ".gitkeep", "")
    for skill in ptype.get("skills", []):
        _write(dest / "skills" / skill / "SKILL.md", f"---\nname: {skill}\nstatus: not generated\n---\n\n# {skill}\n\nNot generated yet.\n")
        _write(dest / "skills" / skill / "references" / ".gitkeep", "")
    _write(dest / "shared" / "sources.md", "# Sources\n\nCanonical bibliography. Cite as [[source_id]] and give the full citation from this table.\n\n| Source id | Citation | Used in |\n| --- | --- | --- |\n\n## External references (not in the brain)\n\n")
    _write(dest / "data" / "raw" / ".gitkeep", "")
    _write(dest / "data" / "models" / ".gitkeep", "")
    _write(dest / "data" / "manifest.yaml", "files: []\n")
    _write(dest / "data" / "README.md", "# Data\n\nLarge inputs and model objects live here and are not versioned. Record where each file came from below.\n\n")
    if git_cfg and git_cfg.get("enabled"):
        icm_git.init_repo(dest, git_cfg)
    return dest
