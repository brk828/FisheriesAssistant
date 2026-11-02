"""Uploads public-domain PDFs to the website's PDF folder (https://www.marsheducation.org/library/textpdf/) by FTP.

    python -m utils.site_ftp test                 connect, find the PDF folder, report; uploads nothing
    python -m utils.site_ftp pending              upload registered public-domain IDs not yet uploaded (retry after a failure)
    python -m utils.site_ftp upload FILE...       upload these files under their own names
    python -m utils.site_ftp folder DIR [--dry-run]
                                                  upload every PDF in DIR not already on the server (e.g. the Marsh
                                                  Library's MarshLibrary_PublicDomain folder)

Settings in fisheries_agent/.env: MARSH_FTP_PASS (required; never printed or logged), MARSH_FTP_USER (default native43),
MARSH_FTP_HOST (default ftp.marsheducation.org), MARSH_FTP_PORT (default 21), MARSH_FTP_REMOTE_DIR (the folder that serves /library/textpdf/;
found automatically when unset, and `test` tells you which one it found), MARSH_FTP_TLS (default "on": encrypted FTPS
with a verified certificate; "noverify" keeps encryption but skips the certificate check, for a host whose certificate
names another server; "off" allows plain FTP, which sends the password unencrypted; use only if the host offers nothing else).
Rules: a file already on the server with the same size is skipped; one with a different size is never overwritten
(it is reported). Each upload goes to <name>.part and is renamed when complete, then its size is checked.
Every upload is logged to runs/ftp_uploads.jsonl (no password).
"""
import ftplib
import json
import os
import ssl
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from utils import llm_provider, public_domain

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_DIR / "runs" / "ftp_uploads.jsonl"
SITE_PDF_URL = "https://www.marsheducation.org/library/textpdf/"
CANDIDATE_DIRS = ("library/textpdf", "public_html/library/textpdf", "www/library/textpdf", "htdocs/library/textpdf",
                  "httpdocs/library/textpdf", "html/library/textpdf", "textpdf", ".")


class _TLS(ftplib.FTP_TLS):
    """FTPS that reuses the control connection's TLS session on data connections (many servers require it)."""

    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(conn, server_hostname=self.host, session=self.sock.session)
        return conn, size


def _settings() -> dict:
    llm_provider._load_env()
    pw = (os.getenv("MARSH_FTP_PASS") or "").strip()
    if not pw:
        raise SystemExit(f"MARSH_FTP_PASS is not set in {llm_provider.ENV_PATH}.")
    return {"host": os.getenv("MARSH_FTP_HOST") or "ftp.marsheducation.org", "port": int(os.getenv("MARSH_FTP_PORT") or 21), "user": os.getenv("MARSH_FTP_USER") or "native43",
            "pw": pw, "dir": (os.getenv("MARSH_FTP_REMOTE_DIR") or "").strip(), "tls": (os.getenv("MARSH_FTP_TLS") or "on").strip().lower()}


def _scrub(text, s: dict) -> str:
    return str(text).replace(s["pw"], "[password]")


def connect():
    """Logged-in connection in binary, passive mode. Raises SystemExit with a plain explanation on failure."""
    s = _settings()
    try:
        if s["tls"] == "off":
            ftp = ftplib.FTP(timeout=60)
            ftp.connect(s["host"], s["port"])
            ftp.login(s["user"], s["pw"])
        else:
            ctx = ssl.create_default_context()
            if s["tls"] == "noverify":
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
            ftp = _TLS(context=ctx, timeout=60)
            ftp.connect(s["host"], s["port"])
            ftp.auth()
            ftp.login(s["user"], s["pw"])
            ftp.prot_p()
    except ssl.SSLCertVerificationError as e:
        raise SystemExit(f"The FTP server's certificate did not verify ({e.verify_message}). If the host is right, set "
                         "MARSH_FTP_TLS=noverify in .env (still encrypted).")
    except ftplib.error_perm as e:
        msg = _scrub(e, s)
        if msg[:3] in ("500", "502", "504", "534") and s["tls"] != "off":
            raise SystemExit(f"The server does not accept encrypted FTP ({msg}). Plain FTP would send the password "
                             "unencrypted; set MARSH_FTP_TLS=off in .env only if you accept that.")
        raise SystemExit(f"FTP login refused: {msg}")
    except (OSError, ftplib.Error) as e:
        raise SystemExit(f"Could not connect to {s['host']}: {_scrub(e, s)}")
    ftp.set_pasv(True)
    ftp.voidcmd("TYPE I")
    return ftp, s


