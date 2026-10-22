---
species: N/A
common_name: N/A
family: N/A
habitat: Colorado River, Grand Canyon riparian ecosystem
ocean_basin: N/A
location: Grand Canyon, Colorado River, Arizona
tags: #ecosystem-modeling #adaptive-management #river-ecology #Grand-Canyon #simulation-model #riparian-habitat #aquatic-production #sediment-transport
title: "Grand Canyon ecosystem model: Preliminary development of modeling shell and straw-man sub-models an overview for adaptive management workshop participants"
source_id: "14860"
minckley_id: "14860"
source_citation: "C. Walters, J. Buszowski, J. Korman and L. Gunderson (1998). Grand Canyon ecosystem model: Preliminary development of modeling shell and straw-man sub-models an overview for adaptive management workshop participants. Minckley Library ID: 14860."
source_file: "14860.pdf"
text_extraction: "ocr"
---
# Grand Canyon Ecosystem Model: Preliminary Development of Modeling Shell and Straw-Man Sub-models

#ichthyology #marine-biology #ecosystem-modeling #adaptive-management #river-ecology

## Executive Summary

This document presents a preliminary overview of the Grand Canyon Ecosystem Model (GCEM), a comprehensive simulation framework developed for adaptive management of the [[Colorado River]] ecosystem below [[Glen Canyon Dam]]. Prepared for a May 1998 workshop, the model integrates physical, biological, and socio-economic sub-models to evaluate alternative water management regimes. The modeling shell operates on a monthly timestep from 1948 to present, using historical forcing data to calibrate predictions against observed ecosystem changes. The framework divides the river into 12 reaches and simulates dam operations, flow routing, sediment transport, water quality, aquatic and riparian production, animal populations (both reach-scale and system-scale species), and recreation/cultural impacts. The model aims to support policy screening, research prioritization, and experimental management design for resolving uncertainties about ecosystem responses to flow management.

## Background & Description

The GCEM modeling shell consists of four interconnected sub-models. The **Physical Sub-model** simulates [[Glen Canyon Dam]] operations, flow routing through 12 river reaches, sediment transport and storage dynamics, and water quality parameters (temperature and oxygen). It uses historical monthly release volumes (1963-1997) and the PEAKSHAVE algorithm to generate hourly discharge patterns under different flow scenarios, including alternatives from the Environmental Impact Statement.

The **Aquatic Productivity and Riparian Habitat Sub-model** predicts benthic algal biomass as a function of flow, suspended sediment, and light penetration using depth-stratified calculations across reach-averaged cross-sections divided into two-foot depth slices. Detrital production drives benthic insect biomass dynamics. Riparian vegetation is categorized into five community types based on water table position: hydro riparian zone (HRZ) marsh, lower riparian zone (LRZ) dominated by tamarisk and willow, middle riparian zone (MRZ) with drought-resistant grasses, upper riparian zone (URZ) with mesquite and hackberry, and desert communities. Vegetation succession responds to stage fluctuations, flooding tolerance, and competitive interactions.

The **Animal Population Sub-model** employs two approaches: reach-scale population dynamics for species with localized life histories (small birds, snails) using simple recruitment-survival balance equations, and system-scale age-structured models for migratory fish species. The system-scale component uses delay-difference biomass dynamics for age k+ animals combined with Beverton-Holt recruitment relationships. Recruitment carrying capacity varies with habitat conditions through multiple life history stanzas, incorporating effects of food availability, predation risk, and physical habitat factors.

The **Recreation/Socio-economic/Cultural Sub-model** tracks campsite demand versus availability by reach, estimates trout fishing quality based on predicted fish abundance and growth, calculates power generation economics using PEAKSHAVE optimization, and provides indices of potential impacts on archaeological sites and ethnobotanical resources.

## Ecological & Environmental Context

The model addresses fundamental ecological questions about "top-down" versus "bottom-up" control of trophic processes in the [[Colorado River]] ecosystem. Post-dam flow stabilization substantially increased primary productivity in both aquatic and riparian habitats, with cascading effects on insect production and vertebrate populations. The framework explicitly represents behavioral mechanisms limiting trophic interactions, including the concept of foraging "arenas" where prey availability to predators depends on rapid behavioral exchanges rather than overall prey density.

For benthic systems, the model assumes donor-controlled (bottom-up) transfer from algal production to detritus to filter-feeding insects, with limited direct grazing. Available detritus concentration to filter feeders (D_a) follows the relationship: D_a = vD/(v + fB/V_f), where v is sinking/mixing rate, D is water column detritus concentration, f is filtering rate per biomass, B is filter feeder biomass per area, and V_f is effective foraging volume. This formulation predicts intense resource competition even when river-wide detritus concentrations are high.

