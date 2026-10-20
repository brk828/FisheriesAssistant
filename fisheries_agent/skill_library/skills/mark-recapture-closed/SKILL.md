---
name: mark-recapture-closed
description: Abundance from closed-population capture-recapture (Lincoln-Petersen, Chapman, Schnabel, Huggins), with assumptions, diagnostics and R workflow.
status: draft
generated: 2026-10-20
---

# mark-recapture-closed

## When to use

Closed-population mark-recapture methods estimate abundance when the population is demographically and geographically closed during sampling (no births, deaths, immigration, or emigration) [[AssessmentOfBiasAndPrecisionAm_2023]]. Field applications include lake trout surveys, walleye pulse fishing, lobster no-take reserves, pirarucu fisheries assessment, dolphin abundance surveys, marine turtle foraging areas, and creel survey angler counts [[AssessmentOfBiasAndPrecisionAm_2023]]. Studies typically involve spawning aggregations or short time scales where closure assumptions are reasonable [[AssessmentOfBiasAndPrecisionAm_2023]][[StatusAssesmentOfAShoalBassPop_2012]].

## Assumptions and study design

Critical assumptions include random sampling without replacement, complete mixing of marked and unmarked individuals, closed population, capture probability independence, mark retention, appropriate sampling area definition, and temporal closure [[AssessmentOfBiasAndPrecisionAm_2023]]. Population closure assumptions should be evaluated; violations should be minimal [[EvaluationOfALongtermPredatorR_2016]]. 

Sampling design considerations affect estimator performance [[AssessmentOfBiasAndPrecisionAm_2023]]. Boat electrofishing and raft electrofishing are common capture methods for riverine species [[EvaluationOfALongtermPredatorR_2016]][[FlatheadCatfishAbundanceAndGro_1985]]. Boat-mounted pulsed-DC electrofishers enable tagging of >20% of estimated populations in favorable conditions [[FlatheadCatfishAbundanceAndGro_1985]]. PIT-tags and internal anchor tags (such as Floy tags) are used for marking, with double-marking experiments evaluating tag retention [[StatusAssesmentOfAShoalBassPop_2012]][[EvaluationOfALongtermPredatorR_2016]]. Tag loss of 12.2% for Floy tags has been documented, potentially biasing estimates upward by ~10% [[EvaluationOfALongtermPredatorR_2016]][[FlatheadCatfishAbundanceAndGro_1985]].

## Simple estimators

For two-visit studies, use the Chapman estimator rather than Lincoln-Petersen, Chao, or Bayesian estimators [[AssessmentOfBiasAndPrecisionAm_2023]]. The Chapman estimator achieves <2% bias at minimum sample size thresholds [[AssessmentOfBiasAndPrecisionAm_2023]]. 

For multiple-visit studies, always use bias-adjusted versions of the Schnabel or Schumacher-Eschmeyer estimators rather than original formulations [[AssessmentOfBiasAndPrecisionAm_2023]][[EstimatingAnimalAbundance_X-e15b3990]]. Apply ceiling function to adjusted Schnabel estimates for integer population sizes [[AssessmentOfBiasAndPrecisionAm_2023]]. Multi-visit methods reduce variance compared to two-visit methods at equal total sample sizes [[AssessmentOfBiasAndPrecisionAm_2023]]. Field applications report similar results from both estimators (e.g., Schnabel: 7,647 fish, 95% CI 6,154–10,111; Schumacher-Eschmeyer: 8,013 fish, 95% CI 6,575–10,256) [[FlatheadCatfishAbundanceAndGro_1985]].

## Bias and precision

Do not apply any estimator when sample sizes fall below minimum thresholds, as extreme downward bias (>50%) occurs [[AssessmentOfBiasAndPrecisionAm_2023]]. Adjusted Schnabel exhibits -3% to -10% bias depending on number of visits and population size [[AssessmentOfBiasAndPrecisionAm_2023]]. Adjusted Schumacher-Eschmeyer shows lowest root mean square error in the small-sample range where bias is still present [[AssessmentOfBiasAndPrecisionAm_2023]].

Use parametric bootstrap methods for confidence intervals rather than normal approximations [[AssessmentOfBiasAndPrecisionAm_2023]]. Recognize that minimum sample size rules provide lower bounds; larger samples are needed when assumption violations are suspected [[AssessmentOfBiasAndPrecisionAm_2023]]. Precision is no surrogate for accuracy—estimates can be precise but systematically biased [[EstimatingAnimalAbundance_X-e15b3990]]. Mark-recapture estimates can have wide confidence intervals due to low recapture rates (e.g., 95% CI spanning 33,690–200,608 based on 6 recaptures) [[HydroacousticSurveysOfFishAbun_13336]].

## Heterogeneity and behavioral response

Heterogeneous detection probabilities produce negatively biased population estimates [[EstimatingAnimalAbundance_X-e15b3990]]. Detection probability varies with species characteristics, environmental conditions, and observer factors [[EstimatingAnimalAbundance_X-e15b3990]]. Individual heterogeneity in capture probability, incomplete mixing, and population openness all violate assumptions and require larger sample sizes [[AssessmentOfBiasAndPrecisionAm_2023]].

Huggins closed-capture models can estimate abundance with individual covariates such as fish length [[EvaluationOfALongtermPredatorR_2016]]. Capture probability may vary by year, reach, pass, and fish total length with size thresholds (e.g., 600 mm) [[EvaluationOfALongtermPredatorR_2016]]. The regression-based Schumacher-Eschmeyer offers additional robustness to assumption violations at the cost of higher small-sample variability, making it preferable when capture probability heterogeneity is suspected but cannot be modeled explicitly [[AssessmentOfBiasAndPrecisionAm_2023]].

## Model selection and reporting

AICc model selection with small-sample bias adjustment is used to compare models with constant, time-varying, or equal capture and recapture probabilities [[StatusAssesmentOfAShoalBassPop_2012]][[EvaluationOfALongtermPredatorR_2016]]. Top-ranked models are identified by Akaike weight (e.g., 72%) and number of estimable parameters [[EvaluationOfALongtermPredatorR_2016]]. Report abundance estimates with 95% confidence intervals [[FlatheadCatfishAbundanceAndGro_1985]]. Population estimates feed into harvest models, trend analysis, adaptive management frameworks, and other population assessments [[EstimatingAnimalAbundance_X-e15b3990]].

## Workflow in R

1. Use **FSA** [[web:cran-FSA]] for simple Chapman, Schnabel, and Schumacher-Eschmeyer estimators
2. Use **Rcapture** [[web:cran-Rcapture]] for loglinear models of closed populations
3. Use Program MARK or **marked** [[web:cran-marked]] for Huggins closed-capture models with individual covariates [[EvaluationOfALongtermPredatorR_2016]]
4. Apply parametric bootstrap methods for confidence intervals [[AssessmentOfBiasAndPrecisionAm_2023]]
5. Conduct AICc model selection to compare alternative capture probability structures [[StatusAssesmentOfAShoalBassPop_2012]][[EvaluationOfALongtermPredatorR_2016]]
