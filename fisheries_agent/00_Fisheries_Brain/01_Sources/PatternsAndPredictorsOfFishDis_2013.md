---
species:
  - Brown Trout (Salmo trutta)
  - Brook Trout (Salvelinus fontinalis)
  - Cutthroat Trout (Oncorhynchus clarkii)
  - Largemouth Bass (Micropterus salmoides)
  - Smallmouth Bass (Micropterus dolomieu)
  - Northern Pike (Esox lucius)
  - European Perch (Perca fluviatilis)
  - Roach (Rutilus rutilus)
  - Mottled Sculpin (Cottus bairdi)
  - Bullhead (Cottus gobio)
  - Barbus barbus
  - Fundulus heteroclitus
  - Fundulus notatus
  - Fundulus olivaceus
  - Leuciscus idus
  - Leuciscus leuciscus
  - Alburnus alburnus
  - Abramis brama
  - Tinca tinca
  - Etheostoma nigrum
  - Etheostoma flabellare
  - Percina rex
  - Oncorhynchus masou rhodurus
  - Salvelinus leucomaenis
  - Thymallus thymallus
  - Cottus pollux
  - Cottus rhenanus
target_species: "N/A"
common_name: Multiple freshwater fish species
family:
  - Salmonidae
  - Cyprinidae
  - Centrarchidae
  - Esocidae
  - Percidae
  - Cottidae
  - Fundulidae
  - Ictaluridae
  - Catostomidae
habitat: Rivers and streams
ocean_basin: N/A
location: Global (16 countries, 5 continents)
tags:
  - meta-analysis
  - dispersal modeling
  - movement ecology
  - leptokurtic kernels
  - population dynamics
  - river rehabilitation
analytical_category:
  - meta-analysis
  - dispersal kernel fitting
  - multiple regression
  - mixed-effects modeling
  - regression trees
model_framework: Leptokurtic dispersal kernel (superimposed normal distributions)
software_environment:
  - R
  - Python
  - SciPy
data_requirements:
  - Mark-recapture or telemetry data
  - Minimum three distance classes
  - Fish recapture/detection frequencies per distance class
  - Fish morphometry (length, aspect ratio)
  - Stream characteristics (order, width, discharge)
  - Study duration
key_assumptions:
  - Fish populations consist of stationary and mobile components
  - Movement is heterogeneous and leptokurtic
  - Upstream and downstream movements are symmetrical
  - Movement distance increases with time
  - No directional bias in dispersal
keywords_stubs:
  - #dispersal_kernel
  - #movement_distance
  - #stationary_component
  - #mobile_component
  - #fish_morphometry
  - #stream_size
  - #aspect_ratio
  - #home_range
  - #metapopulation
  - #recolonization
  - #habitat_connectivity
title: "Patterns and predictors of fish dispersal in rivers"
source_id: "X-297a7aaa"
doc_type: "analyses_and_modeling"
source_citation: "J. Radinger, C. Wolter (2013). Patterns and predictors of fish dispersal in rivers. Fish and Fisheries 15(3): 456-473."
doi: "10.1111/faf.12028"
source_file: "Patterns and predictors of fish dispersal in Rivers (Radinger and Wolter 2013).pdf"
text_extraction: "text"
---
# Patterns and Predictors of Fish Dispersal in Rivers

#ichthyology #multi-family #movement-ecology #meta-analysis

## Analytical Objective & Scope

**Core Problem Addressed**: Quantifying fish dispersal distances and identifying general predictors of movement patterns across freshwater fish species to inform population dynamics, recolonization potential, and recovery time predictions following environmental changes or habitat restoration.

**Methodological Classification**: Novel comprehensive meta-analysis applying leptokurtic dispersal kernel fitting to heterogeneous movement data. This study extends previous salmonid-focused analyses (Rodríguez 2002) to 62 species across 12 families, developing predictive regression models for dispersal parameters based on morphological, environmental, and temporal covariates. The approach represents an adaptation of existing dispersal kernel theory to a broad taxonomic scope with standardized parameter extraction from diverse empirical studies.

## Mathematical & Statistical Framework

**Model Formulation**: The leptokurtic dispersal kernel consists of two superimposed normal distributions describing the probability of occurrence of an individual as a function of distance (x) from the source population:

F(x) = p · (1/√(2πσ²stat)) · e^(-(x-μ)²/(2σ²stat)) + (1-p) · (1/√(2πσ²mob)) · e^(-(x-μ)²/(2σ²mob))

where σstat = mean movement distance of the stationary component (m), σmob = mean movement distance of the mobile component (m), p = share of the stationary component on the total population (proportion), and μ = mean displacement (set to zero for simplicity, assuming no directional bias).

