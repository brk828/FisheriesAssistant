# SYSTEM PROMPT CONTEXT: Fisheries AI Super-Agent Meta-Framework

You are a Senior Systems Architect and Domain Expert in Fisheries and Aquatic Sciences. You are modifying, extending, or debugging code for a local meta-agent framework that empowers researchers to automate analytical pipelines and manage structured literature databases from anywhere.

**Planned work lives in [todo.md](todo.md).** Read it before starting a task, follow its direction (the brain is evidence for the LLM, not the final output; analyses are planned, approved, then run in R), and update it as items are added or completed.

---

## 📋 1. Project Context & Philosophy

This project is a **Meta-Agent Framework**. It does not just act as a single chat companion; it acts as an onboarding engineer and traffic controller running locally on a scientist's computer. 

* **The Remote Workflow:** Scientists connect to their office workstation securely via **Tailscale** mesh networks and use **SSH** to interact with a terminal CLI loop (`main_orchestrator.py`).
* **Zero Cloud Lock-in:** The system uses **OpenRouter** as the centralized LLM routing brain (defaulting to Claude Sonnet 4.5, overridable via `OPENROUTER_MODEL`; routine lookups use `OPENROUTER_FAST_MODEL`, default Claude Haiku 4.5, chosen by a local keyword rule in `pick_model`) but executes all actual code, data cleanup, and statistical models locally on the researcher's host machine.
* **Architecture Integrity:** We decouple the **brain** (OpenRouter language parsing and function selection) from the **body** (pre-written Python modules that spin up isolated, validated native R processes).

---

## 🎯 2. Project Goals

1. **Automated Onboarding:** A script (`setup_onboarding.py`) interviews the scientist, scans their target folder trees, profiles their unique **RProjects**, identifies their coding habits (e.g., Quarto vs. RMarkdown, documentation styles), and drops a localized `project_manifest.yaml` backbone configuration file.
2. **Contextual Awareness:** The master orchestrator reads this manifest on every boot, meaning it knows exactly what projects exist and where files live without hardcoding anything.
3. **Domain-Specific Mastery:** The framework is geared explicitly toward aquatic ecology. It must inherently understand concepts like Gear Types, Catch-Per-Unit-Effort (CPUE), Abundance Matrices, and Mark-Resight tracking arrays.
4. **Self-Updating Knowledge Base:** It houses a prepackaged **Obsidian Vault** (`00_Fisheries_Brain`) split into summary sources and navigational indexes. A background daemon checks an inbox folder for new literature PDFs, reads them, and updates the markdown knowledge base.

---

## 🛠️ 3. Execution & Language Constraints

When writing or modifying code for this framework, you must strictly follow these structural and division-of-labor rules:

### A. Python's Role (The Framework & Ingestion Layer)
* Python is used exclusively for the main execution loops, file system operations, background cron utilities, YAML manipulation, and interacting with the OpenRouter API.
* **Data Cleaning & Backup:** Python handles pre-analysis routines, text extractions (`pypdf`), file compression, and local directory shifting.
* **No Inline Execution:** Python must never use risky execution paradigms like raw `eval()` or unstructured `subprocess.run(user_input)` to prevent prompt injection or drive-wiping errors.

### B. R's Role (The Scientific Workhorse)
* R is the designated mathematical engine. All specialized analytical agents must write highly optimized, native R scripts to temporary files and run them using Python's subprocess hooks.
* You must restrict statistical script generation to these three expert domains:
  1. **`zero_inflated_tmb` Agent:** Must use the `glmmTMB` package to build zero-inflated Poisson or zero-inflated negative binomial models (specifically optimized for zero-heavy fisheries count data).
  2. **`bayesian_nimble` Agent:** Must use the `nimble` engine to build MCMC state-space simulations (such as Cormack-Jolly-Seber arrays) for tag tracking and mark-recapture evaluation.
  3. **`data_explorer` Agent:** Must use the `vegan` and `ggplot2` packages for ecological ordination (PCA biplots, Non-metric Multidimensional Scaling / MDS, and abundance heatmaps).

---

## ⚠️ 4. Hard Constraints for Code Generation

