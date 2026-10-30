---
species: Lingcod (Ophiodon elongatus)
common_name: Lingcod
family: Hexagrammidae
habitat: Marine demersal shelf waters; commercial trawl fishery
ocean_basin: Pacific
location: Southwest Vancouver Island, British Columbia, Canada (PMFC Major Area 3C-N)
tags: [fish-growth, size-structured-model, stock-assessment, errors-in-variables, lingcod, fisheries-science]
title: "Fish growth: investigations based on a size-structured model"
source_id: "PML2301"
marsh_id: "PML2301"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. T. Schnute, L. J. Richards, A. J. Cass (1989). Fish growth: investigations based on a size-structured model. Canadian Journal of Fisheries and Aquatic Sciences, vol. 46. Marsh Library ID: PML2301."
source_file: "Schnute J.T. et al. 1989. Fish growth investigations based ona size structure model .pdf"
text_extraction: "text"
---
# Fish Growth: Investigations Based on a Size-Structured Model

#ichthyology #marine-biology #hexagrammidae

## Executive Summary

This paper (Schnute, Richards & Cass, Canadian Journal of Fisheries and Aquatic Sciences, vol. 46, 1989) develops and tests a size-structured population model built on the linear [[Ford-Walford Growth Law]] for individual fish growth. Weight at the start of one year determines weight one year later, and survival is combined with growth through a population-level dynamic equation. The authors derive statistical estimators and confidence regions for the growth parameters and apply them to a [[Lingcod]] stock off southwest Vancouver Island. Tag recapture data provide the primary estimates, and aged fishery samples and size-frequency fishery data serve as consistency checks. The paper is the first of two; the companion paper addresses survival and recruitment.

## Background & Description

The authors frame growth as a linear law, w' = W + ρw, where w is weight at the start of a year, w' is weight one year later, W is the intercept and ρ the slope. The law generalizes the [[Von Bertalanffy Growth Equation]] for 0 < ρ < 1 (with asymptotic size W∞ = W/(1-ρ)) and remains valid for ρ > 1, where no asymptote exists. Weight is used as the size measure because total catch weight is recorded in the fishery and tagged-fish data directly support the linear law.

Schnute's size-structured model rests on three assumptions:

1. The linear growth law described above applies to individual fish.
2. A population density N(w, t) obeys a conservation relation in which survivors from year t, after growth, define the weight distribution in year t+1. Only fish already recruited are included.
3. Mortality is not size selective for recruited fish, so the survival fraction equals 1 for weights at or above the recruitment weight V.

Population quantities (numbers, biomass, mean weight and weight dispersion of order n, with variance at n = 2) are defined for the total, newly recruited and previously exploited groups (Table 1).

The authors note a formal analogy with [[Kinetic Theory of Gases]]: the individual growth law parallels the population growth law, and growth shrinks or expands weight dispersion depending on whether ρ is below or above 1.

## Ecological & Environmental Context

The worked example concerns [[Lingcod]] in [[Pacific Marine Fisheries Commission Area 3C-N]], where a commercial trawl fishery takes most of the catch. Biological samples have been collected since 1956. Female lingcod tend to be larger than males at a given age, but landed fish were dressed and headed at sea before 1975, so sex could not be determined. Sampling therefore uses only the May–September fishery, when sexes are nearly equally mixed. The authors argue that the size-structured model is more robust to sexual size differences than an age-structured model.

Choosing the minimum recruitment weight V is a compromise: it must be large enough for constant gear selectivity but small enough to retain most of the catch. Weight-frequency distributions averaged over 1956–86 indicated near-full recruitment at 2.25 kg, the lower bound of the 2.5 kg weight class.

Data sets used:
- Tagged fish released in 1982 and recovered in 1983 (364 fish), the main source for parameter estimation.
- Aged fishery samples from 1977–85, used to fit a von Bertalanffy curve.
- Size-frequency fishery samples from 1956–86, compiled into weight-frequency tables.

## Key Findings

- **Model equations:** Schnute's model yields four population relations: numbers at t+1 equal new recruits plus survivors; biomass at t+1 is survivors scaled by a survival factor and a growth factor X'/X; mean weight of previously exploited fish follows the projected growth law; and dispersion is multiplied by ρ.
- **Errors-in-variables estimation:** Tag data fitted with an errors-in-variables model give ρ and V' by maximum likelihood (eqs. 2.8–2.9). The paper shows that a likelihood-ratio approach yields confidence regions for both parameters.
- **Tag-based estimates (adopted):** ρ = 1.025 and V' = 2.88 kg (Table 3, eq. 3.6). The 95% confidence region for ρ spans roughly 0.997 to 1.054. V' varies from 2.25 to 3.83 kg in this region, so it is less precisely defined.
- **Single-parameter confidence interval for V':** A 95% interval of (2.5 kg, 3.64 kg) is reported when V' is treated as the sole parameter of interest. The lower bound 2.5 kg is set by the constraint V' ≥ V.
- **Von Bertalanffy comparison:** Least-squares fitting of the von Bertalanffy growth curve to aged fishery samples (ages 2–17 years) gives an estimated ρ of 0.991 and V' of 2.98 kg, close to the tag-based estimates. The authors nonetheless prefer tag-based estimates because the errors-in-variables approach models measurement error realistically and the tag data directly support the linear law.
- **Fishery size-frequency data:** Fishery-based estimates with fixed V' = 2.88 kg and V' = 3.50 kg were tested and rejected. With V' = 3.50 kg, most tagged points lie below the fitted line, and the fitted ρ falls below the tag-data confidence region.
- **Extreme case:** Constraining V' to 3.50 kg gives ρ = 1.024 (eq. 3.7). This case is kept to examine the consequences of a large V'.
- **Empirical support for the gas analogy:** Tag data and fishery population means share a trend line of slope ρ through (V, V'), and fishery standard deviations follow a parallel line through the origin. The authors interpret this as evidence that individual and population behavior are linked as theory predicts.
- **Model assumptions for fishing mortality:** Equal survival for recruited fish is assumed, extending the common assumption that natural mortality is size-independent.
- **Companion work:** Survival and recruitment estimation, and serial correlation from process error, are deferred to Schnute, Richards & Cass (1989).