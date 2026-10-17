"""Git option for ICM workspaces: .gitignore generation, git init, and a size-cap check for large files."""
import shutil
import subprocess
from pathlib import Path

DEFAULT_MAX_FILE_MB = 50
DEFAULT_IGNORE_TYPES = [
    "*.rds", "*.RData", "*.rdata", "*.rda", "*.nimble*", "*.mcmc", "*.samples",
    ".Rhistory", ".Rproj.user/", ".env", ".env.*",
]
DEFAULT_IGNORE_PATHS = ["data/"]
_MARK = "# --- ICM large-file rules ---"


def settings(enabled: bool, ignore_types=None, ignore_paths=None, max_file_mb=None) -> dict:
    """Normalized git settings as stored in _config/project.yaml."""
    return {
        "enabled": bool(enabled),
        "ignore_types": list(DEFAULT_IGNORE_TYPES if ignore_types is None else ignore_types),
        "ignore_paths": list(DEFAULT_IGNORE_PATHS if ignore_paths is None else ignore_paths),
        "max_file_mb": DEFAULT_MAX_FILE_MB if max_file_mb is None else max_file_mb,
    }


def gitignore_text(cfg: dict, extra_files=()) -> str:
    lines = [_MARK, f"# Files over {cfg['max_file_mb']} MB are listed below by the size check."]
    lines += cfg["ignore_types"] + cfg["ignore_paths"] + sorted(set(extra_files))
    return "\n".join(dict.fromkeys(lines)) + "\n"


def oversized(root: Path, max_mb: float) -> list:
    """Relative POSIX paths of files above the cap, ignoring .git."""
    limit = max_mb * 1024 * 1024
    out = []
    for p in Path(root).rglob("*"):
        if ".git" in p.relative_to(root).parts or not p.is_file():
            continue
        if p.stat().st_size > limit:
            out.append(p.relative_to(root).as_posix())
    return sorted(out)


def apply_size_cap(root: Path, cfg: dict) -> list:
    """Rewrites .gitignore so every file above the cap is ignored; returns the files added."""
    root = Path(root)
    big = oversized(root, cfg["max_file_mb"])
    (root / ".gitignore").write_text(gitignore_text(cfg, big), encoding="utf-8")
    return big


def init_repo(root: Path, cfg: dict) -> tuple:
    """Writes .gitignore and runs git init. Returns (ok, message). Never creates a remote."""
    root = Path(root)
    apply_size_cap(root, cfg)
    git = shutil.which("git")
    if not git:
        return False, "git was not found on PATH; .gitignore was written but no repository was created."
    r = subprocess.run([git, "init", "-q"], cwd=root, capture_output=True, text=True)
    if r.returncode:
        return False, (r.stderr or r.stdout).strip()[:300]
    return True, "Initialized a git repository (no remote configured)."
