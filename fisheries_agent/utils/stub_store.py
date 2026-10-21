"""Concept stubs, consolidated into one Markdown file per initial letter.

Layout of 00_Fisheries_Brain/02_Brain/: Stubs_A.md ... Stubs_Z.md plus Stubs_MISC.md (digits, symbols, non-Latin).
Each file holds one `## Concept` block per stub with `### Summary`, `### Context` and `### Mentioned In`
subsections; blocks are sorted by name so git diffs stay small. In Obsidian a concept is reached with
[[Stubs_A#Concept Name]]. The sources still link with plain [[Concept Name]] (that is the key the search index uses).

Before the one-time migration (python -m utils.stub_consolidate) the folder still holds one file per concept.
Reading works in both layouts; writing refuses until the migration has been run, so the two never mix.
"""
import os
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STUBS_DIR = BASE_DIR / "00_Fisheries_Brain" / "02_Brain"

LETTERS = [chr(c) for c in range(ord("A"), ord("Z") + 1)] + ["MISC"]
PREFIX = "Stubs_"
SECTIONS = ("Summary", "Context", "Mentioned In")
LETTER_FILES = {f"{PREFIX}{l}.md" for l in LETTERS}


class StubStoreError(RuntimeError):
    pass


def bucket(name: str) -> str:
    for ch in unicodedata.normalize("NFKD", name):
        if ch.isalnum():
            up = ch.upper()
            return up if "A" <= up <= "Z" else "MISC"
    return "MISC"


class Stub:
    __slots__ = ("name", "meta", "summary", "context", "mentions")

    def __init__(self, name: str, meta: str = "", summary: str = "", context: str = "", mentions=None):
        self.name = name
        self.meta = meta
        self.summary = summary
        self.context = context
        self.mentions = list(mentions or [])

    def merge(self, other: "Stub") -> None:
        """Folds another copy of the same concept into this one; nothing is lost, nothing is duplicated."""
        self.meta = self.meta or other.meta
        self.summary = self.summary or other.summary
        have = set(self.context.splitlines())
        extra = [l for l in other.context.splitlines() if l.strip() and l not in have]
        if extra and not self.context:
            self.context = other.context
        elif extra:
            self.context = f"{self.context}\n\n" + "\n".join(extra)
        self.mentions += [m for m in other.mentions if m not in self.mentions]

    def render(self) -> str:
        out = [f"## {self.name}"]
        if self.meta:
            out.append(self.meta)
        if self.summary:
            out += ["", "### Summary", self.summary]
        if self.context:
            out += ["", "### Context", self.context]
        out += ["", "### Mentioned In", *self.mentions]
        return "\n".join(out) + "\n"

    def legacy_text(self) -> str:
        """The old one-file-per-concept body (H1 title, `##` sections); what the search index parses."""
        out = [f"# {self.name}", ""]
        for title, value in (("Summary", self.summary), ("Context", self.context)):
            if value:
                out += [f"## {title}", value, ""]
        out += ["## Mentioned In", *self.mentions]
        return "\n".join(out) + "\n"


def _defuse(line: str) -> str:
    """A heading inside a stub would split it into a new concept, so it becomes bold text."""
    if re.match(r"^#{1,6}\s", line):
        return "**" + line.lstrip("#").strip() + "**"
    return line


def _finish(lines: list) -> str:
    return "\n".join(lines).strip("\n").strip()


def parse_letter_file(text: str) -> dict:
    """lowercase name -> Stub. Duplicate blocks (for example after a git merge) are merged."""
    stubs, cur, sec = {}, None, None
    buf = {"Summary": [], "Context": [], "Mentioned In": []}

    def close():
        if cur is None:
            return
        new = Stub(cur[0], cur[1], _finish(buf["Summary"]), _finish(buf["Context"]),
                   list(dict.fromkeys(l.strip() for l in buf["Mentioned In"] if l.strip())))
        key = new.name.lower()
        if key in stubs:
            stubs[key].merge(new)
        else:
            stubs[key] = new

    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            close()
            cur, sec = (line[3:].strip(), ""), None
            buf = {k: [] for k in SECTIONS}
        elif cur is None:
            continue
        elif line.startswith("### ") and line[4:].strip() in SECTIONS:
            sec = line[4:].strip()
        elif sec is None:
            if line.startswith("<!-- fm:"):
                cur = (cur[0], line.strip())
        else:
            buf[sec].append(line)
    close()
    return stubs


