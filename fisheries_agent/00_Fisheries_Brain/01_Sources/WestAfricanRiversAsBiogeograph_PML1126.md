---
species:
  - "Multiple species (fish communities of 39 West African rivers and 11 tributaries; species not individually named)"
common_name: "West African river fish communities (multiple species)"
family: "N/A"
habitat: "Freshwater rivers and tributaries (catchments, lacustrine and riverine systems)"
ocean_basin: "Atlantic (West African coast)"
location: "West Africa: Senegal to Zaire river drainages, including Niger, Volta, Sassandra, and Bandama basins"
tags: [ichthyology, freshwater-fish, biogeography, species-area-relationship, west-africa, insular-biogeography, ridge-regression]
title: "West African rivers as biogeographic islands: species richness of fish communities"
source_id: "PML1126"
marsh_id: "PML1126"
library: "Marsh Library"
permission: "not public domain"
source_citation: "B. Hugueny (1989). West African rivers as biogeographic islands: species richness of fish communities. Oecologia 79: 236-243. Marsh Library ID: PML1126."
source_file: "Hughueny B. 1989. West african rivers as biogeographic islands species richness of fish communities.pdf"
text_extraction: "text"
---
# Species Richness of West African River Fish Communities as Biogeographic Islands

#ichthyology #marine-biology #freshwater-fish #species-richness #biogeography

## Executive Summary

This study by [[Bernard Hugueny]] tests whether West African rivers behave as [[Insular Biogeography|biogeographic islands]] for fish. Using 39 rivers along the West African coast from the Senegal to the Zaire, the author models fish species richness against catchment surface area, mean annual discharge, vegetation diversity, and percentage forest cover. Species richness was positively related to catchment area through a power function with an exponent of 0.32. A predictive model using ln(surface area) and ln(discharge) explained 90% of the variance. Tributaries of major rivers had more species than the model predicted, which the author interprets as consistent with higher extinction rates in riverine habitats, a weaker isolation effect within river networks, and possible [[Pleistocene Forest Refuge Hypothesis|Pleistocene forest refuge]] effects.

## Background & Description

Species-area relationships are a central idea in [[Island Biogeography Theory]], which has been applied to mountaintops, caves, and forest fragments. Rivers are considered insular for freshwater fish because, unlike marine taxa, most fish cannot cross surrounding terrestrial habitat. Earlier African studies by [[Daget and Iltis]] (1965, 13 rivers, mostly Ivory Coast), [[Welcomme]] (1979, 25 rivers), and [[Livingstone et al.]] (1982) used catchment area or related measures as predictors.

Data for this study were drawn from ORSTOM ichthyological surveys, carried out over about 10 years for onchocerciasis-control programmes, together with published lists and museum collections (including the Muséum National d'Histoire Naturelle, Paris, and the Natural History Museum, London). Species that are primarily marine were excluded, and lacustrine species were counted where catchments contained lakes.

## Ecological & Environmental Context

- **Study sample:** 39 rivers (Table 1) and a separate set of 11 tributaries, in the drainage areas of the Niger, Volta, Sassandra, and Bandama, plus coastal rivers from Senegal to Zaire.
- **Variables measured:**
  - SR: species richness (from literature, reports, and collections).
  - S: catchment surface area (km²), measured from maps at 1:1,000,000.
  - DV: diversity of terrestrial vegetation types, calculated as a Shannon index using natural logarithms, based on [[White Vegetation Map of Africa]] (1983).
  - PF: percentage of drainage area covered by lowland rain forest and associated transition types.
  - AD: annual mean discharge (m³ s⁻¹), taken from gauging stations near river mouths over 1 to 66 years of records.
- **Statistical approach:** Multiple regression with [[Ridge Regression]] to handle collinearity, [[Variance Inflation Factor]] (VIF) diagnostics, forward stepwise selection, residual analysis (Draper and Smith sign test), and [[Moran's I]] to detect spatial autocorrelation of residuals.
- **Key relationships:** Surface area and discharge were strongly intercorrelated, because discharge was taken as surface area multiplied by precipitation.

## Key Findings

1. **Power-law species-area relationship:** The best fit was a power function on log-transformed data, with exponent z = 0.32. Residuals were randomly distributed and showed no spatial autocorrelation. The author states the z value falls within the 0.15–0.39 range reported by [[May 1975]] for insular systems.

2. **Predictive model:** Ridge regression and forward stepwise selection retained ln(discharge) and ln(surface area) as predictors of ln(species richness). Together they accounted for 90% of variance. The initial full multiple regression had a multiple correlation coefficient of 0.955 but a maximum VIF of 23.5, indicating strong collinearity. Forest percentage and vegetation diversity were dropped in the ridge analysis.

3. **Non-significant habitat diversity effect:** Vegetation diversity had negative coefficients under least squares, but became positive at ridge k values above about 0.2. The author concludes that the data did not confirm the habitat-diversity hypothesis, and that a more suitable diversity index is needed.

4. **Tributaries have more species than predicted:** The model underestimated species richness in 9 of 11 tributaries (sign test, the author reports a significant difference, W = 4.45, P < 0.05). The author interprets this as higher extinction rates in river systems and continuous gene flow within river networks, consistent with a lower insularity effect for tributaries.

5. **Spatial pattern of residuals:** Residuals showed significant positive spatial autocorrelation, forming three groups: (1) Gambia and Konkouré rivers; (2) rivers between eastern Ivory Coast and Benin; and (3) Cameroon, Gabon, and Zaire rivers. The Cameroon–Gabon–Zaire group was interpreted as consistent with Pleistocene forest refuges. The eastern Ivory Coast–Benin group was considered probably artificial, reflecting poor faunal knowledge of small western rivers.

6. **Tropical versus temperate comparison:** The z value (0.32) is higher than values reported for European rivers (about 0.19 to 0.24), which the author links to greater inter-habitat diversity in the tropics. The author notes that this explanation requires the discharge–surface area relationship to be similar across regions.

7. **Conclusion:** Rivers can be treated as biogeographic islands for fish, but the strength of insularity appears lower for tributaries. The author cautions that surface area is not directly measured, so the biological meaning of z is uncertain. Refuge explanations are only partly supported and require evaluation with phylogeny, distribution, and endemism data.

## References

- [[Hugueny 1989]], *Oecologia* 79: 236–243.