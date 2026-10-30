---
species: Oncorhynchus mykiss
common_name: Rainbow trout
family: N/A
habitat: Freshwater river (upper Rangitikei River, trout fishery)
ocean_basin: N/A
location: Rangitikei River, New Zealand
tags: [ichthyology, marine-biology, oncorhynchus-mykiss, mark-recapture, tag-resight, tag-recovery, fisheries-statistics, joint-modeling]
title: "Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data"
source_id: "PML0173"
marsh_id: "PML0173"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Richard J. Barker (1997). Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data. Biometrics, Vol. 53, No. 2, pp. 666-677. Marsh Library ID: PML0173."
source_file: "Barker R.J. 1997. Joint modeling of live recapture tag resight and tag recovery data .pdf"
text_extraction: "text"
---
# Joint Modeling of Live-Recapture, Tag-Resight, and Tag-Recovery Data

#ichthyology #marine-biology #oncorhynchus-mykiss

## Executive Summary

This statistical paper by [[Richard J. Barker]] (Department of Statistics, Massey University) proposes a [[Joint Modeling Framework]] for [[Mark-Recapture Studies]] that combine three kinds of observation on marked animals: live recapture, resighting without capture, and tag recovery from dead animals. The model extends the [[Jolly-Seber Model]] to include resightings made at any time between capture occasions. Closed-form [[Maximum Likelihood Estimator]]s are derived. The estimator matches the one suggested by [[Jolly (1965)]], but only under the [[Random Emigration]] assumption.

The model is applied to a pilot study of [[Rainbow Trout]] (*Oncorhynchus mykiss*) in the upper [[Rangitikei River]], New Zealand. The study tests whether tagging can estimate [[Angling Pressure]] on the trout fishery. The pilot data show that resighting rates are much higher in summer than in winter, and that survival rates are poorly estimated.

## Background & Description

**Problem.** In [[Mark-Recapture Studies]], marked animals are observed after release in three main ways:

- **Live recapture** at later sampling occasions (the setting of the original [[Jolly-Seber Model]]).
- **Resighting** of tagged animals without physical capture, for example by anglers or observers across a wide area.
- **Tag recovery** from animals found dead, commonly through hunting or fishing.

Data often combine all three. Earlier methods handled them separately. [[Brownie et al. (1985)]] and [[Burnham (1993)]] addressed parts of the problem, and [[Mardekian and McDonald (1981)]] proposed an estimator for combined recovery and recapture data. The author argues that Mardekian and McDonald's method is not fully efficient because it ignores intermediate captures, and that it rests on restrictive emigration assumptions (see [[Barker (1995)]]).

**Model structure.** The model assumes:
- Capture occurs at discrete, regularly spaced occasions, treated as instantaneous.
- Only animals "at risk of capture" can be physically captured. Resightings can occur anywhere in the population's range.
- Losses on capture and resighting are included, and the number of animals released after capture is treated as fixed and known.
- Animals released after resighting are classed separately from those released after capture.

**Parameters.** The model uses survival probabilities, capture probabilities, resighting probabilities, and probabilities of being at risk of capture. Two resighting-related parameters (the probabilities of being resighted, and of not being resighted, in each interval) are needed because no assumption is made about survival between sampling times. The emigration structure is handled by modeling "at risk" status between occasions.

**Assumptions.** The model extends the standard [[Jolly-Seber Model]] assumptions (Seber 1982), including:
1. All animals share the same survival and capture parameters at a given time.
2. Animals at risk of capture share one parameter set, and animals not at risk share another.
3. Resightings occur throughout the range, but capture occurs only in the at-risk part.
4. The resighting probability does not depend on where animals are located in their range.

**Data coding.** Data are summarized by encounter-history codes adapted from [[Pollock et al. (1990)]]. The paper uses a reduced m-array, following [[Burnham et al. (1987)]], as the sufficient statistic. The codes cover capture, release, resighting, and non-observation, in combinations of "released" and "not released" on observation.

## Ecological & Environmental Context

