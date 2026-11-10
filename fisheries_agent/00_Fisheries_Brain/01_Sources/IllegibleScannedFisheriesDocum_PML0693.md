---
species: ["Ovis canadensis", "Callinectes sapidus", "Megaptera novaeangliae", "Rattus rattus", "Phasianus colchicus"]
common_name: ["Bighorn sheep", "Blue crab", "Humpback whale", "Roof rat", "Ring-necked pheasant"]
family: ["Bovidae", "Portunidae", "Balaenopteridae", "Muridae", "Phasianidae"]
habitat: "Mixed: montane and forest terrain, coastal and estuarine waters, farmland, islands and enclosed study grids"
ocean_basin: "North Atlantic Ocean (humpback whales, Gulf of St. Lawrence); N/A for terrestrial taxa"
location: "Trickle Mountain, Colorado; Oregon; Utah; Freetown, Sierra Leone; Rottnest Island, Western Australia; Northern Territory, Australia; southern British Columbia; northern Michigan; Chesapeake-region blue crab fishery (N/A specific)"
tags: ["population-ecology", "mark-recapture", "removal-methods", "wildlife-biology", "abundance-estimation"]
title: "Estimating Abundance: Removal Methods and Resight Methods"
source_id: "PML0693"
marsh_id: "PML0693"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Unknown author (n.d.). Estimating Abundance: Removal Methods and Resight Methods. Marsh Library ID: PML0693."
source_file: "Estimating abundance removal methods and resight methods.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Estimating Abundance: Removal Methods and Resight Methods

#population-ecology #wildlife-biology #mark-recapture

## Executive Summary

This chapter of a population-ecology text explains how to estimate abundance and density when animals are captured once (removal methods) or identified by sightings without recapture (resight methods). It covers change-in-ratio estimators, Eberhardt's index-removal method, catch-effort (Leslie and Ricker) models, mark-resight estimators (the [[Joint Hypergeometric Estimator]] and the [[Bowden Estimator]]), computer-intensive capture-history models ([[Program CAPTURE]]), enumeration methods, and density-estimation corrections for edge effects. Worked examples use pheasants, feral horses, blue crabs, bighorn sheep, humpback whales, and house mice. The main message is that every estimator rests on explicit assumptions (closure, equal catchability, known removals), and that enumeration is a biased last resort.

## Background & Description

The chapter has three parts:

- **Exploited-population techniques (Section 3.1).** These were developed in the 1940s so managers could estimate populations under harvest. They include the [[Change-in-Ratio Method]], [[Eberhardt Index-Removal Method]], and [[Catch-Effort Method]].
- **Resight methods (Section 3.2).** These are newer, based on marking animals so they can be identified at a distance. They were developed for [[Radio-Collared Animals]] but work with any mark visible to a distant observer.
- **Computer-intensive models (Section 3.3)** and **enumeration and density methods (Sections 3.4 and 3.5)**, which cover [[Program CAPTURE]], the [[Minimum Number Alive]] method, and corrections for the effective trapping area.

The change-in-ratio approach traces to Kelker (1940). Its generalized form (Paulik and Robson 1969) requires two types of organisms (x-types and y-types) and a differential change in their numbers during observation. The chapter's formula is:

N₁ = (R₂ − p₂R) / (p₁ − p₂)

where R = R₁ + R₂ is the net removal, p₁ and p₂ are the proportions of x-types before and after, and R₁, R₂ are the net changes for each type.

## Ecological & Environmental Context

Most methods here assume a **closed population** during sampling. Several ecological processes violate this and bias estimates:

- **Edge effects.** Home ranges that extend beyond the trapping grid make the effective area larger than the physical area, so density is overestimated when the population is divided by the trapped area. The chapter shows this with a [[Boundary Strip Method]] and [[Nested Grids Method]].
- **Variable catchability.** Heterogeneity (some animals are "trap-happy" or "trap-shy"), time effects (weather), and behavioral responses to capture all change capture probability. These sources define the [[Capture Model Heterogeneity]] problem addressed by [[Otis et al. 1978]] models.
- **Immigration and emigration.** Attractive traps, long removal periods, and animals that move on and off the study area all break closure.
- **Negative bias in enumeration.** Counts of marked and seen animals are always at or below the true population size, and the bias is severe when catchability is low.

The chapter also notes that some methods suit endangered species, where capture may cause harm, but enumeration may then be the only feasible option.

## Key Findings

**Change-in-ratio (Section 3.1.1)**
- **Worked example (pheasants, Paulik and Robson 1969):** Pre-hunt sample had 800 of 1,400 adults female (p₁ = 0.571428). Post-hunt sample had 1,800 of 2,000 female (p₂ = 0.900000). The kill was 8,000 males and 500 females. The estimate was N₁ = 21,761 pheasants at time 1 and N₂ = 13,261 at time 2.
- **Confidence intervals:** With large samples (about 500 or more per sample), the 95% interval was 19,964 to 23,558. With small samples (fewer than 100–200), the chapter uses the reciprocal method, which gives asymmetric, wider limits.
- **Planning rules (Figures 3.1 and 3.2):** The expected change in proportion (Δp) is the critical variable. The exploitation rate has minor influence, and Δp below 0.05 makes the method impractical. For ±25% accuracy with deer and Δp ≈ 0.30, about 200–250 animals per sample are needed; ±10% accuracy requires 1,050–1,400 per sample.
- **Unequal catchability:** [[Pollock et al. 1985]] proposed a two-stage removal design (x-types removed first, then y-types). This is robust to unequal catchability but requires more work.

