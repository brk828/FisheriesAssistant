"""Compare stub-first search with approved-library retrieval; no LLM calls.

Run from fisheries_agent: python -m utils.rag_eval ARTIFACT --mode lexical
The default question files include the existing retrieval set and the RAG pilot.
Source hits are retrieval proxies, NOT validation of scientific claims.
"""
import argparse
from contextlib import redirect_stdout
import json
import statistics
import sys
import time
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
QUESTION_FILES = (BASE / "brain_meta" / "eval_questions.yaml",
                  BASE / "brain_meta" / "rag_eval_questions.yaml")


def score(question: dict, evidence: list) -> dict:
    """Match expected source identities without interpreting passage content."""
    expected = set(map(str, question.get("sources", [])))
    found = set()
    for item in evidence:
        found.add(str(item.get("source_id", "")))
        found.add(str(item.get("stem", "")))
        found.add(Path(item.get("source_file", "")).stem)
    if question.get("expect_abstain"):
        return {"check": "abstention", "passed": not evidence}
    if expected:
        return {"check": "source_hit", "passed": bool(expected & found)}
    return {"check": "manual_review", "passed": None}


def compare(questions: list, retrieve, baseline) -> dict:
    """Call injected local search functions, retaining separate baseline metrics."""
    results = []
    for question in questions:
        start = time.perf_counter()
        text = baseline(question["query"])
        baseline_ms = (time.perf_counter() - start) * 1000
        expected = question.get("sources", [])
        concepts = question.get("concepts", [])
        if question.get("expect_abstain"):
            baseline_pass = None  # The old text interface has no abstention contract.
        elif question.get("none"):
            baseline_pass = isinstance(text, str) and len(text) < 12000
        elif expected or concepts:
            baseline_pass = (any(str(s) in text for s in expected)
                             or any(str(c).lower() in text.lower() for c in concepts))
        else:
            baseline_pass = None
        start = time.perf_counter()
        pack = retrieve(question)
        elapsed = (time.perf_counter() - start) * 1000
        evidence = pack["evidence"]
        results.append({
            "query": question["query"],
            "track": question.get("track", "methodological"),
            "baseline": {"passed": baseline_pass, "ms": round(baseline_ms, 2)},
            "rag": {**score(question, evidence), "ms": round(elapsed, 2),
                    "evidence_ids": [e["evidence_id"] for e in evidence],
                    "retrieval": pack.get("retrieval", {})},
            "review": question.get("review", "Check claim support and applicability manually."),
        })
    metrics = {}
    for method in ("baseline", "rag"):
        checked = [r[method] for r in results if r[method]["passed"] is not None]
        metrics[method] = {
            "passed": sum(r["passed"] for r in checked), "checked": len(checked),
            "median_ms": round(statistics.median(r[method]["ms"] for r in results), 2) if results else 0,
        }
    return {
        "metrics": metrics, "results": results,
        "limitations": [
            "Baseline searches the full vault; RAG searches only explicitly approved exported sources.",
            "Missing expected sources may reflect export scope, not retrieval quality.",
            "Source hits do not verify citation content, numerical bounds or claim support.",
            "Concept-only legacy questions require manual RAG review; stubs are not exported evidence.",
            "Review conflicting studies, appropriate abstention and scientific applicability manually.",
            "Latency includes initialization and integrity checks; no Windows installation test is implied.",
        ],
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--mode", choices=("lexical", "hybrid"), default="lexical")
    parser.add_argument("--file", action="append", type=Path,
                        help="Question YAML; repeat to combine sets (defaults to both shipped sets)")
    args = parser.parse_args(argv)
    if not args.artifact.is_absolute():
        parser.error("Artifact must be an absolute path")
    from utils import brain_index, rag_library

    questions = []
    for path in args.file or QUESTION_FILES:
        try:
            items = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            parser.error(f"Cannot read question file {path}: {exc}")
        if not isinstance(items, list) or any(not isinstance(q, dict) or not q.get("query") for q in items):
            parser.error(f"Expected a list of questions with query fields: {path}")
        questions.extend(items)

    def retrieve(question):
        track = question.get("track", "methodological")
        if track == "biological":
            request = {field: question[field] for field in rag_library.TRACK_FIELDS[track] if field in question}
            request.setdefault("parameter", question["query"])
        else:
            request = {field: question[field] for field in rag_library.TRACK_FIELDS["methodological"] if field in question}
            request.setdefault("goal", question["query"])
        request["track"] = track
        return rag_library.query_export(args.artifact, request,
                                        mode="semantic" if args.mode == "hybrid" else "lexical")

    try:
        with redirect_stdout(sys.stderr):
            if args.mode == "hybrid":
                manifest, _ = rag_library.load_export(args.artifact)
                if not manifest.get("embedding"):
                    raise ValueError("Hybrid evaluation requires an artifact with approved embeddings")
            report = compare(questions, retrieve, brain_index.search_brain)
        report["requested_mode"] = args.mode
        report["artifact_bytes"] = sum(p.stat().st_size for p in args.artifact.rglob("*") if p.is_file())
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(2, f"Evaluation failed: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
