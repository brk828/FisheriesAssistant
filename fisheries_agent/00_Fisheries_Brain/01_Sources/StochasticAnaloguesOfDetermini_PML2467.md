---
species: Callosobruchus maculatus
common_name: Cowpea weevil
family: Bruchidae
habitat: Laboratory culture under constant environment (experimental data); individual-based simulation
ocean_basin: N/A
location: N/A (laboratory experiments by Utida, 1967; authors affiliated with Umeå, Sweden, and IIASA, Laxenburg, Austria)
tags: [population-ecology, stochastic-models, theoretical-ecology, ricker-map, entomology, bruchidae]
title: "Stochastic analogues of deterministic single-species population models"
source_id: "PML2467"
marsh_id: "PML2467"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. Brännström, D. J. T. Sumpter (2006). Stochastic analogues of deterministic single-species population models. Theoretical Population Biology 69 (2006) 442-451. Marsh Library ID: PML2467."
source_file: "Stochastic analogues of deterministic single species population models .pdf"
text_extraction: "text"
---
# Stochastic Analogues of Deterministic Single-Species Population Models

#entomology #coleoptera #bruchidae #population-ecology

## Executive Summary

This theoretical population biology paper derives stochastic versions of single-species, discrete-generation population models with first-order density feedback. It separates [[Demographic Stochasticity]] from [[Environmental Stochasticity]] and shows that the form of the variance depends on the noise source. Demographic noise gives variance proportional to the expectation. Multiplicative environmental noise gives variance proportional to the square of the expectation. These candidate models were fitted by [[Maximum Likelihood Estimation]] to output from an [[Individual-Based Model]] and to laboratory data on the [[Cowpea Weevil]] (*Callosobruchus maculatus*). The demographic models fit simulated demographic noise significantly better than the environmental models. However, the traditional choices, additive normal and multiplicative lognormal noise, fit nearly all datasets well. The paper concludes that variance form matters in principle for fitting ecological time series but may matter less in practice than assumed.

## Background & Description

**Motivation.** Population fluctuations arise from environmental forcing, density-dependent regulation, demographic stochasticity (variation in offspring number per individual), and deterministic non-linear dynamics such as cycles and chaos. Ecological time series are often short and contain observation error, which makes predictive modelling difficult. The authors argue that stochastic and deterministic components should be weighted appropriately within a model.

**Base model.** The deterministic skeleton is a first-order feedback map, N(t+1) = f(N_t) = N_t g(N_t), where g is the net reproduction rate per individual. Two traditional stochastic analogues are used as baselines:
- Additive normal noise: N(t+1) = f(N_t) + σε_t, with ε ~ N(0,1).
- Multiplicative lognormal noise for the [[Ricker Map]]: N(t+1) = b N_t exp(r(1 − N_t/K) + σε_t − σ²/2).

**First-principles derivation.** Individuals produce binomially distributed surviving offspring, with a maximum of *b* offspring per individual. A density-dependent correlation between individuals' contributions is assumed. Using the Engen et al. decomposition of variance into demographic and environmental parts, the authors derive:
- Demographic case (constant environment): Var[N_{t+1}|N_t] = C·f(N_t), so variance is proportional to expectation.
- Environmental case (multiplicative effect, negligible demographic variance): Var[N_{t+1}|N_t] = C·f(N_t)², so variance is proportional to the square of expectation.
- For the Ricker map with environment-dependent carrying capacity, a linear approximation gives variance proportional to the square of expectation, with a constant depending on the environmental variance, K and b.

**Models tested (Table I).** The paper compares about ten candidate models:
- D1 and D2: demographic noise, normal and lognormal.
- DW: demographic model from diffusion approximations (Engen et al., 1998), used by Sæther et al. (2000).
- E1 and E2: environmental noise, normal and lognormal.
- N1: additive normal observation error with constant variance.
- T1: the individual-based model's theoretical "benchmark" map.

**Methods.**
- *Individual-based model:* Individuals are distributed randomly across *n* resource sites. Reproduction then occurs per site, with environmental noise modeled as a binomial variable. The model follows Sumpter and Broomhead (2001) and Johansson and Sumpter (2003).
- *Fitting:* Models were fitted by maximum likelihood, minimized with the Nelder–Mead simplex algorithm, with restarts from random initial parameters. Carrying capacity was bounded at 10 times the mean of the time series.
- *Time series:* Simulated series had length 20, sampled after 100 generations, and included only non-extinct series (100 series used for averages).
- *Laboratory data:* Four replicate experiments from Utida (1967) on *Callosobruchus maculatus*. Populations were censused and given fresh food every 25 days, in a constant environment.

## Ecological & Environmental Context

- **Dynamical regimes.** The individual-based model shows stable dynamics for *b* < 8 (e.g., *b* = 4), periodic dynamics for 8 < *b* < 15 (e.g., *b* = 10), and chaotic dynamics for *b* > 15 (e.g., *b* = 18). Model fit depends strongly on regime.
- **Noise shifts with population size.** As the number of resource sites increases, the dominant noise shifts from demographic to environmental. Demographic variance scales with *n*, while environmental variance scales with *n*².
- **Taylor's power law.** At equilibrium, the demographic and environmental models predict log-log slopes of 1 and 2 respectively for variance against mean. These match the common observation that most populations have slopes near these extremes (Anderson et al., 1982). Under periodic or chaotic dynamics, the authors do not expect Taylor's law to hold in general.
- **Extinction risk.** Models with noise independent of population size overestimate stochastic effects at small population sizes and underestimate them at large sizes. This matters for extinction-time estimation.
- **Weevil context.** The laboratory cultures had a constant environment, so environmental noise and observation error should be minimal. This makes the weevil data a test of demographic models.

## Key Findings

1. **Variance form follows noise source.** Demographic noise gives Var ∝ expectation. Multiplicative environmental noise gives Var ∝ expectation². Environmental variance depends on how noise enters the parameters, so it is not always proportional to the square of the expectation.
2. **Model Tl is the best benchmark.** In the absence of environmental noise, the theoretically derived model T1 gave the least biased estimates of *b* and the highest likelihood across most values of *b*.
3. **Demographic models fit demographic noise well.** Models D1 and D2 gave nearly identical estimates and were close to T1 in likelihood. For *b* > 12, D1 was preferred over E1 in more than 90% of fits.
4. **Environmental models fit less well.** E1 and E2 were somewhat worse than D1 and D2 for periodic and chaotic dynamics, with biases of opposite sign. The DW model over-estimated *b* for *b* > 8 and had variance tending to infinity as population approached zero.
5. **Surprising success of the normal model.** Model N1 (constant variance, additive noise) gave estimates of *b* closest to T1 across all values of *b*. Its variance did not match the theoretical demographic variance, so its good fit was unexpected.
6. **Environmental noise test.** At *p* = 0.5, E1 was selected over D1 more often for small *n*. D1 became more likely to be selected as *n* grew under periodic dynamics, and for chaotic dynamics E1 was preferred only above about *n* = 2000.
7. **Weevil data.** Of four replicate experiments on *Callosobruchus maculatus*, environmental models gave the best fit in three. Model N1 fitted best in the fourth. Demographic models had only slightly lower log-likelihoods but were never the best fit.
8. **Practical conclusion.** Normal and lognormal stochastic models fit both simulated and experimental data well, so the variance form matters less in practice than the authors first supposed. Multiple-noise models (combining demographic and environmental components) did not converge reliably in preliminary tests.
9. **Future work.** The authors identify age-structured populations, higher-order feedback, and environmental change correlated between years as priorities for improving extinction predictions.