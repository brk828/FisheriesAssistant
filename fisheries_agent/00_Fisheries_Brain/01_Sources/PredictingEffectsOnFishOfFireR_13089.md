---
species: "Multiple game fish species (rainbow trout, coho salmon)"
common_taxa_studied: ["Oncorhynchus mykiss (rainbow trout)", "Oncorhynchus kisutch (coho salmon)"]
family: "Salmonidae"
habitat: "Freshwater streams and rivers (Western Montana, Pacific Northwest)"
ocean_basin: "N/A (Freshwater/Terrestrial Stream Systems)"
study_type: "Predictive Modeling / Toxicology"
publication: "USDA Forest Service Research Paper INT-166"
date: "June 1975"
authors: ["Wayne P. Van Meter", "Charles E. Hardy"]
source_id: "13089"
---

# Predicting Effects on Fish of Fire Retardants in Streams

#ichthyology #marine-biology #freshwater-ecology #Salmonidae #ecotoxicology #wildfire-management

## Executive Summary

This 1975 USDA Forest Service research paper presents a computational method to predict the likelihood of fish kills resulting from aerial application of fire retardant chemicals dropped into streams. The model estimates the distance or time required for a stream to dilute retardant-derived ammonia (NH3) to non-lethal concentrations via turbulent and shear-driven mixing. Field inputs are limited to (1) pounds of nitrogen (calculated as NH3) entering the stream and (2) stream discharge rate and mean velocity near the point of introduction. The authors report an expected accuracy of ±75%, which — despite being imprecise — is presented as operationally valuable for pre- and post-fire decision-making regarding [[Fire Retardant]] use near waterways containing game fish such as [[Rainbow Trout]] and [[Coho Salmon]].

## Background & Description

- **Context**: Aerial fire retardant drop missions increased from near zero in the mid-1950s to nearly 15,000 missions (~17 million gallons) by 1971.
- **Chemical shift**: Sodium calcium borate retardants were phased out in the early 1960s (heavy, expensive, soil sterilant) in favor of ammonium-based salts — diammonium phosphate, monoammonium phosphate, ammonium polyphosphate, and ammonium sulfate — which act as fertilizers at low doses but are toxic at high doses.
- **Toxic agent**: The limiting toxic factor in fire retardants for fish is the **neutral, nonionized ammonia molecule (NH3)**, not the ammonium ion (NH4+). The equilibrium between NH3 and NH4+ is pH-dependent, governed by the ionization constant Ka = 1.8 × 10⁻⁵.
- **Foundational methodology**: Built on stream-tracing techniques developed for the [[Monocacy River]] (Maryland) dye-dispersion study (Taylor 1970; Kilpatrick et al. 1970), originally designed to predict contamination timing for municipal water intakes.
- **Core concept — Unit Concentration (Cu)**: A normalized metric allowing comparison of dispersion behavior across streams of different discharge and dye-load magnitudes:

  Cu = (conservative concentration, mg/L) × (Q, cfs) / (amount introduced, lb)

- **Lapsed time (TL)**: Time from contaminant introduction to peak concentration at a sampling point.
- **Exposure time (TE)**: Defined (by the authors, adapting Taylor's drinking-water-safety threshold of 5%) as the duration concentration remains ≥50% of peak concentration — the operational definition of "hazard window" for fish.
- **Effective concentration (Ce)**: Empirically found to be 0.83 × peak conservative concentration, based on integrated area above the 50%-peak threshold in Monocacy River curves.

## Ecological & Environmental Context

- **Habitat affected**: Freshwater streams and rivers in fire-prone regions of the western United States (case data drawn from Western Montana streams: Eightmile Creek, Blodgett Creek, Lolo Creek, Blackfoot River).
- **Mechanism of dilution**: Contaminant dilution depends on lateral, vertical, and longitudinal mixing. Lateral/vertical mixing occurs quickly; longitudinal dispersion (driven by velocity-gradient shear between channel-center and bank/bottom flow) continues indefinitely downstream.
- **Stream-size effects on fish risk**:
  - **Large streams**: Rapid dilution; short exposure times; higher concentrations tolerable.
  - **Small streams**: Slower dilution, longer exposure times, greater lethality risk; may require tributary inflow to reach safe dilution.
- **Non-retardant fire impacts**: The paper notes fires independently cause fish mortality via elevated stream temperature and ash content — retardant effects must be distinguished from these confounding causes.
- **Species sensitivity note**: Toxicity of nonionized ammonia varies by species and age of fish, and is also influenced by minor retardant constituents (corrosion inhibitors, spoilage inhibitors, thickeners), contributing to model uncertainty.
- **Interagency context**: Referenced ongoing collaborative research (Western Fisheries Ecology Station/EPA, Corvallis, OR, with USFS and BLM) to establish water quality criteria protecting Pacific Northwest freshwater fishes — some of this unpublished toxicity data informed the model's dose-response curves.

## Key Findings

- **Toxicity data sources**: Dose-response ("tolerance time" vs. NH3 concentration) curves were built using:
  - [[Herbert And Shurben 1964]] data — fingerling rainbow trout, controlled pH 7.8, ammonium chloride exposure.
  - [[Blahm Et Al 1972]] data — subyearling/yearling rainbow trout and coho salmon, exposed to four commercial fire retardant formulations, pH measured but uncontrolled.
- **Mortality thresholds modeled**: Separate tolerance-time curves generated for **10% mortality** and **50% mortality** levels as functions of nonionized ammonia concentration (Ceu).
- **Computation workflow** (5 steps):
  1. Acquire Q, mean velocity (v), and pH.
  2. Assume a downstream travel distance.
  3. Compute exposure time (TE) from lapsed time (TL) using velocity and appropriate figures.
  4. Compute tolerance time (Tp) via unit concentration (Cu), estimated NH3 load, conservative concentration (Cc), effective concentration (Ce = 0.83 Cc), and nonionized fraction (Ceu) from pH.
  5. Calculate ratio TE/Tp; iterate distance until ratio ≈ 1.00, defining the **"critical distance"** beyond which fish survival is likely.
- **Sample case — Lolo Creek** (Q = 35.9 ft³/s, v = 1.21 ft/s, pH 8.0, 111 lb NH3 introduced): Critical distance calculated at approximately **29,500 feet** (using the 10% mortality criterion).
- **Sample case — Blodgett Creek** (Q = 11.7 ft³/s, v = 0.43 ft/s, pH 8.0, 76 lb NH3): Ratio TE/Tp remained far below 1.00 even at 7,500–12,500 ft under the 50% mortality criterion, indicating persistent lethal risk over the tested distances in this smaller stream.
- **Accuracy**: Overall system accuracy estimated at **±75%**, propagated via root-sum-square combination of uncertainties in species sensitivity, retardant load estimation, and hydrologic field data.
- **Two primary applications**:
  1. **Pre-fire planning** — using pre-tabulated low-flow discharge/cross-section data to judge acceptable risk before ordering a retardant drop across a stream.
  2. **Post-incident assessment** — calculating the actual zone of potential fish damage after an accidental retardant release, using measured Q and cross-section at the point of entry.
- **Generalizability**: The dilution-computation framework is presented as broadly applicable to any soluble contaminant introduced as a single slug at a single point in a flowing stream, beyond fire retardant contexts specifically.