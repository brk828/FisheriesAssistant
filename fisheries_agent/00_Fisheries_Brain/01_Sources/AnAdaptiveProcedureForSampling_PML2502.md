---
species: "N/A"
common_name: "Orange Roughy; Shrimp (unspecified species); Krill (unspecified species)"
family: "N/A"
habitat: "Deep-sea floor and pinnacles (orange roughy); extensive ocean and survey bays (shrimp, krill)"
ocean_basin: "Pacific (inferred from survey locations)"
location: "Chatham Rise, New Zealand; Alaska shrimp survey areas; open ocean (krill)"
tags: [ichthyology, marine-biology, sampling-design, orange-roughy, shrimp, statistics]
title: "An Adaptive Procedure for Sampling Animal Populations"
source_id: "PML2502"
marsh_id: "PML2502"
library: "Marsh Library"
permission: "not public domain"
source_citation: "S. K. Thompson, F. L. Ramsey, G. A. F. Seber (1992). An Adaptive Procedure for Sampling Animal Populations. Biometrics, Volume 48, Issue 4, pp. 1195-1199. Marsh Library ID: PML2502."
source_file: "Thompson S.K. et al. 1992. an adaptive procedure for sampling animal populations.pdf"
text_extraction: "text"
---
# An Adaptive Procedure for Sampling Animal Populations

#ichthyology #marine-biology #orange-roughy #shrimp

## Executive Summary

This paper, by [[Steven K. Thompson]], [[Fred L. Ramsey]] and [[George A. F. Seber]] (published in [[Biometrics]], 1992), develops an **adaptive stratified sampling procedure** for animal populations. In this design, the number of samples taken in one stratum or primary unit depends on the observations made in earlier units. The method targets sparse but highly clustered populations, where simple random sampling yields many empty samples. Two estimators are developed: a **design-unbiased** strategy, whose unbiasedness rests on the random selection of sites, and a **model-unbiased** strategy, whose unbiasedness rests on an assumed spatial model. The theory is illustrated with a [[Shrimp Trawl Survey]] example from Alaska.

## Background & Description

- **Problem:** Clustered populations have a coefficient of variation of the number per unit area that is much greater than 1, so large sample sizes are needed for a given precision. Examples include [[Krill]], which are a key food for whales, and [[Orange Roughy]] on the [[Chatham Rise]] in New Zealand. Orange roughy aggregate around pinnacles to spawn, and their survey density estimates set fishing quotas.
- **Limitations of existing approaches:** Conventional stratification needs prior knowledge of abundance patterns. Two-phase sampling with stratified means is biased. [[Kremers]] obtained an unbiased estimator using the [[Rao-Blackwell Method]], but it is computationally complex.
- **Proposed approach:** The sample size in each primary unit after the first is set by observations from earlier units. Sampling intensity rises near high abundance and falls after low counts, while conventional estimators remain unbiased.
- **Shrimp context:** [[Alaska Department of Fish and Game]] trawl surveys estimate shrimp density from catch weight and swept area. Shrimp schooling is modeled with exponential-shaped correlation functions of abundance by distance between tows.

## Ecological & Environmental Context

- Shrimp habitat in a survey area (such as a bay) is divided into a grid of primary units of roughly equal area.
- Shrimp show aggregation tendencies that are well known from past data, but their exact location in a given survey cannot be predicted in advance. Surveys often record many consecutive zero or near-zero catches before catches rise steadily on approaching an aggregation.
- The authors assume that clustering arises from density differences between primary units rather than within them, which holds when animal patches are much larger than a primary unit. They describe this as an "apparent" rather than "true" contagious model.
- Spatial distributions are modeled as a [[Spatial Poisson Process]].

## Key Findings

**1. Design-unbiased adaptive estimator (Section 2)**
- Let the study region have *L* primary units (strata) of area A_h, each split into N_h secondary units. A random sample of n_h secondary units is drawn from unit *h*, with n_h depending on the density observed in earlier units.
- The estimator D̂ = Σ W_h D̂_h, where W_h = A_h/A, is **unbiased** (Eq. 2 and Eq. 6).
- The standard stratified-sampling variance formula still applies, so the variance estimator is valid in the adaptive setting (Eq. 7). Unbiasedness depends on the design, not on population assumptions.
- The result extends when the secondary-unit size also depends on earlier observations.

**2. Model-unbiased adaptive estimator (Section 3)**
- Within each primary unit, animals follow a spatial Poisson process with intensity λ_h. The λ_h values are treated as observations from a spatial process with mean μ.
- Secondary units need not be chosen at random. They may be placed systematically or purposively, because randomness is imposed by the model.
- The authors evaluate the **mean squared error** of D̂ as the more appropriate criterion. Under the model, u_2 is an unbiased estimate of E[(D̂ − D)²].
- If primary-unit totals are treated as fixed, the conditional distribution is binomial, and the variance estimator u_6 is unbiased.

**3. Shrimp design example (Section 4)**
- Strategy 1: In the first primary unit, m_1 random half-mile tows are made. If the catch is 50 pounds per mile or less, m_1 tows are made in the next unit. If it exceeds 50 pounds per mile, m_2 tows are made (m_2 > m_1). The ratio r = m_2/m_1 is key to the design.
- Strategy 2 (variation): m_1 = 1 and m_2 = 2, with the two half-mile tows merged into one one-mile tow. This is easier to run at sea because tow allocation is random. Its variance can be estimated only under the Poisson model, with each n_h equal to 1 or 2.
- The authors state that practical guidelines require data and experience. Optimal design (minimizing Var[D̂] for a fixed expected total tow length) was still under investigation. Greater aggregation calls for a larger r to offset the extra low catches.

**4. Overall conclusions**
- Adaptive sampling is a more efficient way to survey sparse, highly clustered populations.
- Both estimator families are unbiased, under different assumptions: design-based (random site selection) and model-based (Poisson spatial model).
- The method is supported by earlier work from [[Francis]] (1984), [[Thompson]] (1990, 1991a, 1991b) and [[Seber]] (1986).

**Funding and dates:** Partly supported by [[National Science Foundation]] Grant DMS-9016708. Received September 1990, revised May 1991, accepted July 1991.