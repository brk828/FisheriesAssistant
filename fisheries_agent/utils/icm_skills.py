"""Generates draft project skills (skills/<name>/SKILL.md) from brain evidence, with a citation audit and gap report.

    python -m utils.icm_skills <workspace> [skill ...] [--force]

For each topic in icm_templates/skills.yaml the brain is searched, approved sources are copied into the skill's
references/, and the LLM drafts the skill from that evidence only. Topics with no close source are not written up;
they are listed in skills/<name>/GAPS.md with the kind of source that would fill them. Drafts are marked
`status: draft`; set `status: reviewed` after checking to protect a skill from regeneration.
"""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from utils import icm_seed

SKILLS_PATH = Path(__file__).resolve().parent.parent / "icm_templates" / "skills.yaml"
_CITE = re.compile(r"\[\[([^\]]+)\]\]")
UNSOURCED_LINE = "Unsourced: no supporting source in the brain yet."


def load_specs() -> dict:
    return yaml.safe_load(SKILLS_PATH.read_text(encoding="utf-8")) or {}


def build_prompt(skill: str, spec: dict, answers: dict, evidence: list) -> str:
    parts = [
        f"Write the body of a SKILL.md file named '{skill}' for a fisheries research project.",
        f"Purpose: {spec['description']}",
        "Rules:",
        "- Use ONLY the evidence below. Do not add facts, methods or numbers that the evidence does not support.",
        "- Cite every substantive statement as [[source_id]] using only the ids listed under that topic.",
        f"- For a topic marked NO EVIDENCE write its heading and the single line '{UNSOURCED_LINE}' and nothing else.",
        "- Structure: a short '## When to use' section, then one '## <topic>' section per topic in the order given, "
        "then '## Workflow in R' (a short ordered list that only uses methods and packages named in the evidence).",
        "- Markdown only, no front matter, under 900 words.", "",
        "Project answers: " + "; ".join(f"{k}: {v}" for k, v in answers.items() if v), "",
    ]
    for ev in evidence:
        parts.append(f"### Topic: {ev['name']}")
        if not ev["candidates"]:
            parts += ["NO EVIDENCE", ""]
            continue
        for c in ev["candidates"]:
            parts.append(f"- [[{c['source_id']}]] {c['cite']}\n  Excerpt: {c['excerpt']}")
        parts.append("")
    return "\n".join(parts)


def web_block(web: list) -> str:
    """Prompt section for internet evidence. Each item: {'id': 'web:...', 'kind': 'cran'|'paper', 'text': str}."""
    lines = ["", "### Web evidence (internet, verified lookups; NOT from the vault)",
             "Rules for this section: cite these only by their id, for example [[web:cran-glmmTMB]]. Use them for current package names, "
             "versions and the existence of methods papers only. Do not take formulas, numbers or recommendations from them beyond what the "
             "text states. Name an R package only if it is listed here or appears in the vault evidence above.", ""]
    lines += [f"- [[{w['id']}]] ({w['kind']}) {w['text']}" for w in web]
    return "\n".join(lines) + "\n"


def audit(text: str, allowed: set) -> tuple:
    """Removes citations to ids that are not in the skill's references and marks uncited statements.
    Returns (clean text, {'unknown_cites': [...], 'marked_uncited': n})."""
    unknown = []

    def keep(m):
        if m.group(1) in allowed:
            return m.group(0)
        unknown.append(m.group(1))
        return ""

    text = _CITE.sub(keep, text)
    out, heading, marked, in_code = [], "", 0, False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
        elif in_code:
            pass
        elif s.startswith("#"):
            heading = s.lower()
        elif (len(s) > 40 and not _CITE.search(s) and not s.startswith("Unsourced")
              and "when to use" not in heading and "(unsourced)" not in s):
            line = line.rstrip() + " (unsourced)"
            marked += 1
        out.append(line)
    return "\n".join(out) + "\n", {"unknown_cites": unknown, "marked_uncited": marked}


def _is_protected(skill_md: Path) -> bool:
    return skill_md.is_file() and bool(re.search(r"^status:\s*reviewed\s*$", skill_md.read_text(encoding="utf-8"), re.M))


def generate(root: Path, skill: str, llm, approve=None, force: bool = False, spec: dict = None, web: list = None) -> dict:
    """Builds one skill. Returns {'status': 'draft'|'refs-only'|'protected', 'copied': n, 'gaps': n, 'audit': {...}}."""
    root = Path(root)
    if spec is None:
        specs = load_specs()
        if skill not in specs:
            raise ValueError(f"Unknown skill '{skill}'. Available: {', '.join(specs)}")
        spec = specs[skill]
    folder = root / "skills" / skill
    skill_md = folder / "SKILL.md"
    if _is_protected(skill_md) and not force:
        return {"status": "protected", "copied": 0, "gaps": 0, "audit": {}}
    answers = icm_seed.project_config(root).get("answers") or {}
    approve = approve or (lambda loc, r: r["candidates"])

    evidence, gaps, copied = [], [], 0
    for topic in spec["topics"]:
        r = icm_seed.search_topic(topic, answers)
        found = bool(r["candidates"])
        chosen = approve(f"skill {skill}", r) if found else []
        r["candidates"] = [c for c in chosen if icm_seed.copy_note(c, folder / "references")]
        copied += len(r["candidates"])
        if not r["candidates"]:
            gaps.append({"where": f"skill {skill}", **r, "declined": found})
        evidence.append(r)
    icm_seed.write_sources(root)

    allowed = {c["source_id"] for ev in evidence for c in ev["candidates"]}
    web = web or []
    allowed |= {w["id"] for w in web}
    report, status = {}, "refs-only"
    if llm is not None and allowed:
        prompt = build_prompt(skill, spec, answers, evidence)
        if web:
            prompt += web_block(web)
        draft = llm(prompt)
        draft, report = audit(re.sub(rf"\A\s*#\s+{re.escape(skill)}\s*\n", "", draft), allowed)
        head = (f"---\nname: {skill}\ndescription: {spec['description']}\nstatus: draft\n"
                f"generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}\n---\n\n# {skill}\n\n")
        folder.mkdir(parents=True, exist_ok=True)
        skill_md.write_text(head + draft.strip() + "\n", encoding="utf-8")
        status = "draft"
    text = icm_seed.gaps_text(f"Gaps for skill: {skill}", gaps)
    if report:
        text += (f"\n## Citation audit\n\n- Citations removed (id not in references): {', '.join(report['unknown_cites']) or 'none'}\n"
                 f"- Statements marked '(unsourced)': {report['marked_uncited']}\n")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "GAPS.md").write_text(text, encoding="utf-8")
    return {"status": status, "copied": copied, "gaps": len(gaps), "audit": report}


def _default_skills(root: Path) -> list:
    from utils import icm_scaffold
    return icm_scaffold.load_types().get(icm_seed.project_config(root).get("type"), {}).get("skills", [])


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    force = "--force" in argv
    args = [a for a in argv if a != "--force"]
    if not args:
        print(__doc__)
        return 2
    from utils import icm_wizard
    root = Path(args[0])
    skills = args[1:] or _default_skills(root)
    llm = icm_wizard.make_llm()
    if llm is None:
        print("No OPENROUTER_API_KEY configured: references and gap reports will be written, but no skill draft.")
    for s in skills:
        r = generate(root, s, llm, approve=icm_seed.prompt_approve, force=force)
        print(f"{s}: {r['status']}; copied {r['copied']} note(s), {r['gaps']} gap(s) (see skills/{s}/GAPS.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
