---
species: ["Xiphias gladius", "Thunnus alalunga", "Thunnus maccoyii", "Katsuwonus pelamis", "Thunnus albacares", "Thunnus obesus", "Makaira nigricans", "Prionace glauca", "Isurus oxyrinchus", "Lutjanus campechanus", "Cololabis saira", "Dissostichus mawsoni", "Larimichthys polyactis", "Molva molva", "Homarus gammarus"]
target_species: "N/A"
common_name: ["broadbill swordfish", "albacore tuna", "southern bluefin tuna", "skipjack tuna", "yellowfin tuna", "bigeye tuna", "blue marlin", "blue shark", "shortfin mako", "red snapper", "Pacific saury", "Antarctic toothfish", "small yellow croaker", "ling", "European lobster"]
family: ["Xiphiidae", "Scombridae", "Carcharhinidae", "Lamnidae", "Lutjanidae", "Scomberesocidae", "Nototheniidae", "Gadidae", "Nephropidae"]
habitat: ["pelagic", "demersal", "benthic", "reef"]
ocean_basin: ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Southern Ocean"]
location: ["global", "multiple ocean basins"]
tags: ["CPUE standardization", "stock assessment", "fishery-dependent data", "abundance indices", "statistical modeling", "best practices"]
analytical_category: ["CPUE standardization", "GLM", "GAM", "GLMM", "spatiotemporal modeling", "model selection", "uncertainty estimation", "data diagnostics"]
model_framework: ["GLM", "GAM", "GLMM", "GAMM", "spatiotemporal models (STM)", "VAST", "delta models", "hurdle models", "Bayesian models", "mixed-effects models", "geostatistical models"]
software_environment: ["R", "stats::glm", "mgcv", "brms", "TMB", "VAST", "R-INLA", "lme4", "glmmTMB", "nlme", "geepack", "DHARMa", "sdmTMB"]
data_requirements: ["catch data", "effort data", "operational-level records", "vessel ID", "spatial coordinates", "temporal resolution", "gear specifications", "environmental covariates", "species composition", "size/age/sex data", "logbook data", "observer data"]
key_assumptions: ["catchability proportional to abundance", "separability of fishing mortality", "constant selectivity through time", "independence of observations", "appropriate error distribution", "spatial stationarity", "no preferential sampling bias"]
keywords_stubs: ["#CPUE", "#standardization", "#GLM", "#GAM", "#spatiotemporal", "#catchability", "#selectivity", "#targeting", "#fleet-definition", "#data-exploration", "#model-diagnostics", "#uncertainty", "#preferential-sampling", "#effort-creep", "#misreporting", "#zero-inflation", "#delta-model", "#predict-then-aggregate", "#index-fishery", "#multispecies", "#environmental-covariates", "#spatial-correlation", "#random-effects", "#model-selection", "#AIC", "#residual-analysis", "#influence-plots", "#simulation-testing"]
title: "Catch per unit effort modelling for stock assessment: A summary of good practices"
source_id: "X-a1386ca0"
doc_type: "analyses_and_modeling"
source_citation: "S. D. Hoyle, R. A. Campbell, N. D. Ducharme-Barth, A. Grüss, B. R. Moore, J. T. Thorson, L. Tremblay-Boyer, H. Winker, S. Zhou, M. N. Maunder (2024). Catch per unit effort modelling for stock assessment: A summary of good practices. Fisheries Research 269: 106860."
doi: "10.1016/j.fishres.2023.106860"
source_file: "Hoyle et al. CPUE modeling for stock assessment.pdf"
text_extraction: "text"
---
# Catch per unit effort modelling for stock assessment: a summary of good practices

#ichthyology #Scombridae #Xiphiidae #Carcharhinidae #stock-assessment #CPUE-standardization

## Analytical Objective & Scope

**Core Problem Addressed**: This review synthesizes best practices for standardizing fishery catch-per-unit-effort (CPUE) data to produce reliable indices of relative abundance for stock assessments, particularly when fishery-independent surveys are unavailable. The fundamental challenge is removing confounding effects of changes in fishing practice (catchability variation) from observed catch rates so that standardized CPUE reflects true changes in stock density.

