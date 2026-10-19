---
species: []
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: ["Riverine", "Streams", "Freshwater"]
ocean_basin: "N/A"
location: ["Colorado River Basin", "United States", "American West"]
tags: ["threat assessment", "spatial modeling", "ecological integrity", "cumulative effects", "GIS", "conservation planning"]
analytical_category: ["Spatial Analysis", "Multi-Metric Index", "Threat Mapping", "Cumulative Effects Modeling", "Validation"]
model_framework: "Weighted aggregation of spatially explicit threat indices with upstream cumulative effects"
software_environment: ["GIS", "R"]
data_requirements: ["High-resolution hydrography (NHDPlus HR)", "Land use/land cover rasters", "Infrastructure vector layers", "Climate data", "Water withdrawal records", "Dam inventories", "In situ ecological integrity metrics"]
key_assumptions: ["Additive effects among threats within categories", "Inverse-distance weighting captures overland flow pathways", "Log-linear decay function for upstream cumulative effects based on discharge", "Expert-derived weights approximate relative threat contributions", "Threat indices serve as surrogates for field-based assessments"]
keywords_stubs: ["#threat_assessment", "#spatial_modeling", "#ecological_integrity", "#cumulative_effects", "#GIS", "#conservation_planning", "#Colorado_River_Basin", "#freshwater_conservation", "#multi_scale_analysis", "#benthic_macroinvertebrates", "#fish_assemblages", "#water_quality", "#hydrologic_alteration", "#habitat_fragmentation", "#geomorphology"]
title: "Multi-scale threat assessment of riverine ecosystems in the Colorado River Basin"
source_id: "X-4679b2ee"
doc_type: "analyses_and_modeling"
source_citation: "L. Comte, J. D. Olden, S. Lischka, B. G. Dickson (2022). Multi-scale threat assessment of riverine ecosystems in the Colorado River Basin. Ecological Indicators 138: 108840."
doi: "10.1016/j.ecolind.2022.108840"
source_file: "Olden et al. 2022 - Colorado River threat assesment.pdf"
text_extraction: "text"
---
# Multi-scale threat assessment of riverine ecosystems in the Colorado River Basin

#ichthyology #freshwater_ecology #conservation_science

## Analytical Objective & Scope

**Core Problem Addressed**: Developing spatially explicit threat indices to assess ecological integrity across the entire [[Colorado River Basin]] (>1,067,700 km of river network) in the absence of comprehensive field-based monitoring. The assessment aims to identify specific threats, pathways of impairment, and conservation priorities across perennial, intermittent, and ephemeral stream segments.

**Methodological Classification**: Novel adaptation combining existing spatial frameworks (inverse-distance weighting, flow accumulation analysis) with a comprehensive threat categorization system. The approach extends previous threat mapping efforts by: (1) accounting for three spatial extents of influence (valley bottom, catchment, river network); (2) incorporating upstream cumulative effects with discharge-based decay functions; (3) aggregating 69 individual threat indices into six threat categories using expert-derived weights; (4) validating threat indices against in situ ecological integrity metrics.

## Mathematical & Statistical Framework

**Model Formulation**: 

Valley bottom threat index for stream segment *i*:
$$T_{VB,i} = \frac{\sum_{j=1}^{n} w_j \cdot I_{j,i}}{A_i}$$
where *w_j* is threat intensity (0-1), *I_{j,i}* is presence/absence in cell *j*, and *A_i* is total valley bottom area.

Catchment threat index with inverse-distance weighting:
$$T_{C,i} = \frac{\sum_{j=1}^{n} w_j \cdot d_{j}^{-1} \cdot \log(FA_j) \cdot I_{j,i}}{\sum_{j=1}^{n} d_{j}^{-1} \cdot \log(FA_j)}$$
where *d_j* is distance to nearest stream, *FA_j* is flow accumulation (number of contributing cells).

Upstream cumulative effects with log-linear decay:
$$T_{cum,i} = \min\left(T_{local,i} + \sum_{k \in upstream} T_{local,k} \cdot e^{-\lambda \cdot \Delta Q_{i,k}}, T_{max}\right)$$
where Δ*Q* is difference in mean annual discharge between segments, λ is decay parameter, constrained to never exceed maximum local threat value.

