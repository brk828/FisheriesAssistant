"""Local search index over the Obsidian vault (00_Fisheries_Brain).

Navigation order is stubs first (02_Brain concept notes: summary, related concepts,
"Mentioned In" source ids), then source excerpts. Everything runs locally in SQLite FTS5;
no tokens are spent until the compact result is handed to the LLM.

Rebuild manually with:  python -m utils.brain_index
"""
import json
import math
import re
import sqlite3
import sys
from pathlib import Path

import yaml

from utils import brain_enrich

BASE_DIR = Path(__file__).resolve().parent.parent
BRAIN_DIR = BASE_DIR / "00_Fisheries_Brain"
SOURCES_DIR = BRAIN_DIR / "01_Sources"
STUBS_DIR = BRAIN_DIR / "02_Brain"
DB_PATH = BASE_DIR / ".brain_index.sqlite"

SCHEMA_VERSION = "2"
CHUNK_CHARS = 1500
MAX_STUBS = 5
MAX_EXCERPTS = 4
SUMMARY_CHARS = 320
EXCERPT_CHARS = 700
RELATED_SHOWN = 6
MENTIONS_SHOWN = 5

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "in", "is", "it", "its",
    "of", "on", "or", "that", "the", "this", "to", "was", "were", "what", "when", "where", "which",
    "with", "about", "does", "do", "can", "tell", "me", "any", "there",
}

_WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
_META_FIELDS = ("species", "family", "habitat", "region", "location", "study_type", "document_type", "tags")


def _signature() -> str:
    count, newest, total = 0, 0.0, 0
    for folder in (STUBS_DIR, SOURCES_DIR):
        if not folder.exists():
            continue
        for p in folder.glob("*.md"):
            st = p.stat()
            count += 1
            newest = max(newest, st.st_mtime)
            total += st.st_size
    return f"{SCHEMA_VERSION}:{count}:{int(newest)}:{total}:{brain_enrich.metadata_signature()}"


def _split_frontmatter(text: str):
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        data = {}
    return (data if isinstance(data, dict) else {}), text[m.end():]


def _flatten(value) -> str:
    if isinstance(value, (list, tuple)):
        return "; ".join(str(v) for v in value)
    return "" if value is None else str(value)


