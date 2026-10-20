---
species:
  - Balistes capriscus
target_species: "Gray Triggerfish (Balistes capriscus)"
common_name: Gray Triggerfish
family: Balistidae
habitat: Natural and artificial reefs, continental shelf
ocean_basin: Gulf of Mexico
location: Northern Gulf of Mexico, Eastern Gulf of Mexico (West Florida Shelf), Western Gulf of Mexico (Texas coast)
tags:
  - age_and_growth
  - von_Bertalanffy
  - Bayesian_hierarchical_model
  - ageing_error
  - sexual_dimorphism
  - stock_assessment
analytical_category:
  - Bayesian hierarchical modeling
  - von Bertalanffy growth model
  - multi-reader age estimation
  - sex-specific growth comparison
  - ageing protocol comparison
model_framework: Bayesian hierarchical von Bertalanffy growth model with location-scale T distribution for ageing error
software_environment:
  - R
  - STAN
  - cmdstanr
  - bayestestR
data_requirements:
  - Fork length measurements (mm)
  - Age estimates from multiple readers (n=3)
  - Multiple ageing structures (otoliths, dorsal spines)
  - Sex determination
  - Fractional age for age-0 fish
  - Minimum sample sizes: 1182 otoliths, 1219 new spine, 1243 old spine
key_assumptions:
  - Annual periodicity of growth zone formation
  - Log-normal process error in length-at-age
  - Location-scale T distribution for between-reader variability
  - Shared L0 (size at birth) across protocols and sexes
  - Weakly informative priors derived from maximum likelihood estimates
keywords_stubs:
  - "#von_Bertalanffy"
  - "#Bayesian_growth_model"
  - "#ageing_error"
  - "#sexual_dimorphism"
  - "#multiple_readers"
  - "#otolith_ageing"
  - "#dorsal_spine_ageing"
  - "#stock_assessment_implications"
  - "#Gulf_of_Mexico"
  - "#Balistidae"
title: "Bayesian estimation of von Bertalanffy growth parameters for gray triggerfish, Balistes capriscus, incorporating multiple readers and ageing structures"
source_id: "X-08f59426"
doc_type: "analyses_and_modeling"
source_citation: "D. W. Chamberlin, Z. A. Siders, J. C. Potts, W. D. Rogers, M. A. Taylor, W. F. Patterson (2025). Bayesian estimation of von Bertalanffy growth parameters for gray triggerfish, Balistes capriscus, incorporating multiple readers and ageing structures. Canadian Journal of Fisheries and Aquatic Sciences 82: 1-12."
doi: "10.1139/cjfas-2024-0315"
source_file: "bayesian-estimation-of-von-bertalanffy-growth-parameters-for-gray-triggerfish-balistes-capriscus-incorporating-multiple.pdf"
text_extraction: "text"
---
# Bayesian estimation of von Bertalanffy growth parameters for gray triggerfish, Balistes capriscus, incorporating multiple readers and ageing structures

#ichthyology #Balistidae #von_Bertalanffy #Bayesian_hierarchical_model #ageing_error #sexual_dimorphism

## Analytical Objective & Scope

**Core Problem Addressed:** Accurate estimation of [[Gray Triggerfish]] growth parameters while accounting for ageing error from multiple readers and comparing three ageing protocols (whole otoliths, new dorsal spine protocol, old dorsal spine protocol). The study addresses how biased age estimates from the historical [[Kolmos et al. 2013]] dorsal spine protocol affect growth parameter estimates used in [[Gulf of Mexico]] stock assessments.

**Methodological Classification:** Adaptation of an existing model. The authors developed a sex-specific Bayesian hierarchical formulation of the [[von Bertalanffy Growth Model]] (VBGM) that extends prior work by [[Cope and Punt 2007]] and [[Chamberlin et al. 2023b]] to simultaneously compare growth parameters across multiple ageing protocols and sexes while incorporating between-reader variability as a random effect.

## Mathematical & Statistical Framework

**Model Formulation:**

The size-at-birth formulation of the VBGM (eq. 2):
$$L_i = L_\infty - (L_\infty - L_0)e^{-kt_i}$$

where $L_i$ is length at age $t_i$ of individual $i$, $L_\infty$ is asymptotic length, $L_0$ is size at birth, and $k$ is the Brody growth coefficient.

Protocol-specific model (eq. 3):
$$\hat{L}_{i,p} = L_{\infty,p} - (L_{\infty,p} - L_0)e^{-k_p t_{i,p}}$$

where $p$ denotes different protocols (otolith, new spine, old spine).

