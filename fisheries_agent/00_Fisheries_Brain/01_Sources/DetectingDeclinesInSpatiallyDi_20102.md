---
species: N/A
common_name: N/A
family: N/A
habitat: Simulated fragmented landscape (10 x 10 grid of good habitat patches separated by bad-habitat strips)
ocean_basin: N/A
location: N/A
tags:
  - population-ecology
  - metapopulation-ecology
  - conservation-monitoring
  - simulation-modeling
title: "Detecting declines in spatially distributed populations"
source_id: "20102"
minckley_id: "20102"
source_citation: "E. Meir and P. Karieva (n.d.). Detecting declines in spatially distributed populations. . Minckley Library ID: 20102."
source_file: "20102.pdf"
text_extraction: "ocr"
---
# Detecting Declines in Spatially Distributed Populations

#population-ecology #metapopulation-ecology #conservation-monitoring

## Executive Summary

This paper uses an [[Individual-Based Model]] of a [[Metapopulation Theory|metapopulation]] to test how well three trend-detection techniques identify population declines, and how sampling design affects that performance. The authors simulate abrupt and gradual [[Habitat Fragmentation|habitat destruction]], sample populations as counts or as presence/absence data, and vary sampling effort, frequency, and error. The main conclusions are that none of the three techniques is reliable enough for real data, that the [[Dennis Maximum Likelihood Extinction Estimator|maximum likelihood extinction estimator]] performs best, and that [[Presence Absence Data]] detects declines about as well as [[Population Counts]]. The authors also argue for a new model-based technique that works with presence/absence data.

## Background & Description

Monitoring is a major part of [[Conservation Monitoring]], from large schemes such as the [[Breeding Bird Survey]] to site-level plans for rare and endangered species. Monitoring involves trade-offs among:

- Time spent per site versus number of sites, with the extreme case being detailed population estimates at a few sites versus occupancy-only surveys at many sites.
- Sampling frequency.
- Acceptable sampling error.

The authors note that few studies have examined these trade-offs. Earlier work has compared statistical methods mainly on real datasets, where the true trend is usually unknown. The authors therefore favor simulation, in which the underlying process and trend are known. They also highlight [[Thomas 1996]] as a key prior comparison of regression-based trend methods, which tested only declining simulated populations.

The model assumes that fragmentation and habitat loss threaten persistence, and that survival depends on the number of fragments and the dispersal between them. Below a critical number of fragments, a population is expected to go extinct.

## Ecological & Environmental Context

**Simulated landscape and population**

- Landscape: 10 x 10 array of good habitat patches, each 5 x 5 squares, separated by bad-habitat strips 2 squares wide. The world wraps around to avoid edge effects.
- Starting population: 400 individuals placed randomly.
- Movement: random, one square per timestep.
- Mortality: 0.08 per timestep in good habitat, 0.15 in bad habitat, plus 0.2 extra when an individual has a neighbor (density dependence).
- Reproduction: once every 12 timesteps (defined as one "year"), with each individual on good habitat producing 4 offspring.

**Habitat destruction scenarios**

- Abrupt: 30 of 100 good patches destroyed at once. The authors found that destroying 30% of habitat consistently drove the population to extinction.
- Gradual: 5 randomly chosen patches destroyed every 5 years until 80 of 100 were lost.
- Destruction does not kill individuals directly. It causes population decline indirectly through higher death rates and lower birth rates in bad habitat.

**Analysis design**

- 100 model runs per destruction level, with the first 20 years discarded as transient. Runs lasted until extinction, or 290 years for controls.
- Sampling: 5, 10, 20, or 40 patches (5% to 40% of original habitat; 7% to 57% of remaining habitat after 30% destruction). Data-set lengths were 10, 20, 40, or 80 years.
- Each combination was resampled ten times with different patch sets, and results were averaged.
- Sampling error: counts were drawn from normal distributions with variance at 10% or 50% of the actual value. Presence/absence error was one-sided, with no false positives.

**Statistical techniques compared**

