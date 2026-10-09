"""Turns non-Minckley PDFs into vault notes, taking the citation from the PDF itself.

Drop PDFs into 00_Fisheries_Brain/pdfs_to_process/ and run:

    python -m utils.pdf_ingest status                 # what is waiting / already done (local only)
    python -m utils.pdf_ingest extract [files...]     # text (OCR where needed) + citation lookup, no LLM
    python -m utils.pdf_ingest process [files...] [--yes] [--limit N] [--model ID] [--no-crossref]
        Full run: shows a token/cost estimate and asks before sending any document text to OpenRouter.

Pipeline per PDF
  1. Text: the PDF's own text layer (pypdf) page by page; pages with no usable text are OCRd
     (Tesseract via pdf2image/Poppler). Result is cached in pdfs_to_process/_extracted/ so OCR runs once.
  2. Citation, best source first: Crossref record for a DOI printed on the first pages (verified against
     the text), then an LLM read of the first page (verified/upgraded through a Crossref title search),
     then the filename ("Hartman 2000 - Title.pdf"). Each entry records where it came from.
  3. Note: LLM synthesis in the same layout as the existing 01_Sources notes. Frontmatter gets `title`,
     `source_id` (X-<8 hex of the file hash>, so it can never collide with a numeric Minckley MID),
     `source_citation`, `doi`, `source_file`, `text_extraction`.
  4. Citation fields go to brain_meta/external_citations.json (keyed by source_id), merged by
     brain_citations.load(); the Minckley sheet import never touches that file.
  5. Concept stubs: every [[link]] in the note gets its 02_Brain stub updated (a Mentioned In entry and a short
     Context excerpt), or a new stub if none exists. The search index finds sources through these stubs, so
     without this step a new note would not surface for a topic question. No LLM involved.
  6. brain_meta/ingest_manifest.json records each file (by hash) so reruns skip finished work.

Also: python -m utils.pdf_ingest stubs [note stems...]   (re)applies step 5 to ingested notes; safe to repeat.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BRAIN_DIR = BASE_DIR / "00_Fisheries_Brain"
PDF_DIR = BRAIN_DIR / "pdfs_to_process"
CACHE_DIR = PDF_DIR / "_extracted"
SOURCES_DIR = BRAIN_DIR / "01_Sources"
STUBS_DIR = BRAIN_DIR / "02_Brain"
META_DIR = BASE_DIR / "brain_meta"
EXTERNAL_CITATIONS_PATH = META_DIR / "external_citations.json"
MANIFEST_PATH = META_DIR / "ingest_manifest.json"

ID_PREFIX = "X-"
MIN_PAGE_CHARS = 80  # fewer characters than this on a page means "no text layer"; OCR it
OCR_DPI = 200
MAX_NOTE_CHARS = 90_000
CITE_SAMPLE_CHARS = 3500
NOTE_OUT_TOKENS = 3000
DEFAULT_MODEL = "anthropic/claude-sonnet-4.5"
USER_AGENT = "FisheriesAssistant/1.0 (literature ingest; mailto:none)"

NOTE_SYSTEM = """You are an aquatic ecologist and expert ichthyologist, and a data architect. Extract scientific data from the provided document text and output a highly structured Markdown note optimized for Obsidian. The source may focus on fish or on the broader aquatic ecosystem (invertebrates, plankton, water chemistry, habitat); stay faithful to what it actually covers.

Strictly follow this format:
1. YAML frontmatter at the very top with: species (scientific name or list), common_name, family, habitat, ocean_basin, location, and tags. Use "N/A" for fields the document does not address. Do NOT include title, source_id or citation fields; they are added separately.
2. A single `# Title` heading, then Obsidian tags on one line: #ichthyology #marine-biology #<specific-family-or-taxon>. For non-fish taxa tag that taxon instead.
3. Standardized sections: ## Executive Summary, ## Background & Description, ## Ecological & Environmental Context, ## Key Findings.
4. Use [[Double Brackets]] to cross-link related concepts (species, places, methods), always in Title Case, e.g. [[Largemouth Bass]].
5. Report numbers, sample sizes and statistics exactly as given; never invent data. Skip figure/table debris.

