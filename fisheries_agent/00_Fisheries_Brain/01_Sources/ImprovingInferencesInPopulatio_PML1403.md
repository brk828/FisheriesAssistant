---
species:
  - Deinacrida mahoenui
  - Bos frontalis
  - Eurycea wilderae
common_name:
  - Mahoenui giant weta
  - Gaur
  - Blue-ridge salamander
family: N/A
habitat: Reserve gorse scrub and reverting farmland (weta); tropical forest and grassy clearings (gaur); stream-side and terrestrial forest habitats (salamander)
ocean_basin: N/A
location: New Zealand (North Island, King Country); Peninsular Malaysia (Taman Negara National Park); Great Smoky Mountains National Park, eastern United States
tags: [ecology, statistics, rare-species, detection-probability, occupancy, population-monitoring]
title: "Improving inferences in population studies of rare species that are detected imperfectly"
source_id: "PML1403"
marsh_id: "PML1403"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. I. MacKenzie, J. D. Nichols, N. Sutton, K. Kawanishi, L. L. Bailey (2005). Improving inferences in population studies of rare species that are detected imperfectly. Ecology, vol. 86, no. 5. Marsh Library ID: PML1403."
source_file: "Mackenzie D.I. et al. 2005. improving inferences in population studies of rare species that are detected imperfectly.pdf"
text_extraction: "text"
---
# Improving Inferences in Population Studies of Rare Species That Are Detected Imperfectly

#ichthyology #marine-biology #population-ecology #occupancy-modeling

## Executive Summary

This methodological paper, a [[Special Feature]] in *Ecology* (Vol. 86, No. 5, May 2005), argues that counts of rare animal species are unreliable indicators of population size because detection is imperfect and sample sizes are small. The authors recommend two approaches: (1) borrowing information about [[Detection Probability]] from other times, places, or species; and (2) using alternative state variables, chiefly [[Species Richness]] and [[Occupancy]]. Both are illustrated with case studies on Mahoenui giant weta, Malaysian gaur, and Blue-ridge salamanders. The document is primarily a statistical and ecological review rather than a fish study; no fish taxa are central to its findings.

## Background & Description

The paper begins with two sources of variation in count data. The first is spatial sampling: inferences about large areas require probabilistic selection of smaller sample units. The second is detectability: observed counts (C) are a product of true abundance (N) and detection probability (p), expressed as E(C) = pN, so estimating abundance requires estimating p (N̂ = C/p̂).

Detection probability also biases demographic estimates. Age ratios used to infer reproductive rate become confounded by relative detectability, and survival and movement estimates from marked animals are biased if time- and location-specific detection is ignored.

Rarity compounds these problems. Rare species occur at low densities or occupy few sampling units, and low detection probabilities inflate variance (var(N̂) = var(C)/p̂²). Methods such as distance sampling, removal sampling and capture-recapture generally need sample sizes that rare species cannot supply. The authors also note practical constraints: individuals often cannot be identified, and marking may harm protected animals.

## Ecological & Environmental Context

The paper frames rarity as either low density across a broad range or local abundance confined to a small fraction of sampling units (Gaston 1994). Two conservation contexts are emphasized:

- **Metapopulation dynamics**, where local extinction and colonization are the processes of interest.
- **Management indicators**, where species such as the Blue-ridge salamander were proposed as indicators for National Forests in North Carolina but later removed from lists because their count statistics were highly variable.

The Mahoenui giant weta case shows why abundance monitoring fails: weta occur at low densities, cannot be individually identified, and live in brittle dead gorse foliage that would be damaged by capture. The gaur case reflects a species declining across [[Peninsular Malaysia]] and listed as vulnerable by the IUCN and on CITES Appendix I. The salamander case involves forest habitats in [[Great Smoky Mountains National Park]], where the species uses both aquatic and terrestrial habitats.

## Key Findings

**Methodological principles**

- Simple counts are generally poor indices of population size for rare species. Detection probabilities should be estimated and incorporated into inference.
- **Borrowing information** can be done by aggregating data over times, places or species (e.g., [[Capture-Recapture Modeling]]), or by combining different data types within a shared framework (e.g., [[Hierarchical Modeling]]). Dixon et al. (2005) used this for wasp capture efficiency by the pitcher plant *Darlingtonia californica*. Franklin et al. (2004) used a meta-analysis of California Spotted Owl populations, and Nichols et al. (2000) used double-observer models for avian point counts.
- **Alternative state variables** can provide robust inference with less sampling effort than abundance. These are species richness and occupancy.

**Species richness**

- Raw richness counts are unreliable because the observed fraction of the species pool varies with habitat and composition.
- Richness can be estimated using temporal replication (capture-recapture models for species), spatial replication, combined designs, or detection frequencies from a single sample (jackknife estimators).
- Dynamics can be estimated through local extinction, colonization and turnover, which were applied to forest bird communities by Boulinier et al. (1998, 2001).

**Occupancy**

- Occupancy (the proportion of sites where a species is present) can be a more appropriate state variable when the goal is range or metapopulation analysis.
- Naive occupancy estimates are biased by detection differences. Moilanen (2002) found that detectability was the largest source of bias in metapopulation incidence functions.
- MacKenzie et al. (2002) developed a single-season model with detection histories. Royle and Nichols (2003) extended this to account for abundance-related heterogeneity in detection.
- MacKenzie et al. (2003) extended the model to multiple seasons, estimating colonization (γ) and local extinction (ε) probabilities while accounting for imperfect detection.

**Case study 1: Mahoenui giant weta (*Deinacrida mahoenui*)**

- 72 circular plots (3 m radius) were surveyed between 23 and 27 March 2004, each three to five times, by three surveyors.
- The weta was detected at 35 of 72 plots, giving a naive occupancy of 0.49.
- Model-averaged estimates were about 30% higher than the naive estimate. Surveyor differences in detection were evident. The study was a pilot, and the plots were confined to more accessible reserve areas.

**Case study 2: Malaysian gaur (*Bos frontalis*)**

- Gaur were surveyed in three study areas in Taman Negara using monthly grid-cell sampling (nine 5 × 5 km cells per area) for five months, sequentially over 1999–2001.
- Naive occupancy was 0.67, 0.55 and 0.11 for areas 1–3.
- Single-area estimates were 0.86 and 0.60 for areas 1 and 2. Area 3 had only one detection, so information was shared across areas through detection probabilities.
- The model-averaged estimates for areas 1 and 2 were similar to the separate analyses, and the area 3 estimate was judged more realistic.

**Case study 3: Blue-ridge salamander (*Eurycea wilderae*)**

- Data came from 39 sites in the Roaring Fork Watershed, sampled over four years (1998–2001).
- Detection probability varied strongly by year. Models assuming constant detection received less than 3% of total AIC weight.
- Model-averaged 1998 occupancy was 0.97, colonization probability was 0.16 and local extinction probability was 0.29.
- Projected occupancy was 0.70, 0.59 and 0.54 for 1999–2001, indicating a downward trend consistent with rainfall records.
- Estimated vital rates were lower than naive estimates, suggesting that some apparent turnover reflected nondetection.

**Conclusions**

The authors argue that rare species are the ones most needing reliable inference and the hardest to study. They recommend borrowing information and using occupancy and related state variables, rather than abandoning inference or relying on raw counts.