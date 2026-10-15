---
species:
  - Gila pandora
  - Pantosteus plebeius
common_name:
  - Rio Grande Chub
  - Rio Grande Sucker
family:
  - Leuciscidae
  - Catostomidae
habitat: Freshwater streams, small to medium-sized dryland streams, pools, riffles, runs
ocean_basin: N/A
location: Rio Grande basin, Colorado, New Mexico, United States
tags:
  - conservation
  - habitat-suitability
  - occupancy-modeling
  - random-forest
  - threatened-species
  - nonnative-species
  - stream-ecology
title: "Site- and landscape-scale estimates of ecological suitability inform desert fish conservation"
source_id: "X-365e2fb8"
source_citation: "R. J. Friebertshauser, K. R. Bestgen (2026). Site- and landscape-scale estimates of ecological suitability inform desert fish conservation. Transactions of the American Fisheries Society."
doi: "10.1093/tafafs/vnag031"
source_file: "Friebertshauser and Bestgen 2026.pdf"
text_extraction: "text"
---
# Site- and Landscape-Scale Estimates of Ecological Suitability Inform Desert Fish Conservation

#ichthyology #freshwater-ecology #Leuciscidae #Catostomidae #conservation-biology #habitat-modeling

## Executive Summary

This comprehensive study assessed ecological suitability for two imperiled Rio Grande basin fishes—[[Rio Grande Chub]] (*Gila pandora*) and [[Rio Grande Sucker]] (*Pantosteus plebeius*)—using dual modeling approaches across their overlapping ranges in Colorado and New Mexico. Researchers conducted fish community surveys and habitat assessments at 112 sites between 2022–2023, capturing 16,491 individual fish representing 25 species. Site-scale multispecies occupancy models identified water temperature, pool characteristics (for chub), and riffle quantity (negatively for sucker) as key habitat associations, while landscape-scale random forest models revealed that modeled mean August stream temperature and watershed position (upstream drainage area, Strahler order) were primary predictors of presence. Both species showed positive associations with warmer, small- to medium-sized streams. [[Rio Grande Chub]] occupancy was modestly reduced by [[Brown Trout]] (*Salmo trutta*) presence. Spatial predictions identified 7,607 km of suitable habitat for Rio Grande Chub and 5,732 km for Rio Grande Sucker, with the greatest linear extent occurring in north-central New Mexico's Rio Grande/Elephant Butte basin, though proportionally higher suitability occurred in southern portions of the study area.

## Background & Description

[[Rio Grande Chub]] (family: [[Leuciscidae]], formerly Cyprinidae) were historically abundant throughout the [[Rio Grande]] and [[Pecos River]] basins and the [[San Luis Valley Closed Basin]] in Colorado and New Mexico, with a single population in Texas. [[Rio Grande Sucker]] (family: [[Catostomidae]]) once ranged from southern Colorado to Chihuahua, Mexico, occupying the Rio Grande basin, San Luis Valley Closed Basin, [[Mimbres River]], and multiple drainages in the Sierra Madre Occidental. Both species have experienced significant declines resulting in state conservation designations in Colorado and New Mexico. Threats include habitat degradation, nonnative [[Brown Trout]] and [[White Sucker]] (*Catostomus commersonii*), consumptive water use, wildfire, and climate change.

The study area encompassed three HUC4 basins: Rio Grande headwaters (HUC4: 1301), Rio Grande/Elephant Butte (HUC4: 1302), and Rio Grande/Mimbres (HUC4: 1303). Survey sites ranged from 1,437 to 3,197 m elevation and spanned 32.94°N to 38.36°N latitude. Sites were selected using generalized random-tessellation stratified design along environmental gradients, with 52 sites in Rio Grande Headwaters, 61 in Rio Grande/Elephant Butte, and 7 in Rio Grande/Mimbres basins.

Fish communities were surveyed using two-pass backpack electrofishing at 112 sites. Site lengths approximated 20× mean wetted channel width (minimum 50 m, maximum 150 m) and included at least three riffle, run, and pool mesohabitats. Habitat assessments measured physiochemical parameters across 10 equally spaced transects (50 points total) including substrate composition (Wentworth scale), mesohabitat percentages, water temperature, turbidity, pool depth, and woody debris cover. Shannon diversity indices quantified substrate and mesohabitat heterogeneity.

## Ecological & Environmental Context

Native fishes comprised 8 species (62% of 16,491 total fish captured, n=10,151 individuals) detected at 84 of 112 locations. Nonnative taxa represented 17 species (38%, n=6,340) detected at 99 sites. [[Brown Trout]] and [[White Sucker]] were most common nonnatives, detected at 59 (53%) and 56 (50%) locations respectively. Three [[Rio Grande Chub]] × [[Longnose Dace]] (*Rhinichthys cataractae*) hybrids were detected at three locations (79, 155, 177 mm total length).

[[Rio Grande Chub]] were detected at 51 of 110 sites (46%): 17 in Rio Grande headwaters, 30 in Rio Grande/Elephant Butte, 4 in Rio Grande/Mimbres. Reproductive populations (based on juvenile presence) occurred in main-stem Rio Grande but not Rio Chama. Rio Grande Chub and Brown Trout co-occurred at 34 of 110 sites (30%).

[[Rio Grande Sucker]] were captured at 41 of 112 sites (37%): 11 in Rio Grande headwaters, 26 in Rio Grande/Elephant Butte, 4 in Rio Grande/Mimbres. None were collected from Rio Grande or Rio Chama main stems. Rio Grande Sucker co-occurred with Brown Trout at 26 of 112 sites (23%) and with White Sucker at 14 of 112 sites (12%).