The text may come from OCR; silently fix obvious scan errors (e.g. 'f1sh' -> 'fish'). Return ONLY raw Markdown."""

CITE_SYSTEM = """You read the first page of a scientific document and report its bibliographic details. Reply with only a JSON object with these keys (use "" when not stated on the page; never guess):
"title", "authors" (format 'K. J. Hartman, C. D. Smith': initials then surname, comma-separated; an organization name if there are no personal authors), "year" (4 digits), "publication" (journal/series/report series name only), "volume", "issue", "pages", "doi", "document_type" (Journal Article, Report, Thesis, Book Chapter, Letter, Other)."""

REQUIRED_HEADERS = ("## Executive Summary", "## Key Findings")


# ------------------------------------------------------------------ helpers
def _load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def source_id_for(digest: str) -> str:
    return ID_PREFIX + digest[:8]


def _norm(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", (text or "").lower()).split())


def _similar(a: str, b: str) -> float:
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def list_pdfs(names: list = None) -> list:
    if names:
        out = []
        for n in names:
            p = Path(n)
            p = p if p.is_file() else PDF_DIR / n
            if p.is_file():
                out.append(p)
            else:
                print(f"Not found: {n}")
        return out
    return sorted(PDF_DIR.glob("*.pdf"), key=lambda p: p.name.lower())


# --------------------------------------------------------------- extraction
def find_tesseract() -> str:
    """Path to the Tesseract executable: TESSERACT_CMD, then PATH, then the usual Windows install folders."""
    import shutil
    env = os.getenv("TESSERACT_CMD")
    if env and Path(env).is_file():
        return env
    found = shutil.which("tesseract")
    if found:
        return found
    for root in (os.getenv("ProgramFiles"), os.getenv("ProgramFiles(x86)"), os.getenv("LOCALAPPDATA")):
        cand = Path(root, "Tesseract-OCR", "tesseract.exe") if root else None
        if cand and cand.is_file():
            return str(cand)
    return ""


def find_poppler() -> tuple:
    """(found, bin folder to pass to pdf2image or '' when it is on PATH): POPPLER_PATH, PATH, then winget's folder."""
    import shutil
    env = os.getenv("POPPLER_PATH")
    if env and any((Path(env) / n).is_file() for n in ("pdftoppm", "pdftoppm.exe")):
        return True, env
    if shutil.which("pdftoppm"):
        return True, ""
    local = os.getenv("LOCALAPPDATA")
    if local:
        for hit in Path(local, "Microsoft", "WinGet", "Packages").glob("*oschwartz10612.Poppler*/**/pdftoppm.exe"):
            return True, str(hit.parent)
    return False, ""


def _ocr_page(path: Path, page_no: int) -> str:
    import pytesseract
    from pdf2image import convert_from_path

    exe = find_tesseract()
    if exe:
        pytesseract.pytesseract.tesseract_cmd = exe
    images = convert_from_path(
        str(path), dpi=OCR_DPI, first_page=page_no, last_page=page_no, poppler_path=find_poppler()[1] or None
    )
    return "\n".join(pytesseract.image_to_string(im) for im in images)


