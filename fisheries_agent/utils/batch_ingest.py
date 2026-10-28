"""Unattended ingest of the remaining public-domain Minckley PDFs through Anthropic's Message Batches API (half price).

Run from fisheries_agent (close the Agent and Batch windows first, or at least do not run the feeder at the same time):
    python -m utils.batch_ingest --size 5     small test run of the 5 smallest remaining documents
    python -m utils.batch_ingest              everything still on the public-domain list
    python -m utils.batch_ingest --list restricted --long full
                                              the non-public-domain list (python -m utils.minckley_lists restricted)
    python -m utils.batch_ingest status       where the current run stands (counts and batch status)
    python -m utils.batch_ingest cancel       cancel batches in flight; rerun later to resubmit what did not finish
Full text: every extracted document is also saved to 00_Fisheries_Brain/full_text/<MID>.md (gitignored, never synced
or published; many of these documents are copyrighted). --no-full-text turns this off.
Options: --list public|restricted, --yes (skip the cost question), --long cap|full|skip (documents over 250k characters; default cap),
--workers N (documents OCRd in parallel), --chunk N (documents per submitted batch), --poll SECONDS, --no-sync.

How it works (same prompts and note format as the interactive ingest; only the delivery differs):
 1. Picks MIDs from unprocessed_public_domain_mids.csv that have no note, are not excluded, and are not in the feeder's
    current batch (smallest first). Shows a cost estimate (batch = 50% of list) and asks once.
 2. For each chunk: copies/merges the PDF into pdfs_to_process/_batch/ (a subfolder the watcher never reads), extracts
    text (OCR in parallel), deletes the staged copy (the text is cached), and submits one batch of note requests.
 3. Polls. Finished notes are written exactly like pdf_ingest (frontmatter, stubs, citations, manifest, done CSV);
    truncated notes are resubmitted once on OPENROUTER_FALLBACK_MODEL with a doubled budget, incomplete ones once more
    on the same model. New concept stubs get their summaries in a follow-up batch.
 4. At the end: index smoke check and the usual git sync of the brain (skip with --no-sync).
State is saved in runs/batch_ingest_state.json after every step, so a closed window or reboot just needs a rerun.
The Anthropic key (ANTHROPIC_API_KEY) is read from .env and never printed. Model ids are the usual OpenRouter-style
ones (OPENROUTER_INGEST_MODEL, default anthropic/claude-haiku-5.5), translated for Anthropic.
"""
import argparse
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from utils import brain_citations, brain_index, llm_provider, minckley_batch, minckley_lists, pdf_ingest
from utils.pdf_ingest import (BATCH_PDF_DIR, CACHE_DIR, MANIFEST_PATH, MAX_NOTE_CHARS, NOTE_MAX_TOKENS, STUB_SYSTEM,
                              _load_json, _save_json)
from utils.stub_store import StubStore, StubStoreError

STATE_PATH = pdf_ingest.BASE_DIR / "runs" / "batch_ingest_state.json"  # local only (runs/ is gitignored)
FULL_TEXT_DIR = pdf_ingest.BRAIN_DIR / "full_text"  # local only: gitignored, outside SYNC_PATHS, the index and the site
FULL_TEXT_IGNORE = "fisheries_agent/00_Fisheries_Brain/full_text/"
API_BASE = os.getenv("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
API_VERSION = "2023-06-01"
BATCH_DISCOUNT = 0.5
MIN_TEXT_CHARS = 50  # fewer letters/digits than this: nothing to summarize, so the document fails instead of being sent
MAX_BATCH_BYTES = 150_000_000  # Anthropic's limit is 256 MB per batch
MAX_TRIES = 3  # submissions per request before it counts as failed (errors, expiry)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _say(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M')}] {msg}", flush=True)


# ------------------------------------------------------------------ batch API
class BatchAPI:
    """Minimal Message Batches client (stdlib only). Error messages never contain the key."""

    def __init__(self):
        llm_provider._load_env()
        self._key = os.getenv("ANTHROPIC_API_KEY", "")
        if not self._key or self._key.startswith("your_"):
            raise SystemExit(f"ANTHROPIC_API_KEY is not set in {llm_provider.ENV_PATH}; batch ingest needs the Anthropic account.")

    def _call(self, method: str, url: str, body: dict = None, raw: bool = False):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "x-api-key": self._key, "anthropic-version": API_VERSION, "content-type": "application/json"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    payload = r.read()
                return payload if raw else json.loads(payload)
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "replace")[:400].replace(self._key, "[key]")
                if e.code in (429, 500, 502, 503, 504, 529) and attempt < 3:
                    time.sleep(20 * (attempt + 1))
                    continue
                raise RuntimeError(f"Anthropic batch API {method} {url.rsplit('/v1/', 1)[-1]} failed ({e.code}): {detail}")
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if attempt < 3:
                    time.sleep(30 * (attempt + 1))
                    continue
                raise RuntimeError(f"Anthropic batch API unreachable: {e}")

    def create(self, requests: list) -> dict:
        return self._call("POST", f"{API_BASE}/v1/messages/batches", {"requests": requests})

    def get(self, batch_id: str) -> dict:
        return self._call("GET", f"{API_BASE}/v1/messages/batches/{batch_id}")

    def cancel(self, batch_id: str) -> dict:
        return self._call("POST", f"{API_BASE}/v1/messages/batches/{batch_id}/cancel", {})

    def results(self, batch: dict):
        url = batch.get("results_url") or f"{API_BASE}/v1/messages/batches/{batch['id']}/results"
        for line in self._call("GET", url, raw=True).decode("utf-8").splitlines():
            if line.strip():
                yield json.loads(line)