The Rio Grande basin is predominantly arid or semiarid, with increasing diversions, dams, and groundwater pumping threatening flow stability. Species endemism is high in southwestern streams where water scarcity disproportionately impacts native fishes.

## Key Findings

**Site-Scale Occupancy Modeling (Multispecies Occupancy Models, n=93 sites for chub, n=92 for sucker):**

*Rio Grande Chub:*
- Water temperature positively associated with occupancy: β=0.18 (95% CI [0.08, 0.28]). Occupancy probabilities at 7.8°C, 14.4°C, 21.0°C were 0.32, 0.61, 0.84 respectively
- Pool percentage positively associated: β=0.030 (95% CI [-0.010, 0.080]). Occupancy at 15.4%, 30.7%, 46.1% pool habitat: 0.43, 0.55, 0.65 with nonnative trout present; 0.53, 0.65, 0.76 without trout
- Average pool depth positively associated: β=0.012 (95% CI [-0.0060, 0.30]). Occupancy at 30, 60, 90 cm depths: 0.49, 0.58, 0.67
- Nonnative trout occupancy negatively associated: β=-0.35 (95% CI [-1.30, 0.59]). Occupancy 0.45 with trout present vs. 0.54 without (at mean covariate values)
- Interactive effect: pool percentage mediated trout effect (β=-0.010, 95% CI [-0.060, 0.30])
- Detection probability: 95.4% (95% CI [88.1, 98.3])

*Rio Grande Sucker:*
- Water temperature positively associated: β=0.22 (95% CI [0.11, 0.34]). Occupancy at 7.8°C, 14.4°C, 21.0°C: 0.15, 0.46, 0.78
- Riffle percentage negatively associated: β=-0.030 (95% CI [-0.070, 0.00]). Occupancy at 16.7%, 33.3%, 49.9% riffle: 0.44, 0.30, 0.20
- No significant associations with nonnative trout or White Sucker occupancy
- Detection probability: 89.8% (95% CI [79.7, 95.3])

**Landscape-Scale Random Forest Models (n=110 sites for chub, n=109 for sucker):**

*Model Performance:*
- Rio Grande Chub: accuracy 0.91, sensitivity 0.92, specificity 0.90, AUC 0.94 (testing set)
- Rio Grande Sucker: accuracy 0.82, sensitivity 0.82, specificity 0.82, AUC 0.94 (testing set)
- Bootstrapped iterations (n=500) showed mean accuracy 0.73 (chub) and 0.72 (sucker)

*Most Important Predictors (Rio Grande Chub):*
1. Modeled mean August stream temperature (NorWeST): positive 14-17°C, declining above 17°C
2. Upstream drainage area: low probability >500 km² (larger, lower-drainage streams)
3. Mean annual diurnal air temperature range: low probability at <17°C or >19°C

*Most Important Predictors (Rio Grande Sucker):*
1. Modeled mean August stream temperature: positive relationship, optimum ~20°C
2. Upstream drainage area: similar pattern to chub
3. Strahler order: high probability limited to lower-order streams
4. Mean annual diurnal air temperature range: highest probability at smaller fluctuations, declining dramatically around 16.5°C

**Spatial Predictions of Suitable Habitat:**

*Rio Grande Chub (20,584 km total stream length analyzed):*
- 7,607 km (36.9%) predicted suitable (probability ≥0.5)
- By basin: Rio Grande/Mimbres 71.6% (842 km), Rio Grande/Elephant Butte 45.3% (5,710 km), Rio Grande headwaters 15.5% (1,055 km)
- High suitability (≥0.75): 1,705 km
- Elevation range: 1,328-2,567 m; Strahler orders 1-8
- Removing extrapolative predictions: 3,945 km suitable of 8,122 km analyzed

*Rio Grande Sucker (21,195 km total):*
- 5,732 km (27.0%) predicted suitable
- By basin: Rio Grande/Mimbres 62.7% (1,121 km), Rio Grande/Elephant Butte 33.3% (4,197 km), Rio Grande headwaters 6.1% (414 km)
- High suitability (≥0.75): 111 km (none in headwaters)
- Elevation range: 1,148-2,783 m; Strahler orders 2-6
- Removing extrapolative predictions: 2,666 km suitable of 8,081 km analyzed

**Conservation Implications:**

Greatest linear extent of suitable habitat for both species occurred in north-central New Mexico (Rio Grande/Elephant Butte basin), particularly the [[Jemez River]] basin (HUC8: 13020202): 640 km for Rio Grande Chub, 673 km for Rio Grande Sucker. Proportionally higher suitability occurred toward southern extent of range. Main-stem Rio Grande showed suitability for Rio Grande Chub in canyon-bound reaches upstream of Rio Chama confluence, supported by previous detections. Rio Grande Sucker showed decreasing presence in main-stem Rio Grande. Apparent extirpation of Rio Grande Chub from Rio Chama contrasts with historical surveys.

**Integrated Findings:**

Combining both approaches revealed that warmer, medium-sized streams void of Brown Trout with abundant deep pools are optimal for Rio Grande Chub, while Rio Grande Sucker prefer small, warm streams not dominated by riffles. Site-scale assessments identified local habitat characteristics (mesohabitat, biotic interactions) for restoration and repatriation site selection. Landscape-scale predictions prioritized conservation regions and identified streams for future surveys. Thermal relationships showed positive associations with temperature at both scales, with random forest models suggesting apparent optima (~18°C chub, ~20°C sucker) while occupancy models documented presence at extremes (5.1-27.6°C observed). Upper thermal tolerance limits require experimental determination.