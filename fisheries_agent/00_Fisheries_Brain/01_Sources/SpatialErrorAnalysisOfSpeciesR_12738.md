---
species: "Aplodontia rufa; Peromyscus maniculatus; Tamias amoenus; Ammospermophilus leucurus; Glaucomys sabrinus; Dipodomys californicus; Neotoma lepida; Phenacomys intermedius; Microtus richardsoni; Lemmiscus curtatus"
common_name: "Mountain beaver; Deer mouse; Yellow-pine chipmunk; White-tailed antelope squirrel; Northern flying squirrel; California kangaroo rat; Desert woodrat; Heather vole; Water vole; Sagebrush vole"
family: "N/A"
habitat: "Vegetation polygons across three physiographic provinces of Oregon (East Slope Cascades, Basin and Range, Owyhee Uplands)"
ocean_basin: "N/A"
location: "Oregon, USA"
tags: [ichthyology, marine-biology, gap-analysis, species-richness, gis-error-modeling, rodents]
title: "Spatial error analysis of species richness for a gap analysis map"
source_id: "12738"
minckley_id: "12738"
source_citation: "D. J. Dean, K. R. Wilson and C. H. Flather (1997). Spatial error analysis of species richness for a gap analysis map. Photogrammetric Engineering and Remote Sensing 63(10): 1211-1218. Minckley Library ID: 12738."
source_file: "12738.pdf"
text_extraction: "ocr"
---
# Spatial Error Analysis of Species Richness for a Gap Analysis Map

#ichthyology #marine-biology #rodentia

## Executive Summary

This study uses [[Monte Carlo Simulation]] to test how errors of omission and commission in the [[Gap Analysis Project]] database for Oregon alter the spatial distribution of [[Species Richness]]. Two error types were simulated at rates of 5 and 20 percent: random errors, assumed independent of species distribution, and boundary errors, confined to the edges of each species' range. A subset of ten rodent species and three physiographic provinces was analysed. Random error changed the area of richness classes substantially, while boundary error changed them much less. The authors conclude that [[Error Modeling]] is essential for spatially explicit conservation recommendations derived from GIS databases.

## Background & Description

The paper is a research article in *Photogrammetric Engineering & Remote Sensing* (Vol. 63, No. 10, October 1997), by Denis J. Dean, Kenneth R. Wilson and Curtis H. Flather of Colorado State University and the USDA Forest Service.

Gap Analysis is a layer-based GIS strategy for conserving biological diversity. Its standard steps are:

1. Building a vegetation map from [[Landsat Thematic Mapper]] imagery and other data.
2. Building species distribution maps from range maps, distributional data and [[Habitat Relationship Models]].
3. Combining these layers to find underrepresented habitats and species within existing biodiversity management areas.

The key product is a species richness map, overlaid with land-management and ownership layers to identify "gaps" in protection of species-rich areas.

The authors note that few habitat-relationship models have been formally evaluated. A [[California Condor]] model was reported as robust to input uncertainty, whereas Block et al. (1994) found prediction-to-residency agreement of only 48 to 78 percent for amphibians, reptiles, birds and small mammals in California. Omission errors there ranged from 6 to 39 percent and commission errors from 20 to 44 percent.

## Ecological & Environmental Context

The Oregon GAP database used in the study was built from a digital [[Vegetation Map]] of over 12,000 polygons, [[Physiographic Provinces]] (after Puchy and Marshall, 1993), political boundaries, and habitat-relationship information for over 800 wildlife species. Species presence or absence in each polygon was derived from these layers. Richness was then summed per polygon.

Errors were defined as follows:
- **Omission:** a species is present in a polygon but the procedure predicts absence.
- **Commission:** a species is absent from a polygon but the procedure predicts presence.

The Oregon data were treated as "truth." The study was limited to three physiographic provinces (about 89,195 km², 3,238 polygons). In the original map, 93 percent of the area had richness of 0 to 4, 7 percent (6,291 km²) had richness of 5 or 6, and no polygon exceeded 7.

Random error was applied to any polygon without regard to species range, with errors such as vegetation-mapping inaccuracies as the example. Boundary error was restricted to a band around each species' range edge. The band was defined by contracting the range to 90 percent of its area for omission, and expanding it by the same amount for commission.

## Key Findings

- **Random error has a much larger effect than boundary error.** At 5 percent random error, area in richness classes 0, 1 and 4 fell by 21 to 30 percent, while classes 2, 3, 5 and 6 rose by 35 to 158 percent. At 20 percent, decreases ranged from 50 to 72 percent and increases from 57 to 506 percent.
- **Boundary error produced smaller shifts.** At 5 percent, changes ranged from a 1 to 21 percent decrease to an 8 percent increase at most. At 20 percent, decreases ranged from 4 to 25 percent and increases from 16 to 29 percent.
- **Variability in area was much lower under boundary error.** For richness of 4, the coefficient of variation was 5.7 percent (5 percent random) and 10.1 percent (20 percent random), compared with 0.34 percent and 1.20 percent for boundary error. For richness of 5, values were 13.8 and 12.3 percent for random error and 0.18 and 0.65 percent for boundary error.
- **Map accuracy was low under the error model.** The expected error matrix gave overall theoretical map accuracy of 63 percent at 5 percent error and 28 percent at 20 percent error. Omission errors reached 40 to 83 percent and commission errors 12 to 95 percent across the two tables.
- **Hot-spot areas are sensitive.** Under boundary error, the 6,291 km² of richness 5 or greater could shift by about ±1,300 km². Focusing on the affected 1,300 km² gave a 9 percent decline (118 km²) at 5 percent error and 33 percent decline (428 km²) at 20 percent error. The authors warn that ignoring these errors could direct preliminary surveys to many incorrect areas.
- **Error rates are plausible.** The 5 and 20 percent rates are consistent with published values (Block et al., 1994; Edwards et al., 1996) and may be conservative.
- **Set-coverage methods may be more vulnerable.** The authors hypothesise that [[Set-Coverage Analysis]] may be more sensitive to errors, because it may approximate random error more closely. This was not tested.
- **Full-database effects would likely be larger.** Using all 800 species would allow error to propagate through many more layers, so the effects would probably increase.
- **Recommendation.** Error modeling or sensitivity-analysis capability should be built into Gap Analysis. Without it, users cannot judge the uncertainty of their results.

**Method details:** 50 Monte Carlo iterations were run for each of four simulations (two error types by two rates). Results were reported as area per richness class rather than by an arbitrary "hot spot" threshold. Ten rodent species were selected from the 800 available, based on taxonomic similarity and computational constraints.