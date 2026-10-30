---
species:
  - Peromyscus leucopus
  - Microtus pennsylvanicus
  - Sterna dougalii
common_name:
  - White-footed Mouse
  - Meadow Vole
  - Roseate Tern
family: N/A
habitat: Lowland hardwood forest; old-field habitat; breeding colonies (Roseate Tern, mentioned as an example)
ocean_basin: N/A
location: Patuxent Wildlife Research Center, Maryland, USA
tags:
  - capture-recapture
  - temporary-emigration
  - robust-design
  - population-ecology
  - statistical-ecology
title: "Estimating temporary emigration using capture-recapture data with Pollock's robust design"
source_id: "PML1270"
marsh_id: "PML1270"
library: "Marsh Library"
permission: "not public domain"
source_citation: "W. L. Kendall, J. D. Nichols, J. E. Hines (1997). Estimating temporary emigration using capture-recapture data with Pollock's robust design. Ecology, vol. 78, no. 2, pp. 563-578. Marsh Library ID: PML1270."
source_file: "Kendall W.L. et al. 1997. Estimating temporary emigration using capture recapture data with pollock's robust design.pdf"
text_extraction: "text"
---
# Estimating Temporary Emigration Using Capture-Recapture Data with Pollock's Robust Design

#mammalogy #cricetidae #rodentia #capture-recapture

## Executive Summary

