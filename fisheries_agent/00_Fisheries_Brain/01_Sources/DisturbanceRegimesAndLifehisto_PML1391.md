---
species: N/A
common_name: N/A
family: N/A
habitat: Disturbance-prone juvenile growth habitat and a disturbance-free adult (nongrowth) habitat; the paper is generic and not tied to a specific system
ocean_basin: N/A
location: N/A
tags: [disturbance-ecology, life-history-evolution, theoretical-ecology, metamorphosis]
title: "Disturbance Regimes and Life-History Evolution"
source_id: "PML1391"
marsh_id: "PML1391"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. A. Lytle (2001). Disturbance Regimes and Life-History Evolution. The American Naturalist, vol. 157, no. 5. Marsh Library ID: PML1391."
source_file: "Lytle D.A. 2001. distrubance regimes and life history evolution.pdf"
text_extraction: "text"
---
# Disturbance Regimes and Life-History Evolution

#disturbance-ecology #life-history-evolution #theoretical-ecology

## Executive Summary

This theoretical paper by David J. Lytle (Cornell University, 2001, *The American Naturalist*) develops a [[Disturbance Regime]] model that links the timing, [[Disturbance Predictability]], frequency and severity of disturbances to [[Life-History Evolution]]. The model asks when an organism should stop growing, metamorphose and move to a disturbance-free habitat, and at what body size. It treats both [[Coarse-Grained Disturbance]] (affecting the whole population at once) and [[Fine-Grained Disturbance]] (patch dynamics). The model is an extension of [[Rowe and Ludwig Model]] seasonal time-constraint theory and nests that model as a special case. The paper covers no empirical species; its main claims concern how disturbance regimes shape body size and metamorphosis timing, and how population structure matters only when disturbances are severe.

## Background & Description

Disturbances are known to affect coexistence, nonnative species, invasions and food web structure, but their evolutionary consequences are less well understood. The author notes it is intuitive that organisms will not adapt to events that rarely occur during their lifespan (e.g., volcanoes, large fires, big floods, storms), yet it is unclear how often disturbances must recur to drive evolutionary change.

Disturbances are classed by spatial scale:

- **Fine-grained events** affect part of a population at a time. Examples include gap formation in forest canopies, flash floods and scouring of marine benthos. Fitness is estimated with the [[Arithmetic Mean Fitness]] when patches are pooled into one breeding population.
- **Coarse-grained events** affect the whole population at once. Examples include interannual variation in growing season length or rainfall and hurricanes. Fitness is estimated with the [[Geometric Mean Fitness]].

Earlier coarse-grained models (building on Cohen's work) focus on among-year variation in plants. Other models address diapausing eggs and copepods, which hatch under fish-predation pressure. The model's parameters are:

- **Frequency (f):** the expected number of disturbances per season, with occurrences assumed to follow a [[Poisson Distribution]].
- **Severity (λ):** the expected mortality from a single disturbance, bounded between 0 and 1.
- **Timing (μ):** the mean date of disturbance, modeled as a normal distribution.
- **Predictability (σ):** the standard deviation of disturbance timing.

Survival to adulthood after *i* disturbances is (1 − λ)^i. Growth follows a logistic form, and offspring number is a function of body mass. Metamorphosis carries a fixed time cost (ρ), and seasonal time constraints reduce the value of late-season offspring.

## Ecological & Environmental Context

The paper places disturbance within life-history theory on growing-season constraints in plants and seed or egg dormancy in other organisms. The key ecological idea is that the best strategy depends on how often and how predictably harmful events occur relative to an organism's life span. Juveniles in a disturbance-prone growth habitat face mortality, and adults can escape by moving to a disturbance-free habitat.

Relevant context includes:

- Multiple emergence peaks in aquatic insects (e.g., stoneflies, mayflies) were previously attributed to multivoltinism or semivoltinism. Peckarsky et al. (in press) suggested that one mayfly pattern was instead driven by a biotic disturbance, the onset of fish predation.
- Time constraints accelerate development in several insect taxa, causing earlier maturation at smaller sizes.
- Growth-mortality trade-offs (foraging activity) influence the optimal growth rate.

## Key Findings

**Model structure and predictions**

- Under the arithmetic mean model, the optimal body size at metamorphosis (W) declines with the end of the season (Tc) even without disturbance. Disturbance with high mortality (λ = 1) changes this pattern in several ways:
  - No metamorphosis occurs when disturbances are most likely (period B).
  - The largest individuals metamorphose during the early disturbance peak (period C).
  - Very small individuals keep growing through the peak and then delay until after the disturbance peak (period D). Metamorphosis then resumes at progressively smaller sizes as Tc approaches (period F).
- **Infrequent or unpredictable disturbances have little evolutionary effect**, even when they cause high mortality. When σ is large, the optimal strategy ignores the disturbance regime, and the W(τ) curve resembles the no-mortality case.
- **Predictable disturbances (σ = 3 days in Figure 4) synchronize metamorphosis.** Individuals metamorphose just before the mean disturbance date across a wide range of body sizes, yielding highly synchronous emergence.
- **Higher disturbance frequency produces a greater decline in body size at metamorphosis.** Constant frequency with varying severity gives an inverse relationship between frequency and severity under the arithmetic mean.

**Selection strength (sensitivity analysis)**

- Selection strength, measured as the sum of squared differences between the no-disturbance and disturbance optima, is highest when disturbances are predictable (low σ).
- For slow-growing organisms, selection strength roughly doubles with each order-of-magnitude increase in growth rate, and it approaches zero at much lower σ for fast-growing organisms.
- Predictable disturbance (σ < 40 days in the example) is the realm where selection is strong. Slow-growing, long-lived organisms therefore respond more strongly to unpredictable regimes than fast-growing ones.
- Selection strength is highest for short return intervals and greatest for slow-growing organisms.

**Coarse-grained versus fine-grained disturbance**

- At low or moderate severity, the arithmetic and geometric mean models give nearly identical life histories. Population structure (relative to disturbance scale) therefore does not matter when mortality is low or moderate.
- Under geometric mean assumptions, severity has a proportionately larger effect. The term ln[1/(1 − λ)] exceeds λ, and for λ > 0.8 it is more than twice λ. As λ approaches 1, the term approaches infinity.
- **Severe coarse-grained disturbances** can completely override seasonal time constraints. Metamorphosis then coincides with the disturbance regime, and only individuals below the minimum reproductive size remain in the juvenile habitat.

**Multiple seasonal declines and synchrony**

- When disturbances are sufficiently predictable and frequent, and juvenile size variance is high, one population can metamorphose in two distinct periods: one linked to disturbance and one linked to [[Seasonal Time Constraints]].
- Disturbance can reduce variance in the timing of metamorphosis while increasing variance in body size at metamorphosis, an inverse relationship that depends on the steepness of the W(τ) curve and initial size variation.

**Assumptions and limitations**

- The model assumes logistic growth with a fixed upper limit. Non-asymptotic growth could change results, although disturbance would still produce some decline in size.
- The model assumes mortality comes only from disturbance, with no size-dependent mortality. The author notes that size-specific mortality could favor different patterns.
- The model assumes constant growth rates. The author argues development rate may be more flexible than growth rate, and proposes more sophisticated models that optimize both.
- The author suggests the framework could help identify critical frequency ranges for disturbance and could be extended to include spatial, behavioral, or other evolutionary processes.