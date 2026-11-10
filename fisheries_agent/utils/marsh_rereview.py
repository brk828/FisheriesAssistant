"""Re-run the public-domain review for Marsh documents whose text was garbled when they were first catalogued.

    python -m utils.marsh_rereview plan [--ids PML0001 ...]    what would be sent (default: the PML codes in
                                                                runs/reocr/improved.csv)
    python -m utils.marsh_rereview run [--ids ...] [--yes]       estimate, ask, submit one batch, wait, apply (resumable)
    python -m utils.marsh_rereview status

Launcher: start_marsh_rereview.bat. Needs ANTHROPIC_API_KEY in .env (Anthropic Batches API, 50% price).

Each document gets the same catalog request as the original Marsh ingest (public_domain.META_SYSTEM and meta_user),
built from its current full_text/<code>.md (the re-OCR'd text) and its original file name. The reply sets category,
confidence, permission, copyright notice and reason in brain_meta/marsh_catalog.csv; authors, year and publication
are filled only where the catalog had none or had them from the file name only. A hand override in the
permission_override column still wins. Every change of call is written to runs/marsh_rereview/changes.csv
(old and new category and permission, reason). Afterwards the notes' permission field and the
MarshLibrary_PublicDomain folder are brought in line (`marsh_ingest apply-overrides`); PDFs newly public still need
uploading (`python -m utils.site_ftp folder ...`) and any that are no longer public must be removed from the server.
"""
import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone

from utils import batch_ingest, llm_provider, marsh_ingest, pdf_ingest, public_domain

WORK = pdf_ingest.BASE_DIR / "runs" / "marsh_rereview"
STATE = WORK / "state.json"
CHANGES = WORK / "changes.csv"
DEFAULT_LIST = pdf_ingest.BASE_DIR / "runs" / "reocr" / "improved.csv"
POLL_SECONDS = 60


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _say(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def read_ids(args) -> list:
    if args.ids:
        return list(dict.fromkeys(args.ids))
    with open(DEFAULT_LIST, newline="", encoding="utf-8") as f:
        return [r["id"] for r in csv.DictReader(f) if r["id"].startswith("PML")]


def requests_for(ids: list, model: str) -> tuple:
    from utils.reocr import split_full_text
    rows = {r["code"]: r for r in marsh_ingest.read_catalog()}
    reqs, skipped = [], []
    for code in ids:
        row, ft = rows.get(code), batch_ingest.FULL_TEXT_DIR / f"{code}.md"
        if not row or row["status"] != "done" or not ft.is_file():
            skipped.append(code)
            continue
        head, text = split_full_text(ft)
        user = public_domain.meta_user(row["file"], {"text": text, "pages": head.get("pages", row.get("pages", ""))})
        reqs.append(batch_ingest._request(f"meta-{code}", model, public_domain.META_SYSTEM, user, public_domain.META_MAX_TOKENS))
    return reqs, skipped


def estimate(reqs: list, model: str) -> str:
    tin = sum(len(r["params"]["system"]) + len(r["params"]["messages"][0]["content"]) for r in reqs) // 4
    tout = len(reqs) * 250
    price = pdf_ingest._price(model)
    cost = f", about ${(tin * price[0] + tout * price[1]) * batch_ingest.BATCH_DISCOUNT:.2f}" if price else " (price unavailable)"
    return f"{len(reqs)} catalog requests, ~{tin:,} input + ~{tout:,} output tokens on {model} (Batches API, 50%){cost}."


def apply_reply(row: dict, meta: dict) -> dict:
    """Updates one catalog row from a reply; returns the change record."""
    cat, perm = public_domain.decide(meta)
    change = {"code": row["code"], "old_category": row["category"], "new_category": cat,
              "old_permission": row["permission"], "new_permission": perm, "confidence": meta.get("confidence", ""),
              "override": row.get("permission_override", ""), "reason": meta.get("reason", "")}
    row.update(category=cat, permission=perm, confidence=meta.get("confidence", ""),
               doc_type=meta.get("document_type", row.get("doc_type", "")),
               copyright_notice=(meta.get("copyright_notice") or "")[:300], reason=meta.get("reason", ""))
    weak = not row.get("authors") or "file name" in row.get("authors", "")
    for k in ("authors", "year", "publication"):
        if meta.get(k) and (weak or not row.get(k)):
            row[k] = meta[k]
    return change


def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}


