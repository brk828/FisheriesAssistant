---
species: Sylvilagus floridanus
common_name: Eastern Cottontail
family: Leporidae
habitat: Penned population (example dataset); trapping grids for density estimation
ocean_basin: N/A
location: N/A
tags:
  - leporidae
  - population-ecology
  - mark-recapture
  - software-manual
title: "User's Guide for Interactive Program CAPTURE"
source_id: "PML2192"
marsh_id: "PML2192"
library: "Marsh Library"
permission: "public domain"
source_citation: "E. Rexstad, K. Burnham (1991). User's Guide for Interactive Program CAPTURE. Colorado Cooperative Fish and Wildlife Research Unit, Colorado State University (User's Guide). Marsh Library ID: PML2192."
source_file: "Rexstad E. Burnham K. 1991. User's guide for interactive program capture.pdf"
text_extraction: "text"
---
# CAPTURE User's Guide: Abundance and Density Estimation Software

#leporidae #population-ecology #mark-recapture

## Executive Summary

This July 1991 user's guide describes an enhanced release of [[Program Capture]], a software package for estimating animal abundance and density from [[Mark-Recapture]] data under the [[Closed Population Models|closed-population]] assumption. The guide was written by Eric Rexstad and Kenneth Burnham of the Colorado Cooperative Fish and Wildlife Research Unit at Colorado State University. The release adds an interactive front end, [[2Capture]], for data entry, new estimators, revised confidence intervals, a revised jackknife variance, and expanded [[Simulation Experiments]]. The guide is a software manual, not a field study. Its only biological content is a worked example using capture data from a penned population of Eastern Cottontails.

## Background & Description

The manual extends earlier work on CAPTURE by [[Otis Et Al 1978]] and [[White Et Al 1982]]. The software has two components:

- **2CAPTURE**, an interactive front end that prompts for input, checks responses for inconsistencies, and writes command files. It uses a pull-down menu interface and is accessed through a top-level menu.
- **CAPTURE**, the analytical component. It can also run in batch mode, as in earlier versions.

Menus cover title specification, data reading, model testing, estimation, simulation, and program execution.

**System requirements:**
- IBM-PC compatible computer with an Intel 80x87 numeric coprocessor. Without it, CAPTURE generates an Error 4001 message.
- About 540 Kb of free memory after loading memory-resident programs. CAPTURE is about 430 Kb and 2CAPTURE about 110 Kb, and both must be resident simultaneously.

**Program limits:** 8 nested grids for density estimation and 1000 animals in simulations. Exceeding these requires recompiling after editing PARMTR.INC.

**Distribution files:** 2CAPTURE.EXE, CAPTURE.EXE, a shareware file scanner (LIST), an editable help file, an examples file from Otis et al. (1978), and EDWARD.CAP, the input file used in the guide's example.

## Ecological & Environmental Context

The estimators assume the population is closed, meaning its size and composition stay constant during the study. The guide notes that the [[Closure Test]] has poor power and rarely rejects closure. Estimators are designed around different sources of capture heterogeneity:

- **Time effects:** capture probability varies by occasion.
- **Behavioral effects:** capture probability changes after first capture (trap happiness or shyness).
- **Individual heterogeneity:** capture probability differs among animals.

Density estimation requires trapping grids with equally spaced stations, and it uses a [[Nested-Grid Approach]] that the guide says often fails. Other density methods can use the abundance output from CAPTURE.

## Key Findings

**Data input and model selection**
- Four input types are supported: XY Reduced (the default), XY Complete, Non-XY, and X-Matrix. Only XY types support density estimation.
- A format statement is required for reading data from files. The guide's example uses (T15,A3,3X,18F1.0) for the EDWARD.CAP file.
- The [[Model Selection]] algorithm, based on Otis et al. (1978:57-61), tests for time, behavior, and heterogeneity effects. It then uses a discriminant function to choose the appropriate estimator. Model selection is recommended.

**Estimators**
- Ten abundance estimators are available: Null (M0), [[Darroch Estimator]] (Mt), [[Chao Estimator|Chao's Mt]], Jackknife (Mh), [[Chao Estimator|Chao's Mh]], [[Zippin Estimator]] (Mb), [[Removal Estimator|Generalized Removal]] (Mbh), [[Pollock And Otto Estimator|Pollock and Otto's]] estimator (Mbh), [[Chao Estimator|Chao's Mth]], and [[Burnham Estimator]] (Mtb).
- No estimator exists for the Mtbh model.
- Seven density estimators are available, omitting Pollock and Otto's and Mtbh.
- The new Chao Mt, Chao Mh, Chao Mth, and Burnham Mtb estimators can be requested by keyword. Only the first four characters of each keyword are needed.

**Confidence intervals and variance**
- Confidence intervals for all estimators now use a log-normal approach (Burnham et al. 1987; Chao 1989). This keeps the lower bound at or above the number of distinct animals captured, which the earlier method did not guarantee.
- [[Profile Likelihood Interval|Profile likelihood intervals]] are reported for the Mo, Mt, Mb, Mbh, and Mtb estimators, which have explicit likelihoods. Profile intervals appear only in batch mode with the PROFILE option; they are not computed in simulations.
- The jackknife variance, previously biased low, now uses an unconditional calculation that averages over the estimators selected by sequential chi-square tests.

**Simulation experiments**
- Simulation defaults: seed 1234567, population size 400 (maximum 1000), 7 occasions (maximum 31), and 50 replicates.
- Capture heterogeneity can be specified by homogeneous subpopulations or beta distributions, the latter available only in batch mode.
- Summary tables now include averages, standard deviations, and confidence interval coverage for all models.

**Worked example (EDWARD.CAP)**
- Source: Edwards and Eberhardt (1967), a penned population of 135 wild Eastern Cottontails (*Sylvilagus floridanus*). The true population size is known, which allows estimator performance to be checked.
- The dataset has 18 trapping occasions and 76 animals captured in X-matrix format.
- Model selection favored a time-variation model, and the software suggested the Darroch estimator.
- The Mo estimate was 96 with a standard error of 6.51, under constant capture probability.
- The removal estimate was 94 with a standard error of 10.78.
- Of the 10 estimators, 5 confidence intervals covered the true value of 135. Four of those five came from the newly added estimators.

**Simulation example**
- Setting: N = 100, 100 replicates under the Mtbh model with model selection.
- Of 91 valid replicates, 29 covered the true population size, giving 31.87% coverage. The guide attributes the shortfall to the 9 failed replicates and the known difficulty of this model.

**Limitations and future work**
- Profile likelihood intervals have not been incorporated into the simulation procedure.
- The authors express confidence in the estimators, with possible exception of the Mtbh estimator.
- The model selection algorithm "is in need of extensive work," and some underlying tests may be improved.

**Funding:** The work was supported by the U.S. Fish and Wildlife Service Region 6 Enhancement Program through the Rocky Mountain Arsenal.