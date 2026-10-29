---
species: N/A
common_name: N/A
family: N/A
habitat: Chaparral, pine forest, desert scrub (wildland fire landscapes)
ocean_basin: N/A
location: Idyllwild 7.5-minute quadrangle, San Jacinto Ranger District, San Bernardino National Forest, southern California, U.S.A.
tags: [wildfire, GIS, fire-ecology, spatial-analysis, prescribed-burning, southern-california]
title: "Management of wildfires with a geographical information system"
source_id: "16145"
minckley_id: "16145"
source_citation: "Y. H. Chou (1992). Management of wildfires with a geographical information system. International Journal of Geographical Information Systems 6(2): 123 - 140. Minckley Library ID: 16145."
source_file: "16145.pdf"
text_extraction: "ocr"
---
# Wildfire Management with a Geographical Information System

#ichthyology #marine-biology #wildfire-management

## Executive Summary

This 1992 study by Yue Hong Chou (University of California, Riverside) presents a [[Geographical Information System]] (GIS) method for wildfire managers. The method builds a logistic probability model of fire occurrence from topography, vegetation, temperature, precipitation, proximity to buildings and proximity to roads, applied to the Idyllwild 7.5-minute quadrangle in southern California. It delineates critical zones needing suppression and compares two hypothetical [[Prescribed Burning]] strategies using a district fire danger index (DFDI) and [[Moran's I]] spatial autocorrelation. The document is a research article, not a fish or aquatic study; no aquatic species, water-body or invertebrate data are reported.

## Background & Description

- **Context:** Wildfires threaten natural resources, endangered species, property and lives. Early [[Fire Suppression Policy]] (U.S. Forest Service, 1905; California Department of Forestry, 1924) aimed at near-total exclusion of fire.
- **Critique of suppression:** Comparison of San Diego County (strict control) with northern Baja California (no management) suggested suppression reduced fire numbers but not total acreage burned, because fuels accumulated and produced later fires of unnatural size and intensity (Minnich 1983, 1987, 1989).
- **Modern approach:** Based on [[Fire Ecology]], fires are treated as a natural part of ecosystem steady state. Suppression is reserved for fires threatening property, resources, endangered species or lives; other fires may be left to burn out or used via prescribed burning.
- **Study area:** The Idyllwild quadrangle has a well-recorded fire history (1911–1984). Vegetation is dominated by [[Chaparral]] on steep terrain, with pine forest at high elevations and basin floors, and open desert scrub on the arid margin. Ownership includes National Forest, private holdings and Indian reservations.
- **Database:** Jointly built by the University of California, Riverside and the Pacific Southwest Forest and Range Experiment Station's Riverside Forest Fire Laboratory, using [[ARC/INFO]].

## Ecological & Environmental Context

**Data layers (Table 1):**

| Coverage | Variables extracted |
|---|---|
| Fire activity | Burned areas |
| Topography | Slope gradient and aspect |
| Temperature | Maximum July temperature |
| Precipitation | Annual precipitation |
| Vegetation | Vegetation types |
| Structures | Buildings and camping sites |
| Transportation | Roads and trails |

**Key derived variables:**
- **Geographical units:** Polygons (triangulated irregular networks) classed into 9 aspect classes (8 octants plus flat) and 6 slope-gradient classes (0–50° at 10° intervals, plus >50°). Polygons were preferred over grid cells to keep natural variable boundaries and to handle mixed nominal and ratio scales.
- **Vegetation:** 1:20,000 aerial photographs; 24 species reclassified into eight fuel-model categories (six vegetation types plus water and bare ground). Each received a [[Fire Rotation]] weight (Table 2), ranging from 0.0 (bare ground, water) to 1.0 (dense chaparral, firs, oaks, open pine) with 0.25 for open chaparral and 0.5 for wet meadow. The area-weighted average forms the ROTAT variable.
- **Temperature (TEMP):** Mean July maximum temperatures, with stations roughly 3 °C above altitude-corrected ambient values due to superheating.
- **Precipitation (RAIN):** Contoured from weather-station data, with interpolation for unsampled areas using rain-shadow and windward-slope assumptions (winter storms from 250–220° winds).
- **Proximity:** BUILD (buffer zones at 500 m intervals from buildings and camps) and ROAD (Euclidean distance from unit centroid to nearest road).

## Key Findings

**Probability model (Equations 2–3):**
- A logistic model estimates the probability of burning for each unit, with U as the linear predictor of AREA, ASPCT, SLOPE, ROAD, BUILD, ROTAT, RAIN and TEMP.
- Coefficients came from stepwise logistic regression (BMDP PLR), with a deliberately loose entry criterion. Forecasting accuracy was "nearly 70 per cent."
- Table 3 coefficients, as reported: RAIN −0.0968 (p = 0.0724); ROTAT −1.5900 (p = 0.0000); ASPCT −0.0053 (p = 0.0001); AREA p = 0.0000; TEMP 0.1241 (p = 0.0999); SLOPE 0.0409 (p = 0.5240); BUILD −0.0248 (p = 0.2228); ROAD p = 0.0017.

**Critical zones:**
- The probability map uses five classes at 20% intervals.
- Critical zones are defined as units within 500 m of a building with a fire probability above 80% (Figure 11). Suppression is required immediately if a fire starts in these zones.

**Prescribed burning strategies (Figure 12):**
- Two arbitrary, illustrative proposals each burn four units. Strategy 1 burns 1,085,326 m² and Strategy 2 burns 847,663 m². Because cost scales with area, Strategy 1 is more expensive.
- **DFDI** (Equation 4): The original district average is 0.45. Strategy 1 reduces it to 0.44 and Strategy 2 to 0.43, so the cheaper Strategy 2 is more effective.

**Moran's I (Equation 5) and spatial pattern:**
- Positive I means clustering, negative I means dispersion, and values near zero indicate randomness. A lower I is preferred for fire danger because it indicates scattered high-risk patches.
- Test grids: I = 0.947 (clustered), −1.000 (scattered), −0.168 (random).

| Example | Strategy | Moran's I | Z |
|---|---|---|---|
| Basic effects | 1 | 0.693 | 23.189 |
| Basic effects | 2 | 0.646 | 21.216 |
| First-order neighbourhood | 1 | 0.703 | 23.517 |
| First-order neighbourhood | 2 | 0.650 | 21.747 |

- Strategy 2 gives the lower I in both examples, so it again yields the more desirable pattern.

**Conclusions:**
- The primary aim is a GIS methodology for evaluating preventive and suppressive strategies. The paper does not argue for or against prescribed burning.
- Wildfire management is still needed to limit losses. Managers must distinguish fires that must be suppressed from those beneficial to ecosystems.
- Prescribed burns must follow a full-scale district plan. Otherwise they may create future fire-disaster conditions.
- Local winds and vegetation age were excluded owing to a lack of reliable data. The author notes these should be added once available.