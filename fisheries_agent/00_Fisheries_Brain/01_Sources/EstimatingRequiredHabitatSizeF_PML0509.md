---
species:
  - "Oncorhynchus clarkii virginalis"
  - "Oncorhynchus clarkii lewisi"
  - "Oncorhynchus clarkii utah"
  - "Oncorhynchus clarkii stomias"
  - "Catostomus plebeius"
  - "Salmo trutta"
common_name: "Rio Grande cutthroat trout"
family: "Salmonidae"
habitat: "Small, cold headwater streams; fragmented high-elevation habitats"
ocean_basin: "N/A"
location: "Rio Grande drainage, New Mexico and Colorado, USA"
tags:
  - ichthyology
  - marine-biology
  - salmonidae
  - habitat-size
  - population-viability
  - conservation
title: "Estimating required habitat size for fish conservation in streams"
source_id: "PML0509"
marsh_id: "PML0509"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. E. Cowley (2008). Estimating required habitat size for fish conservation in streams. Aquatic Conservation: Marine and Freshwater Ecosystems 18: 418-431. Marsh Library ID: PML0509."
source_file: "Cowley D.E. 2008. Estimating required habitat size for fish conservation in streams.pdf"
text_extraction: "text"
---
# Estimating Required Habitat Size for Rio Grande Cutthroat Trout Conservation

#ichthyology #marine-biology #salmonidae

## Executive Summary

This study presents a [[Monte Carlo Simulation]] procedure for estimating the [[Minimum Viable Population Size]] and the stream habitat area required to sustain a [[Rio Grande Cutthroat Trout]] population. Viability was defined as an extinction rate below 10% over 100 years and a long-term [[Effective Population Size]] of at least 500 breeding adults. The model combined demographic stochasticity with random population-wide failures of age class 0 (young of year) to represent poor habitat years. The procedure is presented as general enough for any species with adequate population and demographic data.

The minimum viable population was 2750 fish, which at the median density of 1250 fish per hectare requires 2.2 ha of habitat. Required habitat rose sharply as [[Age Class 0 Failure]] rates increased and as fry-to-age-1 survival declined. The author concludes that managers should not aim for the smallest possible viable population, and that habitat restoration improving young-of-year survival is a sound strategy.

## Background & Description

Habitat destruction and fragmentation have confined many native trout of western North America to high-elevation headwaters. Mountain ranges and arid lands act as barriers, while exotic species have further degraded native populations. The Rio Grande cutthroat trout is one of 14 cutthroat trout subspecies native to western North America (Behnke, 1992). It has declined sharply over the past century, although its population trend was reported as stable at the time of the study.

Populations occupy small headwater streams with little opportunity for migration between populations. Such isolation raises the risk of [[Genetic Drift]] and of artificial selection imposed by migration barriers. Management has relied on barriers to protect native populations and on [[Restoration Translocation]] into suitable habitats. Over half of [[Greenback Cutthroat Trout]] and Rio Grande cutthroat trout restoration projects failed to establish self-sustaining populations (Harig et al., 1999).

The paper frames viability using [[Effective Population Size]] (Ne), which is linked to inbreeding, genetic variance and adaptability. Published thresholds vary: 50 for limiting loss of diversity, 500 for retaining adaptive potential, 1000 for genetic security, and 5000 for avoiding long-term mutation effects (Frankel and Soule, 1981; Franklin, 1980; Lande, 1995b; National Research Council, 2002). The study adopts a long-term Ne of at least 500.

## Ecological & Environmental Context

- **Threats:** Drought and climate change, livestock grazing, elk management, and introductions of non-native trout for recreational fishing place isolated populations at risk of local extinction.
- **Stream conditions:** Most occupied New Mexico streams are narrow, with a mean width of about 2 m. Cold summer water temperatures, a lack of deep pools, and reinvasion by non-native salmonids limit translocation success.
- **Associated fauna:** Rio Grande cutthroat trout are members of an indigenous montane assemblage with [[Rio Grande Sucker]] (*Catostomus plebeius*). Competition between the two was reported by Shemai (2004). Other species recorded at surveyed sites include longnose dace (*Rhinichthys cataractae*), white sucker (*Catostomus commersoni*) and brown trout (*Salmo trutta*).
- **Catastrophes:** The model did not address wildfire, drought or episodic pollution, which can extirpate whole populations and may affect several populations at once.
- **Reference populations:** Four relatively unexploited populations in remote streams of the San Pedro Parks Wilderness (Rio de las Vacas, Rito Cafe, Rito de las Perchas, Rio Puerco west) were used as proxies for stable, viable populations.

## Key Findings

### Data and model inputs

