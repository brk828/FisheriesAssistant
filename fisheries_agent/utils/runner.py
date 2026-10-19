"""Single entry point for running external programs (Windows-targeted)."""
import glob
import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
R_TEMPLATES = BASE_DIR / "r_templates"
RUNS_DIR = BASE_DIR / "runs"
MAX_OUTPUT_CHARS = 8000
DEFAULT_TIMEOUT = 900
_KEY_PATTERN = re.compile(r"sk-or-[A-Za-z0-9_\-]+")


def redact(text: str) -> str:
    return _KEY_PATTERN.sub("[REDACTED]", text or "")


def truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    text = redact(text)
    return text if len(text) <= limit else text[:limit] + f"\n...[truncated, {len(text) - limit} more characters]"


def find_rscript():
    found = shutil.which("Rscript")
    if found:
        return found
    candidates = []
    for base in (os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)"), os.environ.get("LOCALAPPDATA")):
        if base:
            candidates += glob.glob(os.path.join(base, "R", "R-*", "bin", "Rscript.exe"))
            candidates += glob.glob(os.path.join(base, "R", "R-*", "bin", "x64", "Rscript.exe"))
    return sorted(candidates)[-1] if candidates else None


def new_run_dir(label: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", label)[:40]
    run_dir = RUNS_DIR / f"{datetime.now():%Y%m%d_%H%M%S}_{safe}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def run_command(cmd: list, cwd=None, timeout: int = DEFAULT_TIMEOUT, log_dir=None) -> tuple:
    """Runs cmd without a shell. Returns (ok, redacted_and_truncated_output)."""
    # Child programs (R, user scripts) must not inherit the API key loaded from .env.
    child_env = {k: v for k, v in os.environ.items() if not k.upper().startswith("OPENROUTER_")}
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=timeout, env=child_env, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        ok, out = result.returncode == 0, (result.stdout or "") + (result.stderr or "")
    except subprocess.TimeoutExpired:
        ok, out = False, f"Timed out after {timeout} seconds."
    except OSError as e:
        ok, out = False, f"Could not start program: {e}"
    if log_dir:
        (Path(log_dir) / "run.log").write_text(
            f"command: {' '.join(map(str, cmd))}\nok: {ok}\n\n{redact(out)}", encoding="utf-8"
        )
    return ok, truncate(out)


def run_shell(command: str, cwd, timeout: int = 300) -> tuple:
    """Runs a user-approved command line through bash (or the platform shell). Returns (ok, redacted_and_truncated_output)."""
    child_env = {k: v for k, v in os.environ.items() if not k.upper().startswith("OPENROUTER_")}
    bash = shutil.which("bash")
    try:
        if bash:
            result = subprocess.run([bash, "-c", command], cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                                    errors="replace", timeout=timeout, env=child_env, stdin=subprocess.DEVNULL)
        else:
            result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                                    errors="replace", timeout=timeout, env=child_env, stdin=subprocess.DEVNULL)
        return result.returncode == 0, truncate((result.stdout or "") + (result.stderr or "") + f"\n[exit code {result.returncode}]")
    except subprocess.TimeoutExpired:
        return False, f"Timed out after {timeout} seconds."
    except OSError as e:
        return False, f"Could not start shell: {e}"


def run_r_template(template: str, csv_path, extra_args: list, label: str) -> tuple:
    """Runs r_templates/<template> as: csv, run_dir, *extra_args. Returns (ok, text, run_dir); R writes output.txt/plot.png to run_dir."""
    rscript = find_rscript()
    if not rscript:
        return False, "Rscript was not found. Install R for Windows and re-run verify_and_install_deps.py.", None
    run_dir = new_run_dir(label)
    cmd = [rscript, "--vanilla", str(R_TEMPLATES / template), str(csv_path), str(run_dir), *map(str, extra_args)]
    ok, out = run_command(cmd, cwd=run_dir, log_dir=run_dir)
    return ok, out, run_dir
