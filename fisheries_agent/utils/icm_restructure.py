"""Restructures an existing project into a new ICM workspace beside it. The original is only ever read.

    python -m utils.icm_restructure <project folder> [--dry-run] [--copy-small-data]

The new folder is <original name>_icm under the projects root. Small text files (scripts, notes, small result tables)
are copied into the stage that matches their role; data files, model objects and binary reports are linked by path in
data/manifest.yaml (size, mtime, sha256) and never copied unless --copy-small-data is given for small data files.
Secrets, hidden files, tooling folders and unclassified binaries stay behind. MIGRATION.md lists everything.
"""
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from utils import gitsync, icm_data, icm_git, icm_scaffold, project_memory

HERE = Path(__file__).resolve().parent.parent
MAP_PATH = HERE / "icm_templates" / "restructure_map.yaml"
COPY_MAX_MB = 1.0
MAX_FILES = 20000
LIST_CAP = 200

TOOLING_DIRS = {"renv", "packrat", "__pycache__", "node_modules", "venv", ".venv"}
SCRIPT_SUFFIXES = {".r", ".rmd", ".qmd", ".py", ".sh", ".nimble"}
MODEL_SUFFIXES = {".rds", ".rdata", ".rda", ".mcmc", ".samples"}
DATA_SUFFIXES = {".csv", ".tsv", ".xlsx", ".xls", ".dat", ".sav", ".dta", ".parquet", ".feather", ".mdb", ".accdb", ".shp", ".tif", ".gdb"}
REPORT_SUFFIXES = {".docx", ".doc", ".pdf", ".pptx", ".html"}
TEXT_SUFFIXES = {".r", ".rmd", ".qmd", ".py", ".sh", ".md", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml", ".log", ".out", ".rproj", ".bib", ".csl", ".tex", ".nimble"}
_LIBRARY = re.compile(r"\b(?:library|require|requireNamespace)\(\s*[\"']?([A-Za-z][A-Za-z0-9.]*)")
_PKG_SCAN_FILES = 40
_PKG_SCAN_BYTES = 30000


def load_map() -> dict:
    return yaml.safe_load(MAP_PATH.read_text(encoding="utf-8")) or {}


def is_icm_workspace(path: Path) -> bool:
    return (Path(path) / "_config" / "project.yaml").is_file() and (Path(path) / "AGENTS.md").is_file()


def category(rel: str) -> str:
    """script, model, report, results, data, doc or other."""
    suffix = Path(rel).suffix.lower()
    if suffix in MODEL_SUFFIXES or suffix.startswith(".nimble") and suffix != ".nimble":
        return "model"
    if suffix in SCRIPT_SUFFIXES:
        return "script"
    if suffix in REPORT_SUFFIXES:
        return "report"
    c = project_memory.classify(rel)
    if c == "other":
        if suffix in DATA_SUFFIXES:
            return "data"
        if suffix in {".md", ".txt", ".bib", ".tex"}:
            return "doc"
    return c


def walk(source: Path):
    """Yields (relative posix path, absolute path, skip_reason or None) for every file, plus hidden or tooling
    folders as skipped entries with a trailing slash. Does not follow symbolic links."""
    source = Path(source)
    n = 0
    for dirpath, dirnames, filenames in os.walk(source):
        keep = []
        for d in sorted(dirnames):
            full = Path(dirpath) / d
            rel = full.relative_to(source).as_posix()
            if d.startswith(".") or d in TOOLING_DIRS or d.endswith("_cache") or full.is_symlink():
                yield rel + "/", full, "hidden or tooling folder (not scanned)"
            else:
                keep.append(d)
        dirnames[:] = keep
        for name in sorted(filenames):
            full = Path(dirpath) / name
            rel = full.relative_to(source).as_posix()
            n += 1
            if n > MAX_FILES:
                yield rel, full, "scan limit reached"
                return
            if full.is_symlink():
                yield rel, full, "symbolic link"
            elif name.startswith("."):
                yield rel, full, "hidden file"
            elif gitsync._SECRET_PATTERN.search(rel):
                yield rel, full, "may contain secrets"
            else:
                yield rel, full, None


def detect_packages(source: Path) -> list:
    """Packages named in library()/require() calls in the first few R scripts, most used first."""
    found = {}
    count = 0
    for rel, full, reason in walk(source):
        if reason or Path(rel).suffix.lower() not in {".r", ".rmd", ".qmd"}:
            continue
        count += 1
        try:
            text = full.read_text(encoding="utf-8", errors="replace")[:_PKG_SCAN_BYTES]
        except OSError:
            continue
        for m in _LIBRARY.findall(text):
            found[m] = found.get(m, 0) + 1
        if count >= _PKG_SCAN_FILES:
            break
    return [k for k, _ in sorted(found.items(), key=lambda kv: (-kv[1], kv[0]))]


def suggest(source: Path, packages: list = None) -> list:
    """Project types ranked from the folder and file names and the packages the scripts use."""
    names = " ".join(rel for rel, _, reason in walk(source) if reason is None)
    packages = packages if packages is not None else detect_packages(source)
    return icm_scaffold.suggest_type(f"{Path(source).name} {names} {' '.join(packages)}")


def build_plan(source, type_key: str, copy_max_mb: float = COPY_MAX_MB, copy_small_data: bool = False,
               hash_limit_mb: float = icm_data.HASH_LIMIT_MB) -> dict:
    """Decides, for every file, whether it is copied, linked or left behind. Reads the source; writes nothing."""
    source = Path(source).resolve()
    mapping = load_map().get(type_key)
    if mapping is None:
        raise ValueError(f"No restructure mapping for project type '{type_key}'.")
    entries, truncated = [], False
    for rel, full, reason in walk(source):
        if reason == "scan limit reached":
            truncated = True
            break
        if rel.endswith("/"):
            entries.append({"rel": rel, "category": "folder", "action": "skip", "reason": reason, "size": 0})
            continue
        try:
            size = full.stat().st_size
        except OSError:
            entries.append({"rel": rel, "category": "other", "action": "skip", "reason": "unreadable", "size": 0})
            continue
        cat = category(rel)
        if reason:
            entries.append({"rel": rel, "category": cat, "action": "skip", "reason": reason, "size": size})
            continue
        suffix = Path(rel).suffix.lower()
        small_text = suffix in TEXT_SUFFIXES and size <= copy_max_mb * 1024 * 1024
        e = {"rel": rel, "category": cat, "size": size, "action": "skip", "reason": "", "dest": None, "stage": None}
        if cat == "model":
            e.update(action="link", dest="data/models", reason="model object")
        elif cat == "data":
            if copy_small_data and small_text:
                e.update(action="copy", dest=f"data/raw/{rel}", reason="small data file copied on request")
            else:
                e.update(action="link", dest="data/raw", reason="data file linked, not copied")
        elif cat == "report":
            e.update(action="link", dest="data/raw", reason="binary report linked")
        else:
            target = mapping.get(cat, "legacy")
            if small_text:
                where = f"legacy/files/{rel}" if target == "legacy" else f"stages/{target}/references/legacy/{rel}"
                e.update(action="copy", dest=where, stage=None if target == "legacy" else target, reason=f"{cat} copied")
            else:
                e.update(reason="binary or large file of unknown role; still in the original project")
        entries.append(e)
    return {"source": str(source), "type": type_key, "entries": entries, "truncated": truncated,
            "copy_max_mb": copy_max_mb, "hash_limit_mb": hash_limit_mb, "copy_small_data": copy_small_data}


def summarize(plan: dict) -> dict:
    out = {"copy": 0, "link": 0, "skip": 0, "link_bytes": 0, "by_stage": {}}
    for e in plan["entries"]:
        out[e["action"]] += 1
        if e["action"] == "link":
            out["link_bytes"] += e["size"]
        if e["action"] == "copy":
            key = e["stage"] or ("data" if str(e["dest"]).startswith("data/") else "legacy")
            out["by_stage"][key] = out["by_stage"].get(key, 0) + 1
    return out


def format_plan(plan: dict, folder: str) -> str:
    s = summarize(plan)
    lines = [f"Restructure plan: {plan['source']}  ->  {folder}", f"Project type: {plan['type']}", "",
             f"  Copy into the workspace: {s['copy']} file(s)" + (f"  {s['by_stage']}" if s["by_stage"] else ""),
             f"  Link by path (not copied): {s['link']} file(s), {s['link_bytes'] / 1024 / 1024:.1f} MB",
             f"  Leave behind: {s['skip']} item(s)"]
    if plan["truncated"]:
        lines.append(f"  Note: scan stopped after {MAX_FILES} files.")
    lines.append("\nThe original project is not modified.")
    return "\n".join(lines)


def _add_legacy_row(stage_ctx: Path, source_name: str) -> None:
    """Adds a legacy-material row to the stage's Inputs table (replacing the 'None' placeholder row)."""
    text = stage_ctx.read_text(encoding="utf-8")
    m = re.search(r"(## Inputs\n\n)(.*?)(\n\n## )", text, re.S)
    if not m or "references/legacy/" in m.group(2):
        return
    lines = [ln for ln in m.group(2).splitlines() if not ln.startswith("| None |")]
    if not any(ln.startswith("|") for ln in lines):
        lines = ["| Source | File/Location | Section/Scope | Why |", "| --- | --- | --- | --- |"]
    row = icm_scaffold._row(["Original project", "`references/legacy/`", f"Files copied from {source_name}; precedent only", "Shows how this work was done before"])
    stage_ctx.write_text(text[:m.start(2)] + "\n".join(lines + [row]) + text[m.end(2):], encoding="utf-8")


def _table(rows: list, header: list) -> str:
    if not rows:
        return "None.\n"
    out = icm_scaffold._table(header, rows[:LIST_CAP])
    if len(rows) > LIST_CAP:
        out += f"\n\n...and {len(rows) - LIST_CAP} more."
    return out + "\n"


def migration_text(plan: dict, name: str, folder: str) -> str:
    entries = plan["entries"]
    copied = [[f"`{e['rel']}`", f"`{e['dest']}`"] for e in entries if e["action"] == "copy"]
    linked = [[f"`{e['rel']}`", e["category"], f"{e['size'] / 1024 / 1024:.2f} MB"] for e in entries if e["action"] == "link"]
    left = [[f"`{e['rel']}`", e["reason"]] for e in entries if e["action"] == "skip"]
    s = summarize(plan)
    return "\n".join([
        f"# Migration: {name}", "",
        f"Created {datetime.now(timezone.utc).strftime('%Y-%m-%d')} from `{plan['source']}` as `{folder}`.",
        "The original project was only read; nothing in it was changed, moved or deleted.", "",
        f"- Copied: {s['copy']} file(s)",
        f"- Linked by path: {s['link']} file(s) ({s['link_bytes'] / 1024 / 1024:.1f} MB), recorded in `data/manifest.yaml`",
        f"- Left behind: {s['skip']} item(s)", f"- Project type: {plan['type']}", "",
        "## Copied", "", _table(copied, ["Original", "In this workspace"]),
        "## Linked (not copied)", "", _table(linked, ["Original", "Kind", "Size"]),
        "## Left behind", "", _table(left, ["Original", "Why"]),
        "## Next steps", "",
        "- Check `GAPS.md` and `skills/` for references the Fisheries Brain could not supply.",
        "- Linked files are verified by size and modification time each time a stage runs (`python -m utils.icm_data <workspace>`).",
        f"- The original remains at `{plan['source']}`; retire it only when you are satisfied with this workspace.", ""])


def execute(plan: dict, projects_root, project_name: str, answers: dict = None, git_cfg: dict = None,
            routing: str = None, profile: str = None, folder: str = None) -> Path:
    """Writes the workspace. Raises if the target exists, overlaps the source, or the source is already an ICM workspace."""
    source = Path(plan["source"])
    if is_icm_workspace(source):
        raise ValueError(f"{source} is already an ICM workspace.")
    folder = folder or icm_scaffold.folder_name(project_name, source.name)
    dest_root = Path(projects_root).resolve()
    target_dir = (dest_root / folder).resolve()
    if target_dir == source or target_dir.is_relative_to(source) or source.is_relative_to(target_dir):
        raise ValueError("The new workspace cannot be inside the original project (or contain it).")
    legacy = {"source": str(source), "migrated": datetime.now(timezone.utc).strftime("%Y-%m-%d")}
    dest = icm_scaffold.scaffold(dest_root, folder, project_name, plan["type"], answers, git_cfg, routing, profile, legacy)

    manifest, stages_with_legacy = [], set()
    for e in plan["entries"]:
        if e["action"] == "skip":
            continue
        src = source / e["rel"]
        if e["action"] == "copy":
            target = dest / e["dest"]
            if not target.resolve().is_relative_to(dest.resolve()):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, target)
            if e["stage"]:
                stages_with_legacy.add(e["stage"])
            if e["dest"].startswith("data/"):
                manifest.append(icm_data.make_entry(target, e["category"], e["dest"], "copied from original", plan["hash_limit_mb"]))
        else:
            manifest.append(icm_data.make_entry(src, e["category"], None, e["dest"], plan["hash_limit_mb"]))
    icm_data.save(dest, manifest)
    for slug in sorted(stages_with_legacy):
        _add_legacy_row(dest / "stages" / slug / "CONTEXT.md", source.name)
    (dest / "legacy").mkdir(exist_ok=True)
    (dest / "legacy" / "README.md").write_text(
        f"# Legacy\n\nThis workspace was restructured from `{source}`. The original is unchanged and is the source of truth for "
        "anything not copied here. Copied files are snapshots; linked files are listed in `data/manifest.yaml`.\n", encoding="utf-8")
    (dest / "MIGRATION.md").write_text(migration_text(plan, project_name, folder), encoding="utf-8")
    (dest / "data" / "README.md").write_text(
        "# Data\n\nLarge inputs and model objects are not versioned. `manifest.yaml` lists files linked from the original project "
        "(path, size, mtime, sha256) and any small data copied here. Record where each file came from below.\n\n", encoding="utf-8")
    if git_cfg and git_cfg.get("enabled"):
        icm_git.apply_size_cap(dest, git_cfg)
    return dest


