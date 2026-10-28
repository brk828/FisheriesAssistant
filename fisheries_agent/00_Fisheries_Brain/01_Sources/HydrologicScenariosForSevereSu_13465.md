---
title: "Hydrologic Scenarios for Severe Sustained Drought in the Southwestern United States"
authors: David G. Tarboton
year: 1995
source_journal: "Water Resources Bulletin, Vol. 31, No. 5"
taxon_focus: "None (hydrology/water resources study — no fish or aquatic biota directly analyzed)"
habitat: "Colorado River Basin (Lees Ferry compact point, Lake Powell, Lake Mead); semi-arid/arid Southwestern United States"
ocean_basin: "N/A — inland freshwater basin (Colorado River drains to Gulf of California)"
river_basin: "Colorado River Basin"
study_type: "Paleoclimate reconstruction / stochastic hydrologic modeling"
source_id: "13465"
---

# Hydrologic Scenarios for Severe Sustained Drought in the Southwestern United States

#hydrology #freshwater-ecology #colorado-river-basin #drought-science #water-resources-management

> **Note on scope:** This source is a hydrology/water-resources paper, not an ichthyological or biological study. It contains no direct data on fish species, populations, or aquatic community structure. It is included here because sustained hydrologic drought scenarios in the [[Colorado River Basin]] have direct downstream relevance to freshwater fish habitat, reservoir ecology (e.g., [[Lake Powell]], [[Lake Mead]]), and instream flow regimes that structure aquatic ecosystems. The note below synthesizes the paper faithfully as a hydrologic/environmental risk assessment.

## Executive Summary

Tarboton (1995) develops and quantifies the risk of severe, sustained drought scenarios for the [[Colorado River Basin]], the principal water source for the southwestern United States, including southern California via the Colorado River Aqueduct. Using 78 years of unimpaired historic streamflow (1906–1983) and two independent tree-ring–based streamflow reconstructions extending back to 1520, the author identifies critical historic and paleo-drought periods at the Lees Ferry compact point. Three drought scenarios are defined — a historic drought (1943–1964), a tree-ring reconstructed "severe drought" (1579–1600), and an artificially rearranged worst-case version of the same period — and their statistical return periods are estimated (ranging from ~50–100 years to potentially >10,000 years) using four stochastic streamflow models. These scenarios and their probabilities underpin subsequent companion papers assessing drought impacts on Colorado River water infrastructure, with implications for any biota, including fish, dependent on regulated flow and reservoir storage in the basin.

## Background & Description

- **Study system:** The [[Colorado River]] drains portions of Wyoming, Colorado, Utah, Arizona, Nevada, California, and New Mexico. Streamflow originates predominantly as snowmelt from the Rocky Mountains and is regulated by major storage reservoirs, principally [[Lake Powell]] and [[Lake Mead]].
- **Legal/hydrologic reference point:** Streamflow accounting is centered on **Lees Ferry, Arizona**, defined as one mile downstream of the confluence of the Colorado and Paria Rivers — the legal compact point dividing the Upper and Lower Colorado River Basins under the Colorado River Compact.
- **Data sources used:**
  1. U.S. Bureau of Reclamation unimpaired historic streamflow at 29 basin sites, 1906–1983 (78 years).
  2. Tree-ring reconstructed streamflow at Lees Ferry, 1520–1961 (442 years) — [[Stockton and Jacoby (1976)]].
  3. Tree-ring reconstructed streamflow at Lees Ferry, 1568–1962 (395 years) — [[Michaelson et al. (1990)]].
- **Reconstruction validity:** Cross-correlation between observed and reconstructed flow was 0.76 (Stockton & Jacoby) and 0.77 (Michaelson et al.), indicating tree-ring proxies capture roughly 58–59% of streamflow variance.
- **Key statistical discrepancy:** Reconstructed-period mean flow (13.5 MAF) is significantly lower (t > 3, p < 0.004) than the historic recorded mean (15.2 MAF), a nonstationarity attributed partly to detrending procedures inherent in tree-ring calibration.

## Ecological & Environmental Context

Although the paper does not address biota directly, its findings characterize the **hydrologic disturbance regime** that governs freshwater habitat conditions throughout the basin:

