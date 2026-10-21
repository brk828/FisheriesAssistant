import copy
import hashlib
import json
from pathlib import Path
import shutil
import socket
import sys
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import MagicMock, patch

import yaml

from utils import rag_library as rag


class RagLibraryTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="fisheries-rag-"))
        self.sources = self.root / "00_Fisheries_Brain" / "01_Sources"
        self.sources.mkdir(parents=True)
        self.config_path = self.root / "approved.yaml"
        self.artifact = self.root / "export"
        self.base = patch.object(rag, "BASE_DIR", self.root)
        self.refs = patch.object(rag.brain_citations, "load", return_value={
            "X-test": {"authors": "Recorded Author", "year": "2020",
                       "title": "Recorded title", "publication": "Journal"},
            "12345": {"title": "Filename MID title"},
            "Legacy": {"authors": "Recovered Author", "title": "Recovered title"},
        })
        self.base.start()
        self.refs.start()
        self.addCleanup(self.base.stop)
        self.addCleanup(self.refs.stop)
        self.addCleanup(lambda: shutil.rmtree(self.root))
        self.config = {"version": 1, "sources": [], "aliases": {
            "xyrauchen texanus": ["razorback sucker"]},
            "chunks": {"max_chars": 240, "overlap_chars": 20}}

    def approve(self, name="Note.md", sid="X-test", species=None, body=None, extra_metadata=None):
        path = self.sources / name
        text = ("---\n" + yaml.safe_dump({"source_id": sid, "title": "Note title",
                    "region": "Colorado", **(extra_metadata or {})}) + "---\n" +
                (body or "# Note\n## Methods\nCPUE count abundance standardized effort.\n"
                 "## Biology\nGrowth and survival in Colorado.\n"))
        path.write_text(text, encoding="utf-8")
        entry = {"path": f"00_Fisheries_Brain/01_Sources/{name}",
                 "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                 "review_finalized": True,
                 "redistribution": {"approved": True, "basis": "Written permission ABC"},
                 "evidence_level": "condensed-note",
                 "tracks": ["methodological", "biological"],
                 "species": species or ["Xyrauchen texanus"]}
        self.config["sources"].append(entry)
        return entry

    def build(self, destination=None):
        self.config_path.write_text(yaml.safe_dump(self.config), encoding="utf-8")
        return rag.build_export(self.config_path, destination or self.artifact)

    def query(self, **kwargs):
        return rag.query_export(self.artifact,
                                kwargs.pop("request", {"track": "methodological", "goal": "CPUE"}),
                                mode=kwargs.pop("mode", "lexical"), **kwargs)

    def test_empty_example_exports_no_automatic_sources(self):
        self.approve()
        self.config["sources"] = []
        manifest = self.build()
        self.assertEqual(manifest["records"], 0)
        pack = self.query()
        self.assertTrue(pack["abstained"])
        self.assertEqual(pack["evidence"], [])

    def test_permissions_and_stale_approval(self):
        approval = self.approve()
        mutations = [{"review_finalized": False}, {"review_finalized": "true"},
                     {"redistribution": {"approved": False, "basis": "yes"}},
                     {"redistribution": {"approved": True, "basis": ""}},
                     {"evidence_level": "probably"}, {"sha256": "0" * 64}]
        for changes in mutations:
            with self.subTest(changes=changes):
                self.config["sources"] = [{**approval, **changes}]
                with self.assertRaises(rag.RagError):
                    self.build()
                self.assertFalse(self.artifact.exists())
        self.config["sources"] = [approval]
        (self.sources / "Note.md").write_text("changed", encoding="utf-8")
        with self.assertRaisesRegex(rag.RagError, "Stale"):
            self.build()

    def test_only_allowlisted_sources_and_no_network_at_query(self):
        self.approve()
        (self.sources / "Secret.md").write_text("# Secret\ncryptic-unexported", encoding="utf-8")
        self.build()
        with patch.object(rag.brain_citations, "load", side_effect=AssertionError("vault access")), \
             patch.object(socket, "create_connection", side_effect=AssertionError("network")), \
             patch.object(rag, "_backend", side_effect=AssertionError("optional import")):
            self.assertFalse(self.query()["abstained"])
            self.assertTrue(self.query(request={"track": "methodological",
                                               "goal": "cryptic-unexported"})["abstained"])

    def test_path_traversal_absolute_and_non_source_rejected(self):
        approval = self.approve()
        for path in ("../Note.md", "/etc/passwd", "00_Fisheries_Brain/02_Brain/Note.md",
                     "00_Fisheries_Brain/01_Sources/nested/Note.md",
                     "00_Fisheries_Brain/01_Sources/../01_Sources/Note.md",
                     "00_Fisheries_Brain\\01_Sources\\Note.md"):
            with self.subTest(path=path):
                self.config["sources"] = [{**approval, "path": path}]
                with self.assertRaises(rag.RagError):
                    self.build()

    def test_source_symlink_and_parent_symlink_rejected(self):
        approval = self.approve()
        note = self.sources / "Note.md"
        outside = self.root / "outside.md"
        note.rename(outside)
        note.symlink_to(outside)
        with self.assertRaisesRegex(rag.RagError, "Symlink"):
            self.build()
        note.unlink()
        outside.rename(note)
        real = self.root / "real-sources"
        self.sources.rename(real)
        self.sources.symlink_to(real, target_is_directory=True)
        with self.assertRaisesRegex(rag.RagError, "Symlink"):
            self.build()

    def test_canonical_citations_preserve_filename_identity(self):
        self.approve(name="Different_2024.md")
        self.approve(name="Paper_12345.md", sid="")
        self.approve(name="Legacy.md", sid="unknown-id")
        self.approve(name="Scanned.md", sid="12345 (scanned)")
        self.approve(name="Missing.md", sid="X-absent")
        self.build()
        _, records = rag.load_export(self.artifact)
        by_name = {r["filename"]: r for r in records}
        self.assertEqual(by_name["Different_2024.md"]["source_id"], "X-test")
        self.assertEqual(by_name["Different_2024.md"]["citation"]["authors"], "Recorded Author")
        self.assertEqual(by_name["Paper_12345.md"]["source_id"], "12345")
        self.assertEqual(by_name["Legacy.md"]["source_id"], "unknown-id")
        self.assertEqual(by_name["Legacy.md"]["citation_lookup_key"], "Legacy")
        self.assertEqual(by_name["Legacy.md"]["frontmatter_source_id"], "unknown-id")
        self.assertEqual(by_name["Scanned.md"]["source_id"], "12345")
        self.assertEqual(by_name["Missing.md"]["citation_status"], "unverified-missing")
        self.assertNotIn("authors", by_name["Missing.md"]["citation"])

    def test_heading_chunks_stability_bounds_and_code_fences(self):
        body = "# Title\n## Methods\n" + "abundance " * 100 + "\n### Model\nfit\n" \
            "```\n# not a heading\n```\n## Results\nCPUE."
        chunks = rag.chunk_markdown(body, 240, 20)
        self.assertEqual(chunks, rag.chunk_markdown(body, 240, 20))
        self.assertTrue(all(len(c["text"]) <= 240 for c in chunks))
        self.assertEqual(chunks[0]["section"], "Title / Methods")
        self.assertIn("# not a heading", next(c["text"] for c in chunks
                                            if c["section"].endswith("Model")))
        self.approve(body=body)
        first = self.build()
        second = self.build(self.root / "second")
        self.assertEqual(first, second)
        records = json.loads((self.artifact / "records.json").read_text())
        self.assertEqual(len({r["evidence_id"] for r in records}), len(records))
        self.assertEqual(records[0]["source_metadata"]["region"], "Colorado")
        self.assertTrue((self.artifact / records[0]["snapshot"]).is_file())

    def test_no_overwrite_and_failed_build_is_unpublished(self):
        self.approve()
        self.artifact.mkdir()
        with self.assertRaisesRegex(rag.RagError, "already exists"):
            self.build()
        self.artifact.rmdir()
        self.config["embedding"] = {}
        with patch.object(rag, "_versions", return_value=rag.PINS):
            with self.assertRaises(rag.RagError):
                self.build()
        self.assertFalse(self.artifact.exists())
        self.assertEqual(list(self.root.glob("*.building-*")), [])

    def test_publication_lock_does_not_reserve_destination_and_cleans_up(self):
        self.approve()
        original_rename = Path.rename
        lock = self.root / "export.publish.lock"

        def rename(source, target):
            self.assertFalse(Path(target).exists())
            self.assertTrue(lock.is_file())
            return original_rename(source, target)

        with patch.object(Path, "rename", new=rename):
            self.build()
        self.assertFalse(lock.exists())
        self.assertTrue((self.artifact / "manifest.json").is_file())

    def test_publication_lock_busy_and_rename_failure_leave_no_artifact(self):
        self.approve()
        lock = self.root / "export.publish.lock"
        lock.write_text("another builder", encoding="utf-8")
        with self.assertRaisesRegex(rag.RagError, "publication lock"):
            self.build()
        self.assertTrue(lock.exists())
        self.assertFalse(self.artifact.exists())
        lock.unlink()
        with patch.object(Path, "rename", side_effect=OSError("rename failure")):
            with self.assertRaisesRegex(OSError, "rename failure"):
                self.build()
        self.assertFalse(lock.exists())
        self.assertFalse(self.artifact.exists())
        self.assertEqual(list(self.root.glob("*.building-*")), [])

    def test_allowlist_order_does_not_change_export(self):
        self.approve(name="Zebra.md")
        self.approve(name="Alpha.md")
        first = self.build()
        self.config["sources"].reverse()
        second = self.build(self.root / "second")
        self.assertEqual(first, second)

    def test_manifest_and_record_checksum_validation(self):
        self.approve()
        self.build()
        records = self.artifact / "records.json"
        original = records.read_bytes()
        records.write_bytes(original + b" ")
        with self.assertRaisesRegex(rag.RagError, "checksum"):
            self.query()
        records.write_bytes(original)
        manifest_path = self.artifact / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["chunker"] = "unknown"
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(rag.RagError, "Manifest checksum"):
            self.query()

    def test_manifest_file_traversal_and_symlinks_rejected(self):
        self.approve()
        self.build()
        manifest_path = self.artifact / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["files"]["../outside"] = "bogus"
        manifest.pop("manifest_sha256")
        manifest["manifest_sha256"] = rag._sha(rag._json(manifest).encode())
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaises(rag.RagError):
            self.query()

    def test_unapproved_artifact_files_and_symlinks_rejected(self):
        self.approve()
        self.build()
        extra = self.artifact / "extra.json"
        extra.write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(rag.RagError, "unapproved"):
            self.query()
        extra.unlink()
        records = self.artifact / "records.json"
        outside = self.root / "records-outside.json"
        records.rename(outside)
        records.symlink_to(outside)
        with self.assertRaisesRegex(rag.RagError, "symlink"):
            self.query()

    def test_species_isolation_alias_and_missing_species(self):
        self.approve()
        self.approve(name="Trout.md", species=["Oncorhynchus mykiss"])
        self.build()
        for species in ("razorback sucker", "Xyrauchen texanus"):
            result = self.query(request={"track": "biological", "species": species,
                                         "parameter": "growth", "region": "Colorado"})
            self.assertFalse(result["abstained"])
            self.assertTrue(all(e["filename"] == "Note.md" for e in result["evidence"]))
        result = self.query(request={"track": "biological", "species": "Unrelated taxon",
                                     "parameter": "growth"})
        self.assertTrue(result["abstained"])
        self.assertEqual(result["retrieval"]["scoped_chunks"], 0)
        with self.assertRaisesRegex(rag.RagError, "species"):
            self.query(request={"track": "biological", "parameter": "growth"})

    def test_biological_parameter_required_and_taxon_context_alone_cannot_match(self):
        self.approve()
        self.build()
        with self.assertRaisesRegex(rag.RagError, "parameter"):
            self.query(request={"track": "biological", "species": "razorback sucker"})
        result = self.query(request={"track": "biological", "species": "razorback sucker",
                                     "parameter": "unrepresented_parameter", "region": "Colorado"})
        self.assertTrue(result["abstained"])
        result = self.query(request={"track": "biological", "species": "razorback sucker",
                                     "parameter": "growth"})
        self.assertFalse(result["abstained"])
        self.assertTrue(all("Biology" in e["section"] for e in result["evidence"]))

    def test_exported_gear_geography_metadata_and_review_status(self):
        self.approve(extra_metadata={
            "gear_types": ["seine"], "location": "Grand Canyon",
            "geographic_region": "Southwest", "region_aliases": ["Colorado basin"],
            "gear_aliases": ["beach seine"]})
        self.build()
        result = self.query(request={"track": "methodological", "goal": "seine"})
        self.assertFalse(result["abstained"])
        item = result["evidence"][0]
        self.assertEqual(item["source_metadata"]["gear_types"], ["seine"])
        self.assertEqual(item["source_metadata"]["location"], "Grand Canyon")
        self.assertEqual(item["source_metadata"]["region_aliases"], ["Colorado basin"])
        self.assertTrue(item["review_finalized"])
        self.assertIsInstance(item["offset"], int)

    def test_ambiguous_aliases_rejected(self):
        self.config["aliases"] = {"taxon a": ["same"], "taxon b": ["same"]}
        with self.assertRaisesRegex(rag.RagError, "Ambiguous"):
            self.build()

    def test_context_field_names_are_not_retrieval_evidence(self):
        self.approve()
        self.build()
        result = self.query(request={"track": "methodological", "methods": "unexported-unique"})
        self.assertTrue(result["abstained"])
        self.assertEqual(result["retrieval"]["matching_chunks"], 0)

    def test_weak_semantic_only_matches_abstain_stronger_remain_candidates(self):
        self.approve()
        self.build()
        _, records = rag.load_export(self.artifact)
        eid = records[0]["evidence_id"]
        request = {"track": "methodological", "goal": "randomunexportedtoken"}
        with patch.object(rag, "_semantic_query", return_value={eid: 0.2}):
            result = self.query(mode="auto", request=request)
        self.assertTrue(result["abstained"])
        self.assertEqual(result["retrieval"]["rejected_semantic_neighbors"], 1)
        with patch.object(rag, "_semantic_query", return_value={eid: 0.9}):
            result = self.query(mode="auto", request=request)
        self.assertEqual(result["status"], "candidates-pending-review")
        self.assertEqual(result["evidence"][0]["match_kind"], "semantic-only-unverified")
        self.assertEqual(result["retrieval"]["support_status"],
                         "unverified-candidates-not-scientific-support")

    def test_bounds_caveats_and_structured_context(self):
        self.approve(body="# Methods\n" + "CPUE abundance. " * 150)
        self.build()
        result = self.query(limit=2, max_chars=5000,
                            request={"track": "methodological", "goal": "CPUE",
                                     "data": {"format": "counts"}, "design": "repeated",
                                     "methods": ["count regression"]})
        self.assertLessEqual(len(result["evidence"]), 2)
        self.assertLessEqual(len(rag._json(result)), 5000)
        self.assertEqual(result["status"], "candidates-pending-review")
        self.assertIn("validator rules", result["caveats"][0])
        self.assertIn("unverified", result["caveats"][1])
        for kwargs in ({"limit": 13}, {"max_chars": 999}, {"mode": "online"}):
            with self.assertRaises(rag.RagError):
                self.query(**kwargs)

    def test_optional_dependencies_fallback_and_explicit_failure(self):
        self.approve()
        self.build()
        result = self.query(mode="auto")
        self.assertEqual(result["retrieval"]["mode"], "lexical")
        self.assertIn("no approved local", result["retrieval"]["fallback_reason"])
        with self.assertRaises(rag.SemanticUnavailable):
            self.query(mode="semantic")
        with patch.object(rag.metadata, "version", side_effect=rag.metadata.PackageNotFoundError):
            with self.assertRaisesRegex(rag.SemanticUnavailable, "Missing optional"):
                rag._versions()

    def test_offline_guard_blocks_connect_and_dns_then_restores(self):
        old = socket.getaddrinfo
        with rag._offline():
            with self.assertRaises(rag.SemanticUnavailable):
                socket.create_connection(("example.com", 443))
            with self.assertRaises(rag.SemanticUnavailable):
                socket.getaddrinfo("example.com", 443)
        self.assertIs(socket.getaddrinfo, old)

    def model_spec(self):
        root = self.root / "approved-model"
        root.mkdir()
        files = {"config.json": b"{}", "modules.json": b"[]",
                 "model.safetensors": b"test-only-not-a-real-model",
                 "LICENSE": b"Synthetic test fixture license text, not a real model license."}
        for name, raw in files.items():
            (root / name).write_bytes(raw)
        return {"path": str(root), "revision": "a" * 40, "license": "Apache-2.0",
                "license_file": "LICENSE",
                "redistribution_approved": True,
                "files": {name: rag._sha(raw) for name, raw in files.items()}}

    def test_approved_model_copy_and_no_unapproved_files(self):
        spec = self.model_spec()
        (Path(spec["path"]) / "unapproved.bin").write_bytes(b"not copied")
        target = self.root / "packaged-model"
        packaged = rag._model_copy(spec, target)
        self.assertNotIn("path", packaged)
        self.assertEqual(packaged["license_file"], "LICENSE")
        self.assertFalse((target / "unapproved.bin").exists())
        self.assertEqual(packaged["files"], spec["files"])
        for changes in ({"revision": "main"}, {"license": ""}, {"redistribution_approved": False},
                        {"license_file": ""}, {"license_file": "not-allowlisted.txt"},
                        {"license_file": "model.safetensors"},
                        {"files": {"../bad": "abc"}}, {"files": {"model.safetensors": "bad"}}):
            with self.subTest(changes=changes):
                with self.assertRaises(rag.RagError):
                    rag._model_copy({**spec, **changes}, self.root / "invalid-model")

    def test_empty_model_license_text_rejected(self):
        spec = self.model_spec()
        license_path = Path(spec["path"]) / "LICENSE"
        license_path.write_text("  \n", encoding="utf-8")
        spec["files"]["LICENSE"] = rag._file_sha(license_path)
        with self.assertRaisesRegex(rag.RagError, "license text must not be empty"):
            rag._model_copy(spec, self.root / "invalid-model")

    def test_model_custom_code_and_pickle_rejected(self):
        spec = self.model_spec()
        root = Path(spec["path"])
        for name, content in (("config.json", b'{"auto_map": {}}'),
                              ("modules.json", b'[{"type": "custom.remote.Model", "path": ""}]'),
                              ("weights.bin", b"pickle")):
            (root / name).write_bytes(content)
            changed = copy.deepcopy(spec)
            changed["files"] = {"model.safetensors": spec["files"]["model.safetensors"],
                                "LICENSE": spec["files"]["LICENSE"],
                                name: rag._sha(content)}
            with self.subTest(name=name):
                with self.assertRaises(rag.RagError):
                    rag._model_copy(changed, self.root / ("invalid-" + name))

    def test_mock_semantic_build_uses_documents_parser_and_vectors(self):
        records = [{"text": "CPUE abundance", "evidence_id": "E-test"}]
        chroma, settings, Document, Storage, Index, Splitter, Store, embed = (
            MagicMock() for _ in range(8))
        node = MagicMock()
        node.text = "CPUE abundance"
        Splitter.return_value.get_nodes_from_documents.return_value = [node]
        embed.get_text_embedding.return_value = [0.1, 0.2]
        with patch.object(rag, "_backend", return_value=(
                chroma, settings, Document, Storage, Index, Splitter, Store, embed)):
            rag._semantic_build(self.root, records)
        Document.assert_called_once_with(text="CPUE abundance", id_="E-test")
        Splitter.return_value.get_nodes_from_documents.assert_called_once()
        self.assertIs(Splitter.call_args.kwargs["tokenizer"], list)
        self.assertEqual(Splitter.call_args.kwargs["chunking_tokenizer_fn"]("CPUE"), ["CPUE"])
        Index.assert_called_once()
        self.assertEqual(Index.call_args.kwargs["transformations"], [Splitter.return_value])
        self.assertEqual(node.id_, "E-test")
        self.assertEqual(records[0]["embedding"], [0.1, 0.2])
        chroma.PersistentClient.assert_called_once()
        chroma.PersistentClient.return_value._system.stop.assert_called_once()

    def test_backend_passes_explicit_offline_safe_model_configuration(self):
        modules = {name: MagicMock() for name in (
            "chromadb", "chromadb.config", "llama_index", "llama_index.core",
            "llama_index.core.bridge", "llama_index.core.bridge.pydantic",
            "llama_index.core.node_parser", "llama_index.core.schema",
            "llama_index.core.vector_stores", "llama_index.core.vector_stores.types",
            "llama_index.embeddings", "llama_index.embeddings.huggingface")}
        with patch.dict(sys.modules, modules), patch.object(rag, "_store_type"):
            rag._backend(self.root / "model")
        modules["llama_index.embeddings.huggingface"].HuggingFaceEmbedding.assert_called_once_with(
            model_name=str(self.root / "model"), cache_folder=str(self.root / "model"),
            device="cpu", trust_remote_code=False, local_files_only=True,
            model_kwargs={"use_safetensors": True}, normalize=True,
            query_instruction="", text_instruction="", show_progress_bar=False)

    def test_clean_chroma_local_bridge_add_query_and_no_mutation(self):
        class BaseStore:
            pass

        store_type = rag._store_type(
            BaseStore, lambda: None, SimpleNamespace, SimpleNamespace,
            SimpleNamespace(NONE="none"))
        collection = MagicMock()
        collection.query.return_value = {
            "ids": [["E-one"]], "documents": [["CPUE abundance"]],
            "distances": [[0.25]]}
        store = store_type(collection)
        node = MagicMock(node_id="E-one")
        node.get_embedding.return_value = [0.1, 0.2]
        node.get_content.return_value = "CPUE abundance"
        self.assertEqual(store.add([node]), ["E-one"])
        collection.add.assert_called_once_with(
            ids=["E-one"], embeddings=[[0.1, 0.2]], documents=["CPUE abundance"])
        request = SimpleNamespace(filters=None, node_ids=None, doc_ids=None,
                                  query_embedding=[0.2, 0.3], similarity_top_k=1)
        result = store.query(request)
        self.assertEqual(result.ids, ["E-one"])
        self.assertEqual(result.nodes[0].id_, "E-one")
        self.assertAlmostEqual(result.similarities[0], 0.778800783)
        collection.query.assert_called_once_with(
            query_embeddings=[[0.2, 0.3]], n_results=1, include=["documents", "distances"])
        with self.assertRaises(rag.RagError):
            store.delete("E-one")
        request.filters = {"species": "not-scoped"}
        with self.assertRaises(rag.RagError):
            store.query(request)
        collection.reset_mock()
        batched_store = store_type(collection, batch_size=1)
        batched_store.add([node, node])
        self.assertEqual(collection.add.call_count, 2)
        self.assertTrue(all(len(call.kwargs["ids"]) == 1
                            for call in collection.add.call_args_list))

    def test_batch_limits_support_pinned_property_and_newer_method(self):
        self.assertEqual(rag._batch_limit(SimpleNamespace(max_batch_size=3)), 3)
        self.assertEqual(rag._batch_limit(SimpleNamespace(get_max_batch_size=lambda: 7)), 7)
        self.assertEqual(rag._batch_limit(SimpleNamespace(max_batch_size=9999)), 512)
        self.assertEqual(rag._batch_limit(SimpleNamespace()), 512)

    def test_mock_query_in_memory_chroma_vector_retriever_and_versions(self):
        records = [{"text": "CPUE", "evidence_id": "E-one", "embedding": [0.1, 0.2]}]
        manifest = {"embedding": {"files": {"model.safetensors": "hash"}},
                    "packages": {**rag.PINS, "PyYAML": rag.metadata.version("PyYAML")},
                    "files": {"model/model.safetensors": "hash"}}
        chroma, settings, Document, Storage, Index, Splitter, Store, embed = (
            MagicMock() for _ in range(8))
        hit = MagicMock()
        hit.node.node_id = "E-one"
        hit.score = 0.8
        Index.from_vector_store.return_value.as_retriever.return_value.retrieve.return_value = [hit]
        with patch.object(rag, "_versions", return_value=rag.PINS), \
             patch.object(rag, "_backend", return_value=(
                chroma, settings, Document, Storage, Index, Splitter, Store, embed)):
            result = rag._semantic_query(self.root, manifest, records, "CPUE", 6)
        self.assertEqual(result, {"E-one": 0.8})
        chroma.EphemeralClient.assert_called_once()
        chroma.PersistentClient.assert_not_called()
        chroma.EphemeralClient.return_value.create_collection.return_value.add.assert_called_once_with(
            ids=["E-one"], documents=["CPUE"], embeddings=[[0.1, 0.2]])
        Index.from_vector_store.assert_called_once()
        self.assertEqual(Index.from_vector_store.call_args.kwargs["transformations"],
                         [Splitter.return_value])
        self.assertIs(Splitter.call_args.kwargs["tokenizer"], list)
        self.assertEqual(Splitter.call_args.kwargs["chunking_tokenizer_fn"]("query"), ["query"])
        with patch.object(rag, "_versions", return_value={**rag.PINS, "torch": "changed"}):
            with self.assertRaisesRegex(rag.SemanticUnavailable, "versions differ"):
                rag._semantic_query(self.root, manifest, records, "CPUE", 6)
        manifest["packages"]["torch"] = "recorded-but-now-missing"
        with patch.object(rag, "_versions", return_value=rag.PINS):
            with self.assertRaisesRegex(rag.SemanticUnavailable, "versions differ"):
                rag._semantic_query(self.root, manifest, records, "CPUE", 6)

    def test_cli_json_success_and_error(self):
        import io
        from contextlib import redirect_stdout
        self.approve()
        self.config_path.write_text(yaml.safe_dump(self.config), encoding="utf-8")
        output = io.StringIO()
        with redirect_stdout(output):
            status = rag.main(["build", "--config", str(self.config_path),
                               "--destination", str(self.artifact)])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output.getvalue())["version"], 1)
        output = io.StringIO()
        with redirect_stdout(output):
            status = rag.main(["query", "--artifact", str(self.artifact),
                               "--request", '{"track":"biological"}'])
        self.assertEqual(status, 2)
        self.assertIn("error", json.loads(output.getvalue()))


if __name__ == "__main__":
    unittest.main()
