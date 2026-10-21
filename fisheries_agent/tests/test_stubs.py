import tempfile
import unittest
from pathlib import Path

from utils import pdf_ingest
from utils.stub_store import StubStore, StubStoreError, bucket, parse_legacy, parse_letter_file

NOTE = """---
title: T
---
# T

## Executive Summary
The [[Colorado River]] holds [[Razorback Sucker]], [[2,4-D]] and [[Élan Creek]].
"""

LEGACY = "---\r\ntype: concept\r\nauto_enriched: true\r\n---\r\n# Spikedace\r\n\r\n## Summary\r\nA minnow.\r\n\r\n## Context\r\n> quote\r\n> -- *[[a]]*\r\n\r\n## Mentioned In\r\n- [[a]]\r\n"


class StubStoreTests(unittest.TestCase):
    def test_bucket(self):
        self.assertEqual(bucket("Colorado River"), "C")
        self.assertEqual(bucket("élan"), "E")
        self.assertEqual(bucket("2,4-D"), "MISC")
        self.assertEqual(bucket("[[x"), "X")

    def test_legacy_parse_and_roundtrip(self):
        stub = parse_legacy(LEGACY, "Spikedace")
        self.assertEqual((stub.summary, stub.mentions), ("A minnow.", ["- [[a]]"]))
        self.assertIn("auto_enriched", stub.meta)
        with tempfile.TemporaryDirectory() as d:
            store = StubStore(Path(d))
            store.create("Spikedace").merge(stub)
            store.flush()
            back = StubStore(Path(d)).get("spikedace")
            self.assertEqual((back.summary, back.context, back.mentions), (stub.summary, stub.context, stub.mentions))
            self.assertIn("# Spikedace", back.legacy_text())

    def test_update_appends_to_letter_files(self):
        with tempfile.TemporaryDirectory() as d:
            store = StubStore(Path(d))
            _, created = pdf_ingest.update_stubs("T", NOTE, store)
            self.assertEqual(len(created), 4)
            self.assertEqual(sorted(p.name for p in Path(d).iterdir()), ["Stubs_C.md", "Stubs_E.md", "Stubs_MISC.md", "Stubs_R.md"])
            n, created = pdf_ingest.update_stubs("T", NOTE, StubStore(Path(d)))
            self.assertEqual((n, created), (0, []))
            n, _ = pdf_ingest.update_stubs("U", NOTE, StubStore(Path(d)))
            stub = StubStore(Path(d)).get("Colorado River")
            self.assertEqual((n, stub.mentions), (4, ["- [[T]]", "- [[U]]"]))
            self.assertEqual(stub.context.count("> -- *[["), 2)

    def test_duplicate_blocks_merge(self):
        text = "# x\n## A\n### Mentioned In\n- [[1]]\n\n## A\n### Summary\nS\n### Mentioned In\n- [[2]]\n"
        stubs = parse_letter_file(text)
        self.assertEqual((len(stubs), stubs["a"].summary, stubs["a"].mentions), (1, "S", ["- [[1]]", "- [[2]]"]))

    def test_writes_refused_until_consolidated(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "Old.md").write_text(LEGACY, encoding="utf-8")
            store = StubStore(Path(d))
            self.assertEqual([s.name for s in store.iter_stubs()], ["Old"])
            with self.assertRaises(StubStoreError):
                store.create("New")


if __name__ == "__main__":
    unittest.main()
