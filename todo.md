# Project To-Do List

Running list of planned work. Add new items as they come up; mark done items with `[x]` and keep them for history.

## Direction: brain as evidence, LLM as writer, R as executor

The Fisheries Brain is a reference, not the output. For a literature question, the framework retrieves relevant evidence from the brain and the LLM writes a plain-language answer from it. For a new analysis or report, the brain shows what and how work was done before, and the output is an analysis plan that is executed in R by the specialized agents (after user approval).

```text
User request -> intent router
  literature question -> evidence retrieval -> LLM answer with citations
  analysis / report   -> data profile + precedent retrieval -> LLM plan -> approve plan -> R agent -> approve run
```

Observations about the current brain (affects the design):
* `01_Sources` notes have front matter (`title`, `species`, `habitat`, `source_id`), headed sections and `[[wikilinks]]`; filenames often carry a date.
* `02_Brain` concept notes hold summaries, quoted evidence with `[[source]]` links, and a "Mentioned In" list; useful as a link graph from topic to sources.
* Front matter is inconsistent (`species` as list or string, `related_species`); normalize during indexing.
* A topic such as razorback sucker matches 20+ sources, so ranking and location filtering are required.
* Current `search_fisheries_brain` returns the first 3 substring matches (1,500 characters each), which is why answers just echo the brain.

## Open questions
- [ ] Citation style: title and year, `source_id`, or both?
- [ ] Per-question cost ceiling (limits how many chunks go to the model).
- [ ] Where plans are saved: `runs/` or the user's project folder; `.md` or `.yaml`.

## Phase B: Brain as a reference

### 1. Brain index and retrieval
- [x] Parse front matter and split notes into heading-level chunks.
- [x] Build a SQLite FTS5 index (fields: species, habitat, year, source id, chunk text); rebuild only when files change.
- [x] Alias table for common/scientific names, built from the vault (`utils/brain_enrich.py` -> `brain_meta/aliases_auto.json`; hand edits in `brain_meta/aliases.yaml` win) and used to expand searches. Still open: place-name aliases.
- [x] Source titles: frontmatter, then first heading, then citation (`brain_meta/source_titles.json`). LLM title pass for the remaining ~1,230 untitled sources: `python -m utils.brain_enrich titles-llm` (shows an estimate and asks first; resumable; run it once).
- [x] Layered retrieval (stub-first): concept stubs ranked by FTS + mention count, related concepts, then source excerpts via `Mentioned In` (`utils/brain_index.py`; `read_brain_source` for deeper reads). Still open: species/place alias table and species/year filters.
- [ ] Return about 8-12 ranked chunks with source id, title, year and the reason matched.
- [x] Evaluation set (`brain_meta/eval_questions.yaml`, 27 questions; run `python -m utils.brain_eval`). Re-run after every retrieval change. Its first run found that paper titles were not searchable, which led to the "documents with matching titles" section. Still to do: add questions from real use, and multi-concept questions.
- [x] Citations: author/year derived into the index (author for ~870 of 2,977 sources, year for ~2,120); answers cite inline plus a References list with source ids. The library spreadsheet (MID = source_id) now supplies authors, year, real title and publication (`python -m utils.brain_citations import`): 2,878 of 2,977 sources have an author and 2,855 a year. Still open: organization-as-author entries like "P. F. R. Office", and 69 sources with no sheet match (30 of the original 99 recovered by reading the MID from the filename suffix). The rest: 7 with an ID the sheet lacks and 62 archival letters/minutes/memos with no identifier; list them with `python -m utils.brain_citations unmatched`. All 69 now have citations recovered from the note text (`python -m utils.recover_citations`; `--report` lists 17 with no author, 2 with no year, 2 low-confidence). Nothing deleted.
- [x] Non-Minckley library additions: `python -m utils.pdf_ingest process` (text layer or OCR -> citation from DOI/Crossref, LLM first-page read, or filename -> note in `01_Sources` + `brain_meta/external_citations.json`). Tested on 2 PDFs (one text, one scanned). Concept stubs for new notes are updated automatically (so topic searches find them). New stubs get an LLM `## Summary` (estimate + consent). The agent checks `pdfs_to_process/` every minute and, on Enter/`ingest`, shows an estimated cost and asks before adding. Minckley PDFs keep their MID (filename or `--mid`; citation from the live sheet; note `source_id`/`minckley_id`; "Minckley Library ID: N" in `source_citation`); duplicates are rejected or confirmed; finished PDFs are deleted. Long documents (>150k characters) are flagged before OCR for a cap/full/skip choice. Still open: per-page OCR progress for big batches, reviewing a few filename-sourced citations.
- [ ] Embeddings only if the evaluation shows keyword search is missing too much.