Aggregated threat category:
$$T_{agg,i} = \frac{\sum_{m=1}^{M} w_m \cdot T_{m,i}}{\sum_{m=1}^{M} w_m}$$
where *w_m* are expert-derived relative weights (0-1 scale, normalized to sum to 1 within category).

Overall threat index (equal weighting across six categories):
$$T_{overall,i} = \frac{1}{6}\sum_{c=1}^{6} T_{agg,c,i}$$

Standardization via empirical cumulative distribution function applied independently to each threat index before aggregation.

**Variables & Covariates**: 

*Response variables* (validation): Benthic macroinvertebrate O/E score (n=181), fish multi-metric index (MMI, n=134), total nitrogen load (TNL, n=181), conductivity (COND, n=181), alteration magnitude of low flow (AMLF, n=194), alteration magnitude of high flow (AMHF, n=194), relative bed stability (RBS, n=172), instream habitat complexity (IHC, n=173).

*Predictor variables* (threat indices): 69 individual indices grouped into six categories: (1) Diffuse pollution (16 indices: urban development intensities, cultivated crops, pasture/hay, livestock ranching, timber production, fertilizer application, roads by class); (2) Point-source pollution (10 indices: coal/energy/metal/nonmetallic mines, abandoned mines, oil & gas wells/pipelines, wastewater treatment facilities, NPDES-permitted facilities, solar farms); (3) Flow regulation/uses (3 indices: instream water storage, water withdrawals, water pipelines); (4) Climate change (2 indices: annual precipitation trend 1950-2005, annual temperature trend 1950-2005); (5) Connectivity (10 indices: road/railway crossings by class, oil & gas pipelines, water pipelines, major/minor dams); (6) Geomorphology (28 indices: valley bottom footprint of urban development, agriculture, livestock, timber, transportation, mines, pipelines, facilities, nonnative vegetation).

*Spatial extents*: Valley bottom (mean area = 0.04 km²), catchment (mean area = 0.31 km²), river network (mean length = 0.57 km).

*Random effects*: Not applicable (spatial analysis, not mixed models).

*Offsets*: Water withdrawal and instream storage normalized by mean annual flow volume; threat indices standardized by empirical CDF.

**Fit Diagnostics & Metrics**: 

Validation via ordinary least squares regression between threat indices and ecological integrity metrics. Significant relationships (P < 0.05) found for: overall threat vs. macroinvertebrate condition (R² = 0.07), overall threat vs. fish condition (R² = 0.10), diffuse pollution vs. TNL (R² = 0.22), diffuse pollution vs. COND (R² = 0.18), point-source pollution vs. TNL (R² = 0.12), point-source pollution vs. COND (R² = 0.08), flow regulation/uses vs. AMHF (R² = 0.13), connectivity vs. IHC (R² = 0.09), geomorphology vs. RBS (R² = 0.04). Breusch-Pagan tests indicated homoscedasticity (all P ≥ 0.05); Kolmogorov-Smirnov tests confirmed normality of residuals except for AMLF.

Sensitivity analysis: Spearman correlations between original and randomized weights ranged 0.79-1.00; correlations with ±25% modified weights ranged 0.996-1.000 (coefficient of variation <1%), indicating robustness to weighting scheme.

Spatial covariation among threats: Mean Spearman's ρ = 0.15 within threat categories, 0.13 between categories. Individual threat contributions to aggregated indices: maximum values 12.1-83.3 (mean = 43.6), indicating most threats contribute substantially in at least some locations.

## Data Requirements & Preprocessing

**Input Data Schema**: 

*Minimum sample size*: Analysis conducted on >1,067,700 km of river network (all NHDPlus HR stream segments in Colorado River Basin). Validation datasets: n = 134-194 sites depending on metric. Watersheds (HUC12): 6,938 of 7,552 included after excluding those with >25% missing threat values or non-flowing habitats.

*Zero-inflation*: Not explicitly addressed; threat indices bounded 0-1 with many segments showing zero values for specific threats. Standardization via empirical CDF applied only to segments where threat detected (non-zero values).

*Missing data*: Stream segments outside U.S. borders or lacking discharge estimates excluded from watershed-scale aggregation. No imputation methods reported.

