"""Reference data (authors, year, real title, publication) from the library spreadsheet.

The sheet's MID column matches each vault source's frontmatter `source_id`. The import keeps only the
columns needed for citations, for sources that exist in the vault, in brain_meta/citations.json.
Nothing from the vault is sent anywhere; the sheet is only downloaded.

    python -m utils.brain_citations import                 # download the default sheet
    python -m utils.brain_citations import --file X.csv    # or use a downloaded CSV export
    python -m utils.brain_citations import --url URL
"""
import csv
import io
import json
import re
import sys
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCES_DIR = BASE_DIR / "00_Fisheries_Brain" / "01_Sources"
CITATIONS_PATH = BASE_DIR / "brain_meta" / "citations.json"
SHEET_ID = "1VdcIpJ4rXUVFOwW6i0VvpDJIgZpCgkElMry7sXPEP34"
DEFAULT_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

_PERSON = re.compile(r"\b[A-Z]\.")


def mid_from_source_id(value) -> str:
    """'16522 (scanned)' -> '16522'; '16414, 16415' -> '16414'; '13029 map' -> '13029'."""
    m = re.match(r"\s*(\d+)", str(value or ""))
    return m.group(1) if m else ""


def short_author(authors: str) -> str:
    """Surname form for inline citations: Smith, Smith and Jones, Smith et al.; organizations are kept whole."""
    authors = re.sub(r"\s+", " ", authors or "").strip()
    if not authors:
        return ""
    if not _PERSON.search(authors):
        return authors
    names = [n.strip() for n in re.split(r",\s*|\s+and\s+|\s*&\s*", authors) if n.strip()]
    surnames = [re.sub(r"^(?:[A-Z]\.\s*)+", "", n).strip() or n for n in names]
    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} and {surnames[1]}"
    return f"{surnames[0]} et al."


def load() -> dict:
    try:
        data = json.loads(CITATIONS_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _vault_mids() -> set:
    mids = set()
    for p in SOURCES_DIR.glob("*.md"):
        head = p.read_text(encoding="utf-8", errors="replace")[:2500]
        m = re.search(r"^source_id:\s*\"?([^\"\r\n]+)", head, re.M)
        if m and mid_from_source_id(m.group(1)):
            mids.add(mid_from_source_id(m.group(1)))
    return mids


def _clean(value) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def import_sheet(text: str) -> int:
    wanted = _vault_mids()
    out = {}
    for row in csv.DictReader(io.StringIO(text)):
        mid = mid_from_source_id(row.get("MID"))
        if not mid or mid not in wanted:
            continue
        year = re.search(r"\d{4}", row.get("year") or "")
        entry = {
            "authors": _clean(row.get("authors")),
            "year": year.group(0) if year else "",
            "title": _clean(row.get("title")),
            "publication": _clean(row.get("publication")).strip(" :"),
            "type": _clean(row.get("type")),
        }
        old = out.get(mid)
        # A repeated MID keeps the row with more filled-in fields.
        if old is None or sum(bool(v) for v in entry.values()) > sum(bool(v) for v in old.values()):
            out[mid] = entry
    CITATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    CITATIONS_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    return len(out)


def _main(argv: list) -> int:
    if not argv or argv[0] != "import":
        print(__doc__)
        return 1
    opt = lambda name: argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else ""
    if opt("--file"):
        text = Path(opt("--file")).read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(opt("--url") or DEFAULT_URL, timeout=90) as resp:
            text = resp.read().decode("utf-8")
    n = import_sheet(text)
    print(f"Saved citations for {n} vault sources to {CITATIONS_PATH.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
