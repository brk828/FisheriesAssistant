---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [capture-recapture, population-estimation, closed-population, statistical-ecology, removal-sampling, primer]
title: "Capture-Recapture and Removal Methods for Sampling Closed Populations"
source_id: "PML2877"
marsh_id: "PML2877"
library: "Marsh Library"
permission: "public domain"
source_citation: "Gary C. White, David R. Anderson, Kenneth P. Burnham, David L. Otis (1982). Capture-Recapture and Removal Methods for Sampling Closed Populations. Los Alamos National Laboratory report LA-8787-NERP. Marsh Library ID: PML2877."
source_file: "White et al. 1982. Capture-Recapture and Removal Methods for Sampling Closed Populations.pdf"
text_extraction: "mixed"
---
# Capture-Recapture and Removal Methods for Sampling Closed Populations: A Primer

#ichthyology #marine-biology #statistical-ecology

## Executive Summary

This document is a primer (preface, chapters 1 to 7 and selected appendix material) by G. C. White, D. R. Anderson, K. P. Burnham and D. L. Otis, written as an accessible companion to the monograph by Otis et al. (1978). It presents the statistical concepts and practical methods for estimating the size and density of animal populations that are assumed to be closed, using [[Capture-Recapture Sampling]] and [[Removal Sampling]] designs. Its emphasis is on concepts and study design rather than derivations. The primer covers eight candidate capture models (Mo, Mt, Mb, Mh and their combinations), associated estimators, a suite of seven goodness-of-fit and assumption tests, and the [[Program CAPTURE]] software that automates model selection and estimation. The authors stress that closure, adequate capture probability and sufficient sample size are the critical requirements, and that a population estimate without a precision measure and an assessment of assumptions is not scientifically valid.

## Background & Description

The primer was written in December 1980 for students and biologists who were not expected to have strong quantitative training beyond introductory statistics. It is intended to be read alongside the monograph and Appendix C lists supplementary reading. The preface notes that many workshop participants did not fully understand the monograph's key points, motivating this simpler treatment. Appendices include a FORTRAN 77 user manual for CAPTURE (Appendix A), answers to chapter exercises (Appendix B), and a general reading list (Appendix C).

The historical sketch in the text profiles several pioneers of the field, including [[Ronald A. Fisher]] (maximum likelihood), [[Peterson-Lincoln Estimator]] originators, George Schnabel, Calvin Zippin, John Darroch, Douglas Chapman, Norman Bailey, Kenneth Burnham, and Leslie Davis-related work on vole populations.

Closure is defined as the absence of births, deaths, immigration and emigration during sampling. Two forms are distinguished: geographic closure (a boundary limits the population) and demographic closure (no gains or losses). Data are summarised in an X matrix of capture histories (1 = captured, 0 = not captured) for each individual on each occasion.

## Ecological & Environmental Context

The primer addresses animal populations generally, with examples from small mammals (voles, mice, Richardson's ground squirrels, pocket gophers, snowshoe hares), fish (electrofishing and removal of fish from ponds and lakes), sea birds (nest success), cotton rats, and wild horses. Variation in capture probability is attributed to three sources: time (weather, effort, trap operation), behavioural response (trap happiness or trap shyness after first capture), and heterogeneity (age, sex, social dominance, home-range position, activity level).

Study design considerations include trap spacing relative to home-range size (the authors suggest spacing no more than about half the home range radius, with at least four traps per home range), the boundary strip effect on density estimates, and avoidance of mortality in traps. Killing traps can cause immigration into the area as local animals are removed, so the study should be short.

## Key Findings

**Core concepts and models**
- Eight models are defined by three sources of variation: Mo (constant p), Mt (time), Mb (behaviour), Mh (heterogeneity), and combinations Mtb, Mth, Mbh and Mtbh.
- Model Mo has a closed-form estimator only for two occasions; the ML estimator requires numerical methods. The Schnabel, Darroch, Zippin and Jackknife estimators are the principal alternatives. The Generalised Removal estimator is used for Mh and removal data.
- Models Mtb, Mbh, Mtbh and Mth have no associated estimator.
- In the Mo example with N = 50 and p = 0.3, the Peterson-Lincoln style estimate varied among replicate simulations; the authors show sampling variability is small for this model when the assumptions hold.

**Worked numerical examples (simulation)**
- For Mo (N = 50, p = 0.3, t = 5), the mean ML estimate across 10 simulations was 49.1 with a standard error of 1.1.
- Under Mt with N = 150, the estimator for data with daily capture probabilities of 0.20 to 0.25 yielded estimates centred near the true value.
- For Mb (trap happy) with N = 100, p = 0.25, c = 0.55, t = 7, the 10-run average estimate was 102.4.
- Under Mh (N = 200), the jackknife estimator averaged 201.3 across replicates; the generalised removal estimator under the same model was biased low (about 175 to 180 in some runs).
- The removal example with N = 625 and p = 0.4 over four removals gave an ML estimate of 562 for the simulated data, with a standard error of 50.0.

**Sample size and design guidance**
- Estimates are unreliable when the number of animals caught is only around 10 to 20; the captured count should be several times larger, and average capture probabilities at least about 0.1, preferably 0.2 or more.
- The coefficient of variation of N should ideally be 0.10 or less for research; 0.20 to 0.30 may be acceptable for management monitoring.
- Recommended minimum: at least 5 trapping occasions for closed-population designs, and at least 3 (preferably 4 or more) removal occasions.
- Grid recommendations: r + c of at least 25 (for example a 13 by 13 grid) for density estimation with nested subgrids.

**Model selection and testing**
- Seven tests compare models and check goodness of fit; program CAPTURE combines them into normalised selection criteria. The authors caution that goodness-of-fit tests for Mh have low power.
- Closure tests can only be made under Mo or Mh assumptions and may reject closure when behavioural or time effects are responsible; the authors state no valid closure test can be built from capture-recapture data alone.

**Density estimation**
- Density D is estimated from nested subgrids using a boundary strip width W, with the naive density of each subgrid regressed against subgrid area.
- In the Richardson's ground squirrel example (10 by 10 grid, 5 occasions), the estimated density was about 64.9 animals per hectare, with the boundary strip estimated as significantly greater than zero (P < 0.01).

**Practical cautions**
- Equal effort on each trapping occasion is strongly recommended; unequal effort introduces time variation and can cause the correct model to have no estimator.
- Unique marking of individuals is preferred; without it, a capture-history X matrix cannot be built and model selection is not possible.
- Sampling variation, spatial variation and temporal variation are distinct sources of variability that should be recognised.
- A 95% confidence interval for N is typically computed as N-hat plus or minus 1.96 standard errors; lower bounds below the number of animals caught should be replaced by that count.