*Data preprocessing steps*:
1. Valley bottom delineation using Valley Bottom Extraction Tool (V-BET)
2. Flow direction and flow accumulation rasters generated for entire basin
3. Inverse-distance weighting calculated per catchment cell: distance to nearest stream × log(flow accumulation)
4. Upstream cumulative effects traced using flow accumulation with discharge-based decay
5. Individual threat indices standardized via empirical CDF (percentile transformation)
6. Aggregation using expert-derived weights normalized within categories
7. Validation metrics log-transformed when necessary to approximate normality

*Spatial resolution*: Threat calculations performed at 30m raster resolution; results attributed to stream segments (mean length 0.57 km).

**Sampling Cross-References**: Validation data from [[National Aquatic Resource Surveys]] (NARS 2008-2009, 2013-2014) and [[HydroMetric]] dataset (Eng 2018). See #NARS_sampling_design, #probabilistic_survey_design, #wadeable_streams for companion documents on field sampling protocols. Biodiversity index from [[EnviroAtlas]] based on IUCN range maps reallocated to HUC12 watersheds; see #species_distribution_modeling, #range_size_rarity for related methods.

## Code Logic

**Key pseudocode for valley bottom threat calculation**:
```
for each stream_segment in basin:
    valley_bottom = extract_valley_bottom(segment)
    for each threat_layer:
        threat_intensity = raster_values(threat_layer, valley_bottom)
        weighted_sum = sum(threat_intensity * cell_area)
        total_area = sum(valley_bottom_area)
        threat_index[segment] = weighted_sum / total_area
```

**Catchment-level inverse-distance weighting**:
```
for each stream_segment:
    catchment = delineate_catchment(segment)
    flow_direction = calculate_flow_direction(DEM)
    flow_accumulation = calculate_flow_accumulation(flow_direction)
    
    for each cell in catchment:
        distance_to_stream = euclidean_distance(cell, nearest_stream)
        weight = (1 / distance_to_stream) * log(flow_accumulation[cell])
        
    for each threat_layer:
        threat_presence = extract_values(threat_layer, catchment)
        numerator = sum(threat_presence * weight)
        denominator = sum(weight)
        threat_index[segment] = numerator / denominator
```

**Upstream cumulative effects with discharge decay**:
```
for each stream_segment in downstream_order:
    local_threat = calculate_local_threat(segment)
    upstream_segments = trace_upstream(segment)
    
    cumulative_threat = local_threat
    for each upstream_seg in upstream_segments:
        delta_discharge = discharge[segment] - discharge[upstream_seg]
        decay_factor = exp(-lambda * delta_discharge)
        cumulative_threat += local_threat[upstream_seg] * decay_factor
    
    # Constrain to never exceed maximum local value
    threat_index[segment] = min(cumulative_threat, max_local_threat)
```

**Aggregation with expert weights**:
```
# Standardize individual threats via empirical CDF
for each threat_index:
    non_zero_values = threat_index[threat_index > 0]
    percentiles = ecdf(non_zero_values)
    threat_index_standardized = percentiles(threat_index)

# Aggregate into categories
for each threat_category:
    weights = expert_weights[category]  # 0-1 scale
    weights_normalized = weights / sum(weights)
    
    aggregated_index = 0
    for each individual_threat in category:
        aggregated_index += weights_normalized[threat] * threat_index_standardized[threat]

# Overall threat index (equal weighting)
overall_threat = mean(aggregated_indices)  # 1/6 weight per category
```

**Validation regression**:
```
# Example: Overall threat vs. fish condition
model = lm(log(fish_MMI) ~ overall_threat_index)
summary(model)  # Extract R², P-value
breusch_pagan_test(model)  # Test homoscedasticity
kolmogorov_smirnov_test(residuals(model))  # Test normality
```

