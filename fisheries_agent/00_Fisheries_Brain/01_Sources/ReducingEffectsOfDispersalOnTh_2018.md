---
species: []
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: ["stream", "freshwater"]
ocean_basin: "N/A"
location: ["North America", "Michigan"]
tags: ["mark-recapture", "abundance estimation", "Chapman estimator", "dispersal bias", "stream fish", "population estimation", "sampling design"]
analytical_category: ["bias analysis", "estimator performance", "simulation study", "closed-population model"]
model_framework: "Chapman's estimator; 2-sample mark-recapture; modified sampling scheme"
software_environment: ["R", "doParallel", "doRNG"]
data_requirements: ["capture counts", "recapture counts", "marked individuals", "minimum 7 recaptures recommended"]
key_assumptions: ["spatial closure (no dispersal)", "equal capture probability within sample", "mark retention", "mark recognition", "Bernoulli sampling"]
keywords_stubs: ["#mark-recapture", "#Chapman-estimator", "#dispersal-bias", "#sampling-variation", "#stream-fisheries", "#electrofishing", "#spatial-closure", "#MRR-estimator", "#Petersen-estimator", "#bias-correction", "#modified-sampling-scheme", "#reach-scale-abundance"]
title: "Reducing effects of dispersal on the bias of 2-sample mark-recapture estimators of stream fish abundance"
source_id: "X-f940cff9"
doc_type: "analyses_and_modeling"
source_citation: "J. N. McNair, C. R. Ruetz, A. Carlson, J. Suh (2018). Reducing effects of dispersal on the bias of 2-sample mark-recapture estimators of stream fish abundance. PLOS ONE 13(8): e0200733."
doi: "10.1371/journal.pone.0200733"
source_file: "McNair et al. 2018 - Reducing effects of dispersal on mark-recapture estimate bias.pdf"
text_extraction: "text"
---
# Reducing effects of dispersal on the bias of 2-sample mark-recapture estimators of stream fish abundance

#ichthyology #stream-fish #mark-recapture #abundance-estimation

## Analytical Objective & Scope

**Core Problem Addressed**: Quantifying and reducing the bias of Chapman's estimator for stream fish abundance when the spatial closure assumption is violated by dispersal between sampling occasions. The standard 2-sample mark-recapture method assumes no fish enter or exit the study reach between samples 1 and 2, but this assumption is commonly violated in practice, especially when block nets cannot be used or are ineffective.

