---
species: "Deltistes luxatus"
common_name: "Lost River sucker"
family: "Catostomidae"
habitat: "Freshwater lake and tributary spawning areas; shoreline upwelling springs and riverine spawning reaches"
ocean_basin: "N/A"
location: "Upper Klamath Lake, Oregon; Upper Klamath River Basin (Oregon and California)"
tags: [capture-recapture, PIT-tags, survival-estimation, endangered-species, freshwater-fisheries, remote-detection, Klamath-Basin]
title: "Improving Inferences from Fisheries Capture-Recapture Studies through Remote Detection of PIT Tags"
source_id: "PML1050"
marsh_id: "PML1050"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. A. Hewitt, E. C. Janney, B. S. Hayes, R. S. Shively (2010). Improving Inferences from Fisheries Capture-Recapture Studies through Remote Detection of PIT Tags. Fisheries 35(5), American Fisheries Society. Marsh Library ID: PML1050."
source_file: "Hewitt D.A. et al. 2010. Improving inferences from fisheries capture recapture studies through remote detection of PIT tags.pdf"
text_extraction: "text"
---
# Improving Inferences from Fisheries Capture-Recapture Studies through Remote Detection of PIT Tags

#ichthyology #marine-biology #catostomidae

## Executive Summary

This feature article from the May 2010 issue of *Fisheries* (the journal of the [[American Fisheries Society]]) reports a case study on [[Lost River Sucker]] (*Deltistes luxatus*), an endangered catostomid in [[Upper Klamath Lake]], Oregon. Traditional [[Trammel Nets]] sampling yielded too few recaptures of [[PIT Tags]]-marked adults for reliable [[Survival Estimation]] using [[Cormack-Jolly-Seber Models]]. From 2005 onward, [[Remote Detection Systems]] (antennas at known spawning springs) raised [[Encounter Probability]] from roughly 2–15% to over 90% in the key years, markedly improving survival precision. The authors argue that remote PIT detection makes [[Capture-Recapture]] studies practical in freshwater and other systems where they were previously considered impracticable.

## Background & Description

**Study species.** Lost River suckers are long-lived catostomids endemic to the Upper Klamath River Basin. Individuals have been aged to over 40 years, and the largest adult females reach about 800 mm fork length. The species was listed under the [[Endangered Species Act]] in 1988 because of range contraction, declining abundance, and lack of evidence of recent recruitment to adult populations. Fishing for suckers was banned in 1987. Other threats, including [[Habitat Alteration]] and [[Nonnative Species]], were identified, but their relative influence is uncertain (NRC 2004).

**Study system.** The most intensively studied remaining population occurs in [[Upper Klamath Lake]], the largest lake in Oregon (280 km²) but relatively shallow (average depth about 2 m). Two spawning subpopulations coexist there: one migrates up tributaries, mainly the lower [[Williamson River]] and [[Sprague River]], and the other spawns at upwelling springs along the eastern shore below Modoc Rim. Most spawning occurs in March and April. The spring-spawning subpopulation was the focus of the analysis, and only fish tagged in 1999 and later were included. Related [[Shortnose Sucker]] (*Chasmistes brevirostris*) co-occur in the lake.

**Context of the issue.** The same issue of *Fisheries* covers the AFS certification program, the Fenske Fellowship, a New York/New Jersey Estuary habitat vision, and a [[Habitat Restoration Tracking]] study, among other items. These are not analyzed here.

## Ecological & Environmental Context

- **Water quality.** Upper Klamath Lake has been eutrophic since the mid-1800s, but human activities (marsh and wetland drainage, timber harvest, and agricultural water control) have made it hypereutrophic. The result is massive blooms dominated by the [[Cyanobacteria]] *Aphanizomenon flos-aquae* (Lindenberg et al. 2009).
- **Mortality.** Summer and fall phytoplankton blooms are associated with direct and indirect adult sucker mortality and large [[Fish Die-Offs]] (Perkins et al. 2000). [[Janney et al. 2008]] found annual survival was reduced in years with conspicuous die-offs, but was also low in years without them.
- **Sampling mortality.** None of the fish died from handling or net-pen retention, and released fish appeared vigorous, so short-term sampling mortality was judged negligible.
- **Population movement.** Very few adults leave Upper Klamath Lake (Banish et al. 2009), so apparent survival closely approximates true survival.

## Key Findings

### Methods and Study Design

