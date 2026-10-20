# Skill library

Prepackaged roles and skills, built here in the development repo and copied into each ICM workspace (`.agent/roles/`, `skills/`) by `python -m utils.skill_library install <workspace>`. Project execution then needs no network. Copies carry a content hash in `_library.json`, so `python -m utils.icm_maintain` can report when the library has a newer version.

- `roles/`: `data-handler`, `analyst`, `synthesist`. Plain Markdown prompts the primary agent adopts on request (for example "@analyst suggest a GOF test"); they are not separate programs.
- `skills/<name>/SKILL.md`: guidelines, formulas, packages and diagnostics for one task. `status: draft` until a person reviews it; `status: reviewed` protects it from regeneration.
- Interface: the data handler writes `data_summary.json` and `data_summary.md` (`python -m utils.data_summary <csv>`); the analyst reads them to recommend models.
- Analysis and synthesis skills are drafted from a brain review (see `todo.md`); the data skills and `scientific-writing-conventions` are mostly hand-written general conventions (the writing skill adds a reporting checklist counted from recent brain notes plus a Part C of style observed in developer-supplied articles).
- Skills drafted from the developer's gitignored `skill_source/` folder (`python -m utils.skill_source`) carry `[[src:id]]` citations listed in `SOURCES.md`; `SUPPLEMENT.md` extends an existing skill. Excerpts of those copyrighted documents are never stored in the library.
