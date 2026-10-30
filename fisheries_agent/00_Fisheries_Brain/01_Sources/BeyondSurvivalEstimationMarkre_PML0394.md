---
species: Eubalaena glacialis
common_name: North Atlantic right whale
family: Balaenidae
habitat: Marine (coastal and continental shelf waters)
ocean_basin: North Atlantic
location: Western North Atlantic; summer feeding grounds in the Gulf of Maine and Bay of Fundy; winter calving grounds off the southeastern U.S.
tags: [marine-biology, cetacea, balaenidae, demography, mark-recapture, matrix-population-models]
title: "Beyond survival estimation: mark-recapture, matrix population models, and population dynamics"
source_id: "PML0394"
marsh_id: "PML0394"
library: "Marsh Library"
permission: "not public domain"
source_citation: "H. Caswell, M. Fujiwara (2004). Beyond survival estimation: mark-recapture, matrix population models, and population dynamics. Animal Biodiversity and Conservation, 27.1: 471-488. Marsh Library ID: PML0394."
source_file: "Caswell H. et al. 2004. Beyond survival estimation mark recapture matrix population models and population dynamics.pdf"
text_extraction: "text"
---
# Beyond Survival Estimation: Mark-Recapture, Matrix Population Models, and Population Dynamics

#marine-biology #cetacea #balaenidae

## Executive Summary

Caswell & Fujiwara (2004) argue that [[Survival Probability]] matters mainly as one component of population dynamics, and that its population consequences only become visible inside a demographic model. They propose that [[Matrix Population Models]] provide a natural bridge between [[Multi-State Mark-Recapture]] data and population dynamics. Because a matrix model describes all life-cycle transitions (not just death), it lets maximum likelihood estimation extend to [[Population Growth Rate]], sensitivity and elasticity, [[Net Reproductive Rate]], [[Generation Time]], and transient dynamics. The approach is illustrated with an ongoing demographic analysis of the endangered [[North Atlantic Right Whale]], whose population growth rate has fallen below 1 in recent years.

## Background & Description

- **Survival is not the endpoint.** Mark-recapture (MR) statistics have long focused on [[Survival Probability]], but the authors note that survival matters as a component of growth. In the simple model N(t+1) = [P(survival) + E(reproduction)] N(t), the rate of increase is the sum of survival and birth rate.
- **Structured models.** Age-, stage-, size-, and location-structured models date back more than a century (e.g., [[Lotka Model]], [[Leslie Matrix]]). Their main value is explanatory: they show how the life cycle drives population dynamics, not merely more accurate prediction.
- **Matrix framework.** A matrix population model requires a projection interval and life-cycle stages chosen by a homogeneity criterion. The projection matrix A is split into T (transitions among living individuals, including death) and F (reproduction). Individual tagging makes MR data inherently individual-level, which is why it fits these models well.
- **Framework variants.** The same logic applies to partial differential, delay-differential and integrodifference equations, but the paper focuses on matrix models because they match typical MR data structure.

### Right whale study system

- The species was hunted to near extinction by commercial whalers; the remaining population was described as "only about 300 individuals."
- Individuals are identified photographically from scars and callosity patterns.
- The [[New England Aquarium]] has surveyed the population since 1980, with a database of over 10,000 sightings. First identification was treated as marking and each resighting as recapture.
- Threats include ship collisions, [[Fishing Gear Entanglement]], and coastal pollution.

## Ecological & Environmental Context

- **Life-cycle structure.** The right whale model distinguishes males and females. Females are divided into calves, immatures, mature females, mothers (reproducing females), and post-mothers (females in an interbirth interval). The post-mother stage enforces a two-year minimum interbirth interval, which the data support.
- **Environmental driver.** Survival and breeding were modelled against the [[North Atlantic Oscillation]] (NAO), a major climatic and oceanographic oscillation defined by barometric pressure difference between Iceland and the Azores. The NAO affects many ecological systems, including plankton in the western North Atlantic where right whales feed.
- **Density and environment.** The authors note that density-dependent and environment-dependent models have received less attention, partly because vital rates as functions of environmental variables were hard to estimate in the field before MR methods.

## Key Findings

### Methodological findings

1. **Likelihood of capture histories.** Using the transition matrix with death as an absorbing stage (the matrix O) gives a simple matrix formula for the probability of any capture history, extending the Cormack-Jolly-Seber likelihood. Log-likelihoods can be maximized, and nested models compared with log-likelihood tests and [[Akaike Information Criterion]] (AIC) values.
2. **Derived quantities.** Because matrix models yield maximum likelihood estimates of any invertible function of parameters, they provide estimates of population growth rate, stable stage distribution, reproductive value, damping ratio, period of oscillation, and sensitivity and elasticity. Standard errors can be obtained by Taylor series (delta method) or parametric bootstrap.
3. **Absorbing Markov chain.** The matrix O can yield life expectancy, age-specific survivorship, [[Net Reproductive Rate]], [[Generation Time]], and the distribution of ages at death, even when age is not in the model.
4. **Fertility estimation.** Including a breeding state in the life cycle allows F to be estimated from the same MR data. The right whale produces a single calf per reproductive event, which makes F relatively easy to construct.
5. **Density dependence.** In a two-stage model with density-dependent fertility, increasing fertility produced a sequence of bifurcations (stable equilibrium, 2-cycle, 4-cycle, period 8 and 16, then chaos). The authors stress that the full bifurcation sequence, not a single equilibrium, characterizes such a model.

### Right whale results

- **Model selection.** Transition parameters were allowed to vary across three quantities (calf survival, mother survival, and birth probability conditional on survival), each constant, a logistic function of time, a function of NAO, or both. This produced 64 candidate models. The time-invariant model ranked last by AIC, so the data clearly did not support constant vital rates.
- **Best model.** It included a temporal trend in mother survival and birth probability, plus NAO effects on calf survival, mother survival, and birth probability. Models with only a temporal trend or only NAO dependence were not supported.
- **Time-invariant benchmark.** For 1980–1997 data, the time-invariant projection matrix gave:
  - Population growth rate λ = 1.025, about 2.5% growth per year.
  - Net reproductive rate R₀ = 2.18.
  - Female calf life expectancy of 32 years; male calf life expectancy of 18.4 years, a pattern the authors note is not unusual in cetaceans.
  - Median interbirth interval of 4.0 years.
- **Elasticity.** In the time-invariant model, λ was most elastic to survival and growth transitions of mature females, mothers, and interbirth females. Changes in fertility would have little effect.
- **Temporal decline.** Calf survival declined slightly, while mother survival and breeding probability declined dramatically, with similar rates in the trend and best models. Mean interbirth interval rose from about 4 to about 7 years. Female life expectancy and net reproductive rate both declined.
- **Population trajectory.** Conditions "have deteriorated since 1980." If conditions typical of the late 1990s were maintained, the population would be doomed to extinction because λ < 1. The decline in λ was attributed mainly to reduced mother survival.
- **Management targets.** Across all models, elasticity to mature female survival was consistently highest, followed by immature survival and mother or post-mother survival. Elasticity to calf survival was consistently lowest. The authors conclude that all models point to the same target for management: improved survival.

### Open problems identified

- Environment-dependent models lack a general theory, especially when dependence cannot be reduced to time-invariance or a stationary stochastic process.
- The observed population growth rate from [[Pradel Growth Rate Estimation]] differs from the demographic λ; few documented cases explain why populations fail to grow at potential rate.
- Estimating fertility (F) needs more attention, possibly via reverse-time MR analysis or integrated modelling of MR and census data.
- Estimating density dependence and stochastic models by MR remains in its infancy; Bayesian hierarchical methods are proposed.
- Combining count data with MR data can make ill-conditioned inverse problems solvable.