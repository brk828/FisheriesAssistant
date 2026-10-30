---
species: ["Anas rubripes", "Dryobates borealis", "Cinclus cinclus"]
common_name: ["American Black Duck", "Red-cockaded Woodpecker", "European Dipper"]
family: ["Anatidae", "Picidae", "Cinclidae"]
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [known-fate-models, survival-analysis, radio-telemetry, capture-recapture, methods]
title: "Models Where the Fate of Every Individual is Known"
source_id: "PML1913"
marsh_id: "PML1913"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Unknown author (n.d.). Models Where the Fate of Every Individual is Known. Marsh Library ID: PML1913."
source_file: "Models where the fate of every individual is known.pdf"
text_extraction: "text"
---
# Known Fate Models for Estimating Survival from Radio-Tagged Animals

#ornithology #survival-analysis #known-fate-models

## Executive Summary

This methods text explains [[Known Fate Models]], a class of survival models in which the fate (alive or dead) of every marked animal is known at each sampling occasion. Because sampling probabilities are assumed to equal 1, the models estimate interval survival probability (S) with high precision even at modest sample sizes. The text compares the [[Kaplan-Meier Method]] with a [[Binomial Model]] fitted by [[Maximum Likelihood Estimation]], explains encounter-history coding and [[Censoring]] rules, and shows how [[Individual Covariates]] can be modeled through a [[Logit Link Function]]. Worked examples use [[Black Duck]] radio-telemetry data and a [[Red-Cockaded Woodpecker]] nestling study. The document is a statistical tutorial, not an aquatic study, and its direct relevance to aquatic ecosystems is limited.

## Background & Description

Known fate models rely on the estimation of survival probability S, the probability that an animal survives an interval between sampling occasions. The text notes that these models suit [[Radio Telemetry]] data, where the status of each tagged animal is confirmed. Costs of radios and possible effects of radios on behavior are the main stated disadvantages. The approach also applies to egg mortality in nests and to sessile organisms such as mollusks.

The text presents three ways of structuring the analysis:

- **Kaplan-Meier Method (1958):** The traditional starting point, used when all animals are marked and released at occasion 1. The estimator is a step function of cumulative survival, useful for comparing groups such as males and females.
- **Staggered entry (Pollock et al. 1989):** New animals are released at later occasions. Under [[Pollock's Staggered Entry Design]], the Kaplan-Meier risk set is redefined to include newly released animals, so the approach needs no new machinery.
- **Binomial model:** The product of binomial likelihoods across intervals. It supports standard likelihood inference and is the basis for the model-selection tools in [[Program MARK]].

Each tagged animal falls into one of three outcomes: it survives to the end of the study, it dies during the study and its carcass is found at the next sampling occasion, or it is censored (for example, through radio failure) at some point.

## Ecological & Environmental Context

The worked examples concern terrestrial birds, not aquatic organisms. The [[Black Duck]] study (Conroy et al. 1989) tracked 48 radio-tagged birds, and the [[European Dipper]] is cited for its flood years, which may define distinct survival periods. The [[Red-Cockaded Woodpecker]] example involves nest-bound nestlings checked by daily visual inspection rather than radio tracking. The text states that nestling fate can be treated as known-fate data even though the birds carry no radios.

The text also flags ecological complications. Censoring may arise from radio failure or from animals leaving the study area. Radio failure may depend on mortality, which can bias survival estimates. Covariates such as body weight can change over time, and in band-recovery and open capture-recapture models, animals never recaptured lack covariate values at later occasions. The text says this problem does not arise in known-fate studies when animals are physically handled rather than only resighted.

## Key Findings

**Kaplan-Meier example (black ducks, 48 radio-tagged birds, 8 weekly intervals):** The survival estimates reported in the text are:

| Interval | Survival estimate | Calculation |
|---|---|---|
| S1 | 0.979 | 47/48 |
| S2 | 0.957 | 45/47 |
| S3 | 0.951 | 39/41 (2 censored/removed from denominator per text) |
| S4 | 0.872 | 34/39 |
| S5 | 0.875 | 28/32 (2 censored) |
| S6 | 0.893 | 25/28 |
| S7 | 0.960 | 24/25 |
| S8 | 1.000 | 24/24 |

The text notes that this full model has 8 parameters, S(t), and that simpler alternatives are possible: a constant model S(.), a two-period model, or a smooth function with an intercept and slope.

**Binomial example (modified black duck data):** The first-interval survival is estimated as 44/48 = 0.917. The log-likelihood is the sum over intervals of the binomial terms, so the full likelihood is a product of independent binomials.

**Encounter-history coding:** Each interval is coded as a pair of digits:

- `10`: survived the interval, given alive at its start
- `11`: died during the interval
- `00`: censored for that interval

The text stresses that a fate is known only if the animal is seen at both the start and end of the interval. Censored intervals usually occur in runs of two or more `00` pairs. The text warns that filling censored gaps with `10` pairs, on the assumption that the animal survived, introduces bias.

**Censoring:** Censoring is assumed to be independent of fate. If many animals are censored, dependence between fate and censoring becomes a concern, and the text recommends considering models that allow sampling probabilities below 1.

**Individual covariates:** Each animal i gets its own survival probability, linked to its covariate X_i by a logit model, logit(S_i) = β₀ + β₁X_i. The MLEs for β₀ and β₁ are the parameters of interest. The text recommends AIC, AICc or QAICc for model ranking, with Akaike weights and evidence ratios for strength of evidence.

**Woodpecker example (illustrative only):** A biologist monitors 88 nestlings from 88 nests, one bird per nest, over 12 daily occasions (days 3 to 15). Three covariates are measured: ectoparasite count, number of nest mates, and hatching weight. The proposed model is logit(S_i) = β₀ + β₁(E) + β₂(H) + β₃(W). The text describes this as an example of how model selection and covariate interpretation could proceed, not as a completed analysis.

**Main conclusions:** The text argues that individual covariates are underused in biological studies, and that known-fate designs allow fuller use of individual information than many investigators currently exploit.