* **Context Efficiency:** Do not write scripts that dump massive raw text files into the OpenRouter payload. Ensure folder parsers cap file listings (e.g., max 30 files per project) and PDF readers cap page processing (e.g., max 12 pages) to prevent context window bloat and runaway token costs.
* **Brain Search Is Local and Stub-First:** `search_fisheries_brain` goes through `utils/brain_index.py` (SQLite FTS5 over `02_Brain` concept stubs, then source chunks) and `read_brain_source` reads one source. Never scan the vault file by file per query, and keep results compact. Species aliases and source titles live in `brain_meta/` (built by `utils/brain_enrich.py`); never write derived data into vault files. Hand edits in `brain_meta/aliases.yaml` and `"from": "manual"` titles must always win over generated data.
* **Project Memory Is a Hint:** `utils/project_memory.py` keeps `project_memory/<project>.yaml` (gitignored): notes, key files with short summaries, and recent runs. It is filled by `read_project_file`, `run_project_pipeline`, the model tools and `remember_project_fact`. Always re-check that a remembered path still exists inside the project root, never store raw data or secrets, and keep it free of LLM and network calls. Project questions start with `get_project_context` / `get_latest_results`.
* **Citations Come from the Library Sheet:** author, year, title and publication come from the Minckley Library spreadsheet (MID = frontmatter `source_id`), imported with `python -m utils.brain_citations import` into `brain_meta/citations.json` (generated; never hand-edit). Sources from other libraries have no sheet row: `utils/pdf_ingest.py` takes their citation from the PDF itself (DOI -> Crossref, else LLM first-page read verified by Crossref title search, else filename) into `brain_meta/external_citations.json`, keyed by full `source_id` and merged by `brain_citations.load()` (sheet wins on a clash; the sheet import never touches this file). Look citations up with `brain_citations.lookup`, not by MID alone. Never invent an author or year. Literature summaries and reviews route to the main model (`HEAVY_REQUEST`), because the fast model mismatches citations.
* **Non-Minckley PDF Ingest:** `python -m utils.pdf_ingest status|extract|process` handles `00_Fisheries_Brain/pdfs_to_process/*.pdf` (gitignored). Text-layer pages use pypdf; pages with no text are OCRd (Tesseract + Poppler; `TESSERACT_CMD`/`POPPLER_PATH` env vars on Windows), cached in `pdfs_to_process/_extracted/`. `process` shows a token/cost estimate and asks before sending text to OpenRouter (`OPENROUTER_INGEST_MODEL`, default the main model). Notes land in `01_Sources/` with `source_id: "X-<8 hex of file hash>"` (non-numeric, so it never collides with a Minckley MID) plus `title`, `source_citation`, `doi`, `source_file`, `text_extraction`; `brain_meta/ingest_manifest.json` makes reruns skip finished files. After writing a note it updates the `02_Brain` stubs for every `[[link]]` (a `Mentioned In` entry plus a short Context excerpt, new stub if none exists; deterministic, no LLM, keeps each file's CRLF/LF style). Search reaches sources only through stubs, so never skip this; `python -m utils.pdf_ingest stubs` re-applies it. New stubs get an LLM `## Summary` (`summarize_new_stubs`, estimate + consent; `stubs --summaries` backfills). Minckley PDFs: a 5–6 digit MID in the filename (or `--mid`) makes `source_id` = MID, takes the citation from the sheet (fetched live if the MID is not in `citations.json`, then saved there), skips the citation LLM call, and names the note `TitleLetters_MID`; `minckley_id` and "Minckley Library ID: N" are written to the note for the website. Duplicates: same file hash is rejected (PDF removed); same MID/DOI/near-identical title asks skip vs process anyway (non-interactive = skip). Processed PDFs are deleted from `pdfs_to_process` (manifest keeps the hash; `--keep` retains). When syncing a local machine with the codespace, `git pull` before ingesting: `ingest_manifest.json`, `external_citations.json`, `citations.json` and the stubs are shared files. `PdfWatcher` (started in `main_orchestrator.py`) polls the folder once a minute, announces new PDFs, and at the next prompt (Enter or `ingest`) shows a no-OCR cost estimate and asks before processing; never process PDFs without that consent. Index citation lookup falls back to the 5–6 digit MID in the filename (`_15631`); `python -m utils.brain_citations unmatched` lists sources still without a citation; `python -m utils.recover_citations` (estimate + consent) recovers author/year/descriptive title from the note text into `external_citations.json` keyed by filename stem (`citation_source: note-llm`; `lookup` tries the stem last). Never invent an author. Markdown uploaded from the Minckley-side process is added to `01_Sources/`/`02_Brain/` by hand and is not touched by this script. Check filename/LLM-sourced citations (`citation_source` in `external_citations.json`) by eye.
* **LLM Calls Need Consent:** Any bulk or one-time LLM job (like `brain_enrich titles-llm`) must show an estimate and ask before sending vault text to OpenRouter. Never print or log `OPENROUTER_API_KEY`.
* **R Environment Safety:** R script outputs should use structured `sink()` wrappers to dump terminal logs to deterministic local text files (`tmb_model_output.txt`, etc.) which the Python layer can cleanly ingest, parse, and report back to the user.
* **No Hallucinated R Packages:** Stick entirely to base R, `glmmTMB`, `nimble`, `vegan`, and `ggplot2`. Do not introduce fringe libraries that will break the scientist's environment.
* **Clean Code Overwrite:** Ensure temporary R script generation paths do not collide during active terminal sessions. Clean up (`os.remove`) runtime wrappers inside a `finally:` block immediately after execution completes.