**Eberhardt's index-removal method (Section 3.1.2)**
- Uses before-and-after index counts plus the known removal R. The chapter's equation is N̂₁ = x₁R / (x₁ − x₂).
- **Feral horse example, Oregon:** 301 counted before removal, 76 after, and 357 removed. N̂ = 477.6 horses, with a 95% interval of 437 to 518 (±8.5%).
- **Precision (Table 3.1):** Coefficients of variation are low only when more than about 40% of the population is seen and more than about 20% is removed.

**Catch-effort methods (Section 3.1.3)**
- Leslie regression and Ricker semilog models extrapolate the decline in catch-per-unit-effort to estimate initial population size.
- **Blue crab example (Fischler 1965, Table 3.2):** The Leslie estimate for male blue crabs was N̂ ≈ 330,268 pounds, with catchability estimated at 0.0005614. The chapter reports the estimate in pounds, as given in the source.
- The Ricker plot for these data was curved, so the Ricker model was not supported. Plotting both models is recommended as an assumption check.
- Braaten (1969) found the DeLury model biased low, and Schnute (1983) addressed variable catchability.

**Resight methods (Section 3.2)**
- The [[Joint Hypergeometric Estimator]] (JHE) maximizes a likelihood over population size N. Its [[Bighorn Sheep]] example (Neal et al. 1993, Trickle Mountain, Colorado, January–February 1989) gave N̂ = 127, with a 95% interval of 112 to 146.
- The [[Bowden Estimator]] uses individual resighting frequencies, with mean frequency f̄ = 3.320 and VAR(f) = 4.8576. It gave N̂ = 126.52 with a wider upper limit of 161. The wider interval reflects the weaker assumption of unequal sightability.
- Both estimators are implemented in NOREMARK (White 1996) and the MARK-RECAPTURE program group.

**Computer-intensive models (Section 3.3)**
- [[Program CAPTURE]] tests eight models, from the null model (M₀) through time (Mₜ), heterogeneity (M_h), behavior (M_b), and combinations, with chi-squared tests for choosing among them. The full model (Mₜₕb) was unsolved and cannot be used.
- Capture histories require at least three, and typically five, sampling periods.
- **Humpback whale example (Palsbøll et al. 1997, Gulf of St. Lawrence, North Atlantic):** 65 genetically distinct individuals were identified from 86 sightings over five sampling periods. The null-model maximum-likelihood estimate was N̂ = 121, with a 90% interval of 121 ± 32.
- **Mark-recapture caution:** For a hare example (Box 2.1 data), the null-model estimate of 2,806 hares was 18% above the Petersen estimate. The null model tends to overestimate when there are fewer than five sampling occasions, so Petersen is preferred for two periods.

**Enumeration methods (Section 3.4)**
- The Minimum Number Alive (MNA) method adds to the number caught the animals inferred to be present between captures.
- It has a negative bias, and [[Jolly and Dickson 1983]] showed the estimate can never exceed the true size. [[Pollock et al. 1990]] found Jolly-Seber estimates less biased than MNA even under heterogeneous capture.
- Enumeration should be a last resort, for example for endangered species where capture harms animals.

**Density estimation (Section 3.5)**
- **Boundary strip:** Adds a strip of about half the average movement radius around the grid. [[Bondrup-Nielsen 1983]] used home-range size instead and recommended a grid at least 16 times the average home range.
- **House mouse example (grid 0.8 ha, Petersen estimate 127 mice, home range 0.34 ha):** Grid-to-home-range ratio A = 2.35, expected overestimate 2.73. Biased density was 159 mice per ha, and corrected density was about 58 mice per ha.
- **Nested grids:** Requires at least four nested grids (for example 15 × 15 traps). Results are sensitive to assumptions, and simulations showed positive bias when the strip width was underestimated (Wilson and Anderson 1985). Richardson's ground squirrel data gave a best estimate of 45 per ha with a 12.4 m boundary strip.
- **Trapping web:** Radial lines of about 16 traps, with 8–12 traps per home range at the center. About 60 individuals are needed for a reasonably precise density estimate (Anderson et al. 1983).

**Summary of the chapter's guidance**
- Check each model's assumptions (closure, equal catchability, known removals) before using it.
- Plan sample sizes before fieldwork; change-in-ratio precision depends mainly on the expected change in proportions.
- Use Eberhardt's method only when about 40% or more of the population can be counted.
- Treat enumeration as a biased fallback, and prefer closed-population or Jolly-Seber estimators.