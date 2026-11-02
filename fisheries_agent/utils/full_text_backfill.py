"""Backfills the local full text of Minckley Library PDFs (no LLM, nothing sent anywhere; text extraction and OCR only).

Every Minckley ID that has a PDF in MINCKLEY_PDF_DIR but no 00_Fisheries_Brain/full_text/<MID>.md gets one, in the same
format batch_ingest writes (header: citation, permission, pages, note link). The folder is gitignored and is never synced,
indexed or published. Meant to run for days in its own window:

    python -m utils.full_text_backfill plan            what is left (counts; --pages also totals pages, slower)
    python -m utils.full_text_backfill run             work through everything left (smallest PDFs first)
        --workers N     documents OCRd at once (default: half the CPU cores)
        --hours H       stop cleanly after H hours (default: run until done)
        --noted-only    only MIDs that already have a note in 01_Sources (default: those first, then the rest)
        --retry-failed  include documents that failed before
        --limit N       at most N documents this run
    python -m utils.full_text_backfill status          done / left / failed, and the last run's speed

Stop any time with Ctrl+C or by closing the window; each file is written whole (temp file, then rename), so a rerun just
continues. The process runs at below-normal priority on Windows (OCR children inherit it) and keeps the PC from sleeping
while it works. Failures are listed in runs/full_text_backfill_failed.json; the log is runs/full_text_backfill.jsonl.
Temporary OCR caches are removed after each document; the library PDFs are only read.
"""
import argparse
import csv
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from utils import brain_citations, minckley_lists, pdf_ingest, public_domain

LOG_PATH = pdf_ingest.BASE_DIR / "runs" / "full_text_backfill.jsonl"
FAILED_PATH = pdf_ingest.BASE_DIR / "runs" / "full_text_backfill_failed.json"
FULL_TEXT_DIR = public_domain.FULL_TEXT_DIR


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _say(msg: str) -> None:
    print(f"[{datetime.now().strftime('%m-%d %H:%M')}] {msg}", flush=True)


def _low_priority_and_awake() -> None:
    if os.name != "nt":
        try:
            os.nice(10)
        except OSError:
            pass
        return
    try:
        import ctypes
        k = ctypes.windll.kernel32
        k.SetPriorityClass(k.GetCurrentProcess(), 0x00004000)  # BELOW_NORMAL_PRIORITY_CLASS; Tesseract children inherit it
        k.SetThreadExecutionState(0x80000000 | 0x00000001)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED (display may still sleep)
    except Exception:
        pass


def _load_failed() -> dict:
    try:
        return json.loads(FAILED_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_failed(data: dict) -> None:
    FAILED_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = FAILED_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=1), encoding="utf-8")
    os.replace(tmp, FAILED_PATH)


def _log(rec: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"timestamp": _now(), **rec}, ensure_ascii=False) + "\n")


def note_stems() -> dict:
    """{MID: note stem} for every Minckley note (frontmatter source_id or the filename suffix)."""
    out = {}
    for stem, sid, *_ in pdf_ingest._vault_catalog():
        if str(sid).isdigit():
            out.setdefault(str(sid), stem)
    return out


def work_list(noted_only: bool = False, retry_failed: bool = False) -> tuple:
    """([(mid, [paths], total bytes, note stem)], counts) smallest first; noted MIDs before the rest."""
    source = minckley_lists.source_dir()
    if not source.is_dir():
        raise SystemExit(f"Minckley PDF folder not found: {source}\nSet MINCKLEY_PDF_DIR in .env.")
    perm = minckley_lists.permissions()
    files = minckley_lists.pdfs_by_mid(source)
    notes = note_stems()
    have = {p.stem for p in FULL_TEXT_DIR.glob("*.md")} if FULL_TEXT_DIR.is_dir() else set()
    failed = _load_failed()
    counts = {"MIDs with a PDF on disk": 0, "full text already saved": 0, "failed before (skipped)": 0}
    todo = []
    for mid, names in files.items():
        if mid not in perm:  # a number in a file name that is not a library ID (a year, a page count ...)
            continue
        counts["MIDs with a PDF on disk"] += 1
        if mid in have:
            counts["full text already saved"] += 1
            continue
        if mid in failed and not retry_failed:
            counts["failed before (skipped)"] += 1
            continue
        if noted_only and mid not in notes:
            continue
        paths = [source / n for n in minckley_lists.pick_files(mid, names)]
        todo.append((mid, paths, sum(p.stat().st_size for p in paths), notes.get(mid, "")))
    todo.sort(key=lambda t: (not t[3], t[2]))
    counts["left to extract"] = len(todo)
    counts["  of which have a note"] = sum(1 for t in todo if t[3])
    counts["  size of what is left (GB)"] = round(sum(t[2] for t in todo) / 1e9, 1)
    return todo, counts


