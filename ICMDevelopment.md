# ICM-Based Project Management: Development Plan

Status: Phases 1-3 complete (standalone tools, not yet wired into the orchestrator); Phase 4 next.

Done so far (Phase 1):
- `fisheries_agent/icm_core/`: vendored ICM core (MIT, pinned to upstream commit `02ba5d8`), with `LICENSE` and `UPSTREAM.json`.
- `utils/icm_update.py`: diff and optional apply against upstream.
- `icm_templates/project_types.yaml`: fixed stage trees for mark_recapture, monitoring_cpue, literature_synthesis and report.
- `utils/icm_scaffold.py`: folder naming, `AGENTS.md` (profile block plus routing block), `CONTEXT.md`, stage contracts, `data/`, never overwrites.
- `utils/icm_git.py`: optional git init, `.gitignore` rules and the 50 MB size cap.
- `utils/icm_validate.py`: convention checks.
- `utils/icm_wizard.py`: `python -m utils.icm_wizard` runs the new-project flow (one-time user profile into `brain_meta/user_profile.md`, flat questionnaire, suggested type and tree for approval, git and ignore questions, LLM-written routing with a plain fallback).
- `utils/gitsync.py`: `commit_changes` now skips files over a workspace's `git.max_file_mb` and reports them.
- `tests/test_icm.py`: 15 tests (`python -m unittest tests.test_icm` from `fisheries_agent`).

Done (Phase 2):
- `brain_index.find_sources(query, limit, core)`: structured source search. Coverage is judged on the topic words (`core`) so species and place names alone cannot make a source count as relevant.
- `icm_templates/reference_topics.yaml` and `icm_templates/skills.yaml`: topic outlines (query, why it matters, kind of source needed). They hold no skill content.
- `utils/icm_seed.py`: `seed` (propose, approve, copy snapshots with hashes in `references/_provenance.json`, write `shared/sources.md` and root `GAPS.md`), `refresh [--apply]`, and `supply` (PDF goes to the ingest inbox; a citation or URL is recorded as an external reference).
- `utils/icm_skills.py`: LLM drafts each `SKILL.md` from copied evidence only, citation audit (unknown ids removed, uncited statements marked), `skills/<name>/GAPS.md`, `status: draft`, and `status: reviewed` protects a skill from regeneration unless `--force`.
- `icm_wizard` offers seeding and skill drafting after a project is created.
- 22 tests in `tests/test_icm.py`.

Not yet done: LLM skill drafts have not been run against a live model, and orchestrator and onboarding integration is planned for Phase 4. Phase 3 (restructuring) is done: `python -m utils.icm_restructure <folder> [--dry-run] [--copy-small-data]`, with `utils/icm_data.py` for the size+mtime linked-file checks. Next: Phase 4.

## 1. Goal

Extend the project-management side of the agent so it can:

1. **Create** new projects as ICM workspaces (staged folders, `AGENTS.md` at the root, a `CONTEXT.md` per stage).
2. **Restructure** existing projects into an ICM workspace, written to a *new* folder so the original is never modified or deleted.
3. **Suggest** a project type and folder structure from a short questionnaire.
4. **Seed each workspace from the Fisheries Brain**: copy the relevant reference notes into the project and generate project-specific skills (e.g. a mark-recapture analysis skill) that cite those notes as sources.