def _section(body: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def _parse_stub(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    _, body = _split_frontmatter(text)
    t = re.search(r"^# (.+)$", body, re.M)
    title = t.group(1).strip() if t else path.stem
    summary = _section(body, "Summary")
    context = _section(body, "Context")
    mentions = list(dict.fromkeys(_WIKILINK.findall(_section(body, "Mentioned In"))))
    related = []
    for line in context.splitlines():
        if line.startswith("> **Related concepts:**"):
            related += _WIKILINK.findall(line)
    related = [r for r in dict.fromkeys(related) if r.lower() != title.lower()]
    # Keep the FTS text focused: strip links and attribution lines from context.
    ctx_text = "\n".join(l for l in context.splitlines() if not l.startswith("> --"))
    ctx_text = _WIKILINK.sub(lambda m: m.group(1), ctx_text)
    return title, summary, ctx_text, related, mentions


_TAG_LINE = re.compile(r"^(?:#[\w\-]+\s*)+$", re.M)


def _chunks(body: str):
    """Yields (heading, text) pieces of at most ~CHUNK_CHARS, split on headings then paragraphs."""
    body = _TAG_LINE.sub("", body)
    parts = re.split(r"^(#{1,4} .+)$", body, flags=re.M)
    heading, current = "", parts[0]
    pieces = []
    for i in range(1, len(parts), 2):
        pieces.append((heading, current))
        heading, current = parts[i].lstrip("# ").strip(), parts[i + 1]
    pieces.append((heading, current))
    for head, text in pieces:
        text = text.strip()
        if not text:
            continue
        buf = ""
        for para in re.split(r"\n\s*\n", text):
            if buf and len(buf) + len(para) > CHUNK_CHARS:
                yield head, buf
                buf = ""
            while len(para) > CHUNK_CHARS * 2:
                yield head, para[:CHUNK_CHARS]
                para = para[CHUNK_CHARS:]
            buf = f"{buf}\n\n{para}" if buf else para
        if buf:
            yield head, buf


def build_index(verbose: bool = True) -> None:
    brain_enrich.ensure()
    titles = brain_enrich.load_titles()
    tmp = DB_PATH.with_suffix(".building")
    tmp.unlink(missing_ok=True)
    db = sqlite3.connect(tmp)
    db.executescript(
        """
        CREATE TABLE stubs(id INTEGER PRIMARY KEY, title TEXT, title_lc TEXT, summary TEXT,
                           related TEXT, mentions TEXT, n_mentions INTEGER);
        CREATE VIRTUAL TABLE stubs_fts USING fts5(title, summary, context, tokenize='porter unicode61 remove_diacritics 2');
        CREATE TABLE sources(source_id TEXT PRIMARY KEY, title TEXT, year TEXT, meta TEXT);
        CREATE VIRTUAL TABLE chunks_fts USING fts5(source_id UNINDEXED, heading, body, tokenize='porter unicode61 remove_diacritics 2');
        CREATE TABLE info(key TEXT PRIMARY KEY, value TEXT);
        """
    )
    n_stubs = n_sources = 0
    for p in sorted(STUBS_DIR.glob("*.md")) if STUBS_DIR.exists() else []:
        try:
            title, summary, ctx, related, mentions = _parse_stub(p)
        except OSError:
            continue
        cur = db.execute(
            "INSERT INTO stubs(title, title_lc, summary, related, mentions, n_mentions) VALUES (?,?,?,?,?,?)",
            (title, title.lower(), summary, json.dumps(related), json.dumps(mentions), len(mentions)),
        )
        db.execute("INSERT INTO stubs_fts(rowid, title, summary, context) VALUES (?,?,?,?)", (cur.lastrowid, title, summary, ctx))
        n_stubs += 1

    for p in sorted(SOURCES_DIR.glob("*.md")) if SOURCES_DIR.exists() else []:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fm, body = _split_frontmatter(text)
        title = _flatten(fm.get("title")) or titles.get(p.stem, {}).get("title") or p.stem
        meta = " | ".join(f"{k}: {_flatten(fm[k])}" for k in _META_FIELDS if fm.get(k))
        db.execute("INSERT OR REPLACE INTO sources VALUES (?,?,?,?)", (p.stem, title, _flatten(fm.get("year")), meta))
        # Frontmatter and title are searchable as a first chunk so species/location queries hit.
        db.execute("INSERT INTO chunks_fts(source_id, heading, body) VALUES (?,?,?)", (p.stem, "Metadata", f"{title}\n{meta}"))
        for head, chunk in _chunks(body):
            db.execute("INSERT INTO chunks_fts(source_id, heading, body) VALUES (?,?,?)", (p.stem, head, chunk))
        n_sources += 1

    db.execute("INSERT INTO info VALUES ('signature', ?)", (_signature(),))
    db.commit()
    db.execute("INSERT INTO stubs_fts(stubs_fts) VALUES ('optimize')")
    db.execute("INSERT INTO chunks_fts(chunks_fts) VALUES ('optimize')")
    db.commit()
    db.close()
    tmp.replace(DB_PATH)
    if verbose:
        print(f"Brain index built: {n_stubs} concept stubs, {n_sources} sources -> {DB_PATH.name}")


_checked = False


def _connect() -> sqlite3.Connection:
    """Opens the index, (re)building it when missing or when the vault changed."""
    global _checked
    if not _checked:
        stale = True
        if DB_PATH.exists():
            try:
                db = sqlite3.connect(DB_PATH)
                row = db.execute("SELECT value FROM info WHERE key='signature'").fetchone()
                db.close()
                stale = not row or row[0] != _signature()
            except sqlite3.Error:
                stale = True
        if stale:
            print("📚 Building the Fisheries Brain index (one-time, a few seconds)...")
            build_index()
        _checked = True
    return sqlite3.connect(DB_PATH)


_alias_lookup = None


def _aliases() -> dict:
    """Maps a lowercase name to the other names in its group."""
    global _alias_lookup
    if _alias_lookup is None:
        _alias_lookup = {}
        for group in brain_enrich.load_alias_groups():
            for name in group:
                _alias_lookup.setdefault(name.lower(), []).extend(n for n in group if n.lower() != name.lower())
    return _alias_lookup


def _expand(query: str):
    """Extra search phrases for any known species name found in the query."""
    low = f" {re.sub(r'[^a-z0-9 ]+', ' ', query.lower())} "
    low = re.sub(r"\s+", " ", low)
    extra = []
    for name, others in _aliases().items():
        key = re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", name)).strip()
        if key and f" {key} " in low:
            extra += others
    return list(dict.fromkeys(extra))


def _terms(query: str):
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.]*[A-Za-z0-9]|[A-Za-z0-9]", query)
    terms = [w.lower().strip(".-'") for w in words]
    terms = [t for t in terms if t and t not in STOPWORDS and len(t) > 1]
    return list(dict.fromkeys(terms))


def _match_expr(terms, columns: str = "") -> str:
    quoted = " OR ".join(f'"{t}"' for t in terms)
    return f"{columns}({quoted})" if columns else quoted


def _clip(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"


def _best_excerpt(text: str, terms) -> str:
    """Picks the window of the chunk densest in query terms."""
    flat = re.sub(r"\s+", " ", _WIKILINK.sub(lambda m: m.group(1), text)).strip()
    if len(flat) <= EXCERPT_CHARS:
        return flat
    low = flat.lower()
    hits = [m.start() for t in terms for m in re.finditer(re.escape(t), low)]
    if not hits:
        return _clip(flat, EXCERPT_CHARS)
    best = max(hits, key=lambda h: sum(1 for x in hits if h <= x < h + EXCERPT_CHARS))
    start = max(0, best - 60)
    return ("…" if start else "") + _clip(flat[start:start + EXCERPT_CHARS + 40], EXCERPT_CHARS)


def search_brain(query: str) -> str:
    """Stub-first search. Returns concept summaries, related concepts, and source excerpts."""
    terms = _terms(query)
    if not terms:
        return "Error: provide at least one meaningful keyword."
    aliases = _expand(query)
    match_terms = terms + [a.lower() for a in aliases if a.lower() not in terms]
    db = _connect()
    try:
        phrase = re.sub(r"\s+", " ", query.strip().lower())
        exact = db.execute("SELECT id FROM stubs WHERE title_lc = ?", (phrase,)).fetchall()
        rows = db.execute(
            "SELECT rowid, bm25(stubs_fts, 12.0, 3.0, 1.0) FROM stubs_fts WHERE stubs_fts MATCH ? ORDER BY 2 LIMIT 40",
            (_match_expr(match_terms),),
        ).fetchall()
        # bm25 is lower-is-better; widely mentioned concepts get a mild boost, exact title match wins.
        scored = {}
        for rid, score in rows:
            n, title_lc = db.execute("SELECT n_mentions, title_lc FROM stubs WHERE id=?", (rid,)).fetchone()
            covered = sum(1 for t in terms if t in title_lc) / len(terms)
            scored[rid] = score - 1.5 * math.log1p(n) - 4.0 * covered
        for (rid,) in exact:
            scored[rid] = -1e9
        top = sorted(scored, key=scored.get)[:MAX_STUBS]

        out, mentioned = [], []
        if aliases:
            out.append(f"(Also searched equivalent names: {', '.join(aliases[:8])})")
        if top:
            out.append("CONCEPTS (from the vault's concept notes; follow a related concept by searching its name):")
        for rid in top:
            title, summary, related, mentions, n = db.execute(
                "SELECT title, summary, related, mentions, n_mentions FROM stubs WHERE id=?", (rid,)
            ).fetchone()
            related, mentions = json.loads(related), json.loads(mentions)
            line = f"- {title} ({n} sources)"
            if summary:
                line += f": {_clip(summary, SUMMARY_CHARS)}"
            out.append(line)
            if related:
                out.append(f"    Related: {', '.join(related[:RELATED_SHOWN])}")
            if mentions:
                out.append(f"    Sources: {', '.join(mentions[:MENTIONS_SHOWN])}")
            mentioned += mentions

        # Excerpts: sources linked from the matching stubs first, then global matches.
        excerpts, seen = [], set()

        def collect(sql, params):
            for sid, head, body in db.execute(sql, params):
                if sid in seen or head == "Metadata" or len(excerpts) >= MAX_EXCERPTS:
                    continue
                seen.add(sid)
                info = db.execute("SELECT title, year FROM sources WHERE source_id=?", (sid,)).fetchone()
                title, year = info if info else (sid, "")
                label = f"[{sid}]" + (f" {title}" if title != sid else "") + (f" ({year})" if year else "")
                where = f" — {head}" if head else ""
                excerpts.append(f"- {label}{where}: {_best_excerpt(body, terms)}")

        linked = list(dict.fromkeys(mentioned))[:60]
        if linked:
            marks = ",".join("?" * len(linked))
            collect(
                f"SELECT source_id, heading, body FROM chunks_fts WHERE chunks_fts MATCH ? AND source_id IN ({marks}) ORDER BY bm25(chunks_fts, 0.0, 2.0, 1.0) LIMIT 30",
                (_match_expr(match_terms), *linked),
            )
        collect(
            "SELECT source_id, heading, body FROM chunks_fts WHERE chunks_fts MATCH ? ORDER BY bm25(chunks_fts, 0.0, 2.0, 1.0) LIMIT 30",
            (_match_expr(match_terms),),
        )
        if excerpts:
            out.append("\nSOURCE EXCERPTS (use read_brain_source with the id for more):")
            out += excerpts
        if not out:
            return f"No matches in the Fisheries Brain for: '{query}'."
        return "\n".join(out)
    finally:
        db.close()


def read_source(source_id: str, query: str = "", max_chars: int = 3500) -> str:
    """Returns the most relevant chunks of one source (or its start when no query is given)."""
    sid = Path(source_id).stem
    db = _connect()
    try:
        info = db.execute("SELECT title, year, meta FROM sources WHERE source_id=?", (sid,)).fetchone()
        if not info:
            return f"Error: source '{source_id}' not found in the Fisheries Brain."
        title, year, meta = info
        terms = _terms(query)
        rows = []
        if terms:
            rows = db.execute(
                "SELECT heading, body FROM chunks_fts WHERE chunks_fts MATCH ? AND source_id = ? ORDER BY bm25(chunks_fts, 0.0, 2.0, 1.0) LIMIT 6",
                (_match_expr(terms), sid),
            ).fetchall()
        if not rows:
            rows = db.execute(
                "SELECT heading, body FROM chunks_fts WHERE source_id = ? AND heading != 'Metadata' ORDER BY rowid LIMIT 6", (sid,)
            ).fetchall()
        head = f"[{sid}] {title}" + (f" ({year})" if year else "") + (f"\n{meta}" if meta else "")
        parts, used = [head], len(head)
        for heading, body in rows:
            piece = (f"## {heading}\n" if heading else "") + body.strip()
            if used + len(piece) > max_chars:
                piece = piece[: max(0, max_chars - used)]
            if not piece:
                break
            parts.append(piece)
            used += len(piece)
        return "\n\n".join(parts)
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != "rebuild":
        print(search_brain(" ".join(sys.argv[1:])))
    else:
        build_index()
