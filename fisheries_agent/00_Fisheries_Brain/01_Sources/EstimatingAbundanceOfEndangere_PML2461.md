---
species:
  - Cyprinella formosa
  - Gila purpurae
  - Poeciliopsis occidentalis sonoriensis
common_name:
  - Beautiful shiner
  - Yaqui chub
  - Yaqui topminnow
family: N/A
habitat: Spring-fed ponds, streams, and cienegas (spring-fed marshes) of the Rio Yaqui watershed
ocean_basin: N/A (freshwater)
location: San Bernardino National Wildlife Refuge and nearby private properties, southeastern Arizona, USA (31.34°N, 109.25°W), and Sonora, Mexico
tags:
  - ichthyology
  - marine-biology
  - cyprinidae
  - poeciliidae
  - endangered-species
  - abundance-estimation
title: "Estimating abundance of endangered fish by eliminating bias from non-constant detectability"
source_id: "PML2461"
marsh_id: "PML2461"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. R. Stewart, M. J. Butler, G. Harris, L. A. Johnson, W. R. Radke (2017). Estimating abundance of endangered fish by eliminating bias from non-constant detectability. Endangered Species Research, vol. 32, pp. 187-201. Marsh Library ID: PML2461."
source_file: "Stewart D.R. et al. 2017. Estimating abundance of endangered fish by eliminating bias from non constant detectability .pdf"
text_extraction: "text"
---
# Eliminating Bias in Abundance Estimates for Endangered Rio Yaqui Fishes

#ichthyology #marine-biology #cyprinidae #poeciliidae

## Executive Summary

This study evaluates and redesigns the monitoring of three endangered or threatened freshwater fishes endemic to the [[Rio Yaqui Watershed]] in southeastern Arizona and Sonora, Mexico: the [[Yaqui Topminnow]], the [[Yaqui Chub]], and the [[Beautiful Shiner]]. The authors argue that standardized sampling with [[Gee Funnel Minnow Trap]]s, which assumes constant [[Detection Probability]], produces catch indices that can misrepresent true abundance, habitat relationships, and population trends. Using historical data (2005–2014) and a 2015 experimental survey, they assessed trap numbers, [[Soak Duration]], and site-level correlates of detectability, then used a [[Bayesian Mixture Model]] to produce bias-corrected abundance estimates. Simulations showed that ignoring [[Variable Detectability]] raised the Type I error rate to 50% and reduced [[Statistical Power]] to about 0.75 under a doubling of population.

## Background & Description

- **Conservation status:** Worldwide, about half of freshwater fishes are threatened or data deficient. The IUCN Red List cited in the paper includes 3120 freshwater fishes, of which 1147 (37%) are threatened and 431 (14%) are data deficient.
- **Study species:** Of seven fishes endemic to the Rio Yaqui watershed near [[San Bernardino National Wildlife Refuge]], the Yaqui topminnow and Yaqui chub are federally listed as endangered, while the beautiful shiner (and the Yaqui catfish) is federally listed as threatened. Recovery criteria call for at least 10 years of self-sustaining populations on refuge lands before downlisting or delisting.
- **Monitoring history:** From 2004 to 2014, federal, state, and conservation partners monitored these fishes annually using a standardized design with 8 to 30 traps per pond, depending on pond size.
- **Objectives:** The authors sought to (1) determine the minimum effective number of trap deployments, (2) optimize soak times, (3) build models that link detection and abundance to site covariates, and (4) test how variable detectability affects raw-count trend detection.
- **Study area:** Refuge lands were established in 1982 to conserve Rio Yaqui fishes, which historically occupied streams, cienegas, pools, and [[Spring-Fed Ponds]] fed by artesian wells. Ponds were shallow (roughly 0.4 to about 4 m deep), clear, and dominated by submergent vegetation such as spiny naiad (*Najas minor*), sago pondweed (*Potamogeton pectinatus*), coontail (*Ceratophyllum demersum*), and horned pondweed (*Zannichellia palustris*).

## Ecological & Environmental Context

- **Habitat structure:** Fish were sampled in ponds stratified by vegetation and depth. Depth strata were deep (>60 cm) and shallow (<60 cm). Pond location relative to the inlet or outlet was also recorded to assess spatial structuring.
- **Detectability drivers:** Dense [[Submergent Aquatic Vegetation]] appears to envelop trap funnels and reduce capture. Water temperature, net depth, and inlet proximity also influenced detection and abundance.
- **Species-habitat patterns:** Beautiful shiner and Yaqui chub had peak abundances in deep, cooler, less-vegetated water (>140 cm in the reported peak). Yaqui topminnows were mainly in shallow water (<70 cm) and open areas with little vegetation (<60%). The authors note that the competition and predation effects among these species are unknown.
- **Management implication:** Because the beautiful shiner and Yaqui chub share deep, cool, sparsely vegetated habitat, managing one may affect the other, and this interaction should be considered in planning.