Spatial distribution patterns for reach-scale species are predicted to follow: N_i = a_1 I_i / R_i - a_2, where N_i is population density in reach i, I_i is food density, R_i is predation risk, and a_1, a_2 are empirical parameters. This linear relationship emerges from assumptions about risk-sensitive foraging and the need for juveniles to achieve critical body size within limited time periods.

The sediment transport component addresses the critical challenge of representing processes occurring at minute-to-hour scales within a monthly timestep model. Sand storage in each two-foot depth slice responds to erosion and deposition rates that vary with water depth (as surrogate for shear velocity), slice sand content, suspended sediment concentration, and reach morphology (debris fans, scour pools). The model uses the exponential concentration profiling equation: C_i+1 = R_i/s_i + (C_i - R_i/s_i) × exp(-s_i × W_i × L_i / Q_i), where R_i is resuspension rate, s_i is sinking rate, C_i is upstream concentration, W_i is wetted width, L_i is reach length, and Q_i is discharge.

## Key Findings

**Model Structure and Capabilities**: The GCEM shell successfully integrates physical, biological, and socio-economic processes at appropriate spatial (12 reaches from Glen Canyon Dam to Lake Mead) and temporal (monthly timestep, 1948-present) scales. The framework allows interactive "game playing" for policy exploration while maintaining sufficient ecological realism through strategic simplification.

**Sediment Transport Challenges**: The sediment component remains highly preliminary and requires substantial refinement. Key uncertainties include: (1) whether to explicitly track sand in different morphology types (Fan Eddy Complexes, channel margins, scour pools) versus using morphology statistics to parameterize reach-averaged processes; (2) how to represent erosion rate dependence on slice sand content to capture armoring, grain size sorting, and slope effects; and (3) methods for predicting beach availability at different stages for recreation assessment.

**Trophic Relationships and Limiting Factors**: The model addresses vague ecological terminology by requiring precise definitions of "limitation" in dynamic terms. For reach-scale species, the framework predicts balanced population densities should be linearly related to overall food density with negative intercepts, a testable prediction that also serves as a diagnostic for top-down versus bottom-up control. Steep slopes in abundance-food relationships indicate high prey availability and likely top-down control requiring detailed predator-prey analysis.

**Fish Population Dynamics**: For system-scale fish species, the multi-stanza recruitment model (equation 6.3.4) allows representation of limiting factors at different life stages while maintaining computational efficiency. The initial equilibrium assumption (populations near balance prior to dam construction) substantially reduces parameter estimation complexity by allowing calculation of scaling parameters from growth-survival data and initial biomass estimates.

**Predation Risk Effects**: The Risk Ratio model (equation 6.3.12) predicts that juvenile survival varies as s_fs = exp[-Z_fs^other - Z_fs^pred × (r_fi / r_f0)], where predation mortality increases with the ratio of current to natural predator abundance per unit habitat (P/A). For species with high baseline juvenile mortality (Z_fs ≈ 5.0), doubling the risk ratio can reduce survival by 92%, from 0.67% to 0.09%.

**Primary Production Spatial Patterns**: Diurnal flow variations create complex spatial patterns in algal biomass depending on timing of stage peaks relative to photoperiod. Sites experiencing peak stage during daylight cannot support productive algal communities due to nocturnal desiccation, while sites peaking at night allow daytime shallow-water production despite higher turbidity. The model captures these effects through depth-slice-specific calculations of flooding duration H(r,d) and light-corrected production rates.

**Parameter Estimation Strategy**: The framework employs spatial gradients in food density and population abundance to estimate aggregate behavioral parameters (arena size, exchange rates, search rates) that cannot be directly measured. This approach allows empirical calibration while maintaining mechanistic linkages between individual-scale processes and population-level patterns.

**Recreation and Cultural Resources**: Campsite availability modeling requires linking sediment storage predictions by depth slice to beach inventory data classified by capacity, useable stage, and attraction. Archaeological site risk assessment needs reach-scale summaries of site numbers by elevation and sensitivity combined with erosion/deposition predictions, though site-specific predictions require higher-resolution two-dimensional models beyond this framework's scope.

**Model Development Priorities**: Critical needs identified for the May 1998 workshop include: (1) refinement of sediment transport relationships using monitoring data and detailed physical models; (2) definition of habitat linkage functions (K_fsh) relating carrying capacity to flow, temperature, turbidity, and substrate for key fish species; (3) empirical estimation of food-competition parameters (a_1, a_2) from spatial abundance-food density data; (4) specification of life history stanzas and associated habitat requirements for endangered species; and (5) validation of temperature and oxygen concentration predictions against downstream profile data.