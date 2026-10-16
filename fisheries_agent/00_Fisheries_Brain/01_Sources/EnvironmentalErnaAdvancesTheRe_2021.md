---
species:
  - Dreissena polymorpha
  - Dreissena rostriformis bugensis
  - Carassius auratus
  - Daphnia magna
  - Trachurus symmetricus
target_species: "Zebra Mussel (Dreissena polymorpha) and Quagga Mussel (Dreissena rostriformis bugensis)"
common_name: "Zebra and Quagga Mussels"
family: "Dreissenidae"
habitat: "Freshwater, benthic"
ocean_basin: "N/A"
location: "Lake Erie, Great Lakes, North America"
tags:
  - eDNA
  - eRNA
  - invasive species
  - degradation kinetics
  - molecular ecology
  - qPCR
analytical_category:
  - exponential decay modeling
  - linear mixed-effects models
  - degradation kinetics
  - ratio-based age estimation
model_framework: "First-order exponential decay; linear mixed-effects models (LMM)"
software_environment:
  - R
  - lme4
  - emmeans
data_requirements:
  - time-series eDNA/eRNA concentrations
  - qPCR quantification (copies/mL)
  - multiple gene targets (mitochondrial and nuclear)
  - replicated mesocosm treatments
  - minimum detection threshold (Ct < 35)
key_assumptions:
  - first-order exponential decay of nucleic acids
  - random shearing of genetic material
  - biphasic decay with initial log-linear phase (0-72 h)
  - independence of decay across gene targets
  - negligible transport in mesocosm setting
keywords_stubs:
  - "#eDNA_degradation"
  - "#eRNA_quantification"
  - "#ratio_RNA_DNA"
  - "#mitochondrial_vs_nuclear"
  - "#qPCR_efficiency"
  - "#legacy_DNA"
  - "#mesocosm_experiment"
  - "#dreissenid_mussels"
  - "#temporal_dynamics"
  - "#age_estimation"
title: "Environmental (e)RNA advances the reliability of eDNA by predicting its age"
source_id: "X-3a2a8281"
doc_type: "analyses_and_modeling"
source_citation: "N. T. Marshall, H. A. Vanderploeg, S. R. Chaganti (2021). Environmental (e)RNA advances the reliability of eDNA by predicting its age. Scientific Reports 11(1)."
doi: "10.1038/s41598-021-82205-4"
source_file: "Marshall et al. 2021 - eRNA advances reliabiltiy of eDNA.pdf"
text_extraction: "text"
---
# Environmental (e)RNA advances the reliability of eDNA by predicting its age

#ichthyology #dreissenidae #invasive-species #molecular-ecology

## Analytical Objective & Scope

**Core Problem Addressed**: Accurate estimation of the age and origin of environmental DNA (eDNA) is complicated by particle transport and legacy genetic material, leading to false positives and misinterpretation of species distribution. This study investigates degradation relationships between fragment size (long vs short), genomic origin (mitochondrial vs nuclear), nucleic acid type (eDNA vs eRNA), and RNA types (mRNA vs rRNA) to improve reliability of environmental genetic sampling.

**Methodological Classification**: Novel application combining multi-gene eDNA/eRNA quantification with ratio-based age estimation. Adapts existing first-order exponential decay models to compare degradation kinetics across genomic origins and nucleic acid types. The eRNA:eDNA ratio approach represents a novel predictor for estimating age of genomic material in aquatic environments.

## Mathematical & Statistical Framework

**Model Formulation**: First-order exponential decay model: Ct = C0e^(-k*t), where Ct is eDNA/eRNA concentration at time t (copies/mL), C0 is initial concentration at time 0, and k is the decay rate constant (per hour). Decay rates estimated as dC′/dt = -kC′, where C′ = Ct/C0 normalizes concentration. Biphasic decay analyzed over initial 72-h log-linear phase.

