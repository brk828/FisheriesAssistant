---
species: "Oncorhynchus tshawytscha"
common_name: "Chinook salmon"
family: "Salmonidae"
habitat: "Freshwater rivers (juvenile rearing and smolt migration); marine (adult phase)"
ocean_basin: "North Pacific"
location: "North Fork Lewis River, Washington, USA (Pacific coast of the United States and Canada context)"
tags: [ichthyology, marine-biology, salmonidae, mark-recapture, population-regression, river-flow, fisheries-management, statistics]
title: "Regression of abundance estimates from mark-recapture surveys against environmental covariates"
source_id: "PML2377"
marsh_id: "PML2377"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. R. Skalski (1996). Regression of abundance estimates from mark-recapture surveys against environmental covariates. Canadian Journal of Fisheries and Aquatic Sciences, Vol. 53. Marsh Library ID: PML2377."
source_file: "Skalski J.R. 1996. Regression of abundance estimates from mark recapture surveys against environmental covariates.pdf"
text_extraction: "text"
---
# Regression of Abundance Estimates from Mark-Recapture Surveys Against Environmental Covariates

#ichthyology #marine-biology #salmonidae

## Executive Summary

This methodological paper by [[John R. Skalski]] (published in the *Canadian Journal of Fisheries and Aquatic Sciences*, 1996) presents two alternatives for regressing abundance estimates from [[Mark-Recapture]] surveys against environmental covariates. The conventional approach uses [[Weighted Least Squares]] (WLS) on square-root-transformed abundance estimates. The alternative uses [[Maximum Likelihood Estimation]] (MLE) with [[Analysis of Deviance]] (ANODEV), which weights survey precision automatically and depends less on distributional assumptions.

Both methods are illustrated with eight brood years (1977–1979 and 1982–1986) of [[Chinook Salmon]] smolt production estimates from the North Fork Lewis River, related to spring river flow. The author recommends MLE with ANODEV for replicated mark-recapture studies, while noting that its computational demands are higher than those of WLS.

## Background & Description

**Study species.** Juvenile fall chinook salmon (*Oncorhynchus tshawytscha*) were tagged in spring with [[Coded Wire Tag]] (CWT) marks and recaptured as returning adults. The paper notes that about 43.6 million smolts were CWT-marked on the Pacific coast of the United States and Canada in 1990 alone (Johnson and Longwill 1991). CWT programs are used to estimate smolt production and survival and to compare stocks and hatchery rearing practices.

**Data source.** The Washington Department of Fisheries ran the tagging studies, with funding support from Pacific Power and Light Company and the [[Bonneville Power Administration]] (contract DE-B179-90BP02341). Table 1 lists, for each brood year, the number of smolts marked, adult captures examined for tags, mark-recaptures, abundance estimates (N̂), standard errors, coefficients of variation, and WLS weights. The raw table values are partly corrupted in the scanned text, so they are not reproduced here.

**Abundance estimation.** Each brood year is modeled as a single mark-recapture (Petersen-type) experiment with a multinomial likelihood. The author uses the [[Chapman Estimator]], a nearly unbiased modification of the [[Petersen Estimator]]. Variance is estimated following Seber (1982). The approximate sampling variance depends on N itself and on the per-period capture rates, so the estimates are skewed and heteroscedastic.

**Motivation.** The study aimed to help set flow management guidelines that protect salmon production. The paper deliberately ignores measurement error from tag loss and misclassification of spawners, which the author treats separately (Skalski 1989). The regression analyses are therefore presented "for illustrative purposes only."

## Ecological & Environmental Context

**Flow characterization.** The key covariate is river flow during the late spring to summer season (1 May–31 July). Flow was measured daily, giving roughly 85 days per season. Choosing among many possible summaries (minimum, maximum, mean, median, by season or month) makes a significant flow-production link almost guaranteed, a problem the author attributes to subjective selection.

**Objective smoothing.** Following [[Ronald Fisher]]'s 1924 solution, which analyzed 60 years of wheat yield at Rothamsted against rainfall, the daily series was smoothed into 5-day averages (17 periods, i = 0 to 16). Each season's trend was then fitted by polynomial regression on time:
- Linear: f_i = β0 + β1·t_i
- Quadratic: f_i = β0 + β1·t_i + β2·t_i²

The regression coefficients (β0, β1, and β2 where applicable) served as the flow covariates. Their fit was low in the linear model (r² from 0.050 to 0.830, mean 0.589), and the quadratic term raised average r² to about 0.66.

**Interpretation of flow coefficients.** β0 represents initial spring flow level, and β1 the rate of flow change over the season. These coefficients are negatively correlated, partly because of stable summer flows after the spring recession. The author notes that because the full population of daily flows was measured, these coefficients are descriptive quantities rather than estimates subject to sampling error, which is analogous to calculating the average grade of a fully surveyed road.

**Management implications.** The fitted surface can serve as a tool for balancing hydroelectric operations with salmon production. The author stresses adaptive management, because only a narrow range of flow conditions was observed in the data.

## Key Findings

1. **Both methods agree on the main relationship.** Smolt production responds to both the initial level and the rate of change of spring flow. Neither term alone is sufficient, which suggests that the "quantity and quality" of river flow jointly matter.

2. **WLS results.** Simple one-variable regressions were not significant (p > 0.10). The joint linear model was significant (P = 0.07) with multiple r² = 0.6582. The fitted model was N̂ = 936.5 + 0.277·β0 + 2.737·β1 (eq. 13, coefficients as transcribed from the scanned text). The quadratic model fit almost as well (r² ≈ 0.6732), so the linear component was judged adequate.

3. **MLE/ANODEV results.** Both slope and intercept were needed (P = 0.08). The quadratic term did not substantially improve fit (r² ≈ 0.6533, P = 0.20). The ANODEV F test for the linear flow model gave F = 4.5098 with P = 0.08 (Table 7). The chi-square test of homogeneous abundance across all eight surveys was rejected (χ² = 5993.9, P ≈ 0), which justified population-specific capture parameters.

4. **Model comparison.** Log-likelihoods ranged from about −113.9 (the most complex model) to about −130.2 (the simplest). Table 6 lists nine alternative models. The MLE fit closely matched the WLS predictions (Fig. 2).

5. **Robustness.** Results held across smoothing algorithms, including 3- and 5-day running medians and 10- and 15-day averages (Tukey 1977).

6. **Methodological comparison (Table 8).**
   - *WLS:* requires a square-root transformation, which induces an artificial curvilinear response; uses inversely proportional weights; relies on standard software and t/F tests.
   - *MLE/ANODEV:* uses original capture data, is self-weighting, relies on asymptotic chi-square and F tests, and needs custom programming (for example, FLETCHER or EXCEL, with GLIM-based tools suggested).

7. **Key conclusion.** MLE and ANODEV are recommended for analyzing replicated mark-recapture studies because they properly weight capture data and allow realistic response models independent of distributional assumptions. The author cautions that their advantage depends on correct specification of the mark-recapture model and that study design remains as important as analysis.

8. **Limitations.** The sample is only eight brood years, the observed flow range is narrow, and the response model includes only flow variables in a system where many environmental factors influence smolt output.