**Variables & Covariates**:
- **Response variables**: log(σstat), log(σmob), p
- **Predictors**: Fish length (L, mm; log-transformed), aspect ratio of caudal fin (AR), stream order (SO, Strahler classification; square-root transformed), discharge (D, m³ s⁻¹; log-transformed), stream width (W, m; log-transformed), study duration (T, days; log-transformed)
- **Random effects** (mixed models): Taxonomic family, species nested within family, study method (mark-recapture, telemetry, traps), individual study
- **Categorical factors**: Taxonomic family (12 families), study method (3 types)

**Fit Diagnostics & Metrics**: 
- Dispersal kernels fitted using least-squares optimization (SciPy optimize package) with equations as fitting conditions rather than data points alone
- Relative errors in sum of squares < 1.49012 × 10⁻⁸ for all fitted solutions
- Multiple regression models: Adjusted R² = 0.62–0.65 for σstat models, 0.76–0.78 for σmob models
- AIC values: 84.83–91.31 (σstat), 37.31–42.62 (σmob)
- Mixed-effects models: AIC based on log-likelihood = 331.62–368.61 (σstat), 285.99–316.12 (σmob)
- Single predictor regressions: R² = 0.07–0.46 (P < 0.01 for all)
- Regression trees: Relative error (1 - R²) = 0.89 (σstat), 0.61 (σmob)
- Pearson correlation between σstat and σmob: r = 0.91 (P < 0.001)
- ANCOVA with post hoc Tukey HSD tests for family and method effects
- Subsample approach (999 replicates) to eliminate pseudo-replication bias

## Data Requirements & Preprocessing

**Input Data Schema**: 
- **Minimum sample size**: 160 data sets from 71 studies covering 62 species
- **Distance classes**: Minimum three distance classes with recapture/detection frequencies or percentages
- **Zero-inflation**: Not explicitly addressed; studies with insufficient recaptures excluded
- **Missing data**: Fish length imputed from FishBase common length when not reported (n = 42 of 160); stream characteristics obtained from cited sources, authors, or hydrological agencies; aspect ratio extracted from FishBase for all species
- **Data transformations**: Log transformation of response variables; Box-Cox tests determined predictor transformations (log or square root)
- **Exclusion criteria**: Studies of obligatory spawning migrations excluded; data sets with non-converging parameter estimates excluded
- **Temporal range**: Study durations 0.25–3285 days (median = 150.5 days)
- **Spatial range**: Stream orders 1–9 (median = 3); discharge 0.1–250 m³ s⁻¹ (median = 1.4); width 1–250 m (median = 6.9 m)
- **Fish size range**: Total length 39–810 mm (median = 192.5 mm)
- **Aspect ratio range**: 0.51–2.29 (median = 1.43)

**Sampling Cross-References**: Studies employed three experimental designs: #mark_recapture (n = 119), #telemetry (n = 31), #traps (n = 10). No significant effect of study method detected on movement parameters (ANCOVA F₃,₇₀ = 1.52 for σstat, 1.47 for σmob; P > 0.1). Data extracted from peer-reviewed literature and grey literature using ISI Web of Knowledge, Scopus, Google Scholar. See #movement_study_design, #capture_recapture_methods, #radio_telemetry, #fish_trapping.

## Code Logic

**Dispersal Kernel Fitting** (Python/SciPy):
```python
# Pseudocode for leptokurtic kernel fitting
from scipy.optimize import least_squares

def dispersal_kernel(x, sigma_stat, sigma_mob, p):
    """Two-component normal distribution"""
    mu = 0  # No directional bias
    stationary = p * (1/sqrt(2*pi*sigma_stat**2)) * exp(-(x-mu)**2 / (2*sigma_stat**2))
    mobile = (1-p) * (1/sqrt(2*pi*sigma_mob**2)) * exp(-(x-mu)**2 / (2*sigma_mob**2))
    return stationary + mobile

def fit_kernel(distance_classes, recapture_percentages):
    """Fit kernel using cumulative percentages as conditions"""
    # Define equations relating cumulative % to area under curve
    # Minimize errors in conditional equations
    result = least_squares(objective_function, initial_params, 
                          bounds=([0,0,0], [inf,inf,1]))
    return result.x  # Returns [sigma_stat, sigma_mob, p]
```

**Multiple Regression Model** (R):
```r
# Four-parameter model (best for sigma_stat with stream order)
model_stat <- lm(log(sigma_stat) ~ log(L) + AR + sqrt(SO) + log(T), 
                 data = fish_data)

# Six-parameter model (best for sigma_mob with all stream size proxies)
model_mob <- lm(log(sigma_mob) ~ log(L) + AR + sqrt(SO) + log(D) + log(W) + log(T),
                data = fish_data)

# Subsample approach to eliminate pseudo-replication
results <- replicate(999, {
  subsample <- fish_data %>% 
    group_by(species, study_reach) %>% 
    sample_n(1)
  lm(log(sigma_mob) ~ predictors, data = subsample)
})
mean_R2 <- mean(sapply(results, function(m) summary(m)$r.squared))
```

