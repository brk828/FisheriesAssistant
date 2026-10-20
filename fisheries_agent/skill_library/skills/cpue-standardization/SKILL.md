---
name: cpue-standardization
description: Defining and standardizing catch per unit effort across gear, effort and season, with models, trend estimation and R workflow.
status: draft
generated: 2026-10-20
---

# cpue-standardization

## When to use

Use CPUE standardization when comparing catch rates across different gear types, seasons, locations, or time periods to isolate population trends from variation in sampling methods and environmental conditions [[CatchPerUnitEffortModellingFor_2024]]. Standardization is critical when monitoring programs involve changes in gear configuration [[InteragencyStandardizedMonitor_1993]] or when high year-to-year variance from small catch sizes and environmental effects on gear efficiency limits detection to long-term trends [[ThoughtsOnTheStatusAndRecovery_1990_05_08]].

## CPUE definition and effort measures

CPUE is defined as catch per unit of standardized effort, with effort measures varying by gear type [[RazorbackSuckerMonitoringEffor_13702]]. For gill and trammel nets, effort is measured in net units (30-100 m multi- and monofilament units with mesh sizes from 1.2 to 7.5 cm bar measure) fished near bottom, with CPUE expressed as fish per 100 m² per night [[RazorbackSuckerMonitoringEffor_13702]]. For electrofishing, effort is measured in hours using boat-mounted, variable voltage, D.C. pulsating units (mostly nighttime), with CPUE expressed as fish per hour [[RazorbackSuckerMonitoringEffor_13702]]. Standardized monitoring datasets document catch per unit effort alongside species composition by age class (YOY, juvenile, adult), habitat conditions, water quality, and weather [[StatusOfTheBiowestDatabase_13632]]. CPUE data can serve as an index to detect population trends when calculated using standardized protocols at consistent locations [[PreliminaryStudyOfTheDesertPup_12499]].

## Gear and size selectivity

Electrofishing gear exhibits size- and species-selectivity compared to other gear types such as gill nets and seines, affecting community composition estimates [[SelectedReferencesOnElectrofis_1980_05_06]]. Unequal catchability and size-selectivity bias population estimates derived from removal methods using electrofishing [[SelectedReferencesOnElectrofis_1980_05_06]]. Each CPUE index in an assessment is associated with a fleet that samples a specific component of the stock, with the assessment model estimating catchability and selectivity for each fleet [[CatchPerUnitEffortModellingFor_2024]]. Fisheries should be defined to minimize selectivity changes through time by accounting for spatial-seasonal-gear variation [[CatchPerUnitEffortModellingFor_2024]].

## Standardization models

CPUE standardization accounts for changes in catchability (q), selectivity (s), and availability (a) to isolate changes in true abundance (M): CPUE = (saqM)/A [[CatchPerUnitEffortModellingFor_2024]]. Most standardizations use generalized linear models (GLM) or extensions [[CatchPerUnitEffortModellingFor_2024]]. GLM takes the form log(CPUE) = β₀ + Σβᵢxᵢ + ε, with categorical (year, area, vessel) and continuous covariates [[CatchPerUnitEffortModellingFor_2024]]. GAM includes smooth functions f(x) for continuous predictors: log(CPUE) = β₀ + Σf(xᵢ) + ε [[CatchPerUnitEffortModellingFor_2024]]. GLMM adds random effects for vessel, trip, or year-area interactions [[CatchPerUnitEffortModellingFor_2024]]. Delta or hurdle models use a two-stage approach modeling encounter probability (binomial) and positive catch rates (lognormal, Gamma) [[CatchPerUnitEffortModellingFor_2024]].

## Trend estimation and uncertainty

Standardized monitoring programs track relative abundance via standardized CPUE, such as spring electrofishing CPUE for adults and seining CPUE for young-of-year [[ThoughtsOnTheStatusAndRecovery_1990_05_08]]. High year-to-year CPUE variance from small catch sizes and environmental effects on gear efficiency can limit detection to long-term trends or only dramatic population changes [[ThoughtsOnTheStatusAndRecovery_1990_05_08]]. Simple techniques using standardized locations and effort can detect population trends over years when monitored annually [[PreliminaryStudyOfTheDesertPup_12499]]. Stochastic resampling methods can be used to determine statistical significance of ecological indices derived from catch data [[UtahLakeEcosystemMonitoringToS_2023]].

## Workflow in R

1. Load the project's own catch and effort files (format and columns are recorded in `data_summary.md` / the project's data manifest during onboarding; use base R or readr/readxl, not a package) with covariates (year, area, gear, environmental variables)
2. Fit GLM with log link for lognormal CPUE or GAM with smooth terms using **mgcv** [[web:cran-mgcv]] [[CatchPerUnitEffortModellingFor_2024]]
3. For zero-inflated data, fit delta models with binomial encounter probability and positive catch components using **glmmTMB** [[web:cran-glmmTMB]] [[CatchPerUnitEffortModellingFor_2024]]
4. Add random effects for vessel, trip, or spatial effects in GLMM framework using **glmmTMB** [[web:cran-glmmTMB]] [[CatchPerUnitEffortModellingFor_2024]]
5. Extract standardized year effects and confidence intervals using **emmeans** [[web:cran-emmeans]]
6. Plot standardized CPUE trends with uncertainty bounds (unsourced)
