"""Project pipelines: an ordered list of R steps declared in <project>/pipeline.yaml, rerun only when their inputs change.

    python -m utils.pipeline check <project_dir>             # which steps are stale and why (read-only)
    python -m utils.pipeline run <project_dir> [--refresh]   # runs stale steps now; --refresh also runs the refresh step(s)
    python -m utils.pipeline schedule <project_dir>          # prints a weekly Task Scheduler / cron line; installs nothing

pipeline.yaml:
    steps:
      - id: refresh-data          # optional; the user's own download/refresh script (.R, .Rmd, .qmd or .py). Runs only with --refresh.
        kind: refresh
        script: scripts/download_data.R
      - id: clean
        script: scripts/01_clean.R          # .R, .Rmd or .qmd
        inputs: [data/raw/*.csv]            # globs relative to the project; a changed file (by content hash) makes the step stale
        outputs: [data/clean/catch.csv]     # a missing output also makes the step stale
      - id: report
        script: report.qmd
        inputs: [data/clean/catch.csv]
        outputs: [report.html]

A step is stale when it never ran, its script or any input changed (content hash; file size and mtime only avoid rehashing),
or an output is missing. Steps run in order, so an upstream step that rewrites a file triggers the steps that read it, and one that
rewrites identical bytes does not. A failed step stops the chain; later steps keep their old state. The framework stores no
credentials: downloading data is the user's own script. State lives in project_memory/<folder>-<hash>.pipeline.json (local, gitignored, keyed by the project folder).
"""
import hashlib
import json
import shlex
import shutil
import sys
from datetime import datetime
from pathlib import Path

import yaml

from utils import project_memory
from utils.runner import find_rscript, new_run_dir, run_command

PIPELINE_FILE = "pipeline.yaml"
MAX_STEPS = 30
MAX_FILES_PER_STEP = 500
SCRIPT_SUFFIXES = {".r", ".rmd", ".qmd"}
REFRESH_SUFFIXES = SCRIPT_SUFFIXES | {".py"}
_ID_OK = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")


def state_path(root: Path) -> Path:
    """Keyed by the project folder, so the agent and a scheduled run share one state."""
    root = Path(root).resolve()
    return project_memory.MEMORY_DIR / f"{project_memory._safe_name(root.name)}-{hashlib.sha1(str(root).encode()).hexdigest()[:8]}.pipeline.json"


def _within(root: Path, rel: str) -> bool:
    p = Path(rel)
    return bool(rel) and not p.is_absolute() and ".." not in p.parts and not rel.startswith(("~", "\\"))


def load(root: Path) -> list:
    """Reads and validates pipeline.yaml; returns the step list. Raises ValueError with a readable message."""
    path = Path(root) / PIPELINE_FILE
    if not path.is_file():
        raise ValueError(f"No {PIPELINE_FILE} in {root}.")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"{PIPELINE_FILE} is not valid YAML: {e}")
    return validate(root, data.get("steps"))


def validate(root: Path, steps) -> list:
    root = Path(root)
    if not isinstance(steps, list) or not steps:
        raise ValueError("pipeline needs a non-empty 'steps' list.")
    if len(steps) > MAX_STEPS:
        raise ValueError(f"pipeline has more than {MAX_STEPS} steps.")
    seen, clean = set(), []
    for i, s in enumerate(steps, 1):
        if not isinstance(s, dict):
            raise ValueError(f"step {i} must be a mapping.")
        sid, script, kind = str(s.get("id", "")), str(s.get("script", "")), str(s.get("kind", "run"))
        if not sid or set(sid) - _ID_OK:
            raise ValueError(f"step {i}: 'id' must use letters, digits, '-' and '_'.")
        if sid in seen:
            raise ValueError(f"duplicate step id '{sid}'.")
        seen.add(sid)
        if kind not in ("run", "refresh"):
            raise ValueError(f"{sid}: kind must be 'run' or 'refresh'.")
        allowed = REFRESH_SUFFIXES if kind == "refresh" else SCRIPT_SUFFIXES
        if not _within(root, script) or Path(script).suffix.lower() not in allowed:
            raise ValueError(f"{sid}: script must be a project-relative {', '.join(sorted(allowed))} path.")
        if not (root / script).is_file():
            raise ValueError(f"{sid}: script '{script}' does not exist.")
        lists = {}
        for key in ("inputs", "outputs"):
            vals = s.get(key) or []
            if not isinstance(vals, list) or not all(isinstance(v, str) and _within(root, v) for v in vals):
                raise ValueError(f"{sid}: '{key}' must be a list of project-relative paths or globs (no '..', no absolute paths).")
            lists[key] = vals
        clean.append({"id": sid, "kind": kind, "script": script, **lists})
    return clean


