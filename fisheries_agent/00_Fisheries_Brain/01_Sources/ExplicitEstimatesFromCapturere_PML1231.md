---
species: N/A
common_name: N/A
family: N/A
habitat: Apple orchard (single-population field study; non-aquatic)
ocean_basin: N/A
location: East Malling Research Station, Kent, UK (orchard data; per Appendix acknowledgement)
tags: [capture-recapture, population-ecology, biostatistics, mark-recapture, stochastic-model]
title: "Explicit estimates from capture-recapture data with both death and immigration-stochastic model"
source_id: "PML1231"
marsh_id: "PML1231"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. M. Jolly (1965). Explicit estimates from capture-recapture data with both death and immigration-stochastic model. Biometrika, vol. 52, no. 1/2, pp. 225-247. Marsh Library ID: PML1231."
source_file: "Jolly G.M. 1965. explicit estimates from capture recapture data with both death and immigration stochastic model.pdf"
text_extraction: "text"
---
# Explicit Estimates from Capture-Recapture Data with Both Death and Immigration: A Stochastic Model

**Note on scope:** This document is a statistical methods paper on animal population estimation. It does not address fish or aquatic taxa. The only worked example is an insect population (female black-kneed capsid, *Blepharidopterus*-group, name partly garbled in OCR) in an apple orchard. The ichthyology and marine-biology tags are therefore omitted.

#population-ecology #biostatistics #capture-recapture

## Executive Summary

G. M. Jolly's 1965 paper in [[Biometrika]] derives a general probability distribution for [[Capture-Recapture Method|capture-recapture]] data from a single open population subject to both death and [[Immigration]]. The model is [[Stochastic Model|stochastic]]: the probability that an animal survives an interval is treated as a probability, not a fixed rate, which Jolly regards as more realistic than the earlier [[Deterministic Model]] (Jolly, 1963).

The paper's main results are:

- Explicit [[Maximum Likelihood Estimation|maximum-likelihood]] estimates of population size, [[Survival Rate]] and numbers of immigrants, obtained without iterative solution.
- Allowance for [[Losses On Capture]], so that the number captured and the number released are treated as separate variables.
- Asymptotic variances and covariances for these estimates.
- Demonstration that the single-recapture and multiple-recapture estimators of [[Seber Model|Seber]] (1962, 1966) are algebraically identical once losses on capture are accounted for.
- An application to a 13-sample orchard dataset, compared with the deterministic estimates from Jolly (1963).

## Background & Description

**Context and prior work.** Jolly reviews earlier capture-recapture theory. Key contributions include:

- [[Cormack Model|Cormack (1964)]]: a stochastic solution with asymptotic variances for a non-random sample of marked fish. The paper does not give further detail about the species.
- [[Seber Model|Seber (1962, 1965, 1966)]]: estimators for the multi-sample single-recapture census, where animals cannot be recaptured more than once. This design arises when recaptures are made during hunting or fishing. Seber's 1966 paper extends this to multiple recaptures with death and immigration.
- [[Darroch Estimator|Darroch (1959, 1961, 1969)]]: maximum-likelihood estimation for populations with death or immigration alone, and estimation equations for the combined case, without variances.

**Definition of a single population.** Jolly defines a "single" population as one in which animals move freely and mix within a single area. Populations split into separate areas are outside this definition. The population may still contain distinct classes of animals behaving differently.

**Notation and assumptions.** Key quantities include:

- *N_i*: total population at sampling time *t_i*.
- *M_i*: number of marked animals at *t_i*.
- *n_i*: number captured in the *i*th sample; *m_i*: number of marked animals in that sample.
- *s_i*: number released after marking; *R_i*: number of released animals later recaptured.
- *B_i*: number of new animals joining the population between *t_i* and *t_{i+1}*.
- *φ_i*: probability that an animal alive at release survives until the next capture.
- *p_i*: probability of capture; *q_i*: probability of release (not a loss on capture).

Assumptions include random sampling, marking so that each animal's capture history is traceable, and a short capture period relative to sampling intervals. Sampling intervals need not be equal.

**Loss versus release.** Jolly treats the number captured and the number released as distinct. Their difference is termed "losses on capture", replacing the earlier term "accidental losses".

## Ecological & Environmental Context

The model applies to any mobile population where sampling is by capture and marking, and it is explicitly relevant to situations such as:

- Recaptures made during hunting or fishing, where losses on capture may be 100%. Jolly notes that recaptured animals are counted once and this loses no information for the estimate.
- Breeding-season recapture, where sampling may be non-random. Jolly examines bias from excluding non-breeders or distant breeders. Bias depends on whether breeding location is associated with age or mark status.
- Mobile populations where ordinary sampling is impractical.

Jolly also notes that the model's assumptions may fail in practice, for example when releases are of predetermined numbers rather than random samples.

## Key Findings

1. **Explicit estimators.** The stochastic model gives closed-form estimates:
   - Marked population at sample *i*: *m̂_i* = Σ(*n_i* − *m_i*+... ) type sums of recapture and release counts, from the summed recapture totals (equation 22).
   - Survival: *φ̂_i* from ratios of marked-population estimates.
   - Immigration: *B̂_i* from successive population estimates and survival.
   The paper states that the estimates are "extremely simple" compared with the deterministic case.

2. **Equivalence with Seber and Darroch.** Seber's (1966) estimators are algebraically identical to Jolly's when losses on capture are zero. Seber's (1962) single-recapture estimators are also identical. Darroch's (1969) estimates coincide with Jolly's when losses on capture are set to zero. The paper therefore confirms that multiple and single recapture are special cases of one general model.

3. **Interpretation.** The population estimate depends on two quantities: the proportion of marked animals in a random sample, and the ratio of future recaptures to releases. Recaptures therefore enter the estimate in two ways.

4. **Variance behaviour.** Unlike the deterministic model, the stochastic variance terms include an error-of-estimation component and a component from random survival. The estimation-error component vanishes as the sampling fraction approaches one. Jolly observes that the variance and bias are reduced by recapturing as many released animals as possible.

5. **Bias.** Bias in the estimator of *m_i* is positive and equal to (*M_i* − *m_i*)(1/*R_i* − 1/*s_i*) to first order.

6. **Deterministic-model comparison (orchard data).** Applied to 13 successive samples from an apple orchard, alternately 3- and 4-day intervals, of female black-kneed capsids (in which dilution by both mortality and immigration occurred), the stochastic estimates are identical to the unweighted estimates from [[Jolly Model|Jolly (1963)]] for the same data. Standard errors for survival are roughly half those under the deterministic model at low *d*, converging at the final sample. For population size, at *d* = 12 the deterministic standard error is 69.0 and the stochastic one is 68.4. The paper attributes the stochastic model's larger survival-rate errors to its extra variance terms, which may be seen as more realistic.

7. **Sampling design recommendations.** Jolly recommends separating the recapture process from the release process where feasible. Recapture can proceed continuously by many observers using a simple mark code. Releases should be made at specific times by experienced staff. Random sampling is required for the release group, but not necessarily for the recapture samples, provided capture probability is unaffected by mark status.

8. **Assumption testing.** Jolly notes that testing assumptions such as age effects on survival or behaviour differences among marked animals falls outside the paper's scope. He suggests comparing observed and expected frequencies, or estimating survival separately for age groups.

9. **Conclusion.** Jolly argues that for capture-recapture problems in general, purely deterministic models, with their approximations, should be replaced by stochastic models, since the stochastic solution is no more complicated and is in fact simpler.