- **Trammel net captures.** Between 1999 and 2007, 8,451 adult Lost River suckers were captured and PIT-tagged at spring spawning areas (the abstract reports "over 8,400"). Nets (30 m × 1.8 m) were set twice weekly at five known spring spawning areas, typically under 500 m² each.
- **Tag types.** Fish tagged before 2005 received 12 or 14 mm 125.0 kHz tags; fish tagged from 2005 on received 12 mm 134.2 kHz tags. The 134.2 kHz tags read at about 15–20 cm from antennas, versus about 5 cm for 125.0 kHz tags.
- **Remote antennas.** A single flat-plate antenna was deployed opportunistically at Cinder Flat spring in 2005 (about 135 hours of sampling, 21 April to 6 May). From 2006, two or three antennas per site were deployed for the entire season at four springs (Cinder Flat, Ouxy, Silver Building, and Sucker), each connected to its own Biomark reader.
- **Models.** Two [[Cormack-Jolly-Seber Models]] sets were compared: one with physical recaptures only, and one with physical recaptures plus remote detections. Models were fit in [[Program MARK]] via RMark in R, ranked with [[Quasi-Akaike Information Criterion]] (QAICc), and model-averaged where appropriate.
- **Assumptions.** PIT tag loss was under 1% over three or more years (double-tagging with Floy and PIT tags). Test-tag scanning checked reader performance. Heterogeneity was addressed with goodness-of-fit testing and a [[Variance Inflation Factor]] (ĉ = 1.17 for the physical-only set; ĉ = 1.35 for the full set).

### Results: Physical Recaptures Only

- Only 2,005 of the 8,451 tagged fish (about 24%) were recaptured in trammel nets through 2008. Annual trammel recaptures never exceeded 500 fish.
- Encounter probabilities never exceeded 0.2. Male encounter probabilities were more than double female values, and female values never exceeded 0.05.
- The top model [φ(sex+time), p(sex+time)] had 0.935 model probability. Survival estimates were imprecise, and the point estimates for both sexes in 2000 and 2001 sat on the boundary of 1.0, indicating inadequate information.
- The authors conclude that limited recaptures (the "[[Big Law of Capture-Recapture]]") prevented robust inference about survival.

### Results: Including Remote Detections

- Remote antennas re-encountered **6,401** tagged fish (about 76%) in 2005–2008.
- In 2005, a single antenna detected 157 previously tagged fish, 125 of which had never been recaptured in nets. Five-site trammel sampling that year recaptured 500 fish.
- In 2006, the first full year, **4,787** fish were detected by antennas versus **182** by trammel nets. Of the detected fish, 3,618 had never been re-encountered by either method.
- Encounter probabilities in 2006 and 2007 rose from 2–15% to over 90%. Fish with 134.2 kHz tags were 98% or greater, and fish with 125.0 kHz tags ranged from 91% to 96%.
- The top model [φ(sex+time), p(sex*time+tagtype*time)] had a model probability of 0.680. Full structure on survival was strongly supported (evidence ratio 7.0 for model 1 vs. 3).
- Model-averaged survival estimates had coefficients of variation never above 4%. Survival in the most recent years was essentially known.
- Female survival was higher than male survival in every year. Between 2002 and 2006, female survival ranged from 85% to 94% and male survival from 79% to 92%. This contradicted the authors' expectation based on reproductive investment.
- Survival estimates for the most recent years were underestimated by more than 7% using physical recaptures alone.

### Costs and Practical Implications

- Total equipment cost for full remote antenna implementation at the study sites in 2006 was about **$54,000 USD**. Maintenance and supplementary costs in later years were typically under **$1,000** per year.
- Systems can be built incrementally by adding antennas and readers as funding allows. Some equipment can be built in-house at lower cost than commercial products.
- Once encounter probabilities rise, fewer fish need to be tagged and released each year, which may offset field costs.
- Limitations include damage from high flows or debris, and the need for antenna arrays to span wide channels (up to 50 m or more).

### Limitations and Future Directions

- **Heterogeneity.** Remote detection increased heterogeneity in encounter probabilities, and goodness-of-fit tests became very sensitive. The authors note that ĉ values above about 3.0 are suspicious.
- **Unmarked fish.** Remote detection only sees the marked fraction of the population, so population size, recruitment, and growth rate cannot be estimated from it alone. Individual covariates (length, weight, condition) still require capture.
- **Broader applications.** The authors propose remote detection for rare or elusive fish in small streams (combined with portable wands), for constriction points in large rivers (such as Columbia River Basin dam bypasses), and for commercial fisheries bottlenecks. Examples include southern rock lobster in Australia (Burch et al. 2009; Frusher et al. 2009) and Bristol Bay crab offloading.
- **Integrated models.** Tag returns and remote encounters can be combined with telemetry and fishery-dependent data through joint-likelihood approaches (e.g., [[Integrated Modeling]]).

### Main Conclusion

Remote PIT detection substantially improved encounter probabilities, survival precision, and the biological inferences available for endangered Lost River suckers. The authors argue that the approach is a practical and cost-effective route for freshwater fisheries to adopt modern [[Capture-Recapture]] methods that have been used mainly in marine and coastal fisheries.