def parse_legacy(text: str, stem: str) -> Stub:
    """One old-style stub file. The file name is the concept name (that is what [[links]] resolve to)."""
    text = text.replace("\r\n", "\n")
    meta = ""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if m:
        pairs = [f"{k}: {v.strip()}" for k, v in re.findall(r"^([\w\-]+):\s*(.*)$", m.group(1), re.M) if k != "type"]
        meta = f"<!-- fm: {'; '.join(pairs)} -->" if pairs else ""
        text = text[m.end():]
    buf = {"Summary": [], "Context": [], "Mentioned In": []}
    sec, seen_title = "Context", False
    for line in text.split("\n"):
        if line.startswith("# ") and not seen_title:
            seen_title = True
            continue
        h = re.match(r"^## (.+?)\s*$", line)
        if h:
            sec = h.group(1) if h.group(1) in SECTIONS else "Context"
            if sec == "Context" and h.group(1) != "Context":
                buf["Context"].append(f"**{h.group(1)}**")
            continue
        buf[sec].append(_defuse(line))
    return Stub(stem, meta, _finish(buf["Summary"]), _finish(buf["Context"]),
                list(dict.fromkeys(l.strip() for l in buf["Mentioned In"] if l.strip())))


def render_letter_file(letter: str, stubs: dict) -> str:
    head = f"---\ntype: concept_index\nletter: {letter}\n---\n# Concept Stubs: {letter}\n"
    blocks = [s.render() for s in sorted(stubs.values(), key=lambda s: (s.name.lower(), s.name))]
    return head + ("\n" + "\n".join(blocks) if blocks else "")


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(text.encode("utf-8"))
    os.replace(tmp, path)


class StubStore:
    def __init__(self, directory: Path = None):
        self.dir = Path(directory) if directory else STUBS_DIR
        self._letters = {}
        self._dirty = set()

    def legacy_files(self) -> list:
        if not self.dir.exists():
            return []
        return sorted(p for p in self.dir.glob("*.md") if p.name not in LETTER_FILES)

    def require_consolidated(self) -> None:
        n = len(self.legacy_files())
        if n:
            raise StubStoreError(
                f"{n} concept stubs are still one file each in {self.dir.name}/. "
                "Run `python -m utils.stub_consolidate --apply --delete` once before ingesting."
            )

    def letter_path(self, letter: str) -> Path:
        return self.dir / f"{PREFIX}{letter}.md"

    def _load(self, letter: str) -> dict:
        if letter not in self._letters:
            path = self.letter_path(letter)
            self._letters[letter] = parse_letter_file(path.read_text(encoding="utf-8", errors="replace")) if path.is_file() else {}
        return self._letters[letter]

    def get(self, name: str):
        return self._load(bucket(name)).get(name.lower())

    def create(self, name: str) -> Stub:
        self.require_consolidated()
        stub = Stub(name)
        self._load(bucket(name))[name.lower()] = stub
        self._dirty.add(bucket(name))
        return stub

    def save(self, stub: Stub) -> None:
        self.require_consolidated()
        self._dirty.add(bucket(stub.name))

    def flush(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        for letter in sorted(self._dirty):
            write_atomic(self.letter_path(letter), render_letter_file(letter, self._letters[letter]))
        self._dirty.clear()

    def iter_stubs(self):
        """Every stub, from the letter files and (before the migration) from the old per-concept files."""
        seen = set()
        for letter in LETTERS:
            for key, stub in self._load(letter).items():
                seen.add(key)
                yield stub
        for p in self.legacy_files():
            if p.stem.lower() not in seen:
                yield parse_legacy(p.read_text(encoding="utf-8", errors="replace"), p.stem)