def _request(custom_id: str, model: str, system: str, user: str, max_tokens: int) -> dict:
    return {"custom_id": custom_id, "params": {
        "model": llm_provider.api_model(model, "anthropic"), "max_tokens": max_tokens,
        "system": system, "messages": [{"role": "user", "content": user}]}}


# ---------------------------------------------------------------------- state
def load_state() -> dict:
    return _load_json(STATE_PATH)


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, STATE_PATH)


def active_mids() -> set:
    """MIDs an unfinished batch run owns (the interactive feeder leaves these alone)."""
    docs = load_state().get("docs", {})
    return {m for m, d in docs.items() if d.get("status") not in ("done", "failed", "skipped")}


def _exclude_in_feeder(mid: str, why: str) -> None:
    fs = _load_json(minckley_batch.STATE_PATH)
    fs.setdefault("excluded", {})[mid] = why
    _save_json(minckley_batch.STATE_PATH, fs)


def _source_dir() -> Path:
    llm_provider._load_env()
    return Path(os.getenv("MINCKLEY_PDF_DIR") or minckley_batch.DEFAULT_SOURCE)


# ------------------------------------------------------------------- estimate
def _typical_cost() -> tuple:
    """(mean list-price USD per Minckley note, number of past notes) from the usage log."""
    try:
        rows = [json.loads(l) for l in pdf_ingest.USAGE_LOG_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    except OSError:
        return None, 0
    done = [r for r in rows if r.get("result") == "done" and str(r.get("source_id", "")).isdigit() and r.get("cost_usd")]
    done = done[-300:]
    return (sum(r["cost_usd"] for r in done) / len(done), len(done)) if done else (None, 0)


def show_plan(items: list, model: str, long_mode: str) -> None:
    from pypdf import PdfReader
    total_pages = 0
    print(f"\n{len(items)} documents (smallest first):")
    for it in items:
        pages = 0
        for p in it["paths"]:
            try:
                pages += len(PdfReader(str(p)).pages)
            except Exception:
                pass
        it["pages"] = pages
        total_pages += pages
        merged = f", merges {len(it['paths'])} files" if len(it["paths"]) > 1 else ""
        print(f"  {it['mid']}: {pages} pages, {it['size'] / 1e6:,.0f} MB{merged}")
    price = pdf_ingest._price(model)
    typical, n = _typical_cost()
    print(f"\nModel {model} on the Anthropic Batches API (50% of list price). {total_pages:,} pages in all.")
    if typical:
        cap = pdf_ingest.FULL_NOTE_CHARS if long_mode == "full" else MAX_NOTE_CHARS
        more = " Documents between 250,000 and 450,000 characters cost up to about twice the average." if long_mode == "full" else ""
        print(f"  Estimate: about ${typical * len(items) * BATCH_DISCOUNT:.2f} (your last {n} Minckley notes averaged ${typical:.3f} each at list price,"
              f" including stub summaries; nothing past {cap:,} characters is sent).{more}")
    elif price:
        cap_in, cap_out = pdf_ingest.estimate_tokens([MAX_NOTE_CHARS] * len(items))
        print(f"  Notes alone at the {MAX_NOTE_CHARS:,}-character cap: about ${(cap_in * price[0] + cap_out * price[1]) * BATCH_DISCOUNT:.2f}.")
    print(f"  Long documents: {long_mode}. OCR runs locally first and is the slow part (large scans can take 10+ minutes each).")


# ----------------------------------------------------------------- extraction
def _stage_and_extract(doc: dict, item_paths: list, long_mode: str, model: str) -> dict:
    """Runs in a worker thread. Returns updates for the doc entry."""
    mid = doc["mid"]
    BATCH_PDF_DIR.mkdir(parents=True, exist_ok=True)
    minckley_batch.stage({"mid": mid, "paths": item_paths}, dest_dir=BATCH_PDF_DIR)
    p = BATCH_PDF_DIR / f"{mid}.pdf"
    d = pdf_ingest.file_hash(p)
    ex = pdf_ingest.extract_text(p, d, verbose=False)
    cache = CACHE_DIR / f"{d[:16]}.json"
    if not cache.is_file():  # extract_text skips caching near-empty text; the batch needs it on disk either way
        _save_json(cache, ex)
    words = len(re.sub(r"\W", "", re.sub(r"--- Page \d+ ---", "", ex["text"])))
    if words < MIN_TEXT_CHARS:
        p.unlink(missing_ok=True)
        raise RuntimeError(f"only {words} readable characters extracted from {ex['pages']} page(s); check the PDF by eye")
    chars = len(ex["text"])
    if chars <= MAX_NOTE_CHARS:
        limit = MAX_NOTE_CHARS
    else:
        limit = {"full": min(chars, pdf_ingest.FULL_NOTE_CHARS), "skip": 0}.get(long_mode, MAX_NOTE_CHARS)
    # the text is cached by hash under _extracted, so the staged copy is no longer needed (the library copy is untouched)
    p.unlink(missing_ok=True)
    return {"digest": d, "pages": ex["pages"], "method": ex["method"], "ocr_pages": len(ex["ocr_pages"]),
            "chars": len(ex["text"]), "limit": limit}


def _cached_text(doc: dict) -> dict:
    ex = _load_json(CACHE_DIR / f"{doc['digest'][:16]}.json")
    if not ex.get("text"):
        raise RuntimeError("extracted text is missing from the cache (pdfs_to_process/_extracted); rerun to extract again")
    return ex


# ------------------------------------------------------------------ full text
def full_text_ignored() -> bool:
    """True only when the repo .gitignore excludes full_text/, so nothing written there can be committed."""
    try:
        lines = (pdf_ingest.BASE_DIR.parent / ".gitignore").read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    return FULL_TEXT_IGNORE in (l.strip() for l in lines)


def write_full_text(mid: str, ex: dict, ref: dict, permission: str, note_stem: str = "") -> Path:
    """Writes the complete extracted text (no character cap) with a small header; returns the path."""
    FULL_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    cite = {**{k: ref.get(k, "") for k in ("authors", "year", "title", "publication", "type")}, "mid": mid}
    head = {
        "minckley_id": mid,
        "title": ref.get("title", ""),
        "source_citation": pdf_ingest.format_citation(cite) if ref else "",
        "permission": permission,
        "pages": ex.get("pages", 0),
        "text_extraction": ex.get("method", ""),
        "characters": len(ex.get("text", "")),
        "note": f"[[{note_stem}]]" if note_stem else "",
        "private": True,
    }
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in head.items())
    body = ("> Local reference copy of the full extracted text. Not for redistribution: this folder is gitignored and is "
            "never synced, indexed or published.\n" + ex.get("text", ""))
    path = FULL_TEXT_DIR / f"{mid}.md"
    tmp = path.with_suffix(".tmp")
    tmp.write_text(f"---\n{fm}\n---\n{body}\n", encoding="utf-8")
    os.replace(tmp, path)
    return path


