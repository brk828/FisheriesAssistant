---
species: N/A
common_name: N/A
family: N/A
habitat: Freshwater streams and lakes (electrofishing field data)
ocean_basin: N/A
location: N/A
tags: [ichthyology, marine-biology, fish-population-dynamics, secondary-production, software]
title: "Modular microcomputer software to estimate fish population parameters, production rates and associated variance"
source_id: "PML1303"
marsh_id: "PML1303"
library: "Marsh Library"
permission: "not public domain"
source_citation: "T. J. Kwak (1992). Modular microcomputer software to estimate fish population parameters, production rates and associated variance. Ecology of Freshwater Fish 1(1): 73-75. Marsh Library ID: PML1303."
source_file: "Kwak T.J. 1991. pop-pro modular stats software.pdf"
text_extraction: "mixed"
---
# Modular Microcomputer Software to Estimate Fish Population Parameters, Production Rates and Associated Variance

#ichthyology #marine-biology #fish-population-dynamics

## Executive Summary

This short communication by T. J. Kwak (Department of Fisheries and Wildlife, University of Minnesota, St Paul) describes Pop/Pro Modular Statistical Software, a set of portable C programs for estimating [[Fish Population Abundance]], [[Biomass]], [[Fish Production]] and the sampling variance of these statistics. The software runs on Apple Macintosh and IBM/IBM-compatible computers and was developed for [[Electrofishing]] field data, though the author notes it may apply to other taxa. The paper is primarily a methods and software description, published in *Ecology of Freshwater Fish* (1992, vol. 1, pp. 73–75). The author explicitly disclaims guarantees of accuracy and states that variance estimates capture sampling error only.

## Background & Description

- **Motivation:** Production is described (citing [[Le Cren]] 1969) as "the best epitome of the population dynamics and environmental performance" of a population. Calculations are complex and variance estimation is laborious, so many biologists rarely estimate production.
- **Existing tools:** Earlier programs by Garman & Waters (1983), Newman & Martin (1983) and Railsback, Holcomb & Ryon (1989) were judged restrictive in method, portability or flexibility.
- **Software scope:** Written in English, developed in C, totalling 18,870 lines of source code. Requires only a word processor or spreadsheet to create input files.
- **Availability:** Free on a double-sided 90 mm disk, sent by the author (format specified as Macintosh or IBM).
- **Modules:** Eight modules are described across two groups:
  - **Population estimation (Pop):** [[Capture-Recapture Method]] (CAPRECAP) and [[Removal Method]] (REMOVAL), in standard and No-Age versions.
  - **Production estimation (Pro):** [[Instantaneous Growth Rate Method]] (G-PRO) and [[Increment Summation Method]] (IS-PRO), with IS-N variants for user-entered intervals (e.g., southern-hemisphere populations).

## Ecological & Environmental Context

- Production studies serve four ecological goals listed by Downing (1984): (1) elucidating energy or material transfer within ecosystems; (2) sound management of aquatic resources; (3) detecting effects of pollution; (4) forming theories of biological productivity.
- Electrofishing has a known size bias, so population estimates are stratified by size group to mitigate it.
- Negative growth intervals are treated as zero production, and a year class present at only one of two sampling dates (e.g., through migration or mortality) is assigned zero mean standing stock. These choices make the outputs conservative minimum estimates.
- Recruited age-0 fish receive production equal to their first-sample biomass and variance (Waters 1983).

## Key Findings

**Population estimation**
- Single-census mark-recapture uses a modified Petersen estimate, N = (M+1)(C+1)/(R+1), with variance V(N) = [N²(C−R)] / [(C+1)(R+2)], where M = marked fish, C = total captured in the second sample, and R = recaptures (Ricker 1975).
- Removal estimates use maximum-likelihood formulas that depend on the number of passes: two removals (closed-form solution), three removals (closed-form with catchability p and variance expressions), and four or more removals (iterative solution for q, followed by N). The same fishing effort must be used in each pass.
- Outputs include abundance, biomass, mean individual weight and variance for the total population and each age class.

**Production estimation**
- At least two population estimates are needed. Production is computed per interval as P = G·B, where G is the instantaneous growth rate and B the mean interval biomass; the production-to-biomass ratio P/B is also reported.
- Variance of G uses the delta method (Taylor expansion of the log of the mean), described as simpler than the jackknife estimator of Newman & Martin (1983).
- IS-PRO uses P = N·Δw, with variance formulas for N, Δw and P given by Newman & Martin (1983).
- Interval-weighted means are computed for abundance and biomass; totals are computed for other parameters.
- Approximate 95% confidence intervals (±2 SE) are reported for total production, mean abundance and biomass, P/B, and total instantaneous growth and mortality rates.

**Practical guidance**
- Units can be converted with multipliers (one for area, one for biomass), ideally applied to final results to preserve precision; variance must be multiplied by the constant squared when a statistic is scaled.
- If an interval spans January 1, production is estimated per year class using a birthday convention (January 1 for northern hemisphere, July 1 for southern).
- Users are responsible for input data quality and should verify a subset of results, as the software has undergone only limited testing.
- Variance estimates reflect sampling error only and do not capture process or systematic error (Walters 1986).

**Software limitations**
- Pop/Pro has undergone limited testing; the author does not guarantee accuracy or application of results.
- The modules include traps for anomalous data, but the user remains responsible for data quality.