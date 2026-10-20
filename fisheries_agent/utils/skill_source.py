"""Drafts skills from the developer's gitignored skill_source/ folder (articles, a report, telemetry and GLM material).

    python -m utils.skill_source extract            # PDFs -> skill_source/_extracted/*.txt (local; OCR for scans); no LLM
    python -m utils.skill_source estimate [skill ...]   # excerpts per source, prompt size and cost; sends nothing
    python -m utils.skill_source draft [skill ...]      # same, then asks before sending excerpts to OpenRouter and writing drafts

Specs: icm_templates/source_skills.yaml. Citations: icm_templates/skill_source_refs.yaml (read from the documents, never invented).
Only short excerpts cut locally are sent, and the prompt forbids copying sentences or code. Entries marked local_only (for example
a licensed book that forbids sharing) are never sent. Excerpts are not stored in the skill library; SOURCES.md lists citations only.
Drafts are status: draft. A skill with status: reviewed is not overwritten.
"""
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from utils import icm_skills
from utils.skill_library import LIBRARY

HERE = Path(__file__).resolve().parent.parent
SOURCE_DIR = HERE / "skill_source"
EXTRACTED = SOURCE_DIR / "_extracted"
REFS_PATH = HERE / "icm_templates" / "skill_source_refs.yaml"
SPECS_PATH = HERE / "icm_templates" / "source_skills.yaml"
IN_PRICE_PER_M, OUT_PRICE_PER_M, OUT_TOKENS = 3.0, 15.0, 4000
_REF_HEAD = re.compile(r"^\s*(references|literature cited|acknowledg(e)?ments)\b", re.I)


def load_refs() -> dict:
    return yaml.safe_load(REFS_PATH.read_text(encoding="utf-8")) or {}


def load_specs() -> dict:
    return yaml.safe_load(SPECS_PATH.read_text(encoding="utf-8")) or {}


def extract_pdfs() -> int:
    """Writes text for each PDF in skill_source/ (page markers kept). Pages without a text layer are OCRd. Skips the existing files."""
    import pypdf

    from utils import pdf_ingest
    EXTRACTED.mkdir(exist_ok=True)
    n = 0
    for pdf in sorted(SOURCE_DIR.rglob("*.pdf")):
        stem = re.sub(r"\W+", "_", pdf.stem)[:60]
        out = EXTRACTED / f"{stem}.txt"
        if out.exists() or "invoice" in pdf.name.lower() or "_files" in str(pdf):
            continue
        reader = pypdf.PdfReader(str(pdf))
        pages = []
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ""
            if len(text.strip()) < 30:
                try:
                    text = pdf_ingest._ocr_page(pdf, i)
                except Exception as e:
                    text = f"[OCR unavailable: {type(e).__name__}]"
            pages.append(f"\n\n=== page {i} ===\n{text}")
        out.write_text("".join(pages), encoding="utf-8")
        n += 1
        print(f"extracted {pdf.name} ({len(reader.pages)} pages)")
    return n


def _body(text: str) -> str:
    """Drops the reference list (the last heading-like references line past the midpoint)."""
    lines = text.splitlines(keepends=True)
    cut = None
    pos = 0
    for line in lines:
        if pos > len(text) * 0.5 and _REF_HEAD.match(line) and len(line.strip()) < 40:
            cut = pos
            break
        pos += len(line)
    return text[:cut] if cut else text


def _heading_key(line: str) -> str:
    return re.sub(r"^[#\s\d.]+", "", line.strip()).lower()


def section_slice(text: str, word: str, width: int) -> tuple:
    """(start, end) of the first short heading-like line that starts with `word`, running `width` characters."""
    pos = 0
    for line in text.splitlines(keepends=True):
        key = _heading_key(line)
        if 0 < len(line.strip()) < 90 and key.startswith(word.lower()):
            return pos, min(len(text), pos + width)
        pos += len(line)
    return None