# -------------------------------------------------------------------- runner
class Runner:
    def __init__(self, state: dict, api: BatchAPI, args):
        self.state, self.api, self.args = state, api, args
        self.model = state["model"]
        self.fallback = state.get("fallback", "")
        self.todo_csv, self.done_csv = minckley_lists.LISTS[state.get("list", "public")]
        self._perm = None

    def _full_text(self, doc: dict, note_stem: str = ""):
        if not self.state.get("full_text"):
            return
        if not full_text_ignored():
            _say(f"Full text NOT saved for {doc['mid']}: {FULL_TEXT_IGNORE} is missing from .gitignore.")
            return
        if self._perm is None:
            self._perm = minckley_lists.permissions()
        mid = doc["mid"]
        ref = _load_json(brain_citations.CITATIONS_PATH).get(mid) or brain_citations.fetch_entry(mid)
        try:
            write_full_text(mid, _cached_text(doc), ref, self._perm.get(mid, ""), note_stem)
        except Exception as e:
            _say(f"{mid}: could not save the full text ({e}); the note is unaffected.")

    # ---- helpers
    def save(self):
        save_state(self.state)

    def _usage(self, doc: dict, model: str, tin: int, tout: int):
        cost = llm_provider.list_price_cost(model, tin, tout)
        cost = (cost or 0.0) * BATCH_DISCOUNT
        u = doc.setdefault("usage", {"in": 0, "out": 0, "cost": 0.0, "requests": 0})
        u["in"] += tin
        u["out"] += tout
        u["cost"] += cost
        u["requests"] += 1
        t = self.state.setdefault("totals", {"in": 0, "out": 0, "cost": 0.0})
        t["in"] += tin
        t["out"] += tout
        t["cost"] += cost

    def _log(self, doc: dict, result: str, **extra):
        p = Path(f"{doc['mid']}.pdf")
        rec = pdf_ingest._new_usage_record(p, doc["mid"], doc.get("model") or self.model)
        u = doc.get("usage", {})
        rec.update({"provider": "anthropic-batch", "pages": doc.get("pages"), "extraction": doc.get("method", "not_started"),
                    "ocr_pages": doc.get("ocr_pages", 0), "source_characters": min(doc.get("chars", 0), doc.get("limit") or MAX_NOTE_CHARS),
                    "tokens_in": u.get("in", 0), "tokens_out": u.get("out", 0), "cost_usd": round(u.get("cost", 0.0), 6),
                    "request_attempts": u.get("requests", 0), "retries": max(0, u.get("requests", 0) - 1),
                    "generation_ids": doc.get("batch_ids", []), "fallback_model": doc.get("fallback_used", ""),
                    "result": result, "batch_discount": BATCH_DISCOUNT, **extra})
        pdf_ingest._finish_usage_record(rec)

    def _fail(self, doc: dict, why: str):
        doc["status"], doc["error"] = "failed", why[:500]
        if doc.get("digest"):
            manifest = _load_json(MANIFEST_PATH)
            manifest[doc["digest"]] = pdf_ingest._record(Path(f"{doc['mid']}.pdf"), doc["digest"], "failed", reason=why[:500])
            _save_json(MANIFEST_PATH, manifest)
        _exclude_in_feeder(doc["mid"], "failed")
        self._log(doc, "failed", error=why[:500])
        _say(f"{doc['mid']} FAILED: {why[:200]}")

    def _queue_note(self, doc: dict):
        ex = _cached_text(doc)
        system, user, _, budget = pdf_ingest.note_request(ex["text"], doc["limit"])
        budget = doc.get("budget") or budget
        cid = f"note-{doc['mid']}-{doc.get('attempt', 0)}-{doc.get('tries', 0)}"
        self.state["queue"].append({"cid": cid, "kind": "note", "mid": doc["mid"],
                                    "request": _request(cid, doc.get("model") or self.model, system, user, budget)})
        doc["status"] = "queued_note"

    def _queue_stubs(self, doc: dict, created: list):
        note = (pdf_ingest.SOURCES_DIR / f"{doc['stem']}.md").read_text(encoding="utf-8")
        for i, (names, user, budget) in enumerate(pdf_ingest.stub_requests(note, created)):
            cid = f"stub-{doc['mid']}-{i}-{doc.get('stub_round', 0)}"
            self.state["queue"].append({"cid": cid, "kind": "stub", "mid": doc["mid"], "names": names,
                                        "request": _request(cid, self.model, STUB_SYSTEM, user, budget)})
            doc["stubs_pending"] = doc.get("stubs_pending", 0) + 1

    # ---- phase 1: stage + extract a chunk
    def extract_chunk(self) -> int:
        todo = [d for d in self.state["docs"].values() if d["status"] == "pending"][: self.args.chunk]
        if not todo:
            return 0
        paths = {it["mid"]: it["paths"] for it in self.state.get("items", [])}
        _say(f"Extracting {len(todo)} documents ({self.args.workers} at a time; OCR where needed)...")
        if self.args.workers > 1:
            os.environ.setdefault("OMP_THREAD_LIMIT", "1")  # one Tesseract thread per document when OCRing in parallel
        with ThreadPoolExecutor(max_workers=max(1, self.args.workers)) as pool:
            futs = {pool.submit(_stage_and_extract, d, [Path(x) for x in paths[d["mid"]]], self.state["long"], self.model): d for d in todo}
            for fut in as_completed(futs):
                d = futs[fut]
                try:
                    d.update(fut.result())
                except Exception as e:
                    d.update({"pages": d.get("pages")})
                    self._fail(d, f"extraction: {e}")
                    continue
                if not d["limit"]:
                    d["status"] = "skipped"
                    _exclude_in_feeder(d["mid"], "skipped")
                    self._log(d, "skipped_too_long")
                    _say(f"{d['mid']}: {d['chars']:,} characters, skipped (--long skip)")
                    continue
                try:
                    self._full_text(d)
                    self._queue_note(d)
                except Exception as e:  # one bad document must not stop the run
                    self._fail(d, f"preparing the request: {e}")
                    continue
                sent = f", sending the first {d['limit']:,} (--long {self.state['long']})" if d["chars"] > d["limit"] else ""
                _say(f"{d['mid']}: {d['pages']} pages ({d['method']}, {d['ocr_pages']} OCR), {d['chars']:,} chars{sent} -> queued")
                self.save()
        self.save()
        return len(todo)

    # ---- submit
    def submit(self):
        queue = self.state["queue"]
        while queue:
            chunk, size = [], 0
            while queue and size < MAX_BATCH_BYTES:
                item = queue[0]
                size += len(json.dumps(item["request"]))
                chunk.append(queue.pop(0))
            batch = self.api.create([c["request"] for c in chunk])
            self.state["batches"][batch["id"]] = {
                "submitted": _now(), "status": batch.get("processing_status", "in_progress"),
                "items": {c["cid"]: {k: v for k, v in c.items() if k != "request"} for c in chunk}}
            for c in chunk:
                doc = self.state["docs"][c["mid"]]
                doc.setdefault("batch_ids", []).append(batch["id"])
                if c["kind"] == "note":
                    doc["status"] = "in_batch"
            notes = sum(c["kind"] == "note" for c in chunk)
            _say(f"Submitted batch {batch['id']}: {notes} notes, {len(chunk) - notes} stub-summary requests.")
            self.save()

    # ---- poll + results
    def poll(self) -> int:
        """Processes every batch that has ended; returns how many are still running."""
        running = 0
        for bid, info in list(self.state["batches"].items()):
            if info.get("processed"):
                continue
            batch = self.api.get(bid)
            info["status"] = batch.get("processing_status")
            info["counts"] = batch.get("request_counts")
            if batch.get("processing_status") != "ended":
                running += 1
                continue
            _say(f"Batch {bid} ended {batch.get('request_counts')}; writing results.")
            seen = set()
            catalog = pdf_ingest._vault_catalog()
            for line in self.api.results(batch):
                cid = line.get("custom_id")
                item = info["items"].get(cid)
                if not item:
                    continue
                seen.add(cid)
                try:
                    if item["kind"] == "note":
                        self._note_result(item, line.get("result", {}), catalog)
                    else:
                        self._stub_result(item, line.get("result", {}))
                except Exception as e:
                    self._fail(self.state["docs"][item["mid"]], f"writing result: {e}")
                self.save()
            for cid, item in info["items"].items():  # anything the results file did not mention: resubmit
                if cid not in seen:
                    self._retry(item, "missing from batch results")
            info["processed"] = _now()
            self.save()
        return running

    def _retry(self, item: dict, why: str):
        doc = self.state["docs"][item["mid"]]
        if item["kind"] == "stub":
            doc["stubs_pending"] = max(0, doc.get("stubs_pending", 1) - 1)
            if doc.get("stub_tries", 0) < MAX_TRIES - 1:
                doc["stub_tries"] = doc.get("stub_tries", 0) + 1
                doc["stub_round"] = doc.get("stub_round", 0) + 1
                note = (pdf_ingest.SOURCES_DIR / f"{doc['stem']}.md").read_text(encoding="utf-8")
                for i, (names, user, budget) in enumerate(pdf_ingest.stub_requests(note, item["names"])):
                    cid = f"stub-{doc['mid']}-{i}-{doc['stub_round']}"
                    self.state["queue"].append({"cid": cid, "kind": "stub", "mid": doc["mid"], "names": names,
                                                "request": _request(cid, self.model, STUB_SYSTEM, user, budget)})
                    doc["stubs_pending"] += 1
            else:
                _say(f"{doc['mid']}: stub summaries not written ({why}); `python -m utils.pdf_ingest stubs --summaries` backfills them.")
            return
        doc["tries"] = doc.get("tries", 0) + 1
        if doc["tries"] >= MAX_TRIES:
            self._fail(doc, f"note request {why} {doc['tries']} times")
            return
        self._queue_note(doc)

    def _note_result(self, item: dict, result: dict, catalog: list):
        doc = self.state["docs"][item["mid"]]
        rtype = result.get("type")
        if rtype != "succeeded":
            err = (result.get("error") or {}).get("error", result.get("error") or {})
            if rtype == "errored" and isinstance(err, dict) and err.get("type") == "invalid_request_error":
                self._fail(doc, f"invalid request: {err.get('message', '')}")
            else:
                self._retry(item, rtype or "unknown result")
            return
        msg = result["message"]
        used = doc.get("model") or self.model
        u = msg.get("usage", {})
        self._usage(doc, used, u.get("input_tokens", 0), u.get("output_tokens", 0))
        text = "".join(b.get("text", "") for b in msg.get("content", []) if b.get("type") == "text")
        attempt = doc.get("attempt", 0)
        if msg.get("stop_reason") == "max_tokens":
            partial = CACHE_DIR / f"{doc['digest'][:16]}_truncated.md"
            partial.parent.mkdir(parents=True, exist_ok=True)
            partial.write_text(text, encoding="utf-8")
            if attempt == 0:
                nxt = self.fallback or used
                _say(f"{doc['mid']}: {used} ran out of output room; resubmitting once with {nxt} and a larger budget.")
                doc.update({"attempt": 1, "model": nxt, "budget": NOTE_MAX_TOKENS * 2, "tries": 0})
                if self.fallback:
                    doc["fallback_used"] = self.fallback
                self._queue_note(doc)
            else:
                self._fail(doc, "model response reached its max_tokens limit")
            return
        note, complete = pdf_ingest.parse_note(text, pdf_ingest.REQUIRED_HEADERS)
        if not complete:
            if attempt == 0:
                doc.update({"attempt": 1, "tries": 0})
                self._queue_note(doc)
            else:
                self._fail(doc, str(pdf_ingest.incomplete_note_error(note)))
            return
        self._finalize(doc, note, catalog)

    def _finalize(self, doc: dict, note: str, catalog: list):
        mid = doc["mid"]
        ex = _cached_text(doc)
        ref = _load_json(brain_citations.CITATIONS_PATH).get(mid) or brain_citations.fetch_entry(mid)
        if not ref:
            self._fail(doc, f"{mid} is not in the Minckley library sheet; ingest it with pdf_ingest instead")
            return
        cite = {**{k: ref.get(k, "") for k in ("authors", "year", "title", "publication", "type")}, "citation_source": "minckley-sheet", "mid": mid}
        p = BATCH_PDF_DIR / f"{mid}.pdf"
        stem, title, _, upd, created = pdf_ingest.write_note(p, ex, cite, mid, mid, note, {"doc_type": "", "secondary_type": ""}, catalog)
        brain_citations.save_entries({mid: ref})
        manifest = _load_json(MANIFEST_PATH)
        manifest[doc["digest"]] = pdf_ingest._record(p, doc["digest"], "done", note=f"{stem}.md", method=ex["method"],
                                                     citation_source="minckley-sheet", doc_type="", via="anthropic-batch")
        _save_json(MANIFEST_PATH, manifest)
        names = next((it["names"] for it in self.state.get("items", []) if it["mid"] == mid), [f"{mid}.pdf"])
        minckley_batch._append_done([[n, mid] for n in names], self.done_csv)
        self._full_text(doc, stem)  # adds the note link to the full-text header
        pdf_ingest._discard(p, doc["digest"])  # removes the cached text too
        doc.update({"status": "done", "stem": stem, "title": title, "finished": _now()})
        self.state.setdefault("written", []).append([stem, title])
        self._log(doc, "done", note=f"{stem}.md")
        _say(f"{mid}: wrote {stem}.md, {upd} stubs updated ({len(created)} new)")
        if created:
            self._queue_stubs(doc, created)

    def _stub_result(self, item: dict, result: dict):
        doc = self.state["docs"][item["mid"]]
        if result.get("type") != "succeeded":
            self._retry(item, result.get("type") or "unknown result")
            return
        msg = result["message"]
        u = msg.get("usage", {})
        self._usage(doc, self.model, u.get("input_tokens", 0), u.get("output_tokens", 0))
        text = "".join(b.get("text", "") for b in msg.get("content", []) if b.get("type") == "text")
        store = StubStore()
        n = pdf_ingest.apply_stub_summaries(text, item["names"], store)
        store.flush()
        doc["stubs_pending"] = max(0, doc.get("stubs_pending", 1) - 1)
        doc["stubs_summarized"] = doc.get("stubs_summarized", 0) + n

    # ---- main loop
    def run(self) -> int:
        while True:
            worked = self.extract_chunk()
            self.submit()
            running = self.poll()
            self.submit()  # retries and stub summaries produced by the results
            open_docs = [d for d in self.state["docs"].values() if d["status"] not in ("done", "failed", "skipped")]
            if not open_docs and not running and not self.state["queue"] and not any(
                    not b.get("processed") for b in self.state["batches"].values()):
                break
            if worked:
                continue  # keep OCRing while earlier batches run
            if running:
                counts = self.status_counts()
                _say(f"Waiting on {running} batch(es); {counts}. Next check in {self.args.poll // 60} min.")
                time.sleep(self.args.poll)
        return self.finish()

    def status_counts(self) -> str:
        c = {}
        for d in self.state["docs"].values():
            c[d["status"]] = c.get(d["status"], 0) + 1
        return ", ".join(f"{v} {k}" for k, v in sorted(c.items()))

    def finish(self) -> int:
        written = self.state.get("written", [])
        if written and not self.state.get("checked"):
            brain_index._checked = False
            for stem, title in written:
                if not pdf_ingest.smoke_check(stem, title):
                    _say(f"WARNING: '{title[:60]}' ({stem}) is not in the search index; check the note.")
            self.state["checked"] = True
        t = self.state.get("totals", {"in": 0, "out": 0, "cost": 0.0})
        failed = [m for m, d in self.state["docs"].items() if d["status"] == "failed"]
        _say(f"Finished: {self.status_counts()}. {t['in']:,} input + {t['out']:,} output tokens, about ${t['cost']:.2f} "
             f"(batch price; list would be ${t['cost'] / BATCH_DISCOUNT:.2f}).")
        if failed:
            print("  Failed (left out of future runs; see runs/pdf_ingest_usage.jsonl): " + ", ".join(failed))
        self.state["finished"] = _now()
        self.save()
        if written and not self.args.no_sync and not self.state.get("synced"):
            rel = self.done_csv.relative_to(pdf_ingest.BASE_DIR).as_posix()
            if pdf_ingest.sync_to_github(f"Add {len(written)} Minckley notes (Anthropic batch)", extra_paths=(rel,)):
                self.state["synced"] = True
                self.save()
        return 1 if failed else 0


