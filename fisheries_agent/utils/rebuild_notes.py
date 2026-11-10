"""Rebuild source notes from their saved full text (after a re-OCR), on the Anthropic Message Batches API (50% price).

    python -m utils.rebuild_notes plan [--ids ID ...]          what would be sent and an estimate (default list:
                                                                runs/reocr/improved.csv)
    python -m utils.rebuild_notes run [--ids ID ...] [--yes]    estimate, ask, submit, wait, write notes (resumable)
    python -m utils.rebuild_notes status | cancel

Launcher: start_rebuild_notes.bat. Needs ANTHROPIC_API_KEY in .env.

For each ID the text comes from 00_Fisheries_Brain/full_text/<ID>.md (header removed), capped at MAX_NOTE_CHARS, and
goes through the same note prompt as batch ingest (pdf_ingest.note_request). The new note replaces the old one under
the same file name. The library fields of the old note are kept (title, source_id, minckley_id, marsh_id, library,
permission, access_category, source_citation, doi, source_file, doc_type, secondary_type), except that a placeholder
title written from unreadable text ("Unreadable OCR Scan ...") is replaced by the new note's heading, also in the
citation, external_citations.json and the Marsh catalog (listed by `status`); text_extraction is taken
from the full-text header and `rebuilt` gets today's date. The old note's stub links are removed first
(remove_notes.clean_stubs) and the new ones added (pdf_ingest.update_stubs); new stubs get summaries in a second
batch. A reply cut off at the output limit is retried once on the fallback model with twice the budget; an
incomplete note once on the same model. State: runs/rebuild_notes/state.json; usage: runs/rebuild_notes/usage.jsonl.
Afterwards commit and push 01_Sources and 02_Brain.
"""
import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from utils import batch_ingest, llm_provider, pdf_ingest, remove_notes
from utils.stub_store import StubStore

WORK = pdf_ingest.BASE_DIR / "runs" / "rebuild_notes"
STATE = WORK / "state.json"
USAGE = WORK / "usage.jsonl"
DEFAULT_LIST = pdf_ingest.BASE_DIR / "runs" / "reocr" / "improved.csv"
FULL_TEXT_DIR = pdf_ingest.BRAIN_DIR / "full_text"
KEEP = ("title", "source_id", "minckley_id", "marsh_id", "library", "permission", "access_category",
        "source_citation", "doi", "source_file", "doc_type", "secondary_type")
