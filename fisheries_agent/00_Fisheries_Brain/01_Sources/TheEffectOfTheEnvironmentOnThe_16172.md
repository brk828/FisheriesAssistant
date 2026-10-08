---
species: "Rainbow trout (Oncorhynchus mykiss, referred to as Salmo gairdneri); comparative references to brown trout (Salmo trutta), minnow, chub, and bluegill"
family: "Salmonidae (primary test species); Cyprinidae and Centrarchidae (comparative species)"
habitat: "Freshwater rivers and streams; laboratory aquaria and river-cage bioassay systems"
ocean_basin: "N/A (freshwater riverine study; no marine/ocean basin relevance)"
source_id: "16172"
---

#ichthyology #marine-biology #ecotoxicology #salmonidae #water-pollution

## Executive Summary

This 1962 paper by Lloyd & Herbert (Water Pollution Research Laboratory, Stevenage) synthesizes laboratory and field research on how physicochemical properties of river water modulate the toxicity of pollutants to fish, principally [[Rainbow Trout]]. The authors distinguish between poisons exhibiting a "threshold" toxic concentration (e.g., ammonia, heavy metals, phenols) and those with no threshold (e.g., anionic detergents), and show that environmental variables—temperature, water hardness (calcium content), dissolved oxygen, and free carbon dioxide—systematically shift toxicity thresholds. A key mechanistic finding is that un-ionized ammonia and hydrogen cyanide toxicity are strongly pH- and temperature-dependent because only the un-ionized fraction is toxic. The paper also introduces an additive model for toxicity of poison mixtures (concentration addition of threshold fractions) and validates laboratory-derived predictions against a 40-day field bioassay using caged trout in a gasworks-effluent-polluted stream, achieving ~82.5% predictive agreement. The work has direct implications for setting safe effluent discharge standards.

## Background & Description

- **Test species and methods**: Toxicity bioassays typically used 10–25 individuals of a species (commonly [[Rainbow Trout]]) exposed to graded dilutions of a poison, recording survival time. Data were plotted as log(median survival time) vs. log(concentration), generating characteristic toxicity curves.
- **Threshold vs. non-threshold poisons**:
  - Poisons like [[Ammonia Toxicity]], heavy metals (copper, zinc, lead), and phenols show a sharply inflected curve — beyond a certain low time, survival curve becomes parallel to the time axis, defining a "threshold concentration" below which fish survive indefinitely.
  - Anionic detergents (synthetic surfactants) show a straight-line log-log relationship with no threshold, complicating "safe concentration" estimation via extrapolation.
- **Safe concentration definitions**: Two proposed approaches — (1) a concentration causing negligible mortality relative to natural background mortality over time, or (2) a concentration killing ≤5–10% of a sensitive species (e.g., trout) within 3 months, calibrated to dry-weather river flow conditions.
- **Chemical speciation effects**: Toxicity often depends on the un-ionized/free fraction of a poison rather than total concentration:
  - Lead nitrate can be rendered non-toxic via precipitation as insoluble basic salts in hard alkaline water.
  - Ammonium salt toxicity (un-ionized NH3 fraction) increases ~10-fold per pH unit rise (7.0→8.0) and ~2-fold per 10°C temperature rise.
  - Sodium nickelocyanide toxicity to bluegill increases ~500-fold as pH falls from 8.0 to 7.0, due to formation of highly toxic HCN from the cyanide complex (Doudoroff, 1956).
  - Potassium ferri-/ferrocyanide toxicity is enhanced by sunlight, which accelerates HCN release from complex decomposition.

## Ecological & Environmental Context

- **River/stream setting**: All experiments concern freshwater lotic systems, particularly rivers receiving effluents from gasworks, coke ovens, sewage works, and industrial trade wastes.
- **Natural fluctuations compounding pollution stress**: Dissolved oxygen in unpolluted rivers naturally fluctuates diurnally (lower at night), and oxygen-demanding effluents exacerbate this, indirectly increasing poison toxicity even without asphyxiation-level hypoxia.
- **Species sensitivity comparisons**: Discussion notes rainbow trout (non-native to UK) may be more sensitive to adverse conditions than native [[Brown Trout]], though data suggest only slight differences between the two salmonids relative to the safety margins ("application factors") used in setting discharge standards. Trout generally rank among the most sensitive aquatic organisms to pollution, though not always the single most sensitive species.
- **Non-toxic stressors**: Suspended solids (e.g., china-clay wastes) were not found to clog gills directly, though epithelial thickening was observed; reduced trout population density in china-clay-affected streams was attributed more to reduced food abundance and destroyed spawning grounds than direct gill damage.
- **Effluent-specific context**: Spent liquors from gas/coke ovens are toxic almost entirely due to ammonia and monohydric phenol content. Domestic sewage effluent, when well-nitrified, is rarely directly toxic; harm to fisheries from such effluent is more often due to dissolved-oxygen depletion in the receiving river, compounded by oxygen demand from aquatic vegetation respiration, benthic organic matter oxidation, and reduced reaeration in sluggish streams.

