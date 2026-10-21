"""Opt-in, approved Markdown exports and offline evidence retrieval.

No ingestion, agent, skill, or execution hooks. Lexical exports require only PyYAML.
Semantic exports additionally require requirements-rag.txt and an already-downloaded,
approved safetensors SentenceTransformer. Query never opens persisted Chroma: it
populates an ephemeral collection from checksummed packaged vectors.

Artifacts are integrity checked, not cryptographically signed; trust the publisher.
The local bridge uses Chroma 0.4.16, outside the four published advisory ranges.
Never serve artifacts, use HttpClient, or accept untrusted databases/model files.
Semantic publication on Windows is unvalidated: pinned Chroma has no public client
close(), and its low-level system stop may not release every HNSW native handle.
"""

import argparse
from contextlib import contextmanager, redirect_stdout
import hashlib
from importlib import metadata
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import socket
import sys
import uuid

import yaml

from utils import brain_citations

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_REL = PurePosixPath("00_Fisheries_Brain/01_Sources")
VERSION = 1
CHUNKER = "heading-characters-v1"
MAX_SOURCE_BYTES = 2_000_000
MIN_SEMANTIC_SCORE = 0.5
PINS = {
    "llama-index-core": "0.14.25",
    "llama-index-embeddings-huggingface": "0.8.0",
    "chromadb": "0.4.16",
    "sentence-transformers": "6.2.0",
    "numpy": "1.26.4",
}
TRACK_FIELDS = {
    "methodological": ("goal", "data", "design", "methods"),
    "biological": ("species", "parameter", "population", "life_stage",
                   "region", "season", "units"),
}
SOURCE_METADATA_FIELDS = tuple(dict.fromkeys(
    TRACK_FIELDS["biological"] + TRACK_FIELDS["methodological"] +
    ("target_species", "related_species", "scientific_name", "common_name",
     "species_aliases", "gear", "gear_type", "gear_types", "gear_aliases",
     "sampling_gear", "habitat", "location", "locations", "geographic_region",
     "geography", "geographic_aliases", "geography_aliases", "location_aliases",
     "region_aliases", "study_design", "sampling_design", "study_type",
     "analytical_category", "model_framework")))
CAVEATS = [
    "Retrieved notes are evidence leads, not scientific values, requirements, "
    "package mandates, validator rules, or approval to run an analysis.",
    "Applicability to the requested design, population, life stage, region, season "
    "and units is unverified; missing context is not a match.",
    "Conflicts are not resolved or automatically detected; compare originals and "
    "retain disagreements. Condensed notes are not original-paper verification.",
    "Semantic similarity is not calibrated scientific support. Semantic-only "
    "neighbors remain unverified candidates, even above the retrieval cutoff.",
    "Character-bounded chunks may split equations or qualifications. Section offsets "
    "are retained; inspect the approved snapshot and original before use.",
]


class RagError(ValueError):
    """Invalid approval, artifact, or request."""


class SemanticUnavailable(RagError):
    """Explicit semantic setup is absent or incompatible."""


def _json(value):
    # YAML may parse date-like note metadata as datetime objects.
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str)


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _file_sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _write_json(path, value):
    path.write_text(_json(value) + "\n", encoding="utf-8")


def _relative(value):
    if not isinstance(value, str) or "\\" in value:
        raise RagError("Expected a portable relative POSIX path")
    p = PurePosixPath(value)
    if p.is_absolute() or not p.parts or any(x in (".", "..") for x in value.split("/")):
        raise RagError("Absolute paths and traversal are not allowed here")
    if ":" in value:
        raise RagError("Drive paths are not allowed")
    return p


def _safe_file(root, relative):
    p = _relative(relative)
    current = root
    for part in p.parts:
        current = current / part
        if current.is_symlink():
            raise RagError(f"Symlinks are not allowed: {relative}")
    if not current.is_file() or not current.resolve().is_relative_to(root.resolve()):
        raise RagError(f"File is absent or outside its root: {relative}")
    return current


def _strings(value, label):
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        raise RagError(f"{label} must be a list of nonempty strings")
    return sorted(set(v.strip() for v in value))


