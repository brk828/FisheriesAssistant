"""Long-term, per-project memory kept in project_memory/<project>.yaml.

Memory is only a hint: every path is re-checked against the project folder and its
modification time before use. Nothing here calls an LLM or the network.
"""
import os
import re
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

import yaml

MEMORY_DIR = Path(__file__).resolve().parent.parent / "project_memory"
READABLE_SUFFIXES = {".txt", ".md", ".csv", ".tsv", ".log", ".r", ".rmd", ".qmd", ".json", ".yaml", ".yml", ".out", ".html"}
MAX_KEY_FILES = 40
MAX_RUNS = 20
MAX_NOTES = 30
MAX_NOTE_CHARS = 200
SUMMARY_CHARS = 300
MAX_SCAN_FILES = 20000

RESULT_DIRS = {"results", "result", "output", "outputs", "runs", "models", "model_output", "figures", "tables"}
RESULT_NAME = re.compile(r"summary|result|model|output|estimate|diagnos|aic|fit", re.I)
DATA_DIRS = {"data", "raw", "raw_data", "inputs", "input"}


def _safe_name(project: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", project)[:80] or "project"


def _path(project: str) -> Path:
    return MEMORY_DIR / f"{_safe_name(project)}.yaml"


def _blank(project: str) -> dict:
    return {"project": project, "updated": "", "notes": [], "key_files": [], "runs": []}


def load(project: str) -> dict:
    path = _path(project)
    if not path.is_file():
        return _blank(project)
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            raise ValueError("not a mapping")
    except (yaml.YAMLError, ValueError, OSError):
        try:
            path.replace(path.with_suffix(".bak"))
        except OSError:
            pass
        return _blank(project)
    base = _blank(project)
    for key, default in base.items():
        if isinstance(data.get(key), type(default)):
            base[key] = data[key]
    return base


def save(project: str, data: dict) -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    data["updated"] = datetime.now().strftime("%Y-%m-%dT%H:%M")
    fd, tmp = tempfile.mkstemp(dir=MEMORY_DIR, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100)
        os.replace(tmp, _path(project))
    except OSError:
        if os.path.exists(tmp):
            os.remove(tmp)


def classify(rel: str) -> str:
    p = Path(rel)
    parts = {x.lower() for x in p.parts[:-1]}
    suffix = p.suffix.lower()
    if suffix in {".r", ".rmd", ".qmd"}:
        return "script"
    if parts & RESULT_DIRS or (RESULT_NAME.search(p.stem) and suffix in READABLE_SUFFIXES):
        return "results"
    if suffix in {".csv", ".tsv"} or parts & DATA_DIRS:
        return "data"
    return "other"


def scan(root: Path) -> dict:
    """Returns {relative path: mtime} for visible files in a project (capped)."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):
                continue
            full = Path(dirpath) / name
            try:
                found[full.relative_to(root).as_posix()] = full.stat().st_mtime
            except (OSError, ValueError):
                continue
            if len(found) >= MAX_SCAN_FILES:
                return found
    return found


def _excerpt(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()[:SUMMARY_CHARS]


def _entry(data: dict, rel: str):
    for e in data["key_files"]:
        if isinstance(e, dict) and e.get("path") == rel:
            return e
    return None


def _prune(data: dict, root: Path) -> None:
    kept = []
    for e in data["key_files"]:
        if isinstance(e, dict) and e.get("path") and (root / e["path"]).is_file():
            kept.append(e)
    kept.sort(key=lambda e: (bool(e.get("pinned")), e.get("hits", 0), e.get("last_used", 0)), reverse=True)
    data["key_files"] = kept[:MAX_KEY_FILES]
    data["runs"] = data["runs"][-MAX_RUNS:]


def record_file(project: str, root: Path, rel: str, text: str = "", pin: bool = None) -> None:
    """Notes that a file was read or requested; refreshes its summary when text is given."""
    full = root / rel
    if not full.is_file() or full.name.startswith("."):
        return
    data = load(project)
    entry = _entry(data, rel)
    if entry is None:
        entry = {"path": rel, "role": classify(rel), "summary": "", "mtime": 0, "hits": 0, "pinned": False, "last_used": 0}
        data["key_files"].append(entry)
    entry["hits"] = int(entry.get("hits", 0)) + 1
    entry["mtime"] = int(full.stat().st_mtime)
    entry["last_used"] = int(time.time())
    if text and full.suffix.lower() in READABLE_SUFFIXES:
        entry["summary"] = _excerpt(text)
    if pin is not None:
        entry["pinned"] = bool(pin)
    _prune(data, root)
    save(project, data)


def record_run(project: str, root: Path, tool: str, ok: bool, label: str = "", run_dir=None, outputs=None) -> None:
    data = load(project)
    data["runs"].append({
        "when": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tool": tool,
        "label": label[:200],
        "ok": bool(ok),
        "run_dir": Path(run_dir).name if run_dir else "",
        "outputs": list(outputs or [])[:10],
    })
    _prune(data, root)
    save(project, data)


def add_note(project: str, root: Path, fact: str) -> str:
    fact = re.sub(r"\s+", " ", fact).strip()[:MAX_NOTE_CHARS]
    if not fact:
        return "Nothing to remember."
    data = load(project)
    if fact not in data["notes"]:
        data["notes"].append(fact)
    data["notes"] = data["notes"][-MAX_NOTES:]
    _prune(data, root)
    save(project, data)
    return f"Remembered for project '{project}': {fact}"


def context(project: str, root: Path) -> str:
    """Compact summary of what is known about a project (a few hundred tokens)."""
    data = load(project)
    _prune(data, root)
    lines = [f"Project memory for '{project}' (updated {data['updated'] or 'never'}):"]
    if data["notes"]:
        lines.append("Notes:")
        lines += [f"- {n}" for n in data["notes"]]
    if data["key_files"]:
        lines.append("Key files (pinned/most used first):")
        for e in data["key_files"][:10]:
            when = datetime.fromtimestamp(root.joinpath(e["path"]).stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            stale = " [changed since last read]" if int(root.joinpath(e["path"]).stat().st_mtime) != e.get("mtime") else ""
            pin = " *pinned*" if e.get("pinned") else ""
            lines.append(f"- {e['path']} ({e.get('role', 'other')}, {when}, read {e.get('hits', 0)}x){pin}{stale}"
                         + (f": {e['summary']}" if e.get("summary") else ""))
    if data["runs"]:
        lines.append("Recent runs:")
        for r in data["runs"][-3:][::-1]:
            outs = f" -> {', '.join(r['outputs'])}" if r.get("outputs") else ""
            where = f" [{r['run_dir']}]" if r.get("run_dir") else ""
            lines.append(f"- {r['when']} {r['tool']} {r.get('label', '')} {'ok' if r.get('ok') else 'FAILED'}{where}{outs}")
    if len(lines) == 1:
        lines.append("Nothing recorded yet. Use get_latest_results or list_project_files.")
    return "\n".join(lines)


def latest_candidates(project: str, root: Path, kind: str = "results") -> list:
    """Files matching kind ('results', 'script', 'data', 'any'), newest first; pinned files lead."""
    data = load(project)
    pinned = {e["path"] for e in data["key_files"] if isinstance(e, dict) and e.get("pinned")}
    files = scan(root)
    rows = []
    for rel, mtime in files.items():
        if Path(rel).suffix.lower() not in READABLE_SUFFIXES:
            continue
        if kind != "any" and classify(rel) != kind:
            continue
        rows.append((rel in pinned, mtime, rel))
    rows.sort(reverse=True)
    return [(rel, mtime) for _, mtime, rel in rows]


def latest_run_dir_output(project: str):
    """Name of the newest recorded run folder (for tools that write outside the project)."""
    for r in reversed(load(project)["runs"]):
        if r.get("run_dir"):
            return r
    return None


def _main(argv: list) -> int:
    if len(argv) >= 2 and argv[0] == "show":
        print(_path(argv[1]).read_text(encoding="utf-8") if _path(argv[1]).is_file() else "No memory yet.")
        return 0
    if len(argv) >= 2 and argv[0] == "clear":
        if _path(argv[1]).is_file():
            _path(argv[1]).unlink()
        print(f"Cleared memory for {argv[1]}.")
        return 0
    print("Usage: python -m utils.project_memory show|clear <project>")
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