- **Flow variability and drought severity:** The reconstructed record reveals multi-decadal to century-scale drought episodes (e.g., 1579–1600, 1600–1630) far more severe than anything captured in the 20th-century gauge record. Such events would translate into prolonged reductions in river discharge, reservoir levels, and downstream habitat connectivity — conditions highly relevant to native fish species in the Colorado River system, such as [[Colorado Pikeminnow]], [[Humpback Chub]], and other basin-endemic species dependent on natural flow variability and reservoir/river interfaces.
- **Reservoir drawdown scenario:** The "Rearranged Severe Drought" scenario, in which the driest years of the 1579–1600 period are clustered at the end, was found to draw [[Lake Powell]] down to "dead level" (i.e., below minimum operational pool). This kind of extreme drawdown scenario has direct implications for aquatic habitat volume, water temperature regimes, and connectivity in regulated systems.
- **Interbasin water transfer stress:** The paper notes that Southern California depends on Colorado River water via the Colorado River Aqueduct, alongside northern California supplies — meaning sustained basin-wide drought propagates hydrologic stress to distant freshwater and aquatic systems outside the basin itself.
- **Stationarity assumption caveat:** The author explicitly cautions that risk quantification assumes climatic/hydrologic stationarity, a simplifying assumption with direct relevance for long-term aquatic conservation planning under a changing climate.

## Key Findings

- **Drought scenarios identified for planning:**
  1. **Colorado Drought of Historic Record (1943–1964):** Derived from the unimpaired gauge record; estimated return period **50–100 years**.
  2. **Colorado Severe Drought (1579–1600):** Tree-ring reconstructed; three consecutive hydrologic droughts in rapid succession; 17-yr mean flow 10.47 MAF, 22-yr mean flow 11.05 MAF (vs. historic mean 15.2 MAF); estimated return period **400–700 years**.
  3. **Colorado Rearranged Severe Drought:** Same total water volume as Scenario 2 but with lowest-flow years clustered at the end (16-year mean = 9.57 MAF); designed as a catastrophic stress-test scenario; estimated return period **2,000–10,000+ years**; used because it drove [[Lake Powell]] to dead pool level in companion impact studies.

- **Streamflow statistics (Table 1):**

| Series | Length (yrs) | Mean (MAF) | SD (MAF) | Lag-1 Correlation | Hurst Coefficient |
|---|---|---|---|---|---|
| Unimpaired flows, Lees Ferry (1906–1985) | 80 | 15.2 | 4.24 | 0.21 (n.s.) | 0.73 |
| Stockton & Jacoby (1976) reconstruction | 442 | 13.5 | 3.59 | 0.32 | 0.63 |
| Michaelson et al. (1990) reconstruction | 395 | 13.8 | 3.61 | 0.26 | 0.65 |

- **Stochastic models used to estimate return periods:**
  - Model 1: Independent annual flows.
  - Model 2: Autoregressive order-1 (fixed parameters).
  - Model 3: Autoregressive order-1 (parameter uncertainty).
  - Model 4: Fractional Gaussian noise (captures long-memory/Hurst behavior).
  - Models 3 and 4 (which account for parameter uncertainty and long-term persistence) gave return-period estimates most consistent with naive record-length estimates; Models 1 and 2 substantially overestimated return periods (by orders of magnitude for the severe and rearranged scenarios), indicating they underrepresent real hydrologic persistence/risk.

- **Disaggregation methodology:** The SPIGOT package (Grygier and Stedinger, 1988/1990) was adapted to disaggregate annual tree-ring-based aggregate flows into monthly, spatially distributed flows at 29 source points, enabling realistic input to basin-wide water allocation models (Colorado River Simulation System, California DWR model) — a technique broadly transferable to instream-flow/habitat modeling for aquatic species.

- **Overall conclusion:** Severe, multi-decade droughts far exceeding the 20th-century observational record are physically plausible in the Colorado River Basin based on paleo-reconstructed streamflow, with return periods estimated at centuries to millennia. These events, and the associated reservoir drawdown scenarios, represent the range of hydrologic stress that any comprehensive aquatic ecosystem or fisheries risk assessment in the basin would need to incorporate.

## Related Concepts
- [[Colorado River Basin]]
- [[Lees Ferry]]
- [[Lake Powell]]
- [[Lake Mead]]
- [[Colorado River Compact]]
- [[Tree-Ring Streamflow Reconstruction]]
- [[Hydrologic Drought]]
- [[Stochastic Streamflow Modeling]]
- [[Instream Flow Requirements]]
- [[Humpback Chub]]
- [[Colorado Pikeminnow]]