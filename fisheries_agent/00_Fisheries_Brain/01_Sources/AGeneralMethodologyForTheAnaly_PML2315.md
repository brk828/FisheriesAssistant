---
species: "N/A"
common_name: "Chinook salmon (Chase River population, adult males and jacks)"
family: "Salmonidae"
habitat: "Freshwater river (spawning run); open-population capture-recapture modelling"
ocean_basin: "N/A"
location: "Chase River, British Columbia, Canada"
tags: [ichthyology, marine-biology, salmonidae, capture-recapture, jolly-seber, fisheries-statistics]
title: "A General Methodology for the Analysis of Capture-Recapture Experiments in Open Populations"
source_id: "PML2315"
marsh_id: "PML2315"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. J. Schwarz, A. N. Arnason (1996). A General Methodology for the Analysis of Capture-Recapture Experiments in Open Populations. Biometrics 52, 860-873. Marsh Library ID: PML2315."
source_file: "Schwarz C.J et al. 1996. A general methodology for the analysis of capture recapture experiments in open population.pdf"
text_extraction: "text"
---
# A General Methodology for the Analysis of Capture-Recapture Experiments in Open Populations

#ichthyology #marine-biology #salmonidae

## Executive Summary

Schwarz and Arnason (1996) present a general likelihood framework for [[Jolly-Seber Model|Jolly-Seber]] capture-recapture experiments on open populations, where animals enter (births, immigration, recruitment) and leave (deaths, emigration) between sampling occasions. The authors argue that the usual Jolly-Seber likelihood treats births inconsistently and makes it hard to impose constraints, often yielding negative birth estimates. They propose modelling births as a multinomial draw from a [[Super-Population]], which simplifies numerical optimisation, allows constraints and covariates, and extends to multiple groups. The method is demonstrated on a salmon escapement dataset from the [[Chase River]], where it removes inadmissible estimates and supports estimation of gross births (escapement).

## Background & Description

- **Scope:** A statistical methods paper, not a species study. The fish data serve only as a worked example.
- **Terminology:** "Births" are any additions to the catchable population (immigration, recruitment); "deaths" are any permanent removals (emigration, death, inactivity). Injections and losses on capture occur at known sample times.
- **Core parameters:** capture probability *p_i*, survival probability *φ_i*, net births *B_i*, total super-population size *N*, and entry probabilities *γ_i* (fraction of net births entering in each interval).
- **Prior approaches:** Darroch (1959), Jolly (1965) and Seber (1965) method-of-moments and closed-form estimators; Cormack (1989) log-linear formulation; Burnham (1991) triangular-array formulation; Crosbie and Manly (1985) parsimonious super-population approach, which this paper extends.
- **Software:** A FORTRAN program for single and multiple groups; [[POPAN-4]] (Arnason and Schwarz, 1995), with a constraint-specification interface; and POPAN-5 for multiple groups, announced as under development for fall 1995.

## Ecological & Environmental Context

The study addresses [[Salmon Escapement Estimation]] in a river fishery. Adult salmon returning to spawn were sampled by weekly river passes with electrofishing. Unmarked fish were individually tagged and marked fish had their tag numbers recorded. Fish were stratified into adult males, adult females and precocious males ("jacks") that return to spawn a year early. Births in this context represent salmon newly entering the river to spawn between two sampling occasions. The authors note that the gross births estimate is the total escapement from the fishery that returns to spawn, which is of particular interest to fisheries managers. The paper includes no information on water chemistry, habitat quality, or other aquatic taxa.

## Key Findings

1. **Inconsistency in the classical model:** The usual Jolly-Seber birth representation is inconsistent with the death-only reduced model and makes constraints on birth parameters difficult to impose.
2. **Super-population formulation:** Births are modelled as a multinomial from a super-population of *N* animals. The likelihood then factors into binomial and multinomial components that can be maximised numerically.
3. **Constraints and covariates:** Constraints (for example, births known to be zero between sample times, or equal survival across intervals) and covariates on capture or survival can be imposed. This includes non-linear constraints via Lagrange multipliers.
4. **Admissibility:** Parameters are parameterised on the logit scale, so estimates of capture, survival and births stay within admissible ranges. Using this, the authors eliminated negative birth estimates and survival estimates above 100% that appeared in the closed-form Chase River estimates.
5. **Numerical method:** Cyclic fixing (maximising over subspaces in turn) is used with a final full-parameter step. The authors report that this converges quickly because each cycle is a series of *k*-dimensional problems rather than one 3*k*-dimensional problem.
6. **Model selection:** Likelihood ratio tests and AIC are used. The number of parameters equals 3*k* minus imposed constraints. Identifiability problems arise when capture probabilities vary over time or data are sparse.
7. **Chase River example:** Summary statistics from the salmon escapement survey are given in a table of weekly captures, marks, releases and recaptures. Weeks 1 and 9 were pooled with weeks 2 and 8 owing to low sample sizes. The final selected model was {*p*_g, *φ*_t, *γ*_{g,t}}, with capture probabilities varying by group but constant over time, survival varying over time but equal across groups, and entry probabilities varying over both time and group. Constraints *p*_1 = *p*_16 = 1 were imposed for identifiability.
8. **Multi-group extension:** The framework extends to groups such as males and females. Identifiability must be checked and constraints imposed, as in [[Lebreton et al. (1992)]] survival modelling.
9. **Standard errors:** Variances for estimated births can be conditioned on the random-birth assumption. For boundary estimates (zero or one), the reported standard error is zero, even though uncertainty exists. The authors suggest profile methods may address this.
10. **Conclusion:** The approach allows a single methodology for model fitting and hypothesis testing, and lets researchers focus on biologically plausible models rather than preprogrammed ones.