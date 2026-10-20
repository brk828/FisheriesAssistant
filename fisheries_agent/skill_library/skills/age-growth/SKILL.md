---
name: age-growth
description: Age determination, back-calculation and growth models (von Bertalanffy) with R workflow and checks.
status: draft
generated: 2026-10-20
---

# age-growth

## When to use

Use this skill when determining fish age from hard structures, validating age estimates, constructing age-length keys, fitting von Bertalanffy growth models, or conducting back-calculation of length at previous ages. This workflow applies to studies requiring growth parameter estimation, age-structure analysis, or validation of ageing methodologies for fisheries stock assessment.

## Age determination and validation

Otoliths are the preferred structure for age determination in many species [[ProposalToDetermineAgesAndPatt_1986_06_15]]. Multiple independent studies found scale-based age estimates for Colorado River big-river fishes to be inaccurate or internally inconsistent [[ProposalToDetermineAgesAndPatt_1986_06_15]]. McCarthy (1986) cross-validated otolith-based aging against known-age hatchery Razorback Sucker, confirming otoliths as the superior structure for age and growth determination, with a strong otolith radius–standard length correlation supporting back-calculation methods [[ProposalToDetermineAgesAndPatt_1986_06_15]].

Age determination is more reliable for identifying relative "old age" (e.g., >10 years) than for pinpointing exact age [[AgeEstimationFromOtolithsOfBon_1997_02_24]]. For subadults, scale-based aging may be feasible in some species, though disruption of scale circuli can occur when fish move between water masses of different temperatures [[LifeHistoryAndEcologyOfTheHump_1995_06_30]]. Validation against otoliths is recommended [[LifeHistoryAndEcologyOfTheHump_1995_06_30]].

Validation should use a larger series of known-age hatchery fish [[AgeEstimationFromOtolithsOfBon_1997_02_24]]. Maintaining accurate, centralized, and complete individual fish records (capture, transfer, holding, release, death) supports future age and origin analyses [[AgeEstimationFromOtolithsOfBon_1997_02_24]]. Non-lethal genetic methodologies may serve as an alternative or complement to otolith extraction for determining origin [[AgeEstimationFromOtolithsOfBon_1997_02_24]].

## Age-length keys

Distinct year or age classes may not be resolvable from length-frequency data alone [[PreliminaryStudiesOfTheShadAlo_15433]]. In Connecticut River shad (n=4,724), the overall length distribution approximated a bell curve with a peak at 18 inches total length [[PreliminaryStudiesOfTheShadAlo_15433]]. Average length of females exceeded average length of males, and average length of the catch shifted progressively as the season advanced [[PreliminaryStudiesOfTheShadAlo_15433]].

Size-class segregation can be used to define age classes for comparative analysis [[TheDietOfJuvenileAndAdultStrip_1967]]. For example, striped bass age classes were defined as: Age I (juvenile) 6–10 inches, Age II (juvenile) 11–15 inches, and Age III+ (adult) ≥16 inches [[TheDietOfJuvenileAndAdultStrip_1967]].

## Growth models

The von Bertalanffy growth model is widely applied to fisheries data [[AnEvaluationOfStripedBassAngli_1969]] [[PopulationDynamicsTrophicInter_2003]] [[BayesianEstimationOfVonBertala_2025]]. Growth parameters can be fitted separately by sex [[AnEvaluationOfStripedBassAngli_1969]] [[PopulationDynamicsTrophicInter_2003]]. 

A sex-specific Bayesian hierarchical formulation of the von Bertalanffy Growth Model extends prior work to account for ageing error from multiple readers and compare multiple ageing structures [[BayesianEstimationOfVonBertala_2025]]. This approach addresses how biased age estimates from different ageing protocols affect growth parameter estimates used in stock assessments [[BayesianEstimationOfVonBertala_2025]].

Growth rates can be compared to international standards to evaluate population-specific patterns [[PopulationDynamicsTrophicInter_2003]]. Linear growth models can reveal whether variation in growth increments is attributable to age effects, year effects, or environmental variation [[PopulationDynamicsTrophicInter_2003]].

## Back-calculation

The fundamental assumption underlying back-calculation of growth is that scale growth and fish body growth are directly proportional (isometric) [[TheUseOfTheScalesOfTheBrownTro_12553]]. However, growth is frequently allometric rather than isometric, particularly in fish under 10 cm [[TheUseOfTheScalesOfTheBrownTro_12553]]. 

The degree of allometry appears correlated with growth rate, with faster-growing populations (e.g., hatchery fish) approaching isometry, while slower-growing populations show strongly allometric relationships [[TheUseOfTheScalesOfTheBrownTro_12553]]. Researchers should quantify potential errors introduced by allometric growth when conducting back-calculations [[TheUseOfTheScalesOfTheBrownTro_12553]].

A strong otolith radius–standard length correlation supports back-calculation methods [[ProposalToDetermineAgesAndPatt_1986_06_15]].

## Bayesian and multi-reader approaches

Accurate estimation of growth parameters while accounting for ageing error from multiple readers can be accomplished using Bayesian hierarchical models [[BayesianEstimationOfVonBertala_2025]]. This approach simultaneously compares multiple ageing protocols (e.g., whole otoliths, dorsal spine methods) [[BayesianEstimationOfVonBertala_2025]].

The method extends established frameworks (Cope and Punt 2007, Chamberlin et al. 2023b) to address how biased age estimates from different readers or structures affect growth parameter estimates [[BayesianEstimationOfVonBertala_2025]].

## Workflow in R

1. Load the project's own age and length files as described in `data_summary.md` (FSA, a CRAN package of fisheries stock-assessment functions [[web:cran-FSA]], is used later for analysis; FSAdata only supplies example datasets [[web:cran-FSAdata]] and is not for project data)
2. Validate age estimates by comparing structures or readers using multi-reader hierarchical models (unsourced)
3. Construct age-length keys and examine length-frequency distributions (unsourced)
4. Fit von Bertalanffy growth models using nonlinear regression with **nlstools** [[web:cran-nlstools]]
5. For Bayesian approaches, fit hierarchical growth models with **brms** [[web:cran-brms]] or **TMB** [[web:cran-TMB]]
6. Conduct back-calculation of length at age, testing for allometric versus isometric growth relationships (unsourced)
7. Compare growth parameters between sexes, populations, or against reference standards (unsourced)
