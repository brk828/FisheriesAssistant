"""Read-only maintenance report for the ICM side of the framework.

    python -m utils.icm_maintain              # every workspace in project_manifest.yaml
    python -m utils.icm_maintain --upstream   # also ask upstream whether the vendored ICM core is behind

For each linked workspace: copied brain notes that changed or disappeared, new brain sources that match a stage
topic, and skills (status: draft) built on notes that changed. Nothing is written; apply with
`python -m utils.icm_seed refresh|seed <workspace>` and regenerate skills with `python -m utils.icm_skills`.
"""
import sys
from pathlib import Path

from utils import icm_integration, icm_seed, icm_update, skill_library


def check_workspace(ws) -> dict:
    ws = Path(ws)
    changed = icm_seed.refresh(ws)
    stale = sorted({Path(folder).parts[1] for folder, _sid, _st in changed if folder.startswith("skills/")})
    return {"changed": changed, "new": icm_seed.new_matches(ws), "stale_skills": stale,
            "library": [(d, st) for d, st in skill_library.status(ws) if st in ("new", "library-updated", "edited-locally")]}


def report(manifest_path=None, upstream: bool = False) -> str:
    projects = (icm_integration._load(manifest_path).get("projects") or {})
    seen, lines = set(), []
    for name, info in projects.items():
        ws = icm_integration.workspace_of(info)
        if not ws or ws in seen:
            continue
        seen.add(ws)
        r = check_workspace(ws)
        lines.append(f"{name}: {len(r['changed'])} changed/missing note(s), {len(r['new'])} new brain match(es)")
        lines += [f"  - {f}: {sid} {st}" for f, sid, st in r["changed"]]
        lines += [f"  - new for {stage} / {topic}: {sid}" for stage, topic, sid, _t in r["new"]]
        lines += [f"  - skill library {d}: {st} (python -m utils.skill_library install <workspace>)" for d, st in r["library"]]
        if r["stale_skills"]:
            lines.append("  - skills built on changed notes (regenerate unless status: reviewed): " + ", ".join(r["stale_skills"]))
    if not seen:
        lines.append("No ICM workspaces are linked in the manifest.")
    if upstream:
        lines.append("ICM core: " + {"current": "up to date with upstream.", "behind": "upstream has newer commits (python -m utils.icm_update).",
                                      "unknown": "could not reach upstream."}[icm_update.upstream_status()])
    return "\n".join(lines)


if __name__ == "__main__":
    print(report(upstream="--upstream" in sys.argv[1:]))
    sys.exit(0)
