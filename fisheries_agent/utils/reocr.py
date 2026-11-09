"""Re-OCR documents whose saved full text is garbled (old scanner text layers, sideways or upside-down pages).

    python -m utils.reocr plan [--max-score 0.45] [--min-phrases 2] [--ids ID ...]   pick the documents
    python -m utils.reocr run [--workers N] [--hours H] [--seconds S]                 OCR them (resumable)
    python -m utils.reocr status                                                      progress and gains
    python -m utils.reocr apply [--min-gain 0.10] [--dry-run]                         replace improved full text

Local only: no LLM, nothing is sent anywhere. Launcher: start_reocr.bat.

How a document is picked (plan): its full_text/<ID>.md has a low "readable-word share" (the share of words of three or
more letters that occur in at least 8 of 1,500 sampled library texts), or its note says two or more times that nothing
could be extracted. --ids picks documents by hand.

How a page is read (run): rendered at 300 dpi in grey, OCR'd upright; when the result reads poorly the page is also
tried at 180, 90 and 270 degrees and, if still poor, with a black-and-white threshold. The best reading wins, and the
old text of that page is kept when it scores higher. Results go to runs/reocr/ (gitignored): text/<ID>.md and one
line per document in results.jsonl. Nothing in full_text/ changes until `apply`, which backs up the old file to
runs/reocr/old/ and lists the replaced IDs in runs/reocr/improved.csv (the notes to rebuild next).
"""
import argparse
import csv
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from utils import pdf_ingest

BRAIN = pdf_ingest.BRAIN_DIR
FULL_TEXT_DIR = BRAIN / "full_text"
SOURCES_DIR = pdf_ingest.SOURCES_DIR
WORK = pdf_ingest.BASE_DIR / "runs" / "reocr"
TARGETS = WORK / "targets.csv"
RESULTS = WORK / "results.jsonl"
VOCAB = WORK / "vocab.json"
DPI = 300
TRY_MORE = 0.80  # below this an upright reading gets the other rotations
TRY_THRESH = 0.60
TOKEN = re.compile(r"[A-Za-z]{3,}")
PAGE_SPLIT = re.compile(r"^--- Page (\d+) ---\s*$", re.M)
EMPTY_NOTE = re.compile(
    r"no (usable|extractable|scientific|coherent|legible|readable|meaningful)[^.]{0,60}(data|content|text|information|findings)"
    r"|could not be (extracted|identified|determined)|placeholder|extraction_status:\s*\"?failed|unusable|re-?scan"
    r"|almost entirely (unreadable|illegible|garbled)|no data (available|extractable)", re.I)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ------------------------------------------------------------------ scoring
def split_full_text(path: Path) -> tuple:
    """(header dict, body text) of a full_text file."""
    t = path.read_text(encoding="utf-8", errors="replace")
    head = {}
    if t.startswith("---"):
        end = t.find("\n---", 3)
        for line in t[3:end].strip().splitlines():
            k, _, v = line.partition(":")
            try:
                head[k.strip()] = json.loads(v.strip())
            except ValueError:
                head[k.strip()] = v.strip()
        t = t[end + 4:]
    t = re.sub(r"\A\s*> Local reference copy[^\n]*\n", "", t)
    return head, t.lstrip("\n")


def load_vocab() -> set:
    if VOCAB.is_file():
        return set(json.loads(VOCAB.read_text(encoding="utf-8")))
    files = sorted(FULL_TEXT_DIR.glob("*.md"))
    random.Random(1).shuffle(files)
    df = {}
    for p in files[:1500]:
        for w in {w.lower() for w in TOKEN.findall(split_full_text(p)[1])}:
            df[w] = df.get(w, 0) + 1
    words = sorted(w for w, c in df.items() if c >= 8)
    WORK.mkdir(parents=True, exist_ok=True)
    VOCAB.write_text(json.dumps(words), encoding="utf-8")
    return set(words)


def score(text: str, vocab: set) -> float:
    words = [w.lower() for w in TOKEN.findall(text)]
    return round(sum(w in vocab for w in words) / len(words), 3) if words else 0.0


