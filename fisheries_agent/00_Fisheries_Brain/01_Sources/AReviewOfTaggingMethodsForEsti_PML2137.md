---
species: N/A
common_name: N/A
family: N/A
habitat: Freshwater and marine fisheries (reservoirs, rivers, lakes, estuaries, nearshore reefs)
ocean_basin: N/A
location: N/A
tags: [ichthyology, marine-biology, fisheries-science, tagging, population-estimation, mortality]
title: "A review of tagging methods for estimating fish population size and components of mortality"
source_id: "PML2137"
marsh_id: "PML2137"
library: "Marsh Library"
permission: "not public domain"
source_citation: "W. E. Pine, K. H. Pollock, J. E. Hightower, T. J. Kwak, J. A. Rice (2003). A review of tagging methods for estimating fish population size and components of mortality. Fisheries, vol. 28, no. 10 (American Fisheries Society). Marsh Library ID: PML2137."
source_file: "Pine W.E. et al 2003. a review of tagging methods for estimating fish population size and components of mortality.pdf"
text_extraction: "text"
---
# Review of Tagging Methods for Estimating Fish Population Size and Mortality Components

#ichthyology #marine-biology #fisheries-science

## Executive Summary

This review, published in *Fisheries* (vol. 28, no. 10, October 2003), synthesizes [[Capture-Recapture Models]] and [[Tag-Return Models]] for estimating fish population size, total mortality, and the fishing and natural components of mortality. The authors argue that fisheries biologists have been slower than wildlife biologists to adopt these methods, despite their wide applicability, the range of tag types available (from fin clips to [[Telemetry]] tags), and new analysis software. The paper offers five recommended strategies: closed models for short studies, the [[Robust Design]] for longer studies, high-reward tags to estimate reporting rate, combining telemetry with tagging, and pilot and simulation studies to test precision before fieldwork.

## Background & Description

The authors are fisheries and statistical researchers at the North Carolina Cooperative Fish and Wildlife Research Unit, North Carolina State University. The article is intended to help fisheries biologists design tagging studies by summarizing the assumptions and basic models available, together with specialized software (Box 1, Tables 1 and 2).

Two families of methods are distinguished:

- **Capture-recapture (mark-recapture):** fish are recaptured alive on multiple sampling occasions. Closed models assume no births, deaths, emigration, or immigration; open models (e.g., [[Jolly-Seber Model]]) allow these changes.
- **Tag-return:** harvested tagged fish are reported by fishers over several years, so recaptures are dead. These [[Brownie Models]] estimate total mortality and survival.

Key terms include capture probability (*p*), the probability that an individual is captured on a sampling occasion; apparent survival (φ), which combines mortality and emigration; and the instantaneous total mortality rate (Z = F + M), where F is fishing and M is natural mortality.

## Ecological & Environmental Context

The authors frame the methods within fisheries management, where population size, survival, and mortality components guide recovery plans for imperiled species, evaluation of [[Marine Protected Areas]], and sustainable harvest regulation. Examples used include [[Largemouth Bass]] in reservoirs sampled by shoreline electrofishing, [[Gulf of Mexico Sturgeon]], [[Striped Bass]] in Lake Gaston, North Carolina, blacktip sharks in a nursery area, and salmon smolts migrating through the Columbia River.

Environmental factors affect sampling. Catchability varies with water temperature, vegetative cover, weather, and season, so catch-per-unit-effort (CPUE) may not track abundance. Bayley and Austen (2002) reported empirical catchability ranging from 7 to 14% for a single electrofishing pass, indicating that capture probability is typically low in fisheries studies, producing sparse data.

## Key Findings

**Why CPUE is unreliable for abundance:**
- CPUE assumes constant catchability over time, which is unlikely; schooling can keep catches high while populations decline.
- CPUE is adequate only for detecting large changes (the paper cites >50%). Tagging studies are preferred for precise abundance and mortality estimates.

