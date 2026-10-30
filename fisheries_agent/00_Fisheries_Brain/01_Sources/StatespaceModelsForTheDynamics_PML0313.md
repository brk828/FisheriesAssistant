---
species: ["Halichoerus grypus", "Cervus nippon", "Cervus elaphus", "Odocoileus virginianus clavium", "Canis lupus", "Puffinus tenuirostris", "Vireo atricapilla", "Maculinea arion", "Acacia nilotica"]
common_name: ["Grey seal", "Sika deer", "Red deer", "Florida Key deer", "Grey wolf", "Short-tailed shearwater", "Black-capped vireo", "Large blue butterfly", "Prickly acacia"]
family: ["Phocidae", "Cervidae", "Canidae", "Procellariidae", "Vireonidae", "Lycaenidae", "Fabaceae"]
habitat: "N/A (general wildlife populations; examples include coastal colonies, woodland and open ranges)"
ocean_basin: "North Atlantic (North Sea and UK waters, as motivating examples)"
location: "Scotland, UK; North Sea; United States; Australia"
tags: [state-space-model, population-dynamics, leslie-matrix, bayesian-inference, sequential-monte-carlo, wildlife-management]
title: "State-space models for the dynamics of wild animal populations"
source_id: "PML0313"
marsh_id: "PML0313"
library: "Marsh Library"
permission: "not public domain"
source_citation: "S. T. Buckland, K. B. Newman, L. Thomas, N. B. Koesters (2004). State-space models for the dynamics of wild animal populations. Ecological Modelling 171 (2004) 157-175. Marsh Library ID: PML0313."
source_file: "Buckland S.T. et al. 2003. State space models for the dynamics of wild animal populations .pdf"
text_extraction: "text"
---
# State-Space Models for the Dynamics of Wild Animal Populations

#marine-biology #population-dynamics #phocidae #cervidae

## Executive Summary

This methods paper (Buckland et al., 2004, *[[Ecological Modelling]]* 171) proposes a unified [[State-Space Model]] framework for jointly specifying population dynamics and the survey or harvest observations taken on a population. The population process is written as a **state process** and the measurements as an **observation process**, so demographic stochasticity and observation error enter the same likelihood. Each demographic sub-process (survival, movement, birth, harvest) is a separate matrix or pdf, and their product is a generalised [[Leslie Matrix]]. Parameters are estimated in a Bayesian setting using [[Sequential Monte Carlo]] filtering. The paper is not a fish study. Its motivating cases include [[Grey Seal]] metapopulations, [[Sika Deer]] range expansion, and [[North Sea Demersal Fish]] stock assessment, with worked examples on simulated populations.

## Background & Description

**Motivation.** Wildlife assessment had no general underlying framework. [[Borchers et al. (2002)]] unified closed-population methods, and Chapter 13 of that work suggested a state-space approach for open populations. This paper develops that suggestion. The authors' projects needed a modular approach, because model components were shared across projects.

**Motivating datasets:**
- UK grey seal metapopulation: counts of pups at breeding colonies, used to forecast abundance.
- Introduced sika deer in Scotland: line transect data on dung pellet groups, used to predict range increase and competition and hybridisation with native red deer.
- North Sea demersal fish stocks: landing and discarding rates from sampled fishing vessels.