POLL_SECONDS = 60
# titles the model wrote from unreadable text ("Unreadable OCR Scan: No Extractable ..."): replaced by the new note's heading
PLACEHOLDER_TITLE = re.compile(r"^(unreadable|illegible|fragmentary|garbled|corrupted|untitled|unidentified|"
                               r"no (extractable|readable|legible))|\b(ocr|scan)\b.*\b(unreadable|illegible|garbled|no extractable)",
                               re.I)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _say(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def fallback_model(primary: str) -> str:
    llm_provider._load_env()
    return pdf_ingest.fallback_model(primary)


# ------------------------------------------------------------------ inputs
def read_ids(args) -> list:
    if args.ids:
        return list(dict.fromkeys(args.ids))
    if not DEFAULT_LIST.is_file():
        raise SystemExit(f"No list: {DEFAULT_LIST} is missing (run `python -m utils.reocr apply` first) or pass --ids.")
    with open(DEFAULT_LIST, newline="", encoding="utf-8") as f:
        return [r["id"] for r in csv.DictReader(f)]


def full_text(doc_id: str) -> tuple:
    """(header dict, text) from full_text/<ID>.md."""
    from utils.reocr import split_full_text
    path = FULL_TEXT_DIR / f"{doc_id}.md"
    if not path.is_file():
        raise RuntimeError(f"no full text at {path.name}")
    return split_full_text(path)


_NOTES = {}


def note_path(doc_id: str) -> Path:
    """The note for an ID: file-name suffix first, then frontmatter source_id (older hand-added Minckley notes)."""
    try:
        return remove_notes.resolve(doc_id)
    except SystemExit:
        if not _NOTES:
            from utils.reocr import note_index
            _NOTES.update(note_index())
        if doc_id in _NOTES:
            return _NOTES[doc_id]
        raise


def old_fields(note: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", note, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if k in KEEP and v:
            try:
                out[k] = json.loads(v) if v[:1] in "\"[{" else v
            except ValueError:
                out[k] = v.strip('"')
    return out


# ------------------------------------------------------------------- plan
def prepare(ids: list) -> tuple:
    docs, problems = {}, []
    for doc_id in ids:
        try:
            head, text = full_text(doc_id)
            path = note_path(doc_id)
        except (RuntimeError, SystemExit) as e:
            problems.append(f"{doc_id}: {e}")
            continue
        limit = min(len(text), pdf_ingest.MAX_NOTE_CHARS)
        docs[doc_id] = {"id": doc_id, "stem": path.stem, "chars": len(text), "limit": limit,
                        "method": head.get("text_extraction", ""), "status": "pending"}
    return docs, problems


def estimate(docs: dict, model: str) -> str:
    in_tok, out_tok = pdf_ingest.estimate_tokens([d["limit"] for d in docs.values()])
    price = pdf_ingest._price(model)
    chars = sum(d["chars"] for d in docs.values())
    capped = sum(1 for d in docs.values() if d["chars"] > d["limit"])
    line = (f"{len(docs)} notes from {chars:,} characters of full text"
            + (f" ({capped} capped at {pdf_ingest.MAX_NOTE_CHARS:,})" if capped else "")
            + f"; model {model} on the Batches API (50% of list price).")
    if price:
        cost = (in_tok * price[0] + out_tok * price[1]) * batch_ingest.BATCH_DISCOUNT
        line += f"\n  Estimate: ~{in_tok:,} input + ~{out_tok:,} output tokens, about ${cost:.2f} including new stub summaries."
    else:
        line += f"\n  Estimate: ~{in_tok:,} input + ~{out_tok:,} output tokens (price unavailable)."
    return line


def cmd_plan(args) -> int:
    llm_provider._load_env()
    model = pdf_ingest.ingest_model(args.model)
    docs, problems = prepare(read_ids(args))
    for p in problems:
        print("  skipped " + p)
    print(estimate(docs, model))
    return 0


# -------------------------------------------------------------------- run
def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}


def save_state(state: dict) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1), encoding="utf-8")
    os.replace(tmp, STATE)


def _note_req(doc: dict, state: dict) -> dict:
    _, text = full_text(doc["id"])
    system, user, _, budget = pdf_ingest.note_request(text, doc["limit"])
    model = doc.get("model") or state["model"]
    cid = f"note-{doc['id']}-{doc.get('attempt', 0)}"
    doc["status"] = "submitted"
    return batch_ingest._request(cid, model, system, user, doc.get("budget") or budget)


def _stub_reqs(doc: dict, state: dict) -> list:
    note = (pdf_ingest.SOURCES_DIR / f"{doc['stem']}.md").read_text(encoding="utf-8")
    out = []
    for i, (names, user, budget) in enumerate(pdf_ingest.stub_requests(note, doc.get("created", []))):
        cid = f"stub-{doc['id']}-{i}"
        state.setdefault("stub_names", {})[cid] = names
        out.append(batch_ingest._request(cid, state["model"], pdf_ingest.STUB_SYSTEM, user, budget))
    doc["created"] = []
    return out


def _usage(state: dict, doc_id: str, model: str, usage: dict, kind: str) -> None:
    tin, tout = usage.get("input_tokens", 0), usage.get("output_tokens", 0)
    price = pdf_ingest._price(model)
    cost = round((tin * price[0] + tout * price[1]) * batch_ingest.BATCH_DISCOUNT, 6) if price else None
    state["totals"]["in"] += tin
    state["totals"]["out"] += tout
    state["totals"]["cost"] += cost or 0
    WORK.mkdir(parents=True, exist_ok=True)
    with open(USAGE, "a", encoding="utf-8") as f:
        f.write(json.dumps({"timestamp": _now(), "id": doc_id, "kind": kind, "model": model, "input_tokens": tin,
                            "output_tokens": tout, "cost_usd": cost, "provider": "anthropic-batch"}) + "\n")


