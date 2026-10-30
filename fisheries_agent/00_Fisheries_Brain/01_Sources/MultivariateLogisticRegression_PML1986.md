---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [biostatistics, logistic-regression, icu-mortality, non-aquatic]
title: "Multivariate Logistic Regression"
source_id: "PML1986"
marsh_id: "PML1986"
library: "Marsh Library"
permission: "public domain"
source_citation: "Unknown author (n.d.). Multivariate Logistic Regression. Marsh Library ID: PML1986."
source_file: "Multivariate logistic regression .pdf"
text_extraction: "mixed"
---
# Multivariable Logistic Regression: Worked ICU Mortality Examples

#biostatistics #logistic-regression #icu-mortality

## Executive Summary

This document is a statistics lecture on [[Logistic Regression]], not aquatic ecology. It contains no fish, invertebrate, plankton, water chemistry, or habitat data, so the ichthyology taxon fields are recorded as N/A. It covers the theory of [[Multiple Logistic Regression]] and then works through examples in R on the [[ICU Dataset]] from [[Hosmer and Lemeshow]]. The main conclusions are:

- Service at ICU admission ([[Service at ICU Admission]]) is associated with mortality. Surgical patients had lower odds of death (OR 0.39, 95% CI 0.19–0.80).
- Sex and [[Location Variable]] (loc) were inconclusive.
- Age and emergency admission type ([[Admission Type]]) are strong independent predictors in the five-variable model.
- Service and admission type are confounded, because they are strongly correlated.

## Background & Description

The document opens by extending [[Univariate Logistic Regression]] to p covariates using the [[Inverse Logit Function]]:

- π(X) = exp(β0 + β1X1 + … + βpXp) / (1 + exp(β0 + β1X1 + … + βpXp))
- logit[π(X)] = ln[π(X) / (1 − π(X))] = β0 + β1X1 + … + βpXp

The logit transform maps the probability range (0, 1) onto (−∞, ∞), so logistic regression is a linear model on the logit scale. Errors are assumed to have mean zero and a [[Binomial Distribution]] with variance π(X)(1 − π(X)).

**Interpreting coefficients**

- **Intercept (β0):** This is the baseline log-odds when all covariates equal zero. With β0 = 0, π = 0.50. With β0 = 1, π ≈ 0.73. With β0 = −1, π ≈ 0.27.
- **Slopes (βi):** exp(βi) is the [[Odds Ratio]] for a one-unit change in Xi. For a change of z units, the OR is exp(z·βi). If the covariates are uncorrelated, each OR is interpreted directly. If they are correlated, each OR is an adjusted effect, and [[Confounding]] and [[Collinearity]] can distort it.

**Estimation**

Coefficients are estimated by [[Maximum Likelihood Estimation]] using statistical software, since no closed-form solution exists. Confidence intervals use standard errors, and hypothesis tests use the [[Likelihood Ratio Test]].

**Recommended workflow**

The document recommends: (1) descriptive statistics by outcome group; (2) graphics for continuous variables; (3) correlation matrices and cross-tabulations to check confounding and collinearity; (4) univariate models for an unadjusted view; (5) consideration of [[Interaction Term]]s; (6) [[Model Selection]] or, preferably, a set of plausible models; (7) interpretation and [[Model Criticism]]. The author states these are guidelines, not rules.

## Ecological & Environmental Context

Not applicable. The document concerns clinical data from intensive care units. Its only environmental relevance is methodological: it describes how to handle correlated and sparse covariates. The author notes that "Location" (loc) had too few patients to analyze. Categories 1 and 2 contained only 5 and 10 patients. The document also distinguishes [[Dummy Variables]] (indicator coding) from multi-level factors in [[R Statistical Software]].

## Key Findings

**Dataset and outcome**

- The [[ICU Dataset]] (Hosmer and Lemeshow, chapter 1, section 1.6.1) has 200 patients and 20 variables after deleting the ID variable.
- The outcome is [[Vital Status]] (sta): 0 = lived, 1 = died.
- The overall death rate is about 20%, which the author describes as few events.

**Univariate results**

| Variable | Coding | Estimate (β) | p-value | OR (95% CI) | Conclusion |
|---|---|---|---|---|---|
| Sex | 0 = male, 1 = female | 0.105 | 0.771 | 1.11 (0.55–2.26) | Inconclusive |
| Service (ser) | 0 = medical, 1 = surgical | −0.947 | 0.0101 | 0.39 (0.19–0.80) | Significant; surgical patients had fewer deaths |
| Location (loc) | 0/1/2 | Unstable (CI spans −2085 to 2122) | 0.986 (loc1) | Not estimable | Dropped |

Crude death rates by sex were 24/124 (0.19) for males and 16/76 (0.21) for females.

**Multivariable model: sex + service**

- Service OR = 0.39 (95% CI 0.19–0.80), p = 0.0105.
- Sex OR = 1.04 (95% CI 0.50–2.13), p = 0.925.
- The author found no confounding between sex and service.
- Predicted mortality probabilities:

| Sex | Service | Predicted probability |
|---|---|---|
| Male | Medical | 0.277 |
| Male | Surgical | 0.129 |
| Female | Medical | 0.284 |
| Female | Surgical | 0.133 |

**Admission type and age**

- Emergency admission (typ = 1) had a much higher death rate. Reconstructed from the OCR'd tables, elective admissions had 2 deaths in 53 (0.04), and emergency admissions had 38 in 147 (0.26).
- Service and admission type are strongly correlated, so their effects overlap.

**Five-variable model: sex + service + age + typ**

- Age: β = 0.0347, p = 0.00156. OR = 1.035 per year (95% CI 1.013–1.058), or about 1.41 per decade (CI about 1.14–1.76).
- Admission type: β = 2.33, p = 0.00368. OR about 10.3 (CI about 2.1–49.6).
- Service: OR = 0.82 (p = 0.567) after adjustment. The author notes its effect was "replaced" by admission type because of their high correlation.
- Sex: p = 0.609, not significant.

**Interaction between sex and service**

- Interaction OR = 3.22 (95% CI 0.74–14.04), p = 0.12. The author calls this inconclusive but does not rule out an interaction.
- Sex OR within medical service = 0.65. Service OR within males = 0.24.
- Service OR within females = 0.24 × 3.22 ≈ 0.78.
- Sex OR within the surgical unit = 0.65 × 3.22 ≈ 2.10.
- The author warns that interaction terms must be interpreted carefully, and that possible confounding means no strong conclusion can be drawn from this model.