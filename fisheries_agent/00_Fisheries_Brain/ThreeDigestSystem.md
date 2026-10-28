**Refined Categorization Strategy:** Transition from generic informative summaries (biology, behavior, conservation) to **specialized, domain-aware Markdown schemas** based on paper focus:
* **Analyses &amp; Modeling:** Dedicated sections/files for statistical techniques, mathematical models, and quantitative workflows.
* **Sampling Design:** Structured breakdowns of field sampling protocols, spatial/temporal controls, and gear specifics.
* **Ecological &amp; Biological Synthesis:** Key conclusions, behavior, and management implications.


## YAML Headers
* **Analyses &amp; Modeling**
\--- title: "Document Title Here" doc\_type: "analyses\_and\_modeling" # Primary designation tag analytical\_category: - "Stock Assessment" - "Population Dynamics" - "Catch-Curve Analysis" model\_framework: "Bayesian State-Space / GAM / Integrated Population Model" software\_environment: - "R (TMB, mgcv)" - "Python (PyMC)" target\_species: - "Common Name (Scientific Name)" data\_requirements: - "Age-length keys" - "Catch per unit effort (CPUE) time-series" key\_assumptions: - "Closed population during sampling interval" - "Stationary gear detectability" keywords\_stubs: - "#bayesian-inference" - "#mortality-estimation" - "#population-model" ---


* **Sampling Design**
\--- title: "Document Title Here" doc\_type: "sampling\_design" # Primary designation tag sampling\_type: - "Stratified Random Survey" - "Electrofishing Protocol" - "Mark-Recapture" - "Trawl Survey" target\_species: - "Common Name (Scientific Name)" gear\_types: - "Boat Electrofisher (GPP 5.0)" - "Gillnet (Experimental Mesh)" spatial\_scale: "Basin-wide / Estuarine / Site-specific" temporal\_frequency: "Seasonal / Annual / Continuous" sample\_size\_requirements: - "Minimum 30 transects per stratum" - "Power analysis target: 80% detection probability" environmental\_covariates: - "Water Temperature (°C)" - "Dissolved Oxygen (mg/L)" - "Turbidity / Secchi Depth" - "Conductivity" keywords\_stubs: - "#field-protocol" - "#gear-standardization" - "#sampling-design" - "#survey-stratification" ---

* **Ecological &amp; Biological Synthesis**
\--- title: "Document Title Here" doc\_type: "ecological\_and\_biological" # Primary designation tag focus\_domains: - "Species Biology" - "Behavior &amp; Movement" - "Ecology &amp; Habitat" - "Conservation &amp; Status" - "Management Guidance" target\_species: - "Common Name (Scientific Name)" life\_stages\_covered: - "Larval / Juvenile / Adult / Spawning Stock" geographic\_region: - "Basin / River / Coastal / Estuarine System Name" conservation\_status: - "Endangered / Threatened / Species of Concern / Stable" management\_jurisdiction: - "State / Federal / Tribal / Regional Fishery Management Council" keywords\_stubs: - "#species-biology" - "#habitat-use" - "#spawning-migration" - "#conservation-status" - "#management-guidelines" ---


## Markdown Structure

* **Analyses &amp; Modeling**
1. Analytical Objective & Scope
Core Problem Addressed: Concise breakdown of the statistical or mathematical challenge solved by the study
Methodological Classification: Clarification of whether the study presents a novel statistical method, an adaptation of an existing model, or a standard empirical application.

2. Mathematical & Statistical Framework
Model Formulation: Primary equations, state-space representations, or likelihood functions.
Variables & Covariates: Explicit definitions of response variables, predictors, random effects, and offset terms.
Fit Diagnostics & Metrics: Reported convergence parameters, posterior uncertainty intervals, or model selection criteria (e.g., AIC, WAIC, $R^2$).

3. Data Requirements & Preprocessing
Input Data Schema: Structural requirements for input matrices/dataframes (e.g., minimum sample size, handling of zero-inflation or missing observations).
Sampling Cross-References: Keyword stubs linking to companion field technique or sampling design documents.

