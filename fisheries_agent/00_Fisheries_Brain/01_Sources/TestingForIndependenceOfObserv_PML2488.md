---
species: "Sigmodon hispidus"
common_name: "Cotton Rat"
family: "Cricetidae"
habitat: "Old pasture with brush piles (terrestrial, small mammal home range)"
ocean_basin: "N/A"
location: "John H. Nelson Environmental Studies Area, 14 km northeast of Lawrence, Kansas, USA"
tags: [home-range, radiotelemetry, autocorrelation, spatial-analysis, mammalogy, statistics]
title: "Testing for independence of observations in animal movements"
source_id: "PML2488"
marsh_id: "PML2488"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. K. Swihart, N. A. Slade (1985). Testing for independence of observations in animal movements. Ecology. Marsh Library ID: PML2488."
source_file: "Swihart R.K. et al. 1985. Testing for independence of observations in animal movements.pdf"
text_extraction: "text"
---
# Testing for Independence of Observations in Animal Movements

#ichthyology #marine-biology #cricetidae

*(Note: the source concerns a terrestrial rodent and statistical methods for animal movement data; the fish and marine tags above are the required header line and do not describe the document's subject. The specific taxon tag is #cricetidae.)*

## Executive Summary

Swihart and Slade (1985, *Ecology* 66(4)) present a bivariate test of the independence of successive locational observations in animal movement studies, based on Schoener's (1981) ratio of mean squared distance between successive observations to mean squared distance from the [[Center of Activity]]. Monte Carlo simulations established critical values for the ratio across sample sizes and home-range eccentricities. The test was demonstrated on a radio-tracked female [[Cotton Rat]] (*Sigmodon hispidus*). The authors also introduce a "time to independence" (ΔT_I) metric to identify the minimum sampling interval at which autocorrelation becomes negligible.

## Background & Description

Independence between successive observations is an implicit assumption in most home-range analyses, yet it is rarely tested. When observations are too frequent, as with [[Radiotelemetry]] or direct observation, successive locations become positively correlated. This inflates the underestimation of sample variance and home-range size, since the covariance between successive observations is omitted.

Earlier approaches include the [[Von Neumann Ratio]] (univariate, applicable to autocorrelated error terms via the [[Durbin-Watson Statistic]]). Because animal movements require bivariate or trivariate distributions, Schoener's (1981) bivariate extension was adopted. The authors note that Schoener's expectation of 2 for the ratio has not been formally proven, but simulations support it.

## Ecological & Environmental Context

- **Study animal:** A 125 g resident adult female cotton rat, fitted with a 3.2 g transmitter on 15 December 1982 and tracked from 17 to 22 December 1982 in an old pasture.
- **Tracking method:** Triangulation with a hand-held three-element Yagi antenna, 1200–2000 h daily, at 5-min intervals (10-min intervals were also common).
- **Behavioral observations:** The radio collar had no apparent adverse effect; body mass was 127 g at study end. Most locations concentrated at a 15 m² brush pile, presumed to be the nesting site.
- **Movement distribution:** Multimodal and asymmetric, not matching the bivariate uniform or normal distributions used in simulations.
- **Home range:** Estimated eccentricity of 1.61.

## Key Findings

1. **Monte Carlo critical values:** For sample sizes of 10 or more, the empirical distribution of Schoener's ratio closely approximated a normal distribution with mean 2, regardless of kurtosis or eccentricity. Regression equations (R² = 0.995 uniform, 0.997 normal) allow critical values to be calculated from the standard deviation.
2. **Robustness to sampling distribution:** For successive observations, the distribution is not materially affected by the underlying distribution of X and Y. Randomization with the observed rat data and a funnel-shaped beta distribution gave results statistically indistinguishable from the normal and uniform cases.
3. **Disjunct pairs:** When each observation is used in only one pair (gaps in data), the distribution differs from the successive-pair case, with different regression coefficients. Critical values from disjunct tables (Table 3) and successive tables (Table 1) serve as bounds on significance.
4. **Cotton rat test:** Using all 302 successive pairs, the ratio was 0.499 against a critical value of 1.935 (α = .25, one-tailed), so successive observations were judged positively correlated (dependent).
5. **Time to independence (ΔT_I):** Autocorrelation was negligible at a time interval of **270 min** (α = .25); α = .05 gave 260 min. ΔT_I was insensitive to using only observations separated by at least 30 min.
6. **Diel cycle:** The ratio declined sharply beyond k > 19 h. At k = 24 h, 35% of point pairs were under 10 m apart, and 85% of these were outside the brush pile, suggesting a daily cycle. The predicted ratio at 24 h was 1.43.
7. **Decision rule for irregular sampling:** If the observed ratio exceeds the upper bound, do not reject H₀ of independence. If it falls below the lower bound, reject H₀ in favor of dependence. Otherwise the test is indeterminate. The example for m = 8 gave bounds of 1.689 and 1.664 at α = .25.
8. **Broader applications:** The authors propose ΔT_I for testing primate territoriality (predicting ΔT_I < 24 h for territorial primates) and for testing the [[Lindstedt and Calder Hypothesis]] that ΔT_I scales with body mass to the power (D − 0.75), where D is the home-range–body-mass scaling exponent.
9. **Movement models:** Non-independence may also arise from home-range shifts, traplining behavior (as in bumblebees and euglossine bees), or temporal cycles in movement.

The authors emphasize that the test does not discourage frequent monitoring; it provides a means to confront the independence assumption directly.