**Methodological Classification**: This is a comprehensive methodological review and synthesis document providing guidance across 16 decision areas in CPUE standardization. It represents an update and expansion of earlier reviews (particularly [[Maunder and Punt 2004]]), incorporating advances in spatiotemporal modeling, multispecies targeting analysis, and joint modeling of CPUE and composition data. The document does not present novel methods but rather synthesizes current best practices and identifies decision points where analysts must choose among alternative approaches.

## Mathematical & Statistical Framework

**Model Formulation**: The foundational catch equation relates catch (C), effort (E), catchability (q), and density (D):

C = qED

where D = N/A (N = abundance, A = area). CPUE = C/E = qD. Expanding to account for selectivity (s) and availability (a):

CPUE = (saqM)/A

where M is true abundance. The goal of standardization is to account for changes in q, s, and a to isolate changes in M.

**GLM/GAM Framework**: Most standardizations use generalized linear models or extensions:
- **GLM**: log(CPUE) = β₀ + Σβᵢxᵢ + ε, with categorical (year, area, vessel) and continuous covariates
- **GAM**: Includes smooth functions f(x) for continuous predictors: log(CPUE) = β₀ + Σf(xᵢ) + ε
- **GLMM**: Adds random effects for vessel, trip, or year-area interactions
- **Delta/Hurdle Models**: Two-stage approach modeling encounter probability (binomial) and positive catch rates (lognormal, Gamma) separately
- **Spatiotemporal Models (STM)**: Include spatial random fields ω(s) and spatiotemporal fields ε(s,t): log(CPUE(s,t)) = β₀ + Xβ + ω(s) + ε(s,t), with Matérn covariance structure

**Variables & Covariates**: 
- **Response**: Catch rate (continuous), catch counts (discrete), presence/absence (binomial)
- **Catchability Covariates**: Vessel ID, gear specifications (hooks-between-floats, net length), bait type, time of day, moon phase, fishing technique. These are "filtered out" by setting to reference levels during prediction.
- **Density Covariates**: Sea surface temperature, chlorophyll-a, dissolved oxygen, spatial coordinates, habitat variables. These are conditioned upon when predicting across space/time.
- **Targeting Indicators**: Species composition clusters, principal component scores from catch composition, catch ratios
- **Random Effects**: Vessel, trip, year-area interaction (when treated as nuisance parameters)
- **Offsets**: Effort (for count data models)

