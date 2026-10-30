---
species: "Somateria mollissima; snowshoe hare (species not named in source)"
common_name: "Common eider; snowshoe hare"
family: "N/A"
habitat: "N/A"
ocean_basin: "N/A"
location: "St Andrews, Fife, Scotland (author affiliation); eider study and hare study sites not specified"
tags: [capture-recapture, log-linear-models, biostatistics, population-ecology]
title: "Log-linear Models for Capture-Recapture"
source_id: "PML0499"
marsh_id: "PML0499"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. M. Cormack (1989). Log-linear Models for Capture-Recapture. Biometrics 45, 395-413. Marsh Library ID: PML0499."
source_file: "Cormack R.M. 1989. Log linear model for capture recapture.pdf"
text_extraction: "text"
---
# Log-linear Models for Capture-Recapture

#population-ecology #biostatistics #capture-recapture #somateria-mollissima

## Executive Summary

This methodological paper by R. M. Cormack develops [[Log-linear Models]] as a unified framework for [[Capture-Recapture]] experiments on free-living populations of unknown size. The models express the expected number of animals with each observable [[Capture History]] as a product of biological parameters, so that maximum likelihood estimates of biological quantities can be obtained through standard GLIM software. The paper extends the framework to [[Open Populations]], [[Trap Dependence]], and long chains of recapture periods, and it treats [[Heterogeneity]] mainly through residual diagnostics. Two examples are used: a closed-population study of snowshoe hares and a 21-year study of eider ducks. The author argues that residual patterns and analyses of data subsets are the main tools for identifying behavioural processes and acceptable models.

## Background & Description

**Problem.** The goal is to estimate the parameters of a population of unknown size from *s* sampling occasions. Each animal is marked so that its pattern of being or not being observed across samples can be recorded. A pattern is coded as a sequence of 1s (seen) and 2s (not seen). With *s* samples there are 2^s − 1 observable capture histories; the all-2 history is unobservable by definition. For *s* = 3 there are 7 observable histories.

**Classical assumptions.** Estimators such as Petersen, Schnabel and [[Jolly-Seber Model]] assume that every animal alive at a sampling time has the same probability of being observed. The paper identifies two ways this can fail:
- **Trap dependence:** capture probability depends on past capture history.
- **Heterogeneity:** individuals differ in inherent catchability because of behaviour or location. Temporary departure from the population is the time-varying form most often considered.

**Log-linear framework.** Observed counts are treated as Poisson or multinomial random variables whose log-expectations are linear in parameters. The paper uses the GLIM parameterisation, in which a main effect for a sample contrasts animals not seen in that sample but seen in all others with those seen in all samples. For a full 2^3 table, this leaves 7 observations modelled by 7 parameters. The author builds models directly from biological parameters rather than from contingency-table ideas, then seeks a one-to-one correspondence between GLIM parameters and biological parameters.

**Poisson versus multinomial.** Conditioning independent Poisson counts on their sum gives the multinomial distribution, so inference is identical when the totals match. The paper notes that the unconditional Poisson estimate may not always coincide with the conditional multinomial estimate. A later example shows the Poisson estimate exceeding the unconditional multinomial estimate, which is a counterexample to a conjecture of [[Bishop et al. Conjecture]].

**GLIM implementation.** GLIM fits generalised linear models by iterated reweighted least squares. Design vectors are created with a VGL-type function that generates a binary-patterned vector for the 2^s factorial order. The paper gives example program code for a three-sample study. Output includes residual deviance, GLIM parameter estimates with asymptotic standard errors, expected counts, and standardised [[Pearson Residuals]].

## Ecological & Environmental Context

**Closed populations.** For a closed population with independent sampling probabilities, the expected numbers are products of *N* and capture probabilities. The paper shows that *N*, *p₁*, *p₂* and *p₃* are linked through GLIM parameters, and that constant sampling effort (*pᵢ* = *p*) is modelled by setting the main effects equal.

**Open populations.** Survival (*φᵢ*) and birth or immigration (*βᵢ*) parameters are incorporated. Birth is treated as the addition of new individuals, and the paper reparameterises birth and death as *γᵢ* and *ψᵢ* so they have probability interpretations. The GLIM interactions then map onto birth and death parameters, as summarised in the correspondence tables. Some parameters are not separately estimable. For example, the initial population size *N* is not estimable, but the sizes at intermediate samples are.

