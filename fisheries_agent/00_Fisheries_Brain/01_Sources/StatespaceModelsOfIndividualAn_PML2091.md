---
species:
  - Cervus elaphus
  - Dermochelys coriacea
  - Halichoerus grypus
  - Gadus morhua
  - Thunnus thynnus
  - Thunnus obesus
  - Parnassius mnemosyne
  - Canis lupus
  - Rangifer tarandus
common_name:
  - Elk
  - Leatherback Turtle
  - Grey Seal
  - Atlantic Cod
  - Atlantic Bluefin Tuna
  - Bigeye Tuna
  - Apollo Butterfly
  - Wolf
  - Caribou
family: N/A
habitat: Marine and terrestrial (for example open woodland, agricultural land, fragmented landscapes, pelagic ocean, marine reserves)
ocean_basin: Atlantic and Pacific (text references the North Atlantic, the Baltic Sea and waters near Hawaii)
location: North Atlantic Ocean; Baltic Sea; waters near Hawaii; Scotland (St Andrews research institutions)
tags: [movement-ecology, state-space-models, animal-movement, marine-biology, review]
title: "State-space models of individual animal movement"
source_id: "PML2091"
marsh_id: "PML2091"
library: "Marsh Library"
permission: "not public domain"
source_citation: "T. A. Patterson, L. Thomas, C. Wilcox, O. Ovaskainen, J. Matthiopoulos (2007). State-space models of individual animal movement. Trends in Ecology & Evolution (Elsevier), doi:10.1016/j.tree.2007.10.009. Marsh Library ID: PML2091."
source_file: "Patterson T.A. et al. 2007. State space models of individual animal movement.pdf"
text_extraction: "text"
---
# State-Space Models of Individual Animal Movement

#movement-ecology #marine-biology #multi-taxa

## Executive Summary

This review, by Patterson and co-authors and published in *Trends in Ecology and Evolution* (2008, vol. 23, no. 2), argues that [[State-Space Model]]s (SSMs) are the most promising analytical framework for individual animal movement. Movement data are stochastic and often subject to severe observation error, and conventional workflows treat error correction, metric calculation and statistical inference as separate steps. An SSM couples a **process model** of movement dynamics with an **observation model** of the sampling process, so uncertainty in the data is propagated into biological inference. The authors present SSMs as a basis for a unified "movement ecology" linking behaviour, biogeography and population dynamics. The paper is a general review rather than a fish study; fish (Atlantic cod, tuna) appear only as illustrative examples.

## Background & Description

**Why movement matters.** Population ecology has moved from temporal abundance fluctuations toward spatially explicit approaches. Some phenomena, including the spread of diseases and invasive species, [[Metapopulation Dynamics]], [[Home Range]] characterisation and [[Marine Reserve]] design, depend on individual movement behaviour rather than average density alone. Interactions among life history, physiology, behaviour and habitat make movement highly complex.

**Nature of movement data.** Movement data are time-indexed positions of individuals. Movement metrics (speed, heading, turning angle, step length, rate of movement between regions) are derived from these positions and are partly shaped by behaviour. Sources include:
- [[Mark-Release-Recapture]] (MRR), which suffers from sampling bias, such as commercial fishery tag returns reflecting fisher behaviour.
- [[Satellite Telemetry]] and [[GPS Tracking]], which suffer from positional imprecision, satellite coverage and interference.
- [[Light-Based Geolocation]], which is affected by weather and cloud cover and depends on day length and noon/midnight estimates.
- [[Radio Telemetry]], which requires error-prone triangulation.
- [[Harmonic Radar]] and [[Electronic Data Storage Tags]].

**Critique of conventional analysis.** The review describes a three-stage pipeline (error correction, metric calculation, statistical analysis). Its shortcomings include:
- Subsampling (discarding data) to reduce autocorrelation.
- Ad hoc error treatments, which embed implicit assumptions about animal movement.
- Compartmentalisation that does not separate observation error from the statistical properties of movement.

Bradshaw et al. are cited as showing that location error can lead to incorrect conclusions about movement behaviour.

**SSM structure.** An SSM is a time-series model of hidden **states** (for example location, behavioural mode, energetic condition) with:
- A process model, x_t = f(x_{t-1}, η_t), predicting the state probabilistically, usually under the [[Markov Condition]].
- An observation model, y_t = h(x_t, ε_t), linking data to states.

