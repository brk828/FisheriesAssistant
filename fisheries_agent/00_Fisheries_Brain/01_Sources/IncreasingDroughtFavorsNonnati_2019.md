---
species:
  - Catostomus clarki
  - Catostomus insignis
  - Gila robusta
  - Ameiurus natalis
  - Lepomis cyanellus
  - Micropterus dolomieu
  - Cyprinella lutrensis
target_species: "N/A"
common_name: "desert sucker, Sonora sucker, roundtail chub, yellow bullhead, green sunfish, smallmouth bass, red shiner"
family: "Catostomidae, Ictaluridae, Centrarchidae, Cyprinidae"
habitat: "dryland river, perennial mainstem, pools, wadeable habitats"
ocean_basin: "N/A"
location: "Verde River, Arizona, USA; Colorado River Basin"
tags:
  - demographic_model
  - multispecies_model
  - matrix_population_model
  - flow_regime
  - drought
  - flood
  - native_species
  - nonnative_species
  - climate_change
  - community_dynamics
analytical_category:
  - stage-structured matrix population model
  - multispecies demographic model
  - density-dependent population dynamics
  - stochastic simulation
  - perturbation analysis
model_framework: "stage-structured matrix population model with density dependence; three life stages (year-1 juveniles, year-2 sub-adults, year-3+ adults); species coupled via aggregate biomass carrying capacity"
software_environment:
  - R v3.4.0
data_requirements:
  - species vital rates (mortality, fecundity, GSI, age at maturity, lifespan)
  - length-weight relationships
  - daily streamflow data (USGS gage 09503700)
  - long-term fish survey data (1994-2008, seven sites)
  - initial population biomass (negative binomial distribution)
  - reach-wide carrying capacity (total fish biomass)
key_assumptions:
  - carrying capacity limited by total fish biomass in 1-km reach
  - density dependence operates through reproduction only
  - baseline mortality constant across life stages within species (except egg/larval)
  - 1:1 sex ratio for all species
  - life cycles completed within 1-km reach
  - closed community (no immigration/emigration)
  - flow events classified into six mutually exclusive types
  - exploitative competition via generalized density dependence
keywords_stubs:
  - "#flow_ecology"
  - "#vital_rates"
  - "#life_history_traits"
  - "#hydrologic_regime"
  - "#environmental_stochasticity"
  - "#species_coexistence"
  - "#temporal_storage_effect"
  - "#recruitment_dynamics"
  - "#Colorado_River_Basin"
  - "#invasive_species"
  - "#community_assembly"
  - "#non_stationarity"
title: "Increasing drought favors nonnative fishes in a dryland river: evidence from a multispecies demographic model"
source_id: "X-b31e6b33"
doc_type: "analyses_and_modeling"
source_citation: "J. S. Rogosch, J. D. Tonkin, D. A. Lytle, D. M. Merritt, L. V. Reynolds, J. D. Olden (2019). Increasing drought favors nonnative fishes in a dryland river: evidence from a multispecies demographic model. Ecosphere 10(4)."
doi: "10.1002/ecs2.2681"
source_file: "Rogosch et al. 2019 - Increasing drought favors nonnative fishes in a dryland river  evidence from a multispecies.pdf"
text_extraction: "mixed"
---
# Increasing drought favors nonnative fishes in a dryland river: evidence from a multispecies demographic model

#ichthyology #Catostomidae #Centrarchidae #Ictaluridae #Cyprinidae

## Analytical Objective & Scope

**Core Problem Addressed**: Understanding how native and nonnative fish populations respond to changing flow regimes (drought and flood sequences) in dryland rivers under climate change. The study addresses the challenge of modeling novel biological assemblages in non-stationary environmental conditions.

**Methodological Classification**: Novel adaptation of an existing modeling framework. The authors adapted a multispecies matrix population model originally designed for riparian vegetation (Lytle and Merritt 2004, Lytle et al. 2017) to fish communities, with important modifications including biomass-based currency, species-specific flow-response relationships, and three-stage life cycles tailored to fish demography.

**Scope**: Seven fish species (three native, four nonnative) in the upper Verde River, Arizona, simulated annually from 1964–2017. Model validated against long-term fish survey data (1994–2008, seven sites). The framework is designed for transferability to other stream systems by adjusting vital rates and flow thresholds.

## Mathematical & Statistical Framework

**Model Formulation**: Stage-structured matrix population model for each species j with three life stages i (year-1 juveniles, year-2 sub-adults, year-3+ adults):

$$B_{i,j}^{t+1} = \begin{bmatrix} F_{1j} & F_{2j} & F_{3j} \\ G_{1j} & 0 & 0 \\ 0 & G_{2j} & P_{3j} \end{bmatrix} \times B_{i,j}^{t}$$

where $B_{i,j}$ is biomass (g) at stage i for species j.

**Density-Dependent Fecundity**:

