---
species: ["Southern Bluefin Tuna (Thunnus maccoyii)", "White Shark (Carcharodon carcharias)", "Antarctic Blue Whale (Balaenoptera musculus intermedia)"]
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: ["marine", "riverine"]
ocean_basin: ["Southern Ocean", "Pacific Ocean"]
location: ["Eastern Australia", "New Zealand", "Antarctic"]
tags: ["close-kin mark-recapture", "CKMR", "population genetics", "kinship inference", "pseudo-likelihood", "parent-offspring pairs", "half-sibling pairs", "abundance estimation", "demographic parameters"]
analytical_category: ["abundance estimation", "demographic parameter estimation", "kinship probability modeling", "pseudo-likelihood inference", "experimental design"]
model_framework: "pseudo-likelihood based on pairwise kinship comparisons; approximates full likelihood under sparse sampling"
software_environment: ["R", "automatic differentiation tools"]
data_requirements: ["genetic samples (DNA)", "individual covariates (age, length, sex, capture time/location)", "sparse sampling: n = O(N^1/2)", "minimum 50-100 kin-pairs for ~15% CV", "microsatellite or SNP markers"]
key_assumptions: ["Hardy-Weinberg equilibrium", "no linkage disequilibrium (LD) for unlinked markers", "sparse sampling of large populations", "independence of adult sampling from offspring number (conditional on covariates)", "no unmodelled heterogeneity in capture probability affecting reproductive output", "random mating (for half-sibling inference)", "negligible mutation rates over study timescale"]
keywords_stubs: ["#CKMR", "#kinship_probability", "#pseudo_likelihood", "#parent_offspring", "#half_sibling", "#Fisher_information", "#genotyping_error", "#SNP_markers", "#microsatellites", "#identity_by_descent", "#sparse_sampling", "#experimental_design", "#abundance_CV", "#fecundity_at_age", "#survival_probability", "#sampling_probability"]
title: "Close-Kin Mark-Recapture"
source_id: "X-4bfd2027"
doc_type: "analyses_and_modeling"
source_citation: "M. V. Bravington, H. J. Skaug, E. C. Anderson (2016). Close-Kin Mark-Recapture. Statistical Science 31(2): 259-274."
doi: "10.1214/16-sts552"
source_file: "CloseKinMarkRecapture.pdf"
text_extraction: "text"
---
# Close-Kin Mark-Recapture

#ichthyology #population_genetics #CKMR #statistical_methods

## Analytical Objective & Scope

**Core Problem Addressed**: Estimating adult abundance and demographic parameters (survival φ, fecundity β, population size N) in wildlife populations by generalizing mark-recapture from "recapture of self" to "recapture of closely-related kin" (parent-offspring, half-siblings) identified through genetic markers. This enables abundance estimation using only dead animals (e.g., commercial fisheries, bycatch, hunting) where live-release tagging is impractical or impossible.

**Methodological Classification**: Novel method extending classical Jolly-Seber mark-recapture framework by incorporating close-kin information from DNA samples. The approach uses pseudo-likelihood based on pairwise kinship comparisons rather than individual capture histories, with explicit formulae for kinship probabilities as functions of demographic parameters and individual covariates.

## Mathematical & Statistical Framework

**Model Formulation**: The pseudo-likelihood for parameters θ = (N, φ, β, p) is constructed from pairwise comparisons:

$$l_P(\theta) = \sum_{1 \leq i < j \leq n} \log P(K_{ij} = k_{ij} | z_i, z_j; \theta)$$

where $K_{ij}$ is the kinship category (MO = mother-offspring, HS = half-sibling, U = unrelated), $z_i$ and $z_j$ are covariate vectors (age, length, sex, capture time/location), and $k_{ij}$ is the observed kinship. An alternative form adds marginal likelihood of covariates:

$$l_P(\theta) = \sum_{1 \leq i < j \leq n} \log P(K_{ij} = k_{ij} | z_i, z_j; \theta) + \sum_{i=1}^n \log P(z_i; \theta)$$

**Mother-Offspring Kinship Probability** (base case, ages known, constant fecundity, lethal sampling):

$$P[K_{ij} = \text{MO} | z_i, z_j] = \frac{I[y_i + \alpha \leq y_j < t_i]}{N_{y_j}}$$

where $y_i$ = birth year of i, $y_j$ = birth year of j, $t_i$ = capture time of i, $\alpha$ = age at maturity, $N_{y_j}$ = adult female population size at $y_j$. The indicator function ensures i was alive and mature when j was born.

**Age-Dependent Fecundity Extension**:

$$P[K_{ij} = \text{MO} | z_i, z_j] = I[y_j < t_i] \times \frac{\beta(a_i - (t_i - y_j))}{\sum_{a \geq \alpha} \beta(a) N_{ay_j}}$$

where $\beta(a)$ = fecundity at age a, $N_{ay_j}$ = number of females aged a at time $y_j$.

**Half-Sibling Kinship Probability** (base case, constant fecundity/mortality):

$$P[K_{ij} = \text{MHS} | y_i, y_j] = \frac{\phi(y_i, y_j)}{N_{y_j}}$$

