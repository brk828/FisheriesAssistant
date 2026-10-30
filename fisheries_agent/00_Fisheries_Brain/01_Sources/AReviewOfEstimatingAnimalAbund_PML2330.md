---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Great Britain (journal context); Auckland, New Zealand (author affiliation)
tags: [population-estimation, animal-abundance, capture-recapture, aerial-census, distance-sampling, fisheries-models, wildlife-statistics]
title: "A Review of Estimating Animal Abundance II"
source_id: "PML2330"
marsh_id: "PML2330"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G.A.F. Seber (1992). A Review of Estimating Animal Abundance II. International Statistical Review, 60(2), pp. 129-166. Marsh Library ID: PML2330."
source_file: "Seber G.A.F. 1992. A review of estimating animal abundance.pdf"
text_extraction: "text"
---
# Review of Estimating Animal Abundance II

#ichthyology #marine-biology #population-estimation

## Executive Summary

This document is a statistical review by G.A.F. Seber, from the Department of Mathematics and Statistics at the University of Auckland, published in the *International Statistical Review* (1992). It updates an earlier review and surveys recent developments in methods for estimating animal abundance and related parameters. Its scope is general wildlife and population science rather than a single species. Methods are covered for radiotelemetry, aerial censusing, distance sampling, [[Removal Method]] approaches, [[Change-In-Ratio Methods]], [[Capture-Recapture Methods]], [[Home Range Estimation]], open-population models, and [[Catch-Effort Models]]. Fish-specific material (acoustics, trawl indices, electrofishing, catch-effort) appears within these sections.

## Background & Description

The review follows an earlier installment (cited as "Sb1" and "Sb2" in the text) and emphasizes methodological advances that continue to shape population estimation:

- **Radiotelemetry** is now widely used across taxa, including small rodents and marine mammals. Radiotransmitters supply information on home range, mortality rates and correction factors for aerial censusing. Users must understand transmitter types, assess their accuracy and recognize technical limits.
- **Passive integrated transponder (PIT) tags**, roughly the size of a grain of rice, can be injected to give a permanent, unique mark that is almost never lost and rarely fails.
- **Photo-identification** of individual whales and dolphins from fluke markings supports population parameter estimation.
- **Computer packages** with built-in model selection and simulation facilities are becoming standard. Resampling methods ([[Bootstrap Methods]], [[Jackknife Methods]]) are increasingly used for variance and interval estimation.

## Ecological & Environmental Context

The review addresses several environmental and biological constraints on estimation:

- **Visibility and availability bias** in aerial surveys, caused by animals hidden by vegetation, terrain, other animals, or turbidity in water. Seal pups that have left the whelping concentration, and underwater aquatic animals obscured by turbid water, are cited examples.
- **Heterogeneity of catchability and sightability**, linked to sex, age, behavior, and trap response, which biases many estimators.
- **Size bias** in line transects, where detection depends on animal size (e.g., size of fish).
- **Electrofishing effects**: electricity can have substantial physiological effects on fish, and larger fish are affected more, altering capture probabilities.
- **Habitat constraints**: rugged terrain and dense cover complicate ground and aerial counts for deer and similar species.
- **Biological considerations** should guide model choice alongside statistical criteria.

## Key Findings

**Acoustic and visual methods**
- Acoustic methods are a major tool for estimating fish abundance, but interpreting readings is difficult. Adaptive sampling is expected to play a larger role.
- Transect designs must be truly random. Zigzag transects, which do not allow proper statistical analysis, should be avoided.

**Aerial censusing and photography**
- Incomplete counts (visibility bias) remain the main problem in aerial surveys.
- Correction approaches include ground counts (double sampling), double-observer counts analysed as a [[Petersen Method]] experiment, the removal method, and radio-collared animals as a sightability reference.
- Double-observer methods assume independent observer sighting. The author advises caution, especially when the two observers have different viewing angles.
- Aquatic surveys using aerial or ground methods suffer availability bias from turbidity. Marsh & Sinclair (1989a, b) used clear and turbid water counts.

**Distance methods**
- Line transect methods, implemented in the program TRANSECT and later DISTANCE, are widely used for individuals and groups. Hazard-rate models performed well across terrestrial and dolphin data.
- Line transects generally have smaller mean square error than strip transects and allow recording of all detected objects, not only those within a fixed strip width.
- Key assumptions include certain detection on the line and no animal movement in response to the observer. Violations bias density estimates.

**Capture-recapture**
- Single-recapture models include hypergeometric, binomial, Poisson and multinomial forms. Confidence intervals for N are sensitive to the chosen distribution, and profile likelihood intervals are preferred.
- Multiple-recapture models (e.g., the CAPTURE program) are compared. Menkins & Anderson found CAPTURE model selection unreliable when N < 100. Jackknife estimators performed best in a known skunk population (Greenwood, Sargeant & Johnson, 1985).
- Edge effects in trapping grids require correction. Density estimates ignoring edge effects are unreliable.

**Change-in-ratio and removal methods**
- The removal method is less efficient than the Petersen estimate and is more sensitive to observer heterogeneity.
- CIR methods are presented as an attractive alternative for white-tailed deer, since they require little data.

**Open populations and survival**
- The Jolly-Seber (J-S) model is central. Software includes POPAN, RELEASE, and MARK-type programs (Lebreton et al., 1992).
- Recovery models for dead animals (banding and tagging data) have grown steadily. The Brownie et al. (1985) framework is widely cited. Heterogeneity and compensatory mortality remain open problems.
- Survival estimation is shifting from population size toward survival estimators, which are more robust to heterogeneity in catchability.

**Catch-effort and demographic methods**
- Catch-per-unit-effort (CPUE) is often assumed to index stock abundance, but the catchability coefficient q may change with density. Stochastic and bootstrap approaches are developing.
- Demographic methods (life tables, Leslie matrices, age-structured models) are reviewed, with a call for a comprehensive survey of catch-effort literature.

**Overall conclusions**
- Summarized as: the Petersen method using radio transmitters is the most promising technique, particularly when detection on the line is not certain.
- The author notes that the home range topic remains confused and that edge-effect questions need further work.
- The review calls for stronger design guidance, more research on Bayesian methods, and better handling of tag loss through double tagging.