Reference: [Interpretable Context Methodology](https://github.com/RinDig/Interpretable-Context-Methodology) (ICM; paper: arXiv 2603.16021).

## 2. Where we are today

- `setup_onboarding.py` asks for an RProjects root, lets the user pick folders, profiles them (R scripts, Quarto/RMarkdown style) and writes `project_manifest.yaml`.
- `utils/project_memory.py` keeps per-project memory (file scan, runs, notes, context).
- `main_orchestrator.py` reads the manifest, routes intents, plans analyses, runs R through specialized agents, and commits changes via `utils/gitsync.py`.
- The brain (`00_Fisheries_Brain/01_Sources`, `02_Brain`) is indexed by `utils/brain_index.py` with retrieval, citations and enrichment.

The manifest describes projects but does not give them structure or project-local knowledge. ICM fills that gap.

## 3. ICM concepts we adopt

| ICM idea | Our use |
|---|---|
| Layer 0 root file (`CLAUDE.md`) | `AGENTS.md` at the project root: where am I, project type, rules, pointers |
| Layer 1 `CONTEXT.md` | Root routing: which stage for which task |
| Layer 2 stage `CONTEXT.md` | Per-stage contract: Inputs, Process, Outputs (+ checkpoints, audits) |
| Layer 3 `references/`, `_config/`, `skills/` | Brain notes copied in, project conventions, generated skills |
| Layer 4 `output/` | Working artifacts and stage handoffs, human-editable |
| One stage, one job; plain text; one-way references; canonical sources | Enforced by a validator (see 6.5) |

Fisheries-flavoured stage sets (proposed starting points, each editable by the user):

- **Mark-recapture / abundance:** 01-data-prep, 02-model-design, 03-analysis (R), 04-review, 05-report.
- **Monitoring / CPUE trends:** 01-data-prep, 02-standardization, 03-analysis, 04-report.
- **Literature synthesis:** 01-question, 02-evidence, 03-synthesis, 04-draft.
- **Report / manuscript:** 01-outline, 02-draft, 03-review, 04-final.
- **Custom:** built from the questionnaire.

## 4. Target workspace layout

```text
<project>_icm/
  AGENTS.md                  Layer 0: user working profile (reused) + project-specific routing (LLM-written)
  CONTEXT.md                 Layer 1: stage routing
  _config/
    project.yaml             questionnaire answers, species, region, citation style
    conventions.md           naming, R style, units (from detected project habits)
  stages/
    01-data-prep/
      CONTEXT.md             Inputs / Process / Outputs, checkpoints, audit
      references/            brain notes relevant to this stage
      output/
    02-.../
  skills/
    mark-recapture/
      SKILL.md               generated, cites references
      references/            brain notes it draws on
  shared/
    sources.md               canonical bibliography (source_id, title, year, brain path)
  data/                      large inputs and model objects (raw downloads, Nimble/mark-recapture fits); git-ignored
  legacy/                    optional: pointers to the original project (never moved)
  .gitignore                 written only if the user chose a git repository (see 6.8)
```

Location and naming (decided):
- All ICM workspaces are created under the **projects root already collected during onboarding** (`global_settings.r_projects_root`).
- **Restructured project:** same folder name as the original plus `_icm` (`Colorado_Pikeminnow` becomes `Colorado_Pikeminnow_icm`). The original stays where it is.
- **New project:** folder name derived from the user's project name (shortened and sanitized to a safe filesystem name when long) plus `_icm`. The full name is kept in `_config/project.yaml`. If the folder already exists, ask before reusing it; never overwrite.

Rules: the original project is read-only input; the new workspace links back to it through `legacy` pointers in `project.yaml` and copies, not moves, anything it needs (data stays where it is, referenced by path).

## 5. ICM repo: clone, vendor or reference?

Options:

1. **Clone the whole repo into every install and keep it updated.** Pulls in unrelated workspaces (script-to-animation, etc.), requires git on user machines, and upstream changes can silently alter behaviour of our generator.
2. **Use ideas only; write our own.** Stable, but we diverge and lose community improvements.
3. **Vendor a pinned subset plus an explicit update command (recommended).**

Recommendation: option 3.

- Vendor only the core pieces we need into `fisheries_agent/icm_core/`: `_core/CONVENTIONS.md`, the stage contract and questionnaire templates, and the workspace-builder stage prompts. Do not vendor the example workspaces.
- Record the upstream URL and commit SHA in `icm_core/UPSTREAM.json` along with the license text and attribution (license checked: MIT, which allows copying and redistribution provided the copyright notice and license text are kept; ship them as `icm_core/LICENSE` and credit Jake Van Clief in `UPSTREAM.json` and the readme).
- Add `python -m utils.icm_update` that fetches upstream at a chosen ref, shows a diff of the vendored files against the pinned SHA, and lets the maintainer accept or reject it. Updates ship through our own repo releases, so users get tested changes rather than raw upstream `main`.
- Our fisheries-specific templates live in `icm_templates/` and override or extend core templates, so upstream updates do not overwrite them.
- Keep the generator independent of upstream's Claude-specific bits (`CLAUDE.md` becomes `AGENTS.md`; no assumption of Claude Code as the runner, since our runner is `main_orchestrator.py` via OpenRouter).

Open question: whether to also contribute a fisheries workspace back upstream (their contribution guide invites new workspaces). Decide after the generator works.

## 6. Components to build

### 6.1 Questionnaire (`utils/icm_questionnaire.py`)
Short, flat, all-at-once (per ICM's questionnaire convention), system-level only:
project name, goal in one sentence, project type (suggested, user confirms), whether it should be a git repository (and, if so, what to ignore), target species and region, data types available, analyses wanted (mark-recapture, CPUE, growth, occupancy, other), deliverables (report, manuscript, dashboard), citation style, R/Quarto preferences. For existing projects, answers are pre-filled from the scan in `setup_onboarding.py` / `project_memory.scan`.

### 6.1a AGENTS.md: reusable profile plus project routing (decided)
`AGENTS.md` is the cross-framework convention, so the file must work in any agent tool, not only ours. It has two parts:

1. **User working profile (reused for most of the file).** How the user conducts their work: preferred tools (R, Quarto vs. RMarkdown, packages), coding and documentation style, naming and units, citation style, review and approval habits (plan, approve, then run), and communication preferences. This is collected once (onboarding, plus detected habits from the project scan) and stored as one canonical file, e.g. `brain_meta/user_profile.md`. Each project's `AGENTS.md` includes it as a marked, generated block with a content hash. A `refresh` command updates the block in all workspaces when the profile changes, and flags blocks the user edited by hand instead of overwriting them.
2. **Project-specific routing (LLM-written).** Written per project from the project type, the questionnaire answers and the ICM building process: what the project is, which stage handles which kind of request, where data and skills live, and the project's constraints. Kept short (token budget checked by the validator) and regenerated or revised on request.

Profile text is never duplicated by hand across projects (ICM canonical-source rule); stage `CONTEXT.md` files point to `AGENTS.md` rather than restating it. Optional thin shims (e.g. a `CLAUDE.md` or `.github/copilot-instructions.md` that just points to `AGENTS.md`) can be generated on request for tools that need a specific filename.

### 6.2 Project-type suggester (`utils/icm_suggest.py`)
Each project type has a **fixed folder structure** (stage names and order) defined in a template, so two projects of the same type always look the same. The LLM does not invent the tree; it fills in the contents (stage `CONTEXT.md` files, routing, skills) within that structure. Only the "Custom" type lets the LLM propose stages, and the user must approve them. Maps answers (and detected files/packages, e.g. `RMark`, `marked`, `FSA`) to a stage template and skill list. Presents the proposed tree and asks for approval or edits before anything is written. LLM is used only to propose and explain; the mapping rules live in a plain YAML table the user can edit.

### 6.3 Restructure of existing projects (`utils/icm_restructure.py`)
1. Scan with `project_memory.scan` and classify files (data, scripts, results, reports).
2. Propose a mapping: which existing files belong to which stage (as references or pointers).
3. Write the new workspace to `<project>_icm/` beside the original (or a user-chosen path). Never edit or delete the source; copy small text files, link to large or data files by path.
4. Produce a `MIGRATION.md` listing what was copied, linked and left behind.
5. Dry-run mode prints the plan without writing.

### 6.4 Brain-to-project seeding (`utils/icm_seed.py`)
(Runs before skill generation; its retrieval results also feed gap detection in 6.5.)
- Use `brain_index` retrieval with queries built from questionnaire answers (species, region, method) to select candidate notes; rank, cap per stage, and show the list for approval.
- Copy selected notes into `stages/*/references/` and `skills/*/references/` with front matter preserved, plus their `source_id`s, and write `shared/sources.md`.
- Honour the ICM "selective section routing" idea: stage `CONTEXT.md` Inputs tables name the specific sections/headings to load, not whole notes.
- Provenance: each copied note records its brain path and a content hash so later brain updates can be detected and offered as a refresh (`icm_seed --refresh`).

### 6.5 Skill generator (`utils/icm_skills.py`) and gap detection
Skills are **LLM-generated as much as possible**; the code supplies structure, evidence and checks, not hand-written skill text.

1. **Select skills** from the project type, questionnaire and detected packages (e.g. mark-recapture, CPUE standardization, growth). A small YAML spec per skill lists the topics to cover (assumptions, model choices, R packages, diagnostics, pitfalls, reporting) and acts as an outline for the LLM, not as content.
2. **Gather evidence** from the brain with `brain_index` retrieval for each topic, restricted to the notes seeded into the project.
3. **Draft `SKILL.md`** with the LLM from that evidence only, with inline citations to `source_id`s in `skills/<name>/references/`. Status `draft` until the user reviews it.
4. **Citation audit:** every substantive claim cites an existing reference; uncited claims are removed or marked.
5. **Gap detection:** for each topic where the brain has weak or no evidence (no notes, only tangential matches, or a needed method with no primary source), write `skills/<name>/GAPS.md` and tell the user. Each gap lists the topic, why it matters, what was searched, and suggested source types (e.g. "primary paper for the Cormack-Jolly-Seber model", "agency protocol for PIT-tag detection"). The user can then:
   - supply a PDF or file: it goes through the existing ingest pipeline (`pdfs_to_process`) into the brain, then seeding re-runs for the project and the skill is regenerated;
   - supply a citation or URL: recorded in `shared/sources.md` as an external reference (not copied unless the user provides the file);
   - accept the gap: the skill keeps the topic marked "unsourced" and the agent says so when it uses it.
6. The same gap check applies to stage references: if a stage needs a reference topic the brain lacks, it is listed in `GAPS.md` at the project root.
7. Generated skills feed the existing plan, approve and run-in-R flow rather than bypassing it.

### 6.6 Validator (`utils/icm_validate.py`)
Checks a workspace against the vendored conventions: every stage has `CONTEXT.md` with Inputs/Process/Outputs; references are one-way; Inputs point at files that exist; no duplicated canonical content; `AGENTS.md` under a token budget; skills cite only existing references. Run after generation and on demand.

### 6.7 Git option and ignore rules (`utils/icm_git.py`)
Asked once in the questionnaire: "Should this project be a git repository?"
- **No:** no `git init`, no `.gitignore`; the rest of the workspace is unchanged.
- **Yes:** run `git init`, then ask a short follow-up about what to keep out of version control:
  - file types/extensions (defaults below, user may add or remove),
  - specific folders,
  - specific files,
  - a size threshold (e.g. any file over N MB; default suggestion 50 MB, user can change).
- Default ignores: everything under `data/`, plus `*.rds`, `*.RData`, `*.rda`, `*.nimble*`, `*.rdata`, large `*.csv`/`*.xlsx` exports, MCMC output and `*.mcmc`/`*.samples` files, `.Rproj.user/`, `.Rhistory`, `.env*`. Ignoring `data/` is the main rule; the others catch large files that end up elsewhere.
- The questionnaire answers are saved in `_config/project.yaml` (`git: {enabled, ignore_types, ignore_paths, max_file_mb}`) so rules can be regenerated.
- Size threshold is not expressible in `.gitignore`, so it is enforced in two places: at ingestion (files above the threshold go to `data/` and their path is added to `.gitignore`) and at commit time (extend `gitsync.snapshot`/`commit_changes` to skip any file over the threshold and report it). The existing secret-file filter stays.
- Add a `data/README.md` describing what belongs there and listing source/download provenance, since the files themselves are not versioned. `MIGRATION.md` records any large files that were linked rather than copied.
- Never `git add` ignored files; sync only pushes if a remote exists, and asks before creating one.

### 6.8 Data ingestion into `data/`
- New and restructured projects get a `data/` folder with `raw/` (downloads, source files as received) and `models/` (Nimble and mark-recapture fits, MCMC output).
- Restructuring: large model objects and raw datasets found in the original project are **linked by path** by default (listed in `data/manifest.yaml` with size and hash) and copied only if the user asks. Small data files below the threshold can be copied.
- **Linked-file checks (decided):** at each stage run, compare the current size and modification time against `data/manifest.yaml`. If either differs, recompute the hash and warn the user (changed or missing file) before the stage proceeds. A full hash check of everything also runs on request ("validate project"). Manifest entries store path, size, mtime and hash.
- Stage `CONTEXT.md` Inputs reference `data/` paths through the manifest so the agent never loads large binaries as context.

### 6.9 Orchestrator integration
- New intents: "create a project", "restructure project X", "refresh project references", "validate project".
- Manifest (`project_manifest.yaml`) gets an `icm_workspace` path per project; `project_memory.context` prefers the workspace's `AGENTS.md`/stage `CONTEXT.md` over a flat scan, loading only the current stage (layered loading).
- Stage runs write to `output/`; `gitsync.commit_changes` already handles commit/sync of project changes.
- Onboarding adds an optional step: "Create ICM workspaces for the selected projects now?"

## 7. Phases

**Phase 0: Decisions (before coding)**
- ICM license confirmed as MIT; vendoring approach approved in principle.
- Workspace location and naming are settled (section 4).
- Agree on the initial project types (start with mark-recapture, monitoring/CPUE, literature synthesis).

**Phase 1: Core and new-project path**
- Vendor ICM core with `UPSTREAM.json`; write `icm_update`.
- User profile file, `AGENTS.md` assembly (profile block plus LLM-written routing), root `CONTEXT.md`, stage `CONTEXT.md`, and fixed per-type folder templates.
- Questionnaire (including the git/ignore questions), suggester, scaffold writer, `icm_git`, `data/` layout, validator.
- Tests: scaffold into a temp dir, validate, assert structure; with git enabled, assert `.gitignore` rules and that large files are never staged.

**Phase 2: Brain seeding and skills**
- Retrieval-driven reference selection with approval step; `sources.md`; provenance hashes.
- Skill generator (LLM-drafted) with mark-recapture as the first skill; citation audit; `GAPS.md` and the supply-a-source flow back into ingestion.
- Evaluation: use `brain_eval` style checks to verify selected references are on-topic for a few known projects.

**Phase 3: Restructure existing projects**
- Scan-to-mapping, dry run, copy/link writer, `MIGRATION.md`.
- Verify the source folder is byte-identical afterwards (hash check in tests).

**Phase 4: Orchestrator and onboarding integration**
- Intents, manifest field, layered context loading, onboarding step.
- Docs: update `readme.md`, `agents.md`, `todo.md`.

**Phase 5: Maintenance**
- `icm_update` workflow, refresh of references when the brain changes, optional upstream contribution.

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Upstream ICM changes break the generator | Pinned SHA, explicit update with diff review |
| License/attribution issues | Check license in Phase 0; ship attribution file |
| Generated skills contain unsupported claims | Draft status, citation audit, user review, evidence limited to seeded notes, `GAPS.md` for missing sources |
| Profile block in `AGENTS.md` drifts between projects | Single canonical profile, hashed block, `refresh` command, hand-edit detection |
| Wrong or noisy brain notes copied in | Ranked list with approval, per-stage caps, location/species filters |
| Restructure damages a user's project | Write to a new folder only; dry run; hash check; never delete |
| Copied notes go stale | Provenance hashes and `--refresh` |
| Large workspaces bloat context | Layered loading; stage `CONTEXT.md` Inputs name sections; token budget in validator |
| Large Nimble/mark-recapture files committed by accident | `data/` ignored by default, user-chosen types/folders/size cap, commit-time size check |
| Repo size from copied notes | Copy only selected notes; large data stays linked, not copied |

## 9. Open questions

Resolved: brain notes are copied as snapshots with a `refresh` command; no symlinks (Windows-only for now; live links could be an optional setting on Mac/Linux later); `AGENTS.md` holds a reusable user working profile plus LLM-written project routing (6.1a); project types have fixed folder structures; skills are LLM-generated with gap reports for missing sources (6.5); size cap default is 50 MB; linked data is checked by size and mtime at each run, with a hash only on mismatch or request; workspaces live in the onboarding projects root with an `_icm` suffix; git is optional and asked per project; large files live in `data/` and are ignored.

None open. Add new questions here as they come up.