**Study system.** The pilot study used [[Rainbow Trout]] in the upper Rangitikei River, New Zealand. Fish were tagged at six-monthly intervals starting March 1993, through to March 1995, with resightings recorded through October 1995. Tagging took place in spring (October) and autumn sessions. Anglers provided the resighting data by reporting tagged fish they caught between capture occasions.

**Fishery relevance.** The model was tested to see whether tagging could estimate angling pressure on a trout fishery. Resighting rates serve as an index of how heavily the fishery is fished. Resighting is an efficient way to gather this information, which makes the [[Joint Modeling Framework]] useful for fisheries management.

**Exposure and loss.** Fish at risk of capture were those present in the river sections sampled during tagging. Any fish caught and released by an angler was counted as "lost on resighting" when it was not released after being reported. The paper notes that more than 70% of tagged trout were released by anglers upon capture. This makes most tag-resighting information unusable under standard procedures, such as those in [[Brownie et al. (1985)]].

## Key Findings

**Methodological results**

- **Joint estimators.** Closed-form [[Maximum Likelihood Estimator]]s are derived for survival, capture, resighting, and related parameters. The estimators use the sufficient statistics from the reduced m-array. The total number of minimally sufficient statistics is 5t − 3, matching the number of identifiable parameters (with *t* capture occasions).
- **Equivalence to Jolly (1965).** Under [[Random Emigration]], the estimator matches [[Jolly (1965)]]. Under permanent emigration, Jolly's estimator is biased and is not the MLE when resightings are present. Under Markov emigration, the equality does not hold for either definition of the marked population.
- **Goodness-of-fit tests.** The paper develops tests based on hypergeometric components of the likelihood, using methods from [[Pollock et al. (1985)]]. Test 1 checks whether resighting has a short-term effect on capture probability. Test 2 checks whether recapture depends on resighting in the next interval. Tests 3 and 4 look at subcohort structure and release-on-resighting patterns. Where expected cell counts are small, exact tests or pooled cells are recommended.

**Pilot study results (Rangitikei River trout)**

- **Resighting rates.** Winter resighting rates (periods 1, 3, and 5) are much lower than summer rates (periods 2 and 4). During summer, at least 15–18% of trout are estimated to be caught by anglers.
- **Survival rates.** Monthly survival estimates are not precisely determined, with large standard errors. Precise survival estimates would need a substantial increase in sampling effort.
- **Capture probabilities.** Capture probabilities are low, around 5%. A mark-recapture-only design would therefore need very large sample sizes.
- **Feasibility.** The large number of tag resightings and recoveries suggests that a tag-recovery-based study might be feasible. The joint analysis lets all sources of information be used, which yields more precise estimates from fewer marked animals.
- **Management recommendation.** Because anglers do not report all tagged fish they catch, encouraging anglers to report every tagged fish would increase the effective resighting probability.

**Population size**

- Under random emigration, the population size (total or at risk of capture) **cannot be estimated** without an additional restrictive assumption about the movement of recruits. This restriction is usually unreasonable. The same limitation applies to the standard Jolly-Seber model without resightings.
- Under permanent or Markov emigration, the Jolly-Seber MLE is a valid estimator of the number of animals at risk of capture.

**Special cases**

- No resightings: the model reduces to the recapture component of [[Jolly-Seber Model]].
- All animals released on resighting: the model generalizes [[Cormack (1964)]] by allowing resightings throughout the interval between releases.
- All animals removed on resighting: the model reduces to the [[Seber-Robson-Youngs Bird-Banding Model]] described by [[Brownie et al. (1985)]].
- Joint band-recovery and recapture models follow from [[Burnham (1993)]], with the resighting-related parameter interpreted as the band-recovery rate.

**Key limitation.** The paper argues that the Jolly-Seber model cannot separate random from permanent emigration when no resightings exist, because both give the same expected recaptures. Survival estimates from the Jolly-Seber model therefore have an ambiguous meaning. Additional information, such as resightings, is needed to model the two kinds of emigration separately.