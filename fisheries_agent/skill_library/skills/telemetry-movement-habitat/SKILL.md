---
name: telemetry-movement-habitat
description: Telemetry data analysis for fish movement and habitat use (error checks, independence, movement rates, mixed models, selection ratios, home range, resource selection) with R workflow.
status: draft
generated: 2026-10-20
---

# telemetry-movement-habitat

## Sampling Unit and Pseudoreplication

The most critical methodological decision when analysing fish telemetry data concerns the sampling unit (general). **Individual fish, not individual locations, must serve as the experimental unit** when making population-level inferences [[src:rogers-white-2007]]. Treating locations as independent observations constitutes pseudoreplication, which the source condemns strongly because it violates independence assumptions on two levels [[src:rogers-white-2007]]. 

First, successive locations from the same fish are temporally autocorrelated [[src:rogers-white-2007]]. Second, pooling location data across individuals eliminates natural between-individual heterogeneity, inflating Type I error rates [[src:rogers-white-2007]]. Study power derives primarily from the number of fish monitored rather than the number of locations per fish [[src:rogers-white-2007]]. 

## Location Error and Data Quality

Quantifying telemetry error is essential before analysis (general). Error stems from both positioning accuracy and coordinate transformation [[src:rogers-white-2007]]. For ultrasonic telemetry, error often increases with distance from shore or other reference points, potentially biasing seasonal movement estimates when fish aggregate offshore in winter [[src:rogers-white-2007]].

Concept sketch only; not executed.
```r
# Conceptual approach - check actual function names against sf documentation
library(sf)
# Calculate distance between true (GPS) and observed positions
position_error <- st_distance(gps_points, landmark_points)
# Model error as function of distance to shore
error_model <- lm(position_error ~ distance_to_shore)
```

## Autocorrelation: Not Always Problematic

Contrary to older perspectives, **serial autocorrelation between successive locations is not inherently problematic** when the individual is the sampling unit [[src:rogers-white-2007]]. In fact, more frequent sampling better describes what animals actually do, provided sampling is representative [[src:rogers-white-2007]]. The emphasis on obtaining uncorrelated location estimates has been misguided, allowing the more serious violation of pseudoreplication to persist [[src:rogers-white-2007]].

However, when modelling habitat relationships, temporal autocorrelation interacts with spatial autocorrelation in environmental covariates [[src:aarts-2008]]. This combination can underestimate parameter uncertainty and lead to spurious inclusion of irrelevant variables [[src:aarts-2008]]. The degree of dependence between observations depends on animal movement rates, observation frequency, and environmental spatial structure [[src:aarts-2008]].

## Movement Metrics

Movement should be quantified at temporal resolutions matching data collection (general). Common metrics include minimum displacement per hour or per day [[src:rogers-white-2007]]. **Expressing fish movement in centimeters per second is usually absurd** and implies unattainable precision [[src:rogers-white-2007]]. Movement data often exhibit increasing variance with increasing magnitude, warranting logarithmic transformation [[src:rogers-white-2007]].

```r
# Calculate minimum displacement - names illustrative only
library(sf)
fish_points_sf <- st_as_sf(fish_data, coords = c("x", "y"))
distances <- st_distance(fish_points_sf[-1,], fish_points_sf[-nrow(fish_points_sf),], by_element = TRUE)
time_intervals <- diff(fish_data$datetime)
movement_rate <- distances / time_intervals
log_movement <- log(movement_rate)
```

## Mixed Models for Movement and Habitat Analysis

Mixed-effects models treat fish as random effects while testing fixed effects of season, temperature, or other factors [[src:rogers-white-2007]][[src:aarts-2008]]. For movement analysis, interactions between fish and temporal factors (e.g., fish × season) can be included as random effects [[src:rogers-white-2007]]. Variance structures may need to account for heterogeneity across groups (e.g., seasonal differences in residual variance) [[src:rogers-white-2007]].

```r
# Example structure - verify against lme4/nlme documentation
library(lme4)
movement_model <- lmer(log(movement) ~ season + water_temp + 
                        (1|fish_id) + (1|fish_id:season), 
                      data = fish_data)
```

Spatial autocorrelation structures may be necessary when model residuals exhibit spatial clustering [[src:aarts-2008]]. This can indicate missing autocorrelated covariates or intrinsic processes like conspecific attraction [[src:aarts-2008]].

## Habitat Use Versus Availability