def save_state(state: dict) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")


def cmd_plan(args) -> int:
    llm_provider._load_env()
    model = pdf_ingest.ingest_model(args.model)
    reqs, skipped = requests_for(read_ids(args), model)
    if skipped:
        print(f"skipped (no catalog row or full text): {', '.join(skipped)}")
    print(estimate(reqs, model))
    return 0


def cmd_run(args) -> int:
    llm_provider._load_env()
    state = load_state()
    api = batch_ingest.BatchAPI()
    if not state or state.get("finished"):
        model = pdf_ingest.ingest_model(args.model)
        reqs, skipped = requests_for(read_ids(args), model)
        if skipped:
            print(f"skipped (no catalog row or full text): {', '.join(skipped)}")
        print(estimate(reqs, model))
        if not reqs:
            return 0
        if not args.yes and input("Send these to the Anthropic Batches API? [y/N] ").strip().lower() not in ("y", "yes"):
            print("Nothing sent.")
            return 0
        batch = api.create(reqs)
        state = {"created": _now(), "model": model, "batch": batch["id"], "requests": len(reqs), "totals": {"in": 0, "out": 0, "cost": 0.0}}
        save_state(state)
        _say(f"Submitted batch {batch['id']} with {len(reqs)} requests.")
    batch_ingest._keep_awake()
    while True:
        info = api.get(state["batch"])
        if info.get("processing_status") == "ended":
            break
        c = info.get("request_counts", {})
        _say(f"{c.get('succeeded', 0)} done, {c.get('processing', 0)} processing; checking again in {POLL_SECONDS}s.")
        time.sleep(POLL_SECONDS)
    rows = marsh_ingest.read_catalog()
    by_code = {r["code"]: r for r in rows}
    changes, failed = [], []
    price = pdf_ingest._price(state["model"])
    for r in api.results(info):
        code = r["custom_id"].split("-", 1)[1]
        res = r["result"]
        if res.get("type") != "succeeded":
            failed.append(code)
            continue
        msg = res["message"]
        u = msg.get("usage", {})
        state["totals"]["in"] += u.get("input_tokens", 0)
        state["totals"]["out"] += u.get("output_tokens", 0)
        if price:
            state["totals"]["cost"] += (u.get("input_tokens", 0) * price[0] + u.get("output_tokens", 0) * price[1]) * batch_ingest.BATCH_DISCOUNT
        text = "".join(b.get("text", "") for b in msg.get("content", []) if b.get("type") == "text")
        meta = public_domain.parse_meta(text)
        if code in by_code:
            changes.append(apply_reply(by_code[code], meta))
    marsh_ingest.write_catalog(rows)
    WORK.mkdir(parents=True, exist_ok=True)
    with open(CHANGES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(changes[0]) if changes else ["code"])
        w.writeheader()
        w.writerows(changes)
    state.update(finished=_now(), failed=failed)
    save_state(state)
    marsh_ingest.cmd_apply_overrides(None)
    return cmd_status(args)


def cmd_status(_args) -> int:
    state = load_state()
    if not state:
        print("No re-review run yet.")
        return 0
    print(f"Batch {state['batch']} ({state['requests']} requests), started {state['created']}"
          + (f", finished {state['finished']}" if state.get("finished") else ", still running")
          + f"; ${state['totals']['cost']:.2f}.")
    if state.get("failed"):
        print(f"failed: {', '.join(state['failed'])}")
    if CHANGES.is_file():
        with open(CHANGES, newline="", encoding="utf-8") as f:
            ch = list(csv.DictReader(f))
        moved = [c for c in ch if c["old_permission"] != c["new_permission"]]
        print(f"{len(moved)} of {len(ch)} calls changed (details in {CHANGES}):")
        for c in moved:
            o = f" [your override: {c['override']}]" if c["override"] else ""
            print(f"  {c['code']}: {c['old_permission']} -> {c['new_permission']} ({c['new_category']}, {c['confidence']}){o}")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", nargs="?", default="plan", choices=["plan", "run", "status"])
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--model", default="")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "run": cmd_run, "status": cmd_status}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