- [ ] (low priority) Review the 69 recovered citations (`python -m utils.recover_citations --report`): fill in the 17 missing authors and 2 missing years where the original PDF is available, and check the Minckley-addressed letters and multi-organization authors.
- [ ] (low priority) Review the 27 Minckley MIDs that appear on more than one row (`brain_meta/minckley_duplicate_mids.csv`) and decide whether to split or merge them; the importer keeps only one row per MID.
- [ ] (low priority) Review the Minckley spell-check log (`brain_meta/minckley_spellfix_log.csv`, 148 changes) for wrong fixes (for example "Mexicao" to "Mexico"), and manually check scientific and author names, which the check skips.

### 2. `research_topic` tool
- [ ] Replace `search_fisheries_brain` with an evidence pack plus a coverage note ("matched N sources, showing M").
- [ ] System prompt rules: plain language, cite source ids, state gaps, no invented studies, keep brain evidence separate from general knowledge.
- [ ] Summarize-then-synthesize path when the evidence is too large, within a token budget.

### 3. `data_profile` tool (local, read-only)
- [ ] Report column names/types, row count, missing values, zero fraction and a rough overdispersion check for a project CSV.
- [ ] Send only the summary to the model; raw data stays local.

### 4. `plan_analysis` tool
- [ ] Inputs: goal, data profile, brain precedent (gear, effort standardization, model families).
- [ ] Saved plan: question, data used, model choice with cited justification, data checks, expected outputs, agent and arguments.
- [ ] State clearly when no available agent fits.
- [ ] Plan approval step before the existing run approval.

## Phase C: Agents, reports, routing

### 5. Consolidate specialized agents
- [ ] Rewrite `03_Specialized_Agents/*.py` (still the old generated-R versions) to use `r_templates/` and `utils/runner.py`.
- [ ] Each agent declares a description (data needed, assumptions, diagnostics) and a tool schema; the orchestrator loads them from a registry.
- [ ] Zero-inflated agent: diagnostics plot and model comparison (e.g. ZIP vs ZINB by AIC).

### 6. Report outline tool
- [ ] Draft sections, methods text based on brain precedent, and results placeholders filled from `runs/` outputs.
- [ ] Save as `.md` or `.qmd` after approval, with a reference list.

### 7. Router and conversation memory
- [ ] Keep message history; route requests as literature question, plan, run or file lookup.
- [ ] Allow several tool rounds per request (e.g. retrieve, profile, then plan).
- [x] Prompt slimming: manifest reduced to project name/path/format/habit (no file lists), Anthropic prompt caching on the system prompt, local keyword router picks the fast model for simple lookups, dropped turns kept as one-line session notes.
- [ ] Later: send only the tool schemas relevant to the route; tune `HEAVY_REQUEST` after real use; compare token use before and after.

## Packaging and quality
- [x] One-step launcher (`start.bat` / `start.py`) and hidden-input key setup (`setup_api_key.py`); needs a test on a clean Windows machine.
- [ ] File-lookup tools limited to registered project folders (`find_files`, `list_reports`, `read_report`).
- [ ] `verify_and_install_deps.py`: use the same Rscript lookup as `utils/runner.py` (R installed but not on PATH); consider a virtual environment.
- [ ] `requirements.txt` and a Windows launcher script.
- [ ] Self-test that makes a one-token API call and reports only success or failure (never prints the key).
- [ ] Tests (pytest) for `utils/safety.py`, manifest handling and the index.
- [ ] Release script that zips `fisheries_agent/` without `.env`, the manifest, `runs/` or `__pycache__`, and checks for key-like strings.
- [ ] Set `PYTHONUTF8=1` (or avoid emoji output) for SSH/redirected sessions on Windows.
- [ ] Verify the three R templates (`zinb.R`, `cjs.R`, `explore.R`) on a Windows machine; `cjs.R` initial-value handling is the least certain.