**Study planning (Box 1):**
- Expected capture histories can be simulated by hand or on a spreadsheet before fieldwork. Example: with *p* = 0.1 and N = 1,000 across three closed samples, the eight possible capture histories are computed, with seven of interest after excluding the no-capture case (000).
- Precision improves by increasing capture probability, the number of samples, or both.

**Closed models:**
- Lincoln-Peterson and Schnabel models are simple and need no uniquely marked fish, but assume closure, equal catchability, and no mark loss. Heterogeneity (e.g., by size, sex, or social status) causes strong negative bias in population size.
- [[Program Capture]] fits a suite of eight closed models (M0 to Mth variants), including heterogeneity models (Mh), and is the only specialized program that does so. The authors suggest the Schnabel model (Mb) should be used only if model selection supports it.
- Recommended minimum: five or more sampling periods for closed experiments, especially when heterogeneity models are used.
- Removal studies: White et al. (1982) recommended capture probabilities of at least 0.2 and population sizes of about 200 individuals; four or more samples are recommended. The authors advise using CAPTURE rather than regression for removal estimates.

**Open models:**
- Jolly-Seber models estimate population size at each sampling date, apparent survival, and recruitment. Apparent survival underestimates true survival unless emigration is zero, so a telemetry study can help separate the two.
- Violations include tag loss (leading to underestimated survival and overestimated population size), trap or tagging trauma, and temporary emigration. Zehfuss et al. (1999) found unbiased N from Jolly-Seber with random temporary emigration only when capture probabilities exceed 0.5, which is rarely true in field work.

**Robust design:**
- Combines short closed-population periods (estimating N while allowing heterogeneity and trap response) with open-model intervals (estimating survival and recruitment). The authors strongly recommend it because it handles both heterogeneity and temporary emigration, and is easy to add to existing sampling programs.

**Tag-return and reporting rates:**
- Brownie models require at least three, and preferably five, years of tagging and recovery. Brownie et al. (1985) suggest tagging at least 300 individuals per year for waterfowl.
- Exploitation rate (u) and total mortality partition into fishing and natural components (F and M) only when the tag-reporting rate is known. The authors list high-reward tagging as one method; in Denson et al. (2002), reporting for red drum was approximately 60%. If high-reward tags are not fully reported, the reporting rate is positively biased.
- Henry (2002) used tags worth US $5 to $100 at Rodman Reservoir, Florida, to estimate tournament exploitation for largemouth bass.

**Telemetry:**
- Telemetry provides direct information about timing and location of natural mortality, which tag-return data cannot give, and does not need a reporting rate. Examples include blacktip shark predation (Heupel and Simpfendorfer 2002), predation on smolts by pike and birds (Jepsen et al. 1998, 2000), and seasonal natural mortality of striped bass (Hightower et al. 2001).
- Key transmitter traits are small size, long battery life, adequate detection range, and unique signals. Remote sonic receivers can monitor an area for months on a single lithium battery.

**Combined tagging-telemetry approach:**
- Simulations by Pollock et al. (in press) using 500 conventional tags and 50 transmitters per year showed improved estimates of F and M and of the reporting rate. M estimates are best when F is low; reporting-rate estimates are best when F is high.

**Recommendations and conclusions:**
- Use pilot and simulation studies to test precision and study feasibility before large field programs.
- Evaluate closure in closed studies through preliminary field work, and consider heterogeneity models.
- For open studies, assess temporary emigration, which can cause large bias. Studies longer than one month are more likely to meet open-model assumptions.
- The authors recommend individual marks so that full capture histories are recorded, enabling assessment of heterogeneity and trap response.
- Combining tagging with telemetry is encouraged for mortality estimates and a complete assessment of mortality components.

**Tables:**
- Table 1 lists software: MARK (open, closed, and robust designs), CAPTURE (closed models including heterogeneity), JOLLY, SURVIV, POPAN, and SPAS. Most are free online.
- Table 2 compares models by mark type, source of fish, typical duration, reporting-rate requirement, and software. Closed-model studies generally run under one month, while Brownie and telemetry studies run for a year or more.