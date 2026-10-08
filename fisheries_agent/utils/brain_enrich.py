"""Derives search metadata for the vault without modifying any vault file.

Outputs go to fisheries_agent/brain_meta/:
  source_titles.json  source id -> {"title", "from"}   (generated; "manual"/"llm" entries are preserved)
  aliases_auto.json   scientific name -> {"canonical", "names": [{"name", "count", "from"}]}
  aliases.yaml        hand-edited groups and ignores; always wins over the automatic table

Run:  python -m utils.brain_enrich            (titles + aliases, local only)
      python -m utils.brain_enrich titles
      python -m utils.brain_enrich aliases
      python -m utils.brain_enrich titles-llm [--yes] [--limit N] [--model ID]
          One-time LLM pass for sources that still have no title. Shows a token/cost estimate and
          asks before sending anything to OpenRouter; resumable (progress is saved after each batch).
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
BRAIN_DIR = BASE_DIR / "00_Fisheries_Brain"
SOURCES_DIR = BRAIN_DIR / "01_Sources"
STUBS_DIR = BRAIN_DIR / "02_Brain"
META_DIR = BASE_DIR / "brain_meta"
TITLES_PATH = META_DIR / "source_titles.json"
AUTO_ALIASES_PATH = META_DIR / "aliases_auto.json"
MANUAL_ALIASES_PATH = META_DIR / "aliases.yaml"
CITATIONS_PATH = META_DIR / "citations.json"

MANUAL_ALIASES_TEMPLATE = """# Hand-maintained species/name aliases. Entries here always win over aliases_auto.json.
#
# aliases: each group lists names that mean the same thing for searching, for example
#   - [Colorado pikeminnow, Colorado squawfish, Ptychocheilus lucius]
# ignore: names that must never be used as an alias (too generic or wrong).
#   - sucker
aliases: []
ignore: []
"""

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
_WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
_BINOMIAL = re.compile(r"^[A-Z][a-z]{2,}(?: [a-z]{3,})(?: [a-z]{3,})?$")
_BINOMIAL_IN_TEXT = r"[A-Z][a-z]{2,} [a-z]{3,}(?: [a-z]{3,})?"
_PAREN_PAIR = re.compile(rf"((?:[A-Z][\w'\-]*\s+){{0,3}}[A-Z][\w'\-]*)\s*\(\s*[*_]*({_BINOMIAL_IN_TEXT})[*_]*\s*\)")
_NAME_LEAD = {"the", "a", "an"}
_BAD_EPITHETS = {
    "sp", "spp", "species", "and", "the", "with", "from", "that", "this", "for", "population", "specified",
    "taxa", "provided", "applicable", "available", "identified", "listed", "known", "data", "none", "only",
}
_BAD_GENERA = {
    "Not", "Multiple", "Various", "Several", "Other", "Unknown", "Mixed", "General", "None", "All", "Many",
    "Native", "Non", "Fish", "Fishes", "No", "Aquatic", "Mostly", "Primarily", "See", "Table", "Figure",
}
MAX_NAMES_PER_SPECIES = 12
_NOISE_WORDS = {
    "now", "also", "historically", "formerly", "cited", "reported", "as", "relevant", "to", "introduced",
    "non-native", "nonnative", "native", "hatchery", "catchable-sized", "stock", "surrogate", "target",
    "species", "listed", "endangered", "threatened", "known", "called", "see", "formerly", "subadult",
    "juvenile", "adult", "larval", "young", "wild", "pending", "verification", "tentative", "identification",
    "hybridization", "context", "undifferentiated", "complex", "spp", "unidentified", "unknown", "possible",
    "probable", "uncertain", "and", "incl", "including", "congeners", "summary", "relatives", "subsp", "subspp",
    "undescribed", "or", "of", "with",
}
_GENERIC_WORDS = {
    "fish", "fishes", "trout", "bass", "sucker", "suckers", "chub", "minnow", "salmon", "catfish",
    "sunfish", "shiner", "dace", "carp", "pupfish", "darter", "species", "river", "lake", "creek",
}


def _split_frontmatter(text: str):
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        data = {}
    return (data if isinstance(data, dict) else {}), text[m.end():]


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _clean_markdown(text: str) -> str:
    text = _WIKILINK.sub(lambda m: m.group(1), text)
    text = re.sub(r"[*_`]+", "", text)
    return re.sub(r"\s+", " ", text).strip(" #:-")


def _text(value) -> str:
    return value.strip() if isinstance(value, str) else ""


def _citation_title(citation: str) -> str:
    m = re.search(r"\(\s*\d{4}[a-z]?\s*\)\.?\s*(.+?)\.(?:\s|$)", citation)
    return _clean_markdown(m.group(1)) if m and len(m.group(1)) > 8 else ""


# ---------------------------------------------------------------- titles

def derive_titles() -> dict:
    """Deterministic titles: frontmatter title, then first body heading, then the citation."""
    out = {}
    for p in sorted(SOURCES_DIR.glob("*.md")):
        fm, body = _split_frontmatter(_read(p))
        title = _clean_markdown(_text(fm.get("title")))
        origin = "frontmatter"
        if not title:
            h = re.search(r"^# (.+)$", body, re.M)
            title, origin = (_clean_markdown(h.group(1)), "heading") if h else ("", "")
        if not title:
            title, origin = _citation_title(_text(fm.get("source_citation")) or _text(fm.get("citation"))), "citation"
        if title:
            out[p.stem] = {"title": title, "from": origin}
    return out


def load_titles() -> dict:
    try:
        return json.loads(TITLES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def write_titles(verbose: bool = True) -> dict:
    META_DIR.mkdir(exist_ok=True)
    previous = load_titles()
    titles = derive_titles()
    kept = 0
    for sid, entry in previous.items():
        # Manual edits always stay; LLM titles stay only where no deterministic title exists.
        if entry.get("from") == "manual" or (entry.get("from") == "llm" and sid not in titles):
            titles[sid] = entry
            kept += 1
    total = len(list(SOURCES_DIR.glob("*.md")))
    TITLES_PATH.write_text(json.dumps(dict(sorted(titles.items())), indent=1, ensure_ascii=False), encoding="utf-8")
    if verbose:
        print(f"Titles: {len(titles)} of {total} sources have a title ({kept} kept from earlier manual/LLM entries); {total - len(titles)} still untitled.")
    return titles


def untitled_sources() -> list:
    have = load_titles()
    return [p.stem for p in sorted(SOURCES_DIR.glob("*.md")) if p.stem not in have]


# ---------------------------------------------------------------- aliases

def _norm(name: str) -> str:
    return re.sub(r"\s+", " ", name.strip().lower())


def _clean_common(name: str) -> str:
    """Returns a plausible common name, or '' for composite strings, phrases and parentheticals."""
    name = re.sub(r"\(.*?\)|\(.*$", "", name)
    name = re.sub(r"\s+", " ", name.strip(" ,;:.*_\"'"))
    words = name.split()
    while words and words[0].lower() in _NAME_LEAD:
        words.pop(0)
    if not words or len(words) > 4 or any(w.lower().strip(",.'\"") in _NOISE_WORDS for w in words):
        return ""
    if any(c in name for c in ",;()"):
        return ""
    if re.search(r"(idae|inae|iformes|oidei)$", name.lower()):
        return ""
    return " ".join(words)


def _valid_binomial(name: str) -> bool:
    name = name.strip()
    if not _BINOMIAL.match(name):
        return False
    genus, epithet = name.split()[:2]
    return genus not in _BAD_GENERA and epithet not in _BAD_EPITHETS


def _frontmatter_pairs(fm: dict):
    """Yields (scientific, common) pairs from species / common_name / scientific_name fields."""
    species = fm.get("species")
    items = species if isinstance(species, list) else re.split(r"[;]", species) if isinstance(species, str) else []
    sci_fields = []
    for item in items:
        item = str(item).strip()
        m = re.match(r"^(.*?)\(([^)]*)\)\s*$", item)
        if not m:
            if _valid_binomial(item):
                sci_fields.append(item)
            continue
        outer, inner = m.group(1).strip(), m.group(2).strip()
        if _valid_binomial(inner.strip("*_ ")):
            sci, commons = inner.strip("*_ "), re.split(r"/| or ", outer)
        elif _valid_binomial(outer.strip("*_ ")):
            sci, commons = outer.strip("*_ "), re.split(r"[/,]| or ", inner)
        else:
            continue
        sci_fields.append(sci)
        for c in commons:
            c = _clean_common(c)
            if c:
                yield sci, c
    common = fm.get("common_name")
    if isinstance(common, str) and len(sci_fields) == 1:
        for c in re.split(r"[/;,]", common):
            c = _clean_common(c)
            if c:
                yield sci_fields[0], c


def _frontmatter_sci(fm: dict):
    species = fm.get("species")
    items = species if isinstance(species, list) else re.split(r"[;]", species) if isinstance(species, str) else []
    for item in items:
        for part in re.findall(r"[A-Za-z][A-Za-z ]+", str(item)):
            part = part.strip()
            if _valid_binomial(part):
                yield part


def build_auto_aliases(verbose: bool = True) -> dict:
    stub_titles = {p.stem.lower() for p in STUBS_DIR.glob("*.md")} if STUBS_DIR.exists() else set()
    known_sci = set()
    structured = defaultdict(Counter)   # sci -> common -> count (frontmatter)
    textual = defaultdict(Counter)      # sci -> common -> count (prose)

    for p in SOURCES_DIR.glob("*.md"):
        text = _read(p)
        fm, body = _split_frontmatter(text)
        for sci, common in _frontmatter_pairs(fm):
            structured[sci][common] += 1
        known_sci.update(_norm(x) for x in _frontmatter_sci(fm))
        for common, sci in _PAREN_PAIR.findall(body):
            common = _clean_common(common)
            if _valid_binomial(sci) and common:
                textual[sci][common] += 1
    for p in STUBS_DIR.glob("*.md") if STUBS_DIR.exists() else []:
        for common, sci in _PAREN_PAIR.findall(_read(p)):
            common = _clean_common(common)
            if _valid_binomial(sci) and common:
                textual[sci][common] += 1

    known_sci.update(t for t in stub_titles if _BINOMIAL.match(t.capitalize()))
    clusters = {}
    for sci in set(structured) | set(textual):
        if _norm(sci) not in known_sci:
            continue
        names = {}
        for common, n in structured[sci].items():
            if len(common.split()) == 1 and n < 2 and _norm(common) not in stub_titles:
                continue
            names[_norm(common)] = {"name": common, "count": n, "from": "frontmatter"}
        for common, n in textual[sci].items():
            key = _norm(common)
            if key in names:
                names[key]["count"] += n
                continue
            single = len(common.split()) == 1
            known = key in stub_titles
            if (n >= 2 and not single) or (n >= 2 and single and known) or (known and n >= 1 and not single):
                names[key] = {"name": common, "count": n, "from": "text"}
        for key in list(names):
            if key in _GENERIC_WORDS or key == _norm(sci) or key == _norm(sci.split()[0]):
                del names[key]
        if names and len(names) <= MAX_NAMES_PER_SPECIES:
            ordered = sorted(names.values(), key=lambda e: (-e["count"], e["name"]))
            clusters[sci] = {"canonical": ordered[0]["name"], "names": ordered}

    # A single word that also starts other names ("Colorado", "Gila") is a place or genus, not a species name.
    leading = {_norm(e["name"]).split()[0] for c in clusters.values() for e in c["names"] if len(e["name"].split()) > 1}
    for c in clusters.values():
        c["names"] = [e for e in c["names"] if len(e["name"].split()) > 1 or _norm(e["name"]) not in leading]
    # A name used by several species is ambiguous; keep it only where it is clearly strongest.
    owners = defaultdict(list)
    for sci, c in clusters.items():
        for e in c["names"]:
            owners[_norm(e["name"])].append((e["count"], sci))
    for key, found in owners.items():
        if len(found) < 2:
            continue
        found.sort(reverse=True)
        keep = found[0][1] if found[0][0] >= 2 * found[1][0] else None
        for _, sci in found:
            if sci != keep:
                clusters[sci]["names"] = [e for e in clusters[sci]["names"] if _norm(e["name"]) != key]
    for sci in list(clusters):
        if not clusters[sci]["names"]:
            del clusters[sci]
        else:
            clusters[sci]["canonical"] = clusters[sci]["names"][0]["name"]

    META_DIR.mkdir(exist_ok=True)
    AUTO_ALIASES_PATH.write_text(json.dumps(dict(sorted(clusters.items())), indent=1, ensure_ascii=False), encoding="utf-8")
    if not MANUAL_ALIASES_PATH.exists():
        MANUAL_ALIASES_PATH.write_text(MANUAL_ALIASES_TEMPLATE, encoding="utf-8")
    if verbose:
        multi = sum(1 for c in clusters.values() if len(c["names"]) > 1)
        print(f"Aliases: {len(clusters)} species clusters ({multi} with more than one common name) -> {AUTO_ALIASES_PATH.name}")
    return clusters


def _load_manual():
    try:
        data = yaml.safe_load(MANUAL_ALIASES_PATH.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        data = {}
    groups = [[str(n) for n in g if n] for g in (data.get("aliases") or []) if isinstance(g, list)]
    ignore = {_norm(str(n)) for n in (data.get("ignore") or [])}
    return groups, ignore


def load_alias_groups() -> list:
    """Returns merged groups of equivalent names (automatic clusters plus manual groups)."""
    try:
        auto = json.loads(AUTO_ALIASES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        auto = {}
    manual, ignore = _load_manual()
    groups = [[sci] + [e["name"] for e in c["names"]] for sci, c in auto.items()]
    # Automatic clusters stay separate (one per species); a manual group may bridge several of them.
    for g in manual:
        keys = {_norm(n) for n in g}
        merged = list(g)
        rest = []
        for existing in groups:
            if keys & {_norm(n) for n in existing}:
                merged += existing
                keys |= {_norm(n) for n in existing}
            else:
                rest.append(existing)
        groups = rest + [merged]
    result = []
    for g in groups:
        seen, names = set(), []
        for n in g:
            if _norm(n) not in ignore and _norm(n) not in seen:
                seen.add(_norm(n))
                names.append(n)
        if len(names) > 1:
            result.append(sorted(names))
    return result


# ---------------------------------------------------------------- LLM titles

TITLE_MODEL = "anthropic/claude-haiku-4.5"
TITLE_BATCH = 8
SNIPPET_CHARS = 700
TITLE_MAX_CHARS = 160

TITLE_SYSTEM = (
    "You write short descriptive titles for archived fisheries documents (papers, letters, memos, meeting notes, reports). "
    "For each numbered item you get a file id (a truncated filename, often ending in a date or number) and the start of "
    "its summary. Write ONE title per item, at most 20 words, based only on the text given. For letters or memos say who "
    "wrote to whom and the subject; include the year when it is given. Do not invent facts. "
    'Reply with only a JSON object mapping each id to its title, e.g. {"ID1": "Title", "ID2": "Title"}.'
)


def _snippet(sid: str) -> str:
    fm, body = _split_frontmatter(_read(SOURCES_DIR / f"{sid}.md"))
    body = re.sub(r"(?m)^(?:#[\w\-]+\s*)+$", "", body)
    m = re.search(r"^## (?:Executive Summary|Summary)\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    text = _clean_markdown(m.group(1) if m else body)
    hints = [f"{k}: {v}" for k in ("document_type", "date", "year", "location") if (v := _text(fm.get(k)) or (str(fm[k]) if fm.get(k) else ""))]
    return (" | ".join(hints) + "\n" if hints else "") + text[:SNIPPET_CHARS]


def _batch_prompt(batch: list) -> str:
    return "\n\n".join(f"[{i}] id: {sid}\n{_snippet(sid)}" for i, sid in enumerate(batch, 1))


def estimate_title_cost(ids: list, model: str):
    """Returns (input_tokens, output_tokens, dollars or None). Tokens use a 4 chars/token approximation."""
    batches = -(-len(ids) // TITLE_BATCH)
    in_chars = batches * len(TITLE_SYSTEM) + sum(len(_snippet(s)) + 60 for s in ids)
    in_tokens = in_chars // 4
    out_tokens = len(ids) * 40
    price = _model_price(model)
    dollars = None if not price else in_tokens * price[0] + out_tokens * price[1]
    return in_tokens, out_tokens, dollars


def _model_price(model: str):
    """Best-effort per-token (prompt, completion) USD price from OpenRouter's public model list."""
    import urllib.request
    try:
        with urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=10) as r:
            for m in json.load(r).get("data", []):
                if m.get("id") == model:
                    pr = m.get("pricing", {})
                    return float(pr.get("prompt", 0)), float(pr.get("completion", 0))
    except Exception:
        return None
    return None


