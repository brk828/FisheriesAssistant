---
species:
  - "Panthera leo"
  - "Rangifer tarandus"
  - "Cervus elaphus"
common_name:
  - "African lion"
  - "Caribou"
  - "Red deer"
family: "N/A"
habitat: "N/A (multi-habitat dataset; habitat types not specified per species)"
ocean_basin: "Two ocean basins (not named)"
location: "Six continents (not named); global Global Population Dynamics Database"
tags:
  - ichthyology
  - marine-biology
  - population-dynamics
  - extinction-risk
  - metapopulation
title: "Characterizing extinction risks for 758 species"
source_id: "16299"
minckley_id: "16299"
source_citation: "W. Fagan, E. Meir, J. Prendergast, A. Folarin and P. Karieva (n.d.). Characterizing extinction risks for 758 species. Minckley Library ID: 16299."
source_file: "16299.pdf"
text_extraction: "ocr"
---
# Characterizing Extinction Risks for 758 Species

#ichthyology #marine-biology #population-dynamics #extinction-risk

## Executive Summary

This paper classifies extinction risk for 758 species, using 1941 population time series from the [[Global Population Dynamics Database]]. The taxa are [[Mammals]], [[Birds]], [[Marine Fish]], and [[Lepidopterans]]. Using the [[Variation Threshold]] concept from [[Fagan Et Al 1999]], species are sorted into [[Extinction Category|extinction categories]]: [[Persistent Species]], [[Dispersal-Dependent Species]], and [[Carrying Capacity-Dependent Species]]. About 90% of species fluctuate enough that extinction is a real possibility over a 100-year horizon, which points to [[Metapopulation Dynamics]] as the main route to persistence. Life history traits (body size, age at first reproduction, offspring number) predicted extinction category well for mammals (83%) but poorly for birds (49%). The authors propose these traits as surrogates for data-poor species in [[Conservation Planning]].

## Background & Description

- **Theoretical basis:** The paper builds on [[R- And K-Selection]] theory and the observed link between life history attributes and population dynamics (colonization ability, extinction risk). Cited sources include Elton 1958, MacArthur and Wilson 1967, Pianka 1970, and Boyce 1984 (the reference list gives 1985 in the text).
- **Three extinction categories** (after Fagan et al. 1999):
  1. Weakly varying populations with high growth rates, where long-term persistence is likely unless an extreme catastrophe occurs.
  2. Populations with low growth rates, where average population size must be large to buffer against extinction in a variable environment.
  3. Highly variable populations that likely depend on dispersal to avoid extinction.
- **Model basis:** Fagan et al. (1999) used [[Ricker Model]], [[Hassell Model]], and exponential growth to a ceiling. For each model, a variation threshold was defined as the level above which there is a greater than 5% chance of extinction in 100 years.
- **Data source:** The [[Global Population Dynamics Database]] (NERC CPB 1999; Kendall et al. 1998). Time series had to be at least 15 years long.
- **Purpose:** Many species lack the data needed for [[Population Viability Analysis]], but large-scale conservation planning urgently needs at least a coarse extinction-risk category for each species.

## Ecological & Environmental Context

- **Population dynamics parameters:** Each time series was fitted with a Ricker model to estimate r (intrinsic rate of increase) and σ (environmental variability), using maximum likelihood under normally distributed process error. Large σ/r ratios predispose populations to extinction. Small σ/r ratios indicate high resilience.
- **Time series length:** Series had between 8 and 138 transitions (median = 18).
- **Closed-population assumption:** Many series count entire populations, while others estimate population size in a region or habitat block. Because the model includes no immigration or emigration, all series were treated as closed populations.
- **Spatial scope:** Species came from six continents and two ocean basins.
- **Conservation relevance:** Multiple population "representations" in a [[Nature Reserve System]] provide colonists and act as a hedge against variability, even when variability itself cannot be managed. Reserve area matters most for carrying capacity-dependent species.

## Key Findings

**Dataset and overall risk**
- 1941 time series representing 758 species were analyzed.
- About 90% of species (nearly 90% in the results) exhibit variability so high that even large carrying capacities cannot buffer them against extinction over 100 years.
- Only a small share of species fall into the carrying capacity-dependent region: 6 of 415 lepidopterans, 8 of 86 mammals, 26 of 166 birds, and 19 of 91 fishes.
- Fraction of species in the extinction-prone (dispersal-dependent) category: 97% of lepidopterans, roughly 80% of birds, 75% of fish, and 88% of mammals.

**Table 1: Key extinction risk parameters (as reported)**

| Group | Species (n) | r Mean | r Median | r Range | r 95% CI | σ/r Mean | σ/r Median | σ/r Range | σ/r 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| Mammals | 86 | 0.63 | 0.61 | 0.02–1.47 | 0.07 | 1.50 | 1.15 | 0.09–14.49 | 0.35 |
| Birds | 166 | 0.44 | 0.42 | 0.08–1.34 | 0.03 | 1.16 | 0.92 | 0.13–5.13 | 0.13 |
| Fishes | 91 | 0.62 | 0.60 | 0.05–1.44 | 0.08 | 2.04 | 1.36 | 0.20–12.57 | 0.43 |
| Lepidopterans | 415 | 0.64 | 0.57 | 0.22–3.19 | 0.03 | 1.19 | 1.03 | 0.20–6.17 | 0.07 |

**Predicting extinction category from life history**
- Mammals: Linear discriminant analysis using adult fresh mass, mean number of offspring, and age at first reproduction correctly predicted the Ricker-derived extinction category for 83% of the 72 mammal species (60 of 72). This included all 8 carrying capacity-dependent species, such as the [[African Lion]] (*Panthera leo*), [[Caribou]] (*Rangifer tarandus*), and [[Red Deer]] (*Cervus elaphus*).
- Birds: The same approach correctly classified only 49% of the 80 bird species.
- Birds classified as dispersal-dependent by life history: 27 of 31 (87%) showed dispersal-dependent dynamics. Misclassified birds were often assigned to the carrying capacity-dependent category when their observed dynamics were too variable for that label.
- The authors suspect long-range migration and longevity unrelated to body mass complicate bird dynamics more than in other taxa.

**Conservation implications**
- Dispersal among populations is a key contributor to persistence for most species, so planners need rules of thumb for how many populations are "enough" and how spatial configuration aids dispersal.
- For mammals, life history traits may indicate whether large reserves (rather than many small reserves) are a key strategy.
- Life history traits offer some statistical predictive power, which is not new as an idea but is new in its application to conservation planning.
- Larger databases may allow refined predictors that combine [[Taxonomy]] and life history traits into a portrait of "most likely" population dynamics.