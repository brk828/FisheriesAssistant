---
species:
  - Cyprinus carpio
  - Chasmistes liorus
target_species: "Common Carp (Cyprinus carpio)"
common_name: "Common Carp"
family: "Cyprinidae"
habitat: "Shallow lake, littoral and pelagic zones"
ocean_basin: "N/A"
location: "Utah Lake, Utah, USA"
tags:
  - invasive species control
  - population modeling
  - adaptive management
  - gear selectivity
analytical_category:
  - age-structured population model
  - integrated population model
  - stock-recruitment analysis
  - simulation modeling
model_framework: "Bayesian hierarchical age-structured integrated population model with Ricker stock-recruitment dynamics"
software_environment:
  - JAGS
  - AD Model Builder
  - R
data_requirements:
  - commercial harvest biomass (monthly, 2009-2018)
  - fishing effort (seine hauls, 2013-2018)
  - standardized seine survey catch (annual, 2012-2018)
  - length-at-age data from dorsal spines (n=166)
  - lake surface area time-series
  - weight-at-age estimates
key_assumptions:
  - constant annual natural mortality across all ages
  - Ricker stock-recruitment relationship
  - recruitment influenced by spawning biomass and lake area
  - age-3 maturity threshold
  - gear selectivity increases with age
  - plus-age group (7+) fully recruited to gear
  - age-0 individuals have zero selectivity
keywords_stubs:
  - "#compensatory_recruitment"
  - "#gear_selectivity"
  - "#density_dependence"
  - "#habitat_dynamics"
  - "#drought_effects"
  - "#lake_level_fluctuation"
  - "#eradication_feasibility"
  - "#management_scenarios"
  - "#June_sucker_recovery"
  - "#submerged_aquatic_vegetation"
title: "Compensatory recruitment, dynamic habitat, and selective gear present challenges to large‐scale invasive species control"
source_id: "X-a514c7e4"
doc_type: "analyses_and_modeling"
source_citation: "T. E. Walsworth, K. Landom, J. W. Gaeta (2020). Compensatory recruitment, dynamic habitat, and selective gear present challenges to large‐scale invasive species control. Ecosphere 11(6)."
doi: "10.1002/ecs2.3158"
source_file: "Walsworth 2020 - Carp dynamics Utah Lake.pdf"
text_extraction: "mixed"
---
# Compensatory recruitment, dynamic habitat, and selective gear present challenges to large-scale invasive species control

#ichthyology #Cyprinidae #invasive_species #population_dynamics

## Analytical Objective & Scope

**Core Problem Addressed**: Evaluate the population-level consequences of a decade-long [[Common Carp]] removal effort in [[Utah Lake]] (>12,000 tons harvested 2009-2018) and determine whether current mechanical removal strategies can maintain carp biomass below management targets (75% reduction) given compensatory recruitment, dynamic lake habitat, and age-selective harvest gear.

**Methodological Classification**: Novel application combining an integrated age-structured population model fitted to empirical data with forward simulation experiments to explore alternative management scenarios. The approach adapts standard fisheries stock-assessment methods to invasive species control in a large, dynamic shallow lake ecosystem.

## Mathematical & Statistical Framework

**Model Formulation**:

Age-structured population dynamics (Eq. 2):
- If a=0: N_{a,y} = R_y
- If 0<a<a*: N_{a,y} = (N_{a-1,y-1} - C_{a-1,y-1})(1-m)
- If a=a*: N_{a*,y} = (N_{a*-1,y-1} - C_{a*-1,y-1})(1-m) + (N_{a*,y-1} - C_{a*,y-1})(1-m)

where a* is the plus-age group threshold (age 7+), R_y is recruitment, m is annual natural mortality, C is annual catch.

Ricker stock-recruitment with environmental covariate (Eq. 3):
R_y = αS_y e^(-βS_y + γA_y) e^(ε_y)

