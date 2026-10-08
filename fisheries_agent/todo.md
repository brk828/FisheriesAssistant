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
- [ ] Parse front matter and split notes into heading-level chunks.
- [ ] Build a SQLite FTS5 index (fields: species, habitat, year, source id, chunk text); rebuild only when files change.
- [ ] Alias table for common/scientific names and place names (e.g. razorback sucker / *Xyrauchen texanus*, Colorado squawfish / pikeminnow).
- [ ] Layered retrieval: species/location/topic filters, rank chunks matching several, follow wikilinks from `02_Brain` concept notes.
- [ ] Return about 8-12 ranked chunks with source id, title, year and the reason matched.
- [ ] Evaluation set of 15-20 questions with expected sources (e.g. razorback sucker in Lake Mohave); re-run after every retrieval change.
- [ ] Embeddings only if the evaluation shows keyword search is missing too much.

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

## Future features
- [ ] Scheduled PDF processor: watch `00_Fisheries_Brain/pdfs_to_process/`, summarize new PDFs into `01_Sources/`, create context links between notes (reuse logic from the separate literature-conversion project). Until then, markdown files are added to `01_Sources/` and `02_Brain/` by hand.
- [ ] Reduce the number of notes in `02_Brain/` by merging them; rely mainly on source chunks, with concept notes as the link graph.
- [ ] Project memory: index the scientist's own reports in registered projects (optional).
- [ ] macOS/Linux support (currently Windows only).
