# ⚓ Fisheries AI Super-Agent Meta-Framework

An intelligent, context-aware orchestrator framework designed specifically for **Fisheries and Aquatic Scientists**. This framework converts a local office computer into a terminal-accessible "super-agent" via secure Tailscale mesh connections and SSH, automating statistical workflows using native R and Python packages.

## 🐟 System Architecture Overview

The system operates via a master-orchestrator pattern powered by **OpenRouter** (default model Claude Sonnet 4.5; set `OPENROUTER_MODEL` in `.env` to change it). Simple lookups (project files, brain search) use a cheaper model, Claude Haiku 4.5 by default; requests to run, plan, interpret or compare use the main model. Set `OPENROUTER_FAST_MODEL` to change the cheaper one, or to `off` to always use the main model that reads a localized, user-specific profile manifest to selectively route tasks to domain expert sub-agents or local workspace scripts.

```text
                  [ Scientist via Tailscale/SSH ]
                                 │
                                 ▼
                     [ main_orchestrator.py ]
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
 📚 [ Fisheries Brain ]  📊 [ Specialized Agents ] 🛠️ [ RProjects ]
    ├── 01_Sources (Notes)  ├── glmmTMB (Counts)    └── Local Scripts
    └── PDF Inbox Scanner   ├── NIMBLE (Bayesian)       (.R, .qmd, .Rmd)
                            └── vegan (Ordination)
```

## 📂 Core Folder Hierarchy

```text
fisheries_agent/
├── .env.template                # Placeholder config; copy to .env (never commit .env)
├── AGENTS.md                    # Behavior guide for the installed agent (developer guide is the repo-root AGENTS.md)
├── start.bat                    # One-step launcher (Windows): runs start.py
├── start.py                     # Runs dependency check, onboarding, key setup, then the orchestrator
├── setup_api_key.py             # Saves your OpenRouter key to .env from hidden input
├── verify_and_install_deps.py   # Checks and optionally installs Python/R dependencies
├── setup_onboarding.py          # Interactive system/project parsing script
├── main_orchestrator.py         # Master CLI gateway run over remote terminals
├── project_manifest.yaml        # Generated machine profile (DO NOT COMMIT)
├── 00_Fisheries_Brain/          # Prepackaged Obsidian-style Vault
│   ├── 01_Sources/              # Condensed markdown literature summaries
│   ├── 02_Brain/                # Concept stubs in 27 files (Stubs_A..Z, Stubs_MISC): summary, related concepts, "Mentioned In" source ids
│   └── pdfs_to_process/         # Background drop-box for new literature
├── brain_meta/                  # Derived search metadata (never edits the vault)
│   ├── source_titles.json       # Source id -> title (frontmatter, heading, citation, or LLM)
│   ├── aliases_auto.json        # Species name clusters built from the vault
│   └── aliases.yaml             # Your hand-edited alias groups and ignores (always win)
├── 03_Specialized_Agents/      # Expert mathematical code blocks
│   ├── bayesian_nimble.py       # Mark-resight and population models
│   ├── zero_inflated_tmb.py     # glmmTMB count regression models
│   └── data_explorer.py         # PCA, MDS, and multivariate visualization
├── skill_library/               # Prepackaged roles, skills and scripts/profile_data.R (copied into ICM workspaces)
├── r_templates/                 # Fixed R scripts; arguments are passed in, never generated as code
├── runs/                        # Per-run output folders and logs (created automatically)
└── utils/
    ├── safety.py                # Validates paths and column names from the model
    ├── runner.py                # Runs R/Quarto with timeouts, logging and key redaction
    ├── brain_index.py           # Local SQLite FTS5 index; stub-first search of the vault
    ├── project_memory.py        # Per-project memory (key files, notes, run history) in project_memory/<project>.yaml
    ├── brain_enrich.py          # Builds source titles and species aliases (optional LLM title pass)
    ├── brain_citations.py       # Citations: Minckley sheet import + external (non-Minckley) citations
    ├── pdf_ingest.py            # PDFs -> notes: text/OCR, citation from the PDF, LLM synthesis
    └── pipeline.py              # Project pipelines: reruns stale R steps listed in pipeline.yaml
```

