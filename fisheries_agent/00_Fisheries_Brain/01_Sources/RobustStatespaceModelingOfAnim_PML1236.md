---
species: "Halichoerus grypus; Cystophora cristata"
common_name: "Gray seal; Hooded seal"
family: "Phocidae"
habitat: "Marine (pelagic and coastal migration and foraging routes)"
ocean_basin: "North Atlantic"
location: "Sable Island, Nova Scotia; Gulf of Maine (track origin); south of Greenland (track terminus)"
tags: [marine-biology, phocidae, movement-ecology, state-space-models, satellite-telemetry]
title: "Robust state-space modeling of animal movement data"
source_id: "PML1236"
marsh_id: "PML1236"
library: "Marsh Library"
permission: "not public domain"
source_citation: "I. D. Jonsen, J. Mills Flemming, R. A. Myers (2005). Robust state-space modeling of animal movement data. Ecology 86(11): 2874-2880. Marsh Library ID: PML1236."
source_file: "Jonsen I.D. et al. 2005. Robust state space modeling of animal movement data .pdf"
text_extraction: "text"
---
# Robust State-Space Modeling of Animal Movement Data

#marine-biology #phocidae #movement-ecology

## Executive Summary

This methods paper proposes a robust [[State-Space Model]] framework for analyzing remotely sensed animal movement data, especially [[Argos Satellite Telemetry]] locations. Such data are hard to analyze because their estimation errors are non-Gaussian and change over time, the locations are observed at irregular intervals, and the underlying behaviors are complex. The framework combines a [[Correlated Random Walk]] (CRW) movement model applied to first differences of locations with a [[Switching Model]] for multiple behavioral modes, and uses [[Student-T Distribution]] error models in place of Gaussian ones. The method is demonstrated on three seal tracks: one [[Hooded Seal]] and two [[Gray Seal]] individuals. The authors argue that the approach keeps all locations rather than discarding noisy ones, and that it yields explicit uncertainty estimates for each state.

## Background & Description

**Problem.** Miniaturized satellite transmitters produce large volumes of animal movement data. Any long pathway can contain several behavioral processes, so estimating a single set of movement parameters for the whole track can hide meaningful variability. Devices such as [[Argos Satellite Telemetry]] tags and [[Archival Tags]] also add complex error structures that must be separated from biological signal.

**Prior work.** The authors build on [[Jonsen et al. 2003]], which proposed a state-space framework using a simple random walk fitted to simulated data. The present paper extends that work to real satellite data with more realistic movement models and robust error handling.

**Argos data.** Argos locations fall into six quality classes (A, B, 0, 1, 2, 3). Classes depend on the number of uplinks, the time between uplinks, and the time since the last location estimate. Their errors vary through time and are strongly non-Gaussian. Locations arrive irregularly, which imposes an artificial time structure on the movement process.

**Model components.**
- *Transition equation:* A simple random walk is first set out, then replaced by a first-difference CRW (DCRW). Its rotation matrix uses a mean turning angle, and its process covariance has separate latitude and longitude variances plus a correlation term. A parameter γ controls autocorrelation in both direction and speed. When γ = 0 the model reduces to a simple random walk.
- *Switching model (DCRWS):* Each behavioral mode (for example, migrating or foraging) has its own movement parameters. Transition probabilities between modes are estimated.
- *Measurement equation:* Irregular observations are linked to the regular time grid by straight-line interpolation. This avoids a priori [[Data Regularization]], which can fail when few observations fall within an interval.
- *Error model:* Each latitude and longitude error is modeled as a [[Student-T Distribution]] with a scale parameter and degrees of freedom that depend on quality class. The t distribution approaches the Gaussian as the degrees of freedom increase.

**Parameter estimation.** Error parameters were estimated a priori from [[Vincent et al. 2002]], which tracked Argos tags on captive gray seals. Maximum likelihood estimates and 95% confidence regions were produced for each quality class. A global scale parameter was also estimated within the model to account for differences among tag types.

## Ecological & Environmental Context

- **Behavioral ecology:** Migration and foraging produce distinct movement signatures. Migration shows persistent direction and speed, while foraging shows frequent course reversals and speed changes.
- **Diving animals:** For diving seals, discarding poor-quality classes (B, A, and 0) removes approximately 90% of the data, which is costly to collect. Ad hoc filtering on maximum travel rate also causes data loss.
- **Spatial patterns:** The hooded seal track began off Maine and ended south of Greenland. Its movement was relatively uniform in step length during northward travel (about 50° to 60° N) and more variable during eastward travel and foraging along the Greenland coast (about 60° N). Both gray seal tracks originated and terminated at [[Sable Island]], [[Nova Scotia]], Canada.
- **Directional variability:** Process variance was larger in east-west movement than in north-south movement for all individuals.
- **Applications:** The framework can be linked to [[Movement Ecology]] questions such as home range, foraging behavior, and migration, and can be overlaid on spatial environmental data.

## Key Findings

**Data and sample sizes**
- Error model source: 425 locations from four captive gray seals tracked with Argos tags (Vincent et al. 2002). Four were extreme observations (more than 100 km from the true location): three in quality class 0 and one in class 2.
- Quality class 3 was the only class approximately Gaussian in both directions. All other classes were better described by a t distribution.
- Case studies:
  1. A juvenile male hooded seal (*Cystophora cristata*), with locations almost daily at varying times of day. Three extreme values were present, and at least two behavioral processes (foraging and migration) were evident.
  2. Gray seal 617 (female), with a combination of complex behavior and numerous extreme observations.
  3. Gray seal 2986 (male), with many dubious observations, some clearly extreme.

**Model performance**
- Both the DCRW and DCRWS models produced reasonable state estimates for extreme observations. Extreme points were strongly downweighted rather than removed.
- The DCRWS model fit the hooded seal and gray seal 2986 data better than the DCRW model. For gray seal 617, the 95% credible limits for behavioral parameters overlapped substantially, so the simpler DCRW model was preferred.

**Behavioral results**
- Hooded seal: Migration showed forward movement with small turns. Foraging showed frequent course reversals. The 95% limits for the autocorrelation parameter overlapped, but movement appeared more persistent during migration. Too little foraging data existed to estimate that parameter reliably.
- Gray seal 2986: Movement was highly persistent during migration and more variable during foraging. The probability of remaining in the migrating mode was intermediate, while the probability of remaining in the foraging mode was high.
- Hooded seal switching probabilities: High probability of remaining in either mode.

**Methodological conclusions**
- Modeling the differences between locations (first-difference CRW) is more sensible than modeling the locations directly, because differences capture speed and direction.
- Because estimation error is handled within the state-space model, turning angles and movement rates can be derived directly from state estimates. Decomposing errors beforehand is unnecessary.
- Credible limits provide an explicit quantification of uncertainty for each state estimate.
- The authors recommend that researchers quantify tracking device errors under field conditions and publish those results.

**Future directions (as stated by the authors)**
1. Improve knowledge of [[Argos Error Distributions]].
2. Incorporate biological and environmental constraints directly into the DCRW models.
3. Model the effects of internal states and environmental covariates on movement behavior.

**Supporting material.** Likelihood surface plots, maximum likelihood estimates, and the data regularization comparison are archived in the ESA Electronic Data Archive (Appendices A and B). The [[WinBUGS]] code and sample data are provided as a supplement. Analyses used [[Bayesian Inference]] fitted via [[Markov Chain Monte Carlo]] in WinBUGS and R, with vague priors.