## Key Findings

### Temperature Effects
- Increased temperature generally decreases survival time (log-survival time vs. temperature often linear), attributed to increased metabolic rate; survival time changes by a factor of 2–3 per 10°C.
- Species-specific responses vary: [[Minnow]] showed a linear ammonia toxicity-temperature relationship (Wuhrmann & Woker, 1953), while [[Chub]] showed decreased survival time from 10–15°C but no further change from 15–25°C.
- For threshold-type poisons (e.g., zinc), the **threshold concentration itself appears largely unaffected by temperature**, though survival time in supra-threshold concentrations is temperature-dependent. Thresholds for un-ionized ammonia and phenols are also little altered by temperature within physiological ranges.

### Water Hardness (Calcium) Effects
- Calcium content primarily affects toxicity of heavy metal salts (zinc, lead, copper) to [[Rainbow Trout]].
- A linear relationship exists between log(threshold concentration) and log(total hardness), but slopes differ among the three metals, so no universal correction factor applies across heavy metals.
- Lead nitrate data were limited to soft waters only, since in harder/more alkaline waters insufficient lead remained in solution to be lethal.

### Dissolved Oxygen Effects
- Reduced dissolved oxygen (even at sub-lethal levels) increases toxicity of zinc, lead, copper, and monohydric phenols.
- The toxicity increase factor (Xs/X, ratio of threshold at air-saturation to threshold at reduced oxygen) was similar across these four poison classes, suggesting a common mechanism.
- **Proposed mechanism**: Trout increase gill ventilation (water flow over gills) as oxygen concentration decreases, increasing poison uptake at the gill absorption site.
- Ammonia toxicity is an exception to this general oxygen-toxicity relationship due to interacting CO2 dynamics (see below).
- Discussion noted that a drop to ~40% air saturation reduced the zinc threshold by only ~30%, suggesting practical significance is real but moderate.

### Free Carbon Dioxide & Ammonia Interaction
- Increasing free CO2 lowers water pH, reducing the un-ionized (toxic) ammonia fraction — reducing overall ammonia toxicity up to the point where CO2 itself becomes lethal.
- However, even after correcting for bulk pH effects on ionization, **elevated CO2 still independently lowers the threshold for un-ionized ammonia** — attributed to fish excreting CO2 at the gill surface, locally lowering pH there and altering un-ionized ammonia concentration at the site of absorption differently than in bulk solution.
- This gill-surface microenvironment effect was modeled theoretically from [[Rainbow Trout]] respiratory physiology and fit well to experimental data.
- Interaction with dissolved oxygen: since CO2 excretion depends on oxygen consumption/ventilation rate, the Xs/X factor for ammonia under varying oxygen levels differs from other poisons at different free-CO2 levels; theoretical curves matched experimental points closely.
- Integrated graphical models were developed allowing prediction of ammonia toxicity thresholds for rainbow trout from temperature, alkalinity, pH, free CO2, and dissolved oxygen, with predictions typically within ±12% of experimental thresholds.

### Toxicity of Poison Mixtures
- Three poison pairs investigated: zinc + copper, ammonia + phenols, and ammonia + zinc.
- **Concentration addition model**: When each poison's concentration is expressed as a fraction of its individual threshold, the mixture reaches its own threshold when the sum of fractions equals 1 (i.e., simple additive toxicity).
- Example: Zinc and ammonia each at 50% of their individual thresholds, when combined, produced ~50% mortality (equivalent to reaching combined threshold), rather than the negligible mortality expected from either alone.

### Field Validation (Gasworks Effluent Study)
- Rainbow trout were caged in a stream polluted with spent gasworks liquor for 40 days; river water sampled every 2 hours for ammonia, phenol, dissolved oxygen, temperature, and pH.
- Laboratory-derived threshold models (based on ammonia + phenol mixture toxicity, adjusted for oxygen/pH/temperature) were used to predict daily fish survival/death.
- Predictions agreed with actual field outcomes on 33 of 40 days (82.5% agreement), supporting the practical utility of the laboratory-derived toxicity models for real river conditions, despite sampling-interval limitations (2-hour gaps could miss brief acute toxic excursions).

### Practical/Regulatory Implications
- Well-nitrified domestic sewage effluent is rarely directly toxic; risk to fisheries is primarily via dissolved-oxygen depletion, which can result from combined effects of effluent oxygen demand, aquatic plant respiration, benthic oxidation, and reduced reaeration — factors that can synergize to create dangerous conditions even when no single factor alone would.
- Non-nitrified sewage effluents may contain ammonia concentrations up to 30 ppm plus industrial trade waste contaminants, motivating further research into sewage-effluent toxicity as a function of trade waste input.
- The authors advocate mechanistic, physiologically grounded explanations (e.g., gill ventilation rate, ionization equilibria) over purely empirical curve-fitting, since mechanistic models allow extrapolation to untested conditions and generalization across poison classes (e.g., predicting that any stimulus increasing gill ventilation rate would likely increase susceptibility to other poisons).