---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [animal-populations, capture-recapture, population-ecology, biostatistics]
title: "A Note on the Multiple-Recapture Census"
source_id: "PML2331"
marsh_id: "PML2331"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. A. F. Seber (1965). A Note on the Multiple-Recapture Census. Biometrika, vol. 52, no. 1/2, pp. 249-259. Marsh Library ID: PML2331."
source_file: "Seber G.A.F. 2002. A note on the multiple recapture census .pdf"
text_extraction: "text"
---
# A Note on the Multiple-Recapture Census

#animal-populations #capture-recapture #population-ecology

## Executive Summary

This 1965 *Biometrika* paper by G. A. F. Seber develops a statistical model for the [[Multiple-Recapture Census]], a capture-mark-recapture method for estimating animal population parameters. The model covers an open population with both immigration and death, which earlier work by [[Darroch Model|Darroch]] treated only in part and which [[Jolly Model|Jolly]] had solved by a different route. Seber's version differs in treating some parameters as unknown constants rather than random variables. The paper derives the joint density of the sample data, gives [[Maximum-Likelihood Estimation|maximum-likelihood]] equations and asymptotic moments via the [[Delta Method]], shows that its estimates match Jolly's, and proposes a [[Likelihood-Ratio Test]] for the key assumption of equal catchability. It also develops a [[Constant Catchability]] restriction for closed populations. No species, site or field data are reported.

## Background & Description

The paper addresses estimation of population parameters (population size, death rate, birth rate) for animal populations using capture-tag-recapture models with minimal assumptions. In the multiple-recapture census, the experimenter takes a sequence of random samples. Members of each sample are marked and returned to the population before the next sample is taken, so every individual can be classified by when, if ever, it was captured before.

Several models exist. The paper highlights three exact, fully stochastic treatments:

- **[[Darroch Model|Darroch (1958, 1959)]]**: the first paper treats a [[Closed Population]] (no immigration, birth, death or emigration). The second treats populations with either immigration or death, but not both, and gives almost unbiased, asymptotically efficient modified maximum-likelihood estimates. For populations with both processes, Darroch gives only the probability generating function and moment estimates.
- **[[Jolly Model|Jolly (1965)]]**: solves maximum-likelihood estimation for the population with both immigration and death, and gives the means and variances of the estimates.
- **[[Seber Model|Seber (1962)]]**: the multi-sample single-recapture census, whose methods the present model follows.

The central assumption of all capture-recapture models is that marked and unmarked individuals have the same probability of capture. The author notes that no test statistic had been published for this assumption and derives one.

## Ecological & Environmental Context

The paper is purely statistical and contains no ecological field data, study organisms, or environmental variables. The population context is general: "animal populations" in closed or open settings, with mortality or emigration between samples and immigration or birth adding unmarked individuals. Key modelling terms:

- **Marked and unmarked individuals**: individuals are marked on capture and returned to the population.
- **Survival/death probability**: each marked individual has a common probability of dying or permanently emigrating between consecutive samples, given it is alive at the earlier sample.
- **Immigration/new unmarked individuals**: the increase in unmarked individuals between samples is treated as a parameter (the paper departs from Darroch by treating it as fixed, not random).
- **Catchability**: the probability that an individual is caught in a given sample, given it is alive. Constant catchability means this does not depend on the individual's earlier capture history.

## Key Findings

**1. Model formulation.** Seber specifies a model for a population with both immigration and death. The sample is characterized by the numbers of individuals caught in specific subsets of samples. The population size before the first sample is denoted m₁. The number of new unmarked individuals entering between samples is treated as an unknown constant, not as a random variable, which differs from Darroch's model. The main assumptions are:
- (1) All individuals alive at any instant have the same probability of capture in each sample.
- (2) Every marked individual, regardless of recapture history, has the same probability of dying or permanently emigrating between consecutive samples.

**2. Density function.** The joint probability density of the recapture data is derived for the general case and proved by induction on the number of samples *s*. The paper notes that four samples are the minimum from which the general form can be inferred. Two checks are reported:
- Setting the immigration term to a specific value recovers the "immigration only" density of Darroch (1959).
- Setting the death term yields Darroch's "death and no immigration" model, but the author notes that setting the second parameter alone does not recover the "death only" model.

**3. Maximum-likelihood estimation.** The maximum-likelihood equations are derived for the population-size, survival and immigration parameters. The author shows that the parameters m_i and p_i cannot be estimated separately, because only their product is identified in the data. Darroch (1959) had conjectured that a set of random variables built from the recapture counts would be the key quantities for estimation. Seber confirms this, showing that the maximum-likelihood estimates are functions of these variables, which are jointly sufficient for the likelihood.

**4. Asymptotic moments.** The asymptotic means and variances of the estimates are derived by the delta method, starting from moments of the recapture statistics. Variance expressions are given for the survival and population-size estimates. The bias-correction approach is compared with Seber (1962). A Poisson approximation is noted for death-rate estimation, for which the author suggests that death rates could be computed from the estimated survival probabilities and plotted over time to check for a trend.

**5. Comparison with Jolly.** Seber shows that his estimates for the number of unmarked individuals before each sample and for the survival and population-size parameters coincide with Jolly's (1965) estimates, though the models are formulated differently. The extra random variables in Jolly's model do not alter estimates of the main parameters. The information in the two models is therefore equivalent.

**6. Test of equal catchability.** The paper derives a likelihood-ratio test of H, the hypothesis that the capture probability is the same for all individuals regardless of previous recaptures. For closed populations:
- If *n* is known, the maximum-likelihood estimates are simple functions of the recapture counts.
- If *n* is unknown, there is insufficient information to test H against a fully general alternative, so a restricted alternative must be chosen.
- The author proposes a "constant catchability until first capture" assumption: for individuals not previously caught, the probability of capture is proportional to effort, with an unknown constant. This gives one restriction on the capture-probability parameters. Only the first two samples are used, since the constant may vary across later samples as the population is disturbed.
- Under this restriction and the identifiability condition, the maximum-likelihood estimates are found using Lagrange multipliers and approximate solutions are obtained through series expansion.
- The test statistic, −2 log (likelihood ratio), is asymptotically chi-square distributed under H₀. The degrees of freedom are stated in the paper but are not clearly legible in the scanned text.

**7. Testability and alternatives.** Constant catchability can often be tested in a separate experiment (for example, if effort is measured as time spent, the assumption implies that captures form a Poisson process). An alternative restriction, that the first recapture does not affect an individual's catchability, is judged a much stronger assumption than constant catchability.

**8. Conclusion.** The author's intuitive judgement is that the constant-catchability assumption for individuals not previously caught, over the first two samples, is the weakest restriction that still allows estimation of all unknown parameters. The paper acknowledges a referee's comments.