def pages_of(body: str) -> dict:
    """{page number: text} from '--- Page N ---' markers."""
    parts = PAGE_SPLIT.split(body)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


# --------------------------------------------------------------------- plan
def note_index() -> dict:
    """{ID: note path} for every source note (file suffix or frontmatter source_id)."""
    out = {}
    for p in SOURCES_DIR.glob("*.md"):
        m = re.search(r"_((?:PML|FAL)\d{4}|\d{5,6})$", p.stem)
        if not m:
            m = re.search(r'source_id:\s*"?(\d{5,6})', p.read_text(encoding="utf-8", errors="replace")[:1500])
        if m:
            out.setdefault(m.group(1), p)
    return out


_CACHE = {}


def _cached(key, make):
    if key not in _CACHE:
        _CACHE[key] = make()
    return _CACHE[key]


def pdf_paths(doc_id: str, head: dict) -> list:
    """The PDF(s) behind a full_text file: Marsh catalog for PML codes, else the Minckley PDF folder."""
    if doc_id.startswith("PML"):
        from utils import marsh_ingest
        cat = _cached("marsh", lambda: {r["code"]: r for r in marsh_ingest.read_catalog()})
        row = cat.get(doc_id)
        return [marsh_ingest.source_dir() / row["file"]] if row and row["file"] else []
    from utils import minckley_lists
    src = minckley_lists.source_dir()
    names = head.get("source_files") or []
    if isinstance(names, str):
        names = [names]
    if not names:
        by_mid = _cached("mids", lambda: minckley_lists.pdfs_by_mid(src))
        names = minckley_lists.pick_files(doc_id, by_mid.get(doc_id, []))
    return [src / n for n in names]