## ICM follow-ups
- [x] Roles and skill library: `skill_library/` (roles, `r-data-handling`, `mark-recapture-data-prep`), installer with hashes, `data_summary` interface, `load_role`/`summarize_project_data`/`check_r_package`/`search_methods_papers` tools.
- [x] Brain review step 1 (local, no LLM): `python -m utils.brain_methods scan|show` with `icm_templates/analysis_lexicon.yaml` -> `brain_meta/analysis_review.json` (28 analysis families, source counts, years, co-mentions).
- [x] Brain review step 2 tooling: `utils/skill_build.py estimate|draft|web` with `icm_templates/library_skills.yaml` (mark-recapture closed/open, count-glm, cpue-standardization, age-growth); web items verified (CRAN, Crossref) and kept separate from vault citations; consent before anything is sent.
- [x] Five analysis skills drafted (skill_library/skills/: mark-recapture-closed/open, count-glm, cpue-standardization, age-growth); all `status: draft`.
- [ ] Review the five drafts (check formulas, R workflow steps and the few `(unsourced)` lines) and mark each `status: reviewed`; the two mark-recapture-open gaps are now filled (see below). Original item: list analyses by data type and sampling design (needs structured extraction at ingest, estimate and consent), then draft analysis skills into `skill_library/skills/` using brain evidence plus web evidence (package docs, vignettes) with consent; keep web-derived claims marked.
- [x] Synthesis skill drafted: `scientific-writing-conventions` (reporting checklist from 55 recent brain notes + developer-written conventions; brain notes are summaries so cannot show prose style).
- [x] Synthesis skill Part C drafted from 13 articles in the gitignored `fisheries_agent/skill_source/` (`python -m utils.skill_source extract|estimate|draft`; specs `icm_templates/source_skills.yaml`, citations `icm_templates/skill_source_refs.yaml`; excerpts cut locally, only paraphrase and original code kept, excerpts never stored). Actual cost ~$0.43 for five drafts.
- [x] 2026-10-20: `mark-recapture-open` sections 'Assumptions and when to use open models' (Schwarz & Arnason 1996, Brownie 1993, Barbour 2013, Hewitt 2010) and 'Bayesian and software implementation' (NIMBLE paper, Calvert 2009, Royle 2009, Besbeas & Morgan 2014) drafted from `skill_source/` (specs `mark-recapture-open-assumptions`/`-bayesian` use a `skill:` key). The nimble CJS sketch is unexecuted; verify with R.
- [x] From `skill_source/`: new draft skills `r-data-exploration` and `telemetry-movement-habitat` (Rogers & White, Aarts, Fieberg); `SUPPLEMENT.md` for `count-glm` (developer's `fish_trapping_report_v8.qmd`, Fieberg) and `mark-recapture-open` (PIT detection/survival: Franssen, Buxton, Webber, Avery).
- [ ] Review these drafts, especially R sketches (R is not installed in the codespace, so no code was run) and the Part C tendencies (13 articles, mostly Southwest native fish; no per-journal claims).
- [ ] The Zuur & Ieno GLM book is licensed and forbids sharing, so it is NOT sent to an LLM (pointer citation only). If wanted, summarize it by hand or confirm terms permit LLM use. `skill_source/` also holds a stickleback 2009 paper (authors missing from the file), Seddon 2007 and Turner 2026 not used yet; `GLM_Chapter*.pdf` and the `.pptx` are unprocessed.
- [ ] Skill-defined run path: generic plan, approve, run for R code (Python is not used for analysis) through `utils/runner.py`.
- [ ] Review the hand-written data skills and mark them `status: reviewed`.
- [ ] Open the analysis set: `icm_skills` drafts from brain evidence only and `skills.yaml` lists a fixed set. Add (1) analysis discovery: search the brain for analyses used for a given data type and goal and propose skills for approval; (2) web evidence (CRAN/package docs, vignettes, methods papers) with consent, recorded as external references and marked as web-derived in the skill; (3) a package check (exists on CRAN, installed, approval before install); (4) a generic way to run skill-defined R code through `utils/runner.py` (plan, approve, run) instead of only the three fixed tools.
- [x] Phase 5 (maintenance): `icm_update --check`, `icm_seed new`, `utils/icm_maintain.py`, refresh tool reports new matches (see `ICMDevelopment.md`). Upstream contribution stays manual.
- [ ] Try the Phase 4 flows (create, restructure, validate, refresh, layered context) with a live model on a real project; tool functions in `main_orchestrator.py` have no direct tests yet.

## Future features
- [x] (done: once-a-minute check in the agent with consent prompt; see agents.md) Scheduled PDF processor: watch `00_Fisheries_Brain/pdfs_to_process/`, summarize new PDFs into `01_Sources/`, create context links between notes (reuse logic from the separate literature-conversion project). Until then, markdown files are added to `01_Sources/` and `02_Brain/` by hand.
- [ ] Reduce the number of notes in `02_Brain/` by merging them into one file per initial letter (`utils/stub_store.py`, ingest and index already use it). Remaining: after the next sync, run `python -m utils.stub_consolidate --apply --delete`, then commit. Optional later: rewrite source links to `[[Stubs_X#Name|Name]]` so Obsidian resolves them.
- [x] Project memory (`utils/project_memory.py`): per-project key files, notes and run history; tools `get_project_context`, `get_latest_results`, `remember_project_fact`; runs recorded automatically.
- [ ] Project memory, later: optional LLM one-line summaries of key files (with consent); index the scientist's own reports.
- [ ] macOS/Linux support (currently Windows only).

## Project pipelines (done, needs live trial)
- `utils/pipeline.py` + tools `check_pipeline`, `define_pipeline`, `run_pipeline`; skill `pipeline-orchestration`; data-handler asks how data arrives. Tested with stand-in scripts (R not installed here). Not built by design: FTP/uploads/credentials.
- Next: try on a real project with R; install a weekly schedule via `python -m utils.pipeline schedule`.

## New-analysis flow (done)
- `list_skills`/`read_skill` tools (workspace copy first, library fallback; skill list also in `get_project_context`), `profile_project_data` (R: `skill_library/scripts/profile_data.R`, CSV/Excel, one entry per sheet, writes `data_summary.*` next to the file), a "New analysis" routine in the system prompt, and a README "How a Project Works" section. R is now installed in the codespace, so the profiler is tested for real; model-written analysis scripts are not yet tried with a live model.
