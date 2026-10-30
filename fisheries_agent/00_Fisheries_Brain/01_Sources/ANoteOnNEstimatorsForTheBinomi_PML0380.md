---
species: N/A
common_name: Impala; Waterbuck
family: N/A
habitat: N/A (study area described only as a small area of Kruger National Park; habitat type not stated)
ocean_basin: N/A
location: Kruger National Park, South Africa
tags: [biostatistics, population-estimation, mammal-counts, binomial-distribution, beta-binomial, kruger-national-park]
title: "A Note on N Estimators for the Binomial Distribution"
source_id: "PML0380"
marsh_id: "PML0380"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. J. Carroll, F. Lombard (1985). A Note on N Estimators for the Binomial Distribution. Journal of the American Statistical Association, Vol. 80, No. 390, Theory and Methods, p. 423. Marsh Library ID: PML0380."
source_file: "Carroll R.J. et al. 1985. a note on N estimators for the binomial distribution.pdf"
text_extraction: "text"
---
# A Note on N Estimators for the Binomial Distribution

#mammalogy #population-ecology #biostatistics

## Executive Summary

This document is a 1985 statistical methods paper by [[Raymond J. Carroll]] and F. Lombard in the *Journal of the American Statistical Association*. It is not an aquatic or ichthyological study. It addresses how to estimate the total number of units, *N*, from binomial success counts when the success probability *p* is also unknown. The authors propose estimators derived from the [[Beta-Binomial Distribution]], obtained by integrating a binomial likelihood over a beta prior for *p*. These estimators are compared against the method of moments and maximum likelihood estimators studied by [[Olkin, Petkau, and Zidek]] (OPZ, 1981), which are known to be unstable. The method is tested on field counts of [[Impala]] herds and [[Waterbuck]] in [[Kruger National Park]]. Those species are terrestrial mammals and are discussed only as data sources. No fish, invertebrates, plankton, or water chemistry are covered.

## Background & Description

**Problem.** Given independent success counts *s*₁, …, *sₖ* from a binomial distribution with unknown *N* and *p*, the goal is to estimate *N*. The [[Method of Moments Estimator]] (MME) and the [[Maximum Likelihood Estimator]] (MLE) can be extremely unstable. A small change in one observed count can produce a large change in the estimate of *N*. This instability arises when the estimated mean and variance are nearly equal, which implies a small apparent *p*.

**Prior stabilized estimators.** OPZ introduced two stabilized versions:
- **MLE:S**: the ordinary MLE, or a jackknifed version based on the maximum count, depending on a stability criterion.
- **MME:S**: the ordinary MME when the stability criterion holds, otherwise a [[Ridge Regression]] correction (Hoerl and Kennard 1970).

OPZ found that both stabilized estimators dominate the ordinary MME and MLE in Monte Carlo simulation. They also found that MME:S is generally better than MLE:S, except when *p* is large and the case is unstable.

