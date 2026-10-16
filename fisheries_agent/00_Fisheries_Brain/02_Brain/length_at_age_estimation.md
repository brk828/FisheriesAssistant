---
type: concept
---
# length_at_age_estimation

## Summary
This is a Bayesian hierarchical approach implemented in JAGS that fits a repeated-measures von Bertalanffy growth model to aged fish, then probabilistically assigns ages to unaged individuals based on their lengths. For each of the unaged fish in survey samples, the method generates 1000 stochastic age draws from a multinomial distribution of age probabilities, propagating age composition uncertainty through the integrated population model to produce robust density-at-age estimates.

## Context

> **Core Problem Addressed**: Evaluate the population-level consequences of a decade-long [[Common Carp]] removal effort in [[Utah Lake]] (>12,000 tons harvested 2009-2018) and determine whether current mechanical removal strategies can maintain carp biomass below management targets (75% reduction)...
> -- *[[CompensatoryRecruitmentDynamic_2020]]*

## Mentioned In
- [[CompensatoryRecruitmentDynamic_2020]]
