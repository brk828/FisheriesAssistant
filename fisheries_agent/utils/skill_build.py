"""Builds prepackaged analysis skills into skill_library/skills/ from brain evidence plus consent-gated web lookups.

    python -m utils.skill_build estimate [skill ...]   # evidence found, web items, prompt size and cost estimate; sends nothing
    python -m utils.skill_build draft [skill ...]      # same, then asks before sending anything to OpenRouter and writing drafts
    python -m utils.skill_build web [skill ...]        # only the web lookups (CRAN existence, Crossref) with a consent question

Skills come from icm_templates/library_skills.yaml. Drafts are written as status: draft with a citation audit, GAPS.md and
SOURCES.md (brain citations and web items kept separate). A skill with status: reviewed is never overwritten.
"""
import sys
from pathlib import Path

import yaml

from utils import brain_citations, icm_seed, icm_skills, web_evidence
from utils.skill_library import LIBRARY

SPEC_PATH = Path(__file__).resolve().parent.parent / "icm_templates" / "library_skills.yaml"
IN_PRICE_PER_M, OUT_PRICE_PER_M, OUT_TOKENS = 3.0, 15.0, 2500   # assumed main-model prices (USD per million tokens)


def load_specs() -> dict:
    return yaml.safe_load(SPEC_PATH.read_text(encoding="utf-8")) or {}


def gather_web(spec: dict) -> list:
    items = []
    for pkg in spec.get("packages", []):
        r = web_evidence.check_r_package(pkg)
        if r.get("exists"):
            items.append({"id": f"web:cran-{pkg}", "kind": "cran", "text": f"R package {pkg} {r['version']} on CRAN: {r['title']} ({r['url']})"})
    if spec.get("web_query"):
        for i, p in enumerate(web_evidence.search_methods_papers(spec["web_query"], rows=5), 1):
            if p["doi"] and p["title"]:
                items.append({"id": f"web:doi-{p['doi']}", "kind": "paper", "text": f"{p['title']} ({p['year']}), {p['journal']}, doi:{p['doi']}"})
    return items


def evidence_for(spec: dict) -> list:
    return [icm_seed.search_topic(t, {}) for t in spec["topics"]]


def estimate(skill: str, spec: dict, evidence: list, web: list) -> dict:
    prompt = icm_skills.build_prompt(skill, spec, {}, evidence) + (icm_skills.web_block(web) if web else "")
    in_tok = len(prompt) // 4
    return {"prompt_chars": len(prompt), "in_tokens": in_tok, "cost": in_tok / 1e6 * IN_PRICE_PER_M + OUT_TOKENS / 1e6 * OUT_PRICE_PER_M,
            "sources": sum(len(e["candidates"]) for e in evidence), "gaps": sum(not e["candidates"] for e in evidence)}


def write_skill_sources(folder: Path, web: list) -> None:
    prov = icm_seed._load_prov(folder / "references")
    lines = [f"# Sources for {folder.name}", "", "## Vault sources (copied snapshots in references/)", ""]
    for sid in sorted(prov):
        cite = prov[sid].get("cite") or sid
        lines.append(f"- [[{sid}]] {cite}")
    lines += ["", "## Web-derived items (internet lookups, not vault evidence)", ""]
    lines += [f"- [[{w['id']}]] {w['text']}" for w in web] or ["- none"]
    (folder / "SOURCES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0] not in ("estimate", "draft", "web"):
        print(__doc__)
        return 2
    cmd, specs = argv[0], load_specs()
    names = argv[1:] or list(specs)
    unknown = [n for n in names if n not in specs]
    if unknown:
        print(f"Unknown skill(s): {', '.join(unknown)}. Available: {', '.join(specs)}")
        return 2
    print("Web lookups send only package names and short topic queries to cran and Crossref (public APIs).")
    use_web = input("Allow them? (y/N): ").strip().lower() in ("y", "yes")
    plan, total = {}, 0.0
    for n in names:
        ev = evidence_for(specs[n])
        web = gather_web(specs[n]) if use_web else []
        est = estimate(n, specs[n], ev, web)
        plan[n] = (ev, web)
        total += est["cost"]
        print(f"- {n}: {est['sources']} vault source(s), {est['gaps']} topic gap(s), {len(web)} web item(s); ~{est['in_tokens']:,} input tokens, ~${est['cost']:.2f}")
    if cmd == "web":
        for n, (_ev, web) in plan.items():
            print(f"\n{n}:\n" + "\n".join(f"  - {w['text']}" for w in web))
        return 0
    print(f"\nEstimated total ~${total:.2f} (assumed prices ${IN_PRICE_PER_M}/M in, ${OUT_PRICE_PER_M}/M out, {OUT_TOKENS} output tokens per skill).")
    if cmd == "estimate":
        return 0
    from utils import icm_wizard
    llm = icm_wizard.make_llm()
    if llm is None:
        print("No OPENROUTER_API_KEY configured (set it in .env with setup_api_key.py). Nothing was sent or written.")
        return 1
    if input("Send these vault excerpts to OpenRouter and write drafts? (y/N): ").strip().lower() not in ("y", "yes"):
        print("Cancelled.")
        return 0
    for n, (ev, web) in plan.items():
        r = icm_skills.generate(LIBRARY, n, llm, approve=lambda loc, res: res["candidates"], spec=specs[n], web=web)
        if r["status"] == "draft":
            write_skill_sources(LIBRARY / "skills" / n, web)
        print(f"{n}: {r['status']}; copied {r['copied']} note(s), {r['gaps']} gap(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
