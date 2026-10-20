---
name: mark-recapture-data-prep
description: Rules for turning capture, contact or detection records into capture histories for mark-recapture models.
status: draft
---
# mark-recapture-data-prep

General conventions written by the developers, not derived from brain citations. Review before marking `status: reviewed`. Model choice belongs to the analyst and the mark-recapture skill.

## Inputs
One row per capture or contact: individual id (tag), date-time, site or reach, occasion info, and optionally length, weight, sex, tag type, recapture flag. Antenna or reader detections are contacts and need the same fields plus the reader id.

## Rules
1. **Individual id:** one row per fish-event keyed by tag. Resolve tag changes and double tags into one id (keep a crosswalk table); report tags seen once with a typo-like near match instead of merging silently.
2. **Occasions:** define occasions from dates before building histories (for example a sampling pass or a fixed window). Several captures inside one occasion collapse to one detection; report how many were collapsed.
3. **Capture history:** one row per individual, one column per occasion, coded 1 (detected) and 0 (not). Keep group or covariate columns (sex, size class, site) in a separate table joined by id.
4. **Order checks:** no recapture before the first capture; first-capture date equals the earliest event; flag individuals recorded after a recorded mortality or removal.
5. **Losses on capture and removals:** record them in their own column, not as zeros, because many models treat them differently.
6. **Effort:** keep effort per occasion (hours, net-nights, distance) in its own table; occasions without effort are not zeros.
7. **Closure window:** note the dates covered and any known immigration, emigration, mortality or recruitment, since this decides between closed and open models.

## Workflow in R
Read and clean with `r-data-handling`, build the occasion table, pivot detections to wide with `tidyr::pivot_wider(values_fn = ~ 1L, values_fill = 0L)`, check the history matrix (`rowSums`, occasions per fish), write `capture_histories.csv`, the covariate table, the effort table and the cleaning log, then summarize with `utils/data_summary.py`.

## Output for the analyst
Number of individuals, occasions, detections per occasion, recapture rate, groups and covariates, and the closure notes, all in `data_summary.json`.
