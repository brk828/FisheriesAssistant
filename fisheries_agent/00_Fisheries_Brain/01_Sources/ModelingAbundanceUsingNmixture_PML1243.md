---
species: "Cormobates leucophaeus; Rhipidura fuliginosa; Dicaeum hirundinaceum; Pachycephala rufiventris; Pachycephala pectoralis; Petroica multicolor"
common_name: "White-throated Treecreeper; Gray Fantail; Mistletoebird; Rufous Whistler; Golden Whistler; Scarlet Robin"
family: N/A
habitat: "Eucalypt woodland (stringybark forest and gum woodland); low shrubland"
ocean_basin: N/A
location: "Mount Lofty Ranges, South Australia"
tags: [ornithology, ecological-modeling, abundance-estimation, woodland-birds, n-mixture]
title: "Modeling abundance using N-mixture models: the importance of considering ecological mechanisms"
source_id: "PML1243"
marsh_id: "PML1243"
library: "Marsh Library"
permission: "not public domain"
source_citation: "L. N. Joseph, T. G. Martin, H. P. Possingham (2009). Modeling abundance using N-mixture models: the importance of considering ecological mechanisms. Ecological Applications 19(3): 631-642. Marsh Library ID: PML1243."
source_file: "Jospeh L.N. et al. 2009. Modeling abundance using N mixture mdels, the importanc of considering ecological mechanisms.pdf"
text_extraction: "text"
---
# Zero-Inflated N-Mixture Models for Estimating Bird Abundance

#ornithology #ecological-modeling #woodland-birds

## Executive Summary

This paper develops the [[N-Mixture Model]] (Royle 2004) to handle zero-inflated count data by using [[Zero-Inflated Poisson]] (ZIP) and [[Zero-Inflated Negative Binomial]] (ZINB) forms. The authors fit four variants (Poisson, ZIP, [[Negative Binomial]], ZINB) to survey data for six woodland bird species in the [[Mount Lofty Ranges]], [[South Australia]], estimating abundance, [[Detection Probability]] and, for zero-inflated forms, [[Occupancy Modeling|probability of occupancy]]. Models are compared on statistical fit ([[Akaike Information Criterion]], AIC) and on [[Ecological Realism]], judged against literature values and expert opinion. The ZINB was the top-ranked model by AIC for all six species, yet its parameter estimates were often ecologically implausible. The authors conclude that the ZIP is the more defensible choice because it models an ecological mechanism (unoccupied sites) rather than a statistical property of the data, and they recommend against routine use of negative binomial N-mixture models for abundance and detection.

## Background & Description

**Purpose and motivation.** Predicting abundance across a species' distribution supports conservation planning and ecological inference, but predictive models built from survey data are often unstable. Count variation has two sources: *true variation* (environmental gradients, metapopulation dynamics, competition, stochasticity) and *false variation* (miscounting, imperfect detection, and absence of individuals that use a site without being present during the survey). A useful model must address both.

**Distribution models.** [[Poisson Regression]] assumes Poisson-distributed error and fails under extra-Poisson variation ([[Overdispersion]]) or [[Zero Inflation]], which arises when many surveyed sites are unoccupied. Negative binomial models accommodate overdispersion by letting the mean vary stochastically, but they cope poorly with large numbers of zeros. Truncating the data to remove zeros discards information about occupancy and can remove zeros produced by detection error. ZIP and ZINB regressions estimate occupancy and abundance together, without truncation.

**The N-mixture framework.** The N-mixture model uses spatially and temporally replicated counts to estimate abundance and detection simultaneously. Observed counts are binomially distributed given the true abundance N and detection probability p; N is itself modeled as a random variable following a Poisson or negative binomial distribution. Detection is modeled with a logit link on covariates such as time of day, season or observer. The authors' novel contribution is the zero-inflated extension, which adds an occupancy component (a Bernoulli process) to the abundance distribution, using a mixture formulation in which some zeros come from the occupancy process and others from the count distribution.

**Survey design.** Surveys ran from 25 August to 19 December 2000 in the Mount Lofty Ranges, an area of national conservation significance with Mediterranean climate, eucalypt woodland and low shrubland. Two vegetation types were sampled: "stringybark" forest (dominated by *Eucalyptus obliqua* and *E. baxteri*) and "gum" woodland (dominated by *E. leucoxylon* and/or *E. fasciculosa*). The team used [[Time-Area Search]] in 2-ha plots (20 minutes per plot, following [[Loyn 1986]]) and assumed population closure over the survey period, justified by surveys being conducted in the first half of the breeding season.

**Focal species.** Six of 111 identified species were chosen to span a range of abundances, detection probabilities and occupancies:
- [[White-throated Treecreeper]] (*Cormobates leucophaeus*)
- [[Gray Fantail]] (*Rhipidura fuliginosa*)
- [[Mistletoebird]] (*Dicaeum hirundinaceum*)
- [[Rufous Whistler]] (*Pachycephala rufiventris*)
- [[Golden Whistler]] (*Pachycephala pectoralis*)
- [[Scarlet Robin]] (*Petroica multicolor*)

