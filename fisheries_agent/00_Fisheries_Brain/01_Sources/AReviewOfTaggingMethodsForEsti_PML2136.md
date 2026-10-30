---
species:
  - Micropterus salmoides
  - Acipenser oxyrinchus desotoi
  - Sciaenops ocellatus
  - Salmo salar
  - Salmo trutta
  - Carcharhinus limbatus
  - Salvelinus namaycush
  - Oncorhynchus mykiss
  - Catostomus latipinnis
  - Ptychocheilus lucius
common_name:
  - Largemouth Bass
  - Gulf of Mexico Sturgeon
  - Red Drum
  - Atlantic Salmon
  - Brown Trout
  - Blacktip Shark
  - Lake Trout
  - Rainbow Trout
  - Flannelmouth Sucker
  - Colorado Squawfish
family: N/A
habitat: Freshwater reservoirs, rivers, streams, lakes, and estuaries; also marine and coastal fisheries
ocean_basin: N/A
location: North America (North Carolina, Florida, Lake Michigan, Colorado River system, Grand Canyon, Gulf of Mexico); Europe (Denmark, Scandinavian rivers); Bahamas and Philippines (cited examples)
tags:
  - ichthyology
  - marine-biology
  - fisheries-science
  - capture-recapture
  - tagging
  - population-estimation
  - mortality
  - telemetry
title: "A review of tagging methods for estimating fish population size and components of mortality"
source_id: "PML2136"
marsh_id: "PML2136"
library: "Marsh Library"
permission: "not public domain"
source_citation: "W. E. Pine, K. H. Pollock, J. E. Hightower, Kwak, Rice (2003). A review of tagging methods for estimating fish population size and components of mortality. Fisheries (American Fisheries Society) 28(10):10-23. Marsh Library ID: PML2136."
source_file: "Pine W.E et al. 2003. A review of tagging methods for estimating fish population size and components of mortality.pdf"
text_extraction: "text"
---
# Review of Tagging Methods for Estimating Fish Population Size and Components of Mortality

#ichthyology #marine-biology #fisheries-science

## Executive Summary

This review, published in *Fisheries* (October 2003, vol. 28, no. 10) by William E. [[Pine]], Kenneth H. [[Pollock]], Joseph E. [[Hightower]], Thomas J. [[Kwak]], and John M. [[Rice]], surveys tagging-based models for estimating fish population size, total mortality, and the components of mortality (fishing and natural). The authors argue that capture-recapture and related tagging models, though long established in wildlife biology and statistics, are underused by fisheries biologists. The review summarizes closed and open population models, tag-return (Brownie) models, telemetry approaches, and combined methods, and it stresses pilot and simulation studies before field work. It also offers a practical framework: models are matched to study duration, mark type, and the required precision of estimates.

## Background & Description

Tagging studies use marks such as [[Fin Clip]]s, [[Passive Integrated Transponder Tag]]s (PIT), and external tags, with returns from harvest, recaptures, or [[Telemetry]] relocations. The review aims to help fisheries biologists design tagging studies by outlining the assumptions and basic models behind each approach and the [[Specialized Software]] available for them (Box 1; Tables 1 and 2).

The authors contrast tagging with [[Catch-Per-Unit-Effort]] (CPUE), a common relative abundance index. CPUE assumes constant catchability over time, which is unlikely in practice. Catch rates can also remain high while populations decline, for example through schooling behavior. CPUE is considered adequate for detecting large changes (e.g., >50%) in abundance. Tagging is the better approach when precise population size, trends, or mortality components are needed.

Table 1 lists software packages for analyzing tagging data, including [[MARK]] (comprehensive capture-recapture analysis), [[CAPTURE]] (closed models with heterogeneity testing), [[JOLLY]] and [[POPAN]] (open models), and [[SPAS]] (two-sample capture-recapture). Table 2 summarizes each model's mark type, fish source, typical duration, reporting-rate requirement, key parameters, and software.

## Ecological & Environmental Context

Capture probability (p) is the central parameter. Fisheries sampling is typically inefficient, so capture probabilities are often low, producing sparse data. [[Bayley and Austen]] (2002) documented wide variation in electrofishing catchability across species, fish size, and environmental conditions. In their examples, largemouth bass are sampled with shoreline electrofishing in reservoirs, and not every fish is collected due to gear avoidance and structural obstacles.

Heterogeneity in capture probability, caused by size, sex, behavior, or social status, is likely in almost all fisheries sampling. It can produce strong negative bias in closed-population estimates. Trap response (a change in capture behavior after a first capture) and temporary emigration also bias estimates. Fish that are captured may also suffer tagging-related mortality, causing initial survival declines. Nonlethal sampling is favored because sampled fish should be captured again in future samples.

Natural mortality, fishing mortality, and movement all change the population between samples, which violates closure. [[Open Population Models]] allow for these changes, and [[Closed Population Models]] require closure within short periods.

## Key Findings

