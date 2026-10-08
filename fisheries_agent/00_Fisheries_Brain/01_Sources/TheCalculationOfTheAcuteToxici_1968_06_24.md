---
species: "Salmo gairdnerii (Rainbow Trout)"
family: Salmonidae
habitat: Freshwater rivers, streams (industrially polluted surface waters)
ocean_basin: N/A (Freshwater study)
source_id: "13831"
---

# The Calculation of the Acute Toxicity of Mixtures of Poisons to Rainbow Trout

#ichthyology #marine-biology #Salmonidae #toxicology #water-pollution

## Executive Summary

This 1968 study by V.M. Brown (Water Pollution Research Laboratory, Stevenage) presents a method for calculating the acute toxicity of mixtures of common industrial pollutants to [[Rainbow Trout]] (*Salmo gairdnerii*). The approach estimates combined toxicity by summing the "proportion of the 48-hr median lethal concentration" (48-hr LC50) contributed by each poison in a mixture — ammonia, phenol, zinc, copper, cadmium, lead, nickel, and hydrogen cyanide — after correcting each poison's individual LC50 for site-specific water quality parameters (temperature, pH, total hardness, bicarbonate alkalinity, total dissolved solids, and dissolved oxygen). The method treats poisons as generalized physiological "stressors" whose effects summate additively, and it was empirically validated for mixtures of two to four poisons under controlled conditions. The paper stresses that this predictive approach is a management tool for assessing river and effluent toxicity but is not a substitute for direct fish bioassay, particularly in critical regulatory contexts.

## Background & Description

This paper is a toxicological/methodological study rather than a morphological description of the species; no anatomical or morphometric data on *Salmo gairdnerii* are provided. The only biologically relevant physiological detail concerns comparative sensitivity between species: [[Rainbow Trout]] were found to be more sensitive to combined-poison mixtures than the cyprinids [[Roach]] (*Rutilus rutilus*) and [[Dace]] (*Leuciscus leuciscus*) over a 48-hr exposure period, indicating an unspecified interspecific difference in physiological tolerance to toxic stress.

## Ecological & Environmental Context

- **Habitat context**: [[Rainbow Trout]] inhabit temperate freshwater rivers and streams that may be subject to industrial and sewage pollution, making them a key indicator/test species for water quality regulation in Britain.
- **Environmental modulators of toxicity**: The acute lethal toxicity of pollutants to trout is not fixed but is strongly modulated by abiotic water quality variables:
  - **Ammonia** toxicity depends on pH, bicarbonate alkalinity, temperature, free CO₂, and dissolved oxygen (toxicity attributable to un-ionized/undissociated ammonia fraction).
  - **Phenol** (particularly gas-liquor/coke-oven derived monohydric phenols) toxicity depends on temperature and dissolved oxygen.
  - **Metals** (zinc, copper, cadmium, lead, nickel) toxicity depends on total water hardness (as CaCO₃) and dissolved oxygen; harder water reduces metal toxicity.
  - **Hydrogen cyanide (HCN)** toxicity is governed by the concentration of molecular (undissociated) HCN rather than the cyanide ion, so toxicity increases as pH decreases; toxicity also appears to increase at lower temperatures.
  - **Dissolved oxygen** was found to affect toxicity of *all* poisons examined — reduced DO consistently increases relative toxicity.
- **Acclimatization effects**: Metal toxicity thresholds depend on fish being acclimatized ≥5 days to the test water's hardness; non-acclimatized fish respond according to the hardness of their water of origin, not the test water — relevant to [[Restocking Programs]] and transfer scenarios.
- **Interspecific comparison**: [[Roach]] and [[Dace]] (cyprinids) showed greater resistance than trout to mixed-poison exposure over 48 hours, suggesting niche-related or physiological differences in pollution tolerance among freshwater fish taxa.
- **Biological variability**: 48-hr LC50 values for ammonia, phenol, and zinc varied by a factor of 2.5 across a 9-month period in the same trout stock, attributed to seasonal/circadian rhythms, age, sex, nutritional state, and strain — underscoring that toxicity is not a fixed species trait but is context- and physiology-dependent.

