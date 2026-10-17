"""Seeds an ICM workspace with reference notes from the Fisheries Brain and reports gaps.

    python -m utils.icm_seed seed <workspace>                # propose, approve, copy stage references, write GAPS.md
    python -m utils.icm_seed refresh <workspace> [--apply]   # show (or apply) brain updates to copied notes
    python -m utils.icm_seed supply <workspace> <pdf|citation|url>   # fill a gap with your own source

Notes are copied as snapshots (never linked) with a content hash in each references/_provenance.json, so later
brain changes can be detected and offered as a refresh. A topic counts as covered only when a source matches at
least MIN_COVERAGE of its search terms; otherwise it is listed in GAPS.md with the kind of source that would fill it.
"""
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from utils import brain_index

HERE = Path(__file__).resolve().parent.parent
TOPICS_PATH = HERE / "icm_templates" / "reference_topics.yaml"
MIN_COVERAGE = 0.6
PER_TOPIC = 3
PER_STAGE = 8
PROVENANCE = "_provenance.json"
EXTERNAL_HEADING = "## External references (not in the brain)"


def _sha(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def project_config(root: Path) -> dict:
    return yaml.safe_load((Path(root) / "_config" / "project.yaml").read_text(encoding="utf-8")) or {}


def fill(query: str, answers: dict) -> str:
    """Replaces {species} and {region} with questionnaire answers (blank when unknown)."""
    out = query.replace("{species}", str(answers.get("species", ""))).replace("{region}", str(answers.get("region", "")))
    return re.sub(r"\s+", " ", out).strip()


def search_topic(entry: dict, answers: dict, per_topic: int = PER_TOPIC) -> dict:
    """Finds brain sources for a topic. `candidates` pass the coverage bar; `tangential` are weaker matches."""
    query = fill(entry["query"], answers)
    core = fill(entry["query"], {})
    found = brain_index.find_sources(query, limit=per_topic * 3, core=core) if query else []
    good = [c for c in found if c["coverage"] >= MIN_COVERAGE][:per_topic]
    weak = [c for c in found if c["coverage"] < MIN_COVERAGE][:3]
    return {**{k: entry.get(k, "") for k in ("topic", "name", "why", "source_hint")}, "query": query, "candidates": good, "tangential": weak}


def propose(root: Path) -> dict:
    """{stage slug: [topic results]} for the workspace's project type."""
    cfg = project_config(root)
    topics = (yaml.safe_load(TOPICS_PATH.read_text(encoding="utf-8")) or {}).get(cfg.get("type"), {})
    answers = cfg.get("answers") or {}
    out = {}
    for slug, entries in topics.items():
        if (Path(root) / "stages" / slug).is_dir():
            out[slug] = [search_topic(e, answers) for e in entries]
    return out


def _load_prov(folder: Path) -> dict:
    p = Path(folder) / PROVENANCE
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def copy_note(candidate: dict, dest_dir: Path) -> bool:
    """Copies one brain source into dest_dir as a snapshot and records its provenance. False if the note is missing."""
    src = brain_index.SOURCES_DIR / f"{candidate['source_id']}.md"
    if not src.is_file():
        return False
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest_dir / src.name)
    prov = _load_prov(dest_dir)
    prov[src.stem] = {
        "brain_path": src.relative_to(HERE).as_posix() if src.is_relative_to(HERE) else str(src),
        "sha256": _sha(src),
        "cite": candidate.get("cite", ""),
        "copied": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    (dest_dir / PROVENANCE).write_text(json.dumps(prov, indent=1, sort_keys=True), encoding="utf-8")
    return True


def prompt_approve(location: str, result: dict) -> list:
    """Shows a topic's candidates; Enter keeps all, 'n' skips, or give numbers like '1,3'."""
    cands = result["candidates"]
    if not cands:
        return []
    print(f"\n[{location}] {result.get('topic') or result.get('name')}")
    for i, c in enumerate(cands, 1):
        print(f"  {i}. {c['short'] or c['source_id']} {c['title'][:80]}")
    ans = input("Keep which? (Enter = all, n = none, or numbers): ").strip().lower()
    if ans in ("n", "no", "none"):
        return []
    if not ans:
        return cands
    keep = {int(x) for x in re.findall(r"\d+", ans)}
    return [c for i, c in enumerate(cands, 1) if i in keep]


def seed(root: Path, approve=None, proposal: dict = None) -> dict:
    """Copies approved candidates into stage references and rewrites shared/sources.md and GAPS.md.
    `approve(location, result) -> list` defaults to keeping everything. Returns {copied: n, gaps: n}."""
    root = Path(root)
    proposal = proposal if proposal is not None else propose(root)
    approve = approve or (lambda loc, r: r["candidates"])
    copied, gaps = 0, []
    for slug, results in proposal.items():
        used = 0
        for r in results:
            if not r["candidates"]:
                gaps.append({"where": f"stage {slug}", **r})
                continue
            chosen = approve(f"stage {slug}", r)[: max(0, PER_STAGE - used)]
            if not chosen:
                gaps.append({"where": f"stage {slug}", **r, "declined": True})
            for c in chosen:
                if copy_note(c, root / "stages" / slug / "references"):
                    copied += 1
                    used += 1
    write_sources(root)
    write_gaps(root, gaps)
    return {"copied": copied, "gaps": len(gaps)}


def _all_reference_dirs(root: Path) -> list:
    root = Path(root)
    return sorted(p.parent for p in root.glob(f"stages/*/references/{PROVENANCE}")) + sorted(p.parent for p in root.glob(f"skills/*/references/{PROVENANCE}"))


def write_sources(root: Path) -> None:
    """Rewrites shared/sources.md from the provenance files, keeping the external references section."""
    root = Path(root)
    path = root / "shared" / "sources.md"
    old = path.read_text(encoding="utf-8") if path.is_file() else ""
    tail = old[old.index(EXTERNAL_HEADING):] if EXTERNAL_HEADING in old else EXTERNAL_HEADING + "\n\n"
    rows = {}
    for folder in _all_reference_dirs(root):
        where = folder.relative_to(root).parent.as_posix()
        for sid, info in _load_prov(folder).items():
            row = rows.setdefault(sid, {"cite": info.get("cite", ""), "where": []})
            row["where"].append(where)
    lines = ["# Sources", "", "Canonical bibliography. Cite as [[source_id]] and give the full citation from this table.", "",
             "| Source id | Citation | Used in |", "| --- | --- | --- |"]
    for sid in sorted(rows):
        cite = rows[sid]["cite"].replace("|", "/") or sid
        lines.append(f"| {sid} | {cite} | {', '.join(rows[sid]['where'])} |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n\n" + tail, encoding="utf-8")


def gaps_text(title: str, gaps: list) -> str:
    out = [f"# {title}", ""]
    if not gaps:
        return "\n".join(out + ["No gaps found: every topic has at least one matching brain source.", ""])
    out += ["Topics where the Fisheries Brain has no close match. To fill one, supply a PDF (it is ingested into the brain) or a "
            "citation/URL (recorded as an external reference) with `python -m utils.icm_seed supply <workspace> <pdf|citation>`, "
            "then reseed. Until then the agent treats the topic as unsourced.", ""]
    for g in gaps:
        out += [f"## {g.get('topic') or g.get('name')} ({g['where']})", "",
                f"- Why it matters: {g.get('why', '')}",
                f"- Searched for: `{g.get('query', '')}`",
                f"- Suggested source: {g.get('source_hint', '')}"]
        if g.get("declined"):
            out.append("- Note: matching sources were found but you declined them.")
        if g.get("tangential"):
            out.append("- Weak matches (not copied): " + "; ".join(f"{t['source_id']}" for t in g["tangential"]))
        out.append("")
    return "\n".join(out)


def write_gaps(root: Path, gaps: list) -> None:
    (Path(root) / "GAPS.md").write_text(gaps_text("Reference gaps", gaps), encoding="utf-8")


def refresh(root: Path, apply: bool = False) -> list:
    """Compares copied notes with the brain. Returns (folder, source_id, status); with apply, updates changed notes."""
    root = Path(root)
    changes = []
    for folder in _all_reference_dirs(root):
        prov = _load_prov(folder)
        for sid, info in prov.items():
            src = HERE / info["brain_path"]
            if not src.is_file():
                changes.append((folder.relative_to(root).as_posix(), sid, "missing in brain"))
            elif _sha(src) != info["sha256"]:
                changes.append((folder.relative_to(root).as_posix(), sid, "changed in brain"))
                if apply:
                    copy_note({"source_id": sid, "cite": info.get("cite", "")}, folder)
    if apply and changes:
        write_sources(root)
    return changes


def supply(root: Path, item: str) -> str:
    """Fills a gap with the user's own source: a PDF goes to the ingest inbox, anything else is an external reference."""
    root = Path(root)
    p = Path(item).expanduser()
    if p.is_file() and p.suffix.lower() == ".pdf":
        from utils import pdf_ingest
        pdf_ingest.PDF_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p, pdf_ingest.PDF_DIR / p.name)
        return (f"Copied {p.name} to {pdf_ingest.PDF_DIR}. Run main_orchestrator.py and answer the ingest prompt, "
                f"then run: python -m utils.icm_seed seed {root} (and regenerate skills).")
    path = root / "shared" / "sources.md"
    text = path.read_text(encoding="utf-8") if path.is_file() else "# Sources\n\n"
    if EXTERNAL_HEADING not in text:
        text = text.rstrip("\n") + f"\n\n{EXTERNAL_HEADING}\n\n"
    path.write_text(text.rstrip("\n") + f"\n- {item.strip()}\n", encoding="utf-8")
    return "Recorded as an external reference in shared/sources.md (not copied into references)."


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 2 or argv[0] not in ("seed", "refresh", "supply"):
        print(__doc__)
        return 2
    cmd, root = argv[0], Path(argv[1])
    if cmd == "seed":
        r = seed(root, approve=prompt_approve)
        print(f"Copied {r['copied']} note(s); {r['gaps']} gap(s) listed in GAPS.md.")
    elif cmd == "refresh":
        changes = refresh(root, apply="--apply" in argv)
        for folder, sid, status in changes:
            print(f"- {folder}: {sid} {status}")
        print("No changes." if not changes else ("Applied." if "--apply" in argv else "Rerun with --apply to update."))
    else:
        if len(argv) < 3:
            print(__doc__)
            return 2
        print(supply(root, " ".join(argv[2:])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