where $\phi(y_i, y_j)$ = probability mother survives from $y_i$ to $y_j$ (assumes $y_i < y_j$).

**General Kinship Framework**: Expected relative reproductive output determines kinship probability:

$$P[K_{ij} = \text{MO} | z_i, z_j] = E_{Y_j, X_j | z_j} \left[ \frac{E[R_i(X_j, Y_j) | z_i]}{E[R^+(X_j, Y_j)]} \right]$$

where $R_i(x,y)$ = reproductive output of i at place x and time y, $R^+(x,y)$ = total reproductive output of all adults.

**Variables & Covariates**:
- **Response**: Kinship category $K_{ij}$ (observed or latent); genetic data $(g_i, g_j)$ when kinship is latent
- **Predictors**: Individual covariates $z = (t, a, \ell, x, \text{sex})$ where t = capture time, a = age, ℓ = length, x = location
- **Latent Variables**: Year of birth y, place of birth x, reproductive output R, true kinship when genetically uncertain
- **Parameters**: $N_t$ (population size time series), $\phi$ (survival probability, may vary with age/covariates), $\beta$ (per capita birth rate, may vary with age/length), $\alpha$ (age at maturity), p (sampling probability)

**Fit Diagnostics & Metrics**: 
- **Fisher Information Matrix** I(θ) for parameter identifiability and experimental design, computed as per-pair information:
$$I(\theta | z_i, z_j) = -\sum_{k \in \mathcal{K}} \frac{\partial^2 \log P(k | z_i, z_j; \theta)}{\partial \theta^2} P(k | z_i, z_j; \theta)$$
then averaged over covariate distributions.
- **Pseudo-likelihood approximates true likelihood** under sparse sampling when:
$$-E\left[\frac{\partial^2 l_P(\theta)}{\partial \theta^2} \Big|_{\theta = \theta_{\text{true}}}\right] = E\left[\left(\frac{\partial l_P}{\partial \theta}\right)\left(\frac{\partial l_P}{\partial \theta}\right)^\top \Big|_{\theta = \theta_{\text{true}}}\right]$$
- **Convergence**: Unbiased estimating equations ensure consistency: $E_{K,Z}[\partial l_P(\theta; K, Z)/\partial \theta |_{\theta = \theta_{\text{true}}}] = 0$
- **CV lower bound**: Approximately $1/\sqrt{h_{\text{target}}}$ where $h_{\text{target}}$ is number of kin-pairs found (e.g., 15% CV for 50 pairs)
- **Southern Bluefin Tuna results**: 45 parent-offspring pairs from ~38,000,000 comparisons (8000 juveniles × 5000 adults) yielded adult abundance estimate just under 2,000,000 animals

## Data Requirements & Preprocessing

**Input Data Schema**:
- **Genetic samples**: DNA from tissue (lethal or biopsy); quality sufficient for 20-25 microsatellite loci or hundreds-to-thousands of SNP markers depending on kinship type
- **Minimum sample size**: $n_{\text{target}} \approx 10\sqrt{N}$ for short-term PO-only studies (crude rule); more generally $n \sim O(N^{1/2})$ for sparse sampling to yield $O(1)$ precision
- **Expected kin-pairs**: $h_{nN} = cn^2 N^{-1}$ where c depends on design (e.g., c = 1/2 for equal juvenile/adult mix in single-sample PO design); target 50-100 pairs for ~15% CV
- **Marker requirements**: ~40 well-chosen SNPs for self-recapture, several hundred for PO pairs, 1000-few thousand for HS pairs (numbers depend on population/sample size)
- **Zero-inflation**: Not applicable; response is kinship category, not count
- **Missing data**: Age may be unmeasured (requires integration over age distribution weighted by sampling probability p(a)); length-at-age distributions f(ℓ|a,y) needed when fecundity/sampling depend on length
- **Covariate requirements**: 
  - Essential: Capture time $t_i$ (always known)
  - Highly valuable: Age $a_i$ (from hard parts, length-age relationships, or future epigenetic methods); enables time-of-marking inference
  - Important when relevant: Length ℓ (for fecundity/selectivity in teleosts), sex (for sex-specific demography), location x (for stock structure)
- **Genotyping error**: Accommodated via $P[g^*_l | g_l]$ (probability of recorded genotype $g^*$ given true genotype g); estimated from multiply-genotyped individuals or related pairs
- **False positive/negative rates**: Likelihood ratio $\Lambda_k(i,j) = P[g^{(i)*}, g^{(j)*} | K_{ij} = k] / (P[g^{(i)*}] P[g^{(j)*}])$ used to set threshold $\Lambda^*_k$ such that false positives from unrelated pairs are <1% of observed pairs; false negative rate $\psi^-_k$ estimated and incorporated into modified kinship probabilities

**Sampling Cross-References**: #sampling_design #stratified_sampling #sparse_sampling #lethal_sampling #biopsy_sampling #age_structured_sampling #juvenile_sampling #adult_sampling #commercial_fishery_sampling #bycatch_sampling #sample_size_determination #Fisher_information_design #optimal_allocation

