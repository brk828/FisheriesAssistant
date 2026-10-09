"""Builds the Minckley Library reference file (brain_meta/minckley_library.csv) from the curated Excel sheet.

The CSV is the project's single reference for Minckley citations (see brain_citations.py). It keeps the
sheet's columns and adds nothing the sheet did not have. A conservative spell check fixes only
high-confidence typos in title/publication and logs every change to brain_meta/minckley_spellfix_log.csv.

    python -m utils.minckley_reference build [--xlsx FILE] [--no-spellcheck]
    python -m utils.minckley_reference spellcheck      # re-run the spell check on the existing CSV
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_XLSX = BASE_DIR / "00_Fisheries_Brain" / "MinckleyLibrary.xlsx"
REFERENCE_CSV = BASE_DIR / "brain_meta" / "minckley_library.csv"
FIX_LOG = BASE_DIR / "brain_meta" / "minckley_spellfix_log.csv"
COLUMNS = ["year", "MID", "authors", "title", "abstract", "publication", "Minckley Library URL",
           "permission", "type", "External URL", "comments", "library"]
SPELL_FIELDS = ("title", "publication")
_WORD = re.compile(r"[A-Za-z]{6,}")
# Legitimate names/words that look like typos of common words.
KEEP = {"aransas", "opinicon", "powel", "shales", "pices", "browni",
        # Spanish/French/Italian/British spellings, legitimate in non-English titles
        "composicion", "contribucion", "distribucion", "edicion", "problemas", "produccion", "vegetacion",
        "scienze", "lettres", "ressources", "accion", "descripcion", "palaeontology", "mexiko"}


def _interior_edit(typo: str, cand: str) -> bool:
    """True when first and last letters are unchanged, so suffix variants (foreign inflections, taxon
    epithets such as -ae/-i) and first-letter changes (Etter/Letter) never count as typos."""
    return typo[0] == cand[0] and typo[-1] == cand[-1]


def _cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def read_xlsx(path: Path) -> list:
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(wb.worksheets[0].iter_rows(values_only=True))
    header = [_cell(h) for h in rows[0]]
    missing = [c for c in ("MID", "authors", "title", "year") if c not in header]
    if missing:
        raise SystemExit(f"{path.name} is missing expected columns: {missing}")
    out = []
    for r in rows[1:]:
        rec = {h: _cell(v) for h, v in zip(header, r)}
        if rec.get("MID") or rec.get("title"):
            out.append({c: rec.get(c, "") for c in COLUMNS})
    return out


def read_csv(path: Path = REFERENCE_CSV) -> list:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(rows: list, path: Path = REFERENCE_CSV) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)


def spellcheck(rows: list) -> list:
    """Fix a word only when it is (a) lowercase-start, (b) not an English word, (c) rare in this sheet
    (at most twice), (d) one interior edit from exactly one real word that is common in the sheet (10+ uses and at
    least 20x the typo's count). Names, foreign words and taxon epithets are therefore left alone. Returns the change log."""
    from spellchecker import SpellChecker
    sp = SpellChecker()
    counts = Counter()
    for r in rows:
        for f in SPELL_FIELDS:
            counts.update(w.lower() for w in _WORD.findall(r[f]))
    fixes = {}
    for w, n in counts.items():
        if n > 2 or w in sp or w in KEEP:
            continue
        cands = [c for c in sp.edit_distance_1(w) if c in sp and counts.get(c, 0) >= 10 and counts[c] >= 20 * n and _interior_edit(w, c)]
        if len(cands) == 1:
            fixes[w] = cands[0]
    log = []
    for r in rows:
        for f in SPELL_FIELDS:
            def repl(m):
                word = m.group(0)
                fix = fixes.get(word.lower())
                if not fix or word[0].isupper() and not word.islower() and not word.istitle():
                    return word
                new = fix.capitalize() if word[0].isupper() else fix
                log.append({"MID": r["MID"], "field": f, "old": word, "new": new})
                return new
            r[f] = _WORD.sub(repl, r[f])
    return log


def write_log(log: list) -> None:
    with open(FIX_LOG, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["MID", "field", "old", "new"])
        w.writeheader()
        w.writerows(log)


def _main(argv: list) -> int:
    if not argv or argv[0] not in ("build", "spellcheck"):
        print(__doc__)
        return 1
    if argv[0] == "build":
        xlsx = Path(argv[argv.index("--xlsx") + 1]) if "--xlsx" in argv else DEFAULT_XLSX
        rows = read_xlsx(xlsx)
        print(f"Read {len(rows)} rows from {xlsx.name}.")
    else:
        rows = read_csv()
    if "--no-spellcheck" not in argv:
        log = spellcheck(rows)
        write_log(log)
        print(f"Spell check changed {len(log)} words ({len({x['old'] for x in log})} distinct); see {FIX_LOG.name}.")
    write_csv(rows)
    print(f"Wrote {REFERENCE_CSV}.")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