**Inferential framework.** The approach is Bayesian. Priors are set for parameters and the initial population state. These may be informative (past studies, expert knowledge) or vague. Posterior samples of parameters and population states are then drawn by computer-intensive methods. Model uncertainty is handled by specifying several candidate models with a prior model distribution. With *m* models and no preference, each receives prior probability 1/*m*.

**Modular design.** The state process is split into sub-processes such as survival, movement and birth. Each can be defined, tested and combined separately, which makes model building more straightforward than writing one complex model in a single step. The paper contrasts this with [[Caswell (2001)]] matrix models, from which it departs in two respects: observations are integrated into the state-space model, and processes are separated for modular definition.

## Ecological & Environmental Context

**Matrix formulation.** A three-age-class [[Leslie Matrix]] model is decomposed into aging, birth and survival matrices. Births are placed in the matrix product so that only newborns surviving their first year count as recruits. This shows how deterministic projection matrices become the mean of a stochastic state process.

**Density, competition and predation.** Structure accommodates density dependence, competition, predator-prey interactions and metapopulations. Process parameters can themselves be functions of covariates such as weather, habitat suitability, or distance between colonies.

**Population examples in the literature.** The authors list recent models that could use this approach, including:
- [[Florida Key Deer]] (Peterson et al., 2003)
- [[Grey Wolf]] (Miller et al., 2002)
- [[Short-Tailed Shearwater]] (Yearsley et al., 2003)
- [[Black-Capped Vireo]] (Parysow and Tazik, 2002)
- [[Large Blue Butterfly]] (Griebeler and Seitz, 2002)
- [[Prickly Acacia]] (Kriticos et al., 2003)

**Worked examples.** Six illustrative populations are presented. Each is simpler than a real case:
1. Two age classes, census with normal errors (small isolated bird population).
2. Five age/stage/sex classes with a removal experiment (large mammal).
3. Two age classes, mark-recapture survey (female population).
4. Density-dependent, harvested population with weather and age effects, line transect survey.
5. Metapopulation of three colonies with Dirichlet-distributed movement of young females.
6. Predator-prey system with strip transect survey.

## Key Findings

- **Framework.** A state-space model comprises three pdfs: initial state, state process and observation process. Inference reduces to integration over states and parameters. The likelihood is an integral of the joint distribution, which is high-dimensional and generally not analytically tractable.
- **Matrix representation.** When sub-process expectations are linear, the conditional expectation of states is a product of matrices (generalised Leslie or Lefkovitch form). Non-linear sub-processes give only approximate matrix forms.
- **Observation models.** Observations can equal state components exactly, be sums of components, or carry error (normal, lognormal, Poisson-based). Exact observations restrict the integral to a subspace of states.
- **Example 2 (removal).** The state has 10 components covering sex, age/stage, removal status and year. Six sub-processes are used. Parameters such as birth rates are confounded with juvenile survival unless extra data or informative priors are supplied.
- **Example 3 (mark-recapture).** The state vector includes capture histories, so its length can reach 2 × 2^t. Juveniles and adults are distinguished for one year after first capture, because winter and spring survival differ.
- **Example 4 (line transect, harvest).** Survival depends on accumulated day-degrees of frost, and birth probability depends on total population size. Only the non-linear survival and birth terms require approximation.
- **Example 5 (metapopulation).** Dirichlet-distributed movement between three colonies is included, and observed counts are lognormal.
- **Example 6 (predator-prey).** Prey and predator births are Poisson, and survival is Bernoulli, with logistic link functions.
- **Estimation.** The paper recommends a recursive filtering algorithm, specifically a [[Bootstrap Filter]] variant. Prediction and update steps estimate the likelihood, and a single particle sample can be reused across parameter values through importance weights ([[Geyer (1996)]]). The [[Kalman Filter]] gives an exact solution only for normal dynamic linear models, and is used as an approximation otherwise ([[Harvey (1989)]]).
- **Posterior sampling.** [[Liu and West (2001)]] combine parameter and state sampling with kernel smoothing to address particle depletion.
- **Extensions.** Discrete space and time limit fidelity for breeding spread across the year. Individual-based models become feasible with simulation fitting. Hierarchical state-space models, with a third process for time-varying parameters, are proposed ([[Newman (2000)]]).
- **Harvest treatment.** Harvest is deterministic in the exploited-population example. If harvest is estimated, its observation should carry stochastic error.
- **Planned work.** The authors note that comparisons of sequential particle filtering with [[Markov Chain Monte Carlo]], and diagnostics based on filtered parameter trajectories and [[Akaike Information Criterion]] or BIC measures, remain to be completed (Newman et al., in preparation). Work on the [[British Grey Seal]] metapopulation (Thomas et al., in press) applies auxiliary particle filtering with kernel smoothing.