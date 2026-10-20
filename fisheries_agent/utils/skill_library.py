"""Copies the prepackaged roles and skills (skill_library/) into an ICM workspace and tracks updates.

    python -m utils.skill_library install <workspace> [--overwrite]   # copy roles to .agent/roles/, skills to skills/
    python -m utils.skill_library status <workspace>                  # which copies differ from the library

Copies are snapshots with a content hash in <workspace>/.agent/_library.json. A copy the user edited locally is never
overwritten (reported instead) unless --overwrite is given; a library skill never replaces a project skill of the
same name that was not installed from the library.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

LIBRARY = Path(__file__).resolve().parent.parent / "skill_library"
RECORD = ".agent/_library.json"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def library_files() -> dict:
    """{relative destination inside a workspace: library file}."""
    files = {}
    for f in sorted((LIBRARY / "roles").glob("*.md")):
        files[f".agent/roles/{f.name}"] = f
    for f in sorted((LIBRARY / "skills").rglob("*")):
        if f.is_file() and f.name != ".gitkeep":
            files[f"skills/{f.relative_to(LIBRARY / 'skills').as_posix()}"] = f
    return files


def _front(text: str) -> dict:
    meta = {}
    if text.startswith("---"):
        for line in text.split("---", 2)[1].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def _skill_dirs(ws=None) -> dict:
    """{skill name: folder}. Library skills first, then the workspace's own copies, which win."""
    found = {d.name: d for d in sorted((LIBRARY / "skills").iterdir()) if (d / "SKILL.md").is_file()}
    if ws and (Path(ws) / "skills").is_dir():
        found.update({d.name: d for d in sorted((Path(ws) / "skills").iterdir()) if (d / "SKILL.md").is_file()})
    return found


def list_skills(ws=None) -> list:
    """[{name, description, status}] for every skill available to a project (workspace copy preferred)."""
    out = []
    for name, d in _skill_dirs(ws).items():
        meta = _front((d / "SKILL.md").read_text(encoding="utf-8"))
        out.append({"name": name, "description": meta.get("description", ""), "status": meta.get("status", "")})
    return out


def read_skill(name: str, ws=None, file: str = "SKILL.md") -> str:
    """Text of one skill file (SKILL.md, SUPPLEMENT.md, SOURCES.md or GAPS.md); a unknown name lists what exists."""
    dirs = _skill_dirs(ws)
    if name not in dirs:
        return f"Unknown skill '{name}'. Available: {', '.join(dirs)}."
    if file not in ("SKILL.md", "SUPPLEMENT.md", "SOURCES.md", "GAPS.md"):
        return "file must be SKILL.md, SUPPLEMENT.md, SOURCES.md or GAPS.md."
    f = dirs[name] / file
    return f.read_text(encoding="utf-8") if f.is_file() else f"'{file}' does not exist for skill '{name}'."


def _load(ws: Path) -> dict:
    p = ws / RECORD
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def status(ws) -> list:
    """(destination, state) for every library file: new, current, library-updated, edited-locally or untracked."""
    ws = Path(ws)
    rec, out = _load(ws), []
    for dest, src in library_files().items():
        target = ws / dest
        if not target.is_file():
            out.append((dest, "new"))
        elif dest not in rec:
            out.append((dest, "untracked"))
        elif _sha(target) != rec[dest]:
            out.append((dest, "edited-locally"))
        elif _sha(src) != rec[dest]:
            out.append((dest, "library-updated"))
        else:
            out.append((dest, "current"))
    return out


def install(ws, overwrite: bool = False) -> dict:
    ws = Path(ws)
    rec = _load(ws)
    done, kept = [], []
    for dest, state in status(ws):
        if state == "current" or (state in ("edited-locally", "untracked") and not overwrite):
            if state != "current":
                kept.append((dest, state))
            continue
        target = ws / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(library_files()[dest], target)
        rec[dest] = _sha(target)
        done.append(dest)
    (ws / RECORD).parent.mkdir(parents=True, exist_ok=True)
    (ws / RECORD).write_text(json.dumps(rec, indent=1, sort_keys=True), encoding="utf-8")
    return {"installed": done, "kept": kept}


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2 or argv[0] not in ("install", "status"):
        print(__doc__)
        return 2
    ws = Path(argv[1])
    if argv[0] == "install":
        r = install(ws, overwrite="--overwrite" in argv)
        print(f"Installed {len(r['installed'])} file(s).")
        for dest, state in r["kept"]:
            print(f"- kept {dest} ({state}); use --overwrite to replace")
    else:
        for dest, state in status(ws):
            if state != "current":
                print(f"- {dest}: {state}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
