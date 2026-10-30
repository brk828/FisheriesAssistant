---
species: ["AGCH", "RHOS", "MEFU", "GIR", "TIC", "PACL", "CAIN", "GARF", "IECY", "AMNA", "CYCA", "PIPR"]
common_name: N/A
family: N/A
habitat: Freshwater streams and rivers (Aravaipa Creek, Gila River, San Pedro River)
ocean_basin: N/A
location: Arizona, USA
tags: [power-analysis, fish-monitoring, statistics, freshwater, arizona]
title: "Power Analysis of Fish Monitoring Data in Arizona"
source_id: "PML2911"
marsh_id: "PML2911"
library: "Marsh Library"
permission: "public domain"
source_citation: "J. R. Wilson (1995). Power Analysis of Fish Monitoring Data in Arizona. Department of Economics, Arizona State University, Tempe (supported by the U.S. Bureau of Reclamation). Marsh Library ID: PML2911."
source_file: "Wilson J.R. 1995, Power analysis of fish monitoring data in Arizona.pdf"
text_extraction: "mixed"
---
# Power Analysis of Fish Monitoring Data in Arizona

#ichthyology #marine-biology #freshwater-fishes

## Executive Summary

This Arizona State University economics report, funded by the [[Bureau Of Reclamation]], uses existing fish survey data to estimate the sample sizes needed to detect change in fish abundance. Its goal is to establish baseline data on the presence and distribution of fishes in the target reaches and to detect changes in species composition and abundance, with a statistical power of 0.80 at a significance level of α = 0.05. The analysis draws on two datasets: the [[Aravaipa Creek]] survey (1943–1990, three locations, 15 species) and the [[Gila River]] and [[San Pedro River]] survey (1991–1993, percent abundance). Both are analyzed with [[Analysis Of Variance]] and [[Mixed Effects Model]] frameworks, and the resulting error variances feed a [[Power Analysis]] table set. The report concludes that roughly 25 to 30 samples per species can detect a 25–30% change in relative abundance at about 80% power.

## Background & Description

The report sets out the statistical framework for fish monitoring:

- **Purpose:** Detect changes in fish species composition and abundance, with the null hypothesis that abundance does not change (in percent or absolute terms).
- **Error types:** A [[Type I Error]] (false detection of change) is controlled at α; a [[Type II Error]] (missed change) is β. Power is 1 − β.
- **Design:** Monitoring is a [[Repeated Measures Design]], which the authors treat as a mixed model with sites as fixed effects. Because species were not present in every period, the data are unbalanced.
- **Key assumption:** [[Compound Symmetry]] (a common correlation among repeated measures), which is required for the [[Randomized Block Design]] analogy.
- **Tasks:** (1) examine sample datasets, (2) evaluate sampling designs, (3) define statistical procedures for future analyses, (4) report, and (5) review.

The report notes that resampling the same sites (the paired t-test case) and reallocating sites randomly each period are two alternative designs. Resampling avoids inflation of error variance from natural spatial variability and is usually more compatible with other monitoring objectives.

## Ecological & Environmental Context

The report argues that fish abundance is hard to monitor accurately. Variability in mortality, growth, and reproduction, together with errors in stock assessment and sampling methods, makes change difficult to detect. Several power analyses cited in the report indicate that current population estimation methods have low power to detect significant changes in abundance. The authors recommend that monitoring be grounded in observed environmental sampling rather than purely theoretical models. A monitoring program should define a clear question, include a design phase and a [[Pilot Study]] to test equipment and sample size, and choose a robust analysis method early on.

## Key Findings

**Aravaipa Creek dataset** (three locations; 15 species, of which 7 were analyzed: AGCH, RHOS, MEFU, GIR, TIC, PACL, CAIN):

- **Count model:** Location effect p = 0.0362; species difference p = 0.0001.
- **Log-count model:** Location effect p = 0.0544; species difference p = 0.0001. The log is the canonical link for [[Poisson Distribution]] count data.
- Significant species differences appeared when abundances differed by roughly 59% to 65% or more, depending on the multiple comparison test used (α = 0.05).
- Location differences appeared at about 28% to 29% or more.
- Species grouping produced four groups: Group 1 (AGCH, PACL), Group 2 (CAIN, MEFU), Group 3 (GIR, TIC, RHOS), and a fourth group. Differences were significant between about 0.783 and 0.962 or more on the log scale.

**Gila River and San Pedro River dataset** (percent abundance, 1991–1993; 17 species, 8 with adequate data: AGCH, NOLU, GARF, PACL, IECY, AMNA, CYCA, PIPR):

- **Percent-abundance model:** Stream effect p = 0.0025; model fit p = 0.0009; model standard deviation 67.08.
- Stream differences were detectable for percent values of 26.04 or more (α = 0.05). Species differences were significant for changes greater than about 20%.
- **Square-root model:** Stream and species effects were significant (model fit p = 0.0001; model standard deviation 3.68). Mean square-root abundance was 4.0376, with a standard error of 3.525 and a significant difference of 5.7. Stream differences appeared above 1.42, and species differences ranged from 10.97 to 15.75 and above.
- The stream effect was significant in both models, but species effects were not uniform across all models.

**Power analysis:**

- The power of a test rises with sample size for a given percent change, and smaller changes require larger samples.
- Sampling at least 25 individuals per species detects a 30% change in relative abundance with power of about 0.80 (Table I).
- Sampling at least 25 individuals per species detects a 25% change with power of about 0.75–0.83 (Table II: n = 25 gives power 0.7542; n = 30 gives 0.8319).
- Table III (15% change, α = 0.05): n = 40 gives power 0.8060; n = 50 gives 0.8874.
- Table IV (10% change): n = 60 gives power 0.8328; n = 70 gives 0.8863.
- Table VII summarizes the 80% power scenarios: 3% change requires n = 320 (power 0.8097); 5% change n = 120 (0.7904); 10% change n = 60 (0.8328); 15% change n = 40 (0.8060); 25% change n = 30 (0.8319); 30% change n = 25 (0.8039).

**Methods and recommendations:**

- Sample size can be computed with [[Power Pack Software]], which runs iterative calculations. Power depends on sample size, type I error, and effect size, and any three determine the fourth.
- Multivariate responses use a [[Hotelling's T-Squared Test]] (F-approximation). Without error correlation, the multivariate test has no more power than a univariate test, and sample size grows roughly linearly with the number of response variables.
- Analyses were run in [[SAS PROC MIXED]] using maximum likelihood estimation with a compound symmetry covariance structure.
- The report uses α = 0.05 as the largest significance level at which the null hypothesis is rejected, but notes there is no common practice for choosing β.