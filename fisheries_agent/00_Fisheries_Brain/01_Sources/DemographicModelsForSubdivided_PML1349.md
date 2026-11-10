---
species: Larus ridibundus
common_name: Black-headed Gull
family: N/A
habitat: Breeding colonies on ponds (one large pond colony and about 20 smaller colonies)
ocean_basin: N/A
location: Central France
tags: [ornithology, population-ecology, demography, multisite-models, renewal-equation]
title: "Demographic models for subdivided populations: the renewal equation approach"
source_id: "PML1349"
marsh_id: "PML1349"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. D. Lebreton (1994). Demographic models for subdivided populations: the renewal equation approach. Marsh Library ID: PML1349."
source_file: "Lebreton J.D. 1994. Demographic models for subdivided populations the renewal equtation approach.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Demographic models for subdivided populations: the renewal equation approach

#ornithology #population-ecology #laridae

## Executive Summary

This theoretical paper restates the multisite [[Renewal Equation]] of [[Le Bras]] (1971) and [[Rogers]] (1974) in matrix form, so that it can be applied to animals with an annual birth pulse living across several sites. The author derives generalizations of age structure, [[Reproductive Value]], [[Net Reproduction Matrix|Net Reproduction Rate]], [[Generation Time]] and [[Sensitivity Analysis|Sensitivities]] that extend one-site results. The approach is illustrated with a two-site [[Leslie Matrix]] model of a [[Black-Headed Gull]] population in central France, split into a "Good" and a "Poor" site. The main conclusion is that the Good site, which holds the largest colony, drives population stability in the first scenario, while strong dispersal of young breeders in the second scenario produces an unexpected imbalance in long-term contributions.

## Background & Description

The paper builds on the observation that births and deaths in natural populations depend strongly on movement, so models must account for dispersal across spatial units. Multiregional models from human demography (Rogers, 1966, 1974) have been adapted to [[Metapopulation|Metapopulations]], where extinction, recolonization and the evolution of dispersal are central questions.

The author considers *p* sites and *n* age classes plus age class 0 for newborns. Only birth-pulse populations are treated, with time steps matching age classes and constant parameters. Key quantities include:

- **Fecundity matrix** *F<sub>i</sub>*: newborns in site *j* per female aged *i* in site *k*, usually diagonal because migration is folded into survival.
- **Migration-survival matrix** *S<sub>i</sub>*: proportion of females surviving from age *i*−1 to *i* and moving between sites.
- **Projection matrices** *P* and *M*, which generalize the [[Leslie Matrix]] and, when the maximum age is unbounded, the Usher matrix.

Under mild connectivity conditions the matrix is primitive, so the [[Perron-Frobenius Theorem]] guarantees a simple positive dominant eigenvalue λ, which is the asymptotic multiplication rate over all sites. The right eigenvector V gives the stable age-by-site structure, and the left eigenvector U gives age-by-site [[Reproductive Value]]s.

The renewal equation reduces the problem to newborns alone. Its determinantal form, det(Λ(λ) − I) = 0, has the same largest root as the full matrix, at the cost of putting λ in polynomial form. Explicit results are derived for:

- Stable age-by-site structure and reproductive values (Eqs. 11–16).
- A compound [[Generation Time]] *T* weighted by site distribution, multiple births and reproductive value (Eqs. 21–22).
- Sensitivities to overall changes in fecundity, survival, or survival traded against fecundity (Eqs. 23–25). These match the one-site results of [[Houllier and Lebreton]] (1986).
- A net reproduction matrix *R* whose dominant eigenvalue indicates whether the population grows or declines (Eqs. 26–30).
- Special cases: adulthood at age *n*, homogeneous sites, and disconnected populations, where the site with the largest multiplication rate eventually dominates.

The paper notes that the renewal approach was neglected in the literature and that a Matlab program implementing the calculations is available.

## Ecological & Environmental Context

The [[Black-Headed Gull]] (*Larus ridibundus*) case is set in central France. Roughly 3000 pairs breed in a large, thriving colony on a single pond, and about 3000 more pairs breed in around 20 other colonies. These smaller colonies are described as less favourable. The author cites evidence that saturation of the largest colony forces many birds to breed in poorer areas, and that breeding starts at an earlier age in small, unfavourable colonies (Allainé, 1988).

Demographic inputs come from [[Capture-Recapture]] analyses of marked birds:

- **Adult annual survival:** 0.822 (Clobert et al., 1987) using data to 1985, and 0.89 in analyses of data up to 1993 (Prévot-Julliard, 1993).
- **Age-specific proportion of breeders** in the largest colony: approximately 0.3, 0.5, 0.7 and 1 for ages 2, 3, 4 and the oldest class (Lebreton et al., 1990).
- **Survival to age 2** for locally recruited birds born in the largest colony: about 0.6.
- **First-year survival:** about 0.4, though the author suspects bias because it comes from recoveries of birds ringed as chicks (Anderson et al., 1985).
- **Transience:** about one-third of birds seen for the first time in the largest colony are estimated to disappear.

The author links these processes to [[Dispersal]] and [[Philopatry]]. Recruitment dispersal from the Poor site to the Good site is symmetric in scenario 1. Scenario 2 adds strong dispersal of young breeders out of the Good site.

## Key Findings

- **Scenario 1 (recruitment dispersal only):** The two-site 10 × 10 Leslie matrix has dominant eigenvalue λ = 0.997, which is near stability. The dominant eigenvalue of the 2 × 2 net reproduction matrix is p(R) = 0.979, which signals asymptotic decline even though neither the Leslie matrix nor *R* shows this directly on inspection.
- **Population distribution:** Scaling the stable structure to 6000 pairs gives 3661 pairs in the Good site and 2339 in the Poor site. The field estimates are about 3000 in each, so the model is roughly consistent with observations.
- **Generation time:** *T* = 7.693 years overall. Offspring born in the Good site have a longer generation time (7.851 years) than those born in the Poor site (7.217 years). Because there is no adult dispersal, the mother's birthplace does not affect generation time.
- **Stability driver:** The largest contribution to newborns, whether measured by λ or by the product of *V* and *U*, is from the Good site to itself, so the Good site is key to population stability in scenario 1.
- **Sensitivity check:** Raising adult survival from 0.82 to 0.89 changes λ by a predicted factor of 1.071, which closely matches the updated Leslie matrix eigenvalue of 1.074.
- **Reproductive values diverge with age:** Site-specific reproductive values are similar at birth but diverge over time because adults do not move between sites.
- **Scenario 2 paradox:** Strong dispersal of young adults out of the Good site makes the renewal matrix close to stochastic, and reproductive values at birth become nearly equal. Even so, the long-term contribution of Good-site-born individuals is largest for the Poor site. The author considers this scenario somewhat unrealistic, since the imbalance would be reduced if dispersal from breeding Poor-site birds were lower or if young breeder dispersal were symmetric.
- **Evolutionary implication:** Because reproductive value at birth is a component of fitness, the author argues that if dispersal–philopatry behaviour is heritable, selection should favour dispersal from sites with low reproductive value toward sites with high value. Equal reproductive values across sites would then mark a balance point. The author notes that this population has no reason to be at selective equilibrium.
- **Methodological conclusion:** The renewal approach generalizes most one-site demographic characteristics to multisite models. The author suggests that [[Site-Specific Reproductive Value]]s should become a key concept in the study of dispersal evolution, and that [[Multisite Capture-Recapture]] models are a promising route to estimating the parameters.