## 🧭 How a Project Works (User Experience)

The agent is a traffic controller: it gathers context, hands it to the language model, and has R do the work. Nothing is run until you approve it.

1. **Onboarding (once).** `start.py` checks dependencies, saves your OpenRouter key, and interviews you about your project folders. For a new project the agent builds an ICM workspace (`AGENTS.md`, `CONTEXT.md`, stage folders, brain-seeded references) and copies in the prepackaged roles and skills (`.agent/roles/`, `skills/`). Tell it the goal once ("manuscript on CPUE change between two locations") and it is remembered with the project.
2. **Say what you want.** For example "analyze the data". The agent reads the project context and goal, then follows its new-analysis routine:
   - **Skills:** `list_skills` / `read_skill` find the skills that match the data type and goal (for example `cpue-standardization`, `count-glm`). Skills marked `draft` are starting points and the agent says so.
   - **Data handler:** `profile_project_data` runs an R script that reads your CSV or Excel file (every sheet) and writes `data_summary.json` and `data_summary.md` next to it: columns, types, missing values, ranges, group counts and hints (effort/CPUE columns, zero-heavy counts, capture histories, dates). Needs R, `jsonlite`, and `readxl` for Excel; the agent asks before installing anything.
   - **Analyst:** the agent proposes a plan from the data summary and the skills (model, formulas, R packages, assumptions, diagnostics) and asks about anything the data cannot answer, such as which column marks the location.
3. **Approve and run.** You approve the plan; the agent writes the R script into the project, you approve the run, and results are reported from the saved output files (`runs/`). If the first script shows something unexpected about the data, the plan is adjusted rather than guessed.
4. **Write up.** `@synthesist` drafts methods and results text from the project's outputs, using the brain for literature and the writing-conventions skill. Every citation comes from the vault; missing ones are marked `[CITATION NEEDED]`.
5. **Keep it current.** A project can have a `pipeline.yaml`: ordered R steps that rerun only when their input files change. When you open a project and steps are out of date, the agent tells you and offers to run them. If your data comes from a download script of your own, point the agent to it and it is added as a refresh step that runs only when you ask. No FTP details or passwords are ever stored. For a weekly run, `python -m utils.pipeline schedule <project folder>` prints a Task Scheduler or cron line for you to install.

Roles you can call by name: `@data-handler`, `@analyst`, `@synthesist`. Role and skill content is in `skill_library/` and is copied into each workspace; your local edits are never overwritten, and `icm_maintain` reports library updates. Analyses are always R; Python only runs the agent and the pipeline engine.

## 🚀 Installation & Onboarding

### Quick start (Windows)
With Python 3.10+ installed, double-click `start.bat` (or run it from a terminal). It checks dependencies, runs onboarding, saves your OpenRouter key from hidden input, then launches the orchestrator. The steps below describe what each part does and how to run it on its own.

### Phase 1: Dependency Check
```bash
python verify_and_install_deps.py
```

### Phase 2: Machine Registration
Run the framework initialization wizard on the host machine to register active workspaces and analyze coding patterns:
```bash
python setup_onboarding.py
```

### Phase 3: Environment Provisioning
Easiest: `python setup_api_key.py` and paste the key when asked. Input is hidden, and the key is saved only to `.env` (never displayed or logged).

Or do it by hand:
1. Duplicate the template file: `copy .env.template .env`
2. Open `.env` in your own editor and fill in your OpenRouter key (never commit or share this file):
```env
OPENROUTER_API_KEY=sk-or-v1-...
```

