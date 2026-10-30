---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Auckland, New Zealand (statistical paper); Phoenix, Arizona, USA (documentary premiere)
tags: [capture-recapture, tag-loss, population-estimation, mark-recapture, fossil-creek]
title: "Tag loss and the Petersen mark-recapture experiment"
source_id: "PML2328"
marsh_id: "PML2328"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. A. F. Seber, R. Felton (1981). Tag loss and the Petersen mark-recapture experiment. Biometrika, 68(1), 211-219. Marsh Library ID: PML2328."
source_file: "Seber G.A.F et al. 1981. Tag loss and the petersen mark recapture experiment.pdf"
text_extraction: "text"
---
# Tag Loss and the Petersen Mark-Recapture Experiment

#ichthyology #marine-biology #population-statistics

## Executive Summary

The document combines two unrelated items. The main content is a statistical paper on how [[Tag Loss]] biases the [[Petersen Estimate]] in a [[Capture-Recapture Method|two-sample capture-mark-recapture]] experiment, for both single and [[Double Tagging]]. It derives bias corrections, introduces approximately unbiased estimators and variance formulas, and concludes that [[Distinguishable Tags]] offer a modest advantage over [[Indistinguishable Tags]]. No fish or aquatic species are studied. The second item is a December 2006 email announcing the world premiere of the documentary *A River Reborn: The Restoration of Fossil Creek*, which covers a stream-flow restoration settlement and has no quantitative content.

## Background & Description

**Statistical paper (Seber and Felton, *Biometrika*, 1981, 68(2): 211-19).** The authors are from the Department of Mathematics, University of Auckland. The [[Petersen Experiment]] captures and marks a sample (sample 1) from a closed population of size N, releases it, then takes a second sample (sample 2) and counts marked individuals (m2). The authors list the standard assumptions:

- the population is closed;
- all individuals have equal capture probability in sample 1;
- marking does not affect catchability;
- sample 2 is a simple random sample;
- tags are not lost between samples;
- all marks are reported on recovery.

Under these assumptions m2 follows a [[Hypergeometric Distribution]]. The paper treats three sampling models: the hypergeometric model, the [[Darroch Model]] (multinomial, random sample sizes), and an intermediate binomial model. In practice the three give essentially the same results, and the authors use the binomial model for convenience.

**Documentary email.** The message, sent by Paul Marsh to a list of Center for Biological Diversity contacts on 19 December 2006, promotes a premiere event in Phoenix. The film tells how, after 100 years of stream diversion, [[Arizona Public Service]] (APS) and environmental advocates, including the [[Center For Biological Diversity]], reached a settlement to restore [[Fossil Creek]], described as a national treasure.

## Ecological & Environmental Context

The paper's concern is methodological rather than ecological. Its motivating setting is animal population monitoring, and the authors cite wildlife and fisheries applications:

- a pup-tagging study of the Cape fur seal (*Arctocephalus pusillus*) at Seal Island, False Bay, South Africa (Best and Rand, 1975);
- a tuna tag-shedding study (Cormack and colleagues, cited as Chapman et al., 1966);
- ear-tag loss in red foxes (Hubert et al., 1976);
- commercial fishing, where distinguishing tags may not be practicable.

The email describes restoration of a flowing stream after a century of diversion. It gives no data on water quality, species or flows, so the ecological context is limited to the restoration narrative.

## Key Findings

### Statistical Results

- **Standard estimator:** The Petersen estimate N̂ = n1·n2/m2, rounded, is the maximum likelihood estimate. The [[Robson And Regier Estimator]], N̂* = (n1+1)(n2+1)/(m2+1) − 1, is unbiased when n1 + n2 > N and approximately unbiased otherwise.
- **Variance:** A variance estimator for N̂* is given, with a large-sample approximation var(N̂) ≈ N²(N − n1)(N − n2)/(n1·n2·N − ...), reducing to about N³/(n1·n2) for moderate capture probabilities.
- **Effect of single-tag loss:** If the tag retention probability is θ0, the Petersen estimator is biased. The paper's example uses a 20% tag loss rate (θ0 = 0.8). The authors state that the bias can be ignored in confidence intervals when it is less than 10% of the standard error.
- **Double tagging:** The bias depends on θ00, the probability of losing both tags. If both tags are lost independently, the bias is small. The corrected estimate ignores animals that have lost both tags.

### Corrections Under Double Tagging

- **Distinguishable tags (A and B):** Assuming independent tag loss, the authors derive maximum likelihood estimates of the retention probabilities. They propose a corrected estimator N̂_B and an approximately unbiased variance estimate. The earlier formula for this estimator in Seber (1973) is shown to be incorrect.
- **Indistinguishable tags:** The estimator N̂_S = 2n1·m2 / (m_s + 2m_as)... is shown to be a good fit when retention rates are equal. Its bias is shown to be of order (θ_A − θ_B)², so it is valid when the two tag types have similar loss rates. The authors state that the correction is still useful when the tags are identical.

### Robustness and Dependence

- Tag loss dependence between the two tags is quantified through the correlation between indicator variables for retention. The estimators are "moderately robust": a fair degree of correlation can be tolerated without appreciable bias, provided retention rates are reasonably high.
- The bias of the indistinguishable-tag estimator in the presence of dependence is shown to be negligible for capture probabilities below 0.9 when N̂ is reasonably large.

### Recommendations

- Use distinguishable tags (N̂_B) where possible, since indistinguishable tags give little efficiency gain.
- If distinguishable tags are impracticable, as in commercial fishing, use the indistinguishable-tag estimator.
- Attach a third permanent tag to a small subsample. This allows the probability of tag loss to be estimated.

### Documentary Premiere Details

- **Event:** World premiere of *A River Reborn: The Restoration of Fossil Creek* on Sunday, 14 January 2007, at the Orpheum Theater, 203 W. Adams St., Phoenix, Arizona.
- **Screenings:** 4 p.m. and 7 p.m., with a reception at 6 p.m.
- **Tickets:** $10 for the general public; free for Center for Biological Diversity members (identify as a member when calling). Box office: 602-262-7272.
- **Production:** Produced by Emmy-winning producer Paul Bockhorst for Northern Arizona University (NAU) and the Museum of Northern Arizona, narrated by Ted Danson.
- **Broadcast:** Airs on KAET Arizona Public Television at 9 p.m. on Wednesday, 17 January 2007. Distribution to public television stations by satellite through the National Educational Telecommunications Association (NETA) is planned for February 2007.
- **Speakers:** Bill Post (APS chairman) and Robin Silver (Center board chair).
- **Contacts:** Dr. Stefan Sommer (NAU, 928-523-4463) and Michelle Harrington (Rivers Program Director, Center for Biological Diversity, 602-628-9909).