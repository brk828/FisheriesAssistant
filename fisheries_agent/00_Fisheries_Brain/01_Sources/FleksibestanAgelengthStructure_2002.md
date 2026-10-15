---
species:
  - North-East Arctic cod (Gadus morhua L.)
  - Barents Sea capelin (Mallotus villosus)
  - Atlantic cod (Gadus morhua L.)
target_species: "North-East Arctic cod (Gadus morhua L.)"
common_name: "North-East Arctic cod"
family: "Gadidae"
habitat: "boreal marine"
ocean_basin: "Arctic, Barents Sea"
location: "Barents Sea, Iceland, eastern Newfoundland, Lofoten"
tags:
  - stock assessment
  - age-length structured model
  - population dynamics
  - fisheries management
  - boreal stocks
analytical_category:
  - statistical catch-at-age analysis (CAGEAN)
  - age-length structured population model
  - parametric modeling
  - likelihood-based estimation
model_framework: "Fleksibest: age-length structured population model with self-contained dynamics fitted to observations"
software_environment:
  - "Modified BORMICON code"
  - "R (implied)"
  - "Optimization algorithms: Hooke and Jeeves, simulated annealing, BFGS"
data_requirements:
  - commercial catch data (age-length structured)
  - scientific survey data (acoustic and bottom trawl)
  - stomach content data for cannibalism
  - weight-length relationships
  - minimum sample size not specified
key_assumptions:
  - biological processes (growth, mortality, maturation) are length-dependent rather than age-dependent
  - fishing mortality is product of length-dependent selectivity and year-specific fishing level
  - no stock-recruitment function; annual recruitment estimated as parameters
  - separate population dynamics for immature and mature stocks
  - cannibalism mortality modeled as function of prey length and predator biomass
  - growth distribution follows specified probability function with mean and variance
keywords_stubs:
  - "#age-length-structure"
  - "#CAGEAN"
  - "#parametric-models"
  - "#boreal-stocks"
  - "#growth-variability"
  - "#cannibalism"
  - "#maturation-model"
  - "#likelihood-estimation"
  - "#VPA-alternative"
title: "Fleksibest—an age–length structured fish stock assessment model"
source_id: "X-7bdd8757"
doc_type: "analyses_and_modeling"
source_citation: "K. Guldbrandsen Frøysa, B. Bogstad, D. W. Skagen (2002). Fleksibest—an age–length structured fish stock assessment model. Fisheries Research 55(1-3): 87-101."
doi: "10.1016/s0165-7836(01)00307-1"
source_file: "age and length based size structure.pdf"
text_extraction: "ocr"
---
# Fleksibest—an age-length structured fish stock assessment model

#ichthyology #Gadidae #stock-assessment #population-modeling

## Analytical Objective & Scope

**Core Problem Addressed**: Fleksibest addresses the inadequacy of age-structured models for boreal fish stocks that exhibit large inter-annual variation in growth rates. Traditional models use age as a proxy for length, which is unsatisfactory when size-at-age varies substantially. The model is designed primarily for [[North-East Arctic Cod]] but applicable to other boreal stocks experiencing high growth variability.

**Methodological Classification**: This is an adaptation and extension of existing CAGEAN (statistical catch-at-age analysis) models, modified from the Icelandic multispecies model [[BORMICON]]. The innovation lies in structuring the population by both age and length groups (abundance matrix approach) rather than using probability distributions for length structure, and in modeling biological processes as functions of length rather than age. The model represents a novel integration of length-structured dynamics into the CAGEAN framework, specifically addressing the biological realities of boreal systems where "age is not a good proxy for size."

## Mathematical & Statistical Framework

**Model Formulation**:

The fundamental population dynamics equation:
$$\frac{dN}{dt} = -Z(t)N(t)$$

where total mortality is partitioned as:
$$Z = F + M$$

The model uses matrix operators to describe stock transitions. The immature stock matrix N(t_{m+1}) relates to N(t_m) as:

$$N(t_{m+1}) = H(t_m)[G(t_m)S(t_m)(N(t_m) - C(t_m)) + R(t_{m+1})]$$

Mature stock:
$$N(t_{m+1}) = H(t_m)[G(t_m)S(t_m)N(t_m) + C'(t_m)]$$

where:
- H = aging matrix (A × A)
- G = growth matrix (L × L band matrix)
- S = survival matrix (L × L diagonal)
- B = maturation matrix (L × L diagonal)
- E = minimum maturation age matrix (A × A)
- R = recruitment matrix (A × L)
- C = fish maturing from immature stock
- C' = fish entering mature stock

**Fishing Mortality Model**:
$$F_f(l_i, t_m) = A_f(y) \cdot \theta_f(t_m) \cdot S_f(l_i)$$

where A_f(y) is annual fishing mortality level for fleet f, θ_f(t_m) distributes mortality across time steps, and S_f(l_i) is length-dependent selectivity.

Total fishing mortality:
$$F(l_i, t_m) = \sum_{f=1}^{N_f} F_f(l_i, t_m)$$

**Natural Mortality Components**:
$$M(l_i, t_m) = M1(l_i) + M2(l_i, t_m)$$

Residual natural mortality (U-shaped function):
$$M1(l) = \begin{cases} a_1 e^{-b_1 l} & l_{min} < l < l_c \\ c & l_c < l < l_h \\ a_2 e^{b_2 l} & l_h < l < l_{max} \end{cases}$$

Cannibalism mortality:
$$M2_{imm}(l_i, t_m) = \frac{\alpha \cdot f(l_i)}{1 + \beta \cdot I^{\gamma}} \cdot P(l_i, t_m)$$

where:
$$f(l_i) = \exp(-\delta \cdot l_i^2)$$
$$P(l_i, t_m) = \sum_{u=imm}^{mat} \sum_{a=a_0}^{A} \sum_{s=j}^{L} N_{u,a,s}(t_m) \cdot W_u(l_s, t_m) \cdot V_u(t_m)$$

with cl_i < l_j (predator must be larger than prey by factor c > 1).

**Growth Models**:

1. von Bertalanffy:
$$\delta l_u(l_i, t_m) = (l_{\infty} - l_i) \cdot (1 - \exp(-k(y) \Delta t))$$

2. Power/linear:
$$\delta l_u(l_i, t_m) = k(y) \Delta t \cdot l_i^q, \quad q \leq 0$$

Growth distribution satisfies:
$$\sum_{i=r}^{r+g} p(i, r | \delta l(l_r, t_m)) = 1$$
$$\sum_{i=r}^{r+g} (i-r) p(i, r | \delta l(l_r, t_m)) = \mu_r$$
$$\sum_{i=r}^{r+g} ((i-r) - \mu_r)^2 p(i, r | \delta l(l_r, t_m)) = \sigma^2$$

where μ_r is mean growth and σ² = k_0 + k_1 μ_r.

**Maturation Model**:
$$m(l) = \frac{1}{1 + \exp(-4\alpha(l - l_{50}))}$$

with minimum maturation age constraint implemented through matrix E.

**Catch Equation**:
$$C_{mod}(f, a, l_i, t_m) = \frac{F_f(l_i, t_m)}{Z(l_i, t_m)} N(a, l_i, t_m) (1 - \exp(-Z(l_i, t_m)))$$

**Survey-Population Relationships**:

Linear model:
$$I_{mod}(s, a, l_i, t_m) = b_s(l_i) + g_s(t_m) \cdot \tau_s(l_i) \cdot N(a, l_i, t_m)$$

Power model:
$$I_{mod}(s, a, l_i, t_m) = g_s(t_m) \cdot \tau_s(l_i) \cdot N(a, l_i, t_m)^{\phi}$$

where τ_s(l_i) is selectivity (often logistic) and b_s(l_i) = b_1 exp(-b_2 l_i).

**Variables & Covariates**:
- Response: N(a, l_i, t_m) = abundance matrix (age × length)
- Predictors: length l_i, age a, time t_m, year y, fleet f, survey s
- Random effects: Not explicitly modeled
- Offsets: None reported
- Covariates: temperature (for gastric evacuation in cannibalism), alternative prey biomass I

**Fit Diagnostics & Metrics**:

Four objective functions implemented:

1. Multinomial likelihood:
$$L_1 = \sum X_{obs} \ln(X_{mod} + \epsilon)$$

2. Log-normal (squared log differences):
$$L_2 = \sum (\ln X_{obs} - \ln X_{mod})^2, \quad X_{mod} > \epsilon \land X_{obs} > \epsilon$$

3. Pearson function:
$$L_3 = \sum \frac{(X_{obs} - X_{mod})^2}{X_{mod} + \epsilon}$$

4. Gamma distribution (constant CV):
$$L_4 = \sum \left[\frac{X_{obs}}{X_{mod} + \epsilon} + \ln(X_{mod} + \epsilon)\right]$$

Consumption objective function:
$$L_{cons} = \sum \frac{(X_{obs} - X_{mod})^2}{n \sigma^2}$$

Total objective function:
$$L_{tot} = \sum_{f=1}^{N_f} w_f L_f + \sum_{s=1}^{N_s} w_s L_s + w_{cons} L_{cons}$$

where w terms are externally set weighting factors.

Convergence criteria, confidence intervals, AIC/WAIC, and R² values are not reported in this document. The paper notes that "careful testing is necessary to choose the best likelihood formulation" and that statistical properties of processed data are "unclear or destroyed," making likelihood choice non-trivial.

## Data Requirements & Preprocessing

**Input Data Schema**:

1. **Commercial catch data**: Total catches in weight by year, quarter, fleet, and area from national reporting; age and length composition from samples; length-weight relationships. These are converted to catch in numbers by year, quarter, fleet, age, and length through "a fairly complicated process with many steps." The document notes that "representativity of the sampling may be quite variable, and the data on total catch may be in error."

2. **Survey data**: Age-length structured abundance indices from acoustic and bottom trawl surveys. Surveys are treated as relative indices rather than absolute abundance estimates due to: (a) limited geographical coverage, (b) vertical coverage problems (acoustic dead zone near bottom, pelagic fish less available to bottom trawl), (c) uncertainty in converting density observations to abundance (gear efficiency, fishing width/height, acoustic target strength unknown).

3. **Stomach content data**: Consumption of small (immature) fish by larger fish, calculated from stomach contents, temperature data, and gastric evacuation rate model. Given as kg per time unit (half year) per predator for each predator age group and prey length group.

**Minimum sample size**: Not specified.

**Zero-inflation**: Not explicitly addressed; objective functions include small constant ε to avoid log(0).

**Missing data**: Not discussed.

**Data processing notes**: The document emphasizes that both CAGEAN and Fleksibest use "processed" data where "statistical properties of the data are unclear or destroyed." An alternative approach would compare model results to "direct observations such as catch in biomass, total acoustic abundance, length samples and subsamples" where "statistical properties of the data are much more clear." Current implementation uses processed data for consistency with previous assessment models ([[XSA]]).

**Sampling Cross-References**:
- #survey-design-acoustic
- #survey-design-bottom-trawl
- #catch-sampling-protocols
- #stomach-content-sampling
- #length-weight-relationships
- #age-length-keys
- #Lofoten-spawning-survey

## Code Logic

**Pseudocode for matrix operations**:

```
# Time step progression for immature stock
N_imm(t_{m+1}) = H(t_m) * [G(t_m) * S(t_m) * (N_imm(t_m) - C(t_m)) + R(t_{m+1})]

# Intermediate calculations
N'(t_m) = N(t_m) * G(t_m)  # Apply growth
N''(t_m) = N'(t_m) * S(t_m)  # Apply survival
C'(t_m) = N''(t_m) * B(t_m)  # Fish that mature
C''(t_m) = E * C'(t_m)  # Apply minimum maturation age

# Growth distribution calculation
for each age a and length group r:
  for i in (r to r+g):  # g = max length groups to grow
    N'(a, i, t_m) += N(a, r, t_m) * p(i, r | δl(l_r, t_m))
  
where p(i, r | δl) satisfies:
  sum over i: p(i, r | δl) = 1  # conservation
  sum over i: (i-r) * p(i, r | δl) = μ_r  # mean growth
  sum over i: ((i-r) - μ_r)^2 * p(i, r | δl) = σ²  # variance

# Survival matrix (diagonal)
S_ii = exp(-Z(l_i, t_m))
where Z(l_i, t_m) = F(l_i, t_m) + M(l_i, t_m)

# Fishing mortality calculation
F(l_i, t_m) = 0
for each fleet f:
  F(l_i, t_m) += A_f(y) * θ_f(t_m) * S_f(l_i)

where θ_f(t_m) = C_f(t_m) / sum_over_year(C_f(t))

# Cannibalism mortality
P(l_i, t_m) = 0
for u in {imm, mat}:
  for a in age_range:
    for s in length_range where cl_i < l_s:
      P(l_i, t_m) += N_{u,a,s}(t_m) * W_u(l_s, t_m) * V_u(t_m)

M2_imm(l_i, t_m) = (α * exp(-δ * l_i²)) / (1 + β * I^γ) * P(l_i, t_m)

# Aging (applied at year end)
if (m mod steps) == 0:
  N_new = H * N_old  # shift ages up one row
  if plus_group:
    N_new[A, :] += N_old[A, :]  # accumulate oldest age
```

**Optimization algorithms** (no code provided, only names):
- Hooke and Jeeves direct search
- Simulated annealing
- BFGS (Quasi-Newton method)

Note: "In order to use a gradient method the objective function must be differentiable, which is not the case with the current implementation of growth."

**Parameter estimation structure**:
```
Required parameters:
  - N(a, l, t_0) for immature and mature stocks
  - Annual recruitment R(y)
  - Annual fishing mortality A_f(y)

Optional parameters (often estimated):
  - Mean length at age in initial year (by maturity status)
  - SD of length at age in initial year
  - Mean length of recruits each year
  - SD of recruit length each year
  - Growth parameters: k(y), variance parameters k_0, k_1
  - Maturation parameters: α, l_50
  - Cannibalism parameters: α, β, γ, δ, c
  - Residual mortality parameters: a_1, a_2, b_1, b_2, c
  - Selectivity parameters for fleets and surveys

Typical run: 150-200 parameters estimated
```

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

The model produces key management quantities:

1. **Spawning Stock Biomass (SSB)**: Calculated directly as the biomass of the mature stock component, rather than applying maturity ogives to total stock as in [[XSA]]. For [[North-East Arctic Cod]], Fleksibest estimated higher SSB than XSA over most of the time series (1982-2000), with a more pronounced peak in early 1990s and steeper recent decline, consistent with acoustic surveys on spawning grounds.

2. **Reference Fishing Mortality (F₅₋₁₀)**: Unweighted arithmetic mean of fishing mortalities for age groups 5-10, used for management purposes. Fleksibest consistently estimated lower F₅₋₁₀ than XSA, which is "reasonable, as Fleksibest estimates higher stock size."

3. **Recruitment**: Annual recruitment at age 3 estimated as model parameters (no stock-recruitment relationship). Fleksibest showed same general trends as XSA but typically higher recruitment estimates.

4. **Catch estimation**: Model estimates catch in numbers via catch equation (Eq. 46), then converts to weight using observed weight-at-length. For NEA cod, Fleksibest