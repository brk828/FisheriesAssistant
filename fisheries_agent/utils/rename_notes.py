"""Rename source notes whose file name is a placeholder ("UnreadableOcrScan..._PML0503") to match their title.

    python -m utils.rename_notes                 dry run: placeholder file names, new names, notes left alone
    python -m utils.rename_notes --apply         rename and update every link
    python -m utils.rename_notes --ids PML0503   only these IDs

A note is renamed when its file name starts with a placeholder word (Unreadable, Illegible, Fragmentary, Garbled,
Corrupted, Untitled, Unidentified, Blank, Damaged, Degraded) and its frontmatter title is a real title (not itself a
placeholder, see rebuild_notes.PLACEHOLDER_TITLE). The new name follows the ingest convention: the title's letters
(first 30) plus the old suffix (_PML0503, _14702, _1991_11_04). Links are rewritten everywhere they can occur:
02_Brain stub files, other source notes, the full-text header (`note:`), brain_meta/marsh_catalog.csv (`note`),
brain_meta/ingest_manifest.json, brain_meta/source_titles.json (key) and brain_meta/public_pdf_ids.csv. Notes whose
title is still a placeholder are listed, not renamed. Commit and push afterwards.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

from utils import pdf_ingest
from utils.rebuild_notes import PLACEHOLDER_TITLE, old_fields

SOURCES = pdf_ingest.SOURCES_DIR
BRAIN = pdf_ingest.BRAIN_DIR
META = pdf_ingest.BASE_DIR / "brain_meta"
PLACEHOLDER_STEM = re.compile(r"^(Unreadable|Illegible|Fragmentary|Garbled|Corrupted|Untitled|Unidentified|Blank|Damaged|Degraded)")
SUFFIX = re.compile(r"_((?:PML|FAL)\d{4}|\d{5,6}|\d{4}(?:_\d{2}){0,2})$")


def new_stem(title: str, old: str) -> str:
    m = SUFFIX.search(old)
    suffix = m.group(0) if m else ""
    letters = re.sub(r"[^A-Za-z ]", "", title or "").title().replace(" ", "")[:30] or "Untitled"
    return letters + suffix


def plan(ids: list) -> tuple:
    renames, left = [], []
    taken = {p.stem.lower() for p in SOURCES.glob("*.md")}
    for p in sorted(SOURCES.glob("*.md")):
        if not PLACEHOLDER_STEM.match(p.stem):
            continue
        if ids and not any(p.stem.endswith(f"_{i}") for i in ids):
            continue
        title = old_fields(p.read_text(encoding="utf-8", errors="replace")).get("title", "")
        if not title or PLACEHOLDER_TITLE.search(title):
            left.append((p.stem, title))
            continue
        stem = new_stem(title, p.stem)
        n = 2
        while stem.lower() in taken and stem.lower() != p.stem.lower():
            stem = f"{new_stem(title, p.stem)}_{n}"
            n += 1
        taken.add(stem.lower())
        renames.append((p.stem, stem, title))
    return renames, left


def _link_pattern(old: str) -> re.Pattern:
    return re.compile(r"\[\[" + re.escape(old) + r"(?=[\]|#])")


def rewrite_text_files(files, mapping: dict) -> int:
    pats = [(_link_pattern(o), "[[" + n) for o, n in mapping.items()]
    changed = 0
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        if "[[" not in text or not any(o in text for o in mapping):
            continue
        new = text
        for pat, rep in pats:
            new = pat.sub(rep, new)
        if new != text:
            f.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def apply(renames: list) -> None:
    mapping = {o: n for o, n, _ in renames}
    for o, n, _ in renames:
        (SOURCES / f"{o}.md").rename(SOURCES / f"{n}.md")
    print(f"stub files updated: {rewrite_text_files(sorted((BRAIN / '02_Brain').glob('*.md')), mapping)}")
    print(f"source notes updated: {rewrite_text_files(sorted(SOURCES.glob('*.md')), mapping)}")
    full = BRAIN / "full_text"
    ft = [full / f"{SUFFIX.search(o).group(1)}.md" for o in mapping if SUFFIX.search(o)]
    print(f"full-text headers updated: {rewrite_text_files([f for f in ft if f.is_file()], mapping)}")
    # marsh catalog and public ID register: the note column
    for path, col in ((META / "marsh_catalog.csv", "note"), (META / "public_pdf_ids.csv", "note")):
        if not path.is_file():
            continue
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fields, rows = reader.fieldnames, list(reader)
        n = 0
        for r in rows:
            v = (r.get(col) or "")
            stem = v[:-3] if v.endswith(".md") else v
            if stem in mapping:
                r[col] = mapping[stem] + (".md" if v.endswith(".md") else "")
                n += 1
        if n:
            with open(path, "w", newline="", encoding="utf-8-sig") as f:
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerows(rows)
        print(f"{path.name}: {n} rows")
    # JSON files edited as text so their layout stays the same
    for path in (META / "ingest_manifest.json", META / "source_titles.json"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        new = text
        for o, n in mapping.items():
            new = new.replace(f'"{o}.md"', f'"{n}.md"').replace(f'"{o}"', f'"{n}"')
        if new != text:
            json.loads(new)
            path.write_text(new, encoding="utf-8")
        print(f"{path.name}: {'updated' if new != text else 'no change'}")


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    renames, left = plan(args.ids or [])
    for o, n, _ in renames:
        print(f"{o}  ->  {n}")
    if left:
        print(f"\nLeft alone, title still a placeholder ({len(left)}):")
        for o, t in left:
            print(f"  {o}: {t}")
    if not args.apply:
        print(f"\n{len(renames)} notes would be renamed. Dry run; add --apply.")
        return 0
    apply(renames)
    print(f"Renamed {len(renames)} notes. Commit and push 01_Sources, 02_Brain and brain_meta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