**Proposed method.** The authors assume *p* follows a beta(*a*, *b*) density, with integer *a* and *b*, and integrate it out of the joint likelihood. The resulting integrated likelihood (their Eq. 3) is maximized over *N* ≥ max(*s*ᵢ) to give the estimator M_beta(*a*, *b*). The approach is justified in a Bayesian setting by Draper and Guttman (1971) and as nuisance-parameter elimination by Barnard et al. (1962). The authors also discuss two alternatives that yield known unstable estimators. One uses a point mass at *p* = *s̄*/*N* and gives the MLE. The other uses a density proportional to 1/*p*, which is equivalent to the conditional MLE.

## Ecological & Environmental Context

The paper's examples are counts of two large mammals in a South African national park. Counts were made from a light aircraft on five cloudless days in a small area of Kruger National Park. The counting was done by five highly trained wildlife officials. The authors state that the assumption of independent binomial counts with roughly equal success probabilities is reasonable but not indisputable. The statistical problem arises in any survey where detection probability is unknown and sometimes very low. The paper does not describe habitat, water features, or ecological processes beyond the counting context.

## Key Findings

**Estimator performance (Table 1).** The authors reanalyzed the difficult cases from OPZ's Table 2. Their conclusions:
- MME and MLE are highly unstable.
- MME:S, MLE:S, M_beta(0,0) (the Haldane/uniform-type case with *a* = *b* = 0), and M_beta(1,1) are stable.
- M_beta(0,0) and M_beta(1,1) give results similar to each other.

**Monte Carlo study (Table 2).** The authors extended OPZ's simulation to 2,000 randomly generated cases.
- Using a symmetric uniform *p* introduced bias toward the authors' estimators. To avoid this, the authors generated *p* from asymmetric beta distributions, including (*a*, *b*) = (0,1), (1,2), (1,3), (1,0), (2,1), and (3,1).
- **Unrestricted case (0 < *p* < 1):** The four estimators performed about equally well when stable. When unstable, MLE:S was clearly the worst.
- **Small *p* (0 < *p* ≤ √2 − 1):** MLE:S was worse than MME:S. The authors' M_beta(0,0) was only about 4% less efficient than MME:S in relative mean squared error, and M_beta(1,1) lost about 1%.
- **Large *p* (√2 − 1 < *p* < 1):** About 90% of cases were stable. The authors' estimators had a clear advantage, especially M_beta(1,1). Overall, M_beta(1,1) was the clear winner in this subset.

**Bias.** The stabilized MLE:S was much more negatively biased than the other stabilized estimators. Some printed bias percentages in the scan are illegible. The reported figures are approximately 20% for MME:S and 30–35% for M_beta(0,0) and M_beta(1,1). For unstable cases with true *p* below √2 − 1, the authors' estimators were negatively biased. Of all unstable cases, 82% fell in this group and 18% had positive bias.

**Example 1: Impala herds (≥25 animals).** Observed counts were 15, one value illegible in the scan, 21, 23, and 26. The dispersion ratio was 1.59, so the case is unstable. Estimates were:
- MME = 57
- MLE:S = 28
- MLE = 53
- M_beta(0,0) = 42
- MME:S = 54
- M_beta(1,1) = 42

When the largest count was changed from 26 to a different value, MME changed from 57 to 77 and MLE from 53 to 74. MME:S, MLE:S, and the M_beta estimators changed little.

**Example 2: Waterbuck.** Observed counts were 53, 57, one illegible value, 67, and 72. The ratio was 1.32, so the case is highly unstable. Estimates were:
- MME = 272
- MLE:S = 72
- MLE = 265
- M_beta(0,0) = 146
- MME:S = 199
- M_beta(1,1) = 140

When the largest count was changed from 72 to 73, the estimates became:
- MME = 362
- MLE:S = 78
- MLE = 355
- M_beta(0,0) = 155
- MME:S = 215
- M_beta(1,1) = 146

The conditional MLE, M_beta(−1,0), was very unstable: 1,545 for the original data and above 4,000 for the perturbed data. Table 3 explores M_beta(α, 0) for several values of α. The authors conclude that a data-dependent choice of α is needed, and that the conditional MLE should be avoided.

**Asymptotic results.**
- For fixed (*a*, *b*) with *N* → ∞, *k* → ∞, and k/N → 0, the standardized estimator is asymptotically normal with a variance that depends on *p*. Smaller *p* gives larger variance.
- Lemma 1 (with *a* = *b* = 0) and Lemma 2 show that increasing the smoothing parameters acts as shrinkage. Larger (*a*, *b*) discounts the possibility of small *p*. This explains why the most severe unstable cases are handled better by (1,1) than by (0,0).
- Under fixed *k* = 2, none of the estimators are consistent in the sense *N̂*/*N* → 1, but the authors expect the estimators to retain a positive probability of an unstable case.

**Conclusions and open problems.**
- The beta-binomial estimators are stable and competitive with, and sometimes better than, the MME:S and MLE:S of OPZ.
- The choice of (*a*, *b*) is flexible, and the authors suggest that the data could be used to select it.
- A Bayesian joint prior on (*N*, *p*) that downweights small *p* and large *N* might yield better estimators.
- The shape of the integrated likelihood is poorly understood, so constructing a confidence interval for *N* remains open.