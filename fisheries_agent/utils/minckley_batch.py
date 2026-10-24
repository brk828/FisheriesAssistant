"""Feeds the unprocessed public-domain Minckley PDFs to the ingest watcher in batches (default 10, up to 100; --size N), smallest first.

Run from fisheries_agent (with main_orchestrator.py running in another terminal to answer the ingest prompt):
    python -m utils.minckley_batch

PDFs are read from MINCKLEY_PDF_DIR (.env) or C:/Obsidian/Fish_Science_Brain/PDFs_To_Process.
Finished MIDs are appended to 00_Fisheries_Brain/process_public_domain_mids.csv.
When the backlog is done, remove this file, the two CSVs, and brain_meta/minckley_batch_state.json.
"""
import csv
import os
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfWriter

from utils import pdf_ingest
from utils.pdf_ingest import BRAIN_DIR, MANIFEST_PATH, META_DIR, PDF_DIR, _load_json, _save_json

TODO_CSV = BRAIN_DIR / "unprocessed_public_domain_mids.csv"
DONE_CSV = BRAIN_DIR / "process_public_domain_mids.csv"
STATE_PATH = META_DIR / "minckley_batch_state.json"
DEFAULT_SOURCE = "C:/Obsidian/Fish_Science_Brain/PDFs_To_Process"
FIELDS = ["source_filename", "mid"]
BATCH_SIZE = 10
MAX_BATCH_SIZE = 100
POLL_SECONDS = 15


