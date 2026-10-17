"""Checks an ICM workspace against the vendored conventions (icm_core/_core/CONVENTIONS.md).

    python -m utils.icm_validate <workspace_folder>

Returns a list of issues; an empty list means the workspace passes.
"""
import re
import sys
from pathlib import Path

STAGE_LINE_TARGET = 80
AGENTS_CHAR_BUDGET = 6000       # roughly 1,500 tokens
REQUIRED_SECTIONS = ("## Inputs", "## Process", "## Outputs")
_PATH_CELL = re.compile(r"`?([^`|]+?)`?")
_STAGE_REF = re.compile(r"(?:\.\./)+(\d\d-[\w-]+)/")


def _inputs_rows(text: str) -> list:
    """Rows of the Inputs table as lists of cells."""
    m = re.search(r"## Inputs\s*\n(.*?)(?=\n## |\Z)", text, re.S)
    rows = []
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("|") and not re.match(r"\|\s*-", line):
                rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows[1:]


def validate(root) -> list:
    root = Path(root)
    issues = []
    agents = root / "AGENTS.md"
    if not agents.is_file():
        issues.append("AGENTS.md is missing.")
    else:
        text = agents.read_text(encoding="utf-8")
        if "BEGIN USER PROFILE" not in text or "BEGIN PROJECT ROUTING" not in text:
            issues.append("AGENTS.md is missing the user profile block or the project routing block.")
        if len(text) > AGENTS_CHAR_BUDGET:
            issues.append(f"AGENTS.md is {len(text)} characters (budget {AGENTS_CHAR_BUDGET}); shorten the profile or routing.")
    ctx = root / "CONTEXT.md"
    if not ctx.is_file():
        issues.append("CONTEXT.md is missing.")
    else:
        for target in re.findall(r"`(stages/[^`]+)`", ctx.read_text(encoding="utf-8")):
            if not (root / target).is_file():
                issues.append(f"CONTEXT.md routes to {target}, which does not exist.")

    stages = sorted(p for p in (root / "stages").glob("*") if p.is_dir()) if (root / "stages").is_dir() else []
    if not stages:
        issues.append("No stages found under stages/.")
    for stage in stages:
        c = stage / "CONTEXT.md"
        if not c.is_file():
            issues.append(f"{stage.name}: CONTEXT.md is missing.")
            continue
        text = c.read_text(encoding="utf-8")
        for sec in REQUIRED_SECTIONS:
            if sec not in text:
                issues.append(f"{stage.name}: missing '{sec}' section.")
        if len(text.splitlines()) > STAGE_LINE_TARGET:
            issues.append(f"{stage.name}: CONTEXT.md is over {STAGE_LINE_TARGET} lines.")
        for row in _inputs_rows(text):
            loc = _PATH_CELL.fullmatch(row[1]).group(1) if len(row) > 1 and _PATH_CELL.fullmatch(row[1]) else ""
            if not loc or loc == "-":
                continue
            ref = _STAGE_REF.match(loc)
            if ref and ref.group(1) >= stage.name:
                issues.append(f"{stage.name}: reads from {ref.group(1)}, which is not an earlier stage (references must be one-way).")
            target = (stage / loc).resolve()
            # Files under output/ are produced at run time, so only their folder must exist.
            check = target.parent if "output" in Path(loc).parts and not loc.endswith("/") else target
            if not check.exists():
                issues.append(f"{stage.name}: input '{loc}' does not exist.")

    for skill in sorted((root / "skills").glob("*/SKILL.md")) if (root / "skills").is_dir() else []:
        refs = {p.stem for p in (skill.parent / "references").glob("*.md")}
        for cited in re.findall(r"\[\[([^\]]+)\]\]", skill.read_text(encoding="utf-8")):
            if cited not in refs:
                issues.append(f"{skill.parent.name}: cites [[{cited}]] but it is not in the skill's references/.")
    return issues


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print(__doc__)
        return 2
    issues = validate(argv[0])
    print("\n".join(f"- {i}" for i in issues) if issues else "Workspace passes validation.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
