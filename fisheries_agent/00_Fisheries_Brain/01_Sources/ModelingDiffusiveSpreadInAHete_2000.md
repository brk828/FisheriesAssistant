---
species:
  - Nocomis leptocephalus
  - Semotilus atromaculatus
  - Clinostomus funduloides
  - Lepomis auritus
  - Ameiurus natalis
  - Anguilla rostrata
  - Notropis procne
  - Notropis albeolus
  - Noturus insignis
  - Lepomis cyanellus
  - Lepomis macrochirus
  - Gambusia affinis
  - Lepomis gulosus
  - Percina spp.
target_species: Bluehead Chub (Nocomis leptocephalus)
common_name: Bluehead Chub
family: Cyprinidae
habitat: Small temperate stream, alternating pools, runs, and riffles
ocean_basin: N/A
location: Durant Creek, Wake County, North Carolina, USA
tags:
  - movement ecology
  - mark-recapture
  - diffusion model
  - population heterogeneity
  - stream fish
  - spatial dynamics
analytical_category:
  - diffusion-advection modeling
  - mark-recapture analysis
  - probit regression
  - maximum likelihood estimation
  - model validation
model_framework: Partial differential equation (diffusion-advection with population heterogeneity)
software_environment:
  - Not reported
data_requirements:
  - Individual mark-recapture data over multiple time intervals
  - Fish length measurements at each capture
  - Growth increments between captures
  - Spatial position (patch/site) at each capture
  - Minimum 30+ recaptures per species for statistical power
key_assumptions:
  - One-dimensional habitat structure
  - Two discrete subgroups (fast and slow dispersers)
  - No recruitment during study period
  - Fixed movement behavior within subgroups over time scale
  - Diffusive spread with constant advection rates
keywords_stubs:
  - "#leptokurtosis"
  - "#upstream_bias"
  - "#phenotypic_heterogeneity"
  - "#size_dependent_movement"
  - "#growth_rate_correlation"
  - "#spatial_spread"
  - "#elastomer_tagging"
title: "MODELING DIFFUSIVE SPREAD IN A HETEROGENEOUS POPULATION: A MOVEMENT STUDY WITH STREAM FISH"
source_id: "X-356f513a"
doc_type: "analyses_and_modeling"
source_citation: "G. T. Skalski, J. F. Gilliam (2000). MODELING DIFFUSIVE SPREAD IN A HETEROGENEOUS POPULATION: A MOVEMENT STUDY WITH STREAM FISH. Ecology 81(6): 1685-1700."
doi: "10.1890/0012-9658(2000)081[1685:mdsiah]2.0.co;2"
source_file: "Modeling diffusive spread in a hetero. pop. Skalski 2000..pdf"
text_extraction: "text"
---
# Modeling Diffusive Spread in a Heterogeneous Population: A Movement Study with Stream Fish

#ichthyology #Cyprinidae #movement_ecology #diffusion_modeling

## Analytical Objective & Scope

**Core Problem Addressed**: Explain the leptokurtic (high-peaked, long-tailed) movement distributions commonly observed in stream fish populations and test whether population heterogeneity in individual movement rates can generate these patterns. The study addresses why classic simple diffusion models (which predict normal distributions) fail to describe empirical movement data.

**Methodological Classification**: Novel adaptation. The authors extend the classic Skellam (1951) diffusion-advection model by incorporating population heterogeneity—structuring the population into two subgroups ("fast fish" and "slow fish") that diffuse at different rates. This represents a mechanistic hypothesis linking individual-level phenotypic variation (size, growth) to population-level dispersal patterns. The approach combines empirical mark-recapture analysis with mathematical model development, parameterization, and validation.

## Mathematical & Statistical Framework

**Model Formulation**: The population heterogeneity model consists of two coupled partial differential equations describing the spatial-temporal density of fast fish F(x,t) and slow fish S(x,t):

∂F/∂t = D_F(∂²F/∂x²) - μ_F(∂F/∂x)  (Eq. 3)

