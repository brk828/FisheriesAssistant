---
species: "Setophaga coronata (Dendroica coronata)"
common_name: "Myrtle Warbler (Yellow-rumped Warbler)"
family: "Parulidae"
habitat: "Coastal island stopover site; songbird migration habitat (mist-netting sites)"
ocean_basin: "Atlantic Ocean (Northwest Atlantic coast)"
location: "Bon Portage Island, Nova Scotia, Canada"
tags: [ichthyology, marine-biology, ornithology, mark-recapture, bayesian-statistics, migratory-stopover, songbirds]
title: "A hierarchical Bayesian approach to multi-state mark-recapture: simulations and applications"
source_id: "PML0356"
marsh_id: "PML0356"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. M. Calvert, S. J. Bonner, I. D. Jonsen, J. Mills Flemming, S. J. Walde, P. D. Taylor (2009). A hierarchical Bayesian approach to multi-state mark-recapture: simulations and applications. Journal of Applied Ecology 46, 610-620. Marsh Library ID: PML0356."
source_file: "Calvert A.M. et al. 2009. A hierarchical bayesian approach to multistate mark  recapture .pdf"
text_extraction: "text"
---
# Hierarchical Bayesian Multi-State Mark-Recapture Modelling of Migratory Stopover Decisions

#ornithology #mark-recapture #bayesian-statistics #parulidae

## Executive Summary

This Journal of Applied Ecology article (Calvert et al., 2009) develops a general hierarchical Bayesian multi-state mark-recapture model for sparse ecological data, tests it on simulated datasets, and applies it to 11 years of autumn stopover data for [[Myrtle Warbler]] migrants at [[Bon Portage Island]], Nova Scotia. The model borrows information across years, producing more precise estimates of [[Departure Probability]] and [[Transience Probability]] than non-hierarchical Bayesian and frequentist [[MARK Software]] approaches. Inter-annual variability suggested by those other methods was largely attributed to sampling error.

Note: the source is a methods paper on statistical modelling applied to songbird data. It contains no fish or aquatic-ecosystem data; the taxon is a passerine bird.

## Background & Description

- **Study system:** Hatch-year Myrtle Warblers (*Dendroica coronata*) were leg-ringed during peak autumn migration (23 September–31 October) as part of a constant-effort mist-netting programme of the [[Bird Studies Canada]] Canadian Migration Monitoring Network, 1996–2006.
- **Sample size:** Between 52 and 562 birds (median 207) were ringed each year.
- **Stopover states:** Individuals were modelled in three states: an initial state (first capture only), a non-transient state (able to be recaptured), and a transient state (departing within 24 h and thus unrecapturable).
- **Fat-load groups:** Birds were classed as "high" fat (furcula at least half-full) or "low" fat (furcula less than half-full or empty) at marking.
- **Model basis:** The multi-state framework extends the [[Cormack-Jolly-Seber Model]] and builds on [[Multi-State Mark-Recapture]] theory and [[Hierarchical Bayesian Inference]] implemented in [[WinBUGS]] and OpenBUGS.
- **Motivation:** The [[Robust Design]] models cannot allow state transitions within primary sampling periods, and traditional methods perform poorly with low survival, low capture probability or small samples.

## Ecological & Environmental Context

- Stopover parameters are analogous to demographic rates: departure corresponds to mortality and transience to movement.
- Daily capture probabilities of migrating songbirds are typically low, roughly 2.3–10.0% in cited studies.
- Fat stores matter for departure decisions, since migrants often carry fuel before crossing barriers such as open ocean.
- Estimates from this type of analysis inform the status of species at risk and conservation or management protocols.

## Key Findings

- **Simulation performance (good data):** With 200 individuals per state, capture probability 0.80, survival 0.70 and 0.90, and movement 0.15 and 0.35, posterior medians of annual and hierarchical means were very close to true values, and 95% credible intervals always included them.
- **Poor-data simulations:** Twelve scenarios (combinations of capture probability 0.20 or 0.05, survival levels, and N = 50 or 200) were run with 25 replicates each. Mean bias was below 0.10 in 32 of 36 parameter-scenario combinations. Exceptions occurred mainly with N = 50 and very low capture (p = 0.05). Bias was greatest for capture probability, and it was most sensitive to low survival combined with small samples or very low capture.
- **Mixed-quality years:** The hierarchical model produced less variable, more accurate estimates and narrower credible intervals than the non-hierarchical model. Years with very low capture were shrunk more strongly toward the hierarchical mean.
- **Model convergence:** Scale reduction factors were below 1.05 for all parameters within 10,000 iterations. Analyses used a 10,000-iteration burn-in and 50,000 further iterations (the stopover analysis used a 20,000-iteration burn-in and 50,000 iterations).
- **Stopover application:** Median departure probabilities were generally higher for high-fat than low-fat birds. The fat effect was clearer in hierarchical estimates. Wide credible intervals gave little evidence for a fat effect on transience.
- **Capture probability:** Hierarchical means were 0.040 (95% CI 0.021–0.092) for high-fat and 0.053 (0.033–0.085) for low-fat birds, with overlapping intervals.
- **Interpretation:** Hierarchical models treat imprecise deviations as sampling error, so they can slightly underestimate true inter-annual variation when data are sparse, but they yield less biased and more precise estimates overall.
- **Recommendations:** Where survival is low or unknown, increase the number of marked individuals and capture probability, for example by improving net placement or using colour rings. Reversible-jump MCMC is suggested as a next step for model selection.
- **Overall conclusion:** The framework is structurally flexible and applicable to other nested designs, species, sites or single-state models, and it strengthens inference from sparse mark-recapture data.