### Phase 4: Remote Connection
Establish connectivity to your office machine using your **Tailscale** mesh IP address or node name:
```bash
ssh scientist@office-pc-alias
cd path/to/fisheries_agent
python main_orchestrator.py
```

## � Run Approval
Every analysis run is shown to you (tool name and arguments) and only starts after you answer `y`. Outputs and logs are saved under `runs/`.

## 📚 Fisheries Brain Search
`search_fisheries_brain` is stub-first and runs locally (no tokens until results reach the model):
1. Concept stubs in `02_Brain` are matched and ranked (text match, title match, number of sources mentioning the concept) and returned with summaries, related concepts and source ids.
2. Source excerpts follow, preferring sources linked from the matched stubs. `read_brain_source` reads the best passages of one source by id.
3. Source titles are searched too, so a question naming a paper finds it directly.
4. Every source comes with a ready-made citation line, `Author (Year). Title. Publication. [source id]`, plus an inline form such as `(Mueller 1994)`. The data comes from the library spreadsheet (MID = the source's `source_id`), imported into `brain_meta/citations.json`; where the sheet has no entry, author and year fall back to frontmatter or the file name. `read_brain_source` also accepts a concept name. Answers cite inline as (Author, Year) and end with a References list that keeps the source ids.
5. Known species names are expanded with their aliases (e.g. squawfish / Colorado pikeminnow / *Ptychocheilus lucius*), and the result says what was expanded.

The index (`.brain_index.sqlite`, gitignored) builds automatically on first use (~15 s) and whenever vault files, titles or aliases change. Maintenance commands, run from this folder:
```bash
python -m utils.brain_index "razorback sucker spawning"   # try a search without the agent
python -m utils.brain_enrich                              # rebuild titles and aliases (local only)
python -m utils.brain_citations import                  # refresh authors/years/titles from the library spreadsheet
python -m utils.pdf_ingest stubs                        # re-apply concept-stub updates for ingested notes
python -m utils.pdf_ingest status                       # PDFs waiting in pdfs_to_process (extract = text/OCR + citation only; process = notes, asks before sending text)
python -m utils.brain_eval                                # run the retrieval test set (local, no LLM)
python -m utils.brain_enrich titles-llm --limit 20        # LLM titles for sources lacking one; shows a cost estimate and asks first
```
Fix a wrong or missing alias in `brain_meta/aliases.yaml`; a title can be set by hand in `source_titles.json` with `"from": "manual"`.

### Additive RAG pilot

The optional RAG export is a **derived release artifact**, not a replacement for the vault or the default stub-first search. Markdown remains authoritative. PDF ingestion, stubs, existing skills and R execution are unchanged. Project literature stays private and continues to use whole-document Markdown references; long references should be read in bounded sections rather than injected wholesale into a prompt.

The first milestone exports only explicitly approved library notes and returns separate **methodological** and **biological** evidence packs. It does not create or execute sub-agents. Method queries should describe the goal, data and sampling design (for example CPUE standardization or zero-heavy counts). Biological queries should identify the species, parameter and relevant population, life stage, location, season and units.

Retrieved passages are untrusted evidence, not instructions. Method applicability, formulas, R implementations and biological values still require scientific review. A genus-level range must not silently become a species-specific rule; empirical ranges normally flag plausibility concerns, not automatic rejection. Delta/hurdle and zero-inflated models are distinct, and no package is mandated solely by a retrieval match. Condensed notes cannot establish details omitted from the original publication.

No source is approved by default. Approval must establish finalization, a redistribution basis, an exact document hash and whether evidence is a condensed note or has been checked against the original. Copyrighted/private material, project PDFs and developer `skill_source/` documents must not be automatically included. The embedding model also needs a redistribution license and a fixed revision.

#### Build and query an approved export

Commands below run from the installed `fisheries_agent` folder; replace `/absolute/...` with your own absolute paths (on Windows, use absolute drive paths and your shell's JSON quoting).

1. Copy `brain_meta/rag_sources.example.yaml` to a local approval file. Its empty allowlist exports **no documents**. For each selected note, fill in its exact path, current SHA-256, `review_finalized`, redistribution approval/basis, `evidence_level`, allowed `tracks`, and reviewed species labels for biological retrieval. The only eligible source directory is the framework's `00_Fisheries_Brain/01_Sources`; project directories and stubs are not eligible.
2. Build a new artifact directory; existing destinations are never overwritten:
   ```bash
   python -m utils.rag_library build --config /absolute/approved-sources.yaml --destination /absolute/rag_artifacts/pilot-v1
   ```
   Without an `embedding` configuration this creates a portable lexical-only export using existing dependencies. Source snapshots, heading-aware bounded chunks, canonical citation lookup results, approvals and checksums are retained. Unknown citations stay explicitly unverified; IDs and filenames are kept separately.
3. Query the exported records, without consulting the live vault:
   ```bash
   python -m utils.rag_library query --artifact /absolute/rag_artifacts/pilot-v1 --mode lexical --request '{"track":"methodological","goal":"CPUE standardization","data":"catch counts and effort","design":"repeated sampling","methods":"delta hurdle and zero-inflated models"}'
   python -m utils.rag_library query --artifact /absolute/rag_artifacts/pilot-v1 --mode lexical --request '{"track":"biological","species":"Xyrauchen texanus","parameter":"annual natural mortality","population":"study population","life_stage":"adult","region":"study region","season":"annual","units":"per year"}'
   ```
   Results are JSON evidence leads, not generated profiles or extracted parameter bounds. The methodological context fields are `goal`, `data`, `design`, `methods`; biological fields are `species`, `parameter`, `population`, `life_stage`, `region`, `season`, `units`. Biological searches require both species and parameter, using explicit approved species labels and reviewed aliases, never automatic genus broadening. Unmatched sources produce an empty evidence pack. Missing population/unit agreement and unresolved conflicts require human review. `--limit` (1–12) and `--max-chars` bound output.

#### Optional local semantic retrieval

Install the separately pinned `requirements-rag.txt` only when opting into the semantic backend, in a dedicated Python 3.10–3.12 environment. The standard agent installation does not require it. Installation can require internet access; runtime retrieval must not.

The approval file's commented `embedding` example requires an **already available** local SentenceTransformer, its exact revision, license and redistribution approval, plus hashes for every required model file. A mandatory `license_file` must identify an allowlisted, nonempty UTF-8 license text; include all required NOTICE and attribution files too. Only approved non-executable model files are copied into the artifact; remote code and pickle model weights are excluded. The builder never downloads a model. Acquire and review a suitable licensed model separately before building; absent weights cause failure rather than a network fetch. These checks record approval, not a legal determination of compliance.

Semantic exports persist a Chroma collection and include packaged vectors, source snapshots and model files. Queries use LlamaIndex retrieval over an ephemeral local Chroma collection populated from those vectors: the shipped persistent database is never opened for writing. This protects the artifact but adds startup time/memory; it is a pilot design, not a large-corpus performance claim. Manifest checks enforce the original embedding files/settings and compatible recorded runtime versions; there is no implicit rebuild. Checksums detect accidental changes, **not an untrusted publisher**.

Semantic relevance filtering is an uncalibrated pilot heuristic. Nearest-neighbor scores do not establish scientific support, even when a passage is returned; evaluate false positives and abstention with the chosen model and corpus.

**Not release-validated:** no real embedding-model integration or clean Windows installation has been exercised. In particular, stopping Chroma may leave native file handles open on Windows and prevent the builder's final directory rename. Validate that publication path before distributing a semantic artifact; lexical exports do not open Chroma.

`--mode semantic` requires the optional backend and performs semantic-plus-lexical retrieval. The default `--mode auto` attempts it and reports lexical fallback when setup is absent/incompatible; `--mode lexical` never loads embeddings. Only use artifacts and models from a trusted publisher, locally; do not expose a Chroma server or use untrusted database files.

**Dependency choice:** the optional backend pins Chroma 0.4.16, outside the reported affected ranges of the server authorization/code-injection advisories found during implementation. A small LlamaIndex vector-store bridge avoids the official adapter's requirement for affected releases; NumPy is pinned for compatibility. This is a constrained pilot environment, not a recommendation to deploy an old Chroma server. Reassess advisories and compatibility before any wider deployment.

#### Evaluate the pilot

```bash
python -m utils.rag_eval /absolute/rag_artifacts/pilot-v1 --mode lexical
python -m utils.rag_eval /absolute/rag_artifacts/pilot-v1 --mode hybrid
```

The evaluator combines `brain_meta/eval_questions.yaml` with `brain_meta/rag_eval_questions.yaml` (or repeat `--file /absolute/questions.yaml` for custom sets). It reports legacy stub-first source hits versus exported retrieval, explicit abstention cases, latency, artifact size and evidence IDs for manual review. Hybrid evaluation requires a semantic artifact/backend and fails rather than silently substituting lexical results. The legacy baseline can build its existing local SQLite index; the RAG artifact stays read-only.

**Compare corpus coverage before interpreting scores:** baseline searches the full vault, while RAG sees only approved sources. Missing gold sources may reflect export scope, and concept-only legacy questions require manual assessment. Retrieval hits are not proof that a formula, citation or biological threshold is correct. No production corpus or embedding model is shipped by this pilot.

Release acceptance requires a clean Windows offline-installation trial and comparison against the current retrieval evaluation set, supplemented by CPUE/count-method and biological-constraint questions. Measure relevant-source recall, citation accuracy, appropriate abstention, latency and artifact size; manually check claim support and conflicting studies. Only then connect the evidence packs to reviewed Markdown analyst/validator skill drafts, keeping project drafts separate from upstream releases.

## ICM Workspaces
Projects can be staged ICM workspaces (`AGENTS.md`, `CONTEXT.md`, stage folders, brain-seeded references and skills). A workspace is linked from `project_manifest.yaml` through `icm_workspace`, and the agent loads it in layers: `get_project_context` returns `AGENTS.md` and `CONTEXT.md`, plus one stage contract when a stage is asked for. Ask the agent to create a project, restructure project X, validate project X or refresh its references; creating and restructuring ask their questions in the terminal. Onboarding offers to restructure each selected project, and the original is never changed. Before a script runs, linked data files are checked against `data/manifest.yaml` and you are asked if any changed. Standalone commands: `python -m utils.icm_wizard`, `icm_restructure`, `icm_validate`, `icm_seed`, `icm_skills`, `icm_data`.

## 🔮 Future Features
* **Scheduled PDF processor:** `utils/pdf_ingest.py` already converts PDFs from `00_Fisheries_Brain/pdfs_to_process/` into `01_Sources/` notes on demand (OCR where needed, citation read from the PDF). It also updates the `02_Brain/` concept stubs so the new notes are searchable. The running agent checks the folder every minute and, on Enter or `ingest`, shows an estimated cost and asks before adding new PDFs. Markdown from the Minckley process is added to `01_Sources/` and `02_Brain/` by hand.
* **Project memory, next steps:** optional LLM one-line summaries of key files, and indexing the scientist's own reports (see the root `todo.md`).

## �💻 System Dependencies
Currently supported platform: **Windows**.
Ensure the host operating system has the following core binaries globally accessible:
* **Python 3.10+** (`openai`, `pyyaml`, `pypdf`, `python-dotenv`; PDF ingest also `pdf2image`, `pytesseract`)
* **Tesseract OCR and Poppler** (only for scanned PDFs in `pdf_ingest`); `verify_and_install_deps.py` checks for them and offers to install via winget, Homebrew or apt
* **R Environment** (`glmmTMB`, `nimble`, `vegan`, `ggplot2`)