∂S/∂t = D_S(∂²S/∂x²) - μ_S(∂S/∂x)  (Eq. 4)

where D_F and D_S are diffusion coefficients, μ_F and μ_S are upstream advection rates for fast and slow fish, respectively. The solution for total density P(x,t) given an instantaneous point release of P₀ fish is:

P(x,t) = Z·P₀/√(4πD_Ft) · exp(-(x-μ_Ft)²/4D_Ft) + (1-Z)·P₀/√(4πD_St) · exp(-(x-μ_St)²/4D_St)  (Eq. 5)

where Z is the proportion of fast fish. The variance is:

Var(X) = 2(ZD_F + (1-Z)D_S)t + Z(1-Z)(μ_F - μ_S)²t²  (Eq. 6)

This reduces to linear increase when advection rates are equal.

**Variables & Covariates**: Response variables include (1) probability of movement (binary: 0=stay, 1=move), (2) direction of movement (downstream negative, upstream positive), (3) distance moved (number of sites/patches). Predictor variables: fish total length (mm), growth rate (mm/mo), time (days), species. Random effects: Not explicitly modeled. Spatial unit: discrete patches (pools and runs, 10-15 m length). Two data sets constructed: Data Set I (all observations, used for variance/kurtosis estimation and size/growth effects) and Data Set II (subset with balanced upstream/downstream sampling effort, used for mean/skewness estimation and model parameterization).

**Fit Diagnostics & Metrics**: Model parameterization via maximum likelihood estimation using one- and two-month movement distributions. Validation via Kolmogorov-Smirnov tests comparing predicted vs. observed distributions at three and four months (bluehead chub 3-mo: D=0.1349, N=59, P>0.20; 4-mo: D=0.1478, N=32, P>0.20). Model comparison via likelihood ratio tests (one vs. two subgroups: χ²=121.36, df=3, P<0.0001; one vs. three subgroups: χ²=137.32, df=6, P<0.0001; two vs. three subgroups: χ²=15.96, df=3, P=0.0012). Kurtosis estimates for bluehead chub over all intervals: 7.34 (SE=0.39, n=157, P<0.002). D'Agostino's test rejected normality for all four species (D<<0.0001, P<0.01 for each). Probit regression for bluehead chub probability of movement: size effect χ²=7.22, df=1, P=0.0072; growth effect χ²=5.16, df=1, P=0.0232; size×growth interaction χ²=6.42, df=1, P=0.0113; model fit χ²=147.81, df=145, P=0.4196. Parameter estimates for two-subgroup model (95% CI): D_F=0.4119 sites²/d (0.3189, 0.5461), D_S=0.0080 sites²/d (0.0048, 0.0142), μ_F=0.0541 sites/d (0.0284, 0.0801), μ_S=0.0051 sites/d (-0.0001, 0.0104), Z=0.5222 (0.4388, 0.6077).

## Data Requirements & Preprocessing

**Input Data Schema**: Mark-recapture study over five months (March-August 1996) with monthly sampling intervals. Total 610 fish marked, 478 recaptures representing 237 individuals. Four species with sufficient data: bluehead chub (216 recaptures), creek chub (123 recaptures), redbreast sunfish (54 recaptures), rosyside dace (28 recaptures). Minimum fish size: >40 mm total length. Spatial extent: 400-m marking section (37 sites), with 180 m searched downstream and up to 180 m upstream. Elastomer tagging allowed unique identification of up to 760 individuals using four colors and 10 anatomical positions. Zero-inflation: substantial, with 25-50% of fish showing zero net displacement over one-month intervals. Missing data: addressed through two-pass electrofishing and weighted/unweighted distribution comparisons (Kolmogorov-Smirnov tests showed distributions statistically indistinguishable, so unweighted data used). Temporal correlation analysis required fish captured in three consecutive months (bluehead chub: n=68 for growth correlation, n=84 for movement correlation).

