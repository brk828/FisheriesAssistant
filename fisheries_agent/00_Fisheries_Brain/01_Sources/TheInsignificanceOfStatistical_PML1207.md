---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Jamestown, ND, USA (author affiliation); The Journal of Wildlife Management context
tags: [statistics, hypothesis-testing, wildlife-science, methodology]
title: "The insignificance of statistical significance testing"
source_id: "PML1207"
marsh_id: "PML1207"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. H. Johnson (1999). The insignificance of statistical significance testing. Journal of Wildlife Management 63(3):763-772. Marsh Library ID: PML1207."
source_file: "Johnson D.H. 1999. The insignificance of statistical significance testing.pdf"
text_extraction: "text"
---
# The Insignificance of Statistical Significance Testing

#ichthyology #marine-biology #statistical-methods

## Executive Summary

This methodological essay by Douglas H. Johnson (U.S. Geological Survey, Northern Prairie Wildlife Research Center) argues that [[Statistical Hypothesis Testing]] adds little value to wildlife research and is frequently misused and misinterpreted. The paper was prompted by a 1998 symposium at The Wildlife Society annual conference, where speakers were "virtually unanimous" that hypothesis testing was overused, misused, and often inappropriate. Johnson reviews the logic of [[P-Value]] interpretation, shows that P-values depend heavily on sample size and on arbitrary cutoffs, notes that point null hypotheses are almost always false, and critiques [[Power Analysis]]. He recommends [[Estimation and Confidence Intervals]], [[Decision Theory]], [[Model Selection]] and [[Bayesian Approaches]] as preferable alternatives.

Note: the document concerns statistical methods in wildlife science and contains no fish or aquatic species data.

## Background & Description

The paper is a commentary published in *The Journal of Wildlife Management* (63(3), 1999). Johnson notes that hypothesis testing in wildlife had grown sharply, and that the American Psychological Association had debated, but rejected, a ban on presenting such tests in its journals (Meehl 1997). The stated objectives are to describe hypothesis testing, discuss common misinterpretations of P-values, outline shortcomings, explain why tests are still used, and outline alternatives.

Johnson describes the four basic steps of hypothesis testing: (1) formulate a [[Null Hypothesis]], usually the opposite of the research hypothesis; (2) collect data by experiment or sampling; (3) compute a test statistic yielding a P-value; and (4) interpret the P-value relative to the null. He distinguishes deductive hypotheses derived from theory from statistical hypotheses describing population properties.

## Ecological & Environmental Context

The document does not address fish, aquatic species, or aquatic habitats. Its ecological examples are terrestrial or general wildlife cases, including:

- Coyote (*Canis latrans*) scat composition differing among seasons (P ≈ 0.03)
- Duckling flock mass differing among years (P < 0.0001)
- Density of bird trees greater in unlogged forest than in logged stands (P = 0.02)
- Lamb kill not correlated with trapper hours (r₁₂ = 0.50, P = 0.095)
- Viable seed counts and random snag slope effects reported as "no difference"

Johnson argues that in ecological systems "everything is connected to everything," so null hypotheses of no effect are almost always false given enough data. He also notes that a Type II error may be far more costly than a Type I error in ecological settings, citing an endangered species example and overharvest in marine fisheries leading to ecosystem collapse (Dayton 1998). These are cited as general arguments rather than fisheries data.

## Key Findings

- **P-values are sample-size dependent.** P can be made arbitrarily small by increasing sample size if the null hypothesis is false, which is almost always the case for point null hypotheses.
- **P-values are misinterpreted.** Four common interpretations (chance probability, reliability, error rate, probability the null is true) are each incorrect. Berger and Sellke (1987) gave an example where P = 0.05 corresponded to a probability of 0.52 that the null was true, with n = 50.
- **P-values depend on unobserved data.** P is the probability of observed or more extreme data given the null, and "more extreme" depends on the sampling plan and investigator intentions.
- **Arbitrary alpha cutoffs.** A fixed α = 0.05 creates an artificial distinction between P = 0.049 and P = 0.051.
- **Failing to reject is not proof.** Eight wildlife examples from the 1996 and 1998 issues treated non-significant results as proof of no effect, despite small samples, suggesting low power rather than true null hypotheses.
- **Power analysis is problematic.** Retrospective power analysis using observed effect sizes is misleading. Power analysis requires three arbitrary parameters (α, power, effect size).
- **Biological vs. statistical significance.** Non-significant unimportant differences and significant important differences are considered acceptable, while significant unimportant differences suggest the sample was too large and non-significant important differences suggest it was too small. Johnson calls this interpretation "schizophrenic."
- **Replication is the stronger criterion.** Johnson cites Fisher's view that solid knowledge comes from repeatedly obtaining significant results, and Shaver's view that the key question is whether an effect of important magnitude is consistently obtained across replications.
- **Scientific versus statistical hypotheses.** Scientific hypotheses are general and falsifiable, while statistical hypotheses about populations are local and usually known to be false in advance. Wildlife research rarely tests the former.
- **Reasons for continued use** (after Nester 1996): apparent objectivity, easy availability in software, habit, training, and journal demands. Johnson attributes heavy use to "physics envy."
- **Recommended alternatives:**
  - *Estimation and confidence intervals*: more informative than P-values; a 95% interval that includes zero implies P > 0.05.
  - *Decision theory*: weighs costs of Type I and Type II errors.
  - *Model selection*: information criteria such as Akaike's, with model averaging (Buckland et al. 1997; Burnham and Anderson 1998).
  - *Bayesian approaches*: yield credible intervals interpretable as the probability that the parameter lies in the interval, at the cost of requiring prior probabilities.
- **Conclusion.** Johnson argues that testing hypotheses, especially those known beforehand to be false, is "the most common and flagrant misuse of statistics" in the field. He calls for journal editors and referees to demand appropriate methods.