def _expand(root: Path, patterns: list) -> list:
    out = set()
    for pat in patterns:
        if any(c in pat for c in "*?["):
            matches = (p for p in root.glob(pat) if p.is_file())
        else:
            matches = [root / pat] if (root / pat).is_file() else []
        for p in matches:
            if p.resolve().is_relative_to(root.resolve()):
                out.add(p.relative_to(root).as_posix())
        if len(out) > MAX_FILES_PER_STEP:
            raise ValueError(f"inputs expand to more than {MAX_FILES_PER_STEP} files; narrow the patterns.")
    return sorted(out)


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _fingerprint(root: Path, rel: str, prior: dict) -> dict:
    """{'m': mtime_ns, 's': size, 'h': sha256}. Rehashes only when size or mtime differ from the prior record."""
    st = (root / rel).stat()
    old = prior.get(rel)
    if old and old.get("m") == st.st_mtime_ns and old.get("s") == st.st_size:
        return old
    return {"m": st.st_mtime_ns, "s": st.st_size, "h": _sha(root / rel)}


def _load_state(root: Path) -> dict:
    p = state_path(root)
    try:
        return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}
    except (OSError, ValueError):
        return {}


def _save_state(root: Path, state: dict) -> None:
    p = state_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(state, indent=1), encoding="utf-8")


def _snapshot(root: Path, step: dict, prior: dict) -> dict:
    files = _expand(root, step["inputs"]) + [step["script"]]
    return {rel: _fingerprint(root, rel, prior) for rel in files}


def stale_reason(root: Path, step: dict, state: dict) -> str:
    """'' when the step is up to date, otherwise a short reason."""
    rec = state.get(step["id"])
    if not rec:
        return "never run"
    prior = rec.get("files", {})
    now = _snapshot(root, step, prior)
    if rec.get("ok") is False:
        return "last run failed"
    if now[step["script"]]["h"] != prior.get(step["script"], {}).get("h"):
        return "script changed"
    new = [r for r in now if r != step["script"] and r not in prior]
    gone = [r for r in prior if r not in now]
    changed = [r for r in now if r in prior and r != step["script"] and now[r]["h"] != prior[r]["h"]]
    if changed or new or gone:
        names = (changed + new + gone)[:3]
        return "input changed: " + ", ".join(names) + (" ..." if len(changed + new + gone) > 3 else "")
    missing = [o for o in step["outputs"] if not _expand(root, [o])]
    if missing:
        return "output missing: " + ", ".join(missing[:3])
    return ""


def check(root: Path, project: str) -> list:
    """Read-only. Returns [{'id', 'kind', 'stale', 'reason'}] for every step. Refresh steps are reported but never counted as stale."""
    root = Path(root)
    state = _load_state(root)
    out = []
    for s in load(root):
        reason = "" if s["kind"] == "refresh" else stale_reason(root, s, state)
        out.append({"id": s["id"], "kind": s["kind"], "stale": bool(reason), "reason": reason or ("on request only" if s["kind"] == "refresh" else "up to date")})
    return out


def summary(root: Path, project: str) -> str:
    """One short block for get_project_context; empty when the project has no pipeline."""
    if not (Path(root) / PIPELINE_FILE).is_file():
        return ""
    try:
        rows = check(root, project)
    except ValueError as e:
        return f"Pipeline: {PIPELINE_FILE} has a problem: {e}"
    stale = [r for r in rows if r["stale"]]
    refresh = [r["id"] for r in rows if r["kind"] == "refresh"]
    head = (f"Pipeline: {len(stale)} of {len(rows)} step(s) out of date; offer run_pipeline." if stale
            else f"Pipeline: all {len(rows)} step(s) up to date.")
    lines = [head] + [f"- {r['id']}: {r['reason']}" for r in stale]
    if refresh:
        lines.append(f"Data refresh step(s): {', '.join(refresh)} (run only if the user asks: run_pipeline with include_refresh).")
    return "\n".join(lines)


