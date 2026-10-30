---
species: N/A
common_name: N/A
family: N/A
habitat: "Island habitats (Polis et al. 1998 example); urban tree stands (Speight et al. 1998 example)"
ocean_basin: N/A
location: "Islands (Polis et al. 1998, unspecified); urban area in England (Speight et al. 1998)"
tags: [statistics, generalized-linear-models, logistic-regression, poisson-regression, ecological-statistics]
title: "Generalized linear models and logistic regression"
source_id: "PML2183"
marsh_id: "PML2183"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. Quinn, M. Keough (2001). Generalized linear models and logistic regression. Experimental Design and Data Analysis for Biologists. Marsh Library ID: PML2183."
source_file: "Quinn G. et al. 2001. 13 generalized linear models and logistic regression.pdf"
text_extraction: "text"
---
# Generalized Linear Models and Logistic Regression

#statistics #ecological-statistics #generalized-linear-models

## Executive Summary

This textbook chapter (from a biostatistics text, p. 437–446 in the source pagination) explains why [[Generalized Linear Models]] (GLMs) are needed when response variables are not normally distributed. It covers the three components of a GLM, the [[Logit Link Function]] used in [[Logistic Regression]] for binary responses, likelihood-based testing with [[Deviance]] and the [[Likelihood Ratio Statistic]], goodness-of-fit and diagnostic methods, and [[Poisson Regression]] for count data, including the problem of [[Overdispersion]]. The document is methodological. It contains no original field data and no aquatic or fish-specific results. Its examples come from terrestrial and island ecology.

## Background & Description

Linear models assume normally distributed responses and errors. They are fairly robust to this assumption, but transformations do not always normalize errors, for example when the response is categorical. The chapter notes that it can be better to model the actual data than transformed data. GLMs, introduced by Nelder & Wedderburn (1972) and developed further by McCullough & Nelder (1989), extend modelling to other distributions.

A GLM has three components:

- **Random component:** the response variable and its probability distribution, drawn from the [[Exponential Family]] (normal, binomial, Poisson, gamma, negative binomial). Binary responses are usually binomial and count responses usually Poisson.
- **Systematic component:** the linear predictor, which may include continuous or categorical predictors, interactions and polynomial terms.
- **Link function:** links the expected value of the response to the predictors. The three common links are identity (standard linear models), log (count data, [[Log-Linear Models]]) and logit (binary data).

GLMs use [[Maximum Likelihood Estimation]] rather than least squares. Parameters are estimated iteratively, and standard errors and confidence intervals are asymptotic, so they are approximate in small samples.

In logistic regression, the response is binary and the probability of an event is transformed into the odds, p/(1−p), and then into the log odds (logit). The log odds are modelled as a linear function of predictors. The logit transformation has two advantages. It maps probabilities from 0–1 onto the whole real line, and it models the binomial error distribution. Coefficients are interpreted on the log-odds scale, and the [[Odds Ratio]] is the usual back-transformed summary.

Poisson regression models counts with a Poisson error term and a log link. In a Poisson distribution the mean equals the variance. The chapter describes Speight et al. (1998), who modelled an egg-code infestation score (one to ten) of the scale insect *Pulvinaria regalis* in an urban area in England against seven predictors, including tree species, tree diameter and distance to the nearest road.

## Ecological & Environmental Context

The chapter's examples are ecological but not aquatic:

- **Polis et al. (1998):** a logistic model of the probability that *Uta* (a lizard, named only as "Uta" in the OCR text) is present on an island, with the predictor being the P/A ratio (a measure of island size, here given as "P/A ratio" without definition).
- **Speight et al. (1998):** the *Pulvinaria regalis* infestation example described above, in an urban English setting.
- **Hypothetical forest example:** number of plant species per plot modelled against soil pH, with overdispersion arising from unmeasured nutrient variation among plots.
- **Hypothetical distance and shrub model:** a multiple logistic model that includes distance and percentage shrub cover as predictors.

No water chemistry, fish or invertebrate datasets are presented.

## Key Findings

1. **Model choice follows the response type.** Binary responses call for logistic regression (binomial errors, logit link). Count responses call for Poisson regression (Poisson errors, log link). Categorical predictors with categorical responses are better handled by log-linear models in [[Contingency Tables]].

2. **Parameter estimation and inference.** Logistic models are fitted by maximizing the likelihood (or its log) iteratively. Standard errors are asymptotic. The chapter recommends the likelihood ratio approach over the [[Wald Test]]. Wald tests lack power with small samples and can be unreliable. The G² statistic, equal to −2 times the difference in log likelihoods between reduced and full models, is approximately χ² distributed when the null hypothesis holds and the assumptions hold.

3. **Deviance as goodness of fit.** Deviance is the GLM analogue of residual sums of squares. Because the log likelihood of a [[Saturated Model]] is zero, the deviance of a model equals its negative twice log likelihood. The difference in deviance between nested models equals G² and can be presented in an [[Analysis Of Deviance]] table. Partial deviance is used for multiple predictors.

4. **Assumptions and limitations.** When predictors are continuous, most observations have a single case for each predictor combination, so the P values for the Pearson χ² and deviance statistics are not reliable as overall goodness-of-fit tests. The statistics remain valid for comparing models. The [[Hosmer-Lemeshow Statistic]] (deciles of risk) addresses this by grouping observations into ten groups, either of equal size or by fixed cutpoints (e.g. all probabilities < 0.10 in the first group). It is approximately χ² distributed with df equal to the number of groups minus two. Hosmer et al. (1997) found the deviance statistic powerful and recommended it.

5. **Pseudo-R² measures.** Menard (2000) discussed analogues of R² for logistic regression and tentatively recommended a measure based on the log likelihoods of the intercept-only model and the full model. The chapter reports this formula but does not give worked values.

6. **Model diagnostics.** Two residual types are used: [[Pearson Residuals]] and deviance residuals. Diagnostics such as leverage and influence are considered extensive. The chapter recommends checking software output against a known dataset, for example from Christensen (1997) or Hosmer & Lemeshow (1989), and cites Tabachnick & Fidell (1996) for a comparison of outputs from four common programs.

7. **Categorical predictors.** These enter as [[Dummy Variables]]. Software may use reference-cell coding (effects are relative to a reference group) or effects coding (each group logit is compared to the overall logit). The coding must be known because it changes the interpretation of coefficients and odds ratios. A binary-response model with categorical predictors is called a logit model.

8. **Overdispersion in count data.** A Poisson model assumes variance equals mean. Real count data often show greater variance (overdispersion). This makes standard errors too small and inflates the Type I error rate. Three remedies are given:
   - correct the standard errors using the dispersion parameter (Agresti 1996; Gardner et al. 1995 give a more complex adjustment);
   - use a more appropriate distribution such as the [[Negative Binomial Distribution]];
   - use [[Quasi-Likelihood Models]], which estimate the dispersion parameter from the data.

   Criteria such as the likelihood ratio statistic and [[Akaike Information Criterion]] (AIC) are also sensitive to overdispersion. Fitzmaurice (1997) suggested scaling them by an estimate of the degree of overdispersion.

9. **Interpretation of Poisson coefficients.** A one-unit increase in the predictor multiplies the expected count by e^β1. A positive coefficient means the count increases with the predictor, and a negative coefficient means it decreases.