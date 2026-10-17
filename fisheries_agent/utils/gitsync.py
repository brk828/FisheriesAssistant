"""Commits agent-made changes in git-backed projects and offers a pull/push sync."""
import os
import re
import shutil
import subprocess
from pathlib import Path

GIT_TIMEOUT = 120
# Never auto-stage files that commonly hold secrets.
_SECRET_PATTERN = re.compile(r"(^|/)(\.env[^/]*|.*\.(pem|key)|\.Renviron|\.Rprofile|id_rsa[^/]*)$", re.IGNORECASE)


def _git(root: Path, *args: str) -> tuple:
    git = shutil.which("git")
    if not git:
        return False, "git was not found on PATH."
    env = {k: v for k, v in os.environ.items() if not k.upper().startswith("OPENROUTER_")}
    env["GIT_TERMINAL_PROMPT"] = "0"
    try:
        r = subprocess.run(
            [git, "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=GIT_TIMEOUT, env=env,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except (subprocess.TimeoutExpired, OSError) as e:
        return False, f"git failed: {e}"
    return r.returncode == 0, ((r.stdout or "") + (r.stderr or "")).strip()


def is_git_project(root: Path) -> bool:
    """True only if the project folder is itself the top level of a git repo."""
    ok, out = _git(root, "rev-parse", "--show-toplevel")
    return ok and Path(out.splitlines()[0]).resolve() == Path(root).resolve()


def snapshot(root: Path) -> dict:
    """Maps each dirty/untracked path to (status, mtime_ns, size) so later changes can be told apart."""
    ok, out = _git(root, "status", "--porcelain", "-uall")
    state = {}
    if not ok:
        return state
    for line in out.splitlines():
        status, path = line[:2], line[3:].strip().strip('"')
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        try:
            st = (Path(root) / path).stat()
            state[path] = (status, st.st_mtime_ns, st.st_size)
        except OSError:
            state[path] = (status, None, None)
    return state


def _max_file_bytes(root: Path):
    """Size cap from an ICM workspace's _config/project.yaml (git.max_file_mb), or None for other projects."""
    cfg = Path(root) / "_config" / "project.yaml"
    if not cfg.is_file():
        return None
    try:
        import yaml
        mb = ((yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}).get("git") or {}).get("max_file_mb")
        return float(mb) * 1024 * 1024 if mb else None
    except Exception:
        return None


def commit_changes(root: Path, before: dict, message: str) -> str:
    """Commits only the files that changed since `before`. Returns a summary for the user/agent."""
    after = snapshot(root)
    changed = [p for p, v in after.items() if before.get(p) != v]
    skipped = [p for p in changed if _SECRET_PATTERN.search(p)]
    changed = [p for p in changed if p not in skipped]
    note = f" (not committed, looks sensitive: {', '.join(skipped)})" if skipped else ""
    cap = _max_file_bytes(root)
    if cap:
        big = [p for p in changed if (after[p][2] or 0) > cap]
        if big:
            changed = [p for p in changed if p not in big]
            note += f" (not committed, over the project's size cap: {', '.join(big)}; move to data/ or raise the cap)"
    if not changed:
        return "Git: no new project changes to commit." + note

    ok, out = _git(root, "add", "--", *changed)
    if not ok:
        return f"Git: staging failed: {out}"
    ok, out = _git(root, "commit", "-m", message, "--only", "--", *changed)
    if not ok:
        return f"Git: commit failed: {out}"
    return f"Git: committed {len(changed)} file(s): {', '.join(changed[:10])}" + (" ..." if len(changed) > 10 else "") + note


def sync(root: Path) -> str:
    """Pull (rebase) then push. Aborts a conflicted rebase so the repo is never left half-merged."""
    ok, out = _git(root, "pull", "--rebase", "--autostash")
    if not ok:
        _git(root, "rebase", "--abort")
        return f"Git sync stopped at pull; nothing was pushed and the repo was left unchanged. Resolve manually.\n{out}"
    ok, out = _git(root, "push")
    if not ok:
        return f"Git pull succeeded but push failed:\n{out}"
    return "Git sync complete (pulled and pushed)."
