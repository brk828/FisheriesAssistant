---
species: "Rainbow Trout (Salmo gairdnerii Richardson)"
family: Salmonidae
habitat: "Freshwater (hard, alkaline bore-hole water; laboratory aquaria)"
ocean_basin: "N/A (freshwater/laboratory study)"
study_type: "Acute toxicology bioassay"
poisons_studied: [Ammonia, Phenol, Zinc]
temperature_range_C: "10-12 (Series 1); 11.7-12.2 (Series 2)"
pH_range: "7.5-7.9"
source: "Brown, V.M., Jordan, D.H.M. & Tiller, B.A. (1969). J. Fish Biol. 1, 1-9"
source_id: "13833"
---

# The Acute Toxicity to Rainbow Trout of Fluctuating Concentrations and Mixtures of Ammonia, Phenol and Zinc

#ichthyology #marine-biology #toxicology #Salmonidae #ecotoxicology #freshwater-pollution

## Executive Summary
This 1969 laboratory study examines the acute toxicity of ammonia, phenol, and zinc to [[Rainbow Trout]] under two experimental conditions: (1) fluctuating vs. constant poison concentrations, and (2) three-poison mixtures at constant concentration. The work extends earlier additive-toxicity models (Lloyd, Herbert) by testing whether fractional-toxicity summation—A₁/A_L + B₁/B_L = 1—remains valid under more variable, ecologically realistic exposure regimes. Key results show that fluctuating exposures (within ±50% of the 48-h LC50) produce survival times statistically indistinguishable from constant-exposure controls, provided fluctuation periodicity does not exceed the poison's "resistance time." For three-poison mixtures, additive toxicity summation held well except when [[Zinc Toxicity|zinc]] dominated (>70% of the mixture), where an antagonistic effect was observed, causing standard predictive models to overestimate actual toxicity.

## Background & Description
- **Species tested:** Hatchery-reared [[Rainbow Trout]] (*Salmo gairdnerii* Richardson).
- **Series 1 (fluctuating concentrations):** Fork length 8.5–14.5 cm.
- **Series 2 (mixture toxicity):** Fork length 5–9 cm (smaller, younger fish).
- No morphological/anatomical pathology data reported; study is purely survival-time/mortality based (behavioral endpoint: cessation of all movement for ≥2 min = death).
- Fish were acclimatized 3+ weeks (Series 1) or 24 h (Series 2) in flowing bore-hole water matching test-water chemistry prior to exposure; unfed during acclimatization/testing.

## Ecological & Environmental Context
- **Water chemistry (bore-hole water used throughout):**
  - Total hardness: 320 mg/l as CaCO₃
  - Total alkalinity (methyl orange): 240 mg/l as CaCO₃
  - Calcium: 120 mg/l; Magnesium: 5 mg/l
  - Dissolved oxygen maintained near air-saturation
  - pH controlled via CO₂/air bubbling (CO₂ 12 ml/min, air 6 l/min)
- **Relevance to [[Freshwater Pollution]] & river management:** The study directly informs pollution-control practice by testing whether laboratory-derived additive toxicity models (originally built on constant-concentration exposures) apply to real-world scenarios where poison concentrations in rivers fluctuate temporally (e.g., due to intermittent effluent discharge).
- **Poisons as environmental stressors:**
  - [[Ammonia Toxicity]] (as NH₃/N, from NH₄Cl)
  - [[Phenol Toxicity]] (C₆H₆O)
  - [[Zinc Toxicity]] (as Zn²⁺, from ZnSO₄·7H₂O)
- Test solutions renewed every 24 h (or every 6 h when phenol present, to prevent microbial degradation of phenol).
- Analytical methods: ammonia via Lee et al. (1960) distillation method; phenol via 4-amino-antipyrine method (Ochynski, 1960); zinc via Sandell (1950) colorimetry.

## Key Findings

### 1. Fluctuating vs. Constant Concentrations
| Poison | Condition | Median Survival (min) | 95% CI |
|---|---|---|---|
| Ammonia | Fluctuating 2-h intervals (1.5↔0.5× LC50) | 370 | 308–445 |
| Ammonia | Fluctuating 1-h intervals | >700 | — |
| Ammonia | Constant 48-h LC50 | >700 | — |
| Zinc | Fluctuating 4-h intervals | 2960 | 2348–3730 |
| Zinc | Fluctuating 2-h intervals | 2340 | 1376–3978 |
| Zinc | Constant 48-h LC50 | 2400 | 1678–3432 |
| Ammonia + Zinc | Fluctuating 3-h intervals | 4400 | 3164–6116 |
| Ammonia + Zinc | Fluctuating 1-h intervals | 3900 | 3333–4562 |
| Ammonia + Zinc | Constant 48-h LC50 | 3400 | 2698–4285 |