## Key Findings

1. **Core method**: Toxicity of a poison mixture = Σ (concentration of each poison in water ÷ its calculated 48-hr LC50 for that water quality). A sum ≥1.0 predicts ≥50% mortality of trout within 48 hours; a sum <1.0 predicts <50% mortality.
2. **Worked example** (water: 320 mg/l hardness, 200 mg/l alkalinity, 400 mg/l TDS, 50% O₂ saturation, 15°C, pH 7.62):

| Poison | Conc. (mg/l) | 48-hr LC50 (mg/l) | Proportion of LC50 |
|---|---|---|---|
| Ammonia | 6.3 | 31.13 | 0.20 |
| Phenol | 1.39 | 4.6 | 0.30 |
| Zinc | 0.62 | 2.8 | 0.22 |
| Copper | 0.12 | 0.4 | 0.30 |
| Cyanide | 0.01 | 0.07 | 0.17 |
| **Sum** | | | **1.19** (predicts >50% mortality in 48 hr) |

3. **Correction factors derived from graphical/nomographic relationships**:
   - Ammonia 48-hr LC50 increases with higher pH, higher alkalinity, and higher temperature but decreases with lower dissolved oxygen and higher free CO₂.
   - Phenol (gas-liquor form) is less toxic than pure phenol at a given temperature; toxicity decreases with warming temperature; reduced DO increases toxicity.
   - Metal toxicity (Zn, Cu, Cd, Pb, Ni) decreases (i.e., LC50 increases) with increasing total hardness; reduced DO increases toxicity (multiplicative correction factor ~0.79 at 50% saturation for Zn and Cu in the example).
   - Copper 48-hr LC50 in hard water (320 mg/l CaCO₃) estimated at ~0.5 mg/l (range 0.2–1.2 mg/l reported in literature).
   - HCN 48-hr LC50 = 0.07 mg/l under example conditions; toxicity governed by molecular HCN fraction, which rises as pH falls.
4. **Standard practical benchmark**: "The concentration killing half a batch of rainbow trout in 2 days" (48-hr LC50) is used as a practical proxy for the true asymptotic "median threshold concentration," which for some poisons (ammonia, cyanide) is reached in 3–6 hr, and for others (zinc, copper) may take 3–7 days.
5. **Empirical validation and limits**: The additive-summation model held reasonably well for 2–4 poison mixtures under controlled lab conditions, but broke down when zinc contributed >70% of mixture toxicity, and *underestimated* toxicity for complex real-world mixtures (sewage effluents, fluctuating river concentrations) — in these cases mortality of 50% of fish occurred at a summed proportion averaging ~0.7, not 1.0.
6. **Confidence limits**: Under controlled testing, the sum corresponding to 50% mortality was estimated to lie between ~0.75 and 1.30 (95% confidence limits), varying with the specific poisons involved.
7. **Known sources of error/limitations**:
   - Unaccounted poisons in real polluted waters.
   - Chemical analysis may overestimate "active" toxic fraction (e.g., complexed/bound metals are less toxic than total measured concentration; molecular cyanide measurements may include less-toxic organic cyanides).
   - Natural biological variability in trout sensitivity (up to 2.5× across seasons).
   - Method has not yet been validated for species other than [[Rainbow Trout]], apart from limited comparative data with [[Roach]] and [[Dace]].
8. **Temperature interactions flagged for future correction**: Preliminary evidence suggests 48-hr LC50 of zinc and un-ionized ammonia to trout is affected by temperature, and HCN is more toxic to trout fry at low (3°C) than high (13°C) temperature — flagged as needing further correction factors in the model.
9. **Regulatory/practical framing**: The method is proposed as a screening/assessment tool for river water and effluent toxicity from chemical/physical data alone, but the author explicitly cautions it cannot replace direct fish toxicity testing in critical regulatory decisions.