def extract_text(path: Path, digest: str, verbose: bool = True) -> dict:
    """Returns {"text", "pages", "ocr_pages", "method", "metadata"}; cached by file hash."""
    cache = CACHE_DIR / f"{digest[:16]}.json"
    cached = _load_json(cache)
    if cached.get("text"):
        return cached
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    try:
        meta = {k.lstrip("/").lower(): str(v) for k, v in (reader.metadata or {}).items()}
    except Exception:
        meta = {}
    parts, ocr_pages = [], []
    for i, page in enumerate(reader.pages, 1):
        try:
            text = (page.extract_text() or "").strip()
        except Exception:
            text = ""
        if len(text) < MIN_PAGE_CHARS:
            if verbose and sys.stdout.isatty():
                print(f"   OCR page {i}/{len(reader.pages)}", end="\r", flush=True)
            try:
                text = _ocr_page(path, i).strip() or text
                ocr_pages.append(i)
            except Exception as e:
                if not ocr_pages and i == 1:
                    raise RuntimeError(
                        f"OCR unavailable ({e}). Install Tesseract and Poppler (apt install tesseract-ocr poppler-utils; "
                        "on Windows set TESSERACT_CMD and POPPLER_PATH) and `pip install pytesseract pdf2image`."
                    )
        parts.append(f"\n--- Page {i} ---\n{text}")
    if verbose and ocr_pages:
        print(f"   OCR'd {len(ocr_pages)} of {len(reader.pages)} pages" + " " * 10)
    n = len(reader.pages)
    method = "ocr" if len(ocr_pages) == n else "mixed" if ocr_pages else "text"
    result = {"text": "".join(parts), "pages": n, "ocr_pages": ocr_pages, "method": method, "metadata": meta}
    if len(re.sub(r"\W", "", result["text"].replace("--- Page", ""))) > 200:
        _save_json(cache, result)
    return result


# ----------------------------------------------------------------- citation
_DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.I)


def find_doi(text: str, metadata: dict) -> str:
    candidates = [metadata.get("doi", ""), metadata.get("subject", ""), text[:6000]]
    for blob in candidates:
        m = _DOI.search(blob or "")
        if m:
            return m.group(1).rstrip(".,;)]}>")
    return ""


def _http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def _initials(given: str) -> str:
    return " ".join(f"{p[0]}." for p in re.split(r"[\s\-]+", given.strip()) if p and p[0].isalpha())


def _crossref_entry(item: dict) -> dict:
    authors = []
    for a in item.get("author", []):
        if a.get("family"):
            authors.append(f"{_initials(a.get('given', ''))} {a['family']}".strip())
        elif a.get("name"):
            authors.append(a["name"])
    year = ""
    for key in ("issued", "published-print", "published-online", "created"):
        parts = (item.get(key) or {}).get("date-parts") or [[None]]
        if parts[0] and parts[0][0]:
            year = str(parts[0][0])
            break
    container = (item.get("container-title") or [""])[0]
    vol, issue, pages = item.get("volume", ""), item.get("issue", ""), item.get("page", "")
    pub = container
    if vol:
        pub += f" {vol}" + (f"({issue})" if issue else "")
    if pages:
        pub += f": {pages}"
    kind = {"journal-article": "Journal Article", "book-chapter": "Book Chapter", "report": "Report"}.get(item.get("type", ""), "")
    return {
        "authors": ", ".join(authors),
        "year": year,
        "title": re.sub(r"<[^>]+>", "", (item.get("title") or [""])[0]).strip(),
        "publication": (pub.strip() + ".") if pub.strip() else "",
        "type": kind,
        "doi": item.get("DOI", ""),
        "citation_source": "crossref",
    }


def crossref_by_doi(doi: str, text: str) -> dict:
    """Crossref record for a DOI, accepted only if its title is actually on the first pages."""
    try:
        item = _http_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]
    except Exception:
        return {}
    entry = _crossref_entry(item)
    words = [w for w in _norm(entry["title"]).split() if len(w) > 3]
    head = _norm(text[:8000])
    if not words or sum(w in head for w in words) / len(words) < 0.5:
        return {}
    return entry


def crossref_by_title(title: str, authors: str, year: str) -> dict:
    if len(title) < 15:
        return {}
    q = urllib.parse.urlencode({"query.bibliographic": f"{title} {authors} {year}".strip(), "rows": 1})
    try:
        items = _http_json(f"https://api.crossref.org/works?{q}")["message"]["items"]
    except Exception:
        return {}
    if not items:
        return {}
    entry = _crossref_entry(items[0])
    if _similar(entry["title"], title) < 0.85:
        return {}
    if year and entry["year"] and abs(int(year) - int(entry["year"])) > 1:
        return {}
    return entry