**Sampling Cross-References**: [[Electrofishing Protocol]], [[Elastomer Tagging]], [[Mark-Recapture Design]], [[Stream Habitat Classification]], [[Block Seine Methods]], [[MS-222 Anesthesia Protocol]]. Sampling conducted with backpack electrofisher (Smith Root Model 12A POW) and 0.6-cm mesh block seines, two passes per site, moving upstream. Fish held in mesh laundry baskets, anesthetized in buffered MS-222, measured, marked, recovered, and released at capture site.

## Code Logic

Not reported. The document describes statistical procedures (probit regression, Kolmogorov-Smirnov tests, Spearman rank correlation, likelihood ratio tests, polynomial regression) and maximum likelihood parameter estimation but provides no pseudocode, R code, or Python implementations.

## Biological & Management Synthesis

**Model-to-Decision Mapping**: The population heterogeneity model provides a mechanistic framework for predicting spatial spread of stream fish populations, with direct implications for understanding colonization rates, recolonization following disturbance, and connectivity in fragmented habitats. The model's ability to generate persistent leptokurtosis (high-peaked, long-tailed distributions) over four months suggests that a minority of highly mobile individuals ("fast fish," ~52% of population with D_F=0.41 sites²/d) contribute disproportionately to long-distance dispersal, while "slow fish" (D_S=0.008 sites²/d, 50-fold slower) maintain local population structure. This has management implications: (1) restoration efforts should account for bimodal dispersal when predicting recolonization timescales; (2) barrier removal or fish passage design should consider that upstream bias (μ_F=0.054 sites/d for bluehead chub) may be species-specific and linked to phenotypic traits; (3) population viability assessments in fragmented streams should incorporate heterogeneous movement rates rather than assuming population homogeneity.

The empirical finding that probability of movement in [[Bluehead Chub]] varies nonlinearly with size and growth (with interaction effects) suggests that movement propensity is condition-dependent and potentially linked to fitness trade-offs. Fast-growing small fish and slow-growing large fish showed higher movement probability, indicating complex relationships between phenotype and dispersal that may reflect habitat quality assessment or competitive interactions. The temporal correlation in growth rates (F₁,₆₆=23.08, P<0.0001) demonstrates persistent individual heterogeneity, supporting the model's assumption of fixed "fast" and "slow" subgroups over ecologically relevant time scales.

For [[Creek Chub]], the decline in kurtosis from 6.65 at one month to 0.40 at four months (convergence to normality) suggests population homogenization over time, potentially through exchange between subgroups—a mechanism not included in the current model but identified as a key extension. This contrast with [[Bluehead Chub]] (persistent kurtosis=7.51 at four months) indicates species-specific differences in the stability of movement phenotypes.

The linear increase in variance with time (bluehead chub: slope t=10.16, P=0.002; creek chub: slope t=7.30, P=0.0053; quadratic terms nonsignificant) validates the diffusion framework while the leptokurtosis invalidates the classic Skellam model. Management applications requiring prediction of spatial spread (e.g., invasive species, stocking programs, barrier effects) should use heterogeneity-structured models rather than simple diffusion to avoid underestimating long-distance dispersal events.

The study identifies key research needs: (1) linking size/growth to movement mechanistically through fitness costs and benefits, (2) determining genetic vs. environmental bases for movement heterogeneity, (3) incorporating exchange rates between subgroups to explain temporal changes in kurtosis, (4) extending to continuous distributions of diffusion coefficients rather than discrete subgroups, (5) testing model predictions in metapopulation and fragmented habitat contexts. The framework is generalizable beyond stream fish to any system where individual heterogeneity in phenotype correlates with movement behavior.

#stream_ecology #dispersal_kernel #individual_variation #phenotype_movement_linkage #metapopulation_connectivity #habitat_fragmentation #colonization_dynamics #Neuse_River_basin #temperate_streams #cyprinid_ecology #centrarchid_ecology #ictalurid_ecology #anguillid_ecology #percid_ecology #poeciliid_ecology #electrofishing #spatial_ecology #advection_diffusion #partial_differential_equations #likelihood_methods #model_selection #AIC #movement_correlation #growth_heterogeneity #size_structure #upstream_migration #riffle_pool_habitat #one_dimensional_habitat