**Mixed-Effects Model** (R/lme4):
```r
library(lme4)

# Random effects: family, species within family, method, study
mixed_model <- lmer(log(sigma_mob) ~ log(L) + AR + sqrt(SO) + log(T) +
                    (1|family) + (1|species:family) + (1|method) + (1|study),
                    data = fish_data)

# Extract variance components
random_effects_variance <- VarCorr(mixed_model)
```

**Regression Tree** (R/rpart):
```r
library(rpart)

# Initial tree with all predictors
tree_mob <- rpart(log(sigma_mob) ~ log(L) + AR + sqrt(SO) + log(D) + log(W) + log(T),
                  data = fish_data)

# Prune to minimize cross-validated error
pruned_tree <- prune(tree_mob, cp = tree_mob$cptable[which.min(tree_mob$cptable[,"xerror"]),"CP"])
```

**R Package 'FISHMOVE'**: Developed to predict dispersal parameters from input variables (fish length, aspect ratio, stream order, time). Package calculates σstat, σmob, and p based on multiple regression coefficients. Available from CRAN repository (see Data S2 for documentation).

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

**Recolonization Time Estimation**: The mobile component (median 30% of population) determines successful dispersal to restored habitats. Using the 50/500 rule (minimum 50 spawners or 500 adults for viable populations), successful recolonization requires ≥150 individuals in the founder population to ensure 50 mobile spawners reach the target with probability = 1. Time lags between rehabilitation and fish response can be estimated from dispersal kernels given distance to nearest source population.

**Movement Distance Predictions**: Median movement distances: σstat = 36.4 m, σmob = 361.7 m. The mobile component moves 13.67 times farther than stationary component (median; IQR 7.78–28.33). Ratio between components is remarkably constant across species and families. Movement distances increase with: (1) fish length (R² = 0.44–0.46), (2) stream size (stream order R² = 0.25–0.34), (3) aspect ratio (R² = 0.07–0.09), (4) study duration (R² = 0.17–0.22).

**Species-Specific Patterns**: [[Cyprinidae]] and [[Fundulidae]] show elevated dispersal distances; [[Cottidae]] show reduced movement (negative residuals), consistent with limited swimming ability of small benthic species. Salmonids, cyprinids, and centrarchids represent 56, 31, and 25 data sets respectively. Family effects significant for both σstat (F₈,₇₀ = 2.38, P < 0.05) and σmob (F₈,₇₀ = 2.75, P < 0.05).

**Habitat Connectivity Implications**: Dispersal kernels can be proportionally truncated to account for barrier passage success, enabling quantitative assessment of fragmentation effects. Applications include: (1) predicting minimum effective size of founder populations for species recovery, (2) estimating time lags in fish response to river rehabilitation based on distance and size of source populations, (3) assessing invasion potential and faunal homogenization by exotic species, (4) predicting range shift rates in response to climate change given available migration corridors.

**Management Reference Points**: The share of stationary individuals (median p = 66.6%, range 13.3–97.6%) was high but unrelated to movement distance. No conclusive predictors found for p except weak relation with body size. High variation in p suggests habitat structure and complexity (not captured by stream type) may influence exploratory behavior and mobility.

**Rejection of Restricted Movement Paradigm**: Results fundamentally challenge Gerking's (1959) "restricted movement paradigm." All populations contain mobile components; fish assemblages constantly experience emigration and immigration at large spatial scales. The concept of static "home range" may not be applicable given time-dependent movement increases. Movement distances increase linearly with time for both stationary and mobile components, contrasting with static home range theory.

**Model Applications**: Leptokurtic dispersal kernels suitable for implementation in individual-based models and species distribution models in dendritic river networks. Kernels provide probabilities of long-distance dispersal (tail probabilities) for given time steps. Example predictions for [[Brown Trout]] (Salmo trutta) show dispersal distances varying with fish size (200–600 mm), stream order (1–5), and time interval (30–365 days).

**Key Biological Correlates**: #fish_length (strongest predictor, asymptotic above 42.5 cm), #swimming_performance (aspect ratio proxy for locomotion mode and metabolism), #stream_size (larger rivers support faster recolonization), #temporal_dynamics (movement increases with √time), #heterogeneous_populations, #leptokurtic_distribution, #metapopulation_dynamics, #gene_flow, #colonization_potential, #habitat_fragmentation, #barrier_effects, #river_rehabilitation, #climate_change_response, #invasion_ecology, #species_conservation