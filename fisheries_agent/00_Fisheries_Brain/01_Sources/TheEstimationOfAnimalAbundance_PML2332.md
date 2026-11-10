---
species: N/A
common_name: N/A
family: N/A
habitat: N/A (general animal populations; fish populations cited as examples, including freshwater streams and ponds)
ocean_basin: N/A
location: N/A
tags: [ichthyology, marine-biology, population-estimation, statistics, mark-recapture]
title: "The estimation of animal abundance and related parameters"
source_id: "PML2332"
marsh_id: "PML2332"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Seber (1982). The estimation of animal abundance and related parameters. Marsh Library ID: PML2332."
source_file: "Seber. 1982. The estimation of animal abundance and related parameters.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# The estimation of animal abundance and related parameters

#ichthyology #marine-biology #population-estimation

## Executive Summary

This text is the opening material and early chapters of a statistical monograph on estimating animal population size and related parameters. It sets out the notation and terminology used throughout, reviews general statistical tools (maximum-likelihood estimation, moment estimation, the [[Delta Method]], conditional variances, regression models, goodness-of-fit tests, and iterative equation solvers), and then applies them to closed-population density estimation and [[Mark-Recapture]] experiments. Although its roots lie in fishery science ([[Beverton-Holt Methods]] and [[Ricker Methods]]), the methods are presented as general tools for pest control, wildlife management and fisheries. The most detailed material concerns the [[Petersen Estimate]] and its bias-corrected successors.

## Background & Description

The author notes that the field was pioneered by fishery scientists, with the major volumes of Beverton and Holt (1957) and Ricker (1958). Interest has since spread to researchers in many areas, and the subject is expanding rapidly. The book aims to organise this literature by the type of statistical model used and to discuss the assumptions behind each model. The author acknowledges several reviews, including De Lury (1954), Scattergood (1954), Ricker (1958, fish), Mosby (1963, wildlife management), Southwood (1966, insects) and Cormack (1968).

Notation is "mnemonic" rather than following the international FAO notation, which the author found unsuitable. For example, N and n denote the number of individuals in the population and sample, while M and m denote marked individuals in the population and sample, and s denotes the number of samples. Each chapter is self-contained in its notation. Standard symbols include E[y], V[y], CV = σ/E[y], the normal distribution N(θ, σ²), and the chi-squared distribution with k degrees of freedom.

### Core Terminology

- **Population change:** Population size in an area is governed by immigration, emigration, total mortality and recruitment.
- **Total mortality:** For exploited populations, this is split into exploitation mortality and [[Natural Mortality]] (predation, disease, climate). Emigration is not counted as mortality.
- **Survival and mortality rates:** If mortality follows a Poisson process with parameter μ, the survival rate over period t is φ_t = e^(−μt) (eq. 1.1). The parameter μ is the [[Instantaneous Mortality Rate]].
- **Mean life expectancy:** Derived from the exponential density, giving a mean of 1/μ (eq. 1.3).
- **Recruitment:** Animals born into the population or growing into the catchable class. In fishery research, this means fish growing into the legally catchable size class. Immigration is not treated as recruitment.
- **Closed vs open populations:** A [[Closed Population]] is unchanged during the study, with migration, mortality and recruitment negligible. Otherwise the population is [[Open Population]].

## Ecological & Environmental Context

The text is primarily statistical, but it gives several field contexts for abundance estimation:

- **Fish populations:** Fish have been counted by draining ponds or water bodies, a method cited from Dice (1938). The "bounded counts" method is proposed for stream censuses by independent divers and for counting migrating fish runs from vantage points. It is also suggested for small ponds through which large seines are drawn at least twice while the population is closed.
- **Population disturbance:** Censuses should disturb animals as little as possible. This avoids double-counting and prevents frightened animals from leaving the study area.
- **Detectability:** Counts depend on animal size, available vegetation cover and seasonal activity.
- **Track and sign counts:** Track-count methods were trialled in a population study. They were not fully developed in time for extensive use, but they showed promise as density indices, especially in areas lacking primitive roads.
- **Calendar of captures:** A method resembling direct enumeration, used in Poland.

## Key Findings

**Statistical framework (Chapter 1)**