_REFS = None


def _citation(mid: str) -> dict:
    global _REFS
    if _REFS is None:
        try:
            _REFS = brain_citations.parse_sheet(brain_citations.REFERENCE_CSV.read_text(encoding="utf-8"))
        except OSError:
            _REFS = {}
    return _REFS.get(mid, {})


def extract(mid: str, paths: list, note: str, permission: str) -> dict:
    """Runs in a worker thread: extracts every file of the MID, writes full_text/<MID>.md, returns a summary."""
    t0 = time.monotonic()
    parts, pages, ocr, methods = [], 0, 0, set()
    for p in paths:
        digest = pdf_ingest.file_hash(p)
        cache = pdf_ingest.CACHE_DIR / f"{digest[:16]}.json"
        keep_cache = cache.is_file()  # someone else's cache (an ingest in progress): leave it alone
        try:
            ex = pdf_ingest.extract_text(p, digest, verbose=False)
        finally:
            if not keep_cache:
                cache.unlink(missing_ok=True)
        if len(paths) > 1:
            parts.append(f"\n=== File: {p.name} ===")
        parts.append(ex["text"])
        pages += ex["pages"]
        ocr += len(ex["ocr_pages"])
        methods.add(ex["method"])
    text = "".join(parts)
    if len("".join(ch for ch in text.replace("--- Page", "") if ch.isalnum())) < 50:
        raise RuntimeError(f"no readable text in {pages} page(s); check the PDF by eye")
    ref = _citation(mid)
    cite = {**{k: ref.get(k, "") for k in ("authors", "year", "title", "publication", "type")}, "mid": mid}
    method = methods.pop() if len(methods) == 1 else "mixed"
    header = {"minckley_id": mid, "title": ref.get("title", ""),
              "source_citation": pdf_ingest.format_citation(cite) if ref else "", "permission": permission,
              "note": f"[[{note}]]" if note else "", "source_files": [p.name for p in paths], "backfilled": _now()[:10]}
    path = public_domain.save_full_text(mid, {"text": text, "pages": pages, "method": method}, header)
    if path is None:
        raise RuntimeError("full_text/ is not in .gitignore; refusing to write")
    return {"pages": pages, "ocr_pages": ocr, "chars": len(text), "seconds": round(time.monotonic() - t0, 1)}


def cmd_plan(args) -> int:
    todo, counts = work_list(args.noted_only, args.retry_failed)
    for k, v in counts.items():
        print(f"{k}: {v:,}" if isinstance(v, int) else f"{k}: {v}")
    if args.pages:
        from pypdf import PdfReader
        total = 0
        for _, paths, _, _ in todo:
            for p in paths:
                try:
                    total += len(PdfReader(str(p)).pages)
                except Exception:
                    pass
        print(f"pages left: {total:,}")
    rate = _recent_rate()
    if rate:
        print(f"Recent speed: {rate[0]:.1f} documents/hour ({rate[1]:.0f} pages/hour) -> roughly {len(todo) / rate[0] / 24:.1f} days at that pace.")
    return 0


def _recent_rate():
    try:
        rows = [json.loads(l) for l in LOG_PATH.read_text(encoding="utf-8").splitlines() if l.strip()]
    except OSError:
        return None
    runs = [r for r in rows if r.get("event") == "run_end" and r.get("hours")]
    if not runs or not runs[-1]["hours"]:
        return None
    r = runs[-1]
    return r["done"] / r["hours"], r["pages"] / r["hours"]


