---
name: r-data-exploration
description: Step-by-step data exploration in R before modeling (outliers, distributions, zeros, collinearity, relationships, independence), with original reusable scaffolds.
status: draft
generated: 2026-10-20
---

# r-data-exploration


Effective modelling of ecological count data—such as fish-trap surveys—requires a structured pre-analysis workflow. This protocol presents a step-by-step exploration sequence designed to inform model family selection, identify necessary transformations, and detect dependence structures before fitting generalized linear models (GLMs) or their extensions. The workflow below is adapted from the developer's own worked report [[src:fish-trapping-report]]; for further background on data exploration for GLMs see Zuur and Ieno (2021) [[src:zuur-ieno-2021]] (pointer only: its text was not read by this draft). Code blocks are original scaffolds **not executed here**; users should adapt them to their own datasets.

---

## 1. Outliers in Covariates

**Purpose:** Extreme values in predictors can distort parameter estimates and mask real ecological patterns. (unsourced)

**Method:** Dotplots (Cleveland plots) for each continuous covariate, ordered by observation index or magnitude. (unsourced)

**Decision informed:** Whether to remove erroneous records, transform skewed variables (e.g., log-transform distance), or retain extremes if biologically plausible [[src:fish-trapping-report]].

```r
library(ggplot2)
library(dplyr)

# Dotplot for continuous covariates
fish_long <- fish |>
  select(TrapID, DistanceFromShore, TrapDepth_m, SeasonalTemp_C) |>
  tidyr::pivot_longer(-TrapID, names_to = "Variable", values_to = "Value")

ggplot(fish_long, aes(x = Value, y = reorder(TrapID, Value))) +
  geom_point(size = 0.8, alpha = 0.6) +
  facet_wrap(~Variable, scales = "free_x") +
  labs(y = "Observation (ordered)", x = "Covariate value") +
  theme_minimal() +
  theme(axis.text.y = element_blank(), axis.ticks.y = element_blank())
```

---

## 2. Response Distribution and Zeros

**Purpose:** Count distributions determine the appropriate model family (Poisson, negative binomial, zero-inflated) and highlight overdispersion or excess zeros [[src:fish-trapping-report]].

**Method:** 
- Histogram of the response variable
- Calculate mean, variance, dispersion ratio (Variance ÷ Mean), and proportion of zeros (unsourced)
- Stratify by key factors (e.g., habitat type) [[src:fish-trapping-report]]

**Decision informed:** 
- Dispersion ratio > 1.5 suggests negative binomial over Poisson [[src:fish-trapping-report]]
- High zero proportion (>20–30%) may require zero-inflated or hurdle models [[src:fish-trapping-report]]

```r
# Summary statistics
fish |>
  summarise(
    n = n(),
    Mean = mean(TrapCount),
    Variance = var(TrapCount),
    Dispersion = Variance / Mean,
    Prop_zeros = mean(TrapCount == 0)
  )

# Histogram with mean overlay
ggplot(fish, aes(x = TrapCount)) +
  geom_histogram(bins = 30, fill = "steelblue", colour = "white") +
  geom_vline(aes(xintercept = mean(TrapCount)), 
             linetype = "dashed", colour = "red") +
  labs(title = "Distribution of trap counts",
       x = "Fish per trap", y = "Frequency")

# By habitat type
fish |>
  group_by(HabitatType) |>
  summarise(
    Mean = mean(TrapCount),
    Dispersion = var(TrapCount) / mean(TrapCount),
    Prop_zeros = mean(TrapCount == 0)
  )
```

---

## 3. Collinearity Among Predictors

**Purpose:** High collinearity inflates standard errors, making coefficient interpretation unstable (general). (unsourced)

**Method:** 
- Pairwise scatterplot matrix for continuous predictors (unsourced)
- Variance Inflation Factor (VIF) after fitting a preliminary linear model; VIF > 3–5 warrants concern (general) (unsourced)

**Decision informed:** Drop or combine collinear variables, or accept collinearity if prediction (not inference) is the goal (general). (unsourced)