Linear mixed-effects model (LMM) for initial concentrations: loge(concentration at t=0) ~ gene region + mussel abundance + (gene region × abundance) + (1|replicate/sample). LMM for decay constants: loge(Ct/C0) ~ time + gene region + mussel abundance + (time × abundance) + (time × gene region) + (1|replicate/sample).

**Variables & Covariates**: Response variables: loge-transformed eDNA/eRNA concentrations (copies/mL), loge(Ct/C0) for normalized decay. Fixed effects: sampling time (continuous, 0-240 h), gene region (categorical: mt-16S, mt-COI, nu-18S, nu-H2B), mussel abundance (quantitative: 2, 6, 12, 24, 48 individuals), fragment length (categorical: short vs long). Random effects: samples nested within replicate tanks. Derived ratios: RatioS:L (short:long fragments), RatioR:D (eRNA:eDNA).

**Fit Diagnostics & Metrics**: qPCR efficiencies ranged 94.3-103.2% (within recommended 90-110% range). R² values for standard curves: 0.989-0.998. Detection threshold: Cycle threshold (Ct) > 35 considered non-detection. Post-hoc Tukey tests via emmeans package evaluated pairwise differences. Linear regression R² for RatioR:D temporal trends: mt-16S R² = 0.54, mt-COI R² = 0.40, nu-18S R² = 0.49. Significance levels: p < 0.001***, p < 0.005**, p = 0.009**.

## Data Requirements & Preprocessing

**Input Data Schema**: Minimum sample size: 13 mesocosm tanks (5 abundance treatments × 3 replicates, minus 2 removed for dead mussels, plus 1 negative control). Water samples: 100 mL collected at 0, 5, 12, 24, 48, 72, 144, 240 h post-mussel removal. Filtration: 1.2 µm glass microfiber filters (GF/C). Zero-inflation: H2B mRNA often undetected after 24 h (23.08% detection at 48 h); COI mRNA undetected after 72 h. Missing data: samples with Ct > 35 excluded from decay analysis as below detection limits. Detection rates at 240 h: ≤30.77% for eDNA markers (except COI: 0%), 69.23-100% for rRNA markers, 0% for mRNA markers.

Extraction protocol: Quick-DNA/RNA Miniprep Plus Kit (Zymo Research) with modified protocol including DNase treatment for eRNA. cDNA synthesis: SuperScript IV VILO Master Mix with oligo(dt)18 and random hexamer primers, including second DNase treatment (ezDNase) to remove eDNA carryover. qPCR: 2× Fast Plus EvaGreen Master Mix on Applied Biosystems QuantStudio Flex 6. Standard curves: log-diluted PCR products from 10^6 to 1 copies/reaction, run in quadruplicates.

**Sampling Cross-References**: #mesocosm_design #mussel_acclimation #water_sampling_protocol #filtration_controls #negative_controls #extraction_blanks #PCR_no_template_controls #temporal_sampling_design #abundance_gradient_experiment

## Code Logic

**R Statistical Analysis Workflow**:

```r
# Linear mixed-effects model for initial concentrations (time 0)
library(lme4)
library(emmeans)

# Model for shedding concentration
model_initial <- lmer(log(concentration) ~ gene_region * abundance + 
                      (1|replicate/sample), data = time0_data)

# Post-hoc Tukey tests
emmeans(model_initial, pairwise ~ gene_region)
emmeans(model_initial, pairwise ~ abundance)

# First-order exponential decay model (0-72 h)
# Normalize concentrations: C_prime = Ct/C0
data$C_prime <- data$Ct / data$C0

# LMM for decay constants
model_decay <- lmer(log(C_prime) ~ time * gene_region + 
                    time * abundance + 
                    (1|replicate/sample), 
                    data = decay_data)

# Extract decay constants (slope coefficients)
decay_constants <- coef(summary(model_decay))

# Calculate half-life from decay constant k
half_life <- log(2) / k  # where k is decay constant

# Ratio analysis
data$RatioS_L <- data$short_fragment / data$long_fragment
data$RatioR_D <- data$eRNA / data$eDNA

# Linear regression for temporal ratio changes
lm_ratio <- lm(log10(RatioR_D) ~ time, data = data)
summary(lm_ratio)  # Extract R² and p-value
```