- [[Linear Regression]] of log(population + 0.5) on year, significant at p < 0.05. Significance was assessed by [[Bootstrapping]].
- [[Rank Trends Analysis]], using a rank-based statistic D, significant at p < 0.05.
- [[Dennis Maximum Likelihood Extinction Estimator]] (Dennis 1991). A population was classed as declining if extinction probability exceeded 10% and mean time to extinction was under 500 years. The authors acknowledge this method was designed for density-independent populations and counts, not presence/absence data.

## Key Findings

**1. Extinction timing in the simulations**

- Under 30% abrupt destruction, populations went extinct after 600 ± 537 years on average (range 76 to 2897 years).
- Under gradual destruction, mean time to extinction was 137 ± 37 years (range 85 to 244).

**2. Population decline is lagged and gradual**

- After abrupt destruction, populations in undestroyed patches declined only slowly, with a lag of several years before the main decline.
- Mean population per occupied patch stayed roughly constant, with large variance.
- Autocorrelation persisted for about 20 years, reflecting spatial dynamics and density dependence.

**3. Many false declines in control populations**

- Regression and rank-trend methods flagged many false declines in controls, especially with longer data sets. Their significance increased with length even though slopes approached zero.
- The maximum likelihood method gave very few false declines on the longest data sets.
- Real-to-false decline ratios were around 3:1 or worse for most schemes, far from the 95% confidence the authors sought.
- The authors note that the pattern of significant positive and negative trends in their controls resembles that reported for [[Breeding Bird Survey]] data, suggesting caution in interpreting those results.

**4. Presence/absence data performs comparably to counts**

- All three techniques detected declines at least as well with presence/absence data as with counts for 20-year data sets, and the same held for 80-year sets.
- Real-to-false decline ratios were similar for regression and rank trends. The maximum likelihood method had a higher ratio with counts on long data sets, but detected more real declines with presence/absence data.
- The authors suggest presence/absence sampling is much faster, possibly 4 to 5 times faster for insects (unpublished observation), so it allows more sites or species to be sampled.

**5. Sampling frequency**

- Sampling less often (every 2 or 5 years rather than yearly) reduced detected declines, but also reduced false declines. The overall ratio did not fall appreciably and sometimes rose.

**6. Robustness to sampling error**

- With 10% error, results changed little for any technique.
- With 50% error, regression and rank-trend detection dropped. The maximum likelihood method was robust, with one exception (80 years of presence/absence data).
- Presence/absence data was slightly more robust to error than counts, except for maximum likelihood.

**7. Choice of sampled patches matters**

- Table 2 shows that the patch set sampled strongly affects results. For 20 years of control data, an average of 25 ± 6 of 100 random configurations flagged a significant decline. For 30% destruction data, the figure was 78 ± 7 (20 years) and 90 ± 7 (80 years). For 80 years of control data, it was 22 ± 7.

**8. Gradual destruction is harder to detect early**

- With only 20 years of data, regression and maximum likelihood detected gradual-destruction declines less well than abrupt-destruction declines. The authors attribute this to only 20% of habitat being lost at 20 years, versus 30% for abrupt destruction.
- At 80 years, both methods detected gradual declines better, because 80% of habitat had been lost.

**9. Discussion and conclusions**

- The authors conclude that none of the three techniques is trustworthy on real data, but that the maximum likelihood approach of [[Dennis Maximum Likelihood Extinction Estimator|Dennis (1991)]] is the most promising. They argue it is the only theoretically sound option among the three.
- They note its main limitations: it assumes density-independent growth, which real populations often violate, and it was built for counts.
- Regression is criticized because its significance tests assume independent samples, which autocorrelated populations violate. The authors argue that trend analysis should instead use relative changes to parameterize a process model, including [[Density Dependence]] and possibly an [[Allee Effect]].
- A preliminary attempt to fit a [[Ricker Model]] to the data did not work, and the authors leave this unresolved.
- The Conclusion calls for a new model-based technique for presence/absence data, tested against simulated data containing both declining and stable populations.

**Note on the document:** The Discussion contains unfinished drafting passages and author comments, including a passage about the Ricker model and an unfinished closing sentence. These are not conclusions and should be treated as incomplete.