---
name: count-glm
description: Count responses (catch, abundance) with Poisson, negative binomial, zero-inflated and hurdle models, mixed effects, diagnostics and R workflow.
status: draft
generated: 2026-10-20
---

# count-glm

## When to use

Use count GLMs when the response variable is discrete abundance or catch data (integers ≥0) from fisheries surveys or sampling programs. These models are appropriate for relative abundance estimates [[IncreasingDroughtFavorsNonnati_2019]], catch per unit effort data [[CatchPerUnitEffortModellingFor_2024]], or count data from electrofishing and other field surveys [[FisheriesSurveyOfTheApacheSitg_1995_07_18]]. Select the distribution and model structure based on the proportion of zeros, variance-to-mean ratio, and sampling design.

## Count distributions and overdispersion

Start with Poisson regression for equidispersed count data. When variance exceeds the mean (overdispersion), use negative binomial models with a dispersion parameter [[IncreasingDroughtFavorsNonnati_2019]]. Initial biomass and survey variance can be characterized using negative binomial distribution parameters for mean and dispersion [[IncreasingDroughtFavorsNonnati_2019]]. The negative binomial distribution is appropriate for relative abundance analysis with catch count data [[InvasionPotentialOfNonnativeFi_2026]].

## Zero-inflation and hurdle models

Document the proportion of zero catches in your dataset [[CatchPerUnitEffortModellingFor_2024]]. Delta or hurdle models are typically required when zeros exceed 5–10% of observations [[CatchPerUnitEffortModellingFor_2024]]. The Tweedie distribution (1 < p < 2) can handle zeros without requiring a separate hurdle component [[CatchPerUnitEffortModellingFor_2024]]. Zero-inflation may not be an issue in all datasets; negative binomial models alone may suffice [[IncreasingDroughtFavorsNonnati_2019]].

## Random effects and repeated sampling

Incorporate random effects for grouping structures in the data. Use fish ID as a random effect when analyzing repeated measurements on individuals [[ChasingNorthernPikeUnderIceLon_2021]]. For depth or spatial sampling, treat replicate units (depth bands, sites) as random effects [[InvasionPotentialOfNonnativeFi_2026]]. Random effects for individual, sampling unit, or month account for non-independence [[InvasionPotentialOfNonnativeFi_2026]]. Report both marginal R² (fixed effects only) and conditional R² (fixed plus random effects) for mixed models [[InvasionPotentialOfNonnativeFi_2026]]. Vessel, trip, or year-area interactions can be treated as nuisance random effects [[CatchPerUnitEffortModellingFor_2024]].

## Offsets and effort

Include effort as an offset term to model catch per unit effort rather than raw counts [[CatchPerUnitEffortModellingFor_2024]]. Appropriate effort units include hooks, sets, hours, days, or electrofishing seconds [[CatchPerUnitEffortModellingFor_2024]][[FisheriesSurveyOfTheApacheSitg_1995_07_18]]. Set-by-set or haul-by-haul operational-level data are preferred over aggregated data, as aggregation can mask targeting changes, introduce bias in mean-variance relationships, and reduce ability to model autocorrelation [[CatchPerUnitEffortModellingFor_2024]].

## Diagnostics and model comparison

Check convergence using gradient checks and confirm the Hessian matrix is positive-definite [[CatchPerUnitEffortModellingFor_2024]]. For non-Gaussian models, use probability-integral-transform (PIT) residuals via the DHARMa package [[CatchPerUnitEffortModellingFor_2024]][[web:cran-DHARMa]]. Examine QQ plots and test for spatial autocorrelation using Moran's I [[CatchPerUnitEffortModellingFor_2024]]. Compare models using AIC [[InvasionPotentialOfNonnativeFi_2026]][[ChasingNorthernPikeUnderIceLon_2021]], BIC, or WAIC [[CatchPerUnitEffortModellingFor_2024]]. Report deviance explained (R²) and conditional R² for mixed models [[CatchPerUnitEffortModellingFor_2024]]. Conduct sensitivity analyses when appropriate [[BayesianEstimationOfVonBertala_2025]]. Gelman-Rubin statistics (<1.1) and effective sample sizes confirm convergence in Bayesian frameworks [[BayesianEstimationOfVonBertala_2025]].

## Workflow in R

1. Fit negative binomial GLMs using `glm.nb()` from MASS [[web:cran-MASS]] or `glmmTMB()` [[web:cran-glmmTMB]] for zero-inflated and hurdle variants
2. Fit generalized linear mixed models (GLMMs) with `glmmTMB()` [[web:cran-glmmTMB]] for random effects and complex distributions
3. Include effort offset terms in the model formula for CPUE standardization [[CatchPerUnitEffortModellingFor_2024]]
4. Check residuals using DHARMa package for PIT residuals and diagnostics [[web:cran-DHARMa]][[CatchPerUnitEffortModellingFor_2024]]
5. Compare models using AIC and evaluate conditional R² for mixed models [[InvasionPotentialOfNonnativeFi_2026]][[CatchPerUnitEffortModellingFor_2024]]

## Supplement
See `SUPPLEMENT.md` in this folder for a worked workflow drawn from developer-supplied sources (draft).