def citation_from_filename(path: Path) -> dict:
    """'Hartman 2000 - The influence of size.pdf' -> author surname, year, (title if after a dash)."""
    stem = path.stem
    year = re.search(r"\b(1[89]\d\d|20\d\d)\b", stem)
    entry = {"authors": "", "year": year.group(1) if year else "", "title": "", "publication": "", "type": "", "citation_source": "filename"}
    m = re.match(r"\s*([A-Z][\w'\-]+(?:\s+et\s+al\.?)?)", stem)
    if m and year:
        entry["authors"] = m.group(1).strip()
    if " - " in stem:
        entry["title"] = stem.split(" - ", 1)[1].strip()
    return entry


def _merge(*entries: dict) -> dict:
    """Earlier entries win field by field; citation_source is that of the entry that supplied the title (else the first)."""
    merged = {}
    for e in entries:
        for k, v in (e or {}).items():
            if v and not merged.get(k):
                merged[k] = v
    merged.setdefault("citation_source", "")
    merged["citation_source"] = next((e["citation_source"] for e in entries if e and e.get("title") and e.get("citation_source")), merged["citation_source"])
    return merged


def free_citation(path: Path, ex: dict, use_crossref: bool) -> dict:
    """Everything that can be learned without an LLM."""
    doi = find_doi(ex["text"], ex["metadata"])
    cross = crossref_by_doi(doi, ex["text"]) if doi and use_crossref else {}
    meta_title = ex["metadata"].get("title", "")
    meta = {}
    if meta_title and not re.search(r"\.(pdf|docx?)$|^untitled|microsoft", meta_title, re.I) and len(meta_title) > 10:
        meta = {"title": meta_title, "authors": ex["metadata"].get("author", ""), "citation_source": "pdf-metadata"}
    return _merge(cross, meta, citation_from_filename(path), {"doi": doi} if doi else {})


def llm_citation(client, model: str, text: str) -> dict:
    reply = _chat(client, model, CITE_SYSTEM, text[:CITE_SAMPLE_CHARS], max_tokens=400)
    m = re.search(r"\{.*\}", reply or "", re.S)
    try:
        data = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}
    clean = lambda k: re.sub(r"\s+", " ", str(data.get(k) or "")).strip()
    year = re.search(r"\d{4}", clean("year"))
    pub = clean("publication")
    vol, issue, pages = clean("volume"), clean("issue"), clean("pages")
    if pub and vol:
        pub += f" {vol}" + (f"({issue})" if issue else "")
    if pub and pages:
        pub += f": {pages}"
    return {
        "title": clean("title"),
        "authors": clean("authors"),
        "year": year.group(0) if year else "",
        "publication": (pub + ".") if pub else "",
        "type": clean("document_type"),
        "doi": clean("doi"),
        "citation_source": "llm",
    }


# --------------------------------------------------------------------- LLM
def _client():
    try:
        from dotenv import load_dotenv
        load_dotenv(BASE_DIR / ".env")
    except ImportError:
        pass
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set (see .env.template).")
    from openai import OpenAI
    return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)


def _chat(client, model: str, system: str, user: str, max_tokens: int, tries: int = 3) -> str:
    import time
    last = None
    for attempt in range(tries):
        try:
            r = client.chat.completions.create(
                model=model, temperature=0, max_tokens=max_tokens,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            )
            return r.choices[0].message.content or ""
        except Exception as e:  # network / rate limit: back off and retry
            last = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"LLM request failed: {last}")


def _strip_fence(text: str) -> str:
    text = (text or "").strip()
    m = re.match(r"^```(?:markdown|md)?\s*\n(.*?)\n```\s*$", text, re.S)
    return (m.group(1) if m else text).strip()


