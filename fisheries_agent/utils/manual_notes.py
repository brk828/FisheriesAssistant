"""Hand-directed fixes for single Marsh Library documents.

    python -m utils.manual_notes handwritten PML0978 [PML0979 ...] [--apply]
        Standard note for a handwritten document OCR cannot read. Author, year and title come from the PDF's file name
        ("Hamman R.L. 1988. Bonytail chub egg collector.pdf" -> R. L. Hamman, 1988, "Bonytail chub egg collector").
        The note says the document is handwritten and points to the original scan; the document is set to public domain
        (permission_override), category correspondence, doc_type handwritten_note. The old note is replaced (its stub
        links are removed first) and renamed to the new title. If the catalog's file name no longer exists (the file was
        renamed in MarshLibrary), the file with the same content is found and the catalog updated.

    python -m utils.manual_notes replace-pdf PML0698 "C:/path/better copy.pdf" [--name "Evermann. 1916. ... (JSTOR).pdf"]
        [--public --reason "..."] [--apply]
        Copies a better PDF of a document into MarshLibrary (the original file stays), points the catalog at it,
        extracts its text (text layer, OCR where needed) into full_text/<code>.md, and with --public sets the
        permission_override to public domain (the reason goes to the catalog's reason column). Then rebuild the note
        with `python -m utils.rebuild_notes run --ids PML0698` (Anthropic batch, needs the API).

Both end by running `marsh_ingest apply-overrides`, which syncs the note's permission and the MarshLibrary_PublicDomain
folder. Dry run without --apply. Commit and push afterwards, and upload new public PDFs (`python -m utils.site_ftp folder`).
"""
import argparse
import hashlib
import re
import shutil
import sys
from pathlib import Path

from utils import marsh_ingest, pdf_ingest, public_domain, remove_notes
from utils.rename_notes import new_stem
from utils.stub_store import StubStore

FULL_TEXT_DIR = pdf_ingest.BRAIN_DIR / "full_text"
NAME = re.compile(r"^(?P<authors>.+?)\.?\s+(?P<year>(?:1[6-9]|20)\d{2}[a-z]?)\.\s*(?P<title>.+?)\.?$")


def cite_from_name(file_name: str) -> dict:
    stem = Path(file_name).stem.strip()
    m = NAME.match(stem)
    if not m:
        return {"authors": "", "year": "", "title": stem}
    authors = m.group("authors").strip()
    a = re.match(r"^([A-Z][A-Za-z'\-]+)\s+((?:[A-Z]\.?\s*)+)$", authors)  # "Hamman R.L." -> "R. L. Hamman"
    if a:
        initials = " ".join(f"{c}." for c in re.findall(r"[A-Z]", a.group(2)))
        authors = f"{initials} {a.group(1)}"
    return {"authors": authors, "year": m.group("year"), "title": m.group("title").strip()}


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def current_file(row: dict) -> str:
    """The row's file name, or the name of the file with the same content when it was renamed."""
    src = marsh_ingest.source_dir()
    if (src / row["file"]).is_file():
        return row["file"]
    size = int(row.get("bytes") or 0)
    for p in src.glob("*.pdf"):
        if (not size or p.stat().st_size == size) and _sha(p) == row.get("sha256"):
            return p.name
    raise SystemExit(f"{row['code']}: {row['file']} is gone and no file in {src} has the same content.")


def _replace_note(row: dict, note: str, stem: str) -> str:
    old = remove_notes.SOURCES_DIR / row["note"] if row.get("note") else None
    store = StubStore()
    if old and old.is_file():
        remove_notes.clean_stubs(store, [old.stem])
        store.flush()
        remove_notes.drop_titles([old.stem])
    path = remove_notes.SOURCES_DIR / f"{stem}.md"
    path.write_text(note, encoding="utf-8")
    if old and old.is_file() and old.resolve() != path.resolve():
        old.unlink()
    pdf_ingest.update_stubs(stem, note)
    return path.name


def handwritten_note(code: str, cite: dict, file_name: str) -> str:
    title = cite["title"]
    citation = marsh_ingest.format_citation(cite, code)
    fm = {"title": title, "source_id": code, "marsh_id": code, "library": marsh_ingest.LIBRARY,
          "permission": public_domain.PUBLIC, "doc_type": "handwritten_note", "source_citation": citation,
          "source_file": file_name, "text_extraction": "none (handwritten; not machine-readable)"}
    who = cite["authors"] or "an unknown author"
    when = f" ({cite['year']})" if cite["year"] else ""
    body = (f"# {title}\n\n## Executive Summary\n\nHandwritten note by {who}{when}, titled \"{title}\" in the library's "
            "file name. The document is handwritten and cannot be read by OCR, so no summary of its content is "
            "available here. The original scan is linked from the library page.\n\n## Key Findings\n\n"
            "- Not available: handwritten document. Read the original scan.\n")
    return pdf_ingest.set_frontmatter(body, fm)