- Only **ammonia alone** showed a statistically significant difference between fluctuating (2-h interval) and constant exposure — fish died rapidly upon re-immersion in the higher concentration, suggesting rapid loss of acclimation/recovery for ammonia specifically.
- At **1-h fluctuation intervals**, ammonia toxicity matched constant-exposure levels (30% mortality in both), implying a "resistance time" threshold below which fluctuation has no differential effect.
- For zinc and the ammonia+zinc mixture, no significant differences were found across fluctuation regimes — supporting the validity of using time-averaged concentrations for these poisons in predictive river models.
- Mixture (ammonia+zinc) survival times at 1.5× LC50 **exceeded** those of either poison alone tested separately — consistent with findings by Herbert & Shurben (1964).

### 2. Single-Poison 48-h LC50 Values (Present Study vs. Historical Data)
| Poison | 48-h LC50 (mg/l) | 95% CI | Slope Function (S) | % of Previously Published Value |
|---|---|---|---|---|
| Ammonia (as N), test (i) | 35.0 | 30.2–40.6 | 1.28 | 78% |
| Ammonia (as N), test (ii) | 36.0 | 31.8–40.1 | 1.11 | 80% |
| Phenol | 8.0 | 7.4–8.6 | 1.08 | 82% |
| Zinc (as Zn²⁺) | 4.0 | 3.50–4.56 | 1.16 | 101.5% |

- Notable finding: locally-derived LC50 values for ammonia and phenol were only ~78–82% of previously published ("standard") values, highlighting **batch-to-batch variability in trout sensitivity** — a key caveat for the additive-toxicity method's assumption of "uniformity of sensitivity."

### 3. Three-Poison Mixture Toxicity (Ammonia + Phenol + Zinc)
| Test | Observed/Predicted 48-h LC50 (95% CI) | Slope (S) | % Ammonia | % Phenol | % Zinc |
|---|---|---|---|---|---|
| a | 1.01 (0.88–1.15) | 1.17 | 38 | 42 | 20 |
| b | 0.85 (0.73–0.99) | 1.20 | 11 | 77 | 12 |
| c | 1.45 (1.27–1.65) | 1.25 | 12 | 14 | 74 |
| d | 1.16 (1.01–1.33) | 1.25 | 76 | 14 | 10 |
| e | 1.45 (1.28–1.64) | 1.27 | 12 | 11 | 77 |

- **Additive toxicity (summation of fractional toxicities) held true** (95% CI embracing 1.0) for mixtures dominated by ammonia (test d) or roughly equal contributions (test a), and phenol-dominated (test b).
- **When zinc predominated (>70%, tests c and e)**, observed toxicity was consistently *less* than predicted (ratio 1.45), indicating a **possible antagonistic interaction** — zinc mixtures were less toxic than simple additive summation would predict.
- Slope functions (S) were lowest (least population variability) in the balanced mixture (test a, S=1.17) and highest where ammonia or zinc predominated (S=1.25–1.27), indicating greater variability in individual tolerance under those conditions.

### 4. Comparison of Present vs. "Standard" LC50 Values in Predicting Mixture Toxicity
| Test | Sum of fractional toxicities (present LC50s) | Sum using "standard" LC50s |
|---|---|---|
| a | 1.01 | 0.83 |
| b | 0.85 | 0.70 |
| c | 1.45 | 1.36 |
| d | 1.16 | 0.90 |
| e | 1.45 | 1.36 |

- Using historical/"standard" LC50 values (from other fish stocks) consistently **overestimated mixture toxicity** relative to using LC50s derived from the actual test population, except when zinc predominated.
- Despite this discrepancy, the authors argue "standard" values remain practically useful for field-level pollution risk assessment on unknown trout populations, though results will be conservative (overestimate risk) except in zinc-dominated systems, where risk would be **underestimated**.

### Broader Implications
- Validates the core assumption underlying the [[Additive Toxicity Model]] (fractional toxicity summation) for predicting the lethality of pollutant mixtures in rivers under realistic, time-varying concentration regimes — **as long as fluctuation period < resistance time** of the specific poison.
- Identifies **zinc as an exception**, exhibiting antagonistic rather than additive behavior when it dominates a mixture's toxic load — an important caveat for regulatory water-quality models relying on simple additive frameworks.
- Reinforces that inter-population variability in trout sensitivity (batch-to-batch LC50 differences) is a significant source of uncertainty in extrapolating laboratory toxicity data to field conditions.
- Connects to related work: [[Herbert And Shurben 1964]], [[Lloyd 1960]], [[Lloyd And Jordan 1963]], establishing a continuous research program on mixture toxicology in salmonids at the Water Pollution Research Laboratory, Stevenage.