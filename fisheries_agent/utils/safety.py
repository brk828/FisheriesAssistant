"""Validation helpers that keep model-supplied tool arguments inside the scientist's projects."""
import csv
import re
from pathlib import Path

IDENT = re.compile(r"^[A-Za-z][A-Za-z0-9_.]{0,63}$")
ALLOWED_METHODS = {"PCA", "MDS", "HEATMAP"}
MIN_ITERATIONS, MAX_ITERATIONS = 1000, 100000


class SafetyError(ValueError):
    """Raised when a tool argument fails validation; the message is safe to show the model."""


def project_roots(manifest: dict) -> list:
    return [Path(p["project_path"]).resolve() for p in manifest.get("projects", {}).values()]


def resolve_in_roots(path: str, roots: list) -> Path:
    try:
        resolved = Path(path).expanduser().resolve()
    except (OSError, RuntimeError):
        raise SafetyError(f"Invalid path: {path}")
    if not any(resolved.is_relative_to(root) for root in roots):
        raise SafetyError("Path is outside the registered project folders.")
    return resolved


def validate_csv(path: str, roots: list) -> Path:
    resolved = resolve_in_roots(path, roots)
    if resolved.suffix.lower() != ".csv" or not resolved.is_file():
        raise SafetyError("Expected an existing .csv file inside a registered project.")
    return resolved


def csv_header(csv_path: Path) -> list:
    with open(csv_path, newline="", encoding="utf-8-sig", errors="replace") as f:
        return next(csv.reader(f), [])


def validate_columns(csv_path: Path, names: list) -> list:
    header = csv_header(csv_path)
    for name in names:
        if not IDENT.match(name):
            raise SafetyError(f"Column name '{name}' has unsupported characters.")
        if name not in header:
            raise SafetyError(f"Column '{name}' not found. Available columns: {', '.join(header[:40])}")
    return names


def parse_zi_formula(formula: str, csv_path: Path) -> str:
    """Returns '1' for an intercept-only formula, otherwise a comma-separated list of validated columns."""
    rhs = formula.strip().lstrip("~").strip()
    if rhs in ("", "1"):
        return "1"
    return ",".join(validate_columns(csv_path, [t.strip() for t in rhs.split("+")]))


def validate_method(method: str) -> str:
    method = method.upper()
    if method not in ALLOWED_METHODS:
        raise SafetyError(f"Method must be one of {sorted(ALLOWED_METHODS)}.")
    return method


def clamp_iterations(iterations) -> int:
    try:
        n = int(iterations)
    except (TypeError, ValueError):
        n = 10000
    return max(MIN_ITERATIONS, min(MAX_ITERATIONS, n))


def validate_prefix_columns(csv_path: Path, prefix: str) -> str:
    if not IDENT.match(prefix):
        raise SafetyError(f"Capture history prefix '{prefix}' has unsupported characters.")
    header = csv_header(csv_path)
    if sum(1 for h in header if h.startswith(prefix)) < 2:
        raise SafetyError(f"Need at least two columns starting with '{prefix}'. Columns: {', '.join(header[:40])}")
    return prefix
