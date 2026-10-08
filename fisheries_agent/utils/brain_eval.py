"""Retrieval test for the brain search. Usage: python -m utils.brain_eval [-v] [--file PATH]

Runs every question in brain_meta/eval_questions.yaml through search_brain (local, no LLM, no network)
and reports hits, where the answer first appeared, and how much text each search returns.
"""
import argparse
import sys
import time
from pathlib import Path

import yaml

from utils import brain_index

DEFAULT_FILE = Path(__file__).resolve().parent.parent / "brain_meta" / "eval_questions.yaml"


def _rank(text: str, needle: str, case: bool):
    hay, n = (text, needle) if case else (text.lower(), needle.lower())
    pos = hay.find(n)
    return None if pos < 0 else pos


def evaluate(path: Path, verbose: bool = False) -> int:
    questions = yaml.safe_load(path.read_text(encoding="utf-8"))
    results = []
    for q in questions:
        start = time.perf_counter()
        out = brain_index.search_brain(q["query"])
        ms = (time.perf_counter() - start) * 1000
        if q.get("none"):
            ok = isinstance(out, str) and len(out) < 12000
            where = "-"
        else:
            hits = [(_rank(out, s, True), s) for s in q.get("sources", [])]
            hits += [(_rank(out, c, False), c) for c in q.get("concepts", [])]
            found = [(p, s) for p, s in hits if p is not None]
            ok = bool(found)
            where = "-"
            if ok:
                first = min(p for p, _ in found)
                marks = [(out.find("DOCUMENTS WITH MATCHING TITLES"), "titles"), (out.find("SOURCE EXCERPTS"), "excerpts")]
                where = "concepts"
                for pos, name in marks:
                    if 0 <= pos <= first:
                        where = name
        results.append((q, ok, where, len(out), ms, out))

    passed = sum(1 for r in results if r[1])
    for q, ok, where, size, ms, out in results:
        if verbose or not ok:
            print(f"{'PASS' if ok else 'FAIL'}  [{where:8}] {size:6} chars {ms:6.0f} ms  {q['query']}")
        if not ok and verbose:
            print(out[:600])
    sizes = sorted(r[3] for r in results)
    print(f"\n{passed}/{len(results)} passed. Output size: median {sizes[len(sizes) // 2]} chars (~{sizes[len(sizes) // 2] // 4} tokens), max {sizes[-1]}.")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--file", default=str(DEFAULT_FILE))
    args = ap.parse_args()
    sys.exit(evaluate(Path(args.file), args.verbose))
