---
species: ["Atlantic sturgeon", "lake trout", "walleye", "American lobster", "pirarucu", "Indo-Pacific humpback dolphin", "marine turtles"]
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: ["freshwater", "marine", "estuarine"]
ocean_basin: ["Atlantic", "Gulf of Mexico"]
location: ["North America", "Delaware River Estuary", "Lake Pend Oreille", "Pamunkey River", "Leizhou Bay China", "Northeastern Gulf of Mexico"]
tags: ["mark-recapture", "population estimation", "closed population", "statistical methods", "Monte Carlo simulation", "bias correction"]
analytical_category: ["population estimation", "mark-recapture", "bias correction", "simulation study", "comparative methods"]
model_framework: ["Lincoln-Petersen", "Chapman", "Chao", "Bayesian", "Schnabel", "Schumacher-Eschmeyer", "hypergeometric distribution", "Poisson distribution"]
software_environment: ["R", "R v4.2.0"]
data_requirements: ["marked individuals", "recapture counts", "sample sizes", "multiple sampling visits", "closed population", "random sampling without replacement"]
key_assumptions: ["closed population (no births, deaths, movement)", "independence between visits (marking does not affect recapture probability)", "independence between individuals (complete mixing)", "sampling without replacement", "no mark loss"]
keywords_stubs: ["#mark-recapture", "#closed-population", "#bias-correction", "#Chapman-estimator", "#Schnabel", "#Schumacher-Eschmeyer", "#Lincoln-Petersen", "#population-size", "#Monte-Carlo-simulation", "#hypergeometric-distribution", "#RMSE", "#minimum-sample-size"]
title: "Assessment of bias and precision among simple closed population mark-recapture estimators"
source_id: "X-39c763eb"
doc_type: "analyses_and_modeling"
source_citation: "K. Dettloff (2023). Assessment of bias and precision among simple closed population mark-recapture estimators. Fisheries Research 265: 106756."
doi: "10.1016/j.fishres.2023.106756"
source_file: "noaa_52288_DS1.pdf"
text_extraction: "text"
---
# Assessment of Bias and Precision Among Simple Closed Population Mark-Recapture Estimators

#ichthyology #population-ecology #statistical-methods

## Analytical Objective & Scope

**Core Problem Addressed**: This study evaluates the comparative statistical performance of common closed population mark-recapture estimators to determine which methods produce the most accurate and precise population size estimates under varying sample sizes. The analysis addresses the practical need for guidance on selecting appropriate estimators and minimum sample sizes for field applications in fisheries and wildlife sciences.

**Methodological Classification**: This is a novel adaptation combining standard empirical application with methodological innovation. The study applies Monte Carlo simulation to compare existing estimators ([[Lincoln-Petersen]], [[Chapman]], [[Chao]], Bayesian, [[Schnabel]], [[Schumacher-Eschmeyer]]) and proposes a new bias-adjusted version of the Schumacher-Eschmeyer estimator. The work extends existing bias-correction theory (Chapman 1951, 1952) to multi-visit scenarios and derives minimum sample size rules for approximately unbiased estimation.

## Mathematical & Statistical Framework

**Model Formulation**:

Two-visit estimators:

- **Lincoln-Petersen** (Eq. 1): $\hat{N} = \frac{Mn}{m}$

- **Chapman** (Eq. 2): $\hat{N} = \frac{(M+1)(n+1)}{(m+1)} - 1$ (based on hypergeometric distribution)

- **Chao** (Eq. 3): $\hat{N} = \frac{(M+n-2m)^2}{4m} + M + n - m$

- **Bayesian** (Eq. 4): $\hat{N} = \frac{(M-1)(n-1)}{(m-2)}$ for m > 2

Multi-visit estimators (k > 2):

- **Schnabel** (Eq. 5): $\hat{N} = \frac{\sum_k M_k n_k}{\sum_k m_k}$

- **Schnabel bias-adjusted** (Eq. 6): $\hat{N} = \frac{\sum_k M_k n_k}{\sum_k m_k + 1}$

- **Schumacher-Eschmeyer** (Eq. 7): $\hat{N} = \frac{\sum_k M_k^2 n_k}{\sum_k M_k m_k}$

- **Schumacher-Eschmeyer bias-adjusted (novel)** (Eq. 8): $\hat{N} = \frac{\sum_{k=2}^k (M_k+1)^2(n_k+1)}{\sum_k M_k(m_k+1)} - 2$

