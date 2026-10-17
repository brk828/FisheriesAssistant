"""Reviews and applies upstream updates to the vendored ICM core (icm_core/).

Run from fisheries_agent:
    python -m utils.icm_update                 # show what differs from upstream main
    python -m utils.icm_update --ref <sha>     # compare against a specific commit/tag/branch
    python -m utils.icm_update --apply         # copy the upstream files in and re-pin the commit

Only the files listed in icm_core/UPSTREAM.json are compared. Local fisheries templates live in icm_templates/
and are never touched. Review the diff, run the validator tests, then commit.
"""
import argparse
import difflib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CORE_DIR = Path(__file__).resolve().parent.parent / "icm_core"
UPSTREAM_PATH = CORE_DIR / "UPSTREAM.json"


def _files(root: Path, rel: str) -> dict:
    """Maps relative file names to paths for a file or a folder (empty if missing)."""
    p = root / rel
    if p.is_file():
        return {"": p}
    if p.is_dir():
        return {f.relative_to(p).as_posix(): f for f in sorted(p.rglob("*")) if f.is_file() and f.name != ".gitkeep"}
    return {}


def _read(p) -> list:
    return p.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True) if p else []


def compare(upstream_root: Path, manifest: dict) -> list:
    """Returns (status, local_rel, upstream_rel, local_path, upstream_path) for every differing file."""
    out = []
    for local_rel, up_rel in manifest["files"].items():
        mine, theirs = _files(CORE_DIR, local_rel), _files(upstream_root, up_rel)
        for name in sorted(set(mine) | set(theirs)):
            a, b = mine.get(name), theirs.get(name)
            if a and b and a.read_bytes() == b.read_bytes():
                continue
            status = "changed" if a and b else ("added upstream" if b else "removed upstream")
            suffix = f"/{name}" if name else ""
            out.append((status, local_rel + suffix, up_rel + suffix, a, b))
    return out


def _clone(ref: str, dest: Path) -> str:
    repo = json.loads(UPSTREAM_PATH.read_text(encoding="utf-8"))["repo"]
    subprocess.run(["git", "clone", "-q", repo, str(dest)], check=True)
    subprocess.run(["git", "checkout", "-q", ref], cwd=dest, check=True)
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=dest, check=True, capture_output=True, text=True).stdout.strip()


def apply(changes: list, upstream_root: Path, manifest: dict, sha: str) -> None:
    for status, local, up, a, b in changes:
        target = CORE_DIR / local
        if b is None:
            target.unlink(missing_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(b, target)
    manifest["commit"] = sha
    UPSTREAM_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ref", default="origin/HEAD", help="upstream commit, tag or branch (default: upstream default branch)")
    ap.add_argument("--apply", action="store_true", help="copy upstream files into icm_core/ and update the pinned commit")
    args = ap.parse_args(argv)

    manifest = json.loads(UPSTREAM_PATH.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as tmp:
        up = Path(tmp) / "up"
        try:
            sha = _clone(args.ref, up)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Could not fetch upstream: {e}")
            return 1
        changes = compare(up, manifest)
        print(f"Pinned: {manifest['commit'][:10]}   Upstream ({args.ref}): {sha[:10]}")
        if not changes:
            print("Vendored files match upstream.")
            return 0
        for status, local, _, a, b in changes:
            print(f"\n=== {local} ({status}) ===")
            sys.stdout.writelines(difflib.unified_diff(_read(a), _read(b), "pinned", "upstream", n=2))
        if args.apply:
            apply(changes, up, manifest, sha)
            print(f"\nApplied {len(changes)} file(s); pinned commit is now {sha[:10]}. Review, test and commit.")
        else:
            print(f"\n{len(changes)} file(s) differ. Rerun with --apply to accept.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