def cmd_handwritten(args) -> int:
    rows = marsh_ingest.read_catalog()
    by = {r["code"]: r for r in rows}
    for code in args.codes:
        row = by.get(code)
        if not row:
            print(f"{code}: not in the Marsh catalog")
            continue
        name = current_file(row)
        cite = cite_from_name(name)
        stem = new_stem(cite["title"], f"x_{code}")
        print(f"{code}: {name} -> {stem}.md  [{cite['authors']}, {cite['year']}, \"{cite['title']}\"]")
        if not args.apply:
            continue
        note = handwritten_note(code, cite, name)
        row.update(file=name, title=cite["title"], authors=cite["authors"], year=cite["year"], category="correspondence",
                   doc_type="handwritten note", permission_override=public_domain.PUBLIC, confidence="high",
                   reason="Handwritten note (owner's review, 2026-11-10); not machine-readable.",
                   note=_replace_note(row, note, stem), extraction="none (handwritten)")
        marsh_ingest.save_citation(code, {**cite, "citation_source": "filename"})
        public_domain.save_full_text(code, {"text": "Handwritten document; no machine-readable text.", "pages": row.get("pages", ""),
                                             "method": "none (handwritten)"},
                                     {"marsh_id": code, "library": marsh_ingest.LIBRARY, "title": cite["title"],
                                      "source_citation": marsh_ingest.format_citation(cite, code),
                                      "permission": public_domain.PUBLIC, "note": f"[[{Path(row['note']).stem}]]"})
    if args.apply:
        marsh_ingest.write_catalog(rows)
        marsh_ingest.cmd_apply_overrides(None)
    else:
        print("Dry run; add --apply.")
    return 0


def cmd_replace_pdf(args) -> int:
    rows = marsh_ingest.read_catalog()
    row = next((r for r in rows if r["code"] == args.code), None)
    if not row:
        raise SystemExit(f"{args.code}: not in the Marsh catalog")
    src = Path(args.pdf)
    name = args.name or f"{Path(row['file']).stem} (replacement){src.suffix}"
    dest = marsh_ingest.source_dir() / name
    print(f"{args.code}: {src} -> {dest}" + ("; permission public domain" if args.public else ""))
    if not args.apply:
        print("Dry run; add --apply.")
        return 0
    if not dest.is_file():
        shutil.copyfile(src, dest)
    digest = pdf_ingest.file_hash(dest)
    ex = pdf_ingest.extract_text(dest, digest, verbose=False)
    (pdf_ingest.CACHE_DIR / f"{digest[:16]}.json").unlink(missing_ok=True)
    row.update(file=name, sha256=_sha(dest), bytes=str(dest.stat().st_size), pages=str(ex["pages"]),
               extraction=ex["method"])
    if args.public:
        row.update(permission_override=public_domain.PUBLIC, reason=args.reason or row.get("reason", ""))
    perm = marsh_ingest.effective_permission(row)
    head = {"marsh_id": args.code, "library": marsh_ingest.LIBRARY, "title": row.get("title", ""),
            "source_citation": marsh_ingest.format_citation(row, args.code), "permission": perm,
            "note": f"[[{Path(row['note']).stem}]]" if row.get("note") else "", "source_files": [name]}
    public_domain.save_full_text(args.code, ex, head)
    marsh_ingest.remove_from_ftp(args.code)  # the public copy is refreshed from the new file
    marsh_ingest.write_catalog(rows)
    marsh_ingest.cmd_apply_overrides(None)
    print(f"{args.code}: {ex['pages']} pages, {len(ex['text']):,} characters ({ex['method']}). "
          f"Now rebuild the note: python -m utils.rebuild_notes run --ids {args.code}")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    h = sub.add_parser("handwritten")
    h.add_argument("codes", nargs="+")
    h.add_argument("--apply", action="store_true")
    r = sub.add_parser("replace-pdf")
    r.add_argument("code")
    r.add_argument("pdf")
    r.add_argument("--name", default="")
    r.add_argument("--public", action="store_true")
    r.add_argument("--reason", default="")
    r.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    return {"handwritten": cmd_handwritten, "replace-pdf": cmd_replace_pdf}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