def _parse_titles(text: str, batch: list) -> dict:
    m = re.search(r"\{.*\}", text or "", re.S)
    try:
        data = json.loads(m.group(0)) if m else {}
    except json.JSONDecodeError:
        return {}
    out = {}
    for sid in batch:
        title = data.get(sid)
        if isinstance(title, str):
            title = _clean_markdown(title).strip("\"' ")
            if 8 <= len(title) <= TITLE_MAX_CHARS:
                out[sid] = title
    return out


def _request_titles(client, model: str, batch: list) -> dict:
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        max_tokens=60 * len(batch) + 100,
        messages=[{"role": "system", "content": TITLE_SYSTEM}, {"role": "user", "content": _batch_prompt(batch)}],
    )
    return _parse_titles(response.choices[0].message.content, batch)


def _write_title_entries(new: dict) -> None:
    titles = load_titles()
    for sid, title in new.items():
        titles[sid] = {"title": title, "from": "llm"}
    TITLES_PATH.write_text(json.dumps(dict(sorted(titles.items())), indent=1, ensure_ascii=False), encoding="utf-8")


def llm_titles(assume_yes: bool = False, limit: int = 0, model: str = "") -> None:
    import os
    try:
        from dotenv import load_dotenv
        load_dotenv(BASE_DIR / ".env")
    except ImportError:
        pass
    model = model or os.getenv("OPENROUTER_TITLE_MODEL", TITLE_MODEL)
    write_titles(verbose=False)
    todo = untitled_sources()
    if limit:
        todo = todo[:limit]
    if not todo:
        print("Every source already has a title.")
        return
    in_t, out_t, dollars = estimate_title_cost(todo, model)
    cost = f"about ${dollars:.2f}" if dollars is not None else "price unavailable (check openrouter.ai/models)"
    print(f"{len(todo)} sources need a title. Model: {model}")
    print(f"Estimated usage: ~{in_t:,} input + ~{out_t:,} output tokens in {-(-len(todo) // TITLE_BATCH)} requests; {cost}.")
    print(f"This sends the first ~{SNIPPET_CHARS} characters of each source's summary to OpenRouter.")
    if not assume_yes and input("Proceed? [y/N] ").strip().lower() not in ("y", "yes"):
        print("Cancelled; nothing was sent.")
        return
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        print("OPENROUTER_API_KEY is not set (see .env.template).")
        return
    from openai import OpenAI
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
    done = failed = 0
    for i in range(0, len(todo), TITLE_BATCH):
        batch = todo[i:i + TITLE_BATCH]
        try:
            got = _request_titles(client, model, batch)
            missing = [s for s in batch if s not in got]
            if missing:
                got.update(_request_titles(client, model, missing))
        except Exception as e:
            print(f"Stopped after {done} titles: {e}\nRe-run the command to continue where it left off.")
            return
        if got:
            _write_title_entries(got)
        done += len(got)
        failed += len(batch) - len(got)
        print(f"  {done + failed}/{len(todo)} processed", end="\r", flush=True)
    print(f"\nAdded {done} LLM titles ({failed} could not be titled). Rebuild is automatic on the next search.")


def metadata_signature() -> str:
    parts = []
    for p in (TITLES_PATH, AUTO_ALIASES_PATH, MANUAL_ALIASES_PATH, CITATIONS_PATH):
        parts.append(f"{int(p.stat().st_mtime)}:{p.stat().st_size}" if p.exists() else "-")
    return "|".join(parts)


def ensure() -> None:
    """Creates any missing sidecar file so the index always has titles and aliases."""
    if not TITLES_PATH.exists():
        write_titles()
    if not AUTO_ALIASES_PATH.exists() or not MANUAL_ALIASES_PATH.exists():
        build_auto_aliases()


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what == "titles-llm":
        args = sys.argv[2:]
        opt = lambda name: args[args.index(name) + 1] if name in args and args.index(name) + 1 < len(args) else ""
        llm_titles("--yes" in args, int(opt("--limit") or 0), opt("--model"))
        sys.exit(0)
    if what in ("titles", "all"):
        write_titles()
    if what in ("aliases", "all"):
        build_auto_aliases()
    if what not in ("titles", "aliases", "all", "titles-llm"):
        print(__doc__)
