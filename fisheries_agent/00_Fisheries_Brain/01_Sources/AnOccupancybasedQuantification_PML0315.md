---
species:
  - Catostomus latipinnis
  - Catostomus discobolus
  - Gila robusta
common_name:
  - Flannelmouth Sucker
  - Bluehead Sucker
  - Roundtail Chub
family:
  - Catostomidae
  - Cyprinidae
habitat: Freshwater rivers and tributaries (flow-regulated streams and mainstem systems)
ocean_basin: N/A (freshwater)
location: Utah, USA; Colorado River Basin
tags:
  - ichthyology
  - marine-biology
  - desert-fishes
  - occupancy-modeling
  - conservation-planning
  - colorado-river-basin
title: "An occupancy-based quantification of the highly imperiled status of desert fishes of the southwestern United States"
source_id: "PML0315"
marsh_id: "PML0315"
library: "Marsh Library"
permission: "not public domain"
source_citation: "P. Budy, M. M. Conner, N. L. Salant, W. V. Macfadden (2015). An occupancy-based quantification of the highly imperiled status of desert fishes of the southwestern United States. Conservation Biology, vol. 00, no. 0, pp. 1-11, DOI 10.1111/cobi.12513. Marsh Library ID: PML0315."
source_file: "Budy P. et al. 2015. An occupancy based qualification of the highly imperiled status of desert fishes of the southwestern united states.pdf"
text_extraction: "text"
---
# Occupancy-Based Quantification of the Highly Imperiled Status of Desert Fishes of the Southwestern United States

#ichthyology #marine-biology #catostomidae #cyprinidae

## Executive Summary

This study uses [[Occupancy Modeling]] to quantify the decline of three endemic [[Desert Fishes]] of the [[Colorado River Basin]] in Utah: [[Flannelmouth Sucker]], [[Bluehead Sucker]], and [[Roundtail Chub]]. The three species are managed together as a "three species" complex, though their status and response to stressors are poorly documented. The authors built [[Robust Design Occupancy Model]] analyses on presence-absence data from two periods: a historic series (1889–2011, 52 river sites) and a contemporary series (2001–2011, 140 sites on 32 rivers).

Occupancy declined sharply during the historic period. By 2011, about 47% of original sites remained occupied by the two suckers and 15% by the chub. Hydrologic variables, especially [[Change In Flood Frequency]] and [[Peak Discharge]], were the strongest correlates of [[Local Extinction]] and [[Local Colonization]]. The authors conclude that the decline is strongly linked to [[Water Development]], that the three species are all highly imperiled, and that the chub may need separate management from the suckers.

## Background & Description

The three species are native, non-charismatic fishes endemic to the Colorado River Basin. Historically they used diverse habitats and moved among connected tributary and mainstem systems. Managers have treated them as an ecological complex because of assumed similarities in habitat requirements, life-history traits, and ecological niches. Recent work (Laub & Budy 2015) questions this assumption.

The authors describe [[Desert Fishes]] of the southwestern United States as among the most imperiled vertebrates worldwide. Their low economic value and conflicts with human water use make them vulnerable. Stressors documented in the basin include:

- Complete dewatering and barriers to connectivity.
- Reduced baseflows from over-allocation for agricultural or urban use, producing lethal temperatures and low dissolved oxygen.
- Loss of high-flow events, which alters riparian vegetation and channel morphology.
- Reduced seasonal variability in discharge and temperature, which affects migration cues.
- Invasion by [[Non-Native Fish Invasion]].

The study's goals were to (1) identify occupancy trends from local colonization and extinction probabilities, (2) relate these to hydrologic and biogeographic covariates, and (3) test whether the three species respond similarly enough to be managed as one complex.

## Ecological & Environmental Context

**Study area and sampling.** Data came from Utah rivers, compiled from targeted and non-targeted efforts. No systematic sampling program existed before 2004. Sites were defined as reaches with minimal sub-population mixing, separated by barriers or by 10–30 km on larger rivers and 5–20 km on smaller ones. Historic data were often coarse, so a site sometimes represented an entire river. Contemporary data came from [[Utah Division Of Wildlife Resources]] managers, supplemented by Bezzerides & Bestgen (2002). Sampling intensity was 2–65% of sites per historic interval and 3–44% of sites per contemporary year.

