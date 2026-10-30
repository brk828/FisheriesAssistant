---
species: N/A
common_name: N/A
family: N/A
habitat: Impounded waters and streams (freshwater)
ocean_basin: N/A
location: Southeastern United States (study context); author affiliated with University of Michigan, Ann Arbor, USA
tags: [fish-sampling, mark-recapture, area-sampling, toxicant-sampling, detonation-sampling, population-estimation, biometrics, freshwater-fish]
title: "Integrated Area Sampling and Mark-Recapture Experiments for Sampling Fish Populations"
source_id: "PML1178"
marsh_id: "PML1178"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. L. Jensen (1992). Integrated Area Sampling and Mark-Recapture Experiments for Sampling Fish Populations. Biometrics 48, 1201-1205. Marsh Library ID: PML1178."
source_file: "Jensen A.L 1992. Intergrated area sampling and mark recapture experiments for sampling fish populations.pdf"
text_extraction: "text"
---
# Integrated Area Sampling and Mark-Recapture Experiments for Sampling Fish Populations

#ichthyology #marine-biology #freshwater-fish

## Executive Summary

This 1992 *Biometrics* paper by A. L. Jensen (School of Natural Resources, University of Michigan) proposes an [[Integrated Estimator]] for estimating fish population size. It combines [[Area Sampling]] using toxicants or detonation (such as [[Rotenone Sampling]] and [[Detonating Cord Sampling]]) with [[Mark-Recapture]] experiments. Conventional toxicant and explosive area sampling treats the whole sampled area, so the mark-recapture step covers the same ground. Jensen instead proposes treating only part of the sampled area, which allows smaller treated areas. Using mathematical derivation and computer simulation, the author finds that the integrated estimator is unbiased and performs well where standard [[Petersen Estimator]] mark-recapture methods are biased. The paper also includes a French-language abstract (Résumé).

## Background & Description

- **Study type:** Statistical methods development with computer simulation. The document contains no field data on specific fish species.
- **Sampling context:** Area sampling with toxicants or explosives is described as an effective way to obtain population estimates for fish in larger bodies of water. It is widely applied in impounded waters and streams of the southeastern United States (Davies and Shelton, 1983).
- **Problem addressed:** In many toxicant and detonation studies, mark-recapture methods are used to estimate a recovery rate. Earlier studies that combined the two (e.g., Bayley and Austin, 1988; Metzger and Shafland, 1986) coincided the two sampled areas.
- **Core proposal:** Treat only part of the sampled area with toxicant or explosive, so that marked fish are released into the wider enclosed area.

## Ecological & Environmental Context

The document is a methods paper and does not describe specific species, habitats, or water-chemistry measurements in ecological detail. Its environmental context is limited to:

- **Habitat types:** Impounded waters (reservoirs) and streams.
- **Geographic setting:** Southeastern United States.
- **Sampling assumptions:** The fish population is assumed to be randomly distributed over the sampled area, and capture probability is assumed constant during first-stage sampling.
- **Population density:** Modeled as *D*, with the mean number of animals in the sampled area given as *D*a = *N*a/*A*, where *a* is the sampled area, *A* is the area inhabited by the population, and *N* is population size.

## Key Findings

### 1. Model Structure

Sampling occurs in two stages:
- **Stage 1 (area sampling):** Fish are captured by toxicant or explosive. Capture probability is *P* = *a*/*A*.
- **Stage 2 (mark-recapture):** Fish captured in Stage 1 are marked or unmarked. Marked fish number *M*, and the count of marked fish in the second sample is *m* out of a second sample of size *n*.

The joint probability mass function is *P*(*n*, *m*) = *P*(*n*) *P*(*m* | *n*). The first stage is approximated with a Poisson distribution (valid when *P* is small and *n* ≪ *N*). The second stage is binomial.

### 2. The Integrated Estimator

The maximum likelihood estimator is:

**N̂ = M + (A/a)(n − m)**

This differs from the Petersen estimator, N̂ = Mn/m. Petersen assumed the proportion marked in the sample equals the proportion marked in the population. The integrated estimator instead assumes the number of unmarked fish per unit area in the sample equals the number of unmarked fish per unit area in the population.

The author shows the integrated estimator can also be written as a difference estimator, N̂ = An/a + (M − Am/a). This is the same structure as the difference estimator used in survey sampling (Sukhatme and Sukhatme, 1970).

### 3. Properties of the Estimator

- **Unbiasedness:** Using two-stage sampling expectation rules, E(N̂) = N, so the integrated estimator is unbiased.
- **Variance:** Derived by decomposing the two-stage variance into a between-stage and within-stage component. The variance estimator is written as a function of (A/a)² and (n − m), with the exact expression given in the paper.

### 4. Simulation Results

- **Comparison set:** Chapman's (1951) hypergeometric-based mark-recapture estimator, area sampling alone, and the integrated estimator.
- **Population:** 10,000 individuals.
- **Proportions sampled with toxicant or detonation:** 0.01, 0.05, 0.10, and 0.20.
- **Replication:** Standard deviations were computed over 1,000 simulation runs for varying numbers marked.
- **Sample size generation:** The second-sample size *n* was drawn from a normal distribution with mean E(n) = aN/A, approximating the Poisson/hypergeometric distributions. Random-number routines followed Naylor et al. (1966).

Key simulation outcomes:

- **Mark-recapture (Chapman):** Seriously biased when *M* and *a*/*A* are small. When a small proportion of the population is marked, its standard deviations are very high.
- **When more than half the population is marked:** Mark-recapture has low bias and better precision than area sampling. The integrated estimator matches the precision of mark-recapture in this situation.
- **When fewer than half the population is marked:** Area sampling is more precise than mark-recapture. Area sampling and the integrated estimator remain unbiased.
- **Overall:** The integrated estimator is precise under both conditions. It is most useful when a moderate proportion of the population is marked and when the proportion of the population sampled with toxicant or detonation is low. Under those conditions it is more precise than either area sampling or mark-recapture alone.

### 5. Practical Conclusion

Coupling area sampling with mark-recapture, and treating only part of the sampled area with toxicant or explosive, allows reliable population estimates from a smaller treated area. This reduces the amount of chemical or explosive needed, and it avoids the bias of standard mark-recapture when few fish are marked.

### 6. Publication Details

- **Journal:** *Biometrics*, 48, 1201–1205, December 1992.
- **Dates:** Received February 1990; revised January 1991; accepted June 1991.
- **Keywords:** Area sampling; detonation sampling; fish; mark-recapture; rotenone sampling.