```r
library(GGally)
library(car)

# Pairwise plots
fish |>
  select(DistanceFromShore, TrapDepth_m, SeasonalTemp_C) |>
  ggpairs()

# VIF from a preliminary linear model (for illustration only)
lm_prelim <- lm(TrapCount ~ DistanceFromShore + TrapDepth_m + 
                SeasonalTemp_C, data = fish)
vif(lm_prelim)
```

---

## 4. Covariate–Response Relationships

**Purpose:** Visualize bivariate associations to detect non-linearity, threshold effects, or interactions [[src:fish-trapping-report]].

**Method:** Scatterplots (continuous predictors) and boxplots (categorical predictors) of response versus each covariate. (unsourced)

**Decision informed:** Whether to include polynomial or spline terms, interaction effects, or treat a continuous variable as categorical (general). (unsourced)

```r
# Continuous covariate
ggplot(fish, aes(x = DistanceFromShore, y = TrapCount)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "loess", se = FALSE, colour = "red") +
  labs(x = "Distance from shore (km)", y = "Trap count")

# Categorical covariate
ggplot(fish, aes(x = HabitatType, y = TrapCount, fill = HabitatType)) +
  geom_boxplot() +
  labs(x = "Habitat type", y = "Trap count") +
  theme(legend.position = "none")
```

---

## 5. Replication and Random Effects

**Purpose:** Assess whether grouping variables (e.g., Region, Site) have sufficient replication to estimate random effects and avoid pseudoreplication [[src:fieberg-2009]].

**Method:** Count observations per level of each candidate random effect; minimum 5–10 levels recommended for stable variance component estimation (general). (unsourced)

**Decision informed:** Include random intercepts for Region or Site if replication is adequate; otherwise, treat as fixed effects [[src:fieberg-2009]].

```r
# Replication per region and site
fish |>
  count(Region, Site) |>
  print(n = Inf)

fish |>
  count(Region)
```

**Interpretation of random effects:** Mixed models yield **subject-specific** (SS) interpretations—the effect of a covariate change *within* the same site or individual—whereas population-averaged (PA) models (e.g., via generalized estimating equations) describe differences *among* groups [[src:fieberg-2009]]. For landscape-scale inferences (e.g., mean catch across habitat types), PA interpretations may be more natural [[src:fieberg-2009]].

---

## 6. Spatial and Temporal Independence

**Purpose:** Residual spatial or temporal autocorrelation indicates missing structure, potentially biasing standard errors and predictions [[src:fish-trapping-report]].

**Method:** 
- **Spatial:** Plot residuals against latitude/longitude; compute Moran's I or use DHARMa's spatial autocorrelation test (general) (unsourced)
- **Temporal:** Plot residuals versus survey date; check for trends or serial correlation [[src:fish-trapping-report]]

**Decision informed:** Add spatial or temporal random effects, include spatial coordinates as covariates, or use spatially explicit models (general). (unsourced)

```r
library(DHARMa)

# Fit preliminary GLM
m_prelim <- glm(TrapCount ~ DistanceFromShore + HabitatType + 
                offset(log(SoakTime_hr)),
                data = fish, family = poisson)

res <- simulateResiduals(m_prelim, n = 250)

# Spatial check (requires longitude, latitude)
testSpatialAutocorrelation(res, 
                           x = fish$Longitude, 
                           y = fish$Latitude)

# Temporal check
plot(fish$SurveyDate_num, residuals(m_prelim, type = "pearson"),
     xlab = "Survey date (numeric)", ylab = "Pearson residuals")
abline(h = 0, lty = 2, col = "red")
```

---

## Summary Checklist

1. **Outliers:** Dotplots → remove errors or transform (unsourced)
2. **Distribution & zeros:** Histogram, dispersion ratio, zero proportion → NB, ZIP, ZINB, or hurdle (unsourced)
3. **Collinearity:** Pairs plots, VIF → drop or combine predictors (unsourced)
4. **Relationships:** Scatterplots, boxplots → polynomial terms, interactions (unsourced)
5. **Replication:** Count per group → random vs. fixed effects (unsourced)
6. **Dependence:** Spatial/temporal residual plots → random effects or covariates (unsourced)

This workflow synthesizes foundational checks into a reproducible sequence. For fuller exposition and case studies, consult Zuur and Ieno (2021) [[src:zuur-ieno-2021]].