## Key Findings

**Historical design (Objective 1: [[Minimum Effective Number of Traps]])**
- Catch was highly variable among ponds and years. Median catch per site was 162 Yaqui chub (range 3–832) and 178 Yaqui topminnow (range 12–1132). Coefficients of variation ranged from 0.56 to 4.75, and [[Relative Standard Error]] (RSE) ranged from 0.14 to 1.15.
- Annual sampling rarely reached the RSE target of 25%. The [[Resampling Analysis]] indicated that about 40 traps per pond would be needed to reach RSE < 25% for both species. Fewer than 25 traps reached this target in at least 40% of resamples.
- Log-linear mixed-effects models showed that the required number of traps was strongly related to CV. The CV model predicted about 39 traps per pond at a mean CV of 1.50. The catch model predicted about 45 traps per pond at a mean catch of 200 fish. The best model included a random year effect.
- Worked example from the Discussion: a pilot effort of 10 traps capturing 300 Yaqui chub would require about 31 traps. If CV were about 3.2, about 113 traps would be needed.

**Soak time experiment (Objective 2: [[Crossover Sampling Design]])**
- The 2015 experiment used 12 ponds, 12 traps per pond, and about 7 h of sampling per pond, split into 2 h and 4 h soak periods separated by a 1 h rest.
- Total catch was 9723 fish from 24 trap deployments: Yaqui topminnow 9021 (93%), Yaqui chub 460 (5%), and beautiful shiner 242 (2%).
- Traps set for 4 h caught more fish overall (mean 23.55, SD 64.59, n = 5652) than traps set for 2 h (mean 16.69, SD 58.73, n = 4071). The species × duration interaction was significant (F = 7.25, p = 0.01).
- The 4 h soak significantly increased catch of beautiful shiner (Tukey's HSD = 2.70, p < 0.01) and Yaqui topminnow (Tukey's HSD = 2.63, p < 0.01). Yaqui chub catch did not differ significantly (Tukey's HSD = 1.86, p > 0.05). Carryover, period, and sequence effects were not significant.

**Detection and abundance (Objective 3)**
- Estimated detection probabilities ranged from 0.06 to 0.25 for beautiful shiner, 0.14 to 0.83 for Yaqui chub, and 0.05 to 0.34 for Yaqui topminnow.
- The 4 h soak increased detection for all three species, by about 75% for beautiful shiner and roughly twofold for Yaqui chub and Yaqui topminnow. The Discussion gives the shiner improvement as 43 to 70%.
- Detectability rose while abundance fell as water temperature increased. Detection went from 0 to 25% at 16 °C to 100% by 19 °C, while abundance of all species fell by 70% across the same span.
- Submergent vegetation reduced detection for beautiful shiner (about 78% at 10% cover vs. 26% at 80%) and Yaqui topminnow (94% vs. 85%). Yaqui chub abundance dropped from 175 at 10% cover to 0 at 80%.
- Beautiful shiner detection declined with net depth while its abundance increased. Yaqui chub detection and abundance both increased with depth. Yaqui topminnow detection fell from 90% at 25 cm to 76% at 500 cm.
- Relative to inlet-distant areas, beautiful shiner were about 10 times more abundant near inlets, Yaqui topminnow were 200 to 600 times more abundant, and Yaqui chub were about 1.5 times more abundant.

**Simulation of variable detectability (Objective 4: [[Type I Error]] and [[Statistical Power]])**
- Simulations used 6 to 120 sites over 3000 replicate datasets, with a 100% population increase in the post-change year.
- **Constant detection:** The Type I error rate was 5%, and power exceeded 0.9.
- **Variable detection assumed constant:** The Type I error rate rose to 50%, and power declined to about 0.75.
- Spurious change detection was highest for beautiful shiner (0.72) and Yaqui topminnow (0.80). Adding more traps increased the chance of detecting spurious change, because more samples made estimates more precise but still biased.

**Conclusions and recommendations**
- Fixed annual trap numbers are inadequate. Trap effort should track observed variability in catch (adaptive sampling) rather than pond size. On average, about 20 more samples per year than historically used were needed.
- Soak duration should be increased to 4 h to better detect the rarer beautiful shiner.
- Mixture models that integrate over heterogeneous detection should be used to estimate true abundance, and power analyses should be run before any survey.
- The authors warn that simple counts could mislead management. For example, uncorrected counts would suggest beautiful shiner are more abundant in shallow water, when detection-corrected data show the reverse.
- The same concern applies to other monitored endangered fishes, such as the [[Desert Pupfish]] and [[Kendall Warm Springs Dace]].