**Methodological Classification**: Novel analytical extension and methodological adaptation. The paper derives new analytical expressions for the expected value and bias of [[Chapman's Estimator]] that account for both dispersal and sampling variation in finite populations (not previously available in the literature). It also proposes and evaluates a modified sampling scheme where the study reach is expanded, sample 1 is restricted to a central zone, and sample 2 covers the entire expanded reach, reducing marked-fish emigration while maintaining the same sampling effort.

## Mathematical & Statistical Framework

**Model Formulation**: 

The standard [[MRR Estimator]] (mark-recapture ratio) is:
$$\hat{N} = \frac{c'm}{r'}$$
where $m$ = number marked in sample 1, $c'$ = total captures in sample 2, $r'$ = recaptures in sample 2. This estimator has undefined moments when $r' = 0$.

[[Chapman's Estimator]] resolves this:
$$\hat{N}^* = \frac{(M+1)(C'+1)}{R'+1} - 1$$

**Closed Population (no dispersal)**: Under Bernoulli sampling with parameters $n$ (abundance), $q$ (sample-1 capture probability), $q'$ (sample-2 capture probability), the unconditional expected value is:
$$E(\hat{N}^*) = O_0 - \phi_0 \lambda_0^{n-1}$$
where $O_0 = n$, $\phi_0 = (1-q)(1-q')n$, $\lambda_0 = 1 - qq'$. Relative bias: $b(\hat{N}^*, n) = -(1-q)(1-q')\lambda_0^{n-1}$ (always negative).

**With Dispersal (standard scheme)**: Let $p$ = exit probability, $\tilde{I}$ = expected number of immigrants. Then:
$$E(\hat{N}^*) = O_1 - \phi_1 \lambda_1^{n-1}$$
where:
- $O_1 = n + \tilde{I}/(1-p) = E(N')/( 1-p)$
- $\phi_1 = [O_1(1-qq'(1-p)) - nq(1-q'(1-p))](1-q'(1-p))$
- $\lambda_1 = 1 - qq'(1-p)$

Relative bias with respect to initial abundance $n$:
$$b(\hat{N}^*, n) = \frac{\tilde{I}}{(1-p)n} - \frac{\phi_1}{n}\lambda_1^{n-1}$$
First term reflects dispersal (positive bias), second term reflects sampling variation (negative bias). Net bias can be positive, negative, or zero.

**Modified Sampling Scheme**: Study reach divided into zones U (upstream), C (central), D (downstream). Sample 1 taken only from zone C (abundance $n_C$), sample 2 from entire reach (abundance $n = n_U + n_C + n_D$). Exit probabilities $p_U$, $p_C$, $p_D$ from respective zones. Expected value:
$$E(\hat{N}^*) = O_2 - \phi_2 \lambda_2^{n_C - 1}$$
where:
- $O_2 = [n(1-\tilde{p}) + \tilde{I}]/(1-p_C) = E(N')/(1-p_C)$
- $\tilde{p} = \pi_U p_U + \pi_C p_C + \pi_D p_D$ (weighted average exit probability)
- $\phi_2 = [O_2(1-qq'(1-p_C)) - n_C q(1-q'(1-p_C))](1-q'(1-p_C))$
- $\lambda_2 = 1 - qq'(1-p_C)$

When properly implemented, $p_C \approx 0$, so $O_2 = E(N')$ and relative bias with respect to $E(N')$ is:
$$b(\hat{N}^*, E(N')) = -[\phi_2/E(N')]\lambda_2^{n_C - 1}$$
This approaches zero as $n_C$ increases (asymptotically unbiased with respect to expected abundance at sample 2).

**Variables & Covariates**:
- Response: $\hat{N}^*$ (Chapman's abundance estimate)
- Parameters: $n$ (initial abundance), $n'$ (abundance at sample 2), $q$, $q'$ (capture probabilities), $p$ (exit probability), $\tilde{I}$ (expected immigrants)
- Random variables: $M$ (sample-1 captures), $C'$ (sample-2 captures), $R'$ (recaptures), $O_m$ (marked emigrants), $O_u$ (unmarked emigrants), $I_u$ (unmarked immigrants)
- Distributional assumptions: $M \sim \text{Binomial}(n, q)$; $C' \sim \text{Binomial}(n', q')$; $O_m \sim \text{Binomial}(m, p)$; $O_u \sim \text{Binomial}(u, p)$

**Fit Diagnostics & Metrics**:
- Bias: $B(\hat{N}^*, n) = E(\hat{N}^*) - n$
- Relative bias: $b(\hat{N}^*, n) = [E(\hat{N}^*) - n]/n$ (expressed as percent)
- Precision: Interquartile range (IQR) from simulations
- Convergence criterion: Asymptotic bias adequate when $|b - b_\infty| \leq 10^{-2}$, requiring $n \geq n_{crit}$ where:
  - Standard scheme: $n_{crit} = 1 + \frac{2 + \log_{10}(b)}{|\log_{10}(\lambda_1)|}$
  - Modified scheme: $n_{crit} = 3[1 + \frac{2 + \log_{10}(b)}{|\log_{10}(\lambda_2)|}]$
- Simulation validation: Empirical mean $\bar{\hat{N}^*}$ compared to theoretical $E(\hat{N}^*)$; agreement within 1% in all cases

## Data Requirements & Preprocessing

**Input Data Schema**:
- Minimum sample size: At least 7 recaptures recommended to avoid pronounced negative bias (Robson and Regier 1958 criterion). With fewer recaptures, sampling variation dominates and creates substantial negative bias.
- Zero-inflation: When $R' = 0$ (zero recaptures), MRR estimator is undefined (infinite); Chapman's modification ensures finite estimates for all outcomes by using $R' + 1$ in denominator.
- Missing data: Not explicitly addressed; method assumes all marked fish are recognized as marked upon recapture.
- Capture probability requirements: For asymptotic bias approximations to be adequate, both $q$ and $q'$ should be ≥0.2 when abundance per zone is ~150. With $q'$ = 0.1 or lower, abundance per zone must be ≫500 for asymptotic results to apply.
- Mark-recapture probability: The probability $qq'$ that any given fish is caught in both samples critically determines the rate at which sampling-variation bias decays with increasing abundance. Low mark-recapture probability (high $\lambda = 1 - qq'$) requires much larger abundances for bias to become negligible.
- Temporal constraints: Time between samples typically 1 day or less to minimize recruitment and mortality; must be short relative to movement rates for modified scheme to be effective.
- Spatial constraints: For modified scheme, distance between boundaries of central zone and expanded reach must exceed ~95th percentile of movement distance distribution during inter-sample interval.

**Sampling Cross-References**: 
#electrofishing #block-nets #spatial-closure #reach-scale-sampling #pilot-study #movement-distance #inter-sample-interval #capture-probability #batch-marking #fin-clips #temporary-marking #two-pass-sampling #depletion-method #removal-sampling #CPUE #single-pass-electrofishing

## Code Logic

**R Simulation Pseudocode** (from Methods):

```r
# Main simulation loop
for (each combination of parameters) {
  # Specify habitat: study reach length, buffer reach lengths, zone lengths
  # Specify fish parameters: initial abundance per zone, capture probabilities,
  #   movement parameters (max distance δ, beta distribution shape)
  # Set n.iter = 10,000
  
  for (i in 1:n.iter) {
    # Assign initial spatial locations (uniform random within each zone)
    fish_locations <- runif(n_total, min=zone_start, max=zone_end)
    
    # Sample 1: Bernoulli capture with probability q
    sample1 <- rbinom(n_fish, size=1, prob=q)
    marked <- which(sample1 == 1)
    
    # Movement: symmetric beta distribution, mode at 0, support [-δ, δ]
    movement <- rbeta_symmetric(n_fish, shape1=4, shape2=4, 
                                min=-delta, max=delta)
    fish_locations <- fish_locations + movement
    
    # Sample 2: Bernoulli capture with probability q'
    # For standard scheme: sample entire study reach
    # For modified scheme: sample zones U, C, D
    sample2 <- rbinom(n_fish_in_reach, size=1, prob=q_prime)
    
    # Determine recaptures
    recaptures <- intersect(marked, which(sample2 == 1))
    R_prime <- length(recaptures)
    
    # Calculate Chapman estimate
    M <- length(marked)
    C_prime <- sum(sample2)
    N_hat <- ((M + 1) * (C_prime + 1)) / (R_prime + 1) - 1
  }
  
  # Calculate empirical statistics
  mean_N_hat <- mean(N_hat_vector)
  bias_n <- (mean_N_hat - n) / n
  bias_N_prime <- (mean_N_hat - mean(N_prime_vector)) / mean(N_prime_vector)
  IQR <- quantile(N_hat_vector, 0.75) - quantile(N_hat_vector, 0.25)
  
  # Calculate theoretical expected value using Eq (8) or (10)
  E_N_hat_theory <- calculate_theoretical_mean(n, q, q_prime, p, I_tilde)
}
```

**Capture Probability Adjustment for Equal Sampling Effort** (Eq 11):
When comparing sampling schemes, if expanded reach is $k$ times the size of central zone, and sampling duration $T$ is constant:
```r
# Relationship between capture probabilities
q_C <- 1 - (1 - q_X)^k
# where q_C = capture prob in central zone with duration T
#       q_X = capture prob in expanded reach with duration T
#       k = size ratio (e.g., k=3 when expanded reach is 3× central zone)
```

**Theoretical Bias Calculation**:
```r
# Standard scheme with dispersal (Eq 8)
O_1 <- n + I_tilde / (1 - p)
phi_1 <- (O_1 * (1 - q*q_prime*(1-p)) - n*q*(1 - q_prime*(1-p))) * 
         (1 - q_prime*(1-p))
lambda_1 <- 1 - q*q_prime*(1-p)
E_N_hat <- O_1 - phi_1 * lambda_1^(n-1)
rel_bias <- (E_N_hat - n) / n

# Modified scheme (Eq 10, with p_C ≈ 0)
O_2 <- n*(1 - p_tilde) + I_tilde  # where p_tilde is weighted avg exit prob
phi_2 <- (O_2 * (1 - q*q_prime) - n_C*q*(1 - q_prime)) * (1 - q_prime)
lambda_2 <- 1 - q*q_prime
E_N_hat <- O_2 - phi_2 * lambda_2^(n_C - 1)
rel_bias_N_prime <- (E_N_hat - O_2) / O_2
```

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

The analytical framework directly informs field sampling design for routine stream fisheries assessments where agencies must estimate reach-scale abundance at hundreds of sites. Key management applications include:

1. **Temporal trend monitoring**: Documenting changes in abundance over time to assess efficacy of fishing regulations. Dispersal-related positive bias can mask population declines if not corrected.

2. **Spatial distribution assessment**: Comparing abundance among reaches to identify critical habitats or reaches requiring enhancement. Systematic bias differences among reaches (due to varying dispersal rates) can lead to misallocation of management resources.

3. **Reference point estimation**: Abundance estimates feed into stock-recruitment models and harvest quota calculations. Bias of 20-100% (common with standard scheme and high dispersal) would severely compromise these applications.

**Decision Rules from Bias Analysis**:

- **When to expand study reach**: If exit probability $p \geq 0.1$ and capture probabilities $q, q' \geq 0.2$, expanding the reach reduces relative bias from ~43% (p=0.3) or ~100% (p=0.5) to ~11% or ~20%, respectively, with same sampling effort.

- **When to use modified scheme**: If dispersal is significant (p ≥0.1) and abundance per zone ≥100, modified scheme reduces bias to near-zero while standard scheme on expanded reach retains 10-20% positive bias. Exception: when both abundance per zone <100 AND capture probability <0.1, standard scheme may perform better due to sampling variation effects.

- **Minimum abundance thresholds**: Asymptotic bias formulas (simpler to calculate) adequately approximate exact bias when abundance per zone ≥150 and both capture probabilities ≥0.2. Below these thresholds, exact finite-population formulas (Eqs 8, 10) are required.

- **Precision requirements**: To achieve ≥7 recaptures (Robson-Regier criterion), with $q = q' = 0.3$ and $n = 100$, expected recaptures = $100 \times 0.3 \times 0.3 = 9$. Lower abundances or capture probabilities require reach expansion or increased effort.

**Practical Implementation Guidance**:

The modified sampling scheme requires determining appropriate buffer distances (zones U and D). Recommended approach: conduct pilot mark-recapture with sample 1 in original reach, sample 2 extending as far as feasible, record recapture distances from original boundaries, then set buffer distance somewhat greater than maximum observed recapture distance. This ensures $p_C \approx 0$ without requiring detailed movement distribution data.

**Trade-offs vs. Alternative Methods**:

- **Open-population methods** ([[Jolly-Seber]], [[Pollock's Robust Design]], spatial mark-recapture): Relax closure assumptions but require permanent unique marking (expensive tags vs. free fin clips) and multiple site visits (3-5 days vs. 2 days). Cost prohibitive for routine assessments across hundreds of reaches.

- **3-pass removal**: Single-day sampling but prone to severe negative bias unless capture probabilities consistently ≥0.5 (difficult to achieve). Not appropriate for large populations.

- **Single-pass electrofishing (CPUE)**: Fastest method but yields only relative abundance, sensitive to uncontrolled variation in catchability. Useful for qualitative trends only.

The modified 2-sample mark-recapture scheme occupies a practical middle ground: more robust to dispersal than standard scheme, more cost-effective than open-population methods, more accurate than removal or CPUE methods, while retaining the logistical advantages of temporary batch marking and 2-day sampling that have made this approach the global standard for stream fisheries management since ~