def window_slices(text: str, patterns: list, width: int = 700) -> list:
    spans = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            spans.append((max(0, m.start() - width // 3), min(len(text), m.start() + width)))
    return spans


def _merge(spans: list) -> list:
    out = []
    for a, b in sorted(spans):
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(b, out[-1][1]))
        else:
            out.append((a, b))
    return out


def load_text(ref: dict) -> str:
    if ref.get("path"):
        return (SOURCE_DIR / ref["path"]).read_text(encoding="utf-8", errors="replace")
    return (EXTRACTED / f"{ref['file']}.txt").read_text(encoding="utf-8", errors="replace")


def excerpt(ref: dict, sel: dict) -> str:
    """Cuts the selected sections or keyword windows from one source, capped at sel['per_chars']."""
    text = _body(load_text(ref))
    cap = int(sel.get("per_chars", 8000))
    spans = []
    sections = sel.get("sections") or []
    if sections:
        each = max(1500, cap // max(1, len(sections)))
        for word in sections:
            s = section_slice(text, word, each)
            if s:
                spans.append(s)
    spans += window_slices(text, sel.get("windows") or [])
    if not spans:
        spans = [(0, cap)]
    pieces, total = [], 0
    for a, b in _merge(spans):
        chunk = re.sub(r"\n{3,}", "\n\n", text[a:b]).strip()
        if total + len(chunk) > cap:
            chunk = chunk[: max(0, cap - total)]
        if chunk:
            pieces.append(chunk)
            total += len(chunk)
        if total >= cap:
            break
    return "\n[...]\n".join(pieces)


def gather(spec: dict, refs: dict) -> tuple:
    """Returns ({id: excerpt}, [problems]). local_only and missing files are reported, never sent."""
    found, problems = {}, []
    for sid, sel in spec["sources"].items():
        ref = refs.get(sid)
        if ref is None:
            problems.append(f"{sid}: not in skill_source_refs.yaml")
        elif ref.get("local_only"):
            problems.append(f"{sid}: local only, not sent")
        else:
            try:
                found[sid] = excerpt(ref, sel)
            except FileNotFoundError:
                problems.append(f"{sid}: text not found (run extract)")
    return found, problems


def build_prompt(name: str, spec: dict, found: dict, refs: dict) -> str:
    pointers = [sid for sid in refs if refs[sid].get("local_only") and sid in spec["sources"]]
    head = [
        f"You are drafting part of a skill file named '{name}' for a fisheries research assistant.",
        f"Purpose: {spec['description']}", "",
        "Rules:",
        "- Base every substantive statement on the excerpts below. Cite as [[src:<id>]] using only the ids given. Mark statements that come from general knowledge, not the excerpts, with (general).",
        "- Excerpts are copyrighted works supplied for internal analysis. Paraphrase and synthesize; never copy sentences, code or figures from them.",
        "- Never invent authors, years, numbers or function names. R packages: only those listed or named in the excerpts.",
        "- Markdown only, no front matter. Keep code blocks short, original and clearly labelled as unexecuted.",
        "- Under 1,100 words (code blocks excluded).", "",
        "Task guidance: " + " ".join(spec["guidance"].split()), "",
    ]
    if spec.get("packages"):
        head += ["Allowed R packages: " + ", ".join(spec["packages"]), ""]
    if pointers:
        head += ["Pointer-only references (no text provided, cite only as a pointer): " + ", ".join(f"[[src:{p}]]" for p in pointers), ""]
    body = []
    for sid, text in found.items():
        body.append(f"### Source [[src:{sid}]] {refs[sid]['cite']}\n{text}\n")
    return "\n".join(head + body)


def estimate(prompt: str) -> dict:
    in_tok = len(prompt) // 4
    return {"chars": len(prompt), "in": in_tok, "cost": in_tok / 1e6 * IN_PRICE_PER_M + OUT_TOKENS / 1e6 * OUT_PRICE_PER_M}


def call_llm(prompt: str) -> tuple:
    from dotenv import load_dotenv
    from openai import OpenAI
    load_dotenv(HERE / ".env")
    key = os.getenv("OPENROUTER_API_KEY")
    if not key or key.startswith("your_"):
        return None, None
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)
    model = os.getenv("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.5")
    r = client.chat.completions.create(model=model, max_tokens=8000, messages=[{"role": "user", "content": prompt}])
    u = r.usage
    return (r.choices[0].message.content or "").strip(), (u.prompt_tokens, u.completion_tokens) if u else None


def _sources_section(used: list, refs: dict) -> str:
    return "\n".join(f"- [[src:{s}]] {refs[s]['cite']}" for s in used)


def write_skill(name: str, spec: dict, draft: str, used: list, refs: dict) -> str:
    folder = LIBRARY / "skills" / spec.get("skill", name)
    folder.mkdir(parents=True, exist_ok=True)
    allowed = {f"src:{s}" for s in refs}
    draft, report = icm_skills.audit(draft, allowed)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    mode, skill_md = spec["mode"], folder / "SKILL.md"
    if mode == "new":
        if icm_skills._is_protected(skill_md):
            return "protected"
        skill_md.write_text(f"---\nname: {name}\ndescription: {spec['description']}\nstatus: draft\ngenerated: {today}\n---\n\n# {name}\n\n{draft.strip()}\n", encoding="utf-8")
    elif mode == "supplement":
        (folder / "SUPPLEMENT.md").write_text(
            f"---\nname: {name}-supplement\nstatus: draft\ngenerated: {today}\n---\n\n# {name}: supplement from developer-supplied sources\n\n{draft.strip()}\n", encoding="utf-8")
        text = skill_md.read_text(encoding="utf-8")
        if "SUPPLEMENT.md" not in text:
            skill_md.write_text(text.rstrip() + "\n\n## Supplement\nSee `SUPPLEMENT.md` in this folder for a worked workflow drawn from developer-supplied sources (draft).\n", encoding="utf-8")
    elif mode == "part":
        text = skill_md.read_text(encoding="utf-8")
        title = spec["section"]
        m = re.search(rf"^## {re.escape(title)}.*?(?=^## |\Z)", text, re.M | re.S)
        if not m:
            return "section not found"
        skill_md.write_text(text[: m.start()] + draft.strip() + "\n\n" + text[m.end():], encoding="utf-8")
    sources = folder / "SOURCES.md"
    base = sources.read_text(encoding="utf-8").rstrip() + "\n\n" if sources.is_file() else f"# Sources for {name}\n\n"
    earlier = re.search(r"## Developer-supplied documents.*?(?=\n## |\Z)", base, flags=re.S)
    if earlier:
        used = [s for s in refs if f"[[src:{s}]]" in earlier.group(0) and s not in used] + list(used)
    base = re.sub(r"\n*## Developer-supplied documents.*?(?=\n## |\Z)", "", base, flags=re.S).rstrip() + "\n\n"
    sources.write_text(base + "## Developer-supplied documents (skill_source/, not in the vault; excerpts are not stored here)\n\n" + _sources_section(used, refs) + "\n", encoding="utf-8")
    if report["unknown_cites"] or report["marked_uncited"]:
        gaps = folder / "GAPS.md"
        old = gaps.read_text(encoding="utf-8").rstrip() + "\n\n" if gaps.is_file() else f"# Gaps for skill: {name}\n\n"
        gaps.write_text(old + f"## Audit of {mode} draft ({today})\n\n- Citations removed (unknown id): {', '.join(report['unknown_cites']) or 'none'}\n- Statements marked '(unsourced)': {report['marked_uncited']}\n", encoding="utf-8")
    return "ok"


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0] not in ("extract", "estimate", "draft"):
        print(__doc__)
        return 2
    if argv[0] == "extract":
        print(f"{extract_pdfs()} PDF(s) extracted to {EXTRACTED}")
        return 0
    refs, specs = load_refs(), load_specs()
    names = argv[1:] or list(specs)
    bad = [n for n in names if n not in specs]
    if bad:
        print(f"Unknown skill(s): {', '.join(bad)}. Available: {', '.join(specs)}")
        return 2
    plan, total = {}, 0.0
    for n in names:
        found, problems = gather(specs[n], refs)
        prompt = build_prompt(n, specs[n], found, refs)
        est = estimate(prompt)
        plan[n] = (found, prompt)
        total += est["cost"]
        print(f"- {n} [{specs[n]['mode']}]: {len(found)} source(s), {sum(map(len, found.values())):,} excerpt chars; ~{est['in']:,} input tokens, ~${est['cost']:.2f}")
        for p in problems:
            print(f"    note: {p}")
    print(f"\nEstimated total ~${total:.2f} (assumed ${IN_PRICE_PER_M}/M in, ${OUT_PRICE_PER_M}/M out, {OUT_TOKENS} output tokens per skill).")
    if argv[0] == "estimate":
        return 0
    if input("Send these excerpts to OpenRouter and write drafts? (y/N): ").strip().lower() not in ("y", "yes"):
        print("Cancelled.")
        return 0
    spent_in = spent_out = 0
    for n, (found, prompt) in plan.items():
        draft, usage = call_llm(prompt)
        if draft is None:
            print("No OPENROUTER_API_KEY configured. Nothing was sent or written.")
            return 1
        status = write_skill(n, specs[n], draft, [s for s in specs[n]["sources"] if s in refs], refs)
        if usage:
            spent_in += usage[0]
            spent_out += usage[1]
        print(f"{n}: {status}")
    print(f"USAGE: {spent_in:,} input + {spent_out:,} output tokens, ~${spent_in / 1e6 * IN_PRICE_PER_M + spent_out / 1e6 * OUT_PRICE_PER_M:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
