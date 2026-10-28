---
species: "Chrysophrys auratus (snapper); Amphidesma ventricosum (toheroa)"
family: "Sparidae (snapper); Mesodesmatidae (toheroa, bivalve)"
habitat: "Coastal trawl grounds; sandy beach (intertidal)"
ocean_basin: "South Pacific (New Zealand waters)"
methodology: "Probability graph paper analysis of size-frequency distributions"
source_id: "16044"
---

#ichthyology #marine-biology #Sparidae #biometrics #population-dynamics

## Executive Summary

This methodological paper by R.M. Cassie (1954) describes and extends techniques for dissecting polymodal (multi-peaked) size-frequency distributions into their component normal distributions using probability graph paper. Building on [[Harding 1949]] and the author's own 1950 work, the method exploits the fact that cumulative percentages of a normally distributed variable plot as a straight line on probability paper — a transformation analogous to the "probit" used in bioassay. The technique allows researchers to graphically extract age-classes or subpopulations from a mixed sample by sequentially fitting the "exposed flank" of each component distribution, once its neighbors have been subtracted out. Four worked examples are provided, all using aquatic organisms: (1) resolving four year-classes from a trawl catch of 256 [[Snapper]] (*Chrysophrys auratus*); (2) cross-validating length-frequency age estimates against scale-reading data, revealing a probable false-ring artifact in age-2 fish; (3) identifying a bimodal-variance (kurtotic) distribution in cod-end meshed snapper attributable to two distinct capture mechanisms; and (4) correcting a bimodal toheroa (*Amphidesma ventricosum*) shell-length distribution for sampling truncation at both size extremes.

## Background & Description

- **Snapper (*Chrysophrys auratus* Forster)**: Length data measured in inches; catch sample of n=256 individuals taken by trawl (~1.25 in mesh). Four distinct year-classes ("0", "1", "2", "3+") identified via points of inflexion in the cumulative frequency curve at 10%, 66%, 91%, and 98.6%.
  - Year-class 0: mean length 3.22 in., SD 0.27 in., n=10 (25.6 in sample)
  - Year-class 1: mean length 5.33 in., SD 0.62 in., n=56 (143.4)
  - Year-class 2: mean length 7.62 in., SD 0.56 in., n=25 (64.0)
  - Year-class 3+: mean length 9.74 in., SD 0.60 in., n=7.6 (19.4)
  - Goodness of fit: χ² = 10.8, df = 12, P = 0.5

- **Toheroa (*Amphidesma ventricosum* Gray)**: Bivalve mollusc; shell length measured in inches from a juvenile beach sample (n=64, "a few months" old). Bimodal distribution resolved into two spawning cohorts after truncation correction:
  - Second spawning: mean 0.23 in., SD 0.11 in., n≈39 (corrected)
  - First spawning: mean 0.72 in., SD 0.14 in., n≈66 (corrected)
  - Goodness of fit: χ² = 1.45, df = 2, P = 0.5

## Ecological & Environmental Context

- **Snapper population structure**: The sampled catch reflects a mixed-age assemblage captured by [[Trawl Gear Selectivity]]; the smaller "0" year-class shows artificially reduced variance due to **truncation** — the trawl mesh (~1.25 in) failed to retain the smallest individuals, biasing the true mean lower and true SD higher than observed.
- **Capture mechanism duality (Example 3)**: A cod-end sample of 63 snapper displayed positive kurtosis (reversed S-shape on probability paper), attributed to two distinct meshing mechanisms — (a) fish caught tightly behind the gill covers (narrow size range, near-zero escape) versus (b) fish caught loosely by head or body (wider size range, higher escape probability). This has implications for interpreting [[Gill Net Selectivity]] data across different gear types.
- **Toheroa recruitment**: Evidence of two discrete spawning pulses within a single summer season, consistent with known life history of intermittent multi-brood spawning in this species. Sampling bias arose from (1) collector preference for small specimens and (2) practical difficulty detecting the smallest shells (<¼ in), producing truncation at both distribution tails — a common artifact in [[Intertidal Bivalve Sampling]].
- Age determination cross-validation: Scale-reading and length-frequency methods for snapper substantially agreed for year-classes 0 and 3, but diverged for classes 1 and 2, suggesting either (a) false annual rings on ~50% of scales classed as age-2 (most likely explanation per author), or (b) a genuinely bimodal age-2 cohort from a secondary late spawning event or a second snapper population with differing growth rate.

## Key Findings

- **Probability paper linearizes normal cumulative distributions**, enabling visual/graphical separation of overlapping component populations ("exposed flank" method), extending the graphical approach of [[Buchanan-Wollaston And Hodgson 1929]] and avoiding the laborious parabola-fitting of arithmetic dissection methods (cf. [[Pearson 1894]]).
- **Sequential extraction technique**: Each component is fit from its uncontaminated ("exposed") tail first; percentages are rescaled ($\times 100/\text{interval}$) and corrected for contamination from adjacent, already-fitted components using an iterative subtraction formula.
- **Standard deviation can be read directly** from the graph as the distance between the 50% and 15.87%/84.13% levels, or more precisely by measuring to the 99.9967% level and dividing by 3.72.
- **Truncation correction formula** introduced: 
  $$P' = p + p'' - \frac{p \cdot p''}{100}$$
  where $P'$ = corrected cumulative percentage, $p$ = observed percentage, $p''$ = percentage lost to truncation — successfully recovers underlying normal parameters even under ~50% (lower tail) and ~20% (upper tail) truncation in the toheroa example.
- **Diagnostic value for distribution shape**: Deviations from linearity on probability paper directly indicate the type of non-normality — increasing slope left-to-right = positive skew; decreasing slope = negative skew; reversed S-shape = positive kurtosis; S-shape = negative kurtosis.
- **Model parsimony emphasized**: Each additional extracted component costs 3 degrees of freedom in subsequent χ² goodness-of-fit testing, so the simplest adequate solution should be preferred; graphical solutions are not maximum-likelihood optimal but are typically within the sampling error of the parameter estimates, and can serve as a first approximation for iterative arithmetic refinement.
- **Biological validity caveat**: Not every continuous biological variable should be decomposed into normal components — such decomposition is only meaningful when a physical/biological interpretation (e.g., distinct age-groups, sexes, or spawning cohorts) can be assigned to each extracted component. Relevant to broader debates on [[Mixture Model Interpretation]] in population biology.