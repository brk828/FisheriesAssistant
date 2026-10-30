---
species:
  - "Morone saxatilis"
  - "Salmo salar"
  - "Salmo trutta"
  - "Carcharhinus limbatus"
common_name:
  - "Striped Bass"
  - "Atlantic Salmon"
  - "Brown Trout"
  - "Blacktip Shark"
family: "N/A"
habitat: "Freshwater reservoirs and lakes (Lake Gaston; reservoirs); estuarine and nursery areas (blacktip shark); river systems (smolt migration)"
ocean_basin: "N/A"
location: "Lake Gaston, North Carolina-Virginia, USA; North Carolina, USA (study institutions); Denmark and Scandinavian rivers (Atlantic salmon and brown trout smolt studies)"
tags:
  - ichthyology
  - marine-biology
  - fisheries-management
  - mortality-estimation
title: "Combining Telemetry and Fisheries Tagging Models to Estimate Fishing and Natural Mortality Rates"
source_id: "PML2151"
marsh_id: "PML2151"
library: "Marsh Library"
permission: "not public domain"
source_citation: "K. H. Pollock, H. Jiang, J. E. Hightower (2004). Combining Telemetry and Fisheries Tagging Models to Estimate Fishing and Natural Mortality Rates. Transactions of the American Fisheries Society 133:639-648. Marsh Library ID: PML2151."
source_file: "Pollock K.H. et al. 2004. combining telemetry and fisheries tagging models to estimate fishing and natural mortality rates.pdf"
text_extraction: "text"
---
# Combining Telemetry and Fisheries Tagging Models to Estimate Fishing and Natural Mortality Rates

#ichthyology #marine-biology #fisheries-management

## Executive Summary

This paper proposes a joint model that combines conventional multiyear tag return data with telemetry data to estimate instantaneous fishing mortality (F), natural mortality (M), and the tag reporting rate (λ) in exploited fish populations. Tag return methods supply information on fishing deaths but cannot observe natural deaths directly and require a reporting rate that is hard to estimate. Telemetry supplies direct information on natural mortality but none on fishing deaths. Using simulations, the authors show that the combined model yields more precise and effectively unbiased estimates than either method alone, and that it can estimate the reporting rate reliably, a task that tag return data alone cannot accomplish. The work is primarily a statistical and methodological study built on simulated data.

## Background & Description

Accurate fisheries management requires knowledge of both fishing and natural mortality, yet natural mortality is difficult to measure because natural deaths are rarely observed. The authors list five estimation approaches: [[Catch Curve Analysis]], regression of total mortality on fishing effort, correlation of M with life-history parameters, [[Tag Return Method]], and [[Telemetry Method]]. Catch curves estimate only total mortality (Z), which equals M only for unfished populations. Life-history correlations need little data but yield estimates of unknown precision.

Tag return models, developed by Pollock and colleagues, require a tag reporting rate, which is difficult to estimate. Approaches to this include reward tagging, creel surveys, port sampling, planted tags, and pre- and postseason tagging models ([[Hearn Et Al. 1998]]; [[Hearn Et Al. 2003]]). Multiyear tag return models also assume that newly tagged fish mix completely with previously tagged fish.

Telemetry methods, extended from the [[Kaplan-Meier Estimator]] and the [[Jolly-Seber Model]] by [[Pollock Et Al. 1995]], directly record live and naturally dead animals at shorter intervals than annual tag returns. [[Hightower Et Al. 2001]] first applied these methods to fish, estimating natural and fishing mortality of [[Striped Bass]] stocked in [[Lake Gaston]]. Joint analysis of different data types has also been used in wildlife survival studies.

## Ecological & Environmental Context

The paper addresses fish populations in which fishing mortality is often low under tight regulation, a situation where traditional tagging models estimate M poorly. The authors also note that hooking mortality can contaminate telemetry-based estimates of natural mortality, citing [[Tournament-Associated Mortality]] and bait and temperature effects on striped bass hooking mortality.

Field examples of natural mortality drawn from the literature include:
- Predation on radio-tagged [[Atlantic Salmon]] and [[Brown Trout]] smolts by [[Northern Pike]] and [[Pikeperch]], detected through reduced transmitter signal strength or tracking into shallow water, and by bird predation.
- Seasonal patterns in fishing and natural mortality of striped bass in a reservoir.
- Nursery-area mortality of juvenile [[Blacktip Shark]] estimated with remote monitoring stations and acoustic transmitters.

## Key Findings

- **Combined model performance:** When telemetry relocation probability equals 1, the combined model estimates annual F and constant M with essentially no bias and smaller standard errors than the separate models. Simulations used 500 tagged fish per year for tag return data and 50 telemetered fish per year.
- **Precision of M:** Relative standard errors (RSEs) for M in the 3-year study were about 0.15 (λ known) and 0.16 (λ estimated). In the 5-year study they were about 0.09 and 0.11 (combined model), versus about 0.12 and 0.13 for telemetry-only analysis, with tag return alone performing poorly. The paper's summary table gives a tag return RSE of 0.3042 for the 3-year study with λ known.
- **Precision of F:** RSEs for annual F were about 8–10% when λ was known and 11–14% when λ was unknown in the 3-year study. Fishing mortality was estimated with slightly greater precision than natural mortality.
- **Tag reporting rate:** The combined model estimated λ reliably, with RSEs of 0.0825 (3 years) and 0.0575 (5 years) at λ = 0.6. At λ = 0.2, RSEs were 0.1119 and 0.0741. Tag return data alone were judged insufficient, and even 20 years of tagging data did not yield reliable estimates of λ or M.
- **Telemetry sample size:** Increasing telemetry tags from 25 to 50 per year sharply reduced the RSE of M (from 0.2327 to 0.1645 over 3 years; from 0.1684 to 0.1187 over 5 years). Increasing regular tags from 500 to 3,000 per year changed the RSE only slightly.
- **Relocation probability:** Lower relocation probability raised RSEs only modestly. Between 0.9 and 1.0, RSE increases were no more than about 10%; for one scenario, RSE for M rose from 18% to 20%.
- **Mortality patterns:** Tag return precision for M improved as F increased, while telemetry precision for M declined as F increased because fewer fish remained in the study. The combined model behaved like the telemetry model because telemetry information dominates.
- **Assumptions:** The authors flag several key assumptions, including representative tagging, no tag loss, no tagging effect on survival, no emigration, and that movement patterns correctly identify natural deaths. Violation of the emigration assumption biases F upward.
- **Future research:** The authors recommend examining incompatibilities among estimates from different methods and investigating reliable tag return estimation of λ from once-a-year data.