def script_command(target: Path):
    """Command list for a project script, or (None, error)."""
    suffix = target.suffix.lower()
    if suffix == ".py":
        return [sys.executable, str(target)], ""
    if suffix in (".r", ".rmd"):
        rscript = find_rscript()
        if not rscript:
            return None, "Rscript was not found."
        if suffix == ".r":
            return [rscript, "--vanilla", str(target)], ""
        return [rscript, "--vanilla", "-e", "rmarkdown::render(commandArgs(TRUE)[1])", str(target)], ""
    if suffix == ".qmd":
        quarto = shutil.which("quarto")
        return ([quarto, "render", str(target)], "") if quarto else (None, "Quarto was not found on PATH.")
    return None, f"Cannot run '{target.suffix}' files."


def run(root: Path, project: str, include_refresh: bool = False, log=print) -> dict:
    """Runs the stale steps in order (all steps when include_refresh and a refresh step exists run first). Returns
    {'ran': [ids], 'skipped': [ids], 'failed': id or '', 'run_dir': Path, 'outputs': [...]}."""
    root = Path(root)
    steps = load(root)
    state = _load_state(root)
    run_dir = new_run_dir(f"pipeline_{project}")
    result = {"ran": [], "skipped": [], "failed": "", "run_dir": run_dir, "messages": []}
    for s in steps:
        if s["kind"] == "refresh":
            if not include_refresh:
                continue
            reason = "refresh requested"
        else:
            reason = stale_reason(root, s, state)
            if not reason:
                result["skipped"].append(s["id"])
                continue
        cmd, err = script_command(root / s["script"])
        if err:
            result["failed"] = s["id"]
            result["messages"].append(f"{s['id']}: {err}")
            break
        log(f"  running {s['id']} ({reason})")
        ok, out = run_command(cmd, cwd=root, log_dir=None)
        (run_dir / f"{s['id']}.log").write_text(f"command: {' '.join(map(str, cmd))}\nok: {ok}\n\n{out}", encoding="utf-8")
        prior = state.get(s["id"], {}).get("files", {})
        if not ok:
            state[s["id"]] = {"ok": False, "when": datetime.now().isoformat(timespec="seconds"), "files": prior}
            _save_state(root, state)
            result["failed"] = s["id"]
            result["messages"].append(f"{s['id']} failed:\n{out[-1500:]}")
            break
        state[s["id"]] = {"ok": True, "when": datetime.now().isoformat(timespec="seconds"), "files": _snapshot(root, s, prior)}
        _save_state(root, state)
        result["ran"].append(s["id"])
    result["outputs"] = sorted({o for s in steps if s["id"] in result["ran"] for o in _expand(root, s["outputs"])})
    return result


def schedule_text(root: Path, project: str) -> str:
    py, base = sys.executable, Path(__file__).resolve().parent.parent
    cmd = f'"{py}" -m utils.pipeline run "{root}"'
    win = f'schtasks /Create /SC WEEKLY /D MON /ST 06:00 /TN "FisheriesPipeline-{project}" /TR "cmd /c cd /d {base} && {cmd}"'
    nix = f"0 6 * * 1 cd {shlex.quote(str(base))} && {py} -m utils.pipeline run {shlex.quote(str(root))} >> pipeline_cron.log 2>&1"
    return ("Nothing was installed. To run this project's pipeline every Monday at 06:00, run one of:\n"
            f"Windows (Command Prompt):\n  {win}\nLinux/macOS (add with `crontab -e`):\n  {nix}\n"
            "A scheduled run reruns only out-of-date steps and never runs the refresh step unless you add --refresh to the command.")


def _project_name(root: Path) -> str:
    return Path(root).resolve().name


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2 or argv[0] not in ("check", "run", "schedule"):
        print(__doc__)
        return 2
    cmd, root = argv[0], Path(argv[1]).resolve()
    name = _project_name(root)
    try:
        if cmd == "check":
            rows = check(root, name)
            print("\n".join(f"{'STALE' if r['stale'] else 'ok   '} {r['id']}: {r['reason']}" for r in rows))
        elif cmd == "schedule":
            print(schedule_text(root, name))
        else:
            res = run(root, name, include_refresh="--refresh" in argv)
            print(f"ran: {', '.join(res['ran']) or 'none'}; up to date: {', '.join(res['skipped']) or 'none'}; logs: {res['run_dir']}")
            for m in res["messages"]:
                print(m)
            return 1 if res["failed"] else 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