def run(source, llm=None, root=None, dry_run: bool = False, copy_small_data: bool = False):
    """Interactive restructure: suggested type, plan preview, questionnaire, git options, then write."""
    from utils import icm_wizard
    source = Path(source).resolve()
    if not source.is_dir():
        raise SystemExit(f"{source} is not a folder.")
    if is_icm_workspace(source):
        raise SystemExit(f"{source} is already an ICM workspace.")
    try:
        root = Path(root) if root else icm_wizard.projects_root()
    except RuntimeError:
        root = source.parent
    folder = icm_scaffold.folder_name(source.name, source.name)
    packages = detect_packages(source)
    ranked = suggest(source, packages)
    print(f"\nRestructuring {source.name}. Packages detected in scripts: {', '.join(packages[:12]) or 'none'}")
    types = icm_scaffold.load_types()
    ordered = ranked + [k for k in types if k not in ranked]
    print("Suggested project type (best match first):")
    for i, k in enumerate(ordered, 1):
        print(f"  {i}. {types[k]['title']} ({k})" + ("  <- suggested" if ranked and i == 1 else ""))
    pick = icm_wizard.ask("Choose a number", "1")
    try:
        type_key = ordered[int(pick) - 1]
    except (ValueError, IndexError):
        type_key = ordered[0]
    plan = build_plan(source, type_key, copy_small_data=copy_small_data)
    print("\n" + format_plan(plan, str(root / folder)))
    if dry_run:
        print("\nDry run: nothing was written.")
        return None
    if (root / folder).exists():
        raise SystemExit(f"{root / folder} already exists; remove or rename it first.")
    if not icm_wizard.PROFILE_PATH.is_file() or not icm_wizard.PROFILE_PATH.read_text(encoding="utf-8").strip():
        icm_wizard.collect_profile()
    print("\nA few questions about the project (Enter to skip):")
    defaults = {"analyses": ", ".join(packages[:8])}
    answers = {k: icm_wizard.ask(q, defaults.get(k, "")) for k, q in icm_wizard.PROJECT_QUESTIONS}
    git_cfg = icm_wizard.ask_git()
    if not icm_wizard.ask_yes_no(f"\nCreate {root / folder}?", True):
        raise SystemExit("Cancelled; nothing was written.")
    ptype = types[type_key]
    llm = llm if llm is not None else icm_wizard.make_llm()
    routing = icm_wizard.write_routing(llm, source.name, ptype, answers)
    dest = execute(plan, root, source.name, answers, git_cfg, routing, folder=folder)
    print(f"Created {dest}\nSee MIGRATION.md for what was copied, linked and left behind.")
    if git_cfg["enabled"]:
        print("Git repository initialized; large files and data/ are ignored.")
    icm_wizard.offer_seeding(dest, ptype, llm)
    return dest


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    run(args[0], dry_run="--dry-run" in argv, copy_small_data="--copy-small-data" in argv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
