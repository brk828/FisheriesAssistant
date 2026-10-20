"""Small, consent-gated web lookups for skill building and analysis planning.

Only two lookups, both against public metadata services (no page scraping, no keys, nothing sent but the query):
  - check_r_package(name): does it exist on CRAN, and its version, title and URL (crandb.r-pkg.org)
  - search_methods_papers(query): methods papers by title/year/DOI (api.crossref.org)

Callers must record results as web-derived (never mix them with brain citations) and must ask the user first.
"""
import json
import re
import urllib.parse
import urllib.request

TIMEOUT = 20
PKG_RE = re.compile(r"^[A-Za-z][A-Za-z0-9.]{1,63}$")
USER_AGENT = "FisheriesAssistant/1.0 (research tool)"


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode("utf-8", errors="replace"))


def check_r_package(name: str) -> dict:
    """{'exists': bool, ...}; {'exists': None, 'error': ...} when CRAN could not be reached."""
    if not PKG_RE.match(name or ""):
        return {"exists": False, "error": "not a valid R package name"}
    try:
        d = _get_json(f"https://crandb.r-pkg.org/{urllib.parse.quote(name)}")
    except urllib.error.HTTPError as e:
        return {"exists": False} if e.code == 404 else {"exists": None, "error": f"HTTP {e.code}"}
    except (OSError, ValueError) as e:
        return {"exists": None, "error": str(e)}
    return {"exists": True, "package": d.get("Package", name), "version": d.get("Version"), "title": d.get("Title"),
            "url": f"https://cran.r-project.org/package={name}"}


def search_methods_papers(query: str, rows: int = 5) -> list:
    """[{'title','year','doi','journal'}] from Crossref; [] on failure."""
    q = urllib.parse.urlencode({"query.bibliographic": query, "rows": max(1, min(rows, 10)),
                                "select": "title,issued,DOI,container-title"})
    try:
        items = _get_json(f"https://api.crossref.org/works?{q}")["message"]["items"]
    except (OSError, ValueError, KeyError):
        return []
    out = []
    for it in items:
        parts = (it.get("issued") or {}).get("date-parts") or [[None]]
        out.append({"title": (it.get("title") or [""])[0], "year": parts[0][0], "doi": it.get("DOI"),
                    "journal": (it.get("container-title") or [""])[0]})
    return out
