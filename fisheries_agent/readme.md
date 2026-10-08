# ⚓ Fisheries AI Super-Agent Meta-Framework

An intelligent, context-aware orchestrator framework designed specifically for **Fisheries and Aquatic Scientists**. This framework converts a local office computer into a terminal-accessible "super-agent" via secure Tailscale mesh connections and SSH, automating statistical workflows using native R and Python packages.

## 🐟 System Architecture Overview

The system operates via a master-orchestrator pattern powered by **OpenRouter** (default model Claude Sonnet 4.5; set `OPENROUTER_MODEL` in `.env` to change it) that reads a localized, user-specific profile manifest to selectively route tasks to domain expert sub-agents or local workspace scripts.

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
├── verify_and_install_deps.py   # Checks and optionally installs Python/R dependencies
├── setup_onboarding.py          # Interactive system/project parsing script
├── main_orchestrator.py         # Master CLI gateway run over remote terminals
├── project_manifest.yaml        # Generated machine profile (DO NOT COMMIT)
├── 00_Fisheries_Brain/          # Prepackaged Obsidian-style Vault
│   ├── 01_Sources/              # Condensed markdown literature summaries
│   ├── 02_Brain/                # Synthesized catalogs, indices, and concepts
│   └── pdfs_to_process/         # Background drop-box for new literature
├── 03_Specialized_Agents/      # Expert mathematical code blocks
│   ├── bayesian_nimble.py       # Mark-resight and population models
│   ├── zero_inflated_tmb.py     # glmmTMB count regression models
│   └── data_explorer.py         # PCA, MDS, and multivariate visualization
├── r_templates/                 # Fixed R scripts; arguments are passed in, never generated as code
├── runs/                        # Per-run output folders and logs (created automatically)
└── utils/
    ├── safety.py                # Validates paths and column names from the model
    ├── runner.py                # Runs R/Quarto with timeouts, logging and key redaction
    └── pdf_processor.py         # (future) Scheduled PDF-to-markdown job
```

## 🚀 Installation & Onboarding

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

## 🔮 Future Features
* **Scheduled PDF processor:** a background job that watches `00_Fisheries_Brain/pdfs_to_process/`, summarizes new PDFs into `01_Sources/`, and creates context links between notes (reusing logic from a separate literature-conversion project). Until then, add markdown files to `01_Sources/` and `02_Brain/` by hand.
* **Smaller Brain:** consolidate the many notes in `02_Brain/` into fewer, richer notes, and add a search index, for faster lookups.

## �💻 System Dependencies
Currently supported platform: **Windows**.
Ensure the host operating system has the following core binaries globally accessible:
* **Python 3.10+** (`openai`, `pyyaml`, `pypdf`, `python-dotenv`)
* **R Environment** (`glmmTMB`, `nimble`, `vegan`, `ggplot2`)
