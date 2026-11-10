"""Remove source notes from the Fisheries Brain, with their stub links.

    python -m utils.remove_notes STEM [STEM ...]            dry run: shows what would change
    python -m utils.remove_notes STEM [STEM ...] --apply    deletes the notes and cleans the stubs

A STEM is a note file name without .md (for example BonytailsInUpperVerde_11948) or just its ID (11948, PML0123,
FAL0001), which is matched against the `_<ID>.md` suffix. For each note this:
  * deletes 01_Sources/<stem>.md;
  * removes its `[[stem]]` line from every stub's Mentioned In list and every Context excerpt that cites it;
  * deletes stubs left with no Mentioned In entry (concepts that only that note created);
  * drops the note's entry from brain_meta/source_titles.json;
  * deletes full_text/<ID>.md when --full-text is given (kept by default: it is local only).
It does not touch the library spreadsheets, the work lists (so removed IDs are not fed to ingest again), the
citation files or the website PDF folder; a public-domain PDF already uploaded stays on the server until it is
removed there. The search index rebuilds itself on the next search. Commit and push afterwards so the site drops it.
"""
import argparse
import re
import sys
from pathlib import Path

from utils import pdf_ingest
from utils.stub_store import LETTERS, StubStore, bucket

SOURCES_DIR = pdf_ingest.SOURCES_DIR
FULL_TEXT_DIR = pdf_ingest.BRAIN_DIR / "full_text"


def resolve(arg: str) -> Path:
    p = SOURCES_DIR / (arg if arg.endswith(".md") else f"{arg}.md")
    if p.is_file():
        return p
    hits = sorted(SOURCES_DIR.glob(f"*_{arg}.md"))
    if len(hits) == 1:
        return hits[0]
    raise SystemExit(f"{arg}: {'no note found' if not hits else 'more than one note: ' + ', '.join(h.name for h in hits)}")


def _link(stem: str) -> re.Pattern:
    return re.compile(r"\[\[" + re.escape(stem) + r"(\|[^\]]*)?(#[^\]]*)?\]\]")


def clean_stubs(store: StubStore, stems: list) -> tuple:
    """Returns (stubs edited, stubs deleted, context excerpts dropped); changes stay in `store` until flush()."""
    pats = [_link(s) for s in stems]
    hit = lambda text: any(p.search(text) for p in pats)
    edited, deleted, excerpts = [], [], 0
    for letter in LETTERS:
        stubs = store._load(letter)
        for key in list(stubs):
            stub = stubs[key]
            mentions = [m for m in stub.mentions if not hit(m)]
            blocks = re.split(r"\n\s*\n", stub.context) if stub.context else []
            keep = [b for b in blocks if not hit(b)]
            if len(mentions) == len(stub.mentions) and len(keep) == len(blocks):
                continue
            excerpts += len(blocks) - len(keep)
            store._dirty.add(letter)
            if not mentions:
                del stubs[key]
                deleted.append(stub.name)
                continue
            stub.mentions = mentions
            stub.context = "\n\n".join(keep)
            edited.append(stub.name)
    return edited, deleted, excerpts


def drop_titles(stems: list) -> int:
    """Removes the notes' entries from source_titles.json as text, so the rest of the file keeps its layout."""
    path = pdf_ingest.BASE_DIR / "brain_meta" / "source_titles.json"
    if not path.is_file():
        return 0
    text = path.read_text(encoding="utf-8")
    n = 0
    for s in stems:
        text, k = re.subn(r'\s*"' + re.escape(s) + r'": \{[^{}]*\},?', "", text, count=1)
        n += k
    if n:
        text = re.sub(r",(\s*\})\s*$", r"\1\n", text)  # a trailing comma left by removing the last entry
        path.write_text(text, encoding="utf-8")
    return n


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("notes", nargs="+")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--full-text", action="store_true", help="also delete full_text/<ID>.md")
    args = ap.parse_args(argv)
    paths = [resolve(a) for a in args.notes]
    stems = [p.stem for p in paths]
    store = StubStore()
    store.require_consolidated()
    edited, deleted, excerpts = clean_stubs(store, stems)
    for p in paths:
        print(f"note: {p.name}")
    print(f"stubs edited: {len(edited)}; excerpts dropped: {excerpts}")
    print(f"stubs deleted (no other source): {len(deleted)}" + (f" -> {', '.join(sorted(deleted))}" if deleted else ""))
    texts = []
    if args.full_text:
        for s in stems:
            t = FULL_TEXT_DIR / f"{s.rsplit('_', 1)[-1]}.md"
            if t.is_file():
                texts.append(t)
                print(f"full text: {t.name}")
    if not args.apply:
        print("Dry run; add --apply to make these changes.")
        return 0
    store.flush()
    drop_titles(stems)
    for p in paths + texts:
        p.unlink()
    print("Done. Commit and push 01_Sources and 02_Brain so the website drops these notes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