def _aliases(value):
    if not isinstance(value, dict):
        raise RagError("aliases must map canonical labels to lists of aliases")
    result = {}
    for name, aliases in value.items():
        if not isinstance(name, str) or not name.strip():
            raise RagError("Alias canonical labels must be nonempty strings")
        result[name.casefold()] = [v.casefold() for v in _strings(aliases, "aliases")]
    # Ambiguous taxa must never silently broaden biological matching.
    seen = {}
    for name, alternatives in result.items():
        for term in [name, *alternatives]:
            if term in seen and seen[term] != name:
                raise RagError(f"Ambiguous alias: {term}")
            seen[term] = name
    return result


def _frontmatter(text):
    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not match:
        return {}, text
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise RagError("Source frontmatter must be a mapping")
    return data, text[match.end():]


def chunk_markdown(body, max_chars=1800, overlap_chars=160):
    """Heading paths and bounded overlapping character slices; no heading mixing."""
    if not 200 <= max_chars <= 8000 or not 0 <= overlap_chars < max_chars // 2:
        raise RagError("chunks require 200..8000 max_chars and overlap < max_chars/2")
    sections, headings, lines, fenced = [], [], [], False
    for line in body.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        heading = None if fenced else re.match(r"^(#{1,6})[ \t]+(.+?)\s*#*\s*$", line)
        if heading:
            if lines:
                sections.append((" / ".join(h[1] for h in headings), "".join(lines)))
            level = len(heading.group(1))
            headings = [h for h in headings if h[0] < level]
            headings.append((level, heading.group(2)))
            lines = []
        else:
            lines.append(line)
    if lines:
        sections.append((" / ".join(h[1] for h in headings), "".join(lines)))
    chunks = []
    for section, text in sections:
        text = text.strip()
        start = 0
        while start < len(text):
            end = min(start + max_chars, len(text))
            window = text[start:end]
            excerpt = window.strip()
            if excerpt:
                offset = start + len(window) - len(window.lstrip())
                chunks.append({"section": section, "offset": offset, "text": excerpt})
            if end == len(text):
                break
            start = end - overlap_chars
    return chunks


