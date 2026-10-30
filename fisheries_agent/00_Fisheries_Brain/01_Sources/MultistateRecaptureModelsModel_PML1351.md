---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: "Canada geese wintering areas (Mid-Atlantic, Chesapeake, Carolinas, USA); Roseate Tern colonies (Falkner Island, Connecticut, USA, and a four-colony metapopulation); Black-headed Gull colony (Plaine du Forez, France); roe deer enclosed reserve (France)"
tags: [statistical-ecology, capture-recapture, population-ecology, multistate-models]
title: "Multistate recapture models: modelling incomplete individual histories"
source_id: "PML1351"
marsh_id: "PML1351"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. D. Lebreton, R. Pradel (2002). Multistate recapture models: modelling incomplete individual histories. Journal of Applied Statistics, Vol. 29, Nos. 1-4, pp. 353-369. Marsh Library ID: PML1351."
source_file: "Lebreton J.D. et al. 2002. Multistate recapture models modelling incomplete individual histories.pdf"
text_extraction: "text"
---
# Multistate Capture-Recapture Models: Modelling Incomplete Individual Histories

#statistical-ecology #capture-recapture #population-ecology

## Executive Summary

This methodological review, authored by J. D. Lebreton and R. Pradel of [[CEFE-CNRS]] (Montpellier, France), examines [[Multistate Capture-Recapture Models]]. These extend the classical one-site [[Cormack-Jolly-Seber Model]] by allowing individuals to move among a finite set of states (geographical sites, or individual categories such as breeding status or body weight class) between sampling occasions. The paper reviews their theory, biological applications, numerical difficulties and future directions, and presents a new multistate model for [[Accession to Reproduction]] that estimates age-dependent accession, natal dispersal and breeding dispersal simultaneously. The document contains no fish or aquatic data; its examples concern birds, deer, voles and human longitudinal data.

## Background & Description

- **Origin:** Spatial capture-recapture began with [[Chapman & Junge (1956)]] and [[Darroch (1961)]]. [[Arnason (1972, 1973)]] produced the general multisite model with time-dependent recruitment and mortality, later generalised by [[Schwarz et al. (1993)]].
- **Terminology:** The authors prefer "multistate" to "multistratum" because the word "stratum" implies deterministic assignment of individuals.
- **Parameterisation:** Survival is replaced by survival-transition probabilities. The movement model is Markovian and is written in matrix notation as a column-stochastic matrix. The model belongs to the product-multinomial class and is fitted by [[Maximum Likelihood Estimation]], with a dead state added to make the matrices column stochastic.
- **Parameter growth:** Relative to the one-state CJS model, the number of parameters rises from 2(K − 1) to s(s + 1)(K − 1). With 10 occasions and 3 states this goes from 18 to 54; with 20 occasions it goes from 38 to 114.
- **Software:** Most models can be fitted in [[Program MARK]], which uses a parameter index matrix approach inherited from [[SURGE]]. Earlier tools included [[MSSURVIV]] and [[SURVIV]].

## Ecological & Environmental Context

The main ecological motivation is [[Dispersal]], which can be split into natal dispersal (birthplace to first breeding site) and breeding dispersal (between successive breeding sites). The authors link the approach to:

- growing interest in spatial population dynamics ([[Metapopulation Dynamics]]) and individual variability;
- [[Breeding Trade-Offs]], where non-manipulative studies often show breeders have higher subsequent breeding probability than non-breeders, possibly masking trade-offs through individual quality differences;
- [[Heterogeneity of Capture]], where states linked to capturability (such as breeding status) can reduce bias in survival estimation relative to pooled CJS analyses;
- [[Longitudinal Studies with Missing Data]] in human health research and [[Hidden Markov Models]].

## Key Findings

**1. Applied case studies (dispersal and state transitions)**

- **[[Canada Goose]] exchanges:** [[Hestbeck et al. (1991)]] studied movement among three wintering areas over three consecutive winters. The time-dependent Arnason-Schwarz model had 24 parameters, some non-separately identifiable. The 63 capture histories allowed exact goodness-of-fit χ² tests, an approach the authors consider impractical for larger K.
- **[[Roseate Tern]] breeding dispersal:** [[Spendelow et al. (1995)]] studied adults across four colonies over five years with 80 parameters. The fully time-dependent model fitted best. Site fidelity estimates were high, with a minimum of 0.825 and 12 of 16 values above 0.900; capture probability varied greatly between sites.
- **[[Snow Goose]] collar loss:** [[Reed & Gauthier]] (in preparation) model collar loss as a transition from a "ringed + collar" state to a "ringed" state.
- **Behavioural state transitions:** In [[Roe Deer]] and [[Black-headed Gull]] studies, multistate models estimate transitions between reproductive states and dispersal between sites.

**2. Canonical accession-to-reproduction model**

- The authors extend [[Clobert et al. (1994)]] to multiple sites. Breeders and non-breeders are treated as separate states, and only breeders are detectable.
- Immature survival is site-dependent up to age 1, and adult survival applies thereafter.
- Natal dispersal (N) is assumed to occur entirely in the first year of life; breeding dispersal (B) is modelled with a separate submatrix.
- Applied to the Roseate Tern metapopulation, the natal dispersal probabilities were larger than the breeding dispersal probabilities, with some parallelism in exchanges. Site A, which had declined markedly, showed the lowest philopatry. Accession to reproduction differed little between sites, with full recruitment by age 5 in the final model.

**3. Longitudinal human data with missing values**

- [[Fitzmaurice et al. (1994)]] analysed weight status (obese or not obese) in 1,014 children over three occasions (1978, 1990, 1992; ages 7–8, 9–11 and 12–14). Over 50% of children had at least one missing value.
- The multistate reanalysis, with constant parameters, gave a survival estimate of about 0.87. The authors found no gender effect on transitions, consistent with the original study.
- A survival estimate different from 1 suggests individuals may leave the study permanently. The missing-data mechanism was judged MCAR under the final model.
- The authors note that Arnason-Schwarz models condition on the first observation, which is a major inadequacy here.

**4. Numerical and statistical difficulties**

- **Boundary estimates:** Many estimates hit 0 or 1. The asymptotic results used for AIC and LRT degrees of freedom do not hold on boundaries; Monte Carlo simulation is suggested.
- **Identifiability:** In a recruitment model with unconstrained breeder and non-breeder survival, parameters were not separately identifiable. Constraining survival to be equal made them identifiable. The authors recommend routinely inspecting profile deviance plots.
- **Local minima:** Roe deer data showed a local minimum of deviance (886.454) above the global minimum (885.547) at the boundary estimate. The authors recommend multiple starting values.
- **Goodness of fit:** No adequate test exists for multistate models. Full enumeration of capture histories becomes prohibitive: for s = 5 and K = 11 there are 60,466,175 histories. Ad hoc alternatives, such as reducing the data to single-state tests within each state, are offered but not fully satisfactory.

**5. Future directions**

- **Multievent models:** Where the observed state is uncertain (for example, a prospecting bird at a colony, or field sex identification errors), a matrix of conditional event probabilities links observations to true states. This framework also allows the full likelihood for the memory model (where transition probabilities depend on earlier history) to be computed.
- **Population growth:** Multistate transition matrices can be linked to population projection matrices, extending the framework toward [[Population Growth Rate]] estimation.
- **Mixed information:** Recoveries, resightings, telemetry and robust-design occasions can be combined within the multistate framework.
- **Software:** The authors note matrix notation facilitates implementation in languages such as MATLAB. A website is listed for case-study data sets.