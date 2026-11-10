"""Copy the public-domain Minckley PDFs into their own folder, as for the Marsh Library.

    python -m utils.minckley_public plan                    counts and size; PDFs in the folder that are no longer
                                                             public domain are listed (never deleted)
    python -m utils.minckley_public copy [--seconds S]      copy what is missing (resumable; S stops it after S seconds)

Source: MINCKLEY_PDF_DIR (default C:/Obsidian/Fish_Science_Brain/MinckleyLibrary). Target: MINCKLEY_PUBLIC_DIR
(default C:/Obsidian/Fish_Science_Brain/MinckleyLibrary_PublicDomain). A MID is public domain when its permission in
brain_meta/minckley_library.csv is "public domain". Each PDF is copied as <MID>.pdf (a MID with more than one main file
gets <MID>.pdf, <MID>_2.pdf ...), through a .tmp file, and listed in ftp_manifest.csv (mid, pdf, original_file, title,
year, added) in the target folder. The library folder is never changed. These PDFs are already on the website
(textpdf/<MID>.pdf); the folder is a local, consistently named copy.
"""
import argparse
import csv
import os
import shutil
import sys
import time
from datetime import date
from pathlib import Path

from utils import llm_provider, minckley_lists

DEFAULT_TARGET = "C:/Obsidian/Fish_Science_Brain/MinckleyLibrary_PublicDomain"
MANIFEST = "ftp_manifest.csv"
FIELDS = ["mid", "pdf", "original_file", "title", "year", "added"]


def target_dir() -> Path:
    llm_provider._load_env()
    return Path(os.getenv("MINCKLEY_PUBLIC_DIR") or DEFAULT_TARGET)


def references() -> dict:
    out = {}
    with open(minckley_lists.LIBRARY_CSV, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            out.setdefault((r.get("MID") or "").strip(), r)
    return out


def work() -> tuple:
    """([(mid, source path, target name)], public-domain MIDs without a PDF, files in the target no longer public)."""
    src, dst = minckley_lists.source_dir(), target_dir()
    perm = minckley_lists.permissions()
    files = minckley_lists.pdfs_by_mid(src)
    public = sorted((m for m, p in perm.items() if p == "public domain"), key=int)
    todo, missing = [], []
    for mid in public:
        names = minckley_lists.pick_files(mid, files.get(mid, []))
        if not names:
            missing.append(mid)
            continue
        for i, n in enumerate(names):
            todo.append((mid, src / n, f"{mid}.pdf" if i == 0 else f"{mid}_{i + 1}.pdf"))
    wanted = {t[2] for t in todo}
    stale = sorted(p.name for p in dst.glob("*.pdf") if p.name not in wanted) if dst.is_dir() else []
    return todo, missing, stale


def _done(path: Path, src: Path) -> bool:
    return path.is_file() and path.stat().st_size == src.stat().st_size


def cmd_plan(_args) -> int:
    todo, missing, stale = work()
    dst = target_dir()
    left = [t for t in todo if not _done(dst / t[2], t[1])]
    print(f"{len({t[0] for t in todo})} public-domain MIDs with a PDF ({len(todo)} files); {len(left)} files left to copy, "
          f"{sum(t[1].stat().st_size for t in left) / 1e9:.1f} GB -> {dst}")
    print(f"{len(missing)} public-domain MIDs have no PDF in {minckley_lists.source_dir()}.")
    if stale:
        print(f"{len(stale)} PDFs in the folder are no longer public domain (not deleted): {', '.join(stale[:20])}")
    return 0


def cmd_copy(args) -> int:
    todo, _, stale = work()
    dst = target_dir()
    dst.mkdir(parents=True, exist_ok=True)
    refs = references()
    man = dst / MANIFEST
    listed = set()
    if man.is_file():
        with open(man, newline="", encoding="utf-8-sig") as f:
            listed = {r["pdf"] for r in csv.DictReader(f)}
    stop = time.monotonic() + args.seconds if args.seconds else None
    copied = 0
    with open(man, "a", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not listed and f.tell() == 0:
            w.writeheader()
        for mid, src, name in todo:
            if stop and time.monotonic() > stop:
                print("Time limit reached; run again to continue.")
                break
            out = dst / name
            if not _done(out, src):
                tmp = out.with_suffix(".tmp")
                shutil.copyfile(src, tmp)
                os.replace(tmp, out)
                copied += 1
            if name not in listed:
                r = refs.get(mid, {})
                w.writerow({"mid": mid, "pdf": name, "original_file": src.name, "title": r.get("title", ""),
                            "year": r.get("year", ""), "added": date.today().isoformat()})
                listed.add(name)
                f.flush()
    print(f"Copied {copied} files; {len(listed)} listed in {man.name}.")
    if stale:
        print(f"{len(stale)} PDFs in the folder are no longer public domain (not deleted): {', '.join(stale[:20])}")
    return 0


def main(argv: list = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", nargs="?", default="plan", choices=["plan", "copy"])
    ap.add_argument("--seconds", type=float, default=0)
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "copy": cmd_copy}[args.action](args)


if __name__ == "__main__":
    sys.exit(main())