def write_rebuilt(doc: dict, note: str) -> tuple:
    """Replaces the note under the same name; returns (stubs updated, stubs created)."""
    path = pdf_ingest.SOURCES_DIR / f"{doc['stem']}.md"
    keep = old_fields(path.read_text(encoding="utf-8")) if path.is_file() else {}
    old_title, new_title = keep.get("title", ""), pdf_ingest.note_title(note)
    if old_title and new_title and PLACEHOLDER_TITLE.search(old_title) and not PLACEHOLDER_TITLE.search(new_title):
        keep["title"] = new_title
        if keep.get("source_citation"):
            keep["source_citation"] = keep["source_citation"].replace(old_title.rstrip("."), new_title.rstrip("."))
        retitle(doc["id"], new_title)
        doc["retitled"] = [old_title, new_title]
    note = pdf_ingest.set_frontmatter(note, {**keep, "text_extraction": doc.get("method", ""), "rebuilt": _now()[:10]})
    if keep.get("title"):  # the heading follows the library title
        note = re.sub(r"^# .+$", "# " + keep["title"].replace("\\", "/"), note, count=1, flags=re.M)
    store = StubStore()
    remove_notes.clean_stubs(store, [doc["stem"]])
    store.flush()
    tmp = path.with_suffix(".tmp")
    tmp.write_text(note, encoding="utf-8")
    os.replace(tmp, path)
    return pdf_ingest.update_stubs(doc["stem"], note)


def retitle(doc_id: str, title: str) -> None:
    """Carries a corrected title into the citation store and, for Marsh codes, the catalog."""
    path = pdf_ingest.BRAIN_DIR.parent / "brain_meta" / "external_citations.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    if doc_id in data:
        data[doc_id]["title"] = title
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    if doc_id.startswith("PML"):
        from utils import marsh_ingest
        rows = marsh_ingest.read_catalog()
        for r in rows:
            if r["code"] == doc_id:
                r["title"] = title
        marsh_ingest.write_catalog(rows)


def handle_note(state: dict, doc: dict, result: dict) -> None:
    model = doc.get("model") or state["model"]
    if result.get("type") != "succeeded":
        if doc.get("tries", 0) < 3:
            doc["tries"] = doc.get("tries", 0) + 1
            doc["status"] = "retry"
        else:
            doc.update(status="failed", error=str(result.get("error") or result.get("type")))
        return
    msg = result["message"]
    _usage(state, doc["id"], model, msg.get("usage", {}), "note")
    text = "".join(b.get("text", "") for b in msg.get("content", []) if b.get("type") == "text")
    attempt = doc.get("attempt", 0)
    if msg.get("stop_reason") == "max_tokens":
        if attempt == 0:
            doc.update(attempt=1, model=fallback_model(model) or model, budget=pdf_ingest.NOTE_MAX_TOKENS * 2, status="retry")
        else:
            doc.update(status="failed", error="reply reached the output limit twice")
        return
    note, complete = pdf_ingest.parse_note(text, pdf_ingest.REQUIRED_HEADERS)
    if not complete:
        if attempt == 0:
            doc.update(attempt=1, status="retry")
        else:
            doc.update(status="failed", error=str(pdf_ingest.incomplete_note_error(note)))
        return
    upd, created = write_rebuilt(doc, note)
    doc.update(status="done", created=created, finished=_now())
    _say(f"{doc['id']}: rewrote {doc['stem']}.md, {upd} stubs linked ({len(created)} new)")


def submit(state: dict, api) -> bool:
    """Sends retries/pending notes and pending stub summaries as one batch; False when there was nothing to send."""
    reqs = [_note_req(d, state) for d in state["docs"].values() if d["status"] in ("pending", "retry")]
    for d in state["docs"].values():
        if d["status"] == "done" and d.get("created"):
            reqs += _stub_reqs(d, state)
    if not reqs:
        return False
    batch = api.create(reqs)
    state["batches"].append({"id": batch["id"], "requests": len(reqs), "created": _now(), "processed": False})
    save_state(state)
    _say(f"Submitted batch {batch['id']} with {len(reqs)} requests.")
    return True