def synthesize_note(client, model: str, text: str) -> str:
    body = text[:MAX_NOTE_CHARS]
    for _ in range(2):
        note = _strip_fence(_chat(client, model, NOTE_SYSTEM, body, max_tokens=NOTE_OUT_TOKENS + 1500))
        if note.startswith("---") and all(h in note for h in REQUIRED_HEADERS):
            return note
    raise RuntimeError("model did not return a complete note (missing frontmatter or required sections)")


# --------------------------------------------------------------------- note
def _yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def set_frontmatter(note: str, fields: dict) -> str:
    """Replaces/adds the given keys in the note's frontmatter, leaving the rest alone."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", note, re.S)
    existing, rest = (m.group(1), note[m.end():]) if m else ("", note)
    lines = [ln for ln in existing.splitlines() if ln.split(":", 1)[0].strip() not in fields]
    lines += [f"{k}: {_yaml(v)}" for k, v in fields.items() if v]
    return "---\n" + "\n".join(lines) + "\n---\n" + rest.lstrip("\n")


def format_citation(c: dict) -> str:
    who = c.get("authors") or "Unknown author"
    year = c.get("year") or "n.d."
    tail = " ".join(x for x in (c.get("title", "").rstrip("."), ) if x)
    pub = c.get("publication", "")
    return f"{who} ({year}). {tail}." + (f" {pub}" if pub else "")


def note_stem(title: str, year: str, sid: str) -> str:
    letters = re.sub(r"[^A-Za-z ]", "", title or "").title().replace(" ", "")[:30] or "Untitled"
    stem = f"{letters}_{year or sid}"
    if (SOURCES_DIR / f"{stem}.md").exists():
        stem = f"{stem}_{sid}"
    return stem


def note_title(note: str) -> str:
    m = re.search(r"^# (.+)$", note, re.M)
    return m.group(1).strip() if m else ""


# -------------------------------------------------------------------- stubs
_WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
_STUB_BAD_CHARS = re.compile(r'[\\/*?:"<>|]')
EXCERPT_CHARS = 300


def _excerpt(note: str) -> str:
    m = re.search(r"^## Executive Summary\s*\n(.*?)(?=^## |\Z)", note, re.S | re.M)
    text = _WIKILINK.sub(lambda x: x.group(0), m.group(1) if m else "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > EXCERPT_CHARS:
        text = text[:EXCERPT_CHARS].rsplit(" ", 1)[0] + "..."
    return text


def _stub_index() -> dict:
    return {p.stem.lower(): p for p in STUBS_DIR.glob("*.md")} if STUBS_DIR.exists() else {}


def update_stubs(stem: str, note: str, index: dict = None) -> tuple:
    """Adds the note to the stub of every concept it links; returns (updated, created) counts."""
    index = _stub_index() if index is None else index
    excerpt = _excerpt(note)
    quote = f"> {excerpt}\n> -- *[[{stem}]]*\n" if excerpt else ""
    names = list(dict.fromkeys(n.strip() for n in _WIKILINK.findall(note) if n.strip() and n.strip() != stem))
    updated = created = 0
    STUBS_DIR.mkdir(parents=True, exist_ok=True)
    for name in names:
        if _STUB_BAD_CHARS.search(name) or len(name) > 100:
            continue
        path = index.get(name.lower())
        if path is None:
            path = STUBS_DIR / f"{name}.md"
            path.write_bytes(f"---\ntype: concept\n---\n# {name}\n\n## Context\n\n## Mentioned In\n".replace("\n", "\r\n").encode("utf-8"))
            index[name.lower()] = path
            created += 1
        raw = path.read_bytes().decode("utf-8", errors="replace")
        eol = "\r\n" if "\r\n" in raw else "\n"  # the vault's stubs use CRLF; keep each file's own style
        text = raw.replace("\r\n", "\n")
        link = f"- [[{stem}]]"
        mentions = re.search(r"^## Mentioned In\s*\n(.*)\Z", text, re.S | re.M)
        if mentions and link in mentions.group(1).splitlines():
            continue
        if quote:
            if re.search(r"^## Context\s*$", text, re.M):
                text = re.sub(r"^## Mentioned In\s*$", lambda _m: quote.rstrip("\n") + "\n\n## Mentioned In", text, count=1, flags=re.M) \
                    if re.search(r"^## Mentioned In\s*$", text, re.M) else text
            else:
                text = re.sub(r"^## Mentioned In\s*$", lambda _m: "## Context\n" + quote + "\n## Mentioned In", text, count=1, flags=re.M)
        if re.search(r"^## Mentioned In\s*$", text, re.M):
            text = text.rstrip("\n") + f"\n{link}\n"
        else:
            text = text.rstrip("\n") + f"\n\n## Mentioned In\n{link}\n"
        path.write_bytes(text.replace("\n", eol).encode("utf-8"))
        updated += 1
    return updated, created


def cmd_stubs(args) -> int:
    manifest = _load_json(MANIFEST_PATH)
    stems = [Path(a).stem for a in args.notes] or [r["note"][:-3] for r in manifest.values() if r.get("status") == "done"]
    index = _stub_index()
    for stem in stems:
        path = SOURCES_DIR / f"{stem}.md"
        if not path.is_file():
            print(f"Not found: {path.name}")
            continue
        u, c = update_stubs(stem, path.read_text(encoding="utf-8"), index)
        print(f"{stem}: {u} stubs updated ({c} new)")
    return 0


# --------------------------------------------------------------------- main
def _price(model: str):
    from utils import brain_enrich
    return brain_enrich._model_price(model)


def cmd_status(_args) -> int:
    manifest = _load_json(MANIFEST_PATH)
    pdfs = list_pdfs()
    if not pdfs:
        print(f"No PDFs in {PDF_DIR}")
        return 0
    for p in pdfs:
        d = file_hash(p)
        rec = manifest.get(d)
        state = f"done -> {rec['note']}" if rec and rec.get("status") == "done" else (f"failed: {rec.get('reason')}" if rec else "waiting")
        print(f"{source_id_for(d)}  {p.name}\n    {state}")
    return 0


def cmd_extract(args) -> int:
    for p in list_pdfs(args.files):
        d = file_hash(p)
        print(f"{p.name}")
        ex = extract_text(p, d)
        c = free_citation(p, ex, not args.no_crossref)
        print(f"   {ex['pages']} pages, method={ex['method']}, ocr_pages={len(ex['ocr_pages'])}, chars={len(ex['text']):,}")
        print(f"   citation ({c.get('citation_source') or 'none'}): {json.dumps({k: v for k, v in c.items() if v}, ensure_ascii=False)}")
        lines = [ln.strip() for ln in ex["text"].splitlines() if ln.strip() and not ln.startswith("--- Page")]
        print(f"   first lines: {' | '.join(lines[:3])[:200]}")
    return 0


def cmd_process(args) -> int:
    manifest = _load_json(MANIFEST_PATH)
    todo = []
    for p in list_pdfs(args.files):
        d = file_hash(p)
        if manifest.get(d, {}).get("status") == "done":
            print(f"Skipping {p.name} (already processed as {manifest[d]['note']})")
            continue
        todo.append((p, d))
    if args.limit:
        todo = todo[: args.limit]
    if not todo:
        print("Nothing to process.")
        return 0

    print(f"Preparing {len(todo)} PDF(s): extracting text (OCR where needed) and looking up citations.")
    prepared = []
    for p, d in todo:
        print(f"-> {p.name}")
        try:
            ex = extract_text(p, d)
        except Exception as e:
            print(f"   FAILED extraction: {e}")
            manifest[d] = _record(p, d, "failed", reason=f"extraction: {e}")
            continue
        cite = free_citation(p, ex, not args.no_crossref)
        print(f"   {ex['pages']} pages, text={ex['method']}, citation so far: {cite.get('citation_source') or 'none'}")
        prepared.append((p, d, ex, cite))
    _save_json(MANIFEST_PATH, manifest)
    if not prepared:
        return 1

    model = args.model or os.getenv("OPENROUTER_INGEST_MODEL") or os.getenv("OPENROUTER_MODEL") or DEFAULT_MODEL
    in_tok = sum(min(len(ex["text"]), MAX_NOTE_CHARS) // 4 + len(NOTE_SYSTEM) // 4 + 1200 for _, _, ex, _ in prepared)
    out_tok = len(prepared) * (NOTE_OUT_TOKENS + 150)
    price = _price(model)
    cost = f"about ${in_tok * price[0] + out_tok * price[1]:.2f}" if price else "price unavailable (check openrouter.ai/models)"
    print(f"\nModel: {model}\nEstimated usage: ~{in_tok:,} input + ~{out_tok:,} output tokens; {cost}.")
    print("This sends the full text of each document (and its first page for citation reading) to OpenRouter.")
    if not args.yes and input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Cancelled; nothing was sent.")
        return 0

    client = _client()
    citations = _load_json(EXTERNAL_CITATIONS_PATH)
    done = 0
    for p, d, ex, cite in prepared:
        sid = source_id_for(d)
        print(f"-> {p.name} [{sid}]")
        try:
            if cite.get("citation_source") != "crossref":
                llm = llm_citation(client, model, ex["text"])
                upgraded = crossref_by_title(llm.get("title", ""), llm.get("authors", ""), llm.get("year", "")) if llm and not args.no_crossref else {}
                cite = _merge(upgraded, llm, cite)
            note = synthesize_note(client, model, ex["text"])
            title = cite.get("title") or note_title(note) or p.stem
            cite["title"] = title
            stem = note_stem(title, cite.get("year", ""), sid)
            note = set_frontmatter(note, {
                "title": title,
                "source_id": sid,
                "source_citation": format_citation(cite),
                "doi": cite.get("doi", ""),
                "source_file": p.name,
                "text_extraction": ex["method"],
            })
            SOURCES_DIR.mkdir(parents=True, exist_ok=True)
            (SOURCES_DIR / f"{stem}.md").write_text(note, encoding="utf-8")
            upd, new = update_stubs(stem, note)
            citations[sid] = {k: cite.get(k, "") for k in ("authors", "year", "title", "publication", "type", "doi", "citation_source")}
            _save_json(EXTERNAL_CITATIONS_PATH, citations)
            manifest[d] = _record(p, d, "done", note=f"{stem}.md", method=ex["method"], citation_source=cite.get("citation_source", ""))
            done += 1
            print(f"   wrote {stem}.md, {upd} concept stubs updated ({new} new)  (citation: {cite.get('citation_source') or 'none'}; {cite.get('authors') or '?'} {cite.get('year') or '?'})")
        except Exception as e:
            print(f"   FAILED: {e}")
            manifest[d] = _record(p, d, "failed", reason=str(e))
        _save_json(MANIFEST_PATH, manifest)
    print(f"\n{done}/{len(prepared)} notes written to {SOURCES_DIR}. Citations that came from the filename or an LLM read are worth a glance in {EXTERNAL_CITATIONS_PATH.name}.")
    return 0 if done == len(prepared) else 1


def _record(path: Path, digest: str, status: str, **extra) -> dict:
    return {"file": path.name, "source_id": source_id_for(digest), "status": status,
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"), **extra}


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(prog="pdf_ingest", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sp = sub.add_parser("stubs")
    sp.add_argument("notes", nargs="*", help="note stems in 01_Sources; default is every ingested note")
    for name in ("extract", "process"):
        sp = sub.add_parser(name)
        sp.add_argument("files", nargs="*", help="PDF names (in pdfs_to_process) or paths; default is all")
        sp.add_argument("--no-crossref", action="store_true", help="do not query Crossref (DOI / title lookups)")
        if name == "process":
            sp.add_argument("--yes", action="store_true", help="skip the cost confirmation")
            sp.add_argument("--limit", type=int, default=0)
            sp.add_argument("--model", default="")
    args = ap.parse_args(argv)
    return {"status": cmd_status, "stubs": cmd_stubs, "extract": cmd_extract, "process": cmd_process}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
