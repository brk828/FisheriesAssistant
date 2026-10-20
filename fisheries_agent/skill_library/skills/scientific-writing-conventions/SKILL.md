---
name: scientific-writing-conventions
description: Conventions and a reporting checklist for methods, results and report text written from project outputs and vault evidence.
status: draft
---
# scientific-writing-conventions

Part A is a reporting checklist informed by a count over the brain's recent source notes. Part B is general convention written by the developers; it is not derived from the brain. Part C is style observed in 13 developer-supplied articles (paraphrased; see SOURCES.md). Review before marking `status: reviewed`.

## Limits of the evidence
- Brain source notes are template summaries, not article prose, so they cannot show writing style. They only show which items a study reports.
- Only 55 of 3,768 notes are dated 2000 or later; treat the counts below as a rough guide.
- Among those 55 notes, the share mentioning each item: sampling design, effort or gear 34; uncertainty (CI, SE, credible interval) 22; stated assumptions 17; software or R 16; diagnostics or goodness of fit 15; limitations 15; sample size 14; model selection (AIC, BIC) 10; data or code availability 6. Items rarely mentioned (availability, model selection) are worth stating anyway.

## Part A. Reporting checklist
Methods: study area and period; sampling design, gear and effort; sample sizes per stratum; data cleaning steps and exclusions; model, software and package versions; assumptions and how they were checked; model selection approach.
Results: sample sizes first; estimates with uncertainty (interval type named); diagnostics or fit results; negative or null results stated as such.
Discussion: assumptions that may be violated; limitations; management relevance only where results support it.
Availability: where data and code live, or why they are not shared.

## Part B. General conventions (developer-written)
- Past tense for what was done and found; present tense for established facts and for what a table or figure shows.
- One main idea per paragraph; lead with the point, then the evidence.
- Define each abbreviation and symbol at first use; use one term per concept throughout.
- Report numbers with consistent precision, units, and the interval type (for example, "95% CI"); do not report more digits than the data support.
- Describe effect size and uncertainty, not only significance.
- Say what each table and figure shows in the text; every figure and table is cited in the text.
- Separate results from interpretation; avoid causal wording unless the design supports it.
- Cite inline (Author year); never cite a source that was not read or that is not in the vault or reference list.

## Part C. Style from journal articles

Observed in 13 articles the developer supplied (listed in `SOURCES.md`; mostly Southwest U.S. native-fish work, plus two methods papers and one non-fish telemetry paper). Descriptions are paraphrased; example frames are original. These are tendencies of this sample, not rules. Check the target journal's author guidelines first. Status: draft, reviewed by no one yet.

### Structure
- Full articles follow Introduction, Methods, Results, Discussion; short management briefs condense these [[src:buxton-2025]] [[src:webber-2014]].
- Abstracts state the objective, the approach, key quantitative results and a management implication [[src:franssen-2021]] [[src:archdeacon-2024]] [[src:buxton-2025]].
- Methods open with the study area (location, landmarks, physical setting), then topical subsections such as collections, design, laboratory work and statistical analysis [[src:franssen-2021]] [[src:webber-2014]] [[src:avery-2011]] [[src:murie-2009]] [[src:walsworth-2020]].
- Results often open with sample sizes and descriptive statistics, and subsection headings tend to mirror those in Methods [[src:franssen-2021]] [[src:archdeacon-2024]] [[src:murie-2009]] [[src:walsworth-2020]].
- Discussions usually restate the main finding against the objective, then interpret mechanisms, compare with other studies, and close with management implications [[src:franssen-2021]] [[src:archdeacon-2024]] [[src:walsworth-2020]] [[src:friesen-2026]].

### Tense and voice
- Past tense for what was done and found; present tense for standing facts about the system or species and for general statements in the Discussion [[src:franssen-2021]] [[src:avery-2011]] [[src:archdeacon-2024]] [[src:murie-2009]].
- First-person plural ("we") is common in Methods and Results.
- Frame: "We collected N fish at [site] between [dates]." Frame: "[Treatment] increased [metric] from X to Y (95% CI = a-b)."

### Statistical reporting
- Test statistics, degrees of freedom and P values sit inside the sentence; point estimates are followed by an interval whose type is named [[src:franssen-2021]].
- Model selection is summarized in a table of information-criterion values, differences and weights, with model-averaged estimates in text or figures [[src:franssen-2021]] [[src:walsworth-2020]].
- Sample sizes are given in parentheses next to the result [[src:franssen-2021]] [[src:leonard-2025]].
- Software and packages are named where the method is described [[src:aarts-2008]].

### Figures and tables
- Captions are standalone: they state what is shown, the unit of analysis, sample size, and what error bars or bands represent [[src:franssen-2021]] [[src:buxton-2025]].
- Multi-panel figures label panels with lowercase letters [[src:nowlin-2006]].
- Caption placement and format follow the journal template (general).

### Abbreviations, names and units
- Abbreviations are defined at first use and used consistently (for example length types and PIT tags) [[src:franssen-2021]] [[src:buxton-2025]] [[src:webber-2014]].
- The common name is given with the scientific name at first mention [[src:murie-2009]] [[src:franssen-2021]].
- Metric units; river position given in river kilometers where relevant [[src:franssen-2021]] [[src:leonard-2025]].

### Hedging
- Inference from indirect evidence is hedged with modal verbs and phrases such as "may", "likely", "we believe", "appears" [[src:avery-2011]] [[src:webber-2014]] [[src:leonard-2025]] [[src:franssen-2021]].
- Non-detection is described as non-detection, with extirpation only "presumed" [[src:leonard-2025]].

### Gaps
- The sample is small and regional; per-journal differences could not be established, so none are claimed.
- Use of the Everglades, Mediterranean and lake studies as style models is untested.

## Rules for the agent
- Take numbers only from `runs/` outputs or project files; otherwise write `[RESULT NEEDED]`.
- Use `[CITATION NEEDED]` rather than guessing a reference.
- Label vault evidence, project results and general knowledge separately.
