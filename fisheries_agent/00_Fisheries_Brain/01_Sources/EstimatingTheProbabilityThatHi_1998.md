---
species: "Atlantic sturgeon (Acipenser oxyrinchus), Alabama sturgeon (Scaphirhynchus suttkusi), Shortnose sturgeon (Acipenser brevirostrum)"
family: "Acipenseridae"
habitat: "Estuarine rivers, coastal river systems (James River VA, Nanticoke River MD, Mobile River Basin AL)"
ocean_basin: "Northwest Atlantic Ocean / Gulf of Mexico drainage"
paper_title: "Estimating the Probability That Historical Populations of Fish Species Are Extirpated"
authors: "Christopher S. Grogan, John Boreman"
journal: "North American Journal of Fisheries Management 18:522-529, 1998"
tags: [ichthyology, marine-biology, acipenseridae]
source_id: "17800"
---

#ichthyology #marine-biology #acipenseridae

## Executive Summary

This paper is a **methodological/statistical conservation biology paper**, not a morphological species account. It addresses the problem of how fishery managers can objectively estimate the probability that a rare fish species has been **extirpated** from a system using only sparse, incidental observation data (museum records, bycatch, survey data), rather than expensive, logistically difficult directed surveys. The authors adapt two indirect statistical methods — originally developed for mammals by [[Solow 1993a]] and [[Burgman Et Al 1995]] — to fish population data, using [[Atlantic Sturgeon]] and [[Alabama Sturgeon]] as case studies. They conclude with a formal 8-step protocol for fisheries managers to follow when assessing extirpation risk.

## Background & Description

Not applicable in the traditional sense — this paper does not describe morphology in detail. However, taxonomic identification issues are discussed as a key confounding factor:

- **[[Atlantic Sturgeon]]** (*Acipenser oxyrinchus*) and **[[Shortnose Sturgeon]]** (*Acipenser brevirostrum*) are noted to be **externally similar in appearance**, historically causing inadequate species-level separation in landings records along the Atlantic coast (New Brunswick to Florida).
- Similarly, **[[Blueback Herring]]** (*Alosa aestivalis*) and **[[Alewife]]** (*Alosa pseudoharengus*) were historically pooled under the collective term "river herring" in landings data, illustrating a recurring taxonomic conflation problem when using historical fisheries records for extirpation analysis.
- Size/age data available for Atlantic sturgeon captures (VIMS trawl survey, James River, VA, 1964–1994): total lengths ranged from 85–997 mm, with probable ages of 0–13 years.

## Ecological & Environmental Context

- **[[Atlantic Sturgeon]]**: Anadromous species inhabiting estuarine/coastal river systems along the Atlantic seaboard; sampled incidentally in the [[James River]] (Virginia) via VIMS trawl surveys (1964–1994). Juvenile stages may compete with shortnose sturgeon for food or space.
- **[[Shortnose Sturgeon]]**: Endangered anadromous species overlapping range with Atlantic sturgeon; suspected extirpated from the [[Nanticoke River]] (a Chesapeake Bay tributary) and mid-Bay Maryland/Virginia waters based on approximately 50 years without a confirmed young-of-year, yearling, or ripe adult observation.
- **[[Alabama Sturgeon]]** (*Scaphirhynchus suttkusi*): Freshwater river species from the Mobile River Basin, Alabama; extremely rare, proposed for endangered listing in 1993, later withdrawn after failed directed sampling efforts (Federal Register 1993, 1994). Museum/confirmed records span 1953–1995.
- Both sturgeon case studies exemplify the broader ecological niche challenge of the paper: **rare, cryptic, or infrequently sampled species** for which population status must be inferred from opportunistic/incidental data rather than systematic surveys.
- Family-wide context: Most species within [[Acipenseridae]] worldwide are considered threatened, endangered, or extirpated across part of their range (Birstein 1993).

## Key Findings

### Statistical Methods for Inferring Extirpation
- **Equation (1)** (Solow 1993a): 
  p = 1 − (t_c/T)^n
  where *n* = number of time intervals with observations, *t_c* = last interval with an observation, *T* = total intervals in series. Assumes a **stationary Poisson process** — constant probability of incidental detection over time; requires random, independent, non-deliberate observations.
