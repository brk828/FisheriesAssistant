---
species: "Cyprinus carpio (common carp), Ictalurus punctatus (channel catfish), Ictalurus catus (white catfish), Tilapia mossambica, Tilapia aurea, Tilapia melanopleura"
family: "Cyprinidae, Ictaluridae, Cichlidae"
habitat: "Freshwater aquaculture ponds"
ocean_basin: "N/A (freshwater pond aquaculture)"
tags: [ichthyology, marine-biology, aquaculture, pond-fish-culture]
source_id: "15117"
---

# Estimation of standing crops and rates of feeding fish in ponds

## Executive Summary
This 1966/1968 paper by H.S. Swingle (Auburn University) presents a quantitative methodology for estimating **standing crop** (total biomass) of pond-cultured fish and for calculating appropriate **daily feeding rates**, using data on feed conversion in [[Channel Catfish]], [[White Catfish]], and several [[Tilapia]] species, as well as [[Common Carp]]. The core contribution is a set of empirical equations that relate cumulative feed input to fish biomass gain via a **pond conversion value ("S")**, offering an alternative/complement to traditional seining-based biomass estimates, which are shown to be subject to substantial sampling error. The work underpins practical aquaculture management protocols for warm-water pond fish culture.

## Background & Description
This paper is methodological/quantitative rather than morphological, but it references body-size classes relevant to feeding rate calculations:

- **Tilapia species** (*T. mossambica*, *T. aurea*, *T. melanopleura*): feeding rate tiers defined by total length classes of 2.4–12.0 cm and 12.0–24.0 cm.
- **Catfish species** (*Ictalurus punctatus*, *I. catus*): five length classes from 2.4 cm to >31.2 cm, each with a distinct optimal daily feeding percentage (decreasing from 5% to 1.5% of body weight as fish grow).
- Larger fish were observed to "cram their stomachs" disproportionately during seining immediately post-feeding, biasing average weight estimates upward; corrections using length-weight relationships were recommended.
- Smaller individuals were found preferentially in shallow water, increasing their vulnerability to seine capture and biasing average population weight estimates downward during non-feeding periods.

## Ecological & Environmental Context
- **Habitat**: Warm-water earthen aquaculture ponds (0.5–10 ha in the Auburn, Alabama experimental system), representative of freshwater pond culture systems used globally for [[Tilapia]] and [[Catfish]] production.
- **Thermal requirements**: Effective feeding/conversion required water temperatures **above 22°C (75°F)** for tilapias and **above 16°C (60°F)** for catfish; feeding below these thresholds was ineffective or unsafe.
- **Trophic dynamics**: Pond systems exhibited significant contributions from **natural fish-food organisms** (plankton/detritus-based food webs stimulated by feed and waste inputs), particularly at low standing crop densities (<1,000 kg/ha), where natural production could supply ~2 kg/ha/day of growth independent of supplied feed.
- **Density-dependent survival**: Survival rates varied strongly by species/variety — scaled common carp: 97–100%/year; mirror carp variety: 80–90%/year; tilapias: 65–90%/year — with direct implications for stocking-based biomass estimation error.
- **Maximum safe feeding loads** (Auburn No. 2 pelleted feed, 46% protein): Channel/White catfish 39 kg/ha/day (34 kg in mid-summer); Java/Nile tilapia 55 kg/ha/day; Congo tilapia 38 kg/ha/day — defining upper ecological/production limits of the system.

## Key Findings

### Sources of Error in Standing Crop Estimation
1. **Average weight error**: Seine samples of <100 catfish or <300 tilapia produced average weight estimates deviating **8–19%** from true values (verified via pond draining).
2. **Population number error**: Reliance on stocking numbers or average mortality assumptions introduces significant error, especially in species/varieties with variable survival (e.g., [[Mirror Carp]], tilapias).

### Pond Conversion Value ("S")
Defined as:
**S = kg feed added / net kg fish produced**

- Catfish (channel & white): **S = 1.5–2.0**, average **1.7**, using Auburn No. 2 pelleted feed at temps >16°C.
- Tilapias (*mossambica*, *aurea*, *melanopleura*): **S = 0.7–1.2**, average **1.0**, at temps >22°C.
- "S" is not constant but **increases progressively** with cumulative feed added (e.g., from 0.5 at 100 kg cumulative feed to 1.7 at 1,700 kg), reflecting diminishing contribution of natural food organisms as standing crop increases.

### Core Equations
1. **Standing crop from feed supplied**:
   `Standing crop = I + F/S`
   where I = initial stocked weight, F = cumulative feed added, S = pond conversion value.

2. **Rate of weight change per interval**:
   `R_T = 1 + (D·P)/S`
   where D = feeding days per interval T, P = daily feeding rate (0.02–0.05), S = conversion value.

3. **General growth equation**:
   `W = I · R^N` (or `log W = log I + N log R`)
   where N = number of feeding intervals T.

4. **Number of intervals required to reach target weight**:
   `N = (log W − log I) / log R`

5. **Initial weight required to reach target weight**:
   `log I = log W − N·log R`

6. **Maintenance-corrected standing crop** (for high initial biomass or short feeding periods):
   `Standing crop = I + (F·M)/S`, where `M = I × 0.005 × number of days fed`.

### Validation Against Draining Data
- Standing crop estimates derived from **cumulative feed ÷ S** were comparable in accuracy to seining-based estimates when checked against actual pond-draining biomass (e.g., 1,255 vs. 1,251 vs. 1,495 kg/ha across paired comparisons).
- Un-fed/unfertilized control ponds averaged **97 kg/ha** standing crop after 210 days from natural productivity alone.

### Practical Feeding Rate Guidelines
- Catfish: feeding rate declines from **5% body weight/day** (2.4–12 cm fish) to **1.5%/day** (>31.2 cm fish).
- Tilapia: feeding rate declines from **3%/day** (2.4–12 cm) to **3%/day** (12–24 cm) [rates listed as consistent across both size classes in source].
- Maintenance ration (no growth) ≈ **0.5% body weight/day**, six days/week — this baseline must be subtracted from gross feeding rate to isolate growth-producing feed allocation.

### Worked Example (Channel Catfish)
- Starting at I = 40 kg, fed 6 days/week at P = 0.03, S = 1.7, over 30 weekly intervals: **W ≈ 821 kg**.
- To scale to 2,000 kg/ha total production required ~40.1 weeks total feeding time, factoring in the 1,300 kg/ha maximum safe feeding threshold constraint.

## Related Concepts
[[Pond Aquaculture]] · [[Feed Conversion Ratio]] · [[Seining Methodology]] · [[Standing Crop Estimation]] · [[Warm-Water Pond Fish Culture]] · [[Auburn No. 2 Pelleted Feed]]