The bias-adjusted Schumacher-Eschmeyer satisfies (Eq. 13): $E[\hat{N}] \to N$ as $\sqrt[k]{\prod_{b=2}^k n_b} \to N$

**Variables & Covariates**:

- **Response variable**: $\hat{N}$ = estimated population size
- **Fixed parameters**: N = true population size (known in simulations)
- **Predictors**: M = number marked on first visit; n = total captured on subsequent visit(s); m = number of marked individuals recaptured
- **Multi-visit notation**: $M_k$ = total marked prior to visit k; $n_k$ = total captured on visit k; $m_k$ = marked recaptured on visit k
- **No random effects**: All estimators are deterministic functions of observed counts

**Fit Diagnostics & Metrics**:

- **Bias**: $bias(\hat{N}) = E[\hat{N}] - N$ calculated from 10,000 simulations
- **Variance**: $var(\hat{N})$ = sample variance across simulations
- **Standard Error**: $SE(\hat{N})$ = sample standard deviation across simulations
- **Scaled RMSE** (Eq. 9): $RMSE_{scaled} = \frac{\sqrt{var(\hat{N}) + bias(\hat{N})^2}}{N}$
- **Percent Error** (Eq. 12): $Pct. Error = 100(\frac{\hat{N} - N}{N})$
- **Convergence**: Estimates calculated from all simulations producing finite values (10,000 iterations per scenario)
- **Coverage**: Not explicitly reported but bias thresholds established (< 2% for Chapman at minimum sample sizes)

## Data Requirements & Preprocessing

**Input Data Schema**:

- **Minimum sample size**: Population-dependent; for Chapman estimator, approximately unbiased when $\sqrt{Mn} \geq 2\sqrt{N}$ (Eq. 10); for adjusted Schnabel, when $\sqrt[k]{\prod_{b=2}^k n_b} \geq \frac{2\sqrt{N}}{k-1}$ (Eq. 11)
- **Sample size range tested**: Very small (producing extreme downward bias) to large (M and n increasing from minimal to substantial fractions of N)
- **Population sizes simulated**: N = 100 to 1,000,000 (results presented primarily for N = 1,000)
- **Number of visits**: k = 2 for two-visit methods; k = 3, 4, 5 for multi-visit methods
- **Zero-inflation**: Acknowledged as problematic at very small sample sizes (no recaptures = no valid estimate)
- **Missing data**: Not applicable; simulations generate complete data
- **Data structure**: Counts of marked (M), captured (n), and recaptured (m) individuals per visit
- **Sampling scenarios**: M = n, M < n, M > n evaluated separately

**Sampling Cross-References**:

The document emphasizes sampling design considerations that affect estimator performance: #random-sampling-without-replacement, #complete-mixing-assumption, #closed-population-assumption, #capture-probability-independence, #mark-retention, #sampling-area-definition, #individual-heterogeneity, #temporal-closure. Field applications cited include #Atlantic-sturgeon-tagging, #lake-trout-surveys, #walleye-pulse-fishing, #lobster-no-take-reserves, #pirarucu-fisheries-assessment, #dolphin-abundance-surveys, #marine-turtle-foraging-areas, #creel-survey-angler-counts.

## Code Logic

**Simulation Framework** (R v4.2.0):

```r
# Core simulation structure (pseudocode from methods)
# Fixed population of known size N generated
# Random sampling without replacement using sample() function

for (iteration in 1:10000) {
  # Two-visit methods:
  marked <- sample(population, size = M, replace = FALSE)
  recaptured <- sample(population, size = n, replace = FALSE)
  m <- length(intersect(marked, recaptured))
  
  # Calculate estimates using Eq. 1-4
  N_hat_LP <- (M * n) / m
  N_hat_Chapman <- ((M + 1) * (n + 1)) / (m + 1) - 1
  N_hat_Chao <- ((M + n - 2*m)^2) / (4*m) + M + n - m
  N_hat_Bayes <- ((M - 1) * (n - 1)) / (m - 2)  # if m > 2
  
  # Multi-visit methods (k visits):
  # Accumulate M_k, n_k, m_k across visits
  # Calculate Schnabel (Eq. 5, 6) and Schumacher-Eschmeyer (Eq. 7, 8)
  N_hat_Schnabel <- sum(M_k * n_k) / sum(m_k)
  N_hat_Schnabel_adj <- sum(M_k * n_k) / (sum(m_k) + 1)
  N_hat_SE <- sum(M_k^2 * n_k) / sum(M_k * m_k)
  N_hat_SE_adj <- sum((M_k + 1)^2 * (n_k + 1)) / sum(M_k * (m_k + 1)) - 2
  
  # Store finite estimates
}

# Calculate performance metrics
bias <- mean(N_hat) - N
SE <- sd(N_hat)
RMSE_scaled <- sqrt(var(N_hat) + bias^2) / N
```