where S_y = Σ(N_{a,y}w_a) for a≥a_m (spawning biomass), A_y is centered/scaled lake surface area in August, α is density-independent productivity, β is density-dependent compensation, γ is lake area effect, ε_y ~ N(0, σ_r²).

Harvest dynamics (Eq. 4):
C_{a,y} = N_{a,y}(1 - e^(-s_a qE))

where q is catchability coefficient, E is fishing effort (seine hauls), s_a is gear selectivity on age a.

Von Bertalanffy growth (Eq. 1):
L_{a,i} = L_{∞,i}(1 - e^(-k_i(a-t_{0,i}))) + ε_{a,i}

with hierarchical random effects on individual-level parameters L_{∞,i}, k_i, t_{0,i}.

**Variables & Covariates**:
- **Response variables**: N_{a,y} (abundance-at-age), H_y (harvest biomass), D_{a,y} (density-at-age from surveys)
- **Predictors**: S_y (spawning biomass), A_y (lake area), E (fishing effort)
- **Random effects**: Individual growth parameters (L_∞, k, t_0), recruitment deviations (ε_y)
- **Offsets**: Lake area for density calculations
- **Fixed parameters**: m (natural mortality, informed by FishLife prior), a_m (age-at-maturity = 3), s_0 = 0, s_{7+} = 1

**Fit Diagnostics & Metrics**:
- Convergence: R-hat < 1.1 for all parameters (Gelman-Hill criterion)
- Model fit to standardized density-at-age: R² = 0.838
- Model fit to observed harvest: R² = 0.997
- Likelihood components: harvest (Eq. 6), density-at-age (Eq. 8), plus-age abundance (Eq. 9)
- Parameter estimates (Table 1): q = 7.85×10⁻⁴ (95% CI: 5.85×10⁻⁴ – 1.03×10⁻³), m = 0.423 (0.380–0.471), α = 2.64 (2.56–2.72), β = 7.53×10⁻⁸ (4.16×10⁻⁸ – 1.15×10⁻⁷), γ = 1.37 (1.10–1.68)
- Age composition uncertainty propagated through 1000 stochastic age estimates per individual
- 95% credible intervals reported for all abundance and biomass estimates

## Data Requirements & Preprocessing

**Input Data Schema**:
- **Commercial harvest**: Monthly biomass removed (kg), 2009-2018; fishing effort (seine hauls) 2013-2018, assumed constant 2009-2012 at mean 2013-2015 levels
- **Standardized surveys**: Annual lake-wide seining, 27-43 hauls per August 2012-2018; total carp count per haul, subsample of 30 individuals for length/weight
- **Age-length data**: Dorsal spine ages from 166 individuals (55-793 mm TL, ages 0-19), collected 2016-2017; 77% agreement between two independent readers, 89% for ages ≤6
- **Lake area**: Monthly surface area estimates from Bureau of Reclamation; range ~28,000 ha (low water, Oct 2016) to ~38,000 ha (full pool)
- **Minimum sample size**: Not explicitly stated; standardized surveys varied 27-43 hauls/year due to accessibility constraints during low water
- **Zero-inflation**: Age-0 carp never captured in standardized surveys (estimated probability = 0 from age composition model)
- **Missing data**: Fishing effort 2009-2012 imputed as mean of 2013-2015; seine haul area/duration not recorded

**Sampling Cross-References**:
- [[standardized_seine_survey_design]] – spatially stratified sites around lake circumference, 184 m × 3 m commercial beach seine, 2-inch square mesh
- [[dorsal_spine_aging_protocol]] – processing following Watkins et al. 2015 recommendations
- [[length_at_age_estimation]] – repeated-measures von Bertalanffy in JAGS, 1000 stochastic age draws per individual from multinomial distribution of age probabilities
- [[commercial_harvest_reporting]] – data provided by June Sucker Recovery Implementation Program and Utah Division of Wildlife Resources

## Code Logic