This methodological paper addresses a core assumption of [[Capture-Recapture]] models for open populations: that all emigration from the sampled area is permanent. The authors define two models of [[Temporary Emigration]], **completely random** and **[[Markovian Emigration]]**, and show how each biases [[Jolly-Seber Model]] estimators and [[Full-Likelihood Approach]] estimators. Using [[Pollock's Robust Design]], they develop a likelihood-based framework that estimates demographic parameters and temporary emigration probabilities, with tests for completely random versus Markovian emigration. They also derive three ad hoc estimators for temporary emigration based on closed-population capture probabilities. The methods are illustrated with small-mammal data from [[White-Footed Mouse]] and [[Meadow Vole]] studies at Patuxent Wildlife Research Center, Maryland.

## Background & Description

Standard open-population models assume permanent emigration. In practice, animals may leave stationary trapping areas temporarily, return to sampled sites in some years but not others, or become unavailable for capture because of their behavior or breeding state. The paper frames temporary emigration as a potentially useful ecological parameter. Where sampling is at breeding sites, the probability of temporary emigration can equal the proportion of non-breeding animals. The example given is [[Roseate Tern]] breeding colonies, where non-breeding birds had capture-observation probabilities of 0 and so were effectively temporary emigrants (Spendelow and Nichols 1989).

The robust design divides sampling into:
- **Primary periods** (e.g., trapping every 8 weeks or annually), between which the population can change through births, deaths, and movement.
- **Secondary periods** (e.g., five consecutive days), within which the population is assumed closed.

Two models of temporary emigration are defined:
- **Completely random emigration:** probability γ_i that a superpopulation member is outside the sampled area in period i, independent of past status.
- **Markovian emigration:** probabilities γ'_i and γ''_i depend on whether the animal was a temporary emigrant in period i − 1.

Both models assume survival does not differ between animals inside and outside the study area.

## Ecological & Environmental Context

**Study systems and sampling design**

- *Peromyscus leucopus* (white-footed mouse): trapped about monthly from 1978 to 1983 in lowland hardwood forest on two 7 × 14 checkerboard grids, with stations 15.2 m apart and individually tagged animals. Capture probabilities were typically above 0.6 but often fell below 0.3 during cold periods (overnight temperatures near 0 °C). The authors contrast two explanations: reduced activity by all animals, or animals sheltering belowground in torpor and becoming temporary emigrants.
- *Microtus pennsylvanicus* (meadow vole): trapped in old-field habitat during 1981 on a 10 × 10 grid, with stations about 7.6 m apart. Five-day trapping sessions were run on 27 June, 1 August, 29 August, and 3 October. Only males with body mass above 21 g were analyzed. A raccoon disturbed traps during one session.

**Interpretation of temporary emigration**

For *P. leucopus*, temporary emigration is interpreted as movement belowground and inactivity (possibly torpor), linked to cold temperatures and short day length. For *M. pennsylvanicus*, it is interpreted as local movement. The authors plan to model γ as a function of covariates such as temperature.

## Key Findings

**1. Bias from temporary emigration depends on the emigration model and estimator**
- Under completely random emigration, the Jolly-Seber survival estimator remains unbiased, although precision declines. Other Jolly-Seber estimators are unbiased for the superpopulation, not the sampled area.
- Under completely random emigration, the full-likelihood approach yields negatively biased capture and survival estimates.
- Under Markovian emigration with γ'_i > γ''_i (the expected pattern), survival and capture estimates are negatively biased for both Jolly-Seber and full-likelihood estimators. When γ'_i < γ''_i, capture estimates are negatively biased but survival estimates are positively biased.

**2. Full-likelihood models that include temporary emigration**
- Model (φ, p, γ) for completely random emigration and model (φ, p, γ', γ'') for Markovian emigration were developed and implemented in the program [[Program Rdsurviv]].
- In simulations with N = 500 per primary period, estimators from the temporary-emigration model were approximately unbiased. Models ignoring temporary emigration were biased.
- Markovian models are not fully identifiable. The authors recommend constraining the penultimate and final γ values to be equal.

**3. Ad hoc estimators for heterogeneous capture probabilities**
- When closed-model assumptions are violated by heterogeneity in capture probability, three ad hoc estimators are offered (Eqs 5, 9, and 11). These are built from [[Lincoln-Petersen Estimator]] and [[Otis et Al. 1978 Closed-Model Estimators]] (Mh, Mt, Mth) and are ratio estimators with delta-method variances.
- The paper notes that negative estimates can occur when the true γ approaches 0 or when closure is violated between secondary periods.

**4. Results for *Peromyscus leucopus* (grids 1 and 2, September 1980 to March 1981)**
- Likelihood-ratio tests rejected models without temporary emigration, indicating some animals were temporarily unavailable for capture.
- Grid 1 showed evidence of Markovian dependence. Grid 2 was analyzed with the completely random model, as indicated by the tests and AIC.
- Temporary emigration probabilities were high for cold periods 3 to 5 and low for periods 2 and 6 to 7, consistent with cold-induced inactivity.
- Estimated monthly survival under the lowest-AIC model was 0.85 on grid 1 (general model mean 0.86) and 0.81 on grid 2 (general model mean 0.80).
- Standard errors for γ estimates were large, reflecting poor precision with small to medium sample sizes.

**5. Results for *Microtus pennsylvanicus* (1981)**
- The full-likelihood models did not fit the data well (for example, GOF χ² = 39.0, df = 8, P < 0.01 for the completely random model). The model with no temporary emigration had the lowest AIC, and likelihood-ratio tests gave no evidence for temporary emigration (P > 0.72).
- Ad hoc estimators based on closed heterogeneity models produced small temporary emigration estimates, with 95% confidence intervals that included zero.
- The authors conclude that temporary emigration was very small during the estimable periods. Capture probabilities were high (for example, p = 0.95, SE = 0.045, and p = 0.92, SE = 0.063), which leaves little room for temporary emigration.

**6. Assumptions and limitations**
- The population must be closed to all gains and losses within each primary period.
- Survival must be equal for animals inside and outside the study area. This could be tested with multistate models (Brownie et al. 1993) but would require sampling outside the study area.
- Recruits are assumed to enter the sampled area with the same probability as the rest of the superpopulation.
- The ad hoc estimators have not been fully characterized. The authors suspect Eq. 11 may be more biased but have a lower mean squared error than Eq. 9.

**7. Recommendations and applications**
- Use the models to test for temporary emigration, distinguish completely random from Markovian emigration, and estimate capture, survival, and temporary emigration probabilities.
- Use [[Program Rdsurviv]] for robust-design data. The full-likelihood approach is efficient even without temporary emigration.
- Multistate models can be combined with temporary emigration models to estimate breeding probabilities and reproductive costs, where non-breeders are unavailable for capture.
- Potential applications include bird breeding grounds (annual primary periods) and amphibian breeding ponds (skipped breeding, tested with [[Balser Test]]).
- Extensions could model γ as a function of state variables such as sex, age, or body size.