---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [animal-abundance, capture-recapture, population-estimation, statistical-ecology, review]
title: "Estimating animal abundance: review III"
source_id: "PML2316"
marsh_id: "PML2316"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. J. Schwarz, G. A. F. Seber (1998). Estimating animal abundance: review III. Marsh Library ID: PML2316."
source_file: "Schwarz C.J. 1998. Estimating animal abundance review 3.pdf"
text_extraction: "mixed"
---
# Estimating Animal Abundance: A Review of Recent Developments

#ichthyology #marine-biology #population-estimation

## Executive Summary

This is a statistical review by Carl J. Schwarz and George A. F. Seber covering methods for estimating animal abundance and related demographic parameters (survival, movement, breeding proportions) from roughly 1991 to the time of writing. It updates two earlier reviews by the same authors (Seber, 1982 and 1986/1992). The review is explicitly broader than abundance alone and covers the principal sampling families: index and survey methods, distance sampling, removal and catch-effort models, change-in-ratio, [[Capture-Recapture]] for closed and open populations, [[Radio Telemetry]], and [[Survival Analysis]]. Fish-specific applications (fisheries catch-effort, stratified trawl surveys, tagging of salmon and herring) appear throughout, but the review itself is general-purpose and does not focus on fish alone.

## Background & Description

The authors define the basic distinction on which method choice depends:

- **Closed populations** remain effectively unchanged during the investigation.
- **Open populations** change through birth, death, and migration.

Methods are organized by the information they yield:

- **Counts and signs:** random plots (quadrats or strips) or lines and points. Sign counts give only a relative index of density, which is useful if the index is proportional to density.
- **Distance sampling:** line-transect and point-transect methods model the detection function g(y) as a function of perpendicular distance.
- **Removal and catch-effort:** effort-based removal of animals; common in [[Fisheries Management]].
- **Change-in-ratio:** removal of one sex or class shifts the observed ratio, from which abundance is inferred.
- **Tagging and marking:** [[Petersen Estimator]] for two samples and multi-sample models (Cormack-Jolly-Seber, Jolly-Seber) with capture histories.

The review assumes readers have access to the standard texts (Seber 1982, 1992; Buckland et al. 1993; Pollock et al. 1990) and to the software listed in Appendix 1, including [[Program Mark]], [[Popan]], [[Program Capture]], and the [[Distance Sampling]] package.

## Ecological & Environmental Context

The authors stress several recurring assumptions that drive field error:

- **Observer and detection bias:** experienced and inexperienced observers differ; some animals are hard to detect (deer are cited as an example); visibility bias can cause negative bias in counts.
- **Heterogeneity:** capture, sighting, and survival probabilities often vary among individuals, which the review identifies as the most-studied violation.
- **Tag loss and tag reporting:** tags may be lost, overlooked, or unreported by the public; reporting rates vary with reward value and geography.
- **Radio-tagging effects:** survival must be unaffected by the radio; location error from signal reflection is a recurring problem.
- **Clustered populations:** sparse but highly clustered populations (e.g., fish schools, aggregated species) motivate [[Adaptive Sampling]].
- **Movement and trap layout:** movement and trap placement can bias population estimates.

Fisheries examples discussed include bottom-trawl surveys stratified by depth, angler creel surveys (roving vs. access-point, with size bias), catch-per-unit-effort (CPUE) estimation, salmon escapement estimation via stratified-Petersen and fence-based designs, and tag-recovery studies of migration among geographic strata.

## Key Findings

**Methodological trends identified by the authors**

1. **Logistic regression and Horvitz-Thompson estimation** are increasingly used to model detection probabilities and correct for undetected animals in line-transect sampling (Buckland et al. 1993; Borchers et al.).
2. **Double-count and double-platform methods** combined with line-transect theory allow estimation of g(0) < 1, i.e. detection probability on the trackline.
3. **Bayesian methods** have become practical through Monte Carlo methods, including the [[Gibbs Sampler]], and are being applied to capture-recapture, band-recovery, and line-transect data.
4. **Quasi-likelihood** is used for over- or under-dispersed data in capture-recapture and relative-density studies.
5. **Model selection** using [[Akaike Information Criterion]] (AIC) and model averaging is now standard, with calls to account for model uncertainty in reported precision.
6. **Robust design** (Pollock 1982) combines open-population models across primary periods with closed-population estimation within secondary periods.
7. **Multi-strata and movement models** extend [[Cormack-Jolly-Seber Model]] approaches to estimate migration among geographic strata, with applications to geese, ducks, and fish.

**Specific reported results and cases (examples from the text)**

- Petersen estimator: N̂ = n1 n2 / m2, obtained by equating tagged proportions in the population and second sample.
- Sample coverage: estimators of species numbers and capture-recapture population size developed for eight closed-population models (Mo, Mt, Mb, Mtb, Mh, Mth, Mbh, Mtbh).
- Radio-tagged pigeons were used to estimate nest numbers on keys in Florida (Strong, Sawicki and Bancroft, 1994).
- Anderson and Southwell (1995): experts and novices both underestimated line-transect density by about 10%.
- Hwang and Chao (1995): new JS estimators are less biased when the coefficient of variation in catchability exceeds 0.4.
- Borchers and colleagues show that doubled-platform and multi-observer line-transect methods estimate g(0) < 1 jointly with covariates.
- Gould and Pollock: maximum likelihood catch-effort estimates were consistently less biased and more precise than least-squares estimates.

**Outlook and recommendations**

- The subject has grown too large for one person to track. The authors recommend more reviews and expository articles, and jokingly suggest a dedicated journal.
- Future research should extend movement and multi-strata models to non-fisheries contexts and to strata based on age or length rather than place.
- Robustness of each new model to heterogeneity needs to be checked routinely.
- Guidelines on experimental design, including when to use adaptive sampling, are needed.
- A generalized software package for analysing diverse survey data is still lacking.
- Training for future scientists should include broader statistics and computing, since bootstrapping and Monte Carlo methods are now essential tools.

**Funding and acknowledgements:** supported by a Natural Sciences and Engineering Research Council of Canada (NSERC) grant to C. J. Schwarz.