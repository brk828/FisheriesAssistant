---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [biostatistics, survival-analysis, kaplan-meier, clinical-methods, otolaryngology]
title: "A practical guide to understanding Kaplan-Meier curves"
source_id: "PML2195"
marsh_id: "PML2195"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. T. Rich, J. G. Neely, R. C. Paniello, C. C. J. Voelker, B. Nussenbaum, E. W. Wang (2010). A practical guide to understanding Kaplan-Meier curves. Otolaryngology-Head and Neck Surgery, 143(3), 331-336. Marsh Library ID: PML2195."
source_file: "Rich J.T et al. 2010. a practical guide to understanding kaplan meier curves.pdf"
text_extraction: "text"
---
# A Practical Guide to Understanding Kaplan-Meier Curves

#survival-analysis #biostatistics #kaplan-meier

## Executive Summary

This tutorial explains how [[Kaplan-Meier Curve|Kaplan-Meier (K-M) curves]] are generated, read and compared. It is a clinical biostatistics article, not an aquatic or fisheries study, so no species, habitat or location data apply. Its method is general: it models time-to-event data in which some subjects are [[Censoring|censored]] before the event occurs. The authors use two small hypothetical groups of six subjects each to show that comparisons must rest on the whole curve, not on isolated time points.

## Background & Description

- **Origin:** [[Edward L. Kaplan]] and [[Paul Meier]] published the foundational method in 1958 ("Nonparametric estimation from incomplete observations," *J Am Stat Assoc*).
- **Scope:** K-M estimates handle "survival" times that need not mean death. Examples in the text include cancer survival, tympanostomy tube duration, onset of hypocalcemia after parathyroid resection, and duration of nasal congestion after septoplasty. The method is also used in nonmedical fields.
- **Publication:** Otolaryngology–Head and Neck Surgery, Vol 143, No 3, September 2010, pp. 331–336 (invited article). Received April 17, 2010; accepted May 10, 2010.
- **Authors:** Jason T. Rich (major author), J. Gail Neely (major author and editor), Randal C. Paniello, Courtney C. J. Voelker, Brian Nussenbaum and Eric W. Wang, all from Washington University School of Medicine, St. Louis, MO.
- **Funding:** National Cancer Institute Cancer Center Support Grant P30 CA091842. Competing interests: none declared.

### Core Concepts

- **[[Serial Time]] vs. [[Calendar Time]]:** Serial time is the clinical-course duration for each subject, from a start point (enrollment or treatment start) to the event or censoring. Calendar time is the trial's real timeline, on which subjects enter at different points.
- **Three variables per subject:** serial time, status at end of serial time (1 = event, 0 = censored), and study group.
- **Censoring:** Censoring means the total survival time cannot be determined, for example because a subject drops out, is lost to follow-up, or the study ends before the event. Censoring can be within the study or terminal (at study end). The authors stress that a censored subject surviving one year does not have a one-year survival.
- **Intervals:** Only events define known survival intervals, drawn as horizontal lines. Censored subjects appear as tick marks and do not end an interval.

## Ecological & Environmental Context

Not applicable. The document does not address aquatic organisms, water chemistry, habitats or ecosystems. Its relevance to aquatic science lies only in the general statistical principle that it is a "nonmedical discipline" tool, which the text mentions without elaboration.

## Key Findings

### Method and Preparation

- Subjects are sorted by ascending serial time within each group, regardless of entry date.
- The input table can be built in Excel or Word and analyzed in programs such as SPSS, SigmaPlot or Origin. Statistical software performs the calculations within seconds.
- Because long durations can dominate means, the authors recommend medians and nonparametric tools.

### Worked Example (Hypothetical Five-Year Trial, Six Subjects per Group)

- **Group 1:** mean survival 3.25 years, median 3.0 years. One subject survived to the end of the study and was terminally censored. The cumulative survival probability at the last interval is 0.167.
- **Group 2:** median survival 1.0 year. The text gives a mean of 1.25 years, but the accompanying table reports 1.750. Group 2 had no remaining subjects after 3.5 years, and one subject was censored within the study.
- **Statistical comparison:** The text reports a log-rank p-value of 0.08 (not significant) in both the results and conclusion. The comparison section gives P = 0.80, which conflicts with this figure.

### Probability Calculations

- Interval survival rate = survivors past the interval divided by those at risk at its start.
- Cumulative probability = product of the interval survival rates up to that point. Example: 6/6 × 5/6 × 4/5 = 0.667 for group 1 in interval three.
- Censoring removes a subject from the denominator (those at risk) but does not change the survival probability directly. Censored subjects who coincide with an event are assumed to fall just after it.
- Extrapolation beyond the last observed time is not justified, since the subjects might have died shortly after.

### Comparing Curves

- The **[[Log-Rank Test]]** sums chi-square contributions across event times to compare full curves.
- The **[[Hazard Ratio]]** gives the relative event rate between groups, based on the full curve. Cox proportional hazards models give a similar comparison.
- Confidence intervals help visualize differences, but statistical significance requires a formal test.
- Small samples may lack the power to detect a real difference, which raises the risk of a [[Type II Error]] (false negative).

### Types of Endpoint in Oncology Literature

- **[[Overall Survival]]:** event is death from any cause.
- **[[Disease-Free Survival]]:** event is relapse. These curves lie below overall survival curves.
- **[[Progression-Free Survival]]:** event is disease progression (tumor growth or spread). Useful for isolating a treatment's effect on the disease.
- **[[Disease-Specific Survival]]:** event is death from the disease. These curves always lie above overall survival and can be misleading because deaths from treatment complications may be excluded.

### Pitfalls and Interpretation Guidelines

- Identify the event of interest and axis units first.
- Curves with many small steps usually reflect more subjects; curves with large steps reflect few subjects and are less accurate.
- A large number of censored subjects, especially early in the study, reduces reliability and should prompt questions about study conduct or treatment effects. Censored subjects should be shown as tick marks.
- Median survival can be read where the curve crosses 50 percent.
- Estimates at the far right of a curve are unreliable because few subjects remain. A cited example is a stage I lung cancer study of 302 patients with median follow-up of 40 months. One patient followed to 10 years produced a 92 percent survival estimate (95% [[Confidence Interval]] 88–95%) at 10 years. Carter and Huang showed that a single subsequent event would drop the estimate to 0 percent. Authors should report numbers at risk for each interval.

### Conclusion of the Article

The authors argue that the K-M method's "main focus is on the entire curve of mortality rather than on the traditional clinical concern with rates at fixed periodic intervals." Looking only at curve endpoints or isolated points can miss the real message.