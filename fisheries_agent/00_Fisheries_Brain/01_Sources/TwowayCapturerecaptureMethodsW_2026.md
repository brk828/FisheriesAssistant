---
species: ["N/A"]
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: "N/A"
ocean_basin: "N/A"
location: ["Cambodia", "Thailand"]
tags: ["capture-recapture", "population estimation", "bootstrap methods", "dual system estimation", "Chapman estimator", "statistical inference"]
analytical_category: ["population size estimation", "variance estimation", "confidence interval construction", "bootstrap resampling"]
model_framework: "Capture-recapture dual system estimation with Chapman estimator and bias-corrected variants"
software_environment: ["R"]
data_requirements: ["two independent sources", "2×2 contingency table", "multinomial distribution", "minimum overlap between sources (n11 > 0)"]
key_assumptions: ["closed population", "independence between sources (OR = 1)", "independence of individuals", "independence of observational occasions", "no population changes during study period"]
keywords_stubs: ["#capture-recapture", "#Chapman-estimator", "#bootstrap", "#population-estimation", "#dual-system", "#confidence-intervals", "#variance-estimation", "#imputed-bootstrap"]
title: "Two-way capture-recapture methods with emphasis on the bootstrap"
source_id: "X-e52c17a2"
doc_type: "analyses_and_modeling"
source_citation: "P. Sangnawakij, R. Lerdsuwansri, P. Pijitrattana, P. Schlattmann, A. Maruotti, D. Bohning (2026). Two-way capture-recapture methods with emphasis on the bootstrap. Statistical Methods &amp; Applications 35(1): 1-22."
doi: "10.1007/s10260-026-00840-5"
source_file: "Sanwnawakij et al 2026 - Two-way capture-recapture methods.pdf"
text_extraction: "text"
---
# Two-way capture-recapture methods with emphasis on the bootstrap

#statistics #population-estimation #capture-recapture

## Analytical Objective & Scope

**Core Problem Addressed**: Estimating the size of elusive target populations using dual system (two-source) capture-recapture methods, with focus on improving uncertainty assessment through bootstrap methods when sample sizes are small and asymptotic variance estimates perform poorly.

**Methodological Classification**: Adaptation and comparison of existing methods. The study evaluates three bootstrap approaches (imputed bootstrap, double bootstrap with imputation, simple bootstrap without imputation) as alternatives to asymptotic normal confidence intervals for the [[Chapman Estimator]] and bias-corrected Chapman estimator in two-source capture-recapture settings.

## Mathematical & Statistical Framework

**Model Formulation**: 

The Chapman estimator for population size N is:
$$\hat{N}_C = \frac{(n_{1\cdot} + 1)(n_{\cdot1} + 1)}{n_{11} + 1} - 1 = n + \frac{n_{10}n_{01}}{n_{11} + 1}$$

with implied estimator of missing cell:
$$\hat{n}_{00C} = \frac{n_{10}n_{01}}{n_{11} + 1}$$

Asymptotic variance:
$$\hat{Var}(\hat{N}_C) = \frac{(n_{1\cdot} + 1)(n_{\cdot1} + 1)n_{10}n_{01}}{(n_{11} + 1)^2(n_{11} + 2)}$$

Bias-corrected Chapman estimator:
$$\hat{N}_{BC} = \frac{\hat{N}_C}{1 - \hat{\Delta}}$$
where $\hat{\Delta} = \exp\{-(n_{1\cdot} + 1)(n_{\cdot1} + 1)/\hat{N}_C\}$

**Variables & Covariates**: 
- **Response**: Population size N (unknown)
- **Observed frequencies**: n₁₁ (identified by both sources), n₁₀ (source 1 only), n₀₁ (source 2 only)
- **Unobserved frequency**: n₀₀ (identified by neither source)
- **Marginals**: n₁. (total in source 1), n.₁ (total in source 2), n (total observed)
- **Dependency measure**: Odds ratio OR = n₁₁n₀₀/n₁₀n₀₁

**Fit Diagnostics & Metrics**: 
- Coverage probability of 95% confidence intervals (target: 0.95)
- Relative bias: $\frac{1}{N}(\frac{1}{R}\sum_{r=1}^{R}\hat{N}_r - N)$
- Interval length
- Variance comparison between true and bootstrap distributions
- Simulations with R = 10,000 replications and B = 5,000 bootstrap samples

## Data Requirements & Preprocessing

