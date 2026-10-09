"""Recover citations for vault notes that have no Minckley-sheet row, from the note text itself.

    python -m utils.recover_citations            # estimate, ask, then recover and save
    python -m utils.recover_citations --report   # show what was recovered / what still has no author or year

Results go to brain_meta/external_citations.json keyed by note filename stem (citation_source "note-llm").
Nothing is invented: an author or year the note does not support is left empty and flagged.
"""
import json
import os
import re
import sys

from utils import brain_citations, brain_index, pdf_ingest

SYSTEM = """You build catalog citations for archival and published documents from an AI-written markdown summary of the document.
Return ONLY a JSON object with these keys:
  "authors": who wrote/sent it. Published works: "First M. Last, First Last". Letters/memos: the sender (person), else the issuing organization. "" if the text does not say.
  "year": 4-digit year the document was written/published, from the text or the filename date. "" if unknown.
  "title": for published works the real title. For letters, memos, minutes and reports without a formal title write a short descriptive title such as "Memo regarding the use of rotenone in the Gila River" or "Letter to Ted Stewart regarding razorback sucker stocking" (recipient only if stated).
  "publication": journal/series/agency report series if stated, else "".
  "type": one of Journal Article, Book, Book Chapter, Report, Letter, Memorandum, Meeting Minutes, Permit Report, Other.
  "confidence": "high" (author and year stated), "medium" (one inferred), or "low" (guesswork).
Never invent a name or a year. The notes are summaries, so wording like "from X to Y" or "dated ..." is the evidence."""

BODY_CHARS = 3500


def _unmatched() -> list:
    refs = brain_citations.load()
    out = []
    for p in sorted(brain_index.SOURCES_DIR.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, _ = brain_index._split_frontmatter(text)
        if not brain_citations.lookup(refs, fm.get("source_id"), p.stem):
            out.append((p, text))
    return out


def _prompt(stem: str, text: str) -> str:
    return f"Filename: {stem}\n\n{text[:BODY_CHARS]}"


def _parse(reply: str) -> dict:
    m = re.search(r"\{.*\}", reply or "", re.S)
    try:
        data = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}
    clean = lambda k: re.sub(r"\s+", " ", str(data.get(k) or "")).strip()
    year = re.search(r"(1[89]|20)\d{2}", clean("year"))
    return {
        "authors": clean("authors"), "year": year.group(0) if year else "", "title": clean("title"),
        "publication": clean("publication"), "type": clean("type"),
        "confidence": clean("confidence").lower() or "low", "citation_source": "note-llm",
    }


def report() -> int:
    ext = json.loads(brain_citations.EXTERNAL_CITATIONS_PATH.read_text(encoding="utf-8"))
    rows = {k: v for k, v in ext.items() if v.get("citation_source") == "note-llm"}
    print(f"{len(rows)} recovered. No author: {sum(1 for v in rows.values() if not v['authors'])}; "
          f"no year: {sum(1 for v in rows.values() if not v['year'])}; low confidence: {sum(1 for v in rows.values() if v.get('confidence') == 'low')}")
    for k, v in sorted(rows.items()):
        flag = "" if v["authors"] and v["year"] else "  <-- " + ("no author " if not v["authors"] else "") + ("no year" if not v["year"] else "")
        print(f"  {k}\n     {v['authors'] or '(none)'} ({v['year'] or 'n.d.'}). {v['title']} [{v.get('confidence')}]{flag}")
    return 0


def main(argv: list) -> int:
    if "--report" in argv:
        return report()
    todo = _unmatched()
    if not todo:
        print("Every source already has a citation.")
        return 0
    model = os.getenv("OPENROUTER_INGEST_MODEL") or os.getenv("OPENROUTER_MODEL") or pdf_ingest.DEFAULT_MODEL
    in_tok = sum(min(len(t), BODY_CHARS) // 4 + len(SYSTEM) // 4 for _, t in todo)
    print(f"{len(todo)} notes without a citation. Model: {model}. {pdf_ingest._cost_text(model, in_tok, len(todo) * 120)}")
    if "--yes" not in argv and input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Cancelled.")
        return 0
    client = pdf_ingest._client()
    path = brain_citations.EXTERNAL_CITATIONS_PATH
    ext = json.loads(path.read_text(encoding="utf-8"))
    for i, (p, text) in enumerate(todo, 1):
        data = _parse(pdf_ingest._chat(client, model, SYSTEM, _prompt(p.stem, text), max_tokens=300))
        if not data.get("title"):
            print(f"[{i}/{len(todo)}] {p.stem}: no usable reply, skipped")
            continue
        ext[p.stem] = data
        path.write_text(json.dumps(ext, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"[{i}/{len(todo)}] {p.stem}: {data['authors'] or '(no author)'} ({data['year'] or 'n.d.'}) [{data['confidence']}]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