def cmd_status(args) -> int:
    if not public_domain.full_text_ignored():
        print("WARNING: full_text/ is not in .gitignore.")
    return cmd_plan(args)


def cmd_run(args) -> int:
    if not public_domain.full_text_ignored():
        print(f"Refusing to run: add {public_domain.FULL_TEXT_IGNORE} to the repo .gitignore first.")
        return 1
    todo, counts = work_list(args.noted_only, args.retry_failed)
    if args.limit:
        todo = todo[: args.limit]
    if not todo:
        print("Nothing left to extract.")
        return 0
    _say(f"{len(todo):,} documents to extract ({counts['  size of what is left (GB)']} GB), {args.workers} at a time"
         + (f", stopping after {args.hours} h" if args.hours else "") + ". Ctrl+C or closing the window stops safely.")
    _low_priority_and_awake()
    if args.workers > 1:
        os.environ.setdefault("OMP_THREAD_LIMIT", "1")  # one Tesseract thread per document
    perm = minckley_lists.permissions()
    failed = _load_failed()
    start = time.monotonic()
    deadline = start + args.hours * 3600 if args.hours else None
    done = pages = fails = 0
    _log({"event": "run_start", "todo": len(todo), "workers": args.workers})
    queue = iter(todo)
    pool = ThreadPoolExecutor(max_workers=args.workers)
    running = {}

    def submit_next() -> bool:
        if deadline and time.monotonic() > deadline:
            return False
        item = next(queue, None)
        if item is None:
            return False
        mid, paths, size, note = item
        running[pool.submit(extract, mid, paths, note, perm.get(mid, ""))] = item
        return True

    try:
        for _ in range(args.workers):
            submit_next()
        while running:
            fut = next(as_completed(list(running)))
            mid, paths, size, note = running.pop(fut)
            try:
                r = fut.result()
                done += 1
                pages += r["pages"]
                failed.pop(mid, None)
                _log({"event": "done", "mid": mid, **r})
                hrs = (time.monotonic() - start) / 3600
                left = len(todo) - done - fails
                eta = f", about {left / (done / hrs) / 24:.1f} days left at this pace" if done >= 5 and hrs > 0 else ""
                _say(f"{mid}: {r['pages']} pages ({r['ocr_pages']} OCR), {r['chars']:,} chars, {r['seconds']:.0f}s. "
                     f"{done:,} done, {left:,} left{eta}")
            except Exception as e:
                fails += 1
                failed[mid] = {"error": str(e)[:300], "files": [p.name for p in paths], "when": _now()}
                _save_failed(failed)
                _log({"event": "failed", "mid": mid, "error": str(e)[:300]})
                _say(f"{mid} FAILED: {str(e)[:150]}")
            submit_next()
    except KeyboardInterrupt:
        _say(f"Stopping. Finishing the {len(running)} document(s) in progress (Ctrl+C again stops at once; "
             "nothing half-written is ever kept). Rerun the same command to continue.")
    finally:
        hrs = (time.monotonic() - start) / 3600
        _log({"event": "run_end", "done": done, "failed": fails, "pages": pages, "hours": round(hrs, 3)})
    pool.shutdown(wait=True, cancel_futures=True)
    _say(f"Run ended: {done:,} extracted ({pages:,} pages), {fails:,} failed, {hrs:.1f} h. "
         f"{'Time limit reached; ' if deadline and time.monotonic() > deadline else ''}rerun the same command to continue.")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(prog="full_text_backfill", description=__doc__.split("\n")[0])
    ap.add_argument("action", nargs="?", default="plan", choices=["plan", "run", "status"])
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    ap.add_argument("--hours", type=float, default=0)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--noted-only", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    ap.add_argument("--pages", action="store_true", help="plan: also total the pages left (reads every PDF)")
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "run": cmd_run, "status": cmd_status}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
