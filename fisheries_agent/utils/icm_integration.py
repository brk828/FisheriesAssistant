"""Links ICM workspaces to project_manifest.yaml and loads their context in layers for the orchestrator.

Layers: AGENTS.md and root CONTEXT.md always; one stage CONTEXT.md only when a stage is asked for.
"""
from pathlib import Path

import yaml

from utils import icm_data, icm_validate

HERE = Path(__file__).resolve().parent.parent
MANIFEST_PATH = HERE / "project_manifest.yaml"
MAX_LAYER_CHARS = 7000


def _load(path) -> dict:
    path = Path(path or MANIFEST_PATH)
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.is_file() else {}


def _save(data: dict, path) -> None:
    Path(path or MANIFEST_PATH).write_text(yaml.dump(data, default_flow_style=False), encoding="utf-8")


def is_workspace(path) -> bool:
    p = Path(path)
    return (p / "AGENTS.md").is_file() and (p / "CONTEXT.md").is_file() and (p / "stages").is_dir()


def workspace_of(info: dict):
    """The project's ICM workspace folder, or None when none is linked or the folder is gone."""
    ws = (info or {}).get("icm_workspace")
    return Path(ws) if ws and is_workspace(ws) else None


def register_workspace(workspace, original: str = None, manifest_path=None) -> str:
    """Adds the workspace as its own project and links it from the original project. Returns the new project name."""
    workspace = Path(workspace).resolve()
    data = _load(manifest_path)
    projects = data.setdefault("projects", {})
    base = projects.get(original, {}) if original else {}
    name = workspace.name
    projects[name] = {
        "project_path": str(workspace),
        "primary_format": base.get("primary_format", "Quarto (qmd)"),
        "documentation_habit": base.get("documentation_habit", "See AGENTS.md in the workspace"),
        "icm_workspace": str(workspace),
    }
    if original in projects:
        projects[original]["icm_workspace"] = str(workspace)
    _save(data, manifest_path)
    return name


def _stages(ws: Path) -> list:
    return sorted(p.name for p in (ws / "stages").glob("*") if (p / "CONTEXT.md").is_file())


def _clip(text: str) -> str:
    return text if len(text) <= MAX_LAYER_CHARS else text[:MAX_LAYER_CHARS] + "\n...[truncated]"


def layered_context(ws, stage: str = "") -> str:
    """AGENTS.md and CONTEXT.md, plus one stage's CONTEXT.md if requested, plus data and gap notices."""
    ws = Path(ws)
    parts = [f"ICM workspace: {ws}", "## AGENTS.md\n" + _clip((ws / "AGENTS.md").read_text(encoding="utf-8")),
             "## CONTEXT.md\n" + _clip((ws / "CONTEXT.md").read_text(encoding="utf-8"))]
    stages = _stages(ws)
    if stage:
        match = next((s for s in stages if s == stage or s.split("-", 1)[-1] == stage or s.startswith(stage)), None)
        if match:
            parts.append(f"## stages/{match}/CONTEXT.md\n" + _clip((ws / "stages" / match / "CONTEXT.md").read_text(encoding="utf-8")))
        else:
            parts.append(f"Stage '{stage}' not found. Stages: {', '.join(stages)}.")
    else:
        parts.append(f"Stages (ask for one with the stage argument to load its contract): {', '.join(stages)}.")
    warn = icm_data.warnings(ws)
    if warn:
        parts.append("Linked data warnings:\n" + "\n".join(f"- {w}" for w in warn))
    if (ws / "GAPS.md").is_file():
        parts.append("GAPS.md lists reference topics the Fisheries Brain could not cover.")
    return "\n\n".join(parts)


def validate_workspace(ws, full_data_check: bool = False) -> str:
    ws = Path(ws)
    issues = icm_validate.validate(ws) + icm_data.warnings(ws, full=full_data_check)
    return "\n".join(f"- {i}" for i in issues) if issues else "Workspace passes validation and linked data matches the manifest."