def _versions():
    result = {}
    for name in PINS:
        try:
            result[name] = metadata.version(name)
        except metadata.PackageNotFoundError as exc:
            raise SemanticUnavailable(
                f"Missing optional {name}; install requirements-rag.txt or use lexical mode"
            ) from exc
        if result[name] != PINS[name]:
            raise SemanticUnavailable(f"{name} must be {PINS[name]}, found {result[name]}")
    # Include transitive numerical/tokenizer/runtime versions, not just top-level pins.
    for name in ("torch", "transformers", "tokenizers", "huggingface-hub",
                 "safetensors", "onnxruntime", "pydantic", "chroma-hnswlib"):
        try:
            result[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            pass
    return result


@contextmanager
def _offline():
    """Defense in depth: offline HF flags plus a network-denial guard, including imports.

    This process-global guard is intended for the local CLI, not concurrent servers.
    """
    flags = {"HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1",
             "HF_HUB_DISABLE_TELEMETRY": "1", "ANONYMIZED_TELEMETRY": "False"}
    old = {key: os.environ.get(key) for key in flags}
    connect, connect_ex, create, resolve = (
        socket.socket.connect, socket.socket.connect_ex, socket.create_connection, socket.getaddrinfo)

    def denied(*args, **kwargs):
        raise SemanticUnavailable("Networking is disabled for RAG model loading and retrieval")

    os.environ.update(flags)
    socket.socket.connect = socket.socket.connect_ex = socket.create_connection = denied
    socket.getaddrinfo = denied
    try:
        yield
    finally:
        socket.socket.connect, socket.socket.connect_ex, socket.create_connection = connect, connect_ex, create
        socket.getaddrinfo = resolve
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _batch_limit(client):
    method = getattr(client, "get_max_batch_size", None)
    reported = method() if callable(method) else getattr(client, "max_batch_size", 512)
    return min(512, reported) if isinstance(reported, int) and not isinstance(reported, bool) and reported > 0 else 512


def _store_type(BaseStore, PrivateAttr, TextNode, QueryResult, MetadataMode):
    """Minimal local bridge: newer official adapters require advisory-affected Chroma."""
    class LocalChromaStore(BaseStore):
        stores_text: bool = True
        _collection: object = PrivateAttr()
        _batch_size: int = PrivateAttr()

        def __init__(self, chroma_collection, batch_size=512):
            super().__init__()
            self._collection = chroma_collection
            self._batch_size = batch_size

        @property
        def client(self):
            return self._collection

        def add(self, nodes, **kwargs):
            ids = [node.node_id for node in nodes]
            for start in range(0, len(nodes), self._batch_size):
                batch = nodes[start:start + self._batch_size]
                self._collection.add(
                    ids=[node.node_id for node in batch],
                    embeddings=[node.get_embedding() for node in batch],
                    documents=[node.get_content(metadata_mode=MetadataMode.NONE) for node in batch])
            return ids

        def delete(self, ref_doc_id, **kwargs):
            raise RagError("Published evidence is immutable; deletion is not supported")

        def query(self, query, **kwargs):
            if query.filters or query.node_ids or query.doc_ids:
                raise RagError("Apply scope before populating the local Chroma collection")
            result = self._collection.query(
                query_embeddings=[query.query_embedding], n_results=query.similarity_top_k,
                include=["documents", "distances"])
            ids = result["ids"][0]
            return QueryResult(
                ids=ids,
                nodes=[TextNode(id_=eid, text=text)
                       for eid, text in zip(ids, result["documents"][0])],
                similarities=[math.exp(-distance) for distance in result["distances"][0]])

    return LocalChromaStore


def _backend(model_dir):
    try:
        import chromadb
        from chromadb.config import Settings
        from llama_index.core import Document, StorageContext, VectorStoreIndex
        from llama_index.core.bridge.pydantic import PrivateAttr
        from llama_index.core.node_parser import SentenceSplitter
        from llama_index.core.schema import MetadataMode, TextNode
        from llama_index.core.vector_stores.types import BasePydanticVectorStore, VectorStoreQueryResult
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    except ImportError as exc:
        raise SemanticUnavailable("Install requirements-rag.txt or use lexical mode") from exc
    embed = HuggingFaceEmbedding(
        model_name=str(model_dir), cache_folder=str(model_dir),
        device="cpu", trust_remote_code=False, local_files_only=True,
        model_kwargs={"use_safetensors": True}, normalize=True,
        query_instruction="", text_instruction="", show_progress_bar=False,
    )
    store = _store_type(BasePydanticVectorStore, PrivateAttr, TextNode,
                        VectorStoreQueryResult, MetadataMode)
    return chromadb, Settings, Document, StorageContext, VectorStoreIndex, SentenceSplitter, store, embed


def _model_copy(spec, destination):
    if not isinstance(spec, dict):
        raise RagError("embedding must be a mapping")
    if not re.fullmatch(r"[0-9a-f]{40}", str(spec.get("revision", ""))):
        raise RagError("embedding.revision must be an exact 40-character commit revision")
    if not isinstance(spec.get("license"), str) or not spec["license"].strip():
        raise RagError("embedding.license is required")
    if spec.get("redistribution_approved") is not True:
        raise RagError("Model redistribution must be explicitly approved")
    root = Path(spec.get("path", ""))
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise RagError("embedding.path must be an absolute local model directory")
    files = spec.get("files")
    if not isinstance(files, dict) or not files:
        raise RagError("embedding.files must explicitly allowlist each model file and SHA256")
    license_file = spec.get("license_file")
    if not isinstance(license_file, str) or license_file not in files:
        raise RagError("embedding.license_file must name an allowlisted license text file")
    license_path = _safe_file(root, license_file)
    if license_path.suffix not in (".txt", ".md") and license_path.name not in ("LICENSE", "NOTICE"):
        raise RagError("embedding.license_file must be a plain-text license document")
    if not license_path.read_text(encoding="utf-8").strip():
        raise RagError("Packaged model license text must not be empty")
    if not any(str(name).endswith(".safetensors") for name in files):
        raise RagError("Only safetensors model weights are supported")
    for name, expected in sorted(files.items()):
        path = _safe_file(root, name)
        if path.suffix not in (".json", ".txt", ".md", ".safetensors", ".model") and path.name not in ("LICENSE", "NOTICE"):
            raise RagError("Only model configs, license/docs, tokenizers and safetensors files are allowed")
        if _file_sha(path) != expected:
            raise RagError(f"Model file approval hash mismatch: {name}")
        if path.suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            if "auto_map" in path.read_text(encoding="utf-8"):
                raise RagError("Remote/custom model code configuration is forbidden")
            if path.name == "modules.json":
                if not isinstance(data, list):
                    raise RagError("Invalid SentenceTransformer modules")
                for module in data:
                    if not str(module.get("type", "")).startswith("sentence_transformers.models."):
                        raise RagError("Only built-in SentenceTransformer modules are supported")
                    if module.get("path"):
                        _relative(module["path"])
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        if _file_sha(target) != expected:
            raise RagError(f"Model file changed while copying: {name}")
    return {key: spec[key] for key in (
        "revision", "license", "license_file", "redistribution_approved", "files")}


def _semantic_build(directory, records):
    with _offline():
        chroma, settings, Document, Storage, Index, Splitter, Store, embed = _backend(directory / "model")
        # Chroma is local-only. Persist a fresh index; never load an external database.
        client = chroma.PersistentClient(path=str(directory / "chroma"),
                                        settings=settings(anonymized_telemetry=False,
                                                          chroma_api_impl="chromadb.api.segment.SegmentAPI"))
        try:
            collection = client.create_collection("approved_evidence", embedding_function=None)
            store = Store(chroma_collection=collection, batch_size=_batch_limit(client))
            # Bypass both tiktoken and NLTK defaults: either may download resources.
            parser = Splitter(chunk_size=16384, chunk_overlap=0, include_metadata=False,
                              tokenizer=list, chunking_tokenizer_fn=lambda value: [value])
            nodes = []
            for record in records:
                document = Document(text=record["text"], id_=record["evidence_id"])
                parsed = parser.get_nodes_from_documents([document])
                # Export chunks are authoritative; never silently re-chunk evidence.
                if len(parsed) != 1 or parsed[0].text != record["text"]:
                    raise RagError("LlamaIndex changed an export chunk; use smaller chunks")
                node = parsed[0]
                node.id_ = record["evidence_id"]
                node.embedding = embed.get_text_embedding(record["text"])
                record["embedding"] = node.embedding
                nodes.append(node)
            Index(nodes, storage_context=Storage.from_defaults(vector_store=store),
                  embed_model=embed, transformations=[parser])
        finally:
            # Pinned Chroma exposes no public close(). Stop its local system before
            # hashing/renaming SQLite files; query never reopens these databases.
            client._system.stop()


def build_export(config_path, destination):
    """Publish a new artifact atomically; the source root is deliberately not configurable."""
    config_path, destination = Path(config_path), Path(destination)
    if not config_path.is_absolute() or not destination.is_absolute():
        raise RagError("Config and destination must be absolute paths")
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or config.get("version") != VERSION:
        raise RagError("Config requires version: 1")
    sources = config.get("sources")
    if not isinstance(sources, list):
        raise RagError("sources must be an explicit allowlist")
    if any(not isinstance(source, dict) for source in sources):
        raise RagError("Each source approval must be a mapping")
    sources = sorted(sources, key=lambda source: str(_relative(source.get("path"))))
    aliases = _aliases(config.get("aliases", {}))
    chunking = {"max_chars": 1800, "overlap_chars": 160}
    chunking.update(config.get("chunks", {}))
    chunk_markdown("", **chunking)
    if destination.exists() or destination.is_symlink():
        raise RagError("Destination already exists; exports never overwrite")
    root = BASE_DIR.resolve()
    authority = root / str(SOURCE_REL)
    if destination.resolve().is_relative_to(authority.resolve()):
        raise RagError("Do not write artifacts into the authoritative source directory")
    refs, records, snapshots, seen = brain_citations.load(), [], {}, set()
    for approval in sources:
        if not isinstance(approval, dict):
            raise RagError("Each source approval must be a mapping")
        rel = _relative(approval.get("path"))
        if rel.parent != SOURCE_REL or rel.suffix.lower() != ".md":
            raise RagError("Only direct Markdown files in 00_Fisheries_Brain/01_Sources are eligible")
        if str(rel) in seen:
            raise RagError("Duplicate source approval")
        seen.add(str(rel))
        path = _safe_file(root, str(rel))
        if path.stat().st_size > MAX_SOURCE_BYTES:
            raise RagError("Source exceeds the 2 MB snapshot bound")
        raw = path.read_bytes()
        digest = _sha(raw)
        if approval.get("sha256") != digest:
            raise RagError(f"Stale or absent approval hash: {rel}")
        rights = approval.get("redistribution", {})
        if approval.get("review_finalized") is not True:
            raise RagError("Source review must be explicitly finalized")
        if not isinstance(rights, dict) or rights.get("approved") is not True or not str(rights.get("basis", "")).strip():
            raise RagError("Source redistribution approval and rights basis are required")
        if approval.get("evidence_level") not in ("condensed-note", "original-checked"):
            raise RagError("Explicit condensed-note or original-checked evidence_level required")
        tracks = _strings(approval.get("tracks"), "tracks")
        if not tracks or not set(tracks) <= set(TRACK_FIELDS):
            raise RagError("tracks must select methodological and/or biological")
        fm, body = _frontmatter(raw.decode("utf-8"))
        sid = str(fm.get("source_id") or "").strip()
        citation = brain_citations.lookup(refs, sid, path.stem)
        # Lookup may use a filename MID or stem; preserve both identities, never
        # replace an external/non-numeric source ID with a filename or numeric prefix.
        lookup_keys = (sid, brain_citations.mid_from_source_id(sid),
                       brain_citations.mid_from_stem(path.stem), path.stem)
        citation_key = next((key for key in lookup_keys if key and key in refs), "")
        canonical = (brain_citations.mid_from_source_id(sid)
                     if sid and citation_key == brain_citations.mid_from_source_id(sid)
                     else sid) or brain_citations.mid_from_stem(path.stem) or path.stem
        source_key = _sha(str(rel).encode())[:20]
        snapshot = f"sources/{source_key}.md"
        snapshots[snapshot] = raw
        provenance = {
            "source_id": canonical, "frontmatter_source_id": sid,
            "filename": path.name, "stem": path.stem, "source_path": str(rel),
            "source_sha256": digest, "snapshot": snapshot,
            "citation": citation, "citation_lookup_key": citation_key,
            "citation_status": "canonical-lookup" if citation else "unverified-missing",
            "title": citation.get("title") or str(fm.get("title") or path.stem),
            "approval": approval, "tracks": tracks,
            "species": _strings(approval.get("species", []), "species"),
            "source_metadata": {str(k): fm[k] for k in SOURCE_METADATA_FIELDS
                                if k in fm},
        }
        for chunk in chunk_markdown(body, **chunking):
            identity = _json([str(rel), digest, CHUNKER, chunking, chunk])
            records.append({**chunk, **provenance, "evidence_id": "E-" + _sha(identity.encode())[:24]})
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = destination.parent / (destination.name + ".building-" + uuid.uuid4().hex)
    staging.mkdir()
    try:
        for name, raw in snapshots.items():
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        packages = {"PyYAML": metadata.version("PyYAML")}
        model = None
        if config.get("embedding") is not None:
            if not records:
                raise RagError("A semantic export requires at least one approved chunk")
            packages.update(_versions())
            model = _model_copy(config["embedding"], staging / "model")
            _semantic_build(staging, records)
        _write_json(staging / "records.json", records)
        files = {str(p.relative_to(staging).as_posix()): _file_sha(p)
                 for p in sorted(staging.rglob("*")) if p.is_file()}
        corpus = _sha(_json([{"path": a["path"], "sha256": a["sha256"]}
                             for a in sorted(sources, key=lambda a: a["path"])]).encode())
        manifest = {"version": VERSION, "chunker": CHUNKER, "chunking": chunking,
                    "packages": packages, "embedding": model, "aliases": aliases,
                    "corpus_sha256": corpus, "records": len(records), "files": files,
                    "semantic_settings": {"normalize": True, "device": "cpu",
                                          "trust_remote_code": False, "local_files_only": True,
                                          "minimum_semantic_score": MIN_SEMANTIC_SCORE},
                    "source_authority": str(SOURCE_REL)}
        manifest["manifest_sha256"] = _sha(_json(manifest).encode())
        _write_json(staging / "manifest.json", manifest)
        # A sibling lock coordinates builders without exposing an empty artifact
        # or relying on POSIX replacement of an existing directory.
        lock = destination.parent / (destination.name + ".publish.lock")
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as exc:
            raise RagError("Another builder holds the artifact publication lock") from exc
        try:
            os.close(descriptor)
            if destination.exists() or destination.is_symlink():
                raise RagError("Destination already exists; exports never overwrite")
            staging.rename(destination)
        finally:
            lock.unlink()
        return manifest
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def load_export(artifact):
    """Read/check exported files only. Never consult the vault or citation databases."""
    root = Path(artifact)
    if not root.is_absolute() or root.is_symlink() or not root.is_dir():
        raise RagError("artifact must be an absolute, nonsymlink directory")
    manifest = json.loads(_safe_file(root, "manifest.json").read_text(encoding="utf-8"))
    expected = manifest.pop("manifest_sha256", None)
    if expected != _sha(_json(manifest).encode()):
        raise RagError("Manifest checksum mismatch")
    manifest["manifest_sha256"] = expected
    if manifest.get("version") != VERSION or manifest.get("chunker") != CHUNKER:
        raise RagError("Unsupported artifact or chunking version; no implicit rebuild")
    if manifest.get("source_authority") != str(SOURCE_REL):
        raise RagError("Invalid source authority")
    chunk_markdown("", **manifest["chunking"])
    actual_files = set()
    for path in root.rglob("*"):
        if path.is_symlink():
            raise RagError("Artifact symlinks are not allowed")
        if path.is_file():
            actual_files.add(path.relative_to(root).as_posix())
    if actual_files != set(manifest["files"]) | {"manifest.json"}:
        raise RagError("Artifact contains missing or unapproved files")
    for name, digest in manifest["files"].items():
        if _file_sha(_safe_file(root, name)) != digest:
            raise RagError(f"Artifact checksum mismatch: {name}")
    if "records.json" not in manifest["files"]:
        raise RagError("Manifest must checksum records")
    model = manifest.get("embedding")
    if model:
        license_file = model.get("license_file")
        if not isinstance(license_file, str) or license_file not in model.get("files", {}):
            raise RagError("Model manifest must identify its packaged license text")
        if manifest["files"].get("model/" + license_file) != model["files"][license_file]:
            raise RagError("Model license text must be included and checksummed")
    records = json.loads(_safe_file(root, "records.json").read_text(encoding="utf-8"))
    if not isinstance(records, list) or len(records) != manifest["records"]:
        raise RagError("Record count mismatch")
    seen = set()
    for record in records:
        if record["evidence_id"] in seen or not record["text"] or len(record["text"]) > manifest["chunking"]["max_chars"]:
            raise RagError("Invalid or duplicate evidence record")
        seen.add(record["evidence_id"])
        if record["snapshot"] not in manifest["files"] or manifest["files"][record["snapshot"]] != record["source_sha256"]:
            raise RagError("Unchecksummed source snapshot")
    return manifest, records


def _canonical(term, aliases):
    term = term.casefold().strip()
    for canonical, alternatives in aliases.items():
        if term == canonical or term in alternatives:
            return canonical
    return term


def _tokens(text):
    stop = {"the", "and", "for", "with", "from", "this", "that", "are", "was", "how", "what"}
    return set(re.findall(r"[\w-]+", text.casefold())) - stop


def _context(request):
    if not isinstance(request, dict) or request.get("track") not in TRACK_FIELDS:
        raise RagError("request.track must be methodological or biological")
    fields = TRACK_FIELDS[request["track"]]
    if set(request) - {"track", *fields}:
        raise RagError("Unknown context fields; see TRACK_FIELDS")
    parts = []
    for key in fields:
        value = request.get(key, "")
        if isinstance(value, (dict, list)):
            value = _json(value)
        if not isinstance(value, str) or len(value) > 3000:
            raise RagError("Context values must be strings or structured JSON, bounded to 3000 characters")
        if value:
            parts.append(f"{key}: {value}")
    if not parts:
        raise RagError("Provide structured context for the requested track")
    if request["track"] == "biological" and not isinstance(request.get("species"), str):
        raise RagError("Biological retrieval requires one explicit species string")
    if request["track"] == "biological" and not request["species"].strip():
        raise RagError("Biological retrieval requires one explicit species; no taxon broadening")
    if request["track"] == "biological" and (
            not isinstance(request.get("parameter"), str) or not request["parameter"].strip()):
        raise RagError("Biological retrieval requires an explicit parameter string")
    return "\n".join(parts)


def _semantic_query(root, manifest, records, text, limit):
    if not manifest["embedding"]:
        raise SemanticUnavailable("Artifact contains no approved local embedding model; use lexical mode")
    actual = {**_versions(), "PyYAML": metadata.version("PyYAML")}
    recorded = manifest["packages"]
    if actual != recorded:
        raise SemanticUnavailable("Artifact semantic package versions differ; no implicit rebuild")
    model = manifest["embedding"]
    for name, digest in model["files"].items():
        if manifest["files"].get("model/" + name) != digest:
            raise RagError("Model identity/checksum does not match manifest")
    with _offline():
        chroma, settings, _, _, Index, Splitter, Store, embed = _backend(root / "model")
        client = chroma.EphemeralClient(settings=settings(
            anonymized_telemetry=False, chroma_api_impl="chromadb.api.segment.SegmentAPI"))
        collection = client.create_collection("query_" + uuid.uuid4().hex, embedding_function=None)
        try:
            batch_size = _batch_limit(client)
            for start in range(0, len(records), batch_size):
                batch = records[start:start + batch_size]
                collection.add(ids=[r["evidence_id"] for r in batch],
                               documents=[r["text"] for r in batch],
                               embeddings=[r["embedding"] for r in batch])
            parser = Splitter(chunk_size=16384, chunk_overlap=0, include_metadata=False,
                              tokenizer=list, chunking_tokenizer_fn=lambda value: [value])
            index = Index.from_vector_store(Store(chroma_collection=collection),
                                            embed_model=embed, transformations=[parser])
            hits = index.as_retriever(similarity_top_k=min(limit, len(records))).retrieve(text)
            return {hit.node.node_id: float(hit.score or 0) for hit in hits}
        finally:
            client.delete_collection(collection.name)


def query_export(artifact, request, mode="auto", limit=6, max_chars=12000):
    """Return bounded evidence, never generated scientific assertions or rules."""
    if mode not in ("auto", "lexical", "semantic") or not 1 <= limit <= 12 or not 1000 <= max_chars <= 50000:
        raise RagError("mode auto|lexical|semantic, limit 1..12, max_chars 1000..50000 required")
    text = _context(request)
    manifest, records = load_export(artifact)
    aliases = manifest["aliases"]
    candidates = [r for r in records if request["track"] in r["tracks"]]
    if request["track"] == "biological":
        taxon = _canonical(request["species"], aliases)
        candidates = [r for r in candidates if taxon in {
            _canonical(s, aliases) for s in r["species"]}]
    excluded = {"track", "species"} if request["track"] == "biological" else {"track"}
    lexical_text = " ".join(_json(value) if isinstance(value, (dict, list)) else value
                            for key, value in request.items() if key not in excluded)
    terms = _tokens(lexical_text)
    parameter_terms = _tokens(request.get("parameter", ""))
    for canonical, alternatives in aliases.items():
        if any(term in lexical_text.casefold() for term in [canonical, *alternatives]):
            terms |= _tokens(" ".join([canonical, *alternatives]))
        if any(term in request.get("parameter", "").casefold() for term in [canonical, *alternatives]):
            parameter_terms |= _tokens(" ".join([canonical, *alternatives]))
    if request["track"] == "biological":
        taxon_terms = _tokens(" ".join([request["species"], taxon, *aliases.get(taxon, [])]))
        terms -= taxon_terms
        parameter_terms -= taxon_terms
    scores = {}
    for r in candidates:
        searchable = " ".join((r["text"], r["section"], r["title"],
                               " ".join(r["species"]),
                               " ".join(_json(v) for v in r["source_metadata"].values())))
        record_terms = _tokens(searchable)
        if request["track"] == "biological" and not parameter_terms & record_terms:
            continue
        score = len(terms & record_terms)
        if score:
            scores[r["evidence_id"]] = float(score)
    fallback, used = None, "lexical"
    semantic, rejected_semantic = {}, 0
    if mode != "lexical" and candidates:
        try:
            neighbors = _semantic_query(Path(artifact), manifest, candidates, text, limit)
            semantic = {eid: score for eid, score in neighbors.items()
                        if score >= MIN_SEMANTIC_SCORE}
            rejected_semantic = len(neighbors) - len(semantic)
            used = "semantic+lexical"
        except SemanticUnavailable as exc:
            if mode == "semantic":
                raise
            fallback = str(exc)
    ranked = sorted(candidates, key=lambda r: (
        -(scores.get(r["evidence_id"], 0) + semantic.get(r["evidence_id"], 0)),
        r["evidence_id"]))
    pack = {"version": VERSION, "status": "candidates-pending-review",
            "track": request["track"], "context": request,
            "retrieval": {"mode": used, "fallback_reason": fallback,
                          "corpus_sha256": manifest["corpus_sha256"],
                          "manifest_sha256": manifest["manifest_sha256"],
                          "exported_chunks": len(records), "scoped_chunks": len(candidates),
                          "minimum_semantic_score": MIN_SEMANTIC_SCORE,
                          "rejected_semantic_neighbors": rejected_semantic,
                          "support_status": "unverified-candidates-not-scientific-support",
                          "matching_chunks": len(set(scores) | set(semantic))},
            "evidence": [], "abstained": True,
            "abstention_reason": "No scoped exported evidence matched this request.",
            "caveats": CAVEATS}
    for record in ranked:
        eid = record["evidence_id"]
        if eid not in scores and eid not in semantic:
            continue
        item = {k: record[k] for k in ("evidence_id", "text", "section", "offset", "source_id",
                "filename", "stem", "source_path", "source_sha256", "snapshot",
                "citation", "citation_lookup_key", "citation_status", "title", "species", "source_metadata")}
        item["evidence_level"] = record["approval"]["evidence_level"]
        item["review_finalized"] = record["approval"]["review_finalized"]
        item["redistribution_basis"] = record["approval"]["redistribution"]["basis"]
        item["match_kind"] = "lexical" if eid in scores else "semantic-only-unverified"
        item["applicability_gaps"] = (
            ["Requested biological parameter has no lexical match; semantic-only candidate."]
            if request["track"] == "biological" and eid not in scores else [])
        item["retrieval"] = {"lexical_overlap": scores.get(eid, 0), "semantic_score": semantic.get(eid)}
        pack["evidence"].append(item)
        pack["abstained"] = False
        pack["abstention_reason"] = None
        if len(_json(pack)) > max_chars:
            pack["evidence"].pop()
            pack["abstained"] = not pack["evidence"]
            if pack["abstained"]:
                pack["abstention_reason"] = "Matching evidence did not fit max_chars; no excerpt returned."
            break
        if len(pack["evidence"]) >= limit:
            break
    if len(_json(pack)) > max_chars:
        raise RagError("Request/provenance exceeds max_chars; shorten context or increase bound")
    return pack


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build")
    build.add_argument("--config", required=True)
    build.add_argument("--destination", required=True)
    query = commands.add_parser("query")
    query.add_argument("--artifact", required=True)
    query.add_argument("--request", required=True, help="Structured context as a JSON object")
    query.add_argument("--mode", choices=("auto", "lexical", "semantic"), default="auto")
    query.add_argument("--limit", type=int, default=6)
    query.add_argument("--max-chars", type=int, default=12000)
    args = parser.parse_args(argv)
    try:
        # Optional libraries may print progress. Keep stdout machine-readable JSON.
        with redirect_stdout(sys.stderr):
            if args.command == "build":
                result = build_export(args.config, args.destination)
            else:
                result = query_export(args.artifact, json.loads(args.request),
                                      args.mode, args.limit, args.max_chars)
        print(_json(result))
        return 0
    except (RagError, OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        print(_json({"error": str(exc)}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
