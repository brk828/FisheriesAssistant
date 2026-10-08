---
species: ["Lepomis macrochirus", "Lepomis microlophus"]
common_names: ["Bluegill", "Redear Sunfish"]
family: Centrarchidae
habitat: "Freshwater lake (littoral/open water zones)"
ocean_basin: "N/A (Freshwater - Lake Bistineau, Louisiana, USA)"
study_type: "Statistical analysis of sex ratio distribution"
sample_method: "Rotenone collection"
year_collected: 1955
publication_year: 1963
source: "Transactions of the American Fisheries Society, Vol. 92, No. 4"
author: "Victor W. Lambou"
source_id: "12688"
---

# Distribution of Sex Ratios of Bluegill and Redear Sunfish

#ichthyology #freshwater-biology #Centrarchidae #population-statistics

## Executive Summary
This short paper by Victor W. Lambou (1963) statistically examines whether the sex ratios of [[Bluegill]] (*Lepomis macrochirus*) and [[Redear Sunfish]] (*Lepomis microlophus*) collected from [[Lake Bistineau]], Louisiana, conform to a **binomial distribution**—the standard assumption underlying most sex-ratio confidence intervals and chi-square tests. Using variance-ratio tests on data from 13 randomly selected 1-acre rotenone sample sites, the author demonstrates that sex ratios for both species deviate significantly from binomial expectations, exhibiting greater "patchiness" (spatial clustering by sex) than the binomial model predicts. This has direct methodological implications for how ichthyologists calculate confidence limits and significance tests for sex ratio data in wild fish populations.

## Background & Description
This paper is a **statistical/methodological note** and does not report morphological data (e.g., length, weight, coloration) for [[Bluegill]] or [[Redear Sunfish]]. The only biological attribute analyzed is **sex** (male/female) as a binary categorical variable used to compute population proportions (p, q) within sampled areas.

## Ecological & Environmental Context
- **Habitat**: [[Lake Bistineau]], a Louisiana freshwater lake, sampled across 13 randomly selected 1-acre plots.
- **Collection Period**: August–September 1955.
- **Collection Method**: [[Rotenone]] application, a standard ichthyocide technique for exhaustive fish sampling within defined areas.
- **Spatial Structure**: The core ecological finding is that both species show **non-random, spatially clustered sex distribution**—i.e., individuals of a given sex tend to co-occur in certain areas of the lake more than random mixing would predict. This suggests behavioral **sexual segregation**, potentially related to spawning site selection, schooling by sex, or habitat partitioning (e.g., nesting males vs. non-nesting females in centrarchid breeding biology).
- **Alternative Explanations Considered**: The author notes that sex-selective bias in the rotenone sampling technique could theoretically produce a similar pattern, but considers this unlikely given the data.

## Key Findings

### Statistical Method
Two variance estimators were compared:
1. **Binomial variance** (Eq. 1): `v(p) = pq/n`
2. **Cluster-sampling variance** (Eq. 3, per [[Cochran 1953]]): accounts for non-constant sample sizes (nᵢ) across the 13 sampling sites.

A **variance-ratio (chi-square) test** (per [[Cochran 1954]]) was used to test deviation from binomial expectation, with 12 degrees of freedom (13 samples − 1).

### Results Table

| Species | χ² statistic | Significance | Binomial variance v(p) | Cluster variance v'(p) |
|---|---|---|---|---|
| [[Bluegill]] | 32.584 | p < 0.010 | 0.000674 | 0.00219 |
| [[Redear Sunfish]] | 31.786 | p < 0.010 | 0.00101 | 0.00394 |

### Interpretation
- Both species show χ² values significant at **p < 0.010** (two-tailed, 12 df), rejecting the null hypothesis that sex ratios follow a binomial distribution.
- In both species, the **cluster-sampling variance estimate exceeds the binomial variance estimate by roughly 3–4×**, confirming that binomial formulas substantially **underestimate the true variance** of sex ratio proportions in these populations.
- This indicates **patchy, non-random spatial segregation by sex** in both [[Bluegill]] and [[Redear Sunfish]] populations within Lake Bistineau.

### Methodological Implication
Researchers computing confidence intervals or conducting significance tests on fish sex ratio data collected via **cluster sampling** (i.e., grouped area samples rather than individually randomized draws) should use cluster-appropriate variance formulas (e.g., [[Cochran's Cluster Sampling Variance]]) rather than the simple binomial `pq/n` formula, to avoid underestimating variability and inflating false-positive significance results.

### Related Concepts
- [[Sex Ratio Segregation in Fish]]
- [[Cluster Sampling in Fisheries Biology]]
- [[Rotenone Sampling Technique]]
- [[Centrarchidae]]
- [[Lake Bistineau Fish Distribution]] (Lambou, 1962)