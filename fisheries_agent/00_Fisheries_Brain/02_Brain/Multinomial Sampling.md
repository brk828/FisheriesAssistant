---
type: concept
---
# Multinomial Sampling

## Summary
Multinomial sampling is the statistical framework underlying the capture-recapture data structure, where observed frequencies (n₁₁, n₁₀, n₀₁) follow a multinomial distribution with probabilities determined by the true population size and capture probabilities. This source uses multinomial sampling in all three bootstrap methods, drawing resamples from multinomial distributions with estimated event probabilities to generate bootstrap confidence intervals. The multinomial framework allows for proper accounting of sampling variability in the 2×2 contingency table structure.

## Context

> **Core Problem Addressed**: Estimating the size of elusive target populations using dual system (two-source) capture-recapture methods, with focus on improving uncertainty assessment through bootstrap methods when sample sizes are small and asymptotic variance estimates perform poorly....
> -- *[[TwowayCapturerecaptureMethodsW_2026]]*

## Mentioned In
- [[TwowayCapturerecaptureMethodsW_2026]]