4. Code Logic & Dynamic Skill Stubs
Executable Code Snippets: Key pseudocode, R scripts, or Python functions that execute the analysis.
Skill Auto-Generation Markers: Modular text stubs formatted so the ICM project installer can ingest them to auto-generate dynamic, project-specific analysis skills for the user's workspace.

5. Biological & Management Synthesis
Model-to-Decision Mapping: Direct translation of analytical results into biological reference points, conservation status updates, or fisheries management guidance

* **Sampling Design**
1. Survey Objectives & Target Population
Primary Sampling Purpose: Specific management or biological question driving the field survey (e.g., relative abundance indexing, occupancy modeling, habitat association).
Target Population & Spatial Boundaries: Geographic scope, target life stages, and defined sampling universe.

2. Gear Specifications & Standardization
Equipment & Mesh/Gear Parameters: Detailed specifications of sampling gear (e.g., net length/mesh sizes, voltage/pulse settings, hook sizes).
Deployment & Effort Standardization: Standard operating procedures for gear deployment, soak time, transect length, or sweep duration to ensure comparability across sites and time.
Selectivity & Bias Considerations: Known gear biases, size-selectivity curves, and environmental factors affecting catchability ($q$).

3. Experimental & Spatial Design Framework
Stratification & Allocation: Rules for spatial stratification (e.g., depth zones, stream order, substrate type) and sample unit allocation (random, systematic, adaptive).
Temporal Scheduling: Timing considerations (e.g., diel cycles, seasonal migration windows, hydrologic conditions).
Detection & Bias Mitigation: Methods to account for non-detection, gear avoidance, or spatial clustering.

4. Field Data Schema & Variable Definitions
Primary Biological Measurements: Measurements captured in the field (e.g., total length, weight, sex, maturity stage, tissue sampling protocols).
Environmental & Spatial Covariates: Required abiotic readings collected concurrently at sampling stations.
QA/QC & Data Entry Protocols: Data validation rules, standardized codes, and field datasheet requirements.

5. Analytical Linkages & Dynamic Skill Stubs
Downstream Model Compatibility: Explicit references linking this sampling protocol to analytical schemas (e.g., "Feeds into Occupancy Model schema" or "Requires CPUE Standardization in R").
Skill Auto-Generation Markers: Modular text stubs enabling the ICM project installer to extract sampling protocols and generate custom field-prep or data-cleaning skills for the user's workspace [2].


* **Ecological &amp; Biological Synthesis**
1. Species Profile & Ecological Context
Taxonomic & Life-History Summary: Core biological parameters (e.g., max age, age-at-maturity, fecundity, growth parameters like Von Bertalanffy $L_\infty, k$).
Habitat Associations: Substrate requirements, thermal tolerances, salinity ranges, and velocity preferences across different life stages.

2. Behavioral & Ecological Findings
Movement Patterns & Migration: Diel movements, seasonal spawning migrations, home range estimates, or straying behavior.
Trophic & Community Interactions: Diet composition, predator-prey dynamics, competitive interactions, or invasive species pressures.
Environmental Drivers: Response to hydrologic regimes, water temperature fluctuations, flow thresholds, or habitat fragmentation.

3. Conservation Status & Population Dynamics
Population Trajectory: Observed trends in abundance, recruitment variability, or mortality drivers.
Threat & Risk Assessment: Primary stressors (e.g., passage barriers, habitat degradation, climate impacts, overexploitation).

4. Management Guidance & Policy Takeaways
Actionable Recommendations: Specific management interventions supported by the paper (e.g., minimum instream flow requirements, seasonal closures, stocking targets, barrier removals).
Biological Reference Points: Critical threshold values cited for management action (e.g., target mortality rates, habitat volume indices).

5. Keyword Stubs & Cross-Schema Linkages
Companion Cross-References: Keyword stubs linking this document to companion Analyses & Modeling or Sampling Design schemas in the library (e.g., linking a spawning study to an electrofishing protocol or catch-curve model stub).
ICM Installer Context Stubs: Structured text tags enabling the Interpretable Context Methodology (ICM) wizard to pull this species/ecosystem knowledge into a tailored project workspace based on the user's selected species and goals.