# ---------------------------------------------------------------------- start
def new_state(args) -> dict:
    source = _source_dir()
    if not source.is_dir():
        raise SystemExit(f"Source folder not found: {source}\nSet MINCKLEY_PDF_DIR in .env.")
    feeder = _load_json(minckley_batch.STATE_PATH)
    in_feeder = {it["mid"] for it in feeder.get("batch", [])}
    todo_csv, done_csv = minckley_lists.LISTS[args.list]
    if not todo_csv.is_file():
        raise SystemExit(f"{todo_csv.name} not found; build it with: python -m utils.minckley_lists {args.list}")
    # the feeder's skip list belongs to the public list; other lists start fresh (earlier failures are retried)
    items, missing = minckley_batch.candidates(source, feeder if args.list == "public" else {}, todo_csv, done_csv)
    items = [it for it in items if it["mid"] not in in_feeder]
    if in_feeder:
        print(f"{len(in_feeder)} MIDs are in the interactive feeder's current batch and are left to it.")
    if missing:
        print(f"{len(missing)} MIDs have no PDF in {source} and are skipped.")
    if args.size:
        items = items[: args.size]
    if not items:
        raise SystemExit("Nothing left to process.")
    model = pdf_ingest.ingest_model(args.model)
    llm_provider.api_model(model, "anthropic")  # refuses a non-Anthropic model before anything is sent
    show_plan(items, model, args.long)
    if not args.no_full_text:
        if not full_text_ignored():
            raise SystemExit(f"Refusing to save full text: add {FULL_TEXT_IGNORE} to the repo .gitignore first (or use --no-full-text).")
        print(f"  Full text of every document is saved locally to {FULL_TEXT_DIR.relative_to(pdf_ingest.BASE_DIR)} (gitignored).")
    if not args.yes and input(f"\nOCR these {len(items)} locally and send them to the Anthropic Batches API? [y/N] ").strip().lower() not in ("y", "yes"):
        raise SystemExit("Cancelled; nothing was sent.")
    return {"created": _now(), "model": model, "fallback": pdf_ingest.fallback_model(model), "long": args.long,
            "list": args.list, "full_text": not args.no_full_text,
            "items": [{"mid": it["mid"], "names": it["names"], "paths": [str(p) for p in it["paths"]]} for it in items],
            "docs": {it["mid"]: {"mid": it["mid"], "status": "pending", "pages": it.get("pages")} for it in items},
            "batches": {}, "queue": []}