**qPCR Quantification**: Standard curves constructed from diluted PCR products quantified using Quant-it Picogreen. Reactions: 20 µL volume with 10 µL 2× Master Mix, 0.5 µL each primer (10 mM), 6.5 µL diH2O, 2.5 µL template. Cycling: 10 min at 94°C, then 40 cycles of 94°C for 15 s and 60°C for 60 s.

## Biological & Management Synthesis

**Model-to-Decision Mapping**: The eRNA:eDNA ratio (RatioR:D) provides a quantitative predictor for estimating age of genomic material in environmental samples. All three gene regions showed RatioR:D decreased by orders of magnitude over 240 h: rRNA markers (mt-16S, nu-18S) decreased from >1000× to ~10× that of eDNA; mRNA (mt-COI) decreased from ~30× to ~1× that of eDNA. This temporal decline enables discrimination between fresh and legacy genetic material, reducing false positives from transported or persistent eDNA.

**Management Applications for [[Dreissena]] Detection**: (1) **Enhanced Detection Sensitivity**: rRNA genes (16S, 18S) found at >1000× higher concentrations than eDNA, improving detection probability for low-abundance invasive populations. (2) **Temporal Resolution**: Detection of mitosis-associated mRNA (H2B) indicates recent presence (<24 h) of living organisms, providing high-confidence early detection. (3) **Age Estimation**: RatioR:D regression models (R² = 0.40-0.54) enable estimation of time since genetic material release, improving interpretation of positive detections in invasion monitoring programs. (4) **Biomass Relationships**: Both eDNA and eRNA shedding rates increased significantly with mussel abundance (p = 0.009**), supporting quantitative applications for estimating population density.

**Reference Points**: Half-life estimates for eDNA: mt-16S (16.23-21.07 h), mt-COI (15.47-19.86 h), nu-18S (13.38-16.78 h), nu-H2B (13.00-16.78 h). Half-life estimates for eRNA: mt-16S (11.36-13.54 h), mt-COI (10.65-12.51 h), nu-18S (8.84-10.09 h). eRNA displayed ~4-5 h faster half-life than corresponding eDNA markers. Detection persistence: eDNA markers detected at 240 h in 0-31% of tanks; rRNA markers detected at 240 h in 69-100% of tanks; mRNA markers undetected after 24-72 h.

**Genomic Marker Selection**: Nuclear DNA (18S, H2B) released in higher initial concentrations than mitochondrial DNA (16S, COI), contrary to traditional assumptions about mitochondrial copy number advantages. No significant difference in decay rates between long and short fragments (141 vs 341 bp for 16S; 75 vs 251 bp for H2B), though weak increase in RatioS:L for H2B (R² = 0.09) suggests slight preferential degradation of longer fragments. Results support multi-gene approaches targeting both nuclear rRNA (high concentration, persistent) and mitosis-associated mRNA (low concentration, rapid decay) for comprehensive invasion monitoring.

**Methodological Considerations**: Study conducted in controlled mesocosms at ~20°C without UV exposure or water flow, potentially underestimating degradation rates in natural systems. Filtration at 1.2 µm may exclude subcellular eDNA fragments, affecting size-dependent degradation patterns. Natural environments involve continuous input of new genetic material from multiple individuals, complicating RatioR:D interpretation compared to single-pulse mesocosm releases. Temperature, pH, salinity, UV radiation, and microbial activity will modulate decay rates in field applications. Cross-references for field implementation: #water_temperature_effects #UV_degradation #microbial_enzymatic_activity #particle_transport #legacy_DNA_persistence #spatiotemporal_mixing #early_detection_protocols #invasion_monitoring_design