## Code Logic

**Kinship Probability Calculation** (conceptual pseudocode for base MO case):
```
function P_MO(i, j, N_vector, alpha):
    y_i = t_i - a_i  # birth year of i
    y_j = t_j - a_j  # birth year of j
    
    # Check if i could be j's mother
    if (y_i + alpha <= y_j) and (y_j < t_i):
        return 1 / N_vector[y_j]  # N at j's birth year
    else:
        return 0
```

**Pseudo-Likelihood Evaluation** (conceptual):
```
function pseudo_likelihood(theta, data):
    log_lik = 0
    
    # Pairwise comparisons
    for i in 1:(n-1):
        for j in (i+1):n:
            # Calculate kinship probabilities for all categories
            P_MO_ij = kinship_prob_MO(i, j, theta)
            P_HS_ij = kinship_prob_HS(i, j, theta)
            P_U_ij = 1 - P_MO_ij - P_HS_ij  # Unrelated
            
            # Add log probability of observed kinship
            if k_ij == "MO":
                log_lik += log(P_MO_ij)
            else if k_ij == "HS":
                log_lik += log(P_HS_ij)
            else:  # Unrelated
                log_lik += log(P_U_ij)
    
    # Optional: add marginal likelihood of covariates
    for i in 1:n:
        log_lik += log_prob_covariates(z_i, theta)
    
    return log_lik
```

**Genetic Kinship Inference** (likelihood ratio approach):
```
function identify_kin(g_i, g_j, allele_freqs, error_model, threshold):
    # Calculate likelihood ratio for each kinship type
    Lambda_PO = P(g_i, g_j | K="PO", error_model) / 
                (P(g_i | allele_freqs) * P(g_j | allele_freqs))
    Lambda_HS = P(g_i, g_j | K="HS", error_model) / 
                (P(g_i | allele_freqs) * P(g_j | allele_freqs))
    
    # Classify based on thresholds (set to control false positive rate)
    if Lambda_PO > threshold_PO:
        return "PO"
    else if Lambda_HS > threshold_HS:
        return "HS"
    else:
        return "U"  # Unrelated
```

**Joint Genotype Probability** (for unlinked markers):
```
function P_genotype_pair(g_i, g_j, kinship, allele_freqs):
    # Identity-by-descent probabilities for kinship type
    kappa = get_ibd_probs(kinship)  # (kappa_0, kappa_1, kappa_2)
    
    prob = 1
    for l in 1:L:  # Loop over loci
        # Single-locus probability from equation (5.1)
        P_l = kappa[0] * P(g_i[l]) * P(g_j[l]) +
              kappa[1] * P(g_i[l], g_j[l] | K="PO") +
              kappa[2] * P(g_i[l]) * I(g_i[l] == g_j[l])
        prob *= P_l
    
    return prob
```

**Latent Kinship Approach** (alternative to classification):
```
function pseudo_likelihood_latent(theta, genetic_data, covariates):
    log_lik = 0
    
    for i in 1:(n-1):
        for j in (i+1):n:
            # Sum over all possible kinship categories
            P_total = 0
            for k in kinship_categories:
                P_genetic = P(g_i, g_j | K=k)  # From genetics
                P_prior = kinship_prob(k, z_i, z_j, theta)  # From demography
                P_total += P_genetic * P_prior
            
            log_lik += log(P_total)
    
    return log_lik
```

**Aggregation for Computational Efficiency** (when using classification):
```
function aggregate_comparisons(data):
    # Group pairs with identical (z_i, z_j) and kinship
    classes = {}
    
    for each pair (i,j):
        key = (z_i, z_j, k_ij)
        if key in classes:
            classes[key] += 1
        else:
            classes[key] = 1
    
    # Pseudo-likelihood becomes sum over classes
    log_lik = 0
    for key, count in classes:
        P_k = kinship_prob(key.kinship, key.z_i, key.z_j, theta)
        log_lik += count * log(P_k)  # Binomial contribution
    
    return log_lik
```

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

**Abundance Estimation**: Adult population size N (or time series $N_t$) estimated directly from observed number of kin-pairs H and kinship probabilities. For simple single-sample PO design: $\hat{N}_A = 2n_J n_A / H$ where $n_J$ = juvenile samples, $n_A$ = adult samples. More complex models yield time-series of abundance accounting for mortality, recruitment variability, and age/size structure.

**Demographic Parameters**: 
- **Adult survival** φ estimated from time-lag between parent and offspring sampling (PO pairs) or between half-sibling birth years (HS pairs); inversely related to average recapture time
- **Fecundity** β (age- or size-specific) estimated from relative reproductive output in kinship probabilities; particularly important in teleosts where growth continues after maturity
- **Age at maturity** α may be estimable if sufficient age data available across life stages

**Reference Points & Status**: 
- [[Southern Bluefin Tuna]]: CKMR yielded adult abundance ~2,000,000 (adopted into management), indicating stock at ~5% of pre-exploitation biomass in mid-2000s; ongoing monitoring for recovery assessment
- [[White