def _keep_awake():
    """Windows: keep the PC from sleeping while this process runs (released automatically when it exits)."""
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
        except Exception:
            pass


def cmd_status(_args) -> int:
    state = load_state()
    if not state.get("docs"):
        print("No batch run on record.")
        return 0
    runner = Runner(state, None, _args)
    print(f"Run started {state['created']}, model {state['model']}" + (f", finished {state['finished']}" if state.get("finished") else ""))
    print(f"Documents: {runner.status_counts()}")
    t = state.get("totals", {})
    if t:
        print(f"So far: {t['in']:,} input + {t['out']:,} output tokens, about ${t['cost']:.2f} at batch price.")
    open_batches = {b: i for b, i in state["batches"].items() if not i.get("processed")}
    if open_batches:
        api = BatchAPI()
        for bid in open_batches:
            b = api.get(bid)
            print(f"  {bid}: {b.get('processing_status')} {b.get('request_counts')}")
    for m, d in state["docs"].items():
        if d["status"] == "failed":
            print(f"  {m} failed: {d.get('error', '')[:150]}")
    return 0


def cmd_cancel(_args) -> int:
    state = load_state()
    api = BatchAPI()
    for bid, info in state.get("batches", {}).items():
        if not info.get("processed"):
            api.cancel(bid)
            print(f"Cancel requested for {bid}. Requests already finished are still written on the next run.")
    print("Rerun `python -m utils.batch_ingest` to write finished results and resubmit the rest.")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(prog="batch_ingest", description=__doc__.split("\n")[0])
    ap.add_argument("action", nargs="?", default="run", choices=["run", "status", "cancel"])
    ap.add_argument("--size", type=int, default=0, help="number of documents for a new run (default: all remaining)")
    ap.add_argument("--yes", action="store_true", help="skip the cost question (for scheduled runs)")
    ap.add_argument("--long", choices=["cap", "full", "skip"], default="cap", help="documents over the 250k-character cap")
    ap.add_argument("--workers", type=int, default=max(1, min(4, (os.cpu_count() or 2) // 2)), help="documents OCRd at once")
    ap.add_argument("--chunk", type=int, default=10, help="documents extracted before each batch is submitted")
    ap.add_argument("--poll", type=int, default=300, help="seconds between status checks")
    ap.add_argument("--model", default="", help="OpenRouter-style anthropic/... model (default OPENROUTER_INGEST_MODEL)")
    ap.add_argument("--no-sync", action="store_true", help="do not commit and push the brain at the end")
    ap.add_argument("--list", choices=sorted(minckley_lists.LISTS), default="public", help="which MID list a new run takes from")
    ap.add_argument("--no-full-text", action="store_true", help="do not save the full extracted text to full_text/")
    args = ap.parse_args(argv)
    if args.action == "status":
        return cmd_status(args)
    if args.action == "cancel":
        return cmd_cancel(args)
    try:
        StubStore().require_consolidated()
    except StubStoreError as e:
        print(e)
        return 1
    api = BatchAPI()
    state = load_state()
    if state.get("docs") and not state.get("finished"):
        print(f"Resuming the run started {state['created']}: {Runner(state, api, args).status_counts()}.")
        state.setdefault("queue", [])
    else:
        if state.get("finished"):
            old = STATE_PATH.with_name(f"batch_ingest_state_{state['finished'][:10]}.json")
            shutil.move(str(STATE_PATH), str(old))
        state = new_state(args)
        save_state(state)
    _keep_awake()
    try:
        return Runner(state, api, args).run()
    except KeyboardInterrupt:
        print("\nStopped. Batches already submitted keep running at Anthropic; rerun to pick up their results.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
