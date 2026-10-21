from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from utils import rag_eval


class RagEvaluationTests(unittest.TestCase):
    def test_canonical_id_and_legacy_stem_both_match(self):
        item = {"source_id": "X-1234abcd", "source_file": "notes/CPUE_2024.md"}
        for identity in ("X-1234abcd", "CPUE_2024"):
            self.assertTrue(rag_eval.score({"sources": [identity]}, [item])["passed"])
        self.assertFalse(rag_eval.score({"sources": ["missing"]}, [item])["passed"])
        self.assertTrue(rag_eval.score({"sources": ["legacy"]}, [{"stem": "legacy"}])["passed"])

    def test_abstention_requires_no_evidence(self):
        self.assertTrue(rag_eval.score({"expect_abstain": True}, [])["passed"])
        self.assertFalse(rag_eval.score({"expect_abstain": True}, [{}])["passed"])

    def test_concept_only_questions_are_not_scientific_passes(self):
        self.assertIsNone(rag_eval.score({"concepts": ["CPUE"]}, [])["passed"])

    def test_compare_retains_scope_warning_and_retrieval_mode(self):
        questions = [{"query": "CPUE", "sources": ["paper"]},
                     {"query": "unknown", "expect_abstain": True}]

        def retrieve(question):
            evidence = ([{"source_id": "paper", "evidence_id": "paper:0"}]
                        if question["query"] == "CPUE" else [])
            return {"evidence": evidence, "retrieval": {"mode": "lexical"}}

        report = rag_eval.compare(questions, retrieve, lambda query: "[paper]" if query == "CPUE" else "")
        self.assertEqual(report["metrics"]["rag"]["passed"], 2)
        self.assertEqual(report["metrics"]["baseline"]["checked"], 1)
        self.assertIn("full vault", report["limitations"][0])
        self.assertEqual(report["results"][0]["rag"]["retrieval"]["mode"], "lexical")

    def test_empty_question_list(self):
        report = rag_eval.compare([], lambda q: {}, lambda q: "")
        self.assertEqual(report["metrics"]["rag"]["checked"], 0)

    def test_cli_builds_context_and_requires_real_hybrid_mode(self):
        with tempfile.TemporaryDirectory() as folder:
            questions = Path(folder) / "questions.yaml"
            questions.write_text("- query: mortality\n  track: biological\n"
                                 "  species: Explicit species\n  parameter: mortality\n"
                                 "  expect_abstain: true\n", encoding="utf-8")
            output = io.StringIO()
            with patch("utils.rag_library.query_export", return_value={"evidence": []}) as query, \
                 patch("utils.rag_library.load_export", return_value=({"embedding": {"revision": "test"}}, [])), \
                 patch("utils.brain_index.search_brain", return_value="") as baseline, \
                 redirect_stdout(output):
                result = rag_eval.main([folder, "--mode", "hybrid", "--file", str(questions)])
            self.assertEqual(result, 0)
            request = query.call_args.args[1]
            self.assertEqual(request["species"], "Explicit species")
            self.assertEqual(request["parameter"], "mortality")
            self.assertEqual(query.call_args.kwargs["mode"], "semantic")
            self.assertEqual(json.loads(output.getvalue())["metrics"]["rag"]["passed"], 1)
            baseline.assert_called_once_with("mortality")

    def test_hybrid_evaluation_rejects_lexical_artifact_before_search(self):
        with tempfile.TemporaryDirectory() as folder:
            questions = Path(folder) / "questions.yaml"
            questions.write_text("- query: CPUE\n", encoding="utf-8")
            with patch("utils.rag_library.load_export", return_value=({"embedding": None}, [])), \
                 patch("utils.brain_index.search_brain") as baseline, \
                 redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                rag_eval.main([folder, "--mode", "hybrid", "--file", str(questions)])
            self.assertEqual(error.exception.code, 2)
            baseline.assert_not_called()


if __name__ == "__main__":
    unittest.main()
