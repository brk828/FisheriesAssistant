"""Local brain review: which analysis families the vault's source notes name, and what data they pair with.

    python -m utils.brain_methods scan                      # count source notes per analysis family (no LLM, no network)
    python -m utils.brain_methods show <family> [--limit N]   # the sources and context snippets for one family

`scan` writes brain_meta/analysis_review.json (generated; never hand-edit): per family the source ids, counts, years, and
co-mentioned families. The lexicon is icm_templates/analysis_lexicon.yaml. Mentions are keyword hits, so a high count
means "discussed or used", not "recommended"; the skill drafts decide what the evidence supports.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

from utils import brain_index

HERE = Path(__file__).resolve().parent.parent
LEXICON = HERE / "icm_templates" / "analysis_lexicon.yaml"
OUT = HERE / "brain_meta" / "analysis_review.json"
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
SNIPPET = 220


def load_lexicon() -> dict:
    lex = yaml.safe_load(LEXICON.read_text(encoding="utf-8")) or {}
    return {k: {**v, "rx": re.compile("|".join(f"(?:{p})" for p in v["patterns"]), re.I)} for k, v in lex.items()}


def _year(text: str, name: str):
    """Year from the front matter date, else from a trailing _YYYY in the file name (a trailing _NNNNN is a library id)."""
    m = re.search(r'^date:\s*"?(\d{4})', text, re.M) or re.search(r"_((?:19|20)\d{2})$", name)
    return int(m.group(1)) if m else None


def scan(sources_dir=None) -> dict:
    sources_dir = Path(sources_dir or brain_index.SOURCES_DIR)
    lex = load_lexicon()
    fam = {k: {"group": v["group"], "data": v["data"], "sources": {}, "co": Counter()} for k, v in lex.items()}
    n = 0
    for f in sorted(sources_dir.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        body = FRONT.sub("", text, count=1)
        n += 1
        hit = {k: len(v["rx"].findall(body)) for k, v in lex.items()}
        hit = {k: c for k, c in hit.items() if c}
        for k, c in hit.items():
            fam[k]["sources"][f.stem] = {"hits": c, "year": _year(text, f.stem)}
            fam[k]["co"].update(o for o in hit if o != k)
    out = {"sources_scanned": n, "families": {}}
    for k, d in fam.items():
        years = [s["year"] for s in d["sources"].values() if s["year"]]
        ranked = sorted(d["sources"].items(), key=lambda kv: -kv[1]["hits"])
        out["families"][k] = {
            "group": d["group"], "data": d["data"], "source_count": len(d["sources"]),
            "recent_count": sum(y >= 2000 for y in years), "year_range": [min(years), max(years)] if years else None,
            "top_sources": [sid for sid, _ in ranked[:15]], "co_mentioned": dict(d["co"].most_common(5)),
        }
    return out


def write(result: dict) -> Path:
    OUT.write_text(json.dumps(result, indent=1), encoding="utf-8")
    return OUT


def show(family: str, limit: int = 8, sources_dir=None) -> list:
    sources_dir = Path(sources_dir or brain_index.SOURCES_DIR)
    lex = load_lexicon()[family]
    review = json.loads(OUT.read_text(encoding="utf-8"))["families"][family]
    rows = []
    for sid in review["top_sources"][:limit]:
        body = FRONT.sub("", (sources_dir / f"{sid}.md").read_text(encoding="utf-8", errors="replace"), count=1)
        m = lex["rx"].search(body)
        s = max(0, m.start() - SNIPPET // 2) if m else 0
        rows.append((sid, body[s:s + SNIPPET].replace("\n", " ")))
    return rows


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0] not in ("scan", "show"):
        print(__doc__)
        return 2
    if argv[0] == "scan":
        r = write(scan())
        res = json.loads(Path(r).read_text(encoding="utf-8"))
        print(f"Scanned {res['sources_scanned']} source notes -> {r}")
        for k, v in sorted(res["families"].items(), key=lambda kv: -kv[1]["source_count"]):
            print(f"  {v['source_count']:5d} ({v['recent_count']:4d} since 2000)  {k:26s} [{v['group']}; {v['data']}]")
        return 0
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 8
    for sid, snip in show(argv[1], limit):
        print(f"- {sid}: {snip}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
