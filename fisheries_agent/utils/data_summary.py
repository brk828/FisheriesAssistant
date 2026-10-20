"""Standard data summary: the interface between the data handler and the analyst.

    python -m utils.data_summary <file.csv> [--out <folder>]   # writes data_summary.json and data_summary.md

Reads one CSV (no LLM, no network) and records columns, types, missingness, ranges, group counts and data-type hints
(capture histories, count data with many zeros, CPUE/effort columns, dates). The analyst reads this file, not the raw data.
"""
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

MAX_ROWS = 200_000
MAX_LEVELS = 12
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([ T]\d{2}:\d{2}(:\d{2})?)?$|^\d{1,2}/\d{1,2}/\d{2,4}$")
HISTORY_COL = re.compile(r"^(occ|occasion|pass|session|t|y)[_.]?\d+$", re.I)
COUNT_NAMES = re.compile(r"count|catch|abundance|^n$|num_|n_fish", re.I)
EFFORT_NAMES = re.compile(r"effort|hours|soak|net[_ ]?(night|set)|distance|area|cpue", re.I)
ID_NAMES = re.compile(r"tag|pit|^id$|fish[_ ]?id|individual", re.I)


def _num(v):
    try:
        return float(v)
    except ValueError:
        return None


def _kind(values: list) -> str:
    if not values:
        return "empty"
    if all(_num(v) is not None for v in values):
        return "integer" if all(float(v).is_integer() for v in values) else "numeric"
    if sum(bool(DATE_RE.match(v)) for v in values) >= 0.9 * len(values):
        return "date"
    return "text"


def _profile(name: str, raw: list) -> dict:
    vals = [v.strip() for v in raw if v is not None and v.strip() not in ("", "NA", "N/A", "NULL", "null")]
    kind = _kind(vals)
    out = {"name": name, "type": kind, "missing": len(raw) - len(vals), "unique": len(set(vals))}
    if kind in ("integer", "numeric"):
        nums = [float(v) for v in vals]
        out.update(min=min(nums), max=max(nums), mean=round(sum(nums) / len(nums), 4), zeros=sum(n == 0 for n in nums), negatives=sum(n < 0 for n in nums))
    elif kind == "date":
        out.update(min=min(vals), max=max(vals))
    elif kind == "text" and out["unique"] <= MAX_LEVELS:
        counts = {}
        for v in vals:
            counts[v] = counts.get(v, 0) + 1
        out["levels"] = dict(sorted(counts.items(), key=lambda kv: -kv[1]))
    return out


def _hints(columns: list, n_rows: int, id_col) -> list:
    hints = []
    hist = [c["name"] for c in columns if HISTORY_COL.match(c["name"]) and c.get("max") in (0.0, 1.0) and c.get("min") in (0.0, 1.0)]
    if len(hist) >= 3:
        hints.append(f"capture-history matrix ({len(hist)} occasion columns: {hist[0]} .. {hist[-1]})")
    if id_col:
        c = next(c for c in columns if c["name"] == id_col)
        if c["unique"] < n_rows - c["missing"]:
            hints.append(f"repeated individual ids in '{id_col}' ({c['unique']} unique in {n_rows} rows): recaptures or contacts present")
    for c in columns:
        if c["type"] == "integer" and COUNT_NAMES.search(c["name"]) and c.get("min", 0) >= 0 and n_rows:
            share = c["zeros"] / n_rows
            hints.append(f"'{c['name']}' looks like a count ({share:.0%} zeros" + ("; zero-heavy, consider zero-inflated or hurdle models" if share >= 0.3 else "") + ")")
        if EFFORT_NAMES.search(c["name"]):
            hints.append(f"'{c['name']}' looks like effort or CPUE")
        if c.get("negatives"):
            hints.append(f"'{c['name']}' has {c['negatives']} negative value(s): check")
    dates = [c for c in columns if c["type"] == "date"]
    if dates:
        hints.append("date column(s): " + ", ".join(c["name"] for c in dates))
    return hints


def summarize(csv_path) -> dict:
    path = Path(csv_path)
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        rows = []
        for i, row in enumerate(reader):
            if i >= MAX_ROWS:
                break
            rows.append(row + [""] * (len(header) - len(row)))
    columns = [_profile(name, [r[i] for r in rows]) for i, name in enumerate(header)]
    id_col = next((c["name"] for c in columns if ID_NAMES.search(c["name"])), None)
    duplicates = len(rows) - len({tuple(r) for r in rows})
    return {
        "source_file": path.name, "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "rows": len(rows), "truncated": len(rows) >= MAX_ROWS, "duplicate_rows": duplicates,
        "columns": columns, "hints": _hints(columns, len(rows), id_col), "cleaning_notes": [],
    }


def to_markdown(s: dict) -> str:
    out = [f"# Data summary: {s['source_file']}", "", f"{s['rows']} rows, {len(s['columns'])} columns, {s['duplicate_rows']} duplicate rows.", ""]
    if s["hints"]:
        out += ["## Data-type hints", ""] + [f"- {h}" for h in s["hints"]] + [""]
    out += ["## Columns", "", "| Column | Type | Missing | Unique | Range / levels |", "| --- | --- | --- | --- | --- |"]
    for c in s["columns"]:
        if "levels" in c:
            rng = ", ".join(f"{k} ({v})" for k, v in c["levels"].items())
        elif "min" in c:
            rng = f"{c['min']} to {c['max']}"
        else:
            rng = ""
        out.append(f"| {c['name']} | {c['type']} | {c['missing']} | {c['unique']} | {rng.replace('|', '/')} |")
    out += ["", "## Cleaning notes", "", "(none recorded)" if not s["cleaning_notes"] else "\n".join(f"- {n}" for n in s["cleaning_notes"]), ""]
    return "\n".join(out)


def write_summary(csv_path, out_dir) -> tuple:
    s = summarize(csv_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "data_summary.json").write_text(json.dumps(s, indent=1), encoding="utf-8")
    (out_dir / "data_summary.md").write_text(to_markdown(s), encoding="utf-8")
    return out_dir / "data_summary.json", out_dir / "data_summary.md"


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    src = Path(argv[0])
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else src.parent
    j, m = write_summary(src, out)
    print(f"Wrote {j} and {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
