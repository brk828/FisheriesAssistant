---
species: "Cinclus cinclus; Apus apus; Capreolus capreolus; Lacerta vivipara; Phoenicopterus roseus"
common_name: "European Dipper; Common Swift; Roe Deer; Common Lizard; Greater Flamingo"
family: "Cinclidae; Apodidae; Cervidae; Lacertidae; Phoenicopteridae"
habitat: "Mountain streams; urban colonial nest sites; enclosed forest; peat bogs and heathland; lagoons and coastal lakes"
ocean_basin: "N/A"
location: "Eastern France (dipper, roe deer, lizard); Nimes and Camargue, southern France (swift, flamingo); Europe (general)"
tags: [capture-recapture, survival-analysis, population-ecology, statistical-ecology, animal-marking]
title: "Modeling survival and testing biological hypotheses using marked animals: a unified approach with case studies"
source_id: "PML1350"
marsh_id: "PML1350"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J.-D. Lebreton et al. (1992). Modeling survival and testing biological hypotheses using marked animals: a unified approach with case studies. Ecological Monographs 62(1): 67-118. Marsh Library ID: PML1350."
source_file: "Lebreton J.D. et al. 1992. Modeling survival and testing biological hypotheses using marked animals, a unifies approach with case studies.pdf"
text_extraction: "text"
---
# Modeling Survival and Testing Biological Hypotheses Using Marked Animals: A Unified Approach with Case Studies

#ichthyology #marine-biology #N/A

*Note: This document is a methodological and population ecology monograph, not an ichthyological study. The tag line above follows the required format; the taxa treated are birds, mammals and reptiles, with no fish data.*

## Executive Summary

This monograph (Lebreton et al., *Ecological Monographs* 62(1), 1992) synthesizes capture-recapture and resighting models for estimating animal survival rates from individually marked animals. It presents a unified framework built on the [[Cormack-Jolly-Seber Model]] (CJS), extends it to multiple data sets and cohorts, and recommends a model-building workflow: start from a biologically justified global model, reduce it using [[Akaike's Information Criterion]] (AIC), then test specific hypotheses with [[Likelihood Ratio Test]]s. Five worked examples on European Dippers, Common Swifts, Roe Deer, Common Lizards and Greater Flamingos illustrate the approach. The authors emphasize that analysis now centers on model selection rather than fitting a single model, and that computational software such as [[Program SURGE]] and [[Program RELEASE]] makes this practical.

## Background & Description

Survival is a central life-history parameter, but it is hard to estimate in the wild because the fate of marked individuals is often unknown when they stop being observed. Early [[Capture-Recapture Methods]] treated survival as a nuisance parameter and focused on population size. During the 1980s the emphasis shifted to survival rates, supported by the CJS model, which is conditional on first capture.

The paper's model framework includes:

- Parameters for apparent survival (φ) and capture or recapture probability (p), both conditional on the animal being alive and available.
- Time-, age-, cohort- and covariate-dependent structures, including link functions (logit, log, identity, hazard).
- Multi-group ("multiple data set") models in which groups such as sexes, colonies or treatments share some parameters.
- Goodness-of-fit testing via [[Program RELEASE]] TESTS 2 and 3, and variance inflation (ĉ) for extra-binomial variation.
- Profile likelihood intervals, which are preferred over asymptotic intervals for small samples or boundary estimates.

Key assumptions are independence of fates and identity of rates among marked individuals. The authors note that these are often violated in field studies, particularly in fish populations where capture may depend on body size.

## Ecological & Environmental Context

The examples show how survival and capture estimates depend on habitat and environmental conditions:

- **[[European Dipper]] (*Cinclus cinclus*)**: Mountain stream specialist that nests near water. Winter severity and floods are expected to affect survival. The study covered 22 birds (Table 3) and a larger later dataset of 294 birds (by sex) from eastern France, 1981–1987.
- **[[Common Swift]] (*Apus apus*)**: Urban colonial breeder nesting in buildings. Two neighboring colonies in Nîmes differed in exposure, one sheltered (Good) and one exposed to wind (Poor).
- **[[Roe Deer]] (*Capreolus capreolus*)**: Territorial cervid in a 260-ha enclosure in the Chizé forest, with density and winter conditions as covariates.
- **[[Common Lizard]] (*Lacerta vivipara*)**: Peat bog and heathland species in southern France, where a density manipulation was carried out between two fields.
- **[[Greater Flamingo]] (*Phoenicopterus roseus*)**: Colonial breeder in the Camargue lagoons. The 1984–1985 winter, with lagoons frozen for two weeks, caused heavy mortality.

Few of these examples involve aquatic fish. Only the dipper and flamingo are closely tied to water, and the authors note that fish populations are a case where capture heterogeneity is frequent.

## Key Findings

**Methodological conclusions**

- Model selection, not single-model fitting, is the central task. A global model should match species biology and design, then be reduced by AIC, then tested with a few likelihood ratio tests against neighboring models.
- AIC performed well in the authors' comparisons, usually selecting the same or a nearly identical model to expert choice. The authors recommend keeping candidate models within about one AIC unit of the optimum.
- Goodness-of-fit tests have low power at typical sample sizes. The authors suggest using α = 0.15 for model rejection, with caution.
- Where data show extra variation, the variance inflation factor ĉ = χ²/df should be applied, and standard errors inflated by √ĉ. Values of ĉ above about 3 suggest the model structure is seriously inadequate.
- Design recommendations: maximize the number of released animals and capture probability; plan for at least 10–20 survival estimates (11–21 capture occasions); avoid mark loss; and consider power analysis before fieldwork.

**Example results**

- **Dipper**: Model with constant survival and capture (φ, p) fitted well (LRT χ² = 2.79, df = 1, p = .0951, as reported). Mean annual survival was estimated at 0.56 (SE 0.02) and capture at 0.9. A flood-year model fitted better than the constant model (LRT χ² = 6.74, p = .0094). Survival in flood years was lower than in normal years.
- **Swift**: Colony effects on survival were estimated (good 0.763, SE 0.039; poor 0.621, SE 0.083). The colony difference was significant only as a combined survival-and-capture effect (LRT χ² = 8.295, p = .0159). The authors caution that apparent survival in the poor colony may partly reflect permanent emigration.
- **Roe Deer**: The final model had seven parameters. Females survived better than males, and the mature age classes showed higher survival on the logit scale. Density dependence was weak (one-sided p = .0631). A low survival rate in 1986–1987 dominated the time variation. Senescence was not clearly supported.
- **Common Lizard**: A fifth-cohort effect (captured June 1988) was significant (χ² = 11.826, p = .0027). Survival did not differ detectably between fields before and after the density manipulation. The final annual survival was 0.455 (95% CI 0.355–0.611).
- **Greater Flamingo**: Using adults over 5 years old (284 males, 331 females), survival was 0.973 in normal winters and 0.785 in the severe 1984–1985 winter, a reduction of about 0.19. Overdispersion was ĉ = 2.314. Trap dependence was significant (F = 5.230, p = .0332). No significant sex effect on survival was found.

**Overall message**

The authors argue that ad hoc "return rate" methods, which estimate only a product of survival and capture, can mislead. Capture-recapture modeling separates the two, provided the design, global model and goodness-of-fit checks are sound.