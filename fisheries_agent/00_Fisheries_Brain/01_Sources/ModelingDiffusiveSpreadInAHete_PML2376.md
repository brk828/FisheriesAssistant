---
species:
  - Nocomis leptocephalus
  - Semotilus atromaculatus
  - Lepomis auritus
  - Clinostomus funduloides
common_name:
  - Bluehead Chub
  - Creek Chub
  - Redbreast Sunfish
  - Rosyside Dace
family:
  - Cyprinidae
  - Centrarchidae
habitat: Small temperate stream (Durant Creek), pools and runs
ocean_basin: N/A
location: Durant Nature Park, Raleigh, North Carolina, USA
tags:
  - ecology
  - fish-movement
  - dispersal
  - stream-fish
  - leptokurtosis
title: "Modeling diffusive spread in a heterogeneous population: a movement study with stream fish"
source_id: "PML2376"
marsh_id: "PML2376"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. T. Skalski, J. F. Gilliam (2000). Modeling diffusive spread in a heterogeneous population: a movement study with stream fish. Ecology, 81(6), 1685-1700. Marsh Library ID: PML2376."
source_file: "Skalski G.T. et al. 2000. Modeling diffusive spread in a hetergeneous population .pdf"
text_extraction: "text"
---
# Modeling Diffusive Spread in a Heterogeneous Population: A Movement Study with Stream Fish

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This study uses a five-month mark-recapture experiment in [[Durant Creek]], a small temperate stream in Raleigh, North Carolina, to describe how four stream fish species move and to test a mechanistic explanation for the leptokurtic (peaked, long-tailed) movement distributions commonly seen in field studies. The authors compare the observed spread with the classic [[Skellam Diffusion Model]], which predicts normally distributed displacements, and with a [[Diffusion-Advection Model]] that includes two subgroups of fish dispersing at different rates ("fast" and "slow" fish). The heterogeneous model reproduces the observed leptokurtosis and upstream bias; the homogeneous model does not. The authors argue that individual heterogeneity in size and growth may underlie population-level dispersal patterns.

## Background & Description

Dispersal is a key process in population dynamics, metapopulation persistence, predator-prey and competitive interactions, invasion management and biocontrol. Mathematical dispersal theory has been developed extensively, but empirical validation has been limited because following large numbers of organisms through space and time is difficult. Stream fish communities offer practical advantages for movement studies: several species occur at sufficient densities, individuals can be marked, animals can be observed at natural densities, and small streams approximate one-dimensional habitats, which simplifies analysis.

The study adopts both a [[Lagrangian Perspective]] (tracking individuals) and a [[Eulerian Perspective]] (population-level spread). Individual fish were marked with [[Elastomer Tagging]], a fluorescent liquid that hardens into a visible, flexible implant. Of 610 marked fish (all over 40 mm total length), 478 recaptures were recorded, representing 237 different individuals. Fourteen fish species were captured; four yielded enough data for analysis:

- Bluehead chub: 216 recaptures (most abundant)
- Creek chub: 124 recaptures
- Redbreast sunfish: 51 recaptures
- Rosyside dace: 28 recaptures

Sampling ran from 15 March to 15 August 1996 at roughly monthly intervals, six sampling occasions in total, across 37 sites in a 400-m section of the creek. Fish were captured by [[Backpack Electrofishing]] with block nets, and movement was measured in units of sampling sites (patches).

## Ecological & Environmental Context

Durant Creek is a 1-km reach flowing through secondary-succession hardwood forest in the park; headwaters drain suburban residential areas, and the creek showed sediment deposition and flash flood effects. Depths ranged from about 2 cm in riffles to 1.5 m in pools, with widths of 1 to 4 m. Substrates ranged from sand to bedrock, and the channel alternated among riffles, runs and pools. Aquatic insect densities appeared low, though caddisflies, dobsonflies, cranefly larvae, water striders, midges and damselflies were observed; [[Crayfish]] (Cambaridae) were the most frequently seen invertebrates.

Bluehead chubs and creek chubs were considered residents, based on observations of adults and abundant young-of-the-year. The other species may have been immigrants from downstream areas and reservoirs. Fish were held in mesh baskets, anesthetized in MS-222 for tagging and measurement, and released in cover near the capture point.

## Key Findings

**Movement patterns**
- Movement distributions for all four species deviated significantly from normality (D'Agostino's test, P < 0.01) and were leptokurtic: higher peaks and longer tails than a normal distribution.
- Bluehead chub showed a clear upstream bias (χ² = 7.19, df = 1, P = 0.0073); rosyside dace were also more likely to move upstream. Creek chub and redbreast sunfish showed no directional bias.
- Median distances moved downstream and upstream did not differ significantly for any species.

**Species, time and size effects**
- Neither species nor time had strong effects on movement distributions; bluehead and creek chub distributions did not differ in any recapture interval.
- For bluehead chubs, probability of movement varied with size and growth, with a significant size × growth interaction (χ² = 6.42, P = 0.0113): movement probability increased with size in slow-growing fish and decreased with size in fast-growing fish.
- For creek chubs, probability of movement was related to size (χ² = 11.22, P = 0.0008) but not to growth.
- Growth of individual bluehead chubs was positively correlated between consecutive intervals (P < 0.0001); creek chub growth was not significantly correlated.
- Among movers, size and growth had little relationship with distance moved, except that redbreast sunfish showed a negative size–distance relationship (R_s = -0.6844, N = 14, P = 0.0069).

**Temporal correlations**
- No significant temporal correlations in movement probability, direction, or distance were found for bluehead and creek chubs combined (e.g., χ² = 1.97, P = 0.5787 for movement probability; Spearman R_s = 0.0590, P = 0.59).

**Spatial spread through time**
- Variance of movement distributions increased linearly with time for both chub species, consistent with simple diffusion (bluehead linear term P = 0.002; creek chub P = 0.0053). Intercepts and quadratic terms were not significant.
- Bluehead chubs showed upstream bias and leptokurtosis across all four months; creek chub leptokurtosis declined over time and vanished by the fourth month.

**Model results**
- The [[Homogeneity Model]] (single-subgroup diffusion-advection) could not reproduce the peaked, long-tailed distributions and overestimated the frequency of moves of intermediate length.
- The two-subgroup [[Heterogeneity Model]] was statistically indistinguishable from field data after three months (D = 0.1349, N = 59, P > 0.20) and four months (D = 0.1478, N = 32, P > 0.20).
- Adding a third subgroup significantly improved fit (χ² = 15.96, df = 3, P = 0.0012) but only slightly, raising concerns about [[Parameter Explosion]].
- The model suggests that fast fish dispersed with a much larger diffusion coefficient than slow fish, and that the fast-fish subgroup comprised about 52% of the population.

**Conclusions and implications**
- Heterogeneity in fitness-influencing traits such as size and growth may explain heterogeneity in individual movement, which in turn can generate leptokurtosis at the population level.
- Population heterogeneity may affect invasion speed and rate of spread; leptokurtic distributions can allow faster spread than normal-distribution models predict.
- Future work should link individual-level behavior to population dispersal, test exchange rates between subgroups, and assess environmental versus genetic causes of heterogeneity.