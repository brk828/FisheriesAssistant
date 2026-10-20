---
species: ["Larus ridibundus", "Branta canadensis", "Sterna dougallii", "Microtus pennsylvanicus", "Rissa tridactyla", "Phoenicopterus ruber", "Capreolus capreolus", "Anser caerulescens"]
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: ["breeding colonies", "wintering areas", "enclosed reserves"]
ocean_basin: "N/A"
location: ["Mid-Atlantic", "Chesapeake", "Carolinas", "Falkner Island Connecticut", "Forêt France"]
tags: ["capture-recapture", "multistate models", "survival estimation", "dispersal", "movement ecology", "statistical methodology"]
analytical_category: ["survival analysis", "movement modeling", "dispersal estimation", "recruitment modeling", "longitudinal data analysis"]
model_framework: "Arnason-Schwarz multistate capture-recapture model; Cormack-Jolly-Seber generalization; hidden Markov chains"
software_environment: ["MARK", "MSSURVIV", "SURGE", "Matlab"]
data_requirements: ["discrete capture occasions", "individual capture histories", "state assignments at capture", "marked individuals", "multiple sites or states"]
key_assumptions: ["Markovian transitions (fate depends only on last state)", "independence of individuals", "state-dependent capture probability", "survival independent of past beyond last occasion"]
keywords_stubs: ["#multistate-models", "#capture-recapture", "#dispersal-estimation", "#survival-probability", "#transition-matrices", "#breeding-dispersal", "#natal-dispersal", "#recruitment", "#movement-ecology", "#Arnason-Schwarz", "#maximum-likelihood"]
title: "Multistate recapture models: Modelling incomplete individual histories"
source_id: "X-d3a15ffa"
doc_type: "analyses_and_modeling"
source_citation: "J. D. Lebreton, R. P. Cefe (2002). Multistate recapture models: Modelling incomplete individual histories. Journal of Applied Statistics 29(1-4): 353-369."
doi: "10.1080/02664760120108638"
source_file: "Lebreton and Pradel 2002 Multistate recapture models modelling incomplete ind histories.pdf"
text_extraction: "text"
---
# Multistate recapture models: modelling incomplete individual histories

#ichthyology #capture-recapture #statistical-methodology

## Analytical Objective & Scope

**Core Problem Addressed**: Multistate capture-recapture models extend traditional single-site models to estimate survival, movement, and transition probabilities when individuals can move among a finite set of states (geographical sites or individual covariates) between sampling occasions. The models address spatial population dynamics, individual variability, dispersal estimation, and heterogeneity in capture probability.

**Methodological Classification**: This is primarily a methodological review and extension of existing models. The Arnason-Schwarz model (Arnason 1972, 1973; Schwarz et al. 1993) is the canonical multistate generalization of the Cormack-Jolly-Seber (CJS) model. Novel developments include: (1) multisite accession to reproduction models that simultaneously estimate age-dependent recruitment, natal dispersal, and breeding dispersal; (2) mixture models combining different information types; (3) connections to longitudinal studies with missing data and hidden Markov chains; (4) multistate growth rate models; (5) models accommodating uncertainty in state assignment.

## Mathematical & Statistical Framework

**Model Formulation**: The multistate model considers capture-recapture histories over K occasions and s sites/states. Capture histories are sequences of 0 (not captured) and integers i (i = 1,...,s) designating state at capture.

The fundamental parameters are:
- **Survival-transition probabilities** φ_ijk: probability of surviving from occasion k in state i and transitioning to state j
- **Capture probabilities** p_ik: probability of capture at occasion k in state i (time and state dependent)

The survival-transition probabilities decompose as:
φ_ijk = σ_ik × c_ijk

where σ_ik is conditional survival probability (departure state i, time k) and c_ijk are transition probabilities conditional on survival. The transition matrix **W**_k = [c_ijk] is column stochastic (Σ_j c_ijk = 1).

**Matrix Notation**: The model uses matrix formulation where **U**_k = [φ_ijk] are survival-transition matrices, **P**_k = diag(p_ki) are capture probability matrices. The likelihood is an exact matrix generalization of the CJS likelihood. Adding a "dead state" makes **U**_k column stochastic.

For the **multisite accession to reproduction model**, states combine breeders (A, B, C) and non-breeders (a, b, c) across sites. Transition matrices have block structure:

```
W_k = [B × diag(A_k)    B    ]
      [N × diag(A_k)    0    ]
```