- **Maximum-likelihood estimation:** Under reasonable conditions, the estimate is asymptotically normal. Approximate 100(1−α)% confidence intervals take the form θ̂ ± z(α/2)·σ̂. For a 95% interval, α = 0.05 and z = 1.96. Coefficient of variation C = σ̂/θ̂ measures the proportional width of the interval.
- **Bias rule:** A bias correction b is included in the confidence interval if it exceeds 10% of θ̂ (Cochran 1963).
- **Weighted mean:** The minimum-variance estimator uses weights proportional to 1/σᵢ². Unweighted means have an unbiased variance estimate Σ(xᵢ − x̄)²/[n(n−1)].
- **Delta method:** Gives approximate means, variances and covariances of functions of random variables. Its exact formula for independent x and y is V[xy] = (E[x])²V[y] + (E[y])²V[x] + V[x]V[y] (eq. 1.11).
- **Weighted regression:** Least-squares estimates are given for simple, zero-intercept and multiple weighted linear models, with confidence intervals for the slope and intercept. A Fieller-type interval is used for the ratio of parameters. For the special model in eq. 1.15, the author uses the t-based interval (1.17) rather than the normal approximation (1.19), because the parameter is often small (< 10).
- **Goodness-of-fit tests:**
  - *Binomial:* The Binomial Index of Dispersion is asymptotically χ² distributed.
  - *Poisson:* The [[Poisson Index of Dispersion]] (T₂) is generally more sensitive than the chi-squared statistic (T₁). Rao and Chakravarti (1956) suggest the χ² approximation is good when the mean exceeds 3.
  - *Multinomial with unknown N:* The test statistic is asymptotically χ² with k − 1 − t degrees of freedom as N → ∞.
- **Iterative solution:** Covers the [[Newton-Raphson Method]] and the method of false positions. Barnett (1966) is cited as showing that false positions is preferred when the likelihood equation has multiple roots.

**Density estimation (Chapter 2)**

- Total counts over the whole area are the most direct approach. A "maximal" density can be obtained by excluding uninhabitable areas.
- A 2×2 contingency table compares fox frequency indices for summer and winter seasons. The chi-squared value was not significant, so there was no evidence of a seasonal difference.

**Closed population: single mark release (Chapter 3)**

- **[[Petersen Estimate]]:** N̂ = n₁n₂/m₂, where n₁ animals are marked and released, and m₂ of n₂ animals in the second sample are marked. The text lists the standard assumptions: marking does not affect catchability, marks are not lost, all marks are reported, and the second sample is random.
- **[[Hypergeometric Model]]:** The conditional distribution of m₂ given n₁ and n₂ is hypergeometric. The Petersen estimate is asymptotically normal but biased for small samples.
- **[[Chapman Estimator]] (N*):** Unbiased when n₁ + n₂ ≥ N. For n₁ + n₂ < N, the bias is approximately N·b, where b = exp{−(n₁+1)(n₂+1)/N}. Robson and Regier recommend that μ₂ (the expected number of recaptures) exceed 4, so that b is below 0.02. If m₂ > 7, the researcher can be 95% confident that μ₂ > 4.
- **Variance:** V[N*] ≈ N·φ(μ₂ + ...). Chapman (1951) notes that when the expected number of recaptures is below about 10, the census may fail to give even the correct order of magnitude. At μ₂ = 10, the standard deviation is 0.36N. The coefficient of variation is approximately C ≈ 1/√μ₂, so accuracy depends mainly on the number of recaptures.
- **Seber's unbiased variance estimator:** Exactly unbiased when n₁ + n₂ > N.
- **[[Bailey Binomial Model]]:** The binomial approximation to the hypergeometric model gives N̂ = n₁n₂/m₂ as the maximum-likelihood estimate. Bailey's modification N̂ₐ = n₁(n₂+1)/(m₂+1) has a small proportional bias. The model also applies under systematic sampling if marked and unmarked animals mix uniformly and have equal catch probability at each location.
- **Random sample size:** If n₁ is random, N* remains approximately unbiased. The conditional variance differs from the fixed-n₁ variance only slightly for large N.
- **Confidence intervals:**
  - *Poisson approximation* (p < 0.1 and m₂/n₂ < 0.1): Confidence limits are read from tables, and the worked example gives (15,020; 38,650) for N with n₁ = 1000, n₂ = 500, m₂ = 20.
  - *Normal approximation* (p < 0.1, m₂ > 50): The worked example gives (20,700; 31,600) for N with n₂ = 1000, m₂ = 80 (p = 0.08).
  - *Clopper–Pearson binomial intervals*: For m₂ = 18 and n₂ = 60 (p = 0.3), the 95% interval for p is (0.190, 0.433).
- **Sample-size design:** Robson and Regier (1964) give three standard accuracy levels, all at 1 − α = 0.95:
  - (i) A = 0.50 for preliminary or management surveys
  - (ii) A = 0.25 for more accurate management work
  - (iii) A = 0.10 for careful population-dynamics research

  Figures 3.1 and 3.2 give recommended sample sizes for N < 500 and N ≤ 300 respectively. The text advises level (iii) when N is later multiplied or divided by other estimates, such as biomass or survival.
- **[[Bounded Counts Method]]:** For units that are hard to count or that may be missed, the estimate is N̂ = 2N_m − N_(m−1), where N_m and N_(m−1) are the largest and second-largest counts. Robson and Whitlock (1964) cover the bias for more than two counts, which is of order 1/s² for s independent counts.