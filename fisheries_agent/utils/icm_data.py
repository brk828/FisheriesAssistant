"""Manifest of large and linked files for an ICM workspace (data/manifest.yaml).

Linked files stay where they are; the manifest records path, size, mtime and sha256 so changes are noticed.
At each stage run call check(): it compares size and modification time and only re-hashes a file when one of
them differs. verify_all() re-hashes everything on request.

    python -m utils.icm_data <workspace> [--full] [--accept]
"""
import hashlib
import sys
from pathlib import Path

import yaml

HASH_LIMIT_MB = 500          # larger files are recorded without a hash and checked by size and mtime only
_CHUNK = 1024 * 1024


def manifest_path(root) -> Path:
    return Path(root) / "data" / "manifest.yaml"


def load(root) -> list:
    p = manifest_path(root)
    if not p.is_file():
        return []
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("files") or []


def save(root, files: list) -> None:
    p = manifest_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump({"files": files}, sort_keys=False, allow_unicode=True), encoding="utf-8")


def sha256(path, limit_mb: float = None):
    """Chunked sha256, or None when the file is above the limit."""
    path = Path(path)
    if limit_mb is not None and path.stat().st_size > limit_mb * 1024 * 1024:
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(_CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def make_entry(path, kind: str, stored_as: str = None, note: str = "", hash_limit_mb: float = HASH_LIMIT_MB) -> dict:
    """Entry for a file. `stored_as` is a path relative to the workspace for copied files; otherwise `path` is absolute."""
    p = Path(path)
    st = p.stat()
    return {
        "path": stored_as or str(p.resolve()),
        "kind": kind,
        "size": st.st_size,
        "mtime_ns": st.st_mtime_ns,
        "sha256": sha256(p, hash_limit_mb),
        "note": note,
    }


def resolve(root, entry: dict) -> Path:
    p = Path(entry["path"])
    return p if p.is_absolute() else Path(root) / p


def _inspect(root, entry: dict, full: bool) -> dict:
    """Status of one entry: ok, touched (mtime differs, content same), changed, or missing."""
    p = resolve(root, entry)
    if not p.is_file():
        return {"path": entry["path"], "status": "missing"}
    st = p.stat()
    same_meta = st.st_size == entry.get("size") and st.st_mtime_ns == entry.get("mtime_ns")
    if same_meta and not full:
        return {"path": entry["path"], "status": "ok"}
    if st.st_size != entry.get("size"):
        return {"path": entry["path"], "status": "changed"}
    if not entry.get("sha256"):
        return {"path": entry["path"], "status": "ok" if same_meta else "changed",
                **({} if same_meta else {"detail": "modified; no stored hash to compare"})}
    same = sha256(p) == entry["sha256"]
    if same:
        return {"path": entry["path"], "status": "ok" if same_meta else "touched"}
    return {"path": entry["path"], "status": "changed"}


def check(root, full: bool = False) -> list:
    """Problems only: entries that are missing or changed (plus 'touched' notes). Empty list means all good."""
    return [r for r in (_inspect(root, e, full) for e in load(root)) if r["status"] != "ok"]


def verify_all(root) -> list:
    return check(root, full=True)


def warnings(root, full: bool = False) -> list:
    """Human-readable warnings for missing or changed files (touched-but-identical files are not warned about)."""
    out = []
    for r in check(root, full):
        if r["status"] == "missing":
            out.append(f"Linked file is missing: {r['path']}")
        elif r["status"] == "changed":
            out.append(f"Linked file changed since it was recorded: {r['path']}" + (f" ({r['detail']})" if r.get("detail") else ""))
    return out


def accept(root, paths=None) -> int:
    """Records the current state of changed files (all of them, or only `paths`) after the user has reviewed them."""
    files = load(root)
    n = 0
    for e in files:
        if paths is not None and e["path"] not in paths:
            continue
        p = resolve(root, e)
        if p.is_file() and _inspect(root, e, True)["status"] in ("changed", "touched"):
            e.update(make_entry(p, e["kind"], e["path"] if not Path(e["path"]).is_absolute() else None, e.get("note", "")))
            n += 1
    if n:
        save(root, files)
    return n


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    root = Path(args[0])
    if "--accept" in argv:
        print(f"Accepted the current state of {accept(root)} file(s).")
        return 0
    problems = warnings(root, full="--full" in argv)
    print("\n".join(problems) if problems else f"All {len(load(root))} linked file(s) match the manifest.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