def cmd_plan(args) -> int:
    vocab = load_vocab()
    notes = note_index()
    rows = []
    ids = args.ids or sorted(p.stem for p in FULL_TEXT_DIR.glob("*.md"))
    for k, doc_id in enumerate(ids, 1):
        if k % 2000 == 0:
            print(f"  checked {k} of {len(ids)}", flush=True)
        ft = FULL_TEXT_DIR / f"{doc_id}.md"
        if not ft.is_file() or doc_id not in notes:
            continue
        head, body = split_full_text(ft)
        s = score(body, vocab)
        flags = len(EMPTY_NOTE.findall(notes[doc_id].read_text(encoding="utf-8", errors="replace")))
        if args.ids or s < args.max_score or flags >= args.min_phrases:
            pdfs = pdf_paths(doc_id, head)
            rows.append({"id": doc_id, "note": notes[doc_id].stem, "old_score": s, "note_flags": flags,
                         "pages": head.get("pages", ""), "pdfs": "|".join(str(p) for p in pdfs),
                         "pdf_found": all(p.is_file() for p in pdfs) and bool(pdfs)})
    WORK.mkdir(parents=True, exist_ok=True)
    with open(TARGETS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
    missing = [r["id"] for r in rows if not r["pdf_found"]]
    pages = sum(int(r["pages"] or 0) for r in rows)
    print(f"{len(rows)} documents, {pages} pages -> {TARGETS}")
    if missing:
        print(f"PDF not found for {len(missing)}: {', '.join(missing[:20])}{' ...' if len(missing) > 20 else ''}")
    return 0


# ---------------------------------------------------------------------- run
def _setup_ocr():
    import pytesseract
    exe = pdf_ingest.find_tesseract()
    if exe:
        pytesseract.pytesseract.tesseract_cmd = exe
    return pytesseract


def read_page(path: Path, page_no: int, vocab: set) -> tuple:
    """(text, score, how) for one page: upright first, other rotations and a threshold only when needed."""
    from pdf2image import convert_from_path
    from PIL import ImageOps
    tess = _setup_ocr()
    img = convert_from_path(str(path), dpi=DPI, first_page=page_no, last_page=page_no, grayscale=True,
                            poppler_path=pdf_ingest.find_poppler()[1] or None)[0]
    t = tess.image_to_string(img)
    best = (t, score(t, vocab), "rot0", 0)
    if best[1] < TRY_MORE:
        # pick the angle from a quick half-resolution pass, then read that angle at full resolution
        small = img.resize((img.width // 2, img.height // 2))
        quick = {a: score(tess.image_to_string(small if a == 0 else small.rotate(a, expand=True)), vocab)
                 for a in (0, 180, 90, 270)}
        angle = max(quick, key=quick.get)
        if angle != 0 and quick[angle] > quick[0]:
            t = tess.image_to_string(img.rotate(angle, expand=True))
            s = score(t, vocab)
            if s > best[1]:
                best = (t, s, f"rot{angle}", angle)
    if best[1] < TRY_THRESH:
        im = img if best[3] == 0 else img.rotate(best[3], expand=True)
        im = ImageOps.autocontrast(im, cutoff=2).point(lambda x: 255 if x > 110 else 0)
        t = tess.image_to_string(im)
        s = score(t, vocab)
        if s > best[1]:
            best = (t, s, f"rot{best[3]}+threshold", best[3])
    return best[:3]


def reocr_document(row: dict, vocab: set) -> dict:
    t0 = time.monotonic()
    import pypdf
    doc_id = row["id"]
    head, body = split_full_text(FULL_TEXT_DIR / f"{doc_id}.md")
    old_pages = pages_of(body)
    out, how, kept_old, n = [], {}, 0, 0
    for fi, pdf in enumerate(Path(p) for p in row["pdfs"].split("|") if p):
        count = len(pypdf.PdfReader(str(pdf)).pages)
        if row["pdfs"].count("|"):
            out.append(f"\n=== File: {pdf.name} ===")
        for pg in range(1, count + 1):
            n += 1
            text, s, method = read_page(pdf, pg, vocab)
            old = old_pages.get(pg, "") if fi == 0 else ""
            if old and score(old, vocab) > s:
                text, method = old, "kept old"
                kept_old += 1
            how[method] = how.get(method, 0) + 1
            out.append(f"\n--- Page {pg} ---\n{text.strip()}\n")
    new_body = "".join(out)
    (WORK / "text").mkdir(parents=True, exist_ok=True)
    (WORK / "text" / f"{doc_id}.md").write_text(new_body, encoding="utf-8")
    return {"id": doc_id, "old_score": score(body, vocab), "new_score": score(new_body, vocab), "pages": n,
            "methods": how, "kept_old_pages": kept_old, "seconds": round(time.monotonic() - t0, 1), "when": _now()}


def _worker(row: dict) -> dict:
    try:
        return reocr_document(row, _worker.vocab)
    except Exception as e:  # one bad PDF must not stop the run
        return {"id": row["id"], "error": f"{type(e).__name__}: {e}", "when": _now()}


def _init_worker(vocab: set) -> None:
    _worker.vocab = vocab
    try:  # below-normal priority so the PC stays usable
        if os.name == "nt":
            import ctypes
            ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
        else:
            os.nice(10)
    except Exception:
        pass


def done_ids() -> set:
    if not RESULTS.is_file():
        return set()
    return {json.loads(l)["id"] for l in RESULTS.read_text(encoding="utf-8").splitlines()
            if l.strip() and "error" not in json.loads(l)}


def cmd_run(args) -> int:
    if not TARGETS.is_file():
        raise SystemExit("No targets yet: run `python -m utils.reocr plan` first.")
    vocab = load_vocab()
    with open(TARGETS, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("pdf_found") == "True"]
    done = done_ids()
    todo = sorted((r for r in rows if r["id"] not in done), key=lambda r: int(r["pages"] or 0))
    print(f"{len(todo)} documents to re-OCR ({len(done)} done), {sum(int(r['pages'] or 0) for r in todo)} pages; "
          f"{args.workers} workers. Stop any time; run again to continue.", flush=True)
    keep_awake = None
    if os.name == "nt":
        import ctypes
        keep_awake = ctypes.windll.kernel32.SetThreadExecutionState
        keep_awake(0x80000000 | 0x00000001)
    limit = time.monotonic() + (args.hours * 3600 if args.hours else 0) + (args.seconds or 0)
    timed = bool(args.hours or args.seconds)
    try:
        with ProcessPoolExecutor(args.workers, initializer=_init_worker, initargs=(vocab,)) as pool:
            pending = {}
            it = iter(todo)

            def submit() -> bool:
                if timed and time.monotonic() > limit:
                    return False
                r = next(it, None)
                if r is None:
                    return False
                pending[pool.submit(_worker, r)] = r
                return True

            for _ in range(args.workers):
                submit()
            while pending:
                fut = next(as_completed(pending))
                pending.pop(fut)
                res = fut.result()
                with open(RESULTS, "a", encoding="utf-8") as f:
                    f.write(json.dumps(res) + "\n")
                if "error" in res:
                    print(f"{res['id']}: FAILED {res['error']}", flush=True)
                else:
                    print(f"{res['id']}: {res['old_score']:.2f} -> {res['new_score']:.2f}, {res['pages']} pages, "
                          f"{res['seconds']} s {res['methods']}", flush=True)
                submit()
    finally:
        if keep_awake:
            keep_awake(0x80000000)
    return cmd_status(args)


# ------------------------------------------------------------ status, apply
def results() -> dict:
    out = {}
    if RESULTS.is_file():
        for l in RESULTS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                if r["id"] not in out or "error" not in r:
                    out[r["id"]] = r
    return out


def cmd_status(_args) -> int:
    total = 0
    if TARGETS.is_file():
        with open(TARGETS, newline="", encoding="utf-8") as f:
            total = sum(1 for r in csv.DictReader(f) if r.get("pdf_found") == "True")
    res = results()
    ok = [r for r in res.values() if "error" not in r]
    gains = [r["new_score"] - r["old_score"] for r in ok]
    print(f"done {len(ok)} of {total}; failed {len(res) - len(ok)}")
    if ok:
        print(f"better by 0.10 or more: {sum(g >= 0.10 for g in gains)}; reading 0.70 or better now: "
              f"{sum(r['new_score'] >= 0.70 for r in ok)}; still below 0.45: {sum(r['new_score'] < 0.45 for r in ok)}")
    return 0


def cmd_apply(args) -> int:
    applied = []
    for r in results().values():
        if "error" in r or r["new_score"] < r["old_score"] + args.min_gain:
            continue
        ft = FULL_TEXT_DIR / f"{r['id']}.md"
        new = WORK / "text" / f"{r['id']}.md"
        if not (ft.is_file() and new.is_file()):
            continue
        applied.append(r)
        if args.dry_run:
            continue
        (WORK / "old").mkdir(parents=True, exist_ok=True)
        old_copy = WORK / "old" / ft.name
        if not old_copy.is_file():
            old_copy.write_bytes(ft.read_bytes())
        head, _ = split_full_text(ft)
        head.pop("characters", None)
        head.pop("private", None)
        head["previous_extraction"] = head.get("text_extraction", "")
        head["reocr"] = r["when"][:10]
        text = new.read_text(encoding="utf-8")
        from utils import public_domain
        public_domain.save_full_text(r["id"], {"text": text, "pages": r["pages"],
                                               "method": f"reocr ({DPI} dpi, rotation)"}, head)
    print(f"{'would replace' if args.dry_run else 'replaced'} {len(applied)} full-text files (gain >= {args.min_gain})")
    if applied and not args.dry_run:
        with open(WORK / "improved.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id", "old_score", "new_score", "pages"])
            for r in sorted(applied, key=lambda r: r["id"]):
                w.writerow([r["id"], r["old_score"], r["new_score"], r["pages"]])
        print(f"List for rebuilding notes: {WORK / 'improved.csv'}")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["plan", "run", "status", "apply"])
    ap.add_argument("--max-score", type=float, default=0.45)
    ap.add_argument("--min-phrases", type=int, default=2)
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) // 2))
    ap.add_argument("--hours", type=float, default=0)
    ap.add_argument("--seconds", type=float, default=0)
    ap.add_argument("--min-gain", type=float, default=0.10)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "run": cmd_run, "status": cmd_status, "apply": cmd_apply}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