def collect(state: dict, api) -> None:
    for b in state["batches"]:
        if b["processed"]:
            continue
        while True:
            info = api.get(b["id"])
            if info.get("processing_status") == "ended":
                break
            c = info.get("request_counts", {})
            _say(f"Batch {b['id']}: {c.get('succeeded', 0)} done, {c.get('processing', 0)} processing; checking again in {POLL_SECONDS}s.")
            time.sleep(POLL_SECONDS)
        store = None
        for r in api.results(info):
            cid = r["custom_id"]
            kind, doc_id = cid.split("-")[0], cid.split("-")[1]
            doc = state["docs"].get(doc_id)
            if doc is None:
                continue
            if kind == "note":
                try:
                    handle_note(state, doc, r["result"])
                except Exception as e:  # one bad note must not stop the run
                    doc.update(status="failed", error=f"{type(e).__name__}: {e}")
            elif r["result"].get("type") == "succeeded":
                msg = r["result"]["message"]
                _usage(state, doc_id, state["model"], msg.get("usage", {}), "stub")
                text = "".join(x.get("text", "") for x in msg.get("content", []) if x.get("type") == "text")
                store = store or StubStore()
                pdf_ingest.apply_stub_summaries(text, state.get("stub_names", {}).get(cid, []), store)
            save_state(state)
        if store:
            store.flush()
        b["processed"] = True
        save_state(state)


def cmd_run(args) -> int:
    state = load_state()
    if state and not state.get("finished"):
        _say(f"Resuming the run started {state['created']}.")
    else:
        llm_provider._load_env()
        model = pdf_ingest.ingest_model(args.model)
        docs, problems = prepare(read_ids(args))
        for p in problems:
            print("  skipped " + p)
        if not docs:
            print("Nothing to rebuild.")
            return 0
        print(estimate(docs, model))
        if not args.yes and input("Send these to the Anthropic Batches API? [y/N] ").strip().lower() not in ("y", "yes"):
            print("Nothing sent.")
            return 0
        state = {"created": _now(), "model": model, "docs": docs, "batches": [],
                 "totals": {"in": 0, "out": 0, "cost": 0.0}}
        save_state(state)
    api = batch_ingest.BatchAPI()
    batch_ingest._keep_awake()
    collect(state, api)
    while submit(state, api):
        collect(state, api)
    state["finished"] = _now()
    save_state(state)
    return cmd_status(args)


def cmd_status(_args) -> int:
    state = load_state()
    if not state:
        print("No rebuild run yet.")
        return 0
    counts = {}
    for d in state["docs"].values():
        counts[d["status"]] = counts.get(d["status"], 0) + 1
    t = state["totals"]
    print(f"Run of {state['created']}: {counts}; {t['in']:,} input + {t['out']:,} output tokens, ${t['cost']:.2f}"
          + (f"; finished {state['finished']}" if state.get("finished") else ""))
    for d in state["docs"].values():
        if d["status"] == "failed":
            print(f"  {d['id']}: {d.get('error', '')}")
    retitled = [d for d in state["docs"].values() if d.get("retitled")]
    if retitled:
        print(f"{len(retitled)} placeholder titles replaced by the new note's heading (check these):")
        for d in retitled:
            print(f"  {d['id']}: {d['retitled'][1]}")
    return 0


def cmd_cancel(_args) -> int:
    state = load_state()
    api = batch_ingest.BatchAPI()
    for b in state.get("batches", []):
        if not b["processed"]:
            api.cancel(b["id"])
            print(f"cancel requested for {b['id']}")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", nargs="?", default="plan", choices=["plan", "run", "status", "cancel"])
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--model", default="")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "run": cmd_run, "status": cmd_status, "cancel": cmd_cancel}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
