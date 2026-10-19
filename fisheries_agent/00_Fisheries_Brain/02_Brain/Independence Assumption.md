---
type: concept
---
# Independence Assumption

## Summary
The independence assumption requires that the two data sources capture individuals independently, meaning capture by one source does not affect the probability of capture by the other source (odds ratio = 1). This source evaluates estimator performance under varying degrees of dependence, showing that the Chapman estimator and bootstrap methods perform well under independence and moderate dependence (OR < 3.5) but suffer from variance underestimation and poor confidence interval coverage when sources show extreme positive dependence (OR ≥ 3.5). When sources are dependent, the Chapman estimator provides a conservative lower bound on population size.

## Context

> **Core Problem Addressed**: Estimating the size of elusive target populations using dual system (two-source) capture-recapture methods, with focus on improving uncertainty assessment through bootstrap methods when sample sizes are small and asymptotic variance estimates perform poorly....
> -- *[[TwowayCapturerecaptureMethodsW_2026]]*

## Mentioned In
- [[TwowayCapturerecaptureMethodsW_2026]]
