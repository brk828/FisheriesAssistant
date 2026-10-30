---
species: Merluccius capensis x M. paradoxus
common_name: Cape hake (Namibian hake)
family: Merlucciidae
habitat: Marine demersal (hake case study; not a species-level ecological study)
ocean_basin: Atlantic
location: Namibia (Southeast Atlantic)
tags: [fisheries-statistics, state-space-models, likelihood-inference, monte-carlo, population-dynamics, errors-in-variables]
title: "State-space likelihoods for nonlinear fisheries time-series"
source_id: "PML1056"
marsh_id: "PML1056"
library: "Marsh Library"
permission: "not public domain"
source_citation: "P. d. Valpine, R. Hilborn (2005). State-space likelihoods for nonlinear fisheries time-series. Canadian Journal of Fisheries and Aquatic Sciences 62(9): 1937-1952. Marsh Library ID: PML1056."
doi: "10.1139/f05-116"
source_file: "Hilborn R. et al. 2005. State space likelihoods for nonlinear fisheries time series.pdf"
text_extraction: "text"
---
# Monte Carlo Kernel Likelihood for Nonlinear State-Space Fisheries Models

#ichthyology #marine-biology #merlucciidae

## Executive Summary

This methodological paper addresses how to estimate parameters of fisheries population models when both process error (true population fluctuations) and observation error (survey noise) are present. The authors show that the widely used [[Errors-In-Variables Method]] (EV), which maximizes a joint likelihood over parameters and unobserved states, is not a classical likelihood. It gives asymptotically biased parameter estimates and unreliable confidence intervals. They propose the [[Monte Carlo Kernel Likelihood]] (MCKL), which estimates an integrated classical likelihood from a Bayesian posterior sample using weighted kernel density estimation. Simulations on a linear autoregressive model and on a Schaefer-type model fitted to [[Namibian Hake Data]] show that integrated likelihoods outperform EV. The authors frame the work as filling a methodological gap rather than arguing for classical over Bayesian inference.

## Background & Description

**Problem.** Fisheries time series are typically noisy, and separating process error from observation error is difficult. Earlier approaches include the [[Kalman Filter]] for linear models, the EV method for nonlinear models, and full joint likelihood integration. Integration over the state space is hard for nonlinear models, and Bayesian MCMC has been the main route to handling both error types.

**Framework.** The authors use a general state-space formulation:
- Population dynamics: X_t = F(X_{t-1}, v_{t-1}), with v as process error.
- Observations: Y_t = G(X_t, e_t), with e_t as observation error.
- Parameters θ cover quantities such as growth, survival, fecundity, and error variances. The authors reserve "parameter" for these and do not treat unknown states as parameters.

**Key distinction.** The classical likelihood (eq. 3) integrates over all possible state trajectories. The EV likelihood (eq. 4) instead uses the joint probability of one specific state trajectory and the observations. The two are equal only at the integrand level, so EV is not a true likelihood.

**Candidate methods compared:**
- EV (errors-in-variables), with a known ratio of error variances.
- CKF (constrained Kalman Filter), which uses the same constrained parameter space as EV but integrates over states.
- KF (Kalman Filter), which estimates both error variances without constraints.
- MCKL, the proposed Monte Carlo integrated likelihood for nonlinear models.

## Ecological & Environmental Context

The study is methodological, so ecological content is limited to the case study. The hake example uses the [[Namibian Hake]] fishery, which has an annual catch series and an abundance index starting in 1965. Harvest was assumed to be negligible before the data began, which justified a burn-in approach for initial states. The population model is a [[Schaefer Surplus Production Model]] with parameters for intrinsic growth rate (r), carrying capacity (K), survey catchability (q), process error (σ_p), and observation error (σ_o). The authors stress that separating process and observation error is inherently difficult, and the likelihood surfaces show ridges that run from all-process-error to all-observation-error solutions.

## Key Findings

**1. EV is not a classical likelihood.**
- EV's asymptotic parameter estimates do not converge to true values, even when the variance constraint is correct.
- EV systematically underestimates error variances, consistent with earlier work (e.g., [[Ludwig And Walters 1981]]).
- Likelihood-based confidence intervals from EV, using Hessians, do not achieve nominal coverage and become less accurate as data increase.

**2. Linear autoregressive (AR) simulations.**
- The authors simulated 200 data sets for each combination of autocorrelation (φ = -0.25, 0.25, 0.75), constraint ratio λ (0.25, 0.50, 0.75), and series length n (40 and 200).
- CKF had lower RMSE than EV in nearly every case. The exceptions were some φ estimates at n = 40 with λ = 0.75.
- EV bias grew with more data; CKF bias shrank.
- At a nominal 5% rejection rate, EV rejected the true parameters about 99% of the time, while CKF rejected them about 11% of the time. An "EV adjusted" version, which doubles the test statistic, was also inaccurate.
- The KF performed worse than CKF on parameter estimates because it struggled to estimate error variances. Its confidence regions were nonetheless a useful approximation.

**3. The Bayesian justification for EV does not hold.**
- Schnute (1994) suggested that EV can be justified as a Bayesian joint posterior maximum with an uninformative prior.
- The authors show that standard likelihood theory applies to parameters but not to states, so the joint-posterior argument breaks down.

**4. MCKL method.**
- MCKL estimates the likelihood as a weighted, importance-sampled kernel density estimate of the Bayesian posterior (eq. 20). The posterior acts as the importance sampling density.
- It requires an MCMC posterior sample, a kernel bandwidth choice, and a maximization routine (Nelder-Mead with restarts in this paper).
- Accuracy increases with Monte Carlo sample size. The method is relatively simple to implement once posterior samples are available.
- It can also support state distribution estimates by fixing parameters and sampling states.

**5. Namibian hake case study.**
- A Schaefer model was fitted with MCKL. Data were simulated 100 times for each of three parameter sets, with observation error fixed at 0.01, 0.05, or 0.10 (the full MLE gave 0.01, the lower bound).
- EV with known variance ratio was more biased, had higher RMSE, and gave very inaccurate confidence regions.
- MCKL with a known variance ratio had low bias and RMSE, and its confidence regions were useful.
- MCKL with an unknown variance ratio gave similar parameter estimates, but separating process from observation error was again difficult. In some runs it estimated all-process-error or all-observation-error models.
- Confidence regions for the unknown-ratio case were wide, and they often spanned the full range from all-process to all-observation error. The authors present this as an honest reflection of uncertainty.

**6. Scope and recommendations.**
- Integrated state-space likelihoods (classical or Bayesian) outperform EV for both linear and nonlinear models.
- Integrated likelihoods do not require assumptions about the relative size of process and observation error.
- Choosing between Bayesian and classical analysis should be separated from model complexity. MCKL allows classical analysis of complex models that include both error types, so each approach can be applied to the same problem.
- Future work should test more data sets and more complex age- or size-structured models.