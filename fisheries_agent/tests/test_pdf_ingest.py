import unittest
import json
import os
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from utils import pdf_ingest


class PdfIngestTests(unittest.TestCase):
    def setUp(self):
        pdf_ingest.USAGE.update({"in": 0, "out": 0, "cost": 0.0, "cost_exact": True, "requests": 0, "retries": 0})
        pdf_ingest.ACTIVE_DOCUMENT_USAGE = None

    def test_chat_raises_on_length_finish_without_network_retry(self):
        client = Mock()
        client.chat.completions.create.return_value = Mock(
            usage=Mock(prompt_tokens=12, completion_tokens=4500, cost=None),
            choices=[Mock(finish_reason="length", message=Mock(content="partial"))],
        )

        with self.assertRaises(pdf_ingest._OutputTruncatedError):
            pdf_ingest._chat(client, "test", "system", "user", 4500)

        client.chat.completions.create.assert_called_once()
        self.assertEqual(pdf_ingest.USAGE["in"], 12)
        self.assertEqual(pdf_ingest.USAGE["out"], 4500)
        self.assertEqual(pdf_ingest.USAGE["cost"], 0.0)

    def test_chat_captures_exact_cost_and_marks_lost_attempt_inexact(self):
        record = pdf_ingest._new_usage_record(Path("sample.pdf"), "X-test", "test-model")
        client = Mock()
        client.chat.completions.create.side_effect = [
            OSError("response unavailable"),
            Mock(
                id="gen-test",
                usage=Mock(prompt_tokens=21, completion_tokens=8, cost=0.000123),
                choices=[Mock(finish_reason="stop", message=Mock(content="ok"))],
            ),
        ]
        pdf_ingest.ACTIVE_DOCUMENT_USAGE = record
        try:
            with patch("time.sleep"):
                self.assertEqual(pdf_ingest._chat(client, "test-model", "sys", "source", 100, tries=2), "ok")
        finally:
            pdf_ingest.ACTIVE_DOCUMENT_USAGE = None

        self.assertEqual(record["tokens_in"], 21)
        self.assertEqual(record["tokens_out"], 8)
        self.assertEqual(record["cost_usd"], 0.000123)
        self.assertFalse(record["cost_exact"])
        self.assertEqual(record["request_attempts"], 2)
        self.assertEqual(record["retries"], 1)
        self.assertEqual(record["generation_ids"], ["gen-test"])

    def test_chat_marks_cost_inexact_when_usage_is_missing(self):
        record = pdf_ingest._new_usage_record(Path("sample.pdf"), "X-test", "test-model")
        client = Mock()
        client.chat.completions.create.return_value = Mock(
            id="gen-no-usage",
            usage=None,
            choices=[Mock(finish_reason="stop", message=Mock(content="ok"))],
        )
        pdf_ingest.ACTIVE_DOCUMENT_USAGE = record
        try:
            self.assertEqual(pdf_ingest._chat(client, "test-model", "sys", "source", 100), "ok")
        finally:
            pdf_ingest.ACTIVE_DOCUMENT_USAGE = None

        self.assertFalse(record["cost_exact"])
        self.assertFalse(pdf_ingest.USAGE["cost_exact"])
        self.assertEqual(record["generation_ids"], [])

    def test_usage_log_appends_one_jsonl_record(self):
        with tempfile.TemporaryDirectory() as temp:
            log_path = Path(temp) / "usage.jsonl"
            record = pdf_ingest._new_usage_record(Path("report.pdf"), "12345", "test-model")
            with patch.object(pdf_ingest, "USAGE_LOG_PATH", log_path):
                pdf_ingest._append_usage_record(record)

            lines = log_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(json.loads(lines[0])["file"], "report.pdf")
            self.assertIn("completed_at", json.loads(lines[0]))

    def test_synthesize_note_retries_truncated_output_with_larger_budget(self):
        valid_note = "---\ntitle: Test\n---\n\n" + "\n\n".join(
            f"{header}\nText." for header in pdf_ingest.REQUIRED_HEADERS
        )
        with patch.object(
            pdf_ingest,
            "_chat",
            side_effect=[pdf_ingest._OutputTruncatedError("truncated"), valid_note],
        ) as chat:
            result = pdf_ingest.synthesize_note(None, "test", "source")

        self.assertEqual(result, valid_note)
        self.assertEqual([call.kwargs["max_tokens"] for call in chat.call_args_list], [4500, 9000])

    def test_ingest_model_defaults_to_haiku_and_uses_ingest_override(self):
        with patch.dict(os.environ, {"OPENROUTER_MODEL": "anthropic/claude-sonnet-5.5"}, clear=True):
            self.assertEqual(pdf_ingest.ingest_model(), "anthropic/claude-haiku-5.5")
        with patch.dict(os.environ, {"OPENROUTER_INGEST_MODEL": "anthropic/claude-sonnet-5.5"}, clear=True):
            self.assertEqual(pdf_ingest.ingest_model(), "anthropic/claude-sonnet-5.5")

    def test_existing_note_lookup_matches_minckley_id_only(self):
        catalog = [
            ("same-title", "98765", "same-doi", "Report title", "2024"),
            ("same-mid", "12345", "other-doi", "Unrelated title", "1990"),
        ]

        self.assertEqual(pdf_ingest.existing_note_for_minckley_id("12345", catalog), "same-mid")
        self.assertEqual(pdf_ingest.existing_note_for_minckley_id("98765", catalog), "same-title")
        self.assertEqual(pdf_ingest.existing_note_for_minckley_id("11111", catalog), "")
        self.assertEqual(pdf_ingest.existing_note_for_minckley_id("", catalog), "")

    def test_long_document_timeout_defaults_to_hard_cap(self):
        with patch.object(pdf_ingest, "_price", return_value=(1e-7, 5e-7)), patch.object(
            pdf_ingest, "_input_with_timeout", return_value=None
        ) as input_with_timeout:
            limit = pdf_ingest.choose_limit("long.pdf", 300_000, 100, "test-model")

        self.assertEqual(limit, pdf_ingest.MAX_NOTE_CHARS)
        input_with_timeout.assert_called_once_with(
            unittest.mock.ANY, pdf_ingest.LONG_DOC_PROMPT_TIMEOUT
        )

    def test_process_only_skips_existing_minckley_id(self):
        with tempfile.TemporaryDirectory() as temp:
            ordinary = Path(temp) / "ordinary-report.pdf"
            known_mid = Path(temp) / "12345.pdf"
            ordinary.write_bytes(b"ordinary PDF")
            known_mid.write_bytes(b"Minckley PDF")
            ordinary_hash = pdf_ingest.file_hash(ordinary)
            manifest = {ordinary_hash: {"file": ordinary.name, "status": "done", "note": "Earlier.md"}}
            extracted = {"text": "text", "pages": 1, "ocr_pages": [], "method": "text", "metadata": {}}
            args = SimpleNamespace(
                files=[str(known_mid), str(ordinary)], mid="", limit=0, model="", long="cap",
                no_crossref=True, yes=False, type="", keep=True,
            )
            with patch.object(pdf_ingest.StubStore, "require_consolidated"), patch.object(
                pdf_ingest, "_load_json", side_effect=[manifest, {}]
            ), patch.object(pdf_ingest, "_save_json") as save_json, patch.object(
                pdf_ingest,
                "_vault_catalog",
                return_value=[("Existing.md", "12345", "", "Different title", "1990")],
            ), patch.object(pdf_ingest, "quick_estimate", return_value=(100, 1, 0)), patch.object(
                pdf_ingest, "choose_limit", return_value=pdf_ingest.MAX_NOTE_CHARS
            ), patch.object(pdf_ingest, "extract_text", return_value=extracted) as extract, patch.object(
                pdf_ingest, "free_citation", return_value={"citation_source": "filename"}
            ), patch.object(pdf_ingest, "_cost_text", return_value="estimated $0"), patch(
                "builtins.input", return_value="n"
            ), patch.object(pdf_ingest, "_append_usage_record") as append_record:
                result = pdf_ingest.cmd_process(args)

            self.assertEqual(result, 0)
            extract.assert_called_once_with(ordinary, ordinary_hash)
            self.assertTrue(ordinary.exists())
            saved_manifest = save_json.call_args.args[1]
            self.assertEqual(saved_manifest[pdf_ingest.file_hash(known_mid)]["status"], "skipped")
            self.assertIn("Minckley ID 12345", saved_manifest[pdf_ingest.file_hash(known_mid)]["reason"])
            records = [call.args[0] for call in append_record.call_args_list]
            self.assertEqual(
                {record["result"] for record in records},
                {"skipped_existing_minckley_id", "cancelled_before_send"},
            )
            self.assertEqual(len(records), 2)


if __name__ == "__main__":
    unittest.main()