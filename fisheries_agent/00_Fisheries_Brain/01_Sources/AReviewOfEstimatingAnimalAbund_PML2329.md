---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Auckland, New Zealand (author affiliation)
tags: [animal-abundance, capture-recapture, population-estimation, biometrics, review]
title: "A Review of Estimating Animal Abundance"
source_id: "PML2329"
marsh_id: "PML2329"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. A. F. Seber (1986). A Review of Estimating Animal Abundance. Biometrics 42, 267-292. Marsh Library ID: PML2329."
source_file: "Seber G.A.F. 1986. A review of estimating animal abundance.pdf"
text_extraction: "text"
---
# A Review of Estimating Animal Abundance

#ichthyology #marine-biology #fisheries-science #population-estimation

## Executive Summary

This review by [[G. A. F. Seber]] (University of Auckland) surveys developments in estimating animal abundance and related parameters, such as survival rates, published since the author's 1982 book. The paper is general to animal populations rather than fish-specific. It covers density estimation from sampling units (quadrats, strips, lines, points), aerial censusing, [[Capture-Recapture Methods]] for closed and open populations, [[Band Recovery]] models, and [[Catch-Effort Models]] in fisheries. The author argues that computing advances have made robustness checks possible and that several older methods are now of historical interest only. The paper concludes that many problems remain open, including heterogeneity in capture, edge effects, and identifiability in age-specific survival models.

## Background & Description

- **Scope:** Literature review covering roughly the five years after the author's book manuscript was submitted in 1979, with terminology following that book.
- **Prior reviews cited:** Youngs and Robson (1978), Begon (1979), Cormack (1979), Ralph and Scott (1981), Blower, Cook, and Bishop (1981), White et al. (1982), Seber (1982), and North and Morgan (1985).
- **Technological advances identified:**
  1. Very small radio transmitters (Amlaner and MacDonald, 1980). Thomas (1980) describes a 1-g transmitter, though transmitter failure remains a problem.
  2. Remote sensing, such as thermography, which detects animals by the heat they radiate.
  3. Underwater acoustics, including [[Hydroacoustic Surveys]] for fish counts and biomass.
  4. Widespread computer availability, enabling simulation, Monte Carlo inference, the jackknife, and the bootstrap.
- **Methodological theme:** Standard estimators are sensitive to departures from assumptions, which has renewed interest in robust nonparametric procedures.
- **Definition used:** A closed population is one in which migration, mortality, and recruitment are negligible during the study period.

## Ecological & Environmental Context

**Sampling design and spatial pattern**
- Populations are usually patchy, so stratified or systematic sampling with a random start is preferred. Systematic designs give more even coverage.
- Marine survey data often contain many zeros, and treating zeros separately can yield more efficient abundance estimators (Pennington, 1983). This is relevant to plankton and trawl surveys.
- For very patchy populations over large areas, such as plankton or krill, [[Adaptive Sampling]] concentrates effort in high-density areas (Thompson, 1982).

**Aggregation models**
- The [[Negative Binomial Distribution]] models clustered populations, including trawl catches, mosquitoes, and pellet groups.
- [[Taylor's Power Law]] (variance = a·mean^b, with b usually between 1 and 2) is described as remarkably stable for a given species. The author notes that k in the negative binomial lacks a clear ecological meaning.

**Aerial and visual surveys**
- Strip transects are preferred over quadrats for aerial work. Visibility correction is the central problem, and [[Petersen Method]] applied to two independent observers is one approach.
- Marine surveys (for example, walrus and seabird counts) present their own difficulties.

**Line transects and distance methods**
- [[Line Transect Sampling]] is the main method for mobile animals such as birds. Perpendicular distance is preferred to radial distance (Hayes and Buckland, 1983).
- The [[Fourier Series Estimator]] (Burnham et al., 1980) is more robust than many parametric alternatives. Buckland (1982a) reported that analytic confidence intervals were too narrow, with coverage at least 80% for nominal 95% intervals.
- Line-intercept methods have been extended to estimate fish density using hydroacoustics (Kimura and Lemberg, 1981).

**Trapping and home range**
- Grid trapping requires correction for the [[Edge Effect]], often by adding a strip of half the home-range width (Dice, 1938). Home range itself is hard to measure and varies by species, sex, and density.
- [[Anderson Web Trapping Design]] (Anderson et al., 1983) avoids the edge-effect question entirely.

**Fisheries**
- [[Catch-Effort Models]] for closed and open populations are discussed, along with the problems of combining data across gear types and locations.
- Ratio-based catch-effort models were found unreliable for parameter estimation in freshwater fish sampling (Robson and Spangler, 1978).
- Tag loss and double tagging affect [[Petersen Method]] estimates in fish studies (Seber and Felton, 1981; Wetherall, 1982).

## Key Findings

1. **Negative binomial limitations:** Its k parameter lacks clear ecological meaning and it does not include a regular spatial distribution as a special case. Taylor's power law is preferred as a more universal descriptor.
2. **Aerial census correction:** The bounded-counts method is inappropriate unless the average proportion seen exceeds 0.8 (Routledge, 1982), which excludes many surveys.
3. **Line transect model choice:** Models based on perpendicular distance outperform those based on radial distance. Nonparametric and Fourier approaches are more robust than standard parametric models.
4. **Closed-population models:** Among the Otis et al. (1978) models, Mh and Mth are considered the most useful because heterogeneity and trap response are common. The Mh jackknife estimator and the generalised removal estimator for Mth are favoured. Earlier truncated binomial, geometric, and Skellam models are judged inappropriate and should be abandoned, since they give widely different estimates and goodness-of-fit tests fail to discriminate.
5. **Open-population (Jolly-Seber) model:** It is widely used for populations with death, emigration, and recruitment. Heterogeneity causes negative bias in population size, and trap-happy response causes negative bias in population estimates but not in survival estimates. A proposed sampling design (Pollock, 1982) exploits the robustness of survival estimates.
6. **Band-recovery models:** Model I (constant survival and recovery within a year) is fairly robust to stratified recovery rates. Age-specific survival models suffer identifiability problems, so they should not be used unless an independent estimate of one parameter is available, such as from radiotelemetry.
7. **Composite dynamic method:** The author strongly recommends against using life-table methods of this type (Anderson, Burnham, and White, 1985).
8. **Radio telemetry outlook:** As cheap, reliable transmitters become available, reporting-rate and identifiability problems should largely disappear, with reporting rate becoming 1.
9. **Survival from periodic visits:** The Mayfield estimator is the maximum likelihood solution for regular intervals. For irregular visits, Bart and Robson (1982) give a maximum likelihood solution, though questions of design and visit frequency remain.
10. **Open research needs:** The author identifies the following as unresolved: heterogeneity of capture, flexible open-population models, the edge effect in grid trapping, identifiability of age-specific survival, and adaptive sampling for patchy populations.

---

*Note on source:* The document is a journal review article, not a proposal or budget. It includes a French-language abstract (Résumé) and an extensive reference list, which are summarised rather than reproduced here.