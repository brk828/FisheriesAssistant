---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Fort Collins, Colorado, USA
tags: [population-ecology, capture-recapture, software, statistics]
title: "Program MARK"
source_id: "PML2879"
marsh_id: "PML2879"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. C. White, K. P. Burnham (1997). Program MARK. Marsh Library ID: PML2879."
source_file: "White G.C. Burnham K.P.1997. Program Mark.pdf"
text_extraction: "text"
---
# Program MARK: Software for Mark-Recapture Parameter Estimation

#population-ecology #mark-recapture #capture-recapture

## Executive Summary

This document is a documentation and distribution page for [[Program Mark]], a Windows 95/NT program that estimates demographic parameters (survival, recapture, recovery, recruitment, and population size) from marked animals that are re-encountered later. It covers the supported data types, the models and parameterizations, installation and distribution notes, version-change history, training opportunities, known problems, and a reference list. The page does not address any particular fish species or aquatic habitat. Its example data come from an [[American Fisheries Society]] monograph on fish survival experiments, but no species is named.

## Background & Description

[[Program Mark]] fits models to an encounter history for each animal. Re-encounters can come from:

- **Dead recoveries**, such as harvested animals
- **Live recaptures or resightings**, such as re-trapped or re-sighted animals
- **Radio tracking**
- Combinations of these sources

Time intervals between encounters need not be equal; they default to one time unit. The program can model several attribute groups (for example, treatment and control animals) and covariates. Parameters can be constrained through a parameter index matrix (PIM) and a design matrix, and link functions include logit, probit, log-log, complementary log-log, sine, log, and identity.

Key features and interface:

- Results are stored in a Results Database that keeps the input and output for each model.
- The Results Browser shows estimates, standard errors, goodness-of-fit tests, deviance residuals, likelihood ratio tests, and over-dispersion adjustments.
- The interface uses context-sensitive help, and the theory is described in an electronic book.
- Program MARK provides **[[Cormack-Jolly-Seber Model]]**, **[[Dead Recovery Model]]**, **[[Joint Live and Dead Recovery Model]]**, **[[Known Fate Model]]**, **[[Closed Capture Model]]**, **[[Robust Design Model]]**, **[[Multi-Strata Model]]**, and **[[Jolly-Seber Model]]** data types, with six to seven data types in total depending on how the list is counted.

Alternative programs named in the document include [[Program Surge]], [[Program Capture]], and [[Program Fofana]] (rendered in OCR as "FoFAf{"). The document notes that none of these three handles band recovery, joint live-dead, robust design, or multi-strata models.

## Ecological & Environmental Context

The methods target wildlife and fisheries populations where individuals are marked and later re-detected. The document's examples are mostly general and include:

- Survival estimation in the presence of emigration. In the [[Cormack-Jolly-Seber Model]], the apparent survival phi(i) equals s(i)(1 − E(i)), where E(i) is the probability of emigrating from the study area.
- Dead recovery studies, where [[Band Recovery Models]] estimate survival S(i) and band reporting rate r(i).
- Known-fate studies, often using radio telemetry, where encounter probability is 1 whether the animal is alive or dead.
- Closed-population abundance estimation (N), where [[Individual Heterogeneity]] is a key limitation.
- Temporary emigration in the [[Robust Design Model]], which uses multiple trapping sessions close together in time.
- The example data from the American Fisheries Society monograph (Burnham et al. 1987) on fish survival experiments based on release-recapture. It has 5 re-encounter occasions and 2 groups and is live recapture data.

## Key Findings

**Scope and capabilities**
- Models cover live recapture, dead recovery, joint live/dead, known fate, closed capture, robust design, multi-strata, and Jolly-Seber data.
- Individual covariates can be used in the [[Huggins Models]], which were added in June 1998 to the closed capture and robust design models.
- Closed capture models cannot use individual covariates because never-captured animals enter the likelihood through N.
- The multi-strata model includes only the movement model without memory.

**Parameterization notes**
- MARK uses the primary parameterization S(i) and r(i) for band recovery models. This improves numerical stability and matches the CJS parameterization. The last S(i) and r(i) are confounded.
- When S(i) is at or near one, its standard error is not estimated correctly.

**Software distribution and installation**
- The program is a test version and was distributed on multiple zipped disks, or as one large "onedisk" zip file.
- It does not run well on Windows 3.1. Windows 95 and NT are supported, but NT lacks some threading features in simulation and multiple-model runs.
- SETUP must be run after unzipping. Installation should not target the unzipping directory.
- Graphics require registering two ActiveX packages: First Impression (vcfiu.ocx) and Graphics Server (graphs32.ocx).

**Version history**
- A new compiler was introduced on 3 March 1998 and requires updated files.
- On 11 September 1997 the author moved the numerical code to Digital Visual Fortran, reducing execution time to about 60% of before per the author's note.
- April 1998: interactive PIM charts, design matrix paste from the clipboard, a saturated model value for robust design (deviance still incorrect in some datasets), and a re-parameterized Barker model.
- May 1998: an "identity" design matrix keyword replaces stored matrices, and the non-estimability threshold was changed from 0.3E-6 to a dimension-dependent value.
- June 1998: seven new models were added, including Huggins (1991) for robust design, Jolly-Seber parameterizations, and Pradel (1996) recruitment, survival, and growth-rate models.

**Known problems**
1. The closed capture deviance divided by its degrees of freedom is not a valid estimate of c-hat, because these models are not in the exponential family.
2. Deviance is a poor goodness-of-fit test for sparse data. A parametric bootstrap procedure in the Tests menu is provided.
3. Running several estimation jobs at once can abort the program. Results can be recovered through the Output > Append menu.
4. Stability improves with more available memory, so closing other applications and restarting the program is recommended.

**Training and support**
- Documentation is electronic only, through a Windows Help file, an HTML version, a PDF, and a WordPerfect description prepared for the EURING 97 conference.
- An introductory user guide and course notes from Colorado State University (FW663, *Analysis of Vertebrate Populations*, taught by [[David R. Anderson]] and [[Gary C. White]]) are referenced.
- An intermediate workshop was scheduled for June 7–11, 1999, in Fort Collins, Colorado. A related course, FW663 "Sampling and Analysis of Vertebrate Populations," was planned for Spring 2000.

**Bug reports**
Users are asked to send the input file, the number of occasions, groups, and the data type, and any results file (MIME or uuencoded).

**Core references**
- Burnham et al. (1987): fish survival experiments based on release-recapture, the example dataset.
- Brownie et al. (1985): band recovery theory.
- Lebreton et al. (1992): modeling survival in marked animals.
- Pollock et al. (1990): capture-recapture inference.
- Kendall et al. (1995, 1997): robust design models.
- Huggins (1989, 1991): conditional likelihood with individual covariates.
- Pradel (1996): recruitment and population growth-rate models.

---

*Note: The original document also contains a 50-plus reference bibliography, promotional site and hit-counter material, and a few garbled OCR fragments, which were omitted.*