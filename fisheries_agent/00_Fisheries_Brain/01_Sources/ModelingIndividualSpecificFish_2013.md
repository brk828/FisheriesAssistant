---
species:
  - Oncorhynchus mykiss
target_species: "Rainbow Trout (Oncorhynchus mykiss)"
common_name: Rainbow Trout
family: Salmonidae
habitat: Freshwater headwaters
ocean_basin: N/A
location: Rangitikei River, New Zealand
tags:
  - growth_modeling
  - capture_recapture
  - hierarchical_models
  - von_Bertalanffy
analytical_category:
  - Hierarchical Bayesian modeling
  - Growth curve estimation
  - Capture-recapture analysis
  - Model comparison
model_framework: von Bertalanffy growth curve with individual random effects
software_environment:
  - JAGS
  - R
  - R2jags
data_requirements:
  - Multiple length measurements per individual
  - Time between captures
  - Sex (when available)
  - Season of first capture
key_assumptions:
  - Normal observation error (truncated at zero)
  - Exchangeable individual parameters
  - von Bertalanffy curve applicable over observed range
  - Missing sex data is missing at random
keywords_stubs:
  - "#von_Bertalanffy"
  - "#MCMC"
  - "#individual_growth"
  - "#nuisance_parameters"
  - "#model_checking"
  - "#posterior_predictive"
  - "#cross_validation"
  - "#sex_differences"
title: "Modeling Individual Specific Fish Length from Capture–Recapture Data Using the von Bertalanffy Growth Curve"
source_id: "X-7ada1135"
doc_type: "analyses_and_modeling"
source_citation: "M. R. Schofield, R. J. Barker, P. Taylor (2013). Modeling Individual Specific Fish Length from Capture–Recapture Data Using the von Bertalanffy Growth Curve. Biometrics 69(4): 1012-1021."
doi: "10.1111/biom.12069"
source_file: "GrowthCurveBayesian Schofield et al. 2013.pdf"
text_extraction: "text"
---
# Modeling Individual Specific Fish Length from Capture–Recapture Data using the von Bertalanffy Growth Curve

#ichthyology #Salmonidae #growth_modeling #hierarchical_models

## Analytical Objective & Scope

**Core Problem Addressed**: Estimating individual-specific growth parameters (maximum length, growth rate) from capture-recapture data when age is unobserved, with focus on how hierarchical assumptions about nuisance parameters influence inference about biological parameters of interest.

**Methodological Classification**: Adaptation of existing von Bertalanffy models. The paper compares two standard parameterizations—Age at First Capture (AFC) and Length at First Capture (LFC)—within a Bayesian hierarchical framework, demonstrating that "equally plausible a priori distributional assumptions about nuisance parameters can influence the inference for the parameters of interest." This is a novel comparative analysis rather than a new method, emphasizing the sensitivity of inference to modeling choices for parameters defined by study design rather than biology.

**Study Context**: Analysis of 527 [[Rainbow Trout]] from the [[Rangitikei River]] headwaters, New Zealand, captured 1–5 times between March 1993 and November 2004 (734 total length measurements). Data include 605 measurements from 13 tagging occasions plus 129 angler-reported measurements. Individuals <400 mm excluded; sex recorded for 515 fish.

## Mathematical & Statistical Framework

**Model Formulation**:

*Data Model*:
$$y_i(t_j) \sim N(g_i(t_j)(1-M_i) + M_i L_i, \sigma^2_y) \text{ T}(0,\infty)$$

where $y_i(t_j)$ = observed length of individual $i$ at capture $j$; $g_i(t_j)$ = von Bertalanffy growth curve; $M_i$ = latent maturity indicator (Bernoulli($\pi_M$)); $L_i$ = maximum length; $\sigma^2_y$ = combined process and observation variance; T(0,∞) = truncation ensuring positive lengths.

*AFC Parameterization*:
$$g_i(t_j) = L_i(1 - k_i^{a_i + \Delta_{ij}})$$

where $a_i$ = age at first capture relative to hypothetical age-at-zero-length; $\Delta_{ij}$ = time since first capture; $k_i$ = growth rate.

*LFC Parameterization*:
$$g_i(t_j) = \lambda_i + (L_i - \lambda_i)(1 - k_i^{\Delta_{ij}})$$

where $\lambda_i$ = length at first capture.

**Variables & Covariates**:

*Response*: Length measurements $y_i(t_j)$ (mm), ranging 400–750 mm.

*Individual-level parameters*:
- $L_i$ ~ N($\beta_{L0} + \beta_{L1}m_i, \sigma^2_L$) T(0,∞): maximum length
- logit($k_i$) ~ N($\beta_{k0}(1-m_i) + \beta_{k1}m_i, \sigma^2_k$): growth rate
- log($a_i$) ~ N($\beta_{a0} + \beta_{a1}m_i + \beta_{a2}s_i, \sigma^2_a$): AFC model nuisance parameter
- $\lambda_i$ ~ N($\beta_{\lambda 0} + \beta_{\lambda 1}m_i + \beta_{\lambda 2}s_i, \sigma^2_\lambda$) T(0,$L_i$): LFC model nuisance parameter

*Covariates*: $m_i$ = sex (1=male, 0=female); $s_i$ = season at first capture (1=spring, 0=autumn); $\Delta_{ij}$ = time between captures (years).

*Random effects*: Individual-specific $L_i$, $k_i$, and $a_i$ or $\lambda_i$ (depending on parameterization).

**Fit Diagnostics & Metrics**:

*Convergence*: Gelman-Rubin diagnostic and effective sample size calculated for all parameters. LFC model had larger effective sample sizes for all mean-level parameters.