**Bootstrap Confidence Intervals** (referenced but not implemented):

```r
# Parametric bootstrap for two-visit data (Tyers 2021 approach)
# Resample m with replacement using binomial distribution
m_bootstrap <- rbinom(n_bootstrap, size = n, prob = m/n)
# Calculate N_hat for each bootstrap sample
# Construct confidence intervals from bootstrap distribution
```

Code provided in Supporting Information for readers to run simulations under custom parameters.

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

**Population Status Assessment**: The Chapman estimator is recommended as the superior two-visit method for estimating closed population sizes, providing approximately unbiased estimates when $\sqrt{Mn} \geq 2\sqrt{N}$ (Eq. 10). This threshold translates to practical sampling guidance: for a suspected population of 1,000 individuals, at least 63 individuals should be both marked and recaptured (geometric mean) to achieve < 2% negative bias. For populations of 10,000, this increases to 200 individuals.

**Multi-Visit Survey Design**: For studies with k ≥ 3 sampling events, the bias-adjusted Schnabel (Eq. 6) and bias-adjusted Schumacher-Eschmeyer (Eq. 8) both perform well, with trade-offs between bias reduction speed and variance. The adjusted Schnabel becomes unbiased slightly faster, while the adjusted Schumacher-Eschmeyer exhibits lower variability at small sample sizes and greater robustness to assumption violations. The minimum sample size rule (Eq. 11) indicates that for k = 3 visits and N = 1,000, the geometric mean of sample sizes should be approximately 45 individuals per visit to achieve acceptable bias (though -6.5% to -10.6% bias remains at this threshold, Table 1).

**Endangered Species Applications**: The bias-adjusted Schumacher-Eschmeyer is particularly impactful for low-recapture scenarios common in threatened species studies (e.g., [[Atlantic Sturgeon]] with only 2 recaptures among 17 marked). The original unadjusted estimator would substantially overestimate population size in such cases. Applications extend to [[Indo-Pacific Humpback Dolphin]], juvenile [[Marine Turtles]] with high site fidelity, and other species where closed population assumptions are reasonable over short time scales.

**Reference Points & Thresholds**: 
- **Avoid use**: Do not apply any estimator when sample sizes fall below the minimum thresholds (Eq. 10, 11), as extreme downward bias (> 50%) occurs
- **Acceptable bias**: Chapman achieves < 2% bias at threshold; adjusted Schnabel exhibits -3% to -10% bias depending on k and N
- **Precision gains**: Multi-visit methods reduce variance compared to two-visit methods at equal total sample sizes, with adjusted Schumacher-Eschmeyer showing lowest RMSE in the small-sample range where bias is still present

**Management Recommendations**: 
1. Discontinue use of Lincoln-Petersen, Chao, and Bayesian estimators in favor of Chapman for two-visit studies
2. Always use bias-adjusted versions (Eq. 6, 8) rather than original Schnabel or Schumacher-Eschmeyer formulations
3. Apply ceiling function to adjusted Schnabel estimates for integer population sizes
4. Use parametric bootstrap methods (Buckland and Garthwaite 1991, Tyers 2021) for confidence intervals rather than normal approximations
5. Recognize that minimum sample size rules provide lower bounds; larger samples needed when assumption violations suspected (individual heterogeneity in capture probability, incomplete mixing, population openness)

**Fisheries-Specific Guidance**: The methods remain widely applicable in contemporary fisheries (>1,650 articles since 2016), including [[Lake Trout]] population dynamics, [[Walleye]] pulse fishing responses, [[American Lobster]] in marine protected areas, [[Pirarucu]] fisheries assessment, and creel survey angler counts. The regression-based Schumacher-Eschmeyer offers additional robustness to assumption violations at the cost of higher small-sample variability, making it preferable when capture probability heterogeneity is suspected but cannot be modeled explicitly.