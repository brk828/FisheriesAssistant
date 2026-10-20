---
name: count-glm-supplement
status: draft
generated: 2026-10-20
---

# count-glm: supplement from developer-supplied sources


## The model ladder

The primary challenge in count modelling is that **dispersion** (the variance relative to the mean) and **excess zeros** cannot usually be assumed away [[src:fish-trapping-report]]. You move through a **progressive testing ladder** from simple to complex:

1. **Poisson GLM** – baseline assumption; variance equals mean (general). (unsourced)
2. **Negative binomial GLM** – relaxes equidispersion; variance = μ + μ²/k [[src:fish-trapping-report]].
3. **Zero-inflated Poisson (ZIP) or Zero-inflated NB (ZINB)** – splits zeros into "structural" (habitat unsuitable) and "sampling" sources [[src:fish-trapping-report]].
4. **Hurdle models** – separate Bernoulli presence/absence model from truncated count model [[src:fish-trapping-report]].
5. **GLMM** – adds random intercepts when traps cluster by site or region [[src:fish-trapping-report]].
6. **AR(1) GLMM** – absorbs within-site temporal autocorrelation [[src:fish-trapping-report]].

Generalized Poisson (GP) and Conway-Maxwell-Poisson (CMP) distributions offer finer tuning of dispersion but rarely outperform NB in fisheries applications; reserve them for special scientific hypotheses about variance structure [[src:fish-trapping-report]].

---

## Testing dispersion and selecting NB

Before abandoning the Poisson, compute the **Pearson dispersion statistic** [[src:fish-trapping-report]]:

```r
# Manual Pearson chi-square dispersion
phi_hat <- sum(residuals(m_pois, type = "pearson")^2) / m_pois$df.residual
```

Values substantially above 1.0 (rule-of-thumb: >1.5) signal overdispersion [[src:fish-trapping-report]]. Follow up with a formal **score test** using `AER::dispersiontest()`, which tests H₀: Var = μ against H₁: Var = μ + α·μ² [[src:fish-trapping-report]]. A significant result (p < 0.05 and α̂ > 0) mandates moving to the **Negative Binomial** family [[src:fish-trapping-report]].

The NB introduces a dispersion parameter *k* (often called `theta` in R). As *k* → ∞ the NB converges to Poisson; small *k* indicates heavy overdispersion [[src:fish-trapping-report]]. Fit in R with `MASS::glm.nb()` [[src:fish-trapping-report]].

---

## Deciding on zero-inflation or hurdle

When the observed proportion of zeros exceeds what a Poisson or NB predicts—especially if certain habitats are ecologically unsuitable—consider zero-inflated or hurdle models [[src:fish-trapping-report]]. 

- **ZIP / ZINB**: a mixture model where a binomial process governs structural zeros and a Poisson/NB generates counts [[src:fish-trapping-report]]. Use `pscl::zeroinfl()` with `dist = "poisson"` or `dist = "negbin"` [[src:fish-trapping-report]].
- **Hurdle**: the zero/non-zero decision is modelled separately from positive counts (truncated NB). No mixing occurs at zero [[src:fish-trapping-report]]. Fit with `pscl::hurdle(..., dist = "negbin")` [[src:fish-trapping-report]].

Specify zero-inflation predictors (e.g., habitat type) after the `|` in the formula [[src:fish-trapping-report]].

---

## Adding random effects for nested designs

Trap data often exhibit **hierarchical clustering**: multiple traps per site, multiple sites per region [[src:fish-trapping-report]]. Ignoring this treats traps at the same site as independent, which pseudoreplicates the data and deflates standard errors [[src:fieberg-2009]]. A **GLMM** adds random intercepts that model residual correlation within clusters [[src:fish-trapping-report]].

Fit in `glmmTMB` with nested random effects `(1 | Region/Site)`: (unsourced)

```r
library(glmmTMB)
m_glmm <- glmmTMB(
  TrapCount ~ DistanceFromShore + HabitatType + TrapDepth_m +
              offset(log(SoakTime_hr)) + (1 | Region/Site),
  data = fish,
  family = nbinom2
)
```

The `nbinom2` family parameterizes Var = μ + μ²/φ [[src:fish-trapping-report]]. Extract variance components with `VarCorr()` [[src:fish-trapping-report]]. Marginal R² reflects fixed effects alone; conditional R² includes random effects [[src:fish-trapping-report]]. Use `MuMIn::r.squaredGLMM()` to compute both [[src:fish-trapping-report]].

If zero-inflation remains after accounting for clustering, specify `ziformula = ~ <predictors>` in `glmmTMB()` [[src:fish-trapping-report]].

---

## DHARMa residual diagnostics

Standard Pearson or deviance residuals are hard to interpret for non-Gaussian GLMs because their theoretical distribution changes with fitted μ [[src:fish-trapping-report]]. **DHARMa** transforms them into **quantile residuals** uniform on [0,1] under a correct model, regardless of family [[src:fish-trapping-report]].

```r
library(DHARMa)
res <- simulateResiduals(fittedModel = m_nb, n = 500)
plot(res)
testDispersion(res)
testZeroInflation(res)
```

A QQ-plot tracking the diagonal and non-significant dispersion/zero-inflation tests indicate adequate fit [[src:fish-trapping-report]].

**Pitfall**: `pscl::zeroinfl` objects lack a `simulate()` method, so DHARMa cannot be applied directly [[src:fish-trapping-report]] (general: you must switch to `glmmTMB` with `ziformula` for DHARMa-compatible zero-inflated models).

### Spatial autocorrelation

```r
testSpatialAutocorrelation(res, x = fish$Longitude, y = fish$Latitude)
```