**Pre-study simulation.** The authors recommend simple simulations before field work. In a worked example, with three samples, p = 0.10, and N = 1,000, there are 2³ = 8 possible capture histories; excluding the no-capture history (000) leaves seven of interest (Box 1, Table 1). Expected frequencies can be generated by hand, in a spreadsheet, or in MARK or CAPTURE to evaluate precision and plan sampling effort. Such simulations can save time and money.

**Closed models.** Lincoln-Peterson and [[Schnabel Model]]s assume the population is closed to additions and losses, capture probability is equal among animals in each sample, and marks are not lost or overlooked. Both models are simple and widely used, but their assumptions are often violated. The Schnabel model extends Lincoln-Peterson to more than two samples. The [[Removal Method]] is analogous to model M(b) in CAPTURE. For closed models, the authors recommend at least four or more samples, especially when heterogeneity models are to be used. CAPTURE model selection is recommended over the Schnabel model when heterogeneity is present.

**Open models.** The [[Jolly-Seber Model]] (Jolly 1965; Seber 1965) estimates survival, recruitment, and population change, but needs many parameters and performs poorly with sparse data. Its assumptions include equal capture probability and survival among animals and the immediate release of captured fish. Apparent survival estimates are not highly biased by heterogeneity. Temporary emigration, if present, biases estimates, and models such as the [[Robust Design]] can account for it.

**Robust design.** Pollock (1982) proposed a sampling design combining short-term closed samples, which estimate abundance, with open intervals, which estimate survival and recruitment. The authors consider it broadly applicable to fisheries, and it is easily incorporated into many standard sampling programs. An example is four primary periods, each with three weekly secondary samples.

**Auxiliary information and model selection.** Capture probabilities can be estimated empirically (e.g., from radio-tagged fish) or predicted from gear, species, habitat, and environment. Individual covariates such as length can reduce bias. The authors recommend comparing several models using [[Akaike's Information Criterion]] in MARK, with biological knowledge used to select the most parsimonious model.

**Applications to imperiled and sturgeon populations.** Douglas and Marsh (1998) used Jolly-Seber and Cormack-Jolly-Seber models for rare catostomids in the Little Colorado River over four years. Fabrizio et al. (1997) estimated survival of a recovering Lake Trout population in Lake Michigan and found similar estimates from Jolly-Seber and catch-curve methods. Jolly-Seber models were also used for Gulf of Mexico Sturgeon (Chapman et al. 1997; Zehfuss et al. 1999; Pine et al. 2001).

**Tag-return (Brownie) models.** Brownie et al. (1985) models are the standard method for analyzing multi-year tag-return data. Assumptions include representative sampling, no tag loss, no tagging effects on survival, independent fates, correctly reported recovery years, uniform cohort survival and recovery rates, and additive fishing and natural mortality. At least three, and preferably five, years of tagging are needed. Brownie et al. (1995) suggest tagging at least 300 individuals per year as a minimum for waterfowl survival estimates.

**Partitioning mortality.** The tag-reporting rate λ is defined as λ = u/(1 − ...) in the source's notation and relates the exploitation rate to the proportion of tags reported. Exploitation rates should be examined across a range of possible reporting rates. Reporting-rate estimation methods include surreptitiously planted tags, angler or port surveys, high-reward tags, and multi-component catch information. High-reward tags (assumed 100% reported) are the most common approach; if they are not fully reported, the standard-tag reporting rate is positively biased. The authors recommend using reward tags every year to avoid altering angler behavior. Denson et al. (2002) estimated the reporting rate for [[Red Drum]] at approximately 60%. Henry (2002) estimated largemouth bass exploitation in Rodman Reservoir, Florida, using US $5 to $100 variable reward tags and a catch-curve Z estimate, then solved for M.

**Telemetry.** Telemetry estimates survival and mortality through relocations. Important transmitter characteristics are small size, long battery life, adequate detection range, and unique signals. Telemetered fish cannot be directly observed, so viability is inferred from movement. Heupel and Simpfendorfer (2002) monitored juvenile [[Blacktip Shark]]s in a nursery area using remote sonic receivers, which run on one lithium cell battery for several months. Jepsen et al. (1998, 2000) used radio-tagged Atlantic Salmon and Brown Trout smolts and found that predation was indicated by signal movement patterns. Combining telemetry with tagging is recommended for estimating fishing and natural mortality together with reporting rates, although natural-mortality estimates are less precise while reporting-rate estimates are best when fishing mortality is high.

**Conclusions and recommendations.**
- Conduct pilot and simulation studies before large-scale field work.
- Carefully evaluate closure in closed capture-recapture studies, and use multiple sampling periods for heterogeneity models.
- Evaluate temporary emigration in open studies; use a robust design for long-term (>1 month) studies.
- Estimate reporting rates when partitioning total mortality into fishing and natural components.
- Minimize telemetry-related bias by conducting multiple searches or combining searches with remote receivers, and account for emigration and hooking mortality.
- Combining multiple methods should be considered for a complete assessment of mortality components.

The authors conclude that closer communication between biologists and statisticians will improve the application of statistical modeling to fisheries management.