Process error specification (eq. 4):
$$L_{i,p} \sim \text{logNormal}(\log(\hat{L}_{i,p}), \sigma_p)$$

Sex-specific model (eq. 5):
$$\hat{L}_{i,p} = L_{\infty,p,s} - (L_{\infty,p,s} - L_0)e^{-k_{p,s}t_{i,p}}$$

where $s$ denotes sex-specific parameters.

Sex effects as additive linear models (eqs. 7-9):
$$\log(L_{\infty,p,s}) = \log(L_{\infty,p}) + \beta_{L_\infty,s}$$
$$\log(k_{p,s}) = \log(k_p) + \beta_{k,s}$$
$$\log(\sigma_{p,s}) = \log(\sigma_p) + \beta_{\sigma,s}$$

Between-reader variability (eq. 10):
$$t_{i,p,r} \sim \text{location-scaleT}(\nu_{i,p}, \hat{t}_{i,p}, \tau_p)$$

where $t_{i,p,r}$ is observed age from reader $r$, $\nu_{i,p}$ is degrees of freedom (number of reads), $\hat{t}_{i,p}$ is "true" age, and $\tau_p$ is inter-reader variability.

Derived $t_0$ (eq. 11):
$$\hat{t}_{0,p,s} = \frac{1}{k_{p,s}}\log\left(\frac{L_{\infty,p,s} - L_0}{L_{\infty,p,s}}\right)$$

Fractional age for age-0 fish (eq. 1):
$$\text{Frac}_0 = \frac{(FL/0.95)}{365}$$

where juvenile growth rate = 0.95 mm/day.

**Variables & Covariates:**

*Response variable:* Fork length (FL, mm)

*Predictors:* Age (years), ageing protocol (otolith, new spine, old spine), sex (female, male, unknown)

*Random effects:* Between-reader variability ($\tau_p$) modeled via location-scale T distribution; individual "true" age ($\hat{t}_{i,p}$)

*Fixed effects:* Protocol-specific $L_\infty$, $k$, $\sigma$; sex-specific additive effects $\beta_{L_\infty,s}$, $\beta_{k,s}$, $\beta_{\sigma,s}$

*Offsets:* Shared $L_0$ across all models

**Fit Diagnostics & Metrics:**

- Gelman-Rubin statistic: all parameters < 1.01 (convergence criterion < 1.1)
- Bulk effective sample size: mean = 1811 (two parameters had ESS = 212, 220)
- Tail effective sample size: mean = 2488
- Maximum *a posteriori* (MAP) based *p*-value ($p_{MAP}$) at α = 0.10 for parameter comparisons
- 90% credible intervals (CIs) reported for all parameters
- Index of average percent error (iAPE): 10.1% (otoliths), 9.4% (new spine protocol)
- No AIC/WAIC reported; Bayesian framework used posterior distributions for inference
- Sensitivity analysis with hyper-weakly informed priors showed differences only in last significant digit

## Data Requirements & Preprocessing

**Input Data Schema:**

- Total sample size: n = 1270 [[Gray Triggerfish]] from Gulf of Mexico
- Otolith ages: n = 1182 (R1), subset read by R2 and R3
- New spine protocol ages: n = 1219 (R1), subset read by R2 and R3
- Old spine protocol ages: n = 1243 (R1 only, no multiple readers)
- Sex distribution: 685 females, 585 males, unknown sex included via additive effects model
- Age range: 0.37–16 years (varies by protocol and sex)
- Fork length range: converted from filleted FL using regression (R² = 0.99; $FL_{Whole} = 0.99 \times FL_{Filleted} + 0.30$)
- Zero-inflation: Not reported as an issue; age-0 fish assigned fractional ages
- Missing data: Differences in sample sizes due to missing structures or uninterpretable samples; unknown sex individuals included via hierarchical structure

**Sampling Cross-References:**

- #fishery_dependent_sampling: hook-and-line (n=685), longline (n=412), 925 total samples
- #fishery_independent_sampling: hook-and-line, trawl (n=51), spear (n=122), 345 total samples
- #gear_selectivity: combining multiple gear types reduces bias and improves precision
- #spatial_coverage: northern Gulf of Mexico (n=706), eastern Gulf of Mexico/West Florida Shelf (n=391), western Gulf of Mexico/Texas (n=122)
- #natural_and_artificial_reefs: targeted habitats
- #SEAMAP_trawl_survey: source of trawl-caught samples
- #morphometric_data: fork length, weight (fishery-independent only), sex via gonad examination
- #ageing_structure_extraction: sagittal otoliths (vestibular system), first dorsal spine with condyle

