---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [biostatistics, population-ecology, capture-recapture, tag-return, meta-population, insecta]
title: "Separation of survival and movement rates in multi-state tag-return and capture-recapture models"
source_id: "PML1205"
marsh_id: "PML1205"
library: "Marsh Library"
permission: "not public domain"
source_citation: "M. Joe, K. H. Pollock (2002). Separation of survival and movement rates in multi-state tag-return and capture-recapture models. Journal of Applied Statistics, Vol. 29, Nos. 1-4, pp. 373-384. Marsh Library ID: PML1205."
source_file: "Joe M. et al. 2002. Separation of surviavl and movement rates in multi state tag rturn and capture recapture models.pdf"
text_extraction: "text"
---
# Separation of Survival and Movement Rates in Multi-State Tag-Return and Capture-Recapture Models

#population-ecology #capture-recapture #biostatistics #insecta

## Executive Summary

This statistical methods paper (Joe & Pollock, *Journal of Applied Statistics*, 2002) extends [[Multi-State Models|multi-state tag-return and capture-recapture models]] so that [[Survival Rate|survival]] and [[Movement Rate|movement]] rates can be estimated separately. Earlier work assumed movement occurs at the end of each interval. The authors instead treat the time of movement within the interval as a random variable with a known distribution, specifically a [[Uniform Distribution]] or a [[Beta Distribution]]. Simulation studies using a modified [[SURVIV Program]] evaluate bias and precision, and a reanalysis of [[Iwao Insect Data]] illustrates the method. The document is not about fish or any aquatic system. It addresses general population ecology and meta-population management.

## Background & Description

Meta-populations are sets of local populations linked by occasional migration, and their persistence depends on local colonization and extinction (Gilpin & Hanski, 1991). Population ecologists have long focused on birth and death rates, while movement has been harder to estimate because of data and methodological limits (Hestbeck, 1995). Multi-state capture-recapture models (Hestbeck et al., 1991; Brownie et al., 1993; Schwarz et al., 1993) estimate transition probabilities among states. Each transition probability is the product of a survival probability and a movement probability.

The model is built on the [[Arnason-Schwarz Model]] for multiple-state tag-recovery data, and it extends the Brownie et al. (1985) framework. The paper gives two formulations:

- **Tag-return (recovery) data:** animals are released once and may be recovered only once.
- **Capture-recapture data:** animals may be captured repeatedly. The authors show that suitable parameter redefinitions let the same methods apply to both designs (Schwarz et al., 1993).

Standard assumptions are retained. These include no temporary migration out of sampled strata, independent animal behaviour, Markovian movement, and known tag-reporting rates with standard errors. Movement time is modelled in three ways:

1. Movement at the beginning or end of the interval (θ = 0 or 1), as in earlier work.
2. Movement at a fixed time within the interval, which requires iterative estimation because no explicit MLEs exist.
3. Movement time as a random variable with a known density f(θ). Two cases are treated: uniform, which corresponds to random movement, and beta, which is flexible and reduces to uniform when α = β = 1.

## Ecological & Environmental Context

The authors motivate the work with conservation needs for fragmented habitats. Separating survival from movement matters for managing meta-populations, because a patch can have low survival or high emigration, and these produce different management responses (Nichols et al., 1992). Movement can also be estimated with radio-telemetry, which the authors note can be combined with capture-recapture or tag-return data (Powell et al., 2000). The worked example uses insect data on movement between two food plants (Iwao, 1963), a terrestrial system that differs from the aquatic systems the prompt asks about.

## Key Findings

- **Tag-return simulations (24 cases, 500 runs each):** Factors were N tagged (500, 1000, 2000, 5000), movement rate (high 75%, low 25%), and recovery rate (0.1, 0.2, 0.4). Eight beta-distribution shapes were tested. Bias was generally below 2% when movement was low. When movement was high, bias for survival in the asymmetric case (α < β) reached about 13% at N = 500 and dropped with larger samples.
- **Reduced model effect:** Holding survival constant across years roughly halved the bias and sharply reduced RSEs by reducing the number of parameters.
- **Precision:** RSEs fell as more animals were tagged and improved with higher capture or recovery rates (0.4 versus 0.1).
- **Correlations (tag-return, high movement):** Movement and survival estimates for the same area were strongly correlated, with the strength depending on the distribution shape. Movement and survival estimates for different areas were also substantially correlated.
- **Capture-recapture simulations (18 cases, 500 runs each):** Factors were N tagged (500, 1000, 2000), movement rate (75% or 25%), and capture rate (0.1, 0.2, 0.4). Bias was below 2% in most cases and was greatest for the movement-related estimate at N = 500 (up to 14%). Survival and movement estimates for the same area had a substantial negative correlation (−0.81 to −0.43). Survival estimates for different areas were strongly negatively correlated (−0.89 to −0.70).
- **Iwao insect example:** The authors reanalysed the Iwao data, which required constant capture probabilities within each area to achieve convergence. Their 1,000-run simulation produced estimates close to the true values. Their method also estimated survival and movement separately, assuming uniform movement timing (Table 9). Movement rates were moderate, around 30%, in all cases.
- **Limitations and future work:** The authors did not test how robust inferences are to misspecification of the movement-time distribution. They also recommend telemetry data to check the assumption that movement rate does not depend on movement time, to allow separate survival rates for resident and departing animals, and to estimate the movement-time density. Extensions to unknown movement-time distributions and equal catchability are also proposed.