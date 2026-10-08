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
    ├── 01_Sources (RAG)    ├── glmmTMB (Counts)    └── Local Scripts
    └── PDF Inbox Scanner   ├── NIMBLE (Bayesian)       (.R, .qmd, .Rmd)
                            └── vegan (Ordination)
```

## 📂 Core Folder Hierarchy

```text
fisheries_agent/
├── .env.template                # Placeholder config; copy to .env (never commit .env)
├── agents.md                    # Developer/system-prompt context for this framework
├── start.bat                    # One-step launcher (Windows): runs start.py
├── start.py                     # Runs dependency check, onboarding, key setup, then the orchestrator
├── setup_api_key.py             # Saves your OpenRouter key to .env from hidden input
├── verify_and_install_deps.py   # Checks and optionally installs Python/R dependencies
├── setup_onboarding.py          # Interactive system/project parsing script
├── main_orchestrator.py         # Master CLI gateway run over remote terminals
├── project_manifest.yaml        # Generated machine profile (DO NOT COMMIT)
├── 00_Fisheries_Brain/          # Prepackaged Obsidian-style Vault
│   ├── 01_Sources/              # Condensed markdown literature summaries
│   ├── 02_Brain/                # Concept stubs: summary, related concepts, "Mentioned In" source ids
│   └── pdfs_to_process/         # Background drop-box for new literature
├── brain_meta/                  # Derived search metadata (never edits the vault)
│   ├── source_titles.json       # Source id -> title (frontmatter, heading, citation, or LLM)
│   ├── aliases_auto.json        # Species name clusters built from the vault
│   └── aliases.yaml             # Your hand-edited alias groups and ignores (always win)
├── 03_Specialized_Agents/      # Expert mathematical code blocks
│   ├── bayesian_nimble.py       # Mark-resight and population models
│   ├── zero_inflated_tmb.py     # glmmTMB count regression models
│   └── data_explorer.py         # PCA, MDS, and multivariate visualization
├── r_templates/                 # Fixed R scripts; arguments are passed in, never generated as code
├── runs/                        # Per-run output folders and logs (created automatically)
└── utils/
    ├── safety.py                # Validates paths and column names from the model
    ├── runner.py                # Runs R/Quarto with timeouts, logging and key redaction
    ├── brain_index.py           # Local SQLite FTS5 index; stub-first search of the vault
    ├── project_memory.py        # Per-project memory (key files, notes, run history) in project_memory/<project>.yaml
    ├── brain_enrich.py          # Builds source titles and species aliases (optional LLM title pass)
    └── pdf_processor.py         # (future) Scheduled PDF-to-markdown job
```

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
python -m utils.brain_eval                                # run the retrieval test set (local, no LLM)
python -m utils.brain_enrich titles-llm --limit 20        # LLM titles for sources lacking one; shows a cost estimate and asks first
```
Fix a wrong or missing alias in `brain_meta/aliases.yaml`; a title can be set by hand in `source_titles.json` with `"from": "manual"`.

## 🔮 Future Features
* **Scheduled PDF processor:** a background job that watches `00_Fisheries_Brain/pdfs_to_process/`, summarizes new PDFs into `01_Sources/`, and creates context links between notes (reusing logic from a separate literature-conversion project). Until then, add markdown files to `01_Sources/` and `02_Brain/` by hand.
* **Project memory, next steps:** optional LLM one-line summaries of key files, and indexing the scientist's own reports (see `todo.md`).

## �💻 System Dependencies
Currently supported platform: **Windows**.
Ensure the host operating system has the following core binaries globally accessible:
* **Python 3.10+** (`openai`, `pyyaml`, `pypdf`, `python-dotenv`)
* **R Environment** (`glmmTMB`, `nimble`, `vegan`, `ggplot2`)