**Covariates.** Twelve site covariates were considered: six hydrologic (for example, mean annual discharge, peak annual discharge, change in flood frequency, years regulated, water diversion, and the presence of non-native fish or riparian invasion by tamarisk) and six biogeographic (for example, human growth rate, corridor conservation, and riparian invasion). Several hydrologic covariates were strongly intercorrelated (r = 0.53–0.99), so correlated variables were never included in the same model. Exotic fish were present at 89% of sampled sites, so that variable was not used in models, and the tamarisk measure was too coarse to be used.

**Modeling approach.** Models were fit in [[Program MARK]] using the robust design occupancy parameterization. Model selection used [[Akaike Information Criterion]] corrected for small sample size (AICc). Because the true effective sample size is debated, the authors used the most conservative estimate: the number of unique sites times the number of species sampled (123 for the historic set and 373 for the contemporary set). Model averaging accounted for selection uncertainty.

## Key Findings

### Historic Period (1889–2011)

- **Occupancy declined sharply.** The two suckers lost 48% of occupied sites, leaving 47% (95% CI 34–61%) occupied at the end of the period. The chub lost 83%, leaving 15% (95% CI 6–33%).
- **Extinction rose and colonization fell.** The top models included a positive log-linear time trend in local extinction probability and a negative trend in local colonization probability.
- **Flood frequency was the key covariate.** Change in flood frequency, which averaged about −39% across sites, had a significant negative relationship with local extinction. Greater reductions in flood frequency were associated with higher extinction probability.
- **Detection was relatively high.** In 1963, detection probability was 0.69 (95% CI 0.50–0.84) for the suckers and 0.61 (95% CI 0.41–0.78) for the chub. Detection exceeded 0.87 for both groups from 1984 to 1999.
- **Model support.** The top two models carried 86% of the model weight. The best detection model (quadratic time trend) carried 71%.
- **Grouping.** Models treating the two suckers as one group and the chub as another outperformed models with three separate groups and models with all three species combined.

### Contemporary Period (2001–2011)

- **Peak discharge was the key covariate.** As peak annual discharge increased, local extinction probability decreased and local colonization probability increased. Peak discharge ranged from 169 to 28,149 cfs across sites.
- **Stabilization, not recovery.** Decline appeared to slow or level off, but the authors caution that the historic and contemporary data are not directly comparable. Local extirpations at some sites and increased sampling intensity may bias estimates. Occupancy had already dropped to very low levels (17–51% of sites occupied at the start of the contemporary period).
- **Current occupancy.** By the end of the period, about 51% (95% CI 25–76%) of sites were occupied by Flannelmouth Sucker, 65% (95% CI 32–88%) by Bluehead Sucker, and about 13% (95% CI 5–33%) by Roundtail Chub.
- **Chub dynamics.** For the chub, local extinction still far exceeded local colonization. For the two suckers, colonization slightly exceeded extinction.
- **Detection.** The lowest estimated detection probability was 0.74 (95% CI 0.65–0.83) for the suckers and 0.53 (95% CI 0.33–0.72) for the chub.
- **Grouping.** The contemporary top model used three separate species groups, but the two-group and three-group models were competitive (within 0.4 AICc units). Both were much better than a model combining all three species.
- **Human growth.** The response to human growth rate was erratic and showed no clear or significant pattern across species.

### Management Implications

- **Suckers as one unit, chub separate.** The authors conclude it may be biologically appropriate to manage the two suckers as a complex, but the chub may need separate management. A hybrid approach could combine ecosystem-based objectives (for example, natural flow regimes) with species-specific targets and site-level actions such as non-native species control or habitat restoration.
- **Maintain flows.** Maintaining instream flows and some magnitude of spring peak discharge should be immediate priorities. The spring flood cues migration, creates and maintains complex habitat, and reduces the effects of non-native fishes.
- **Connectivity.** Because desert riverine organisms can disperse only longitudinally and drought or over-allocation can dewater river sections, enhancing [[Connectivity]] could raise colonization rates.
- **Future monitoring.** A more robust sampling design would sample fewer sites more often with repeat visits. Simulation could identify the optimal design.
- **Legal thresholds.** Each species may need different triggers for status changes, such as criteria under the [[Endangered Species Act]].
- **Broader use.** The authors suggest occupancy modeling of historic presence-absence records can help assess long-term population change for other poorly known, likely imperiled species, where data are sparse and conservation status is uncertain.