**Age composition model** (JAGS, Bayesian hierarchical von Bertalanffy):
```
# Repeated-measures growth model (Eq. 1)
for(i in 1:n_individuals) {
  log(L_inf[i]) ~ dnorm(mu_Linf, tau_Linf)
  log(k[i]) ~ dnorm(mu_k, tau_k)
  t0[i] ~ dnorm(mu_t0, tau_t0)
  
  for(a in ages[i]) {
    L[a,i] <- L_inf[i] * (1 - exp(-k[i] * (a - t0[i])))
    obs_L[a,i] ~ dnorm(L[a,i], tau_obs)
  }
}

# Stochastic age assignment for unaged fish
for(j in 1:n_unaged) {
  for(a in 0:max_age) {
    # Probability fish of length L_j is age a
    prob_age[a,j] <- dnorm(L_j, L_inf_pop * (1 - exp(-k_pop * (a - t0_pop))), tau_obs)
  }
  # Normalize and sample
  age[j] ~ dmulti(prob_age[,j] / sum(prob_age[,j]), 1000)
}
```

**Integrated population model** (AD Model Builder):
```
// Population dynamics (Eq. 2)
for(int y=1; y<=n_years; y++) {
  N(0,y) = alpha * S(y-1) * exp(-beta * S(y-1) + gamma * A(y-1)) * exp(eps_r(y));
  
  for(int a=1; a<a_plus; a++) {
    N(a,y) = (N(a-1,y-1) - C(a-1,y-1)) * (1 - m);
  }
  
  N(a_plus,y) = (N(a_plus-1,y-1) - C(a_plus-1,y-1)) * (1 - m) 
                + (N(a_plus,y-1) - C(a_plus,y-1)) * (1 - m);
  
  // Harvest (Eq. 4)
  for(int a=0; a<=a_plus; a++) {
    C(a,y) = N(a,y) * (1 - exp(-selectivity(a) * q * effort(y)));
  }
  
  // Spawning biomass (Eq. 3b)
  S(y) = 0;
  for(int a=a_mat; a<=a_plus; a++) {
    S(y) += N(a,y) * weight_at_age(a);
  }
}

// Likelihood components
for(int y=1; y<=n_years; y++) {
  // Harvest (Eq. 6)
  nll_harvest -= dnorm(log(obs_harvest(y)), log(pred_harvest(y)), sigma_h);
  
  // Density-at-age (Eq. 8)
  for(int a=0; a<=a_plus; a++) {
    pred_density(a,y) = N(a,y) / lake_area(y) * (1 - exp(-selectivity(a)));
    nll_density -= dnorm(log(obs_density(a,y)), log(pred_density(a,y)), sigma_d);
  }
  
  // Plus-age abundance (Eq. 9)
  nll_abundance -= dnorm(log(obs_N_plus(y)), log(N(a_plus,y)), sigma_N);
}
```

**Simulation model** (R):
```r
# Stochastic lake area time-series (Eq. 10)
generate_lake_area <- function(n_years, start_year) {
  A_base <- cos(0.436 * (1:720))  # 720-yr series
  A_stoch <- A_base + rnorm(720, 0, 0.25)
  return(A_stoch[start_year:(start_year + n_years - 1)])
}

# Forward simulation
simulate_population <- function(effort_multiplier, selectivity_scenario, n_sims=1000) {
  results <- array(NA, dim=c(n_sims, n_years, n_ages))
  
  for(sim in 1:n_sims) {
    # Initialize
    N <- initial_abundance
    A <- generate_lake_area(n_years, sample(1:620, 1))
    
    for(y in 1:n_years) {
      # Recruitment with stochasticity
      S <- sum(N[a_mat:a_plus] * w)
      R <- alpha * S * exp(-beta * S + gamma * A[y]) * exp(rnorm(1, 0, sigma_r))
      
      # Selectivity by scenario
      if(selectivity_scenario == "current") {
        s <- s_current
      } else if(selectivity_scenario == "reversed") {
        s <- s_reversed
      } else {  # mixed
        s <- 0.5 * s_current + 0.5 * s_reversed
      }
      
      # Harvest and survival
      E <- mean_effort * effort_multiplier
      for(a in 0:a_plus) {
        C[a] <- N[a] * (1 - exp(-s[a] * q * E))
        N_next[a+1] <- (N[a] - C[a]) * (1 - m)
      }
      N_next[0] <- R
      N <- N_next
      
      results[sim, y, ] <- N
    }
  }
  return(results)
}

# Evaluate scenarios
effort_levels <- c(0, 1, 2, 5, 10)  # multiples of mean effort
selectivity_types <- c("current", "reversed", "mixed")

for(effort in effort_levels) {
  for(sel in selectivity_types) {
    sims <- simulate_population(effort, sel)
    # Calculate metrics: biomass < 25% threshold, eradication probability
  }
}
```

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

