"""Work lists of Minckley MIDs still to ingest, one CSV pair per list (to-do and done), in 00_Fisheries_Brain/.

    python -m utils.minckley_lists restricted     (re)build the non-public-domain list and print the counts
    python -m utils.minckley_lists public_missing (re)build the list of public-domain PDFs that have no note
    python -m utils.minckley_lists                counts for every list

Lists:
  public      unprocessed_public_domain_mids.csv / process_public_domain_mids.csv (built by the Minckley-side export)
  restricted  unprocessed_restricted_mids.csv / process_restricted_mids.csv: MIDs whose permission in
              brain_meta/minckley_library.csv is anything but "public domain" (denied, granted ...), that have a PDF
              in MINCKLEY_PDF_DIR and no note in 01_Sources yet.
  public_missing  unprocessed_public_missing_mids.csv / process_public_missing_mids.csv: public-domain MIDs with a PDF
              and no note that the public list left out (most were marked done by the old Fish_Science_Brain pipeline,
              whose notes never reached this brain).
The CSVs hold file names, MIDs and the permission label only (no document content).
"""
import csv
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

from utils import pdf_ingest
from utils.pdf_ingest import BRAIN_DIR, META_DIR

LISTS = {
    "public": (BRAIN_DIR / "unprocessed_public_domain_mids.csv", BRAIN_DIR / "process_public_domain_mids.csv"),
    "restricted": (BRAIN_DIR / "unprocessed_restricted_mids.csv", BRAIN_DIR / "process_restricted_mids.csv"),
    "public_missing": (BRAIN_DIR / "unprocessed_public_missing_mids.csv", BRAIN_DIR / "process_public_missing_mids.csv"),
}
LIBRARY_CSV = META_DIR / "minckley_library.csv"
DEFAULT_SOURCE = "C:/Obsidian/Fish_Science_Brain/PDFs_To_Process"
SUPPLEMENT_RE = re.compile(r"\b(plates?|maps?|appendix|appendices)\b", re.I)
DIGITS = re.compile(r"\d+")


def source_dir() -> Path:
    try:
        from dotenv import load_dotenv
        load_dotenv(pdf_ingest.BASE_DIR / ".env")
    except ImportError:
        pass
    return Path(os.getenv("MINCKLEY_PDF_DIR") or DEFAULT_SOURCE)


def permissions() -> dict:
    """{MID: permission label, lower case} from the library reference (first row wins for duplicate MIDs)."""
    out = {}
    with open(LIBRARY_CSV, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            mid = (r.get("MID") or "").strip()
            if mid:
                out.setdefault(mid, (r.get("permission") or "").strip().lower())
    return out


def pdfs_by_mid(source: Path) -> dict:
    """{MID: [file names]} using the same filename rule as the Minckley-side export (every number in the name)."""
    out = defaultdict(list)
    for p in source.iterdir():
        if p.is_file() and p.suffix.lower() == ".pdf":
            for m in DIGITS.findall(p.stem):
                out[str(int(m))].append(p.name)
    return out


def pick_files(mid: str, files: list) -> list:
    """The plain <MID>.pdf when present (other files are scan variants or supplements); else non-supplement files."""
    plain = [f for f in files if Path(f).stem == mid]
    if plain:
        return plain
    mains = [f for f in files if not SUPPLEMENT_RE.search(Path(f).stem)]
    return sorted(mains or files)


def noted_mids() -> set:
    return {str(c[1]) for c in pdf_ingest._vault_catalog() if str(c[1]).isdigit()}


def build_restricted(name: str = "restricted") -> dict:
    source = source_dir()
    if not source.is_dir():
        raise SystemExit(f"Source folder not found: {source}\nSet MINCKLEY_PDF_DIR in .env.")
    perm = permissions()
    files = pdfs_by_mid(source)
    noted = noted_mids()
    if name == "public_missing":
        restricted = {m for m, p in perm.items() if p == "public domain"}
    else:
        restricted = {m for m, p in perm.items() if p != "public domain"}
    rows, no_pdf, has_note = [], 0, 0
    for mid in sorted(restricted, key=int):
        if mid in noted:
            has_note += 1
            continue
        if mid not in files:
            no_pdf += 1
            continue
        for fname in pick_files(mid, files[mid]):
            rows.append((fname, mid, perm[mid]))
    todo, _ = LISTS[name]
    with open(todo, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source_filename", "mid", "permission"])
        w.writerows(rows)
    kinds = defaultdict(int)
    for mid in {r[1] for r in rows}:
        p = perm[mid]
        kinds["denied" if p == "denied" else "granted" if p.startswith("granted") else p] += 1
    return {f"{'public-domain' if name == 'public_missing' else 'restricted'} MIDs in the library": len(restricted), "already have a note": has_note,
            "no PDF on disk": no_pdf, "to process": len({r[1] for r in rows}), "files": len(rows),
            "by permission": dict(kinds), "csv": todo.name}


def counts() -> None:
    from utils import minckley_batch
    source = source_dir()
    for name, (todo, done) in LISTS.items():
        if not todo.is_file():
            print(f"{name}: no list yet")
            continue
        items, missing = minckley_batch.candidates(source, {}, todo, done)
        print(f"{name}: {len(items)} MIDs left ({sum(i['size'] for i in items) / 1e9:.1f} GB), {len(missing)} without a PDF")


def main(argv: list = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args and args[0] in ("restricted", "public_missing"):
        for k, v in build_restricted(args[0]).items():
            print(f"{k}: {v}")
        return 0
    counts()
    return 0


if __name__ == "__main__":
    sys.exit(main())