R packages likely used (not explicitly stated): `sf`, `raster`, `terra` for spatial operations; `lmtest` for diagnostic tests. Web application developed using GitLab Pages (https://wff-rivers.gitlab.io/mapping/).

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

The threat assessment framework directly informs spatial conservation planning through three management pathways:

1. **Priority watershed identification**: Overlay of overall threat index with native biodiversity index (EnviroAtlas) identifies four management contexts: (a) High biodiversity + low threat = conservation/protection candidates (e.g., Upper Gila, Sonora regions); (b) High biodiversity + high threat = restoration/enhancement candidates (e.g., White-Yampa, Colorado Headwaters, Salt, Middle Gila, Lower Colorado-Lake Mead); (c) Low biodiversity + high threat = potential write-offs or long-term recovery targets; (d) Low biodiversity + low threat = monitoring priorities. Example: Anderson Wash-Muddy River watershed identified as restoration priority due to exceptional biodiversity and high threat from two independent threat clusters (residential development + exploitative activities).

2. **Threat-specific management strategies**: Jackknife analysis reveals relative contributions of individual threats, enabling targeted interventions. Key findings: (a) Perennial streams face cumulative upstream threats requiring watershed-scale management; (b) Intermittent/ephemeral streams show localized threats (urbanization cluster: development + local roads + water withdrawals) amenable to valley-bottom restoration; (c) Livestock ranching, fertilizer application, and local roads contribute disproportionately to diffuse pollution (maximum contributions 43.6-83.3); (d) Water withdrawals dominate flow regulation/uses index, suggesting consumptive use reduction as primary hydrologic management lever; (e) Climate change (precipitation/temperature trends) acts largely independently, requiring adaptation strategies decoupled from other threat mitigation.

3. **Reference condition assessment**: Threat indices validated against biological (macroinvertebrate O/E, fish MMI), chemical (TNL, conductivity), hydrological (flow alteration), and physical (bed stability, habitat complexity) integrity metrics provide empirical benchmarks. Significant negative associations between overall threat and biotic condition (R² = 0.07-0.10) establish threat thresholds: stream segments in 90-100th percentile of overall threat show measurably impaired assemblages. Aggregated indices correlate with specific impairment pathways (e.g., diffuse pollution → elevated nitrogen R² = 0.22; flow regulation → reduced high flows R² = 0.13), enabling diagnosis of dominant stressors and prediction of ecological responses to threat reduction.

**Spatial prioritization outcomes**: Upper and Lower Green River, White-Yampa, and southwestern Basin (Lower Colorado) emerge as highest overall threat; San Juan, Little Colorado, and portions of Gila show comparatively lower threat. Perennial streams (14% of network) disproportionately threatened; intermittent streams (36%) show intermediate threat; ephemeral streams (50%) generally lower threat except near urban centers (Las Vegas, Phoenix, Tucson). Protected areas (GAP Status 1-2) cover portions of low-threat/high-biodiversity regions but gaps exist in southeastern Basin, highlighting expansion opportunities.

**Management caveats**: (1) Additive aggregation assumes no synergistic/antagonistic interactions among threats—likely underestimates cumulative impacts in multi-stressor contexts; (2) Moderate validation R² (0.04-0.22) indicates limited local-scale predictive power, necessitating field verification for site-specific decisions; (3) Expert-derived weights introduce subjectivity, though sensitivity analysis shows robustness (CV <1% for ±25% weight modifications); (4) Static assessment (circa 2016-2019 data) does not project future threats from population growth, climate change, or policy shifts; (5) Framework excludes non-additive threat interactions, invasive species impacts, and fine-scale habitat features (<30m resolution).

**Transferability**: Blueprint applicable to other large river basins with modifications: (1) Threat selection tailored to regional stressor profiles; (2) Weights calibrated via local expert elicitation or empirical relationships where validation data exist; (3) Spatial extents adjusted to basin size and data resolution; (4) Upstream decay functions parameterized using basin-specific discharge or environmental distance metrics. Interactive web application (https://wff-rivers.gitlab.io/mapping/) enables custom weight specification and data download for adaptive management.

#threat_assessment #spatial_modeling #ecological_integrity #cumulative_effects #GIS #conservation_planning #Colorado_River_Basin #freshwater_conservation #multi_scale_analysis #benthic_macroinvertebrates #fish_assemblages #water_quality #hydrologic_alteration #habitat_fragmentation #geomorphology #expert_elicitation #validation #biodiversity_hotspots #restoration_prioritization #climate_change_impacts #urbanization #agriculture #mining #flow_regulation #connectivity #floodplain_development