**Covariates.** Capture probability can be modelled on the logit scale as a linear function of covariates such as sampling effort or climate. For effort, the paper suggests a log-effort form, which gives zero probability at zero effort and diminishing returns.

**Trap dependence.** [[Otis Models]] M_b and M_bh model different capture probabilities for animals previously caught and not previously caught. The log-linear version of Model M_b is identical to the open-population birth-only model, although its interactions are not sign-restricted. For some trap-dependence structures, the log-linear model needs an extra parameter beyond the biological ones, so it is correct but not the most parsimonious description.

**Heterogeneity.** Under heterogeneity, the paper expects standardised residuals plotted against capture frequency to form a concave-upward curve. Animals caught many times are more catchable, and those caught rarely are less catchable. The author also discusses the [[Jackknife Estimator]] of Burnham and Overton and the approach of Pollock and Otto. He argues that the jackknife bias expansion is not theoretically justified, although it performs well in simulations. An alternative procedure successively removes the most frequently caught histories and adds back the expected counts for those histories.

## Key Findings

1. **Log-linear framework.** Expected counts for each capture history are written as products of biological parameters. Maximum likelihood estimates of GLIM parameters yield maximum likelihood estimates of biological parameters where exact equivalence holds, which includes closed models M_0, M_t, M_h and M_b (Otis et al.), and the Jolly-Seber model with its submodels.

2. **Trap dependence.** Log-linear models for trap dependence include the biological model but are not always the most parsimonious form. A test for trap dependence is therefore less powerful than the optimal test.

3. **Heterogeneity diagnostics.** The residual deviance tests for behavioural disturbance asymptotically. Residual patterns indicate the form of heterogeneity. In the snowshoe hare data, one observation (animals caught in all six samples, x = 6) is a dominant outlier. Removing it significantly reduces the residual deviance. The author describes the reduced data as showing a population-size shift from about 74–75 to 77–78, against 87 from the jackknife method.

4. **Snowshoe hare results.** Removing histories with 6, then 5, then 4 captures gives successive residual-deviance reductions, with the moderate evidence for varying capture probability (χ² = 10.2) residing mainly in histories with 4 or 5 captures. Removing the 6-capture data raises the standard error of the population estimate from 3.6 to 5.0 when the Poisson variance is replaced by the multinomial one.

5. **Eider duck study.** The author analyses a 21-year study of [[Eider Duck]] (*Somateria mollissima*) data, with 25 samples. Analysis is restricted to subsets because 2^25 − 1 histories is impractical. Years 20–23 use 63 observable classes. Two categories are fitted exactly by any birth-and-death model: 362 birds seen only before year 20 and 79 birds seen only after year 23.

6. **Model comparison, years 20–23.** Deviances are: closed population 655.2 (56 d.f.); birth only 621.0 (52 d.f.); death only 255.4 (52 d.f.); birth and death 83.1 (48 d.f.); birth and death with trap dependence 80.8 (46 d.f.); birth and death with in-range parameters 83.4 (49 d.f.); constant effort 84.8 (51 d.f.). Neither constant nor varying effort gives an acceptable fit, and conventional one-period trap dependence does not significantly improve it. Assuming constant effort reduces the standard errors of the other GLIM parameters by about 20%.

7. **Residual evidence.** Standardised residuals show too many animals seen in all six samples and large positive residuals for histories 212221, 221221 and 222121. These suggest temporary emigration after initial marking, which the author attributes to a behavioural age effect rather than a response to handling. Across 20 overlapping six-sample analyses, the 221221 and 212221 histories had consistently positive residuals in 17 or more analyses.

8. **Out-of-range estimates.** Negative estimates of birth or death are biologically inadmissible and are removed by omitting the corresponding GLIM parameter. Estimates are not independent, so a combinatorial search may be needed when several are out of range.

9. **Multi-group and effort modelling.** Two groups can be compared only if capture probabilities are the same in both. Covariates such as effort can be modelled, but this reduces information (s − 2 pieces for open populations versus s for closed).

10. **Overall conclusion.** Log-linear models yield maximum likelihood estimates and allow routine diagnosis of heterogeneity, trap dependence and temporary emigration. Heterogeneity is not directly modelled for open populations, but it can be explored and its effects assessed through subset analysis. The author notes that these methods can be implemented in GLIM or the POPAN package (Arnason and Baniuk, 1978), and that some developments, such as the [[Jolly Model]] for constant death rates, cannot yet be handled within the framework.