where **B** is the 3×3 breeding dispersal matrix, **N** is the 3×3 natal dispersal matrix (first year only), and A_k are age-specific accession probabilities. Non-breeders have zero capture probability.

**Variables & Covariates**:
- **Response**: Individual capture history (sequence of states/non-detections)
- **Predictors**: Time (occasion), age (time since first capture), group, state (site or individual covariate category)
- **Random effects**: Not explicitly modeled in basic framework
- **Offsets**: None reported

**Fit Diagnostics & Metrics**: 
- **Maximum likelihood estimation** via iterative minimization of deviance = -2×log-likelihood
- **Model selection**: AIC, likelihood ratio tests (LRT)
- **Goodness-of-fit**: χ² tests when K and s are small (enumerate all capture histories, compare observed vs. expected); parametric bootstrap (Monte Carlo simulation) for larger models
- **Convergence**: Profile deviance plots to detect local minima and non-identifiability
- **Parameter constraints**: Generalized Linear Model (GLM) framework with logit link; design matrices for linear constraints
- **Identifiability**: Formal detection via numerical rank (Catchpole & Morgan 1997); profile deviance plots recommended

**Example Results** (Roseate Tern multisite recruitment model):
- Natal dispersal matrix **N** and breeding dispersal matrix **B** estimated (Table 4)
- Site A philopatry: 0.582 (natal), 0.885 (breeding)
- Site B philopatry: 0.913 (natal), 0.976 (breeding)  
- Site C philopatry: 0.898 (natal), 0.981 (breeding)
- Full recruitment achieved at age 5 years
- Natal dispersal intensity greater than breeding dispersal

**Longitudinal Data Example** (Fitzmaurice et al. 1994 obesity data reanalysis, Table 2):
- Pr(Survival) = 0.8709 (SE = 0.0116)
- Pr(Recapture) = 0.8997 (SE = 0.0128)
- Pr(Non-Obese | Obese) = 0.1169 (SE = 0.0104)
- Pr(Obese | Non-Obese) = 0.2701 (SE = 0.0285)

## Data Requirements & Preprocessing

**Input Data Schema**: 
- **Minimum sample size**: Not explicitly specified; depends on number of states, occasions, and model complexity. With s states and K occasions, the time-dependent Arnason-Schwarz model has s(s+1)(K-1) parameters (e.g., 10 occasions, 3 states = 54 parameters vs. 18 for single-site CJS).
- **Data structure**: Individual capture histories as sequences over K occasions; each capture records state (1 to s) or non-detection (0)
- **Zero-inflation**: Non-breeders in recruitment models have zero capture probability, creating structural zeros
- **Missing data**: The model inherently handles missing observations (non-captures); connections to longitudinal data with MAR (missing at random) and MCAR (missing completely at random) mechanisms
- **Sparseness**: Large number of possible capture histories [(s+1)^(K-1) - 1] creates sparseness issues; affects goodness-of-fit test power and χ² distribution

**Preprocessing**:
- Individuals marked at first capture; analysis conditional on initial releases
- States must be defined (geographical sites, reproductive status, body weight classes, etc.)
- For recruitment models: separate young-marked individuals; first capture always in non-breeder state
- Combination of states possible (e.g., site × reproductive status creates 2s states)

**Sampling Cross-References**: 
- #mark-recapture-design
- #capture-probability-heterogeneity
- #robust-design (primary and secondary occasions)
- #telemetry-data-integration
- #tag-recovery-models
- #resighting-surveys
- #colonial-waterbird-monitoring

## Code Logic

**Matrix Likelihood Calculation** (conceptual pseudocode):

```
# Initialize
U[k] = survival-transition matrix at time k
P[k] = diagonal capture probability matrix at time k
I_minus_P[k] = I - P[k]  # probability of non-capture

# For each individual history
likelihood_i = 1
for k in 1:(K-1):
    likelihood_i = likelihood_i * U[k]
    if captured at k+1:
        likelihood_i = likelihood_i * P[k+1]
    else:
        likelihood_i = likelihood_i * I_minus_P[k+1]
        
# Include "never seen again" probability v
likelihood_i = likelihood_i * v_term

# Total likelihood
L = product over all individuals of likelihood_i
```

**Parameter Index Matrices (PIMs) in MARK**:
```
# For each state and group, define triangular matrices
# Rows = age, Columns = time
# Example: constant parameter across age and time
PIM_survival_state1 = matrix(1, nrow=(K-1), ncol=(K-2)/2)

# Time-dependent only
PIM_survival_state1[,] = 1:(K-1)

# Age and time dependent
PIM_survival_state1 = create_triangular_indices()
```

