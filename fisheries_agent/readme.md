# ⚓ Fisheries AI Super-Agent Meta-Framework

An intelligent, context-aware orchestrator framework designed specifically for **Fisheries and Aquatic Scientists**. This framework converts a local office computer into a terminal-accessible "super-agent" via secure Tailscale mesh connections and SSH, automating statistical workflows using native R and Python packages.

## 🐟 System Architecture Overview

The system operates via a master-orchestrator pattern powered by **OpenRouter (Claude 3.5 Sonnet)** that reads a localized, user-specific profile manifest to selectively route tasks to domain expert sub-agents or local workspace scripts.

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
fisheries_agent_workspace/
├── .env.template                # Empty shell configuration file
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
└── utils/
    └── pdf_processor.py         # Background daemon summarizing raw PDFs
```

## 🚀 Installation & Onboarding

### Phase 1: Machine Registration
Run the framework initialization wizard on the host machine to register active workspaces and analyze coding patterns:
```bash
python setup_onboarding.py
```

### Phase 2: Environment Provisioning
1. Duplicate the template file: `cp .env.template .env`
2. Open `.env` and fill in your unique OpenRouter key:
```env
OPENROUTER_API_KEY=sk-or-v1-...
```

### Phase 3: Remote Connection
Establish connectivity to your office machine using your **Tailscale** mesh IP address or node name:
```bash
ssh scientist@office-pc-alias
cd path/to/fisheries_agent_workspace
python main_orchestrator.py
```

## 💻 System Dependencies
Ensure the host operating system has the following core binaries globally accessible:
* **Python 3.10+** (`openai`, `pyyaml`, `pypdf`, `python-dotenv`)
* **R Environment** (`glmmTMB`, `nimble`, `vegan`, `ggplot2`)