- **Equation (2)** (Burgman et al. 1995):
  p = 1 − (t_c/T)^k
  where *k* = total number of individual observations (not just intervals). More sensitive to observation frequency prior to last sighting; generally yields **higher** extirpation probabilities than Equation (1) when multiple observations occur per interval.
- Equation (1) is a special case of Equation (2) when only one individual is recorded per positive interval.
- Both methods are **insensitive to the distribution pattern** of observations across a time series (i.e., cannot distinguish a constantly low observation rate from a declining population trend). For declining populations, [[Solow 1993b]] method is recommended instead.
- Sensitivity analysis (Table 1): p approaches 1.0 (≈100% probability of extirpation) once *k* > 50 observations **and** the time since last observation ≥ 10% of the total series length.

### Case Study: Atlantic Sturgeon (James River, VA, 1964–1994)
- Survey duration: 31 years (*T* = 31); species observed in 9 of those years (*n* = 9); total individuals captured *k* = 25; last capture in year 25 of the series (*t_c* = 25).
- **Equation (1) estimate**: p = 0.856
- **Equation (2) estimate**: p = 0.995 (higher due to multiple captures clustered 1978–1981)
- Restricting to age ≥1 fish only: p = 0.983 (Eq. 2)
- Restricting to age-0 fish only: p = 0.994 (Eq. 2)
- Demonstrates importance of **not mixing early life-stage and adult data** in extirpation calculations, as it can bias results.
- Sensitivity table (Table 3) shows p increasing sharply with *k*, from 0.194 (k=1) to >0.999 (k=40), holding t_c/T constant at 25/31.

### Case Study: Alabama Sturgeon (Mobile River Basin, AL, 1953–1995)
- Estimated probability of extirpation by 1993 (excluding directed-survey years 1984–1985 and the 1953 starting record):
  - **Equation (1)**: p = 0.96
  - **Equation (2)**: p ≈ 1.00
- If directed-survey collections (1984, 1985) had been included:
  - **Equation (1)**: p = 0.86
  - **Equation (2)**: p ≈ 1.00
- Species was later collected again in 1993 and 1995 after a 7-year gap — **not statistically unusual**, given the historical average inter-sighting interval of 6.2 years. This illustrates the danger of prematurely declaring extirpation.
- Mayden and Kuhajda (1996) documented **7 fish species** previously presumed extirpated/extinct that were rediscovered after 23–110 years — a strong cautionary data point for conservative interpretation of extirpation probabilities.

### Key Methodological Recommendations
1. Only use **opportunistic, random, independent** observation records — never deliberate/directed survey data (violates Poisson assumption).
2. Do **not combine** early life-stage (egg/larval/juvenile) data with adult data in the same time series — early stages are more abundant/variable and bias results.
3. Prioritize data collected in the **species' preferred habitat** (e.g., spawning grounds, migration corridors) matching the ecological question being asked.
4. Avoid combining time series affected by changes in gear selectivity or **taxonomically ambiguous** historical records (e.g., Atlantic vs. shortnose sturgeon; blueback herring vs. alewife).
5. Use **ancillary information** (lifespan, distribution patterns, migratory/habitat changes, contaminant levels, habitat loss, gear changes, anecdotal reports) to contextualize statistical estimates.
6. Suggested **decision thresholds**: p ≥ 0.75 → issue a warning / trigger directed surveys; p ≥ 0.95 → support declaration of likely extirpation.
7. Indirect statistical methods should be treated as a **first-warning screening tool**, not a final determination — final extirpation status should combine indirect methods, [[Direct Survey Methods]] (see [[Reed 1996]]), and ancillary evidence.
8. Consider defining a **"functionally extirpated"** population category — i.e., a population with no potential for further growth (e.g., single-sex remnant), distinct from complete extirpation.

### Broader Significance
- Provides fisheries managers a **statistically grounded, low-cost, first-pass tool** for triaging conservation concern before committing to expensive directed surveys.
- Directly informed a real regulatory case: NMFS/USFWS Section 7 consultation on releasing approximately 7,000 hatchery-reared Atlantic sturgeon into the Nanticoke River, weighed against potential impacts on possibly-extirpated endangered shortnose sturgeon.
- Establishes a formal 8-step protocol for standardizing future extirpation assessments under the [[Endangered Species Act]].