- **Density:** Surveys of 37 New Mexico populations by [[Electrofishing Depletion Surveys]] gave densities from 166 to 13,545 fish/ha, with a mean of 2431 and a median of 1250. The median was used as the more typical value because the distribution is strongly right-skewed.
- **Fecundity:** Regression of log egg number on log total length (n = 148 wild females) gave log(eggs) = −7.49 + 2.50 log(total length), with p < 0.001 and R² = 0.44. Mean fecundity was 255 eggs per female (95% CI 237–275), and mean female length was 183.5 mm. Only 9% of age 2 females were assumed to spawn, and all older females were assumed to spawn.
- **Survival:** Egg-to-fry survival was fixed at 0.1. Fry-to-age-1 survival was not measured for this subspecies, so values of 0.1, 0.3, 0.6 and 0.9 were tested. Survival from age 1 onward was estimated from the four reference populations.
- **Adult proportion:** Adults made up about 0.2 of the reference populations, which gave an initial target population of 2500 (500 / 0.2).

### Simulation design

- **Model:** An age-based transition matrix with a [[Density Dependence]] term based on Ricker's over-compensatory form. Survival used beta-distributed deviates and fecundity used lognormal deviates (coefficient of variation of 20%) to represent [[Demographic Stochasticity]].
- **Failure scenarios:** Age class 0 failure rates ranged from 0 to 0.6 in steps of 0.1. The 0.6 level was the value accepted in the greenback cutthroat trout recovery plan and adopted by Colorado for Rio Grande cutthroat trout management.
- **Replication:** Each scenario ran for 100 years with 10,000 replicates. Long-term Ne was calculated from the heterozygosity decay relationship of Crow and Kimura (1970), with adult count used as the annual Ne.

### Viable population size

- **Initial estimate:** At N = 2500 with fry-to-age-1 survival of 0.9 and no age class 0 failures, mean long-term Ne was 477, below the target of 500. The initial estimate therefore did not meet the goal.
- **Minimum viable population:** Interpolation across population sizes of 2500 to 50,000 gave a minimum of 2750 fish at fry-to-age-1 survival of 0.9 with no failures.
- **Trend:** Viable population size increased as fry-to-age-1 survival declined.
- **Failure effects:** Extinction rates below 10% at N = 250 held only when age class 0 failure was below 0.3. At 0.6 failure, extinction was nearly certain at small sizes and exceeded 90% even at N = 25,000.

### Required habitat size

Habitat area was calculated by dividing viable population size by median density (1250 fish/ha).

| Scenario | Required habitat |
|---|---|
| Fry-to-age-1 survival 0.9, no age class 0 failure | 2.2 ha (≈11 km of 2 m stream) |
| Fry-to-age-1 survival 0.6, age class 0 failure 0.1 | 3.2 ha |
| Fry-to-age-1 survival 0.6, age class 0 failure 0.2 | 6.7 ha |
| Fry-to-age-1 survival 0.6, age class 0 failure 0.3 | 56.0 ha |

### Management implications

- **Avoid minimum targets:** Managers should not target the smallest viable population. Temporal variation in demography and habitat quality pushes requirements well above the minimum.
- **Improve young-of-year survival:** Habitat restoration that raises survival of young of year would increase effective size over the long term.
- **Rank candidate streams:** Required habitat size can rank streams for new populations. Streams should be compared with habitat estimates before translocation.
- **Assess status:** A 2002 candidate status review used the procedure, along with other data, to identify 13 viable populations of Rio Grande cutthroat trout (U.S. Fish and Wildlife Service, 2002). The New Mexico Department of Game and Fish also classifies populations as meeting criteria, below criteria, or having insufficient data.

### Comparison with other studies

- **Reed et al. (2003):** The suggested minimum of about 7000 vertebrates was exceeded only for lower-quality habitat. The author suggests managing Rio Grande cutthroat trout at 8000–16,000 fish for low age class 0 failure and intermediate fry-to-age-1 survival.
- **Hilderbrand and Kershner (2000):** The required 11 km of stream exceeds their minimum stream length of 8 km for cutthroat trout.
- **Greenback cutthroat trout:** The author agrees with Young and Harig (2001) that a 0.6 age class 0 failure rate is unacceptably high for recovery.
- **Limits of Ne:** Rieman and Allendorf (2001) recommended 1000 spawning adults per year for bull trout. Factors such as unequal sex ratios, variance in progeny number and overlapping generations would reduce effective size, so the estimates here are best-case values.

### Limitations

The model is a generalized statistical representation rather than a population-specific analysis. Population-specific [[Population Viability Analysis]] is recommended for predicting the fate of a particular stream population. Effective size was estimated from a simple count of adults, which likely overstates Ne.