**Covariates.** Five covariates were chosen from expert opinion and preliminary AIC-based fitting: rainfall, solar radiation, area of vegetation cover within a 5-km buffer, Julian day of survey, and time of day. Julian day and time of day modeled detection; rainfall, solar radiation and the 5-km buffer modeled abundance and occupancy. Models were fitted by maximum likelihood in MATLAB, with covariates standardized, and 95% confidence intervals calculated as estimate ± 1.96 SE.

## Ecological & Environmental Context

**Sites and vegetation.** Of 109 sites, 48 (44%) were in stringybark forest and 61 (56%) in gum woodland. Each site was visited nine times.

**Expected occupancy patterns.** Predictions drew on vegetation preferences and expert opinion:
- *Mistletoebird* and *Rufous Whistler* have a well-known preference for gum woodland. Because surveys covered both vegetation types, their counts were expected to be zero-inflated.
- *Scarlet Robin* has declined substantially across much of its former range in the Mount Lofty Ranges, so it was expected to be absent from more than 50% of sites (i.e., at least 54 sites).
- The other three species (White-throated Treecreeper, Gray Fantail, Golden Whistler) were found throughout the study region and were not expected to show excess true zeros.

**Plausibility benchmarks.** Expected values came from the *Handbook of Australian, New Zealand and Antarctic Birds* (Higgins et al. 2001, 2002, 2006), the maximum published density per species, doubled to give birds per 2 ha. Experts provided a lower bound of 0.1 on detection probability (an individual present should be detected at least once in 10 surveys). Models were judged unrealistic if they estimated more than 10 birds per 2 ha above the benchmark, a detection probability below 0.1, or more than 10 fewer zero-count sites than expected.

**Interpretation of abundance.** The N-mixture abundance is the number of individuals whose territories at least partly overlap the survey area, not true density. For mobile species, this exceeds true density, so the authors describe it as a *relative density* estimate and caution against extrapolating it as density across a range.

## Key Findings

**1. Model fit favoured the zero-inflated negative binomial.**
- Covariate models always fitted better than null models, with AIC values 4 to 93 points lower; most best covariate models were at least 20 points lower.
- According to AIC, the ZINB was the most parsimonious model for all six species. For the White-throated Treecreeper, the ZIP was equally parsimonious; for the Golden Whistler, the NB was equally parsimonious.
- Models with Δi ≤ 2 were treated as equally supported.

**2. Ecological realism reversed the ranking.**
- The Poisson and ZIP variants produced ecologically realistic estimates for five of six species. Both failed for the Scarlet Robin.
- The Poisson model estimated occupancy near 1 for the Scarlet Robin, versus an expected value below 0.50.
- The ZIP estimated detection probability of 0.06 for the Scarlet Robin, below the expected minimum of 0.1. (The Discussion reports this same 0.06 value as an occupancy estimate, so the source is inconsistent on which parameter it refers to.)
- The NB and ZINB variants were realistic for only two species, the White-throated Treecreeper and the Gray Fantail, both expected to occupy most sites.
- For the Rufous Whistler, Mistletoebird, Scarlet Robin and Golden Whistler, the negative binomial variants predicted site abundances of up to about 20 birds per 2 ha and detection probabilities as low as 0.02. The authors judged this implausible, especially during the breeding season when birds hold discrete territories.

**3. The AIC cannot detect ecological implausibility.** The negative binomial accommodates excess zeros by letting mean abundance vary stochastically. In an N-mixture, this allows a combination of very high abundance and very low detection probability, which fits the data statistically but is ecologically unrealistic. AIC selects on statistical fit and cannot discriminate between models that place error in the detection or abundance component.

**4. Results match an independent study.** [[Kery et al. 2005]] compared N-mixture abundance estimates with territory mapping for six bird species. Their negative binomial N-mixture estimated site abundance up to 8.86 times the territory-mapping value. The Poisson N-mixture was close to territory mapping, with a mean ratio of 1.18 (range 0.93–1.45). AIC and goodness-of-fit still chose the negative binomial for five of six species. The present authors argue that the negative binomial was the inappropriate distribution in both studies.

**5. Zero-inflated Poisson is the recommended model.**
- The ZIP models an ecological mechanism: a site is either suitable and occupied, or it is not. This matches the biology of species absent from unsuitable vegetation.
- The ZIP also gave sensible estimates when data were not zero-inflated.
- The authors recommend that the negative binomial N-mixture not be used to predict abundance and detection probability.
- A standard Poisson N-mixture may suffice when a species is present at nearly all sites; the ZIP is more appropriate where absence from more than about 30% of sites is expected.

**6. Limitations and suggested improvements.**
- The Poisson model fits well when the mean abundance of occupied sites is close to zero (around 5), but it misfits when occupied-site means are further from zero (around 10).
- The Scarlet Robin's ZIP estimate may improve if detection is modelled with more covariates (observer, weather, time of year) and a beta-binomial distribution to absorb extra-binomial variation. The authors note that such models need care to avoid overfitting.
- Dependence among individuals (for example, flocking) violates the independence assumption of the N-mixture, and the current forms are then not appropriate.

**7. Practical guidance.** Ecological mechanisms should be identified before choosing an error distribution. Models that represent those mechanisms, such as the ZIP, are less likely to produce misleading parameter estimates. The ZIP also allows ecological correlates of occupancy and abundance to be included.