**Multisite Recruitment Model Structure**:
```
# Define states: A, B, C (breeders), a, b, c (non-breeders)
# Transition matrix for age k to k+1
if k == 0:  # First year
    W = block_matrix([[B * diag(A_1), B],
                      [N * diag(A_1), zeros(3,3)]])
elif k < age_full_recruitment:
    W = block_matrix([[B * diag(A_k), B],
                      [zeros(3,3) * diag(A_k), zeros(3,3)]])
else:  # Full recruitment
    W = block_matrix([[B, B],
                      [zeros(3,3), zeros(3,3)]])

# Capture probability vector
p = [p_A, p_B, p_C, 0, 0, 0]  # Non-breeders not detectable
```

**Profile Deviance for Identifiability Check**:
```
# Fix focal parameter at range of values
focal_param_values = seq(0, 1, by=0.01)
profile_deviance = vector(length=length(focal_param_values))

for i in 1:length(focal_param_values):
    # Fix focal parameter
    fixed_params = list(focal = focal_param_values[i])
    # Optimize all other parameters
    fit = optimize_likelihood(data, fixed_params)
    profile_deviance[i] = fit$deviance

# Plot: flat line indicates non-identifiability
plot(focal_param_values, profile_deviance)
```

**Software Implementation**: Models fitted using program MARK (White & Burnham 1999), which implements GLM-style constraints via design matrices. Maximum structure for variation: group × time × age for each parameter (φ, c, p). MSSURVIV (Brownie et al. 1993) available for more refined models. Matlab implementations developed (Almeras 1996).

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

1. **Dispersal Management**: Estimates of natal dispersal matrix **N** and breeding dispersal matrix **B** quantify exchange rates between sites/colonies. Site fidelity (diagonal elements c_iik) informs metapopulation connectivity. For [[Roseate Tern]], Site A showed lowest philopatry (0.582 natal, 0.885 breeding) coinciding with population decline, suggesting emigration response to local conditions.

2. **Recruitment Dynamics**: Age-specific breeding probabilities a_ik converted to cumulative proportions of breeders inform population projection models. Full recruitment age (age 5 in [[Roseate Tern]]) defines demographic transition to adult stage. Little site variation in recruitment rates suggests intrinsic rather than site-specific constraints.

3. **Survival Estimation with Heterogeneous Capture**: When capture probability varies by state (e.g., breeders vs. non-breeders), multistate models remove heterogeneity bias in survival estimates compared to pooled single-site analysis. Assumption of equal survival for breeders and non-breeders (conditional on state) is critical for identifiability.

4. **Trade-off Studies**: Defining states by reproductive success (breeder/non-breeder) provides framework for testing cost-of-reproduction hypotheses. Studies in [[Black-legged Kittiwake]] (Cam et al. 1998) and [[Greater Flamingo]] (Tavecchia 1997) found breeders at time t had higher probability of breeding at t+1, suggesting individual quality effects may mask trade-offs in non-manipulative studies.

5. **Closed Population Size Estimation**: Multistate framework with capture-probability states could improve population size estimation by modeling heterogeneity. Relevant when states related to capturability can be defined.

6. **Longitudinal Health Studies**: Reanalysis of obesity data (Fitzmaurice et al. 1994) demonstrates transition probabilities (Pr(Obese|Non-Obese) = 0.27) provide direct insight into process dynamics. Missing data mechanism (MAR vs. MCAR) assessed via state-dependent capture probability.

7. **Population Growth Rate**: Multistate generalization of Pradel (1996) growth rate model estimates seniority matrices **C**_i+1 (backward analysis) and survival-transition matrices **U**_i (forward analysis). Population size vectors related as **N**_i+1 = **K**_i × **N**_i where **K**_i = **C**^(-1)_i+1 × **U**_i. Spectral analysis of **K**_i matrices under various assumptions (constant, random time effects) links to matrix population models.

8. **Robust Design Integration**: Combining multistate models with robust design (primary and secondary occasions) improves precision and allows closure-based abundance estimation within primary periods while modeling open-population dynamics between periods.

**Management Implications**: The framework enables simultaneous estimation of multiple demographic rates (survival, dispersal, recruitment) from a single dataset, improving efficiency and biological realism. Critical for metapopulation management where connectivity and local dynamics interact. Identifiability constraints and goodness-of-fit limitations require careful model building, starting from simple models and adding complexity incrementally (step-up approach) until adequate goodness-of-fit tools are developed.