*MCMC specifications*: 3 chains per model; 10,000 burn-in iterations; 200,000 retained iterations per chain (600,000 total).

*Model comparison*: Posterior predictive checks comparing joint log-densities of (1) data model conditional on parameters, (2) hierarchical model for hybrid parameter, (3) hierarchical model for maximum length, (4) hierarchical model for growth rate. Ten-fold cross-validation for predictive ability (root mean predictive error showed no discernible difference between models).

*Key findings*: AFC model performed better in hierarchical parameter models; LFC model performed better in conditional data model. Neither showed evidence of lack of fit in posterior predictive checks. Estimates of $\pi_M$ (proportion mature at first capture) ranged 10–30% in both models.

## Data Requirements & Preprocessing

**Input Data Schema**:

*Minimum requirements*: At least one length measurement per individual; time of capture; ideally multiple recaptures (only 39 of 527 individuals had ≥3 captures).

*Sample composition*: $f = (368, 120, 31, 7, 1)$ where $f_i$ = number of individuals caught $i$ times. Model is overparameterized except when every individual has ≥2 recaptures, necessitating hierarchical constraints.

*Missing data*: Sex missing for 12 individuals, modeled as $m_i$ ~ Bernoulli($\psi$) where $\psi$ = Pr(male), assuming missing at random.

*Zero-inflation*: Not applicable (continuous length data).

*Preprocessing*: Removed 1 individual with no length measurements and 19 individuals <400 mm (all but one caught once, mostly on occasion 11 during unusually high river temperatures). Final dataset: 527 individuals, 734 length measurements.

*Data structure*: Irregular time intervals between captures; angler-reported data occur both during and after formal tagging study (final measurement November 2004).

**Sampling Cross-References**: [[Capture-Recapture Design]], [[Tagging Studies]], [[Angler Reporting Programs]], [[Mark-Recapture Sampling]]. The study originally focused on fishery regulation effects on population dynamics (Barker, Taylor, and Smith, 2002).

## Code Logic

The authors provide R and JAGS code at www.maramatanga.com. Key pseudocode structure:

```
# Data model (equation 2)
for(i in 1:n) {
  for(j in 1:r[i]) {
    y[i,j] ~ dnorm(g[i,j]*(1-M[i]) + M[i]*L[i], tau.y) T(0,)
  }
  M[i] ~ dbern(pi.M)
}

# AFC parameterization (equation 4)
g[i,j] <- L[i] * (1 - pow(k[i], a[i] + Delta[i,j]))

# LFC parameterization (equation 5)
g[i,j] <- lambda[i] + (L[i] - lambda[i]) * (1 - pow(k[i], Delta[i,j]))

# Hierarchical models
for(i in 1:n) {
  L[i] ~ dnorm(beta.L0 + beta.L1*m[i], tau.L) T(0,)
  logit(k[i]) ~ dnorm(beta.k0*(1-m[i]) + beta.k1*m[i], tau.k)
  
  # AFC model:
  log(a[i]) ~ dnorm(beta.a0 + beta.a1*m[i] + beta.a2*s[i], tau.a)
  
  # LFC model:
  lambda[i] ~ dnorm(beta.lambda0 + beta.lambda1*m[i] + beta.lambda2*s[i], 
                    tau.lambda) T(0, L[i])
  
  # Missing sex
  m[i] ~ dbern(psi)  # when sex not recorded
}

# Priors on hyperparameters (details in Supplementary Materials S2)
```

The LFC truncation T(0, $L_i$) induces positive correlation between $\lambda_i$ and $L_i$ (Turnbull, 1976). The maturity mixture component effectively allows $a_i = \infty$ (AFC) or $\lambda_i = L_i$ (LFC) with probability $\pi_M$.

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

*Sex-specific growth patterns*: Males grow faster but to smaller maximum size than females. Posterior distributions indicate $\beta_{L1}$ (sex effect on maximum length) and $\beta_{k0}$, $\beta_{k1}$ (sex-specific growth rates) differ significantly between sexes. This has implications for [[Size-Selective Harvest]] regulations and [[Sex-Specific Management]].

*Maturity at capture*: 10–30% of captured trout were fully mature (at maximum length), suggesting the fishery targets a mix of growing and mature individuals. This informs [[Harvest Slot Limits]] and [[Trophy Fishery Management]].

*Individual variability*: Substantial variation in both maximum length ($\sigma_L$) and growth rate ($\sigma_k$), though estimates of $\sigma_k$ differ markedly between AFC and LFC models. This variability is critical for [[Population Viability Analysis]] and understanding [[Phenotypic Diversity]].

*Model uncertainty caution*: The paper demonstrates that "equally plausible a priori distributional assumptions about nuisance parameters can influence the inference for the parameters of interest." Specifically, estimates of $\beta_{L0}$ (mean female maximum length), $\beta_{k0}$ (mean female growth rate), and $\sigma_k$ (growth rate variability) differ substantially between parameterizations. Management decisions based on growth parameters should account for this structural uncertainty.

*Limitations acknowledged*: Sample may not be random due to length-dependent capture probability and survival (potential bias). Integration with live-resighting, dead-recovery models (Barker, 1997) recommended for unbiased inference. Only 39 individuals with ≥3 captures limits ability to estimate individual-level parameters without strong hierarchical constraints.

*Extensions not implemented* (due to modest sample size): Correlation between $L_i$ and $k_i$; temporal correlation in observations; length-dependent capture/survival probabilities.

**Biological keyword stubs**: #sexual_dimorphism #maturity_at_capture #individual_variation #growth_rate #maximum_length #freshwater_salmonids #temperate_streams #fishery_regulations