$$F_{ij} = \begin{cases} 0.5 \times GSI_j \times (1 - M_{ej}) \times \left(1 - \frac{\sum_{i=1}^{m}\sum_{j=1}^{n} B_{ij}}{K}\right) \times D_{ej} \times D_{1j}^{-1} & \text{if } \sum B_{ij} < K \\ 0 & \text{otherwise} \end{cases}$$

where K is reach-wide carrying capacity (total biomass), $GSI_j$ is Gonadal-Somatic Index, $M_{ej}$ is egg/larval mortality, $D_{ej}$ is egg density (eggs/g), and $D_{1j}$ converts stage-1 biomass.

**Growth and Survival Transitions**:

$$G_{ij,k} = (1 - (M_{ij} \times Y_{ij,k})) \times D_i \times D_{i+1}^{-1}$$

where $M_{ij}$ is baseline mortality, $Y_{ij,k}$ is a flow modifier for stage i, species j, flow event k.

**Adult Stage Persistence**:

$$P_{3j,k} = (1 - (M_{3j} \times Y_{3j,k})) \times (1 - \alpha_{3j})$$

where $\alpha_{3j} = 1/(\text{maximum age} - 2)$ accounts for lifespan.

**Variables & Covariates**:
- **Response**: Species biomass $B_{ij}$ (converted to abundance via stage-specific weights)
- **Vital rate parameters**: $M_{ij}$ (mortality), $GSI_j$ (reproductive investment), $D_{ij}$ (biomass-abundance conversion), $\alpha_{3j}$ (adult transition probability)
- **Flow modifiers** $Y_{ij,k}$: Adjust mortality based on flow event type k (spring high flood, spring medium flood, summer high flow, spring+summer flood, drought, nonevent)
- **Environmental driver**: Annual flow classification from USGS gage 09503700 (1964–2017)
- **Initial conditions**: Species biomass sampled from negative binomial distribution with mean μ and dispersion k from survey data

**Fit Diagnostics & Metrics**:
- **Spearman rank correlations** (r) between observed and modeled relative abundances: mean r ± SE = 0.67 ± 0.018 across years; significant correlations in 7 of 15 validation years
- **Root Mean Square Error (RMSE)**: Reported per species (e.g., green sunfish had lowest RMSE, indicating best fit)
- **Coverage (C)**: Percentage of 95% confidence intervals overlapping true values (e.g., smallmouth bass and yellow bullhead had high coverage)
- **Model validation period**: 1994–2008 (15 years, omitting 2002)
- **Simulation iterations**: 1000 runs per scenario to capture stochastic variability

## Data Requirements & Preprocessing

**Input Data Schema**:
- **Vital rates**: Literature-derived values for mortality ($M_{ij}$), GSI, egg density, length-weight relationships, age at maturity, maximum lifespan for each species (Table 1, Appendix S1)
- **Flow data**: Daily discharge from USGS gage 09503700 (1963–2017); classified into six annual flow event types based on magnitude, timing, duration thresholds
- **Flow event thresholds**: Spring high flood (>19.8 m³/s, 4-yr return interval Jan–Apr); spring medium flood (>6.2 m³/s, 2.5-yr return interval); summer high flow (>5.7 m³/s, 4-yr return interval May–Sep); drought (≥40 consecutive days below 25th percentile flow)
- **Survey data**: Relative abundance from seven sites, 1994–2008 (n=105 site-years); non-juvenile fish only (stages 2 and 3) due to sampling bias
- **Carrying capacity**: Average total fish biomass from nine 100-m sites in 2012 (Gibson et al. 2015)
- **Initial biomass**: Negative binomial distribution parameters (mean, dispersion) from survey variance
- **Minimum sample requirements**: Not explicitly stated; model uses literature-aggregated vital rates rather than site-specific empirical fits
- **Missing data handling**: 2002 survey year omitted (only 2 of 7 sites sampled)
- **Zero-inflation**: Not reported as an issue; negative binomial distribution accommodates overdispersion in initial conditions

**Sampling Cross-References**: 
- #long_term_monitoring (Stefferud and Rinne 1995, Rinne et al. 1998, Neary et al. 2012)
- #electrofishing_surveys (standardized protocol, seven sites, 60 river km)
- #biomass_estimation (Gibson et al. 2015, 100-m reach surveys)
- #flow_gaging (USGS 09503700, continuous since 1963)

## Code Logic

**Pseudocode for Annual Projection**:

```
For each year t in flow_record (1964–2017):
  1. Classify year into flow_event_type k based on discharge thresholds
  2. For each species j:
     a. Calculate density-dependent fecundity F_ij:
        - Sum total community biomass across all species and stages
        - If total_biomass < K:
            F_ij = 0.5 * GSI_j * (1 - M_ej) * (1 - total_biomass/K) * D_ej * D_1j^-1
        - Else: F_ij = 0
     b. Calculate flow-modified transitions G_ij and P_3j:
        - Apply flow modifier Y_ijk to baseline mortality M_ij
        - G_ij = (1 - M_ij * Y_ijk) * D_i * D_(i+1)^-1
        - P_3j = (1 - M_3j * Y_3jk) * (1 - alpha_3j)
     c. Construct stage matrix A_j with F_ij, G_ij, P_3j
     d. Project biomass: B_j^(t+1) = A_j * B_j^t
  3. Convert biomass to abundance using stage-specific weights D_ij
  4. Store results for iteration

Repeat for 1000 iterations with different initial biomass draws
Calculate mean and 95% CI across iterations
```

