---
species: Panthera tigris
common_name: Tiger
family: Felidae
habitat: Forest reserve with suitable and non-habitat areas (Nagarahole Reserve)
ocean_basin: N/A
location: Nagarahole Reserve, Karnataka, southwestern India
tags: [ichthyology-adjacent: N/A, camera-trapping, spatial-capture-recapture, density-estimation, bayesian-inference, large-felids, carnivore-survey]
title: "Bayesian inference in camera trapping studies for a class of spatial capture-recapture models"
source_id: "PML0181"
marsh_id: "PML0181"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. A. Royle, K. U. Karanth, A. M. Gopalaswamy, N. S. Kumar (2009). Bayesian inference in camera trapping studies for a class of spatial capture-recapture models. Ecology, 90(11), pp. 3233-3244. Marsh Library ID: PML0181."
source_file: "Bayesian inference in camera trapping studies for a class of spatial capture recapture models.pdf"
text_extraction: "text"
---
# Bayesian Inference in Camera Trapping Studies for a Class of Spatial Capture-Recapture Models

#ichthyology #marine-biology #Felidae

*Note: This source is a terrestrial wildlife-statistics paper, not a fish or aquatic study. The taxon tag above is kept only to satisfy the template. The subject is [[Tiger]] (Panthera tigris) density estimation.*

## Executive Summary

Royle, Karanth, Gopalaswamy and Kumar develop a class of [[Spatial Capture-Recapture]] models for estimating abundance and density from [[Camera Trapping]] and related methods. The models are hierarchical, with a [[Point Process Model]] describing where individuals' [[Activity Centers]] lie and an observation model describing capture probability as a function of distance between each animal's activity center and each trap. The authors show these models can be written as [[Generalized Linear Mixed Models]] and fit them in a [[Bayesian Inference]] framework using [[Data Augmentation]], implemented in [[WinBUGS]]. They apply the models to a 2006 tiger survey in [[Nagarahole Reserve]], India, and estimate a density of 13.4 tigers per 100 km² with a 95% posterior interval of (9.3, 19.6).

## Background & Description

Conventional density estimation from trapping arrays applies [[Closed Population Models]] to individually identifiable animals, then converts abundance to density with ad hoc buffers. The standard approach (Karanth and Nichols 1998) adds a buffer strip equal to half the mean maximum distance moved by animals captured in more than one trap. The authors argue these heuristics are poorly understood and cannot be formally extended. Movement of animals on and off the sampled area also violates the assumption of [[Geographic Closure]].

The study focuses on felids with individually unique spot or stripe patterns, such as [[Tiger]], [[Leopard]], [[Jaguar]] and [[Ocelot]]. Surveys usually run 30 to 60 days to ensure demographic closure. Both flanks of each animal are photographed to assign identity. Traps are often placed at ecologically optimal sites, producing irregular arrays.

The tiger data come from a long-term programme in Nagarahole Reserve, Karnataka, running since 1991 under Karanth and colleagues. The 2006 dataset was collected at 120 trap stations, each referenced by latitude, longitude and UTM coordinates. Two camera traps were placed at each location, and sampling ran over 48 nightly occasions between 24 January and 16 March 2006.

## Ecological & Environmental Context

The Nagarahole study area includes a park boundary, forest cover and non-habitat areas inside a 15 km buffer around the trap array. Non-habitat was excluded from the analysis. The authors note the highest-density area lies in the western part of the array, which they describe as having high prey densities (S. Kumar, unpublished data).

Sampling was spatially rotated. The reserve was split into four blocks of about 30 trap stations each. Each block was run for 12 consecutive days, after which cameras moved to the next block. Only about 30 of the 120 locations held an active trap on any given night. The authors treat the resulting non-operational traps as structural zeros, not sampling zeros.

Movement is central to the model. Captures by camera traps can be spatially clustered because animals use their territory non-randomly. The authors suggest that apparent "trap-happiness" in the data may instead reflect non-random space use, not a true behavioural response.

## Key Findings

**Study design and data**
- Sampling covered 120 camera trap stations over 48 nights (24 January to 16 March 2006), with two cameras per station.
- Encounter histories were recorded for 44 individual tigers. Each history was a 120 × 48 binary matrix.
- There were 65 unique individual/occasion combinations and 68 total encounter events.
- Fifteen individuals were captured in more than one trap. Only three "extra-trap captures" occurred, all within a single occasion.
- Of the 68 encounter events, 24 were recaptures, which supply the information about the encounter process.
- Compared with the earlier analysis (Royle et al. 2009, n = 45), one individual was found to be a recapture on reanalysis. The current dataset therefore has one fewer individual but one more recapture.

**Model development**
- Individual capture probability is modelled as a function of distance from each activity center to each trap, using a half-normal detection function (quadratic distance effect) or an exponential detection function.
- Two observation models are compared: a Poisson count model, and a Bernoulli model that records at most one capture per trap per occasion. The authors argue for the Bernoulli model because repeated captures within a night are highly correlated and hard to partition.
- Data augmentation with a zero-inflation parameter (ψ) is used to estimate unknown population size N, under a discrete uniform prior.
- The authors demonstrate that when N is known, the models reduce to standard Poisson or logistic-type GLMMs with random activity centers. Complementary log-log links handle the Bernoulli case.

**Density results**
- Using the half-normal model with behavioural response, the posterior mean density over the study area is 13.4 tigers per 100 km², with a 95% posterior interval of (9.3, 19.6).
- The earlier misspecified multinomial model (Royle et al. 2009) gave about 14.3 tigers per 100 km² with a 95% interval of (2.8, 20.5). The new estimate is similar but substantially more precise.
- The exponential detection model gave summaries of N and density "little changed" from the half-normal model.
- Spatial variation is marked. The highest-density areas have about eight times the density of the lowest-density areas, with a range of roughly 5.35 to 42 tigers per 100 km².
- The distance parameter (1/σ) is strongly positive, with a posterior 95% interval of (0.017, 4.974).

**Behavioural response**
- Under the half-normal model, encounter probability before initial capture is p1 = 0.0157 and afterwards p2 = 0.0292. This implies nearly a doubling of encounter probability, but the difference is imprecise (Pr(β − α > 0) = 0.92).
- The authors consider this biologically unrealistic and likely due to non-random space use. Under the exponential model the behavioural response is much weaker, with the posterior centred near zero.

**Model adequacy**
- Bayesian P-values were used, with values near 0.5 indicating adequate fit.
- Half-normal model: FIT1 P = 0.48 and FIT2 P = 0.47.
- Exponential model: FIT1 P = 0.52 and FIT2 P = 0.61.
- The null model M0, with behavioural response and distance effects set to zero, fitted encounter frequencies adequately (P = 0.58) but was clearly inadequate for spatial clustering (FIT2 P < 0.001).

**Methodological conclusions**
- The hierarchical Bayesian framework is preferred because classical asymptotic methods are questionable with small samples such as the 44 individuals and 24 recaptures here.
- The authors caution against overly complex models for small datasets. Individual heterogeneity models are poorly identifiable with so few animals (Link 2003, Dorazio and Royle 2003).
- Spatial proximity to traps is treated as the main source of heterogeneity, modelled through the spatial covariate.
- The approach is broadly applicable to hair snare, DNA and other non-physical capture methods, and to other carnivores including [[Ocelot]], [[Black Bear]], [[Wolverine]] and [[Pampas Cat]].