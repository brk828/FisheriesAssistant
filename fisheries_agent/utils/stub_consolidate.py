"""One-time migration of the per-concept stub files in 02_Brain/ into Stubs_A.md ... Stubs_Z.md and Stubs_MISC.md.

  python -m utils.stub_consolidate                    dry run: counts per letter and anything unusual; writes nothing
  python -m utils.stub_consolidate --apply            writes the letter files, then re-reads them and checks that every
                                                      stub and every "Mentioned In" entry made it
  python -m utils.stub_consolidate --apply --delete   also deletes the old per-concept files, but only if the check passed

Safe to repeat: existing letter files are merged with, never overwritten. Only .md files directly in 02_Brain/ are
touched (other files, for example a stray .html, are left alone and reported). Run `git pull` first so the stubs from
every machine are present; the old files stay recoverable through git history.
"""
import argparse
import sys
from collections import Counter

from utils.stub_store import LETTERS, StubStore, bucket, parse_legacy, parse_letter_file, render_letter_file, write_atomic


def _load_legacy(store: StubStore):
    stubs, notes = [], Counter()
    for path in store.legacy_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        stub = parse_legacy(text, path.stem)
        stubs.append((path, stub))
        h1 = [l for l in text.replace("\r\n", "\n").split("\n") if l.startswith("# ")]
        if len(h1) != 1:
            notes["files without exactly one '# ' title (extra headings turned into bold text)"] += 1
        elif h1[0][2:].strip() != path.stem:
            notes["files whose '# ' title differs from the file name (file name kept)"] += 1
        if not stub.mentions:
            notes["stubs with no Mentioned In entries"] += 1
    return stubs, notes


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the letter files")
    ap.add_argument("--delete", action="store_true", help="after a successful check, delete the old per-concept files (needs --apply)")
    args = ap.parse_args(argv)
    if args.delete and not args.apply:
        print("--delete needs --apply.")
        return 2

    store = StubStore()
    legacy, notes = _load_legacy(store)
    if not legacy:
        print("No per-concept stub files found; nothing to do.")
        return 0
    other = sorted(p.name for p in store.dir.iterdir() if p.is_file() and p.suffix.lower() != ".md")
    print(f"Found {len(legacy)} per-concept stub files in {store.dir}.")
    counts = Counter(bucket(s.name) for _, s in legacy)
    print("Per letter: " + ", ".join(f"{l}={counts[l]}" for l in LETTERS if counts[l]))
    for note, n in notes.items():
        print(f"Note: {n} {note}")
    if other:
        print(f"Left alone (not .md): {', '.join(other)}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to write the consolidated files.")
        return 0

    merged = {l: dict(store._load(l)) for l in LETTERS}
    for _, stub in legacy:
        slot = merged[bucket(stub.name)]
        key = stub.name.lower()
        if key in slot:
            slot[key].merge(stub)
        else:
            slot[key] = stub
    for letter in LETTERS:
        if merged[letter]:
            write_atomic(store.letter_path(letter), render_letter_file(letter, merged[letter]))
    print(f"Wrote {sum(1 for l in LETTERS if merged[l])} letter files.")

    problems = 0
    for letter in LETTERS:
        path = store.letter_path(letter)
        back = parse_letter_file(path.read_text(encoding="utf-8")) if path.is_file() else {}
        for _, stub in legacy:
            if bucket(stub.name) != letter:
                continue
            got = back.get(stub.name.lower())
            if got is None:
                print(f"MISSING: {stub.name}")
                problems += 1
            elif not set(stub.mentions) <= set(got.mentions) or (stub.summary and not got.summary):
                print(f"INCOMPLETE: {stub.name}")
                problems += 1
    total = sum(len(parse_letter_file(store.letter_path(l).read_text(encoding='utf-8'))) for l in LETTERS if store.letter_path(l).is_file())
    print(f"Check: {total} stubs in the letter files, {problems} problems.")
    if problems:
        print("Originals kept.")
        return 1
    if args.delete:
        for path, _ in legacy:
            path.unlink()
        print(f"Deleted {len(legacy)} old stub files.")
    else:
        print("Originals kept. Re-run with --apply --delete to remove them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
