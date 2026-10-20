---
name: pipeline-orchestration
description: Defines a project's pipeline.yaml (ordered R steps) so results and reports refresh automatically when the project's data changes.
status: draft
---
# pipeline-orchestration

Hand-written by the developers (not derived from the brain or the web). Review before marking `status: reviewed`.

## Idea
A project pipeline is a list of R scripts run in order. Python only checks what changed and runs the scripts (`utils/pipeline.py`); the analysis stays in R. The framework never stores FTP or other credentials: if data is downloaded from a server, the scientist's own script does that.

## When to offer one
- A project has more than one script run in a fixed order, or a report that should be rebuilt after the data changes.
- The data is refreshed from outside (downloaded, synced, exported) and results must follow.

## Building `pipeline.yaml`
1. Read the project's scripts and `data_summary.md` (via `get_project_context`, `list_project_files`, `read_project_file`). Work out which script reads which file and writes which.
2. Propose steps in running order: `id`, `script` (.R, .Rmd, .qmd), `inputs` (files or globs that, when their content changes, rerun the step) and `outputs` (files the step writes). Show the plan and get approval, then call `define_pipeline`.
3. Ask about data refresh during onboarding: "How does new data arrive (a download script, a synced folder, manual export)?" If there is a script, ask where it is, read it, and add it as a step with `kind: refresh` (it may be .R, .qmd or .py). It runs only when the scientist asks (`run_pipeline` with `include_refresh`), never automatically. Do not ask for passwords or server details.
4. Never list the raw data folder itself as an output. List real input files, so a change is detected by content, not by file dates.

## Using it
- `get_project_context` and `check_pipeline` report out-of-date steps and why. Tell the scientist and offer `run_pipeline`; it needs their approval.
- A failed step stops the chain. Report the error from the log, say which steps did not run, and do not claim the reports are current.
- Weekly runs: give the scientist the output of `python -m utils.pipeline schedule <project folder>`. It prints a Task Scheduler or cron line; the scientist installs it. A scheduled run never runs the refresh step unless `--refresh` is added to the command.

## Checks before running
- Scripts use paths relative to the project root; the pipeline runs them with the project as the working directory.
- Each script writes its outputs to the files listed under `outputs`, so a missing output marks the step out of date.
- Output files are not also listed as inputs of the same step.