def _pdf_names(ftp) -> set:
    try:
        return {n.rsplit("/", 1)[-1] for n in ftp.nlst() if n.lower().endswith(".pdf")}
    except ftplib.error_perm:  # "550 No files found" on an empty folder
        return set()


def find_dir(ftp, s: dict) -> str:
    """The configured folder, else the candidate that holds the most PDFs. Never creates a folder."""
    home = ftp.pwd()
    tried = [s["dir"]] if s["dir"] else list(CANDIDATE_DIRS)
    best, best_n = "", -1
    for d in tried:
        try:
            ftp.cwd(home)
            ftp.cwd(d)
        except ftplib.error_perm:
            continue
        n = len(_pdf_names(ftp))
        if n > best_n:
            best, best_n = ftp.pwd(), n
    ftp.cwd(home)
    if not best or (not s["dir"] and best_n <= 0):
        raise SystemExit("Could not find the website's PDF folder on the FTP server (tried: " + ", ".join(tried) +
                         "). Run `python -m utils.site_ftp test` and set MARSH_FTP_REMOTE_DIR in .env.")
    ftp.cwd(best)
    return best


def _log(rec: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"), **rec}) + "\n")


def _remote_size(ftp, name: str):
    """Size in bytes, or None if the server has no such file. Listing switches the connection to ASCII mode, where
    SIZE is refused, so binary mode is set first."""
    try:
        ftp.voidcmd("TYPE I")
        return ftp.size(name)
    except ftplib.error_perm:
        return None


def upload_one(ftp, path: Path, name: str = "", existing: set = None) -> str:
    """'uploaded', 'skipped' (same size already there) or 'conflict' (different file of that name; left alone)."""
    name = name or path.name
    local = path.stat().st_size
    if existing is None:
        existing = _pdf_names(ftp)
    remote = _remote_size(ftp, name)
    if remote is not None or name in existing:  # a listed name whose size cannot be read is never overwritten either
        result = "skipped" if remote == local else "conflict"
        _log({"file": name, "result": result, "bytes": local, "remote_bytes": remote})
        return result
    part = f"{name}.part"
    with open(path, "rb") as f:
        ftp.storbinary(f"STOR {part}", f, blocksize=64 * 1024)
    try:
        ftp.rename(part, name)
    except ftplib.error_perm:
        ftp.delete(part)
        raise
    remote = _remote_size(ftp, name)
    if remote is not None and remote != local:
        _log({"file": name, "result": "size_mismatch", "bytes": local, "remote_bytes": remote})
        raise RuntimeError(f"{name}: uploaded {local:,} bytes but the server reports {remote:,}")
    _log({"file": name, "result": "uploaded", "bytes": local})
    return "uploaded"


def web_ok(name: str) -> bool:
    try:
        req = urllib.request.Request(SITE_PDF_URL + name, method="HEAD", headers={"User-Agent": "FisheriesAssistant upload check"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False


def upload_files(paths: list, quiet: bool = False) -> dict:
    """Uploads the files in one session; returns {name: result or 'failed: ...'}."""
    out = {}
    ftp, s = connect()
    try:
        where = find_dir(ftp, s)
        if not quiet:
            print(f"   FTP: {s['host']}{where if where.startswith('/') else '/' + where} ({len(paths)} file(s))")
        existing = _pdf_names(ftp)
        for p in paths:
            p = Path(p)
            try:
                out[p.name] = upload_one(ftp, p, existing=existing)
            except Exception as e:
                out[p.name] = f"failed: {_scrub(e, s)}"
                _log({"file": p.name, "result": "failed", "error": _scrub(e, s)[:300]})
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()
    return out


def publish_id(code: str) -> str:
    """Uploads the local <ID>.pdf for a registered ID and records it; returns the result (never raises)."""
    p = public_domain.public_pdf_dir() / f"{code}.pdf"
    if not p.is_file():
        return f"failed: {p} not found"
    try:
        result = upload_files([p], quiet=True).get(p.name, "failed")
    except SystemExit as e:  # connection/configuration problems: the note is unaffected, retry with `pending`
        result = f"failed: {e}"
    if result in ("uploaded", "skipped"):
        public_domain.update_registry(code, uploaded=datetime.now(timezone.utc).isoformat(timespec="seconds")[:10])
    return result


# ------------------------------------------------------------------------ CLI
def cmd_test() -> int:
    ftp, s = connect()
    try:
        print(f"Logged in to {s['host']} as {s['user']} ({'plain FTP' if s['tls'] == 'off' else 'FTPS, encrypted'}). Home folder: {ftp.pwd()}")
        where = find_dir(ftp, s)
        names = sorted(_pdf_names(ftp))
        print(f"PDF folder: {where} ({len(names):,} PDFs, e.g. {', '.join(names[:3])})")
        if names:
            print(f"Web check: {SITE_PDF_URL}{names[0]} -> {'OK' if web_ok(names[0]) else 'NOT reachable (is this the right folder?)'}")
        if not s["dir"]:
            print(f"Add this line to .env to fix the folder: MARSH_FTP_REMOTE_DIR={where}")
    finally:
        ftp.quit()
    return 0


def cmd_pending() -> int:
    rows = [r for r in public_domain.read_registry() if not r["uploaded"]]
    if not rows:
        print("Every registered public-domain PDF has been uploaded.")
        return 0
    bad = 0
    for r in rows:
        res = publish_id(r["code"])
        print(f"{r['code']}: {res}")
        bad += not res in ("uploaded", "skipped")
    return 1 if bad else 0


def cmd_files(paths: list, dry: bool = False) -> int:
    paths = [Path(p) for p in paths if Path(p).is_file() and Path(p).suffix.lower() == ".pdf"]
    if not paths:
        print("No PDFs given.")
        return 1
    if dry:
        ftp, s = connect()
        try:
            find_dir(ftp, s)
            have = _pdf_names(ftp)
        finally:
            ftp.quit()
        todo = [p for p in paths if p.name not in have]
        print(f"{len(paths):,} PDFs; {len(paths) - len(todo):,} already on the server by name; {len(todo):,} would be uploaded "
              f"({sum(p.stat().st_size for p in todo) / 1e6:,.0f} MB).")
        return 0
    res = upload_files(paths)
    counts = {}
    for name, r in res.items():
        key = r.split(":")[0]
        counts[key] = counts.get(key, 0) + 1
        if key not in ("uploaded", "skipped"):
            print(f"  {name}: {r}")
    print(", ".join(f"{v:,} {k}" for k, v in sorted(counts.items())) + f". Log: {LOG_PATH}")
    return 0 if set(counts) <= {"uploaded", "skipped"} else 1


def main(argv: list = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] not in ("test", "pending", "upload", "folder"):
        print(__doc__)
        return 1
    if argv[0] == "test":
        return cmd_test()
    if argv[0] == "pending":
        return cmd_pending()
    if argv[0] == "upload":
        return cmd_files(argv[1:])
    rest = [a for a in argv[1:] if a != "--dry-run"]
    if len(rest) != 1 or not Path(rest[0]).is_dir():
        print("Usage: python -m utils.site_ftp folder DIR [--dry-run]")
        return 1
    return cmd_files(sorted(Path(rest[0]).glob("*.pdf")), dry="--dry-run" in argv)


if __name__ == "__main__":
    sys.exit(main())