def _read(path: Path) -> list:
    if not path.is_file():
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def _append_done(rows: list) -> None:
    new = not DONE_CSV.is_file() or DONE_CSV.stat().st_size == 0
    with open(DONE_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(FIELDS)
        w.writerows(rows)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _mids_with_notes() -> set:
    """MIDs that already have a note in 01_Sources (file name ends in _<MID>.md), e.g. processed before this tool
    existed or on another machine. Staging them again would only be skipped or ignored by the ingest watcher."""
    out = set()
    for f in pdf_ingest.SOURCES_DIR.glob("*.md"):
        tail = f.stem.rsplit("_", 1)[-1]
        if tail.isdigit() and 5 <= len(tail) <= 6:
            out.add(tail)
    return out


def candidates(source: Path, state: dict) -> tuple:
    """([{mid, names, paths, size}] smallest first, [mids whose PDF is not in the source folder]).
    Rows sharing a MID (e.g. '19192 (1).pdf', '19192 (2).pdf') form one item and are merged when staged."""
    done = {r["mid"] for r in _read(DONE_CSV)} | _mids_with_notes()
    excluded = set(state.get("excluded", {}))
    groups = {}
    for r in _read(TODO_CSV):
        groups.setdefault(r["mid"], []).append(r["source_filename"])
    on_disk = {p.name.lower(): p for p in source.iterdir() if p.suffix.lower() == ".pdf"}
    items, missing = [], []
    for mid, names in groups.items():
        if mid in done or mid in excluded:
            continue
        names = sorted(names)
        paths = [on_disk.get(n.lower()) for n in names]
        if not all(paths):
            missing.append(mid)
            continue
        items.append({"mid": mid, "names": names, "paths": paths, "size": sum(p.stat().st_size for p in paths)})
    return sorted(items, key=lambda i: i["size"]), missing


def show_estimate(batch: list) -> None:
    model = pdf_ingest.ingest_model()
    sizes, total_pages, long_docs = [], 0, []
    print(f"\nNext {len(batch)} (smallest first):")
    for it in batch:
        chars = pages = ocr = 0
        for p in it["paths"]:
            c, pg, o = pdf_ingest.quick_estimate(p)
            chars, pages, ocr = chars + c, pages + pg, ocr + o
        total_pages += pages
        sizes.append(min(chars, pdf_ingest.MAX_NOTE_CHARS) if chars else 20_000)
        flag = ""
        if chars > pdf_ingest.MAX_NOTE_CHARS:
            long_docs.append(it["mid"])
            flag = f"  TOO LONG (~{chars:,} chars)"
        merged = f" (merges {len(it['paths'])} files)" if len(it["paths"]) > 1 else ""
        scan = f", {ocr} need OCR" if ocr else ""
        print(f"  {it['mid']}: {pages} pages{scan}, {it['size'] / 1024:,.0f} KB{merged}{flag}")
    in_tok, out_tok = pdf_ingest.estimate_tokens(sizes)
    print(f"Total {total_pages} pages. Model: {model}. {pdf_ingest._cost_text(model, in_tok, out_tok)} (scanned pages are a rough guess)")
    if long_docs:
        print(f"Too long for the default cap ({pdf_ingest.MAX_NOTE_CHARS:,} chars): {', '.join(long_docs)}. You choose cap/full/skip in the ingest prompt.")


def stage(item: dict) -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    dest = PDF_DIR / f"{item['mid']}.pdf"
    tmp = dest.with_suffix(".tmp")  # not *.pdf, so the watcher ignores it until complete; copyfile gives a fresh mtime
    if len(item["paths"]) == 1:
        shutil.copyfile(item["paths"][0], tmp)
    else:
        writer = PdfWriter()
        for p in item["paths"]:
            writer.append(str(p))
        with open(tmp, "wb") as f:
            writer.write(f)
    os.replace(tmp, dest)


_HASHES = {}


def _hash(path: Path) -> str:
    """File hash, cached by (name, size, mtime) so the 15-second poll does not re-read unchanged PDFs."""
    st = path.stat()
    key = (path.name, st.st_size, st.st_mtime)
    if key not in _HASHES:
        _HASHES[key] = pdf_ingest.file_hash(path)
    return _HASHES[key]


def _statuses(state: dict) -> dict:
    """{mid: 'done' | 'skipped' | 'failed' | 'duplicate' | None} from the ingest manifest.
    'duplicate': the file left pdfs_to_process without a new record (an exact copy of a note already in the brain)."""
    manifest = _load_json(MANIFEST_PATH)
    latest = {}
    for rec in sorted(manifest.values(), key=lambda r: r.get("timestamp", "")):
        if rec.get("timestamp", "") >= state["staged_at"]:
            latest[rec.get("file")] = rec
    out = {}
    for it in state["batch"]:
        name = f"{it['mid']}.pdf"
        rec = latest.get(name)
        if rec:
            out[it["mid"]] = rec.get("status") if rec.get("status") in ("done", "skipped", "failed") else None
        else:
            staged = PDF_DIR / name
            if staged.exists() and manifest.get(_hash(staged), {}).get("status") == "done":
                # an identical file was finished before this batch; the watcher ignores it, so it would wait forever
                staged.unlink(missing_ok=True)
                print(f"  {it['mid']}: identical PDF already processed earlier; removed the staged copy")
            out[it["mid"]] = None if staged.exists() else "duplicate"
    return out


def wait_and_finish(state: dict) -> None:
    print(f"\nWaiting for {len(state['batch'])} documents. Keep main_orchestrator.py running and answer its ingest prompt. Ctrl+C to stop; rerun to resume.")
    last = None
    while True:
        status = _statuses(state)
        pending = [m for m, s in status.items() if s is None]
        if (len(status) - len(pending), len(pending)) != last:
            last = (len(status) - len(pending), len(pending))
            print(f"  {last[0]} finished, {last[1]} waiting")
        if not pending:
            break
        time.sleep(POLL_SECONDS)
    ok = [it for it in state["batch"] if status[it["mid"]] in ("done", "duplicate")]
    _append_done([[n, it["mid"]] for it in ok for n in it["names"]])
    for it in state["batch"]:
        if status[it["mid"]] in ("skipped", "failed"):
            state.setdefault("excluded", {})[it["mid"]] = status[it["mid"]]
            print(f"  {it['mid']} {status[it['mid']]}; left out of future batches (still in pdfs_to_process if the file remains).")
    print(f"Recorded {len(ok)} MIDs in {DONE_CSV.name}.")
    state.pop("batch")
    _save_json(STATE_PATH, state)
    pdf_ingest.sync_to_github("Update processed Minckley MIDs", extra_paths=(DONE_CSV.relative_to(pdf_ingest.BASE_DIR).as_posix(),))


def _clamp(n: int) -> int:
    return max(1, min(MAX_BATCH_SIZE, n))


def ask_size(current: int) -> int:
    """Lets the user change the batch size (1-100); Enter keeps the current value."""
    raw = input(f"Documents per batch [{current}] (1-{MAX_BATCH_SIZE}, Enter to keep): ").strip()
    if not raw:
        return current
    if not raw.isdigit() or not 1 <= int(raw) <= MAX_BATCH_SIZE:
        print(f"Not a number from 1 to {MAX_BATCH_SIZE}; keeping {current}.")
        return current
    return int(raw)


def main(argv: list = None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="minckley_batch")
    ap.add_argument("--size", type=int, default=0, help=f"documents per batch, 1-{MAX_BATCH_SIZE} (default {BATCH_SIZE}; asked interactively if omitted)")
    args = ap.parse_args(argv)
    size = _clamp(args.size) if args.size else None
    try:
        from dotenv import load_dotenv
        load_dotenv(pdf_ingest.BASE_DIR / ".env")
    except ImportError:
        pass
    source = Path(os.getenv("MINCKLEY_PDF_DIR") or DEFAULT_SOURCE)
    if not source.is_dir():
        print(f"Source folder not found: {source}\nSet MINCKLEY_PDF_DIR in .env.")
        return 1
    state = _load_json(STATE_PATH)
    try:
        while True:
            if not state.get("batch"):
                items, missing = candidates(source, state)
                if missing:
                    print(f"{len(missing)} MIDs have no PDF in {source} and are skipped for now.")
                if not items:
                    print("Nothing left to process. The Minckley backlog is complete; you can remove this tool.")
                    return 0
                if size is None:
                    size = ask_size(BATCH_SIZE)
                batch = items[:size]
                print(f"{len(items)} documents remain.")
                show_estimate(batch)
                if input(f"\nCopy these {len(batch)} into pdfs_to_process? [y/N] ").strip().lower() not in ("y", "yes"):
                    return 0
                state["batch"] = [{"mid": i["mid"], "names": i["names"]} for i in batch]
                state["staged_at"] = _now()
                _save_json(STATE_PATH, state)
                for it in batch:
                    stage(it)
            wait_and_finish(state)
            if input(f"\nProcess another {size}? [y/N] ").strip().lower() not in ("y", "yes"):
                return 0
            size = ask_size(size)
    except KeyboardInterrupt:
        print("\nStopped. Rerun to resume.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