1. **Population Status Assessment**: Model estimates carp biomass declined from 52.5 M kg (2009) to 14.5 M kg (2018), achieving 72.4% reduction and approaching the 75% management target. However, abundance increased from 15.6 M (2016) to 19.1 M (2018) due to strong recent recruitment (ages 0-2), indicating compensatory response to removal pressure.

2. **Gear Selectivity Constraints**: Current commercial seine gear demonstrates very low selectivity for ages 1-4 (s₁ ≈ 0.1, s₄ ≈ 0.3) and zero selectivity for age-0, likely due to deployment in unvegetated nearshore habitats while juveniles occupy vegetated littoral and pelagic zones. This creates a "refuge" pool of biomass minimally impacted by removals.

3. **Compensatory Recruitment Dynamics**: Strong positive effect of lake area on recruitment (γ = 1.37, 95% CI: 1.10-1.68) indicates that periodic high-water years following drought will drive large cohorts even at reduced spawner biomass. The Ricker α parameter (2.64) suggests high intrinsic productivity, enabling rapid population recovery.

4. **Management Scenario Outcomes**:
   - **Current gear, current effort**: Biomass maintained below 25% threshold in <50% of simulations by 2050; no eradication within 100 years even at 10× effort
   - **Reversed selectivity (hypothetical juvenile-targeting gear), 3× effort**: Maintains low biomass in >90% of simulations; 5× effort achieves eradication in ~50% of simulations by 2100
   - **Mixed selectivity (50/50 current/juvenile gear), 5× effort**: Intermediate outcomes; maintains threshold in ~70% of simulations

5. **Reference Points & Decision Rules**:
   - **Target biomass**: 25% of 2009 levels (13.1 M kg) or 25% of maximum (15.6 M kg), associated with increased [[Submerged Aquatic Vegetation]] and [[June Sucker]] habitat
   - **Critical threshold**: Current gear cannot maintain target even at 10× effort due to selectivity limitations
   - **Minimum effective effort**: 3× current levels with juvenile-targeting gear required for >50% probability of maintaining low biomass
   - **Eradication feasibility**: Requires ≥7× effort with juvenile gear sustained for decades; not achievable with current gear at any examined effort level

6. **Adaptive Management Recommendations**: 
   - Develop alternative gears targeting ages 0-4 (e.g., variable mesh gill nets in pelagic habitats, seines in vegetated zones)
   - Intensify removals during drought periods when recruitment is naturally suppressed (low lake area)
   - Monitor age structure annually to detect compensatory recruitment signals
   - Consider non-mechanical alternatives (YY-technology, carp herpes virus) given high costs of mechanical eradication
   - Explicitly evaluate trade-offs between carp control costs and multiple ecosystem goals ([[June Sucker]] recovery, vegetation restoration, water quality)

7. **Uncertainty & Monitoring Needs**: High uncertainty in recruitment at low spawner biomass (no observations <20 M kg); continued monitoring critical to refine stock-recruitment relationship. Lake level fluctuations introduce stochastic variation in recruitment success,