Selection occurs when animals use habitats disproportionately to their availability [[src:rogers-white-2007]][[src:aarts-2008]]. **Availability must reflect what is actually accessible to fish, not simply the total wetted area** [[src:rogers-white-2007]][[src:aarts-2008]]. Barriers (temperature gradients, vegetation, shallow water) restrict access [[src:rogers-white-2007]]. Accessibility surfaces can model the probability of reaching locations based on distance from haulout sites or movement constraints [[src:aarts-2008]].

Chi-square tests have traditionally assessed whether habitat use differs from availability, but these require maintaining individual identity rather than pooling data [[src:rogers-white-2007]]. Two log-likelihood tests evaluate whether fish use habitats similarly to each other and whether, collectively, they use habitats in proportion to availability [[src:rogers-white-2007]].

## Selection Ratios

Selection ratios ($\hat{w}_i$) equal usage divided by availability [[src:rogers-white-2007]]. Values exceeding one indicate selection; values below one indicate avoidance [[src:rogers-white-2007]]. Standard errors account for between-individual variation in selection, and **Bonferroni-adjusted simultaneous confidence intervals control family-wise error rates** when constructing intervals for multiple habitat types [[src:rogers-white-2007]]. The authors caution that sparse data (many expected counts below two) reduce reliability even though chi-square tests are robust to moderate deviations [[src:rogers-white-2007]].

```r
# Illustrative sketch - verify adehabitatHS documentation
library(adehabitatHS)
# Calculate selection ratios with individual variation
# selection_ratio_obj <- widesIII(u_data, a_data, alpha = 0.05)
# where u_data = usage matrix, a_data = availability vector
```

## Resource Selection Functions with Mixed Effects

Logistic regression approaches model habitat selection while incorporating continuous environmental variables [[src:rogers-white-2007]][[src:aarts-2008]]. Used locations are paired with "available" locations sampled from an accessibility distribution [[src:aarts-2008]]. The binary response (used = 1, available = 0) is regressed against environmental covariates [[src:aarts-2008]].

**Including individual as a random effect** addresses both between-individual heterogeneity and autocorrelation issues [[src:aarts-2008]][[src:fieberg-2009]]. However, researchers must recognize that **mixed-model parameters have subject-specific (SS) interpretations**: they describe how the response changes within an individual as that individual's covariates change [[src:fieberg-2009]]. For covariates that do not vary within individuals (e.g., sex), population-averaged (PA) interpretations from generalized estimating equations (GEE) may be more natural [[src:fieberg-2009]].

```r
# Sketch only - check glmmTMB or lme4 syntax carefully
library(glmmTMB)
rsf_model <- glmmTMB(used ~ depth + temperature + substrate + 
                      (1|fish_id), 
                    family = binomial, 
                    data = use_avail_data)
```

For flexible covariate effects, generalized additive structures can be incorporated using spline basis functions [[src:aarts-2008]]. Packages like `amt` (check_r_package) may facilitate these analyses, but users must verify function compatibility.

## Home Range Estimation

Home range methods estimate space use intensity (general). The `adehabitatHR` package (check_r_package) provides kernel density and other estimators. Researchers should recognize that **home range boundaries are arbitrary constructs** and that utilization distributions better represent continuous probability surfaces (general). (unsourced)

```r
# Conceptual only - verify adehabitatHR functions
library(adehabitatHR)
# Convert to spatial points, calculate kernel UD
# fish_sp <- SpatialPoints(coords)
# kud <- kernelUD(fish_sp[,"id"])
```

## Important Cautions

The authors stress several critical points: (unsourced)

- Telemetry studies are correlational; **only manipulative experiments reveal whether underutilized habitats are truly limiting** [[src:rogers-white-2007]]
- Even strong habitat associations may not indicate fitness consequences [[src:rogers-white-2007]]
- Heterogeneity in habitat use within populations is pervasive [[src:rogers-white-2007]]
- Model selection with autocorrelated data may favour overly complex models; **cross-validation provides a practical alternative to information criteria** when serial or spatial autocorrelation cannot be explicitly modelled [[src:aarts-2008]]
- Detectability may vary by habitat, biasing usage estimates unless paths are reconstructed at regular intervals [[src:aarts-2008]]
- Cross-correlation among environmental variables requires careful model selection, potentially guided by biological knowledge [[src:aarts-2008]]

**All substantive analytical decisions require checking function names against current package documentation (check_r_package), as syntax evolves.** (unsourced)
