---
species: "Oncorhynchus mykiss"
common_name: "Rainbow trout"
family: N/A
habitat: "Freshwater river"
ocean_basin: N/A
location: "Upper Rangitikei River, New Zealand"
tags: [mark-recapture, tag-resight, tag-recovery, jolly-seber, population-ecology, fisheries-management, statistical-ecology]
title: "Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data"
source_id: "PML0174"
marsh_id: "PML0174"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. J. Barker (1997). Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data. Biometrics 53, 666-677. Marsh Library ID: PML0174."
source_file: "Barker R.J. 1997. Joint modeling of live recapture tag resight and tag recovery data.pdf"
text_extraction: "text"
---
# Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data

#ichthyology #marine-biology #oncorhynchus-mykiss

## Executive Summary

This methods paper (Barker, *Biometrics* 53, June 1997) proposes a [[Joint Modeling Framework]] for mark-recapture studies in which marked animals are observed three ways: [[Live Recapture]], [[Tag-Resight Model|resighting without capture]] anywhere in the animal's range, and [[Tag-Recovery Model|recovery of dead animals]]. The author derives the likelihood for random movement, gives closed-form [[Maximum Likelihood Estimation]] (MLE), and shows that under [[Random Emigration]] the estimator matches the one suggested by [[Jolly-Seber Model|Jolly (1965)]]. The framework is applied to a pilot study of rainbow trout (*Oncorhynchus mykiss*) in the upper [[Rangitikei River]], New Zealand, where it is used to estimate [[Angling Pressure]] and [[Survival Rate]].

## Background & Description

**Study system.** The paper's empirical case is a pilot study of rainbow trout in the upper Rangitikei River. Fish were tagged at six-monthly intervals beginning March 1993, during spring (October) and autumn (March) tagging operations. Resightings came from anglers who caught tagged trout between capture occasions. Of 68 fish reported captured by anglers, 48 were released, so recapture, tag-resight and tag-recovery all contributed observations after release.

**Motivation.** Jolly (1965) proposed that recaptures and continuous resightings over a wide area could be combined, since the exact time of a resighting does not matter. Earlier approaches had limits:
- [[Brownie and Robson Method|Brownie and Robson (1983)]] required a negligible observation period coinciding with capture occasions.
- [[Mardekian and McDonald Method|Mardekian and McDonald (1981)]] ignored intermediate captures, so they were not fully efficient, and Barker (1995) showed their method holds only under restrictive emigration assumptions.
- [[Burnham Joint Model|Burnham (1993)]] handled joint live-recapture and tag-recovery data, but only where recovered animals were removed from the population.

**Model structure.** The model defines two observation types:
1. *Capture* at times *i* = 1, ..., *t*, applying only to animals "at risk of capture" (for example, birds associated with a banding site, or trout in sampled river sections).
2. *Resighting* in intervals (*i*, *i*+1), for *o* periods, with resightings assumed to occur throughout the whole range.

Losses on capture are handled by conditioning on releases. Losses on resighting correspond to tag recovery and enter the likelihood. A fish caught and released by an angler counts as released on resighting; a killed fish counts as lost.

**Parameters.** The main parameters are survival (*S*), capture probability (*p*), resighting probability (*f*), and movement probabilities between the at-risk and not-at-risk components. The model uses two resighting-related parameters so that no assumption about survival between study times is needed. The paper uses [[Encounter History]] codes adapted from [[Pollock et al 1990|Pollock et al. (1990)]], summarized as a [[Reduced M-Array]] (Table 2) that organizes animals by release cohort and how they were next encountered.

## Ecological & Environmental Context

**Angling pressure as the ecological signal.** The resighting rate is treated as an index of fishing pressure on the trout population, because anglers encounter tagged fish across the whole river. The pilot data distinguish winter resighting rates (periods 1, 3 and 5), which are much lower, from summer rates (periods 2 and 4). The paper reports that during summer at least 15–18% of trout were captured by anglers.

**Sampling limits.** Capture probabilities were low (the scanned text gives "x5%", most likely ≤5%), so a mark-recapture-only study would need very large samples. The number of tag-resightings and recoveries suggested that a tag-recovery-based study might be feasible. However, more than 70% of trout were released by anglers after capture, so most tag-resight information would be unusable under standard procedures such as the models in [[Brownie et al 1985 Band-Recovery Handbook|Brownie et al. (1985)]]. The joint analysis uses all of these sources and can yield more precise estimates from fewer marked animals.

**Survival precision.** Survival estimates were imprecise. Precise survival estimates would need a substantial increase in effort, either more capture effort (raising *p*) or more resighting effort (raising *f*). Because anglers do not report all tagged fish they catch, the paper suggests encouraging anglers to report every tagged fish.

**Population size.** Under random emigration, population size cannot be estimated without restrictive assumptions about recruits. Under [[Permanent Emigration]] or [[Markov Emigration]], the Jolly-Seber estimator remains valid for the number of animals at risk of capture.

## Key Findings

1. **Unified model.** The framework covers live-recapture, tag-resight and tag-recovery models and allows simultaneous analysis of all three. Several published models arise as special cases:
   - No resightings gives the recapture component of the [[Jolly-Seber Model]].
   - All animals released on resighting, with no recaptures, gives the problem treated by [[Cormack Tag-Resight Model|Cormack (1964)]] and Brownie and Robson (1983).
   - Animals removed on resighting gives the [[Seber-Robson-Youngs Bird-Banding Model]] (model M1 of Brownie et al. 1985).
   - All animals lost on resighting gives joint band-recovery and recapture models.

2. **Estimators.** Closed-form MLEs are given for survival, capture and resighting probabilities. Jolly's (1965) estimator is the MLE under [[Random Emigration]]. Under [[Permanent Emigration]] it is not the MLE and is biased. Variances follow from the [[Delta Method]].

3. **Efficiency gains.** Barker (1995) shows that including resightings can noticeably improve precision, especially when capture probabilities are low and resighting probabilities are high. It also reduces sensitivity to heterogeneous capture probabilities.

4. **Goodness-of-fit.** Four component tests are built from the hypergeometric parts of the likelihood, extending [[Pollock Goodness-Of-Fit Tests|Pollock, Hines and Nichols (1985)]] and Burnham et al. (1987). They check:
   - whether resighting has a short-term effect on capture probability (a 2×2 table for each time point);
   - whether the recapture or resighting pattern depends on capture at *i*+1 or resighting in (*i*, *i*+1);
   - subcohort structure, using the hypergeometric distribution conditional on cohorts;
   - whether the probability of release on resighting is the same across marked cohorts.
   Exact hypergeometric probabilities are recommended where expected counts are small.

5. **Emigration ambiguity.** Under random emigration, the expected recapture structure is identical to that under permanent emigration, so the two cannot be distinguished without additional information. The Jolly-Seber survival estimator cannot tell whether it estimates true survival or survival multiplied by permanent-emigration probability. The author argues that extra data permitting separate modeling of emigration types is necessary.

6. **Pilot-study conclusions.** The method is judged promising for estimating angling pressure on the Rangitikei trout fishery. Resighting rates are informative, but survival estimates need more effort before they can be considered precise.

**Acknowledgements and funding.** The author thanks Jim Nichols, Ken Pollock and Peter Taylor (who supplied the trout data), and three anonymous referees. Funding came from Massey University and the Hopkins Family Trust.