## Code Logic

**STAN Implementation:**

The authors used STAN via cmdstanr with the following specifications:

- 8 chains
- 5000 warmup iterations per chain
- 125 sampling iterations per chain
- No U-Turn sampler (NUTS)
- Combined chain-specific posterior samples after assessing convergence

**Prior Specification (weakly informative):**

Maximum likelihood estimates used to generate prior location; 50% coefficient of variation for prior scale. Normal priors on log-transformed parameters for $L_\infty$, $k$, $\sigma$, $\tau$ (Table S1). Strongly informative prior on $L_0$: mean = 2.2 mm, SD = 0.04 mm (from [[Simmons and Szedlmayer 2013]]). Sex-specific additive effects: Normal(0, 1) on log scale.

Weakly informative prior on $\log(\tau)$: mean = -1.0, SD = 4.0.

**R Analysis:**

Three-factor ANOVA models (α = 0.05) to test sex effects on size-at-age:
- Dependent: FL
- Independent: age, ageing structure, sex
- Interaction sliced by ageing structure and age

**Posterior Inference:**

- bayestestR package for MAP-based *p*-values
- 90% credible intervals for all parameters
- Predicted length-at-age over hypothetical ages from 0 to $t_{max}$ by 0.1 year increments

**Pseudocode for hierarchical structure:**

```
for each individual i:
  for each protocol p:
    for each reader r:
      observed_age[i,p,r] ~ location-scaleT(df = n_reads, location = true_age[i,p], scale = tau[p])
    
    predicted_length[i,p] = L_inf[p,sex[i]] - (L_inf[p,sex[i]] - L0) * exp(-k[p,sex[i]] * true_age[i,p])
    
    observed_length[i,p] ~ logNormal(log(predicted_length[i,p]), sigma[p,sex[i]])
```

## Biological & Management Synthesis

**Model-to-Decision Mapping:**

1. **Stock Assessment Implications:** The old spine protocol significantly overestimates the Brody growth coefficient ($k$), leading to overestimation of natural mortality ($M$) and stock productivity. Combined sex old spine $k = 0.55$ year⁻¹ vs. otolith $k = 0.42$ year⁻¹ and new spine $k = 0.39$ year⁻¹. This bias would result in overly optimistic management reference points and increased likelihood of overfishing.

2. **Sexual Dimorphism:** Males grow significantly larger than females ($L_\infty$ new spine: males = 502 mm, females = 447 mm; $p_{MAP} < 0.01$). Both sexes are similar size until age 2–3. Females exhibit significantly higher growth variability ($\sigma$; $p_{MAP} < 0.01$). No significant difference in $k$ between sexes due to posterior uncertainty ($p_{MAP} = 0.18–0.98$). **Management recommendation:** Future stock assessments should incorporate sex-specific growth models and sex-specific landings data.

3. **Ageing Protocol Validation:** Otolith and new spine protocol produce statistically equivalent growth parameters, supporting use of either validated method. Old spine protocol consistently underestimates age for fish ≥5 years, resulting in biased growth curves. Between-reader variability ($\tau$) similar for otolith (0.55) and new spine (0.55) protocols, with no significant difference ($p_{MAP} = 0.52$).

4. **Uncertainty Quantification:** Incorporating multiple readers separates observation error ($\tau$) from process error ($\sigma$), allowing total variance ($\sigma_{total} = \sigma + \tau = 0.68$) to be propagated into stock assessments. Single-reader old spine model underestimates total uncertainty ($\sigma_{total} = 0.14$).

5. **Reference Points:** Derived $t_0$ estimates differ significantly between protocols (old spine vs. validated methods) due to informative prior on $L_0$, but this is an artifact of the model structure rather than biological difference. The key management-relevant parameters are $L_\infty$ and $k$.

6. **Rebuilding Plan Context:** [[Gray Triggerfish]] in the Gulf of Mexico failed to recover at expected rates following decades of overfishing and implementation of a rebuilding plan in the early 1990s. Ageing error from the old spine protocol may have contributed to this failure by producing biased estimates of growth, mortality, recruitment, and fishing mortality reference points.

**Biological Context (keyword stubs):** #spawning_season #fecundity_proxies #size_selective_sampling #gear_selectivity_bias #natural_mortality_estimation #recruitment_dynamics #maximum_age #longevity #reef_associated_species #fishery_dependent_vs_independent #spatial_growth_variation #annual_growth_zones #bomb_radiocarbon_validation #translucent_zones #opaque_zones #otolith_microstructure #dorsal_spine_sections #age_validation #marginal_increment_analysis