**Perturbation Analysis**:

```
For each parameter (M_j, GSI_j, flow_thresholds, K):
  1. Adjust parameter by ±10%
  2. Re-run full simulation (1964–2017)
  3. Calculate proportional change in species relative abundance
  4. Rank parameters by magnitude of community-wide effect
```

**R Implementation Notes**: Model simulation performed in R v3.4.0. Flow classification used `fasstr` package (Goetz and Schwarz 2018). Negative binomial initial conditions sampled using base R functions. Code and data archived at https://doi.org/10.5281/zenodo.1309024.

## Biological & Management Synthesis

**Model-to-Decision Mapping**:

1. **Community Composition Shifts**: Model projects transition from ~80% native dominance (1994) to nonnative dominance by 2017, driven by increased drought frequency (30% in last decade vs. 9% historically). This provides quantitative evidence for climate-driven community reassembly.

2. **Flow Management Targets**: Spring floods (>6.2 m³/s) critical for native species recruitment (especially [[Roundtail Chub]], [[Desert Sucker]], [[Sonora Sucker]]). Absence of spring floods for 9 consecutive years (1996–2004) led to recruitment failure and population declines. Management implication: maintain spring flood frequency to support native persistence.

3. **Drought Vulnerability**: Native species experience high mortality during droughts (both juvenile and adult stages), while nonnatives show lower juvenile mortality and variable adult responses. [[Red Shiner]] and [[Green Sunfish]] benefit from drought via compensatory population growth when large-bodied natives decline. Management implication: drought mitigation (e.g., maintaining base flows, preserving deep refuge pools) disproportionately benefits natives.

4. **Summer Flow Effects**: Elevated summer flows (>5.7 m³/s) reduce [[Smallmouth Bass]] recruitment but have minimal effect on other species. Perturbation analysis showed decreasing summer high-flow threshold reduced yellow bullhead and green sunfish abundance by 35% and 52%, respectively. Management implication: strategic summer flow releases could suppress nonnative populations.

5. **Carrying Capacity Interactions**: Density dependence operates through aggregate biomass, creating exploitative competition. Small-bodied, high-fecundity species ([[Red Shiner]]: 2123 eggs/g, 1-yr maturity) respond rapidly to available carrying capacity when large-bodied natives decline. Perturbation analysis: 10% increase in K increased red shiner abundance by 17%. Management implication: habitat restoration increasing carrying capacity may disproportionately favor nonnatives under current flow regimes.

6. **Temporal Storage Effect**: Long-lived natives ([[Sonora Sucker]]: 5–10 yr lifespan) persist through unfavorable periods via adult survival, enabling coexistence with nonnatives over decadal timescales. However, prolonged absence of favorable conditions (spring floods) exhausts this buffer. Management implication: minimum flood frequency thresholds needed to prevent demographic collapse.

7. **Transferability for Management**: Framework readily applied to other systems by adjusting: (a) vital rates from local or congener studies, (b) flow thresholds from site-specific hydrology, (c) carrying capacity from biomass surveys. Enables scenario testing of flow management alternatives (e.g., dam operations, environmental flow prescriptions) before implementation.

8. **Uncertainty Quantification**: Perturbation analysis identified mortality rates and GSI as most influential parameters (e.g., 10% decrease in [[Desert Sucker]] mortality increased its abundance by 58%). Management implication: prioritize field studies quantifying these vital rates under different flow conditions to reduce model uncertainty.

9. **Climate Change Projections**: Model structure accommodates non-stationary flow regimes. Projected increases in drought frequency and decreases in spring snowmelt floods in [[Colorado River Basin]] (Christensen et al. 2004, Udall and Overpeck 2017) can be directly simulated to forecast community trajectories under climate scenarios.

10. **Conservation Prioritization**: Model identifies [[Roundtail Chub]] as particularly sensitive to spring flood absence (recruitment dependent on floods) and [[Sonora Sucker]] as vulnerable to prolonged low-flow periods. These species warrant targeted monitoring and flow-based conservation actions.

**Limitations for Management Application**: Model assumes closed community (no dispersal), which may overestimate extinction risk in connected river networks. Biotic interactions (predation, competition) emerge from density dependence rather than being explicitly parameterized, potentially underestimating nonnative impacts. Validation period (1994–2008) showed dampened fluctuations compared to observations, suggesting model may underestimate short-term variability. Sampling bias (underrepresentation of juveniles, deep-water adults) complicates validation but does not invalidate flow-response mechanisms.