**Input Data Schema**: 
- Minimum requirement: 2×2 contingency table with three observed cells (n₁₁, n₁₀, n₀₁)
- n₁₁ must be > 0 to avoid undefined estimates
- Chapman estimator is exactly unbiased when n₁. + n.₁ ≥ N
- Small sample sizes (N < 50) can introduce negative bias
- Zero-inflation: Not directly addressed; method assumes at least some overlap between sources
- Missing data: The unobserved cell n₀₀ is the target of estimation

**Sampling Cross-References**: 
- [[Dual System Estimation]]
- [[Two-Source Capture-Recapture]]
- [[Multinomial Sampling]]
- [[Independence Assumption]]

## Code Logic

**Bootstrap I (Imputed Bootstrap)**:
```
1. Calculate event probability vector: 
   p̂ = (n₁₁/N̂_C, n₁₀/N̂_C, n₀₁/N̂_C, n̂₀₀C/N̂_C)
2. Draw (n*₁₁, n*₁₀, n*₀₁, n*₀₀) ~ Multinomial(N̂_C, p̂)
3. Ignore n*₀₀ and calculate:
   n̂*₀₀ = n*₁₀n*₀₁/(n*₁₁ + 1)
   N̂* = n*₁₁ + n*₁₀ + n*₀₁ + n̂*₀₀
4. Repeat B times to get N̂*(1), ..., N̂*(B)
5. Calculate percentile bootstrap confidence interval
```

**Bootstrap II (Double Bootstrap with Imputation)**:
```
1. Calculate p̃ = (n₁₁/n, n₁₀/n, n₀₁/n)
2. Draw (n*₁₁, n*₁₀, n*₀₁) ~ Multinomial(n, p̃)
3. Calculate n̂*₀₀ = n*₁₀n*₀₁/(n*₁₁ + 1)
4. Calculate p̂* = (n₁₁/N̂*, n₁₀/N̂*, n₀₁/N̂*, n̂*₀₀/N̂*)
   where N̂* = n₁₁ + n₁₀ + n₀₁ + n̂*₀₀
5. Draw (n**₁₁, n**₁₀, n**₀₁, n**₀₀) ~ Multinomial(N̂*, p̂*)
6. Ignore n**₀₀ and compute:
   n̂**₀₀ = n**₁₀n**₀₁/(n**₁₁ + 1)
   N̂** = n**₁₁ + n**₁₀ + n**₀₁ + n̂**₀₀
7. Repeat B times
8. Calculate percentile bootstrap confidence interval
```

**Bootstrap III (Simple Bootstrap without Imputation)**:
```
1. Calculate p̃ = (n₁₁/n, n₁₀/n, n₀₁/n)
2. Draw (n*₁₁, n*₁₀, n*₀₁) ~ Multinomial(n, p̃)
3. Compute:
   n̂*₀₀ = n*₁₀n*₀₁/(n*₁₁ + 1)
   N̂* = n*₁₁ + n*₁₀ + n*₀₁ + n̂*₀₀
4. Repeat B times
5. Calculate percentile bootstrap confidence interval
```

All analyses implemented in R (R Core Team 2024).

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

The methods provide population size estimates for hidden or elusive populations where complete enumeration is impossible. Applications demonstrated include:

1. **[[Suicide Data]] in [[Cambodia]]** (n = 158 observed): Estimated total N̂ = 534-539 suicides (95% CI: 358-941 using imputed bootstrap), revealing substantial underreporting in newspaper sources.

2. **[[Heroin Users]] in [[Thailand]]** (n = 1,447 observed): Estimated N̂ = 4,989-5,000 users (95% CI: 4,338-5,868), identifying approximately 3,542-3,553 hidden users not captured by treatment facility records.

**Key Management Implications**:
- Imputed bootstrap (Bootstrap I) recommended for practical applications due to superior coverage probability (closer to nominal 0.95) and reduced computational cost compared to double bootstrap
- Methods perform well under independence (OR = 1) and moderate dependence (OR < 3.5) between sources
- Extreme positive dependence (OR ≥ 3.5) leads to underestimation of variance and poor confidence interval coverage across all methods
- Small sample sizes (N < 50) require bias-corrected Chapman estimator
- Formula-based asymptotic confidence intervals consistently underperform bootstrap methods, especially with small samples
- Bootstrap variance underestimates true variance when sources are highly dependent, leading to overly narrow confidence intervals

The estimand E(N̂) rather than true N should be used for inference when sources are dependent, as the Chapman estimator provides a conservative lower bound in such cases.