Moran's *I* tests whether residuals cluster in geographic space [[src:fish-trapping-report]]. Significance suggests unmeasured spatial covariates or the need for spatial random effects (general).

### Temporal autocorrelation (aggregated)

When multiple traps share the same sampling date, first aggregate residuals per unique time point with `recalculateResiduals(res, group = <time_var>)`, then test: (unsourced)

```r
res_temporal <- recalculateResiduals(res, group = fish$SurveyDate_num)
testTemporalAutocorrelation(res_temporal, time = unique(sort(fish$SurveyDate_num)))
```

[[src:fish-trapping-report]].

### Per-site temporal autocorrelation

A global aggregated test masks site-specific patterns [[src:fish-trapping-report]]. Extract DHARMa scaled residuals, subset by site, and apply `Box.test(..., type = "Ljung-Box")` independently to each time series [[src:fish-trapping-report]]:

```r
sites <- levels(fish$Site)
dh_res <- residuals(res)
pval <- numeric(length(sites))

for (i in seq_along(sites)) {
  sel <- fish$Site == sites[i]
  site_time <- fish$SurveyDate_num[sel]
  site_res <- dh_res[sel]
  tt <- Box.test(site_res[order(site_time)], lag = 1, type = "Ljung-Box")
  pval[i] <- tt$p.value
}

p_adj <- p.adjust(pval, method = "BH")  # Benjamini-Hochberg correction
```

Sites with adjusted *p* < 0.05 warrant further investigation [[src:fish-trapping-report]].

---

## Absorbing temporal autocorrelation with AR(1)

When per-site tests flag persistent autocorrelation, fit an **AR(1) GLMM** in `glmmTMB` [[src:fish-trapping-report]]:

```r
# Create a time factor with the same ordered levels across all sites
fish$Time_fac <- factor(fish$SurveyDate_num, 
                        levels = sort(unique(fish$SurveyDate_num)))

m_ar1 <- glmmTMB(
  TrapCount ~ DistanceFromShore + HabitatType + TrapDepth_m +
              offset(log(SoakTime_hr)) + 
              (1 | Region/Site) +
              ar1(Time_fac + 0 | Site),  # AR1 correlation within Site
  data = fish,
  family = nbinom2
)
```

The AR(1) term models Corr(εᵢₜ, εᵢ,ₜ₊ₖ) = ρᵏ [[src:fish-trapping-report]]. It requires a factor whose levels are identical and ordered across every group [[src:fish-trapping-report]].

---

## Model comparison with AIC

Assemble candidate models in an AIC table using `AIC()` or `MuMIn::model.sel()` [[src:fish-trapping-report]]:

```r
aic_table <- AIC(m_pois, m_nb, m_zinb, m_glmm)
aic_table$delta <- aic_table$AIC - min(aic_table$AIC)
```

ΔAICᵢ = AICᵢ − AIC_min. Models with ΔAICᵢ < 2 have substantial support; ΔAICᵢ > 10 indicates essentially no support (general). **Interpretation limits** [[src:fieberg-2009]]:

- AIC ranks models but does not tell you whether the *best* model fits well—always check DHARMa residuals [[src:fish-trapping-report]].
- AIC cannot be used to compare models fit to different datasets (e.g., complete-case vs. imputed) (general). (unsourced)
- When comparing fixed-effects-only models with GLMMs, the random-effects model typically wins on AIC but addresses a different inferential target (see below) [[src:fieberg-2009]].

---

## Subject-specific vs. population-averaged inference

Fixed-effect GLMs and GLMMs with random intercepts estimate fundamentally different quantities for non-Gaussian outcomes [[src:fieberg-2009]]:

- **Subject-specific (conditional)**: describes how the response changes *within* an individual (or site) as covariates change, conditional on that individual's random effect [[src:fieberg-2009]].
- **Population-averaged (marginal)**: describes the mean response *across the population* of individuals (or sites) [[src:fieberg-2009]].

For logistic and log-link models, **conditional (GLMM) parameters are larger in absolute value** than marginal parameters [[src:fieberg-2009]]. The difference grows with the variance of the random effects [[src:fieberg-2009]].

Many ecological questions—mean catch rate across sites, nest success as a function of landscape—naturally target **population-averaged** inference [[src:fieberg-2009]]. If that is your question, either:

1. Fit a marginal model directly via **GEE** (not covered in source for count data; requires external packages). (unsourced)
2. Fit a GLMM and derive marginal predictions *post hoc* by integrating over the random-effects distribution (challenging analytically; simulation is safest) [[src:fieberg-2009]].

For fisheries trapping where the goal is to predict *mean* catch in *new* locations (not specific to any one site), the population-averaged view is often more appropriate [[src:fieberg-2009]].

---

## Reporting results

1. **Model selection**: present an AIC table with ΔAICᵢ and note the chosen model [[src:fish-trapping-report]].
2. **Dispersion**: report φ̂, the dispersion test result, and estimated NB *k* (theta) [[src:fish-trapping-report]].
3. **Random effects**: report variance components and ICC (intraclass correlation) [[src:fish-trapping-report]].
4. **Coefficients**: exponentiated coefficients on the rate-ratio scale with 95% confidence intervals [[src:fish-trapping-report]].
5. **DHARMa checks**: state that residual diagnostics (QQ plot, dispersion, zero-inflation, spatial and temporal autocorrelation) were satisfactory, or describe corrective steps taken [[src:fish-trapping-report]].
6. **Predictions**: present model-based predictions across covariate ranges, with confidence bands, for a reference site/region [[src:fish-trapping-report]].
7. **Clarify interpretation**: state whether inferences are conditional (site-specific) or marginal (population-averaged) [[src:fieberg-2009]].