**Fit Diagnostics & Metrics**: 
- **Convergence**: Gradient checks, Hessian positive-definite
- **Residuals**: Probability-integral-transform (PIT) residuals via DHARMa package for non-Gaussian models; one-step prediction residuals for sequential data; QQ plots; spatial autocorrelation tests (Moran's I)
- **Goodness-of-Fit**: AIC, BIC, WAIC for model comparison; deviance explained (R²); conditional R² for mixed models; cross-validation (leave-one-out, k-fold)
- **Influence Diagnostics**: Step plots showing incremental covariate effects; coefficient-distribution-influence (CDI) plots quantifying relative influence; counterfactual analyses
- **Uncertainty**: Standard errors via delta method; canonical confidence intervals for categorical time effects; bootstrap methods; MCMC posterior distributions; observation error vs. process error
- **Model Validation**: Simulated data refitting to check Laplace approximation accuracy; comparison of observed vs. predicted distributions; coverage probability checks

## Data Requirements & Preprocessing

**Input Data Schema**: 
- **Minimum Requirements**: Catch (weight or numbers), effort (appropriate unit: hooks, sets, hours, days), spatial location (latitude/longitude or grid cell), temporal information (date, year, season), vessel identifier
- **Operational-Level Data Preferred**: Set-by-set or haul-by-haul records superior to aggregated data (trip, day, or spatial cell aggregates). Aggregation can mask fine-scale targeting changes, introduce bias in mean-variance relationships, and reduce ability to model autocorrelation.
- **Zero-Inflation**: Document proportion of zero catches; delta/hurdle models typically required when zeros exceed 5-10%; Tweedie distribution (1 < p < 2) can handle zeros in continuous framework
- **Missing Data**: Tabulate missingness by covariate; options include dropping records (if <5-10% missing), dropping covariates, rule-based imputation, or sophisticated geostatistical/Bayesian imputation. High missingness (>10%) requires sensitivity testing.
- **Sample Size Considerations**: Sufficient records per covariate level; random effects require >12 levels to estimate distribution shape; core fleet definitions often used to focus on vessels with consistent reporting
- **Outlier Treatment**: Identify via histograms, quantile-based thresholds; distinguish true extreme values from data entry errors; stakeholder consultation valuable

**Data Quality Issues**:
- **Misreporting**: Species misidentification (particularly bycatch); under-reporting (discards, high-grading, quota avoidance); over-reporting (establishing catch history); changes in reporting linked to regulations, e-monitoring, observer training
- **Temporal Changes**: Logbook form changes, data storage method changes, introduction of electronic monitoring, changes in species-specific recording
- **Spatial Resolution**: Finer resolution preferred; aggregation to coarse cells (e.g., 5° squares) can mask localized depletion, preferential sampling patterns
- **Effort Definition**: Must match biological process; inappropriate aggregation (e.g., catch per day when search time varies) can mask abundance declines

**Preprocessing Steps**:
1. **Exploratory Analysis**: Histograms/density plots of all variables; spatial-temporal maps of catch, effort, CPUE; time series of boxplots by strata; correlation analysis; random forest/BRT for variable importance
2. **Data Cleaning**: Remove obvious errors; apply biologically plausible bounds; check for duplicate records
3. **Covariate Engineering**: Create interaction terms; transform continuous variables if needed; define categorical bins for continuous variables when appropriate
4. **Spatial Domain Definition**: Define "core fishery" (e.g., cells with >500 total catch, or fished in >50% of years); consider edge effects and range contractions
5. **Targeting Classification**: Apply cluster analysis (k-means, hierarchical) to species composition; calculate principal components; define catch ratio groups
6. **Stakeholder Engagement**: Validate data patterns; clarify operational practices; identify unreported factors affecting catchability

**Sampling Cross-References**: #logbook-design #observer-programs #electronic-monitoring #species-identification #effort-definition #spatial-stratification #temporal-resolution #core-fleet-definition #data-quality-control #stakeholder-consultation #fishery-characterization #catch-composition-sampling

## Code Logic

**GLM Example (Base R)**:
```r
# Basic GLM with categorical and continuous predictors
model <- glm(cpue ~ factor(year) + factor(area) + factor(vessel) + 
             hooks_between_floats + sea_surface_temp,
             family = Gamma(link = "log"),
             data = catch_effort_data)

# Extract year effects
year_effects <- coef(model)[grep("year", names(coef(model)))]
```

**GAM with Splines (mgcv)**:
```r
library(mgcv)

# GAM with smooth terms and spatial interaction
model <- gam(cpue ~ factor(year) + s(hooks_between_floats, k=4) + 
             s(sea_surface_temp, k=4) + 
             te(longitude, latitude, k=c(10,10)) +
             factor(vessel),
             family = Gamma(link = "log"),
             method = "REML",
             gamma = 1.4,  # Increased penalty to avoid overfitting
             data = catch_effort_data)

# Cyclic spline for month
model_cyclic <- gam(cpue ~ factor(year) + s(month, bs="cc", k=12) + ...,
                    family = Gamma(link = "log"),
                    data = catch_effort_data)
```

**Delta Model (Two-Stage)**:
```r
# Stage 1: Binomial model for encounter probability
model_binomial <- glm(presence ~ factor(year) + factor(area) + ...,
                      family = binomial(link = "logit"),
                      data = catch_effort_data)

# Stage 2: Positive catch rates
model_positive <- glm(cpue ~ factor(year) + factor(area) + ...,
                      family = Gamma(link = "log"),
                      data = catch_effort_data[catch_effort_data$cpue > 0, ])

# Combine predictions
pred_encounter <- predict(model_binomial, newdata, type = "response")
pred_positive <- predict(model_positive, newdata, type = "response")
combined_index <- pred_encounter * pred_positive
```

**Random Effects (glmmTMB)**:
```r
library(glmmTMB)

# Vessel as random effect
model <- glmmTMB(cpue ~ factor(year) + factor(area) + (1|vessel),
                 family = Gamma(link = "log"),
                 data = catch_effort_data)
```

**Spatiotemporal Model (VAST)**:
```r
library(VAST)

# Configure VAST model
settings <- make_settings(n_x = 100,  # Number of spatial knots
                         Region = "User",
                         purpose = "index2",
                         bias.correct = TRUE)

# Fit model
fit <- fit_model(settings = settings,
                Lat_i = data$latitude,
                Lon_i = data$longitude,
                t_i = data$year,
                c_i = data$catch,
                b_i = data$effort,
                a_i = data$area,
                X1_formula = ~ factor(vessel) + hooks_between_floats,
                X2_formula = ~ factor(vessel) + hooks_between_floats,
                Q1_formula = ~ sea_surface_temp,  # Density covariate
                Q2_formula = ~ sea_surface_temp)

# Extract index
index <- plot_biomass_index(fit)
```

**Predict-Then-Aggregate**:
```r
# Create prediction grid covering stock domain
pred_grid <- expand.grid(
  year = unique(data$year),
  area = unique(data$area),
  vessel = reference_vessel,  # Set catchability covariates to reference
  hooks_between_floats = mean(data$hooks_between_floats),
  sea_surface_temp = data$sst_by_area_year  # Use actual density covariate values
)

# Predict for each cell
pred_grid$pred_cpue <- predict(model, newdata = pred_grid, type = "response")

# Aggregate by year, weighted by area
index <- pred_grid %>%
  group_by(year) %>%
  summarise(index = sum(pred_cpue * area_km2) / sum(area_km2))

# Calculate uncertainty via delta method or bootstrap
```

**Influence Plot (influ package)**:
```r
library(influ)

# Calculate influence of each covariate
influence_results <- calculate_influence(model, data)

# Plot CDI values
plot_cdi(influence_results)
```

**PIT Residuals (DHARMa)**:
```r
library(DHARMa)

# Calculate PIT residuals
sim_residuals <- simulateResiduals(fittedModel = model, n = 1000)

# Diagnostic plots
plot(sim_residuals)
testDispersion(sim_residuals)
testZeroInflation(sim_residuals)
testSpatialAutocorrelation(sim_residuals, x = data$longitude, y = data$latitude)
```

**Targeting via Cluster Analysis**:
```r
# Prepare species composition matrix (proportions)
comp_matrix <- catch_data %>%
  group_by(set_id) %>%
  mutate(prop = catch / sum(catch)) %>%
  select(set_id, species, prop) %>%
  pivot_wider(names_from = species, values_from = prop, values_fill = 0)

# Apply transformation
comp_matrix_trans <- asin(sqrt(comp_matrix[, -1]))

# Cluster analysis
clusters <- kmeans(comp_matrix_trans, centers = 4)

# Add cluster ID to original data
catch_data$target_cluster <- clusters$cluster[match(catch_data$set_id, comp_matrix$set_id)]

# Include in standardization model
model <- glm(cpue ~ factor(year) + factor(target_cluster) + ...,
             family = Gamma(link = "log"),
             data = catch_data)
```

## Biological & Management Synthesis

**Model-to-Decision Mapping**: 

**Index Construction and Interpretation**: The standardized CPUE index represents relative abundance of the stock component selected by the fishery, conditional on the spatial domain, selectivity, and availability assumptions. The index is used in stock assessment models via the catch equation, where catchability (q) and selectivity functions link the index to absolute abundance. Changes in the index drive perception of stock status (biomass relative to reference points like B_MSY) and population trends.

**Fleet Definition and Selectivity**: Proper fleet definition is critical for assessment outcomes. Each CPUE index in an assessment is associated with a fleet that samples a specific component of the stock. The assessment model estimates catchability and selectivity for each fleet. Fisheries should be defined to minimize selectivity changes through time by accounting for spatial-seasonal-gear variation. Alternative approaches include: (1) defining multiple fleets with stable selectivity; (2) joint modeling of CPUE and composition data to create separate index and extraction fleets; (3) using spatiotemporal models to account for changing effort distribution. Misspecification of selectivity (e.g., assuming constant when it varies) can bias abundance estimates and reference points.

**Catchability Trends and Effort Creep**: Long-term increases in fishing power ("effort creep") are nearly universal, with typical rates of 1-