A worked example is a [[Correlated Random Walk]] (CRW), with turning angles drawn from a von Mises distribution and step lengths from a lognormal distribution. Extensions include switching between behavioural modes (for example "resident" and "transit") via a transition matrix, and [[Edge-Mediated Behaviour]], in which animals turn back at patch boundaries.

## Ecological & Environmental Context

**Study organisms and systems cited.**
- [[Elk]]: [[Morales et al.]] fitted SSMs and identified "encamped" (slow, variable) and "exploratory" (fast, directed) modes. Encamped movement was associated with open woodland and agricultural habitat. Other work found distance to food, streams and roads, and time of day, affected cyclical elk movements.
- [[Leatherback Turtle]]: [[Jonsen et al.]] used state-space analysis of migration paths and found distinct diurnal differences in movement rates, hypothesised to reflect daytime navigation or night-time foraging on gelatinous plankton. The authors note implications for fishery interactions with this critically endangered species.
- [[Grey Seal]]: SSMs highlighted sex-specific foraging areas.
- [[Atlantic Cod]]: SSMs using temperature, pressure and salinity from electronic tags, combined with ocean-model output, estimated locations and time spent in marine reserves.
- Tuna: [[Bluefin Tuna]] and [[Bigeye Tuna]] movements were estimated with SSMs, including Kalman filter analysis of archival tags near Hawaii.
- [[Apollo Butterfly]] (*Parnassius mnemosyne*): a diffusion model with habitat-specific movement parameters, estimated from capture-recapture data.
- Other taxa: pigeon behavioural switches, wolf movements, and caribou movements modelled with hidden Markov models.

**Environmental covariates.** Process models can take habitat, oceanographic and other environmental data as inputs, so predicted states respond to habitat in a biologically realistic way. Marine applications require highly dynamic oceanographic covariates to be known near the animal's true position, which satellite data often fail to provide because they are spatiotemporally averaged or interpolated.

**Estimation methods.** Maximum likelihood is tractable only in special cases, such as the [[Kalman Filter]] for linear Gaussian SSMs and [[Hidden Markov Model]]s with discrete states. For nonlinear, non-Gaussian models the review points to [[Markov Chain Monte Carlo]] (MCMC) and [[Particle Filtering]] (also called sequential importance sampling). Computation is intensive: one diffusion fit to MRR data required solving a large matrix equation about a million times.

**Model selection.** Candidate models can be compared with [[Akaike Information Criterion]] (AIC) or Bayesian methods, and combined through [[Multi-Model Inference]] and model averaging. These approaches allow direct assessment of the relative support for competing hypotheses.

## Key Findings

1. **SSMs integrate the analysis phases.** By modelling observation error explicitly, SSMs produce inferences that account for input uncertainty rather than hiding it in pre-processing. They estimate state probabilities, process parameters (for example mean speed, turning rate) and observation parameters (for example error variance).
2. **Prior information can be used.** Prior knowledge of observation error from independent studies can be incorporated, which avoids discarding imprecise but costly data.
3. **Behavioural modes are inferred, not assumed.** SSMs estimate the probability of being in each behavioural mode (such as foraging or transit) rather than assigning a single category. Process models can make mode switching depend on covariates such as habitat type.
4. **Mechanistic models enable forecasting.** Because SSMs are based on mechanistic movement models, they can interpolate missing observations, forecast movements in novel environments and predict landscape connectivity. The authors argue they outperform linear classification models for extrapolation.
5. **Simulation links individuals to populations.** Simulating from estimated SSMs can generate expected population spatial distributions, potentially overcoming the failure of individual-based models to replicate real distributions.
6. **SSMs are judged the most suitable tool.** The authors conclude SSMs are the only commonly used candidate that can satisfy all the requirements of an integrated movement analysis, while acknowledging that ecologists will need to work closely with statisticians.

**Future research directions (Box 3):**
- Build more realistic process models incorporating memory, intention and conspecific influence.
- Add physiological state (for example energetics) and environmental information to improve behavioural inference.
- Connect SSMs to optimal-foraging and dynamic state variable theory.
- Use hierarchical or mixed-effects SSMs to quantify individual variation and link it to population redistribution.
- Develop methods for matching uncertain animal positions to environmental covariates, and use onboard tag sensors so covariates are collected at the animal's location.
- Model known sources of observation error, such as serial correlation in satellite errors, tag sensor deterioration and between-tag variation.

**Reference base.** The review draws on 77 numbered references spanning movement ecology, telemetry, SSM methodology and applications.