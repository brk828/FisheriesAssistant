---
species: "Macropus giganteus; Macropus fuliginosus; Macropus rufus"
common_name: "Eastern Grey Kangaroo; Western Grey Kangaroo; Red Kangaroo"
family: "Macropodidae"
habitat: "Terrestrial; climatically defined rangelands, woodlands and arid areas of Australia"
ocean_basin: "N/A"
location: "Australia"
tags: [ichthyology-exempt, macropod, kangaroo, species-distribution-modelling, gis, climate-envelope, australia]
title: "Modelling wildlife distributions using a geographic information system: Kangaroos in relation to climate"
source_id: "14840"
minckley_id: "14840"
source_citation: "P. A. Walker (1990). Modelling wildlife distributions using a geographic information system: Kangaroos in relation to climate. Journal of Biogeography 17(3): 279-289. Minckley Library ID: 14840."
source_file: "14840.pdf"
text_extraction: "ocr"
---
# Modelling Wildlife Distributions Using a Geographic Information System: Kangaroos in Relation to Climate

#ichthyology #marine-biology #macropodidae

*Note: The source concerns terrestrial marsupials, not fish. The tag line above follows the required format; the taxon tag is Macropodidae.*

## Executive Summary

Walker (1990, *Journal of Biogeography* 17: 279–289) describes how the areal distributions of three kangaroo species (*Macropus* spp.) in Australia can be re-expressed in terms of climatic characteristics using [[SIMPLE]], a spatial and inductive modelling system that couples a [[Geographic Information System]] with statistical and rule-induction packages. Two modelling strategies were compared: [[Classification and Regression Trees]] (CART), which produce decision rules, and [[Logistic Regression]] (fitted in [[GLIM]]), which produces probability surfaces. The paper is presented primarily as a demonstration of a tool rather than as a definitive habitat assessment. It builds on the climatic-envelope analysis of [[Caughley et al. 1987]].

## Background & Description

- **Study species:** The three largest members of Macropodoidea: [[Eastern Grey Kangaroo]] (*Macropus giganteus*), [[Western Grey Kangaroo]] (*M. fuliginosus*) and [[Red Kangaroo]] (*M. rufus*).
- **Prior work:** Caughley et al. (1987b) used discriminant analysis to define the climatic envelope of each species and locate unoccupied areas within it. Caughley et al. (1987b) also proposed that no species lives north of 14° latitude, owing to heat and moisture limits.
- **Aim of this paper:** To illustrate two modelling options within a GIS, not to redefine the task or recommend a technique. Model accuracy in replicating observed distributions is reported.
- **Data source:** Grid-cell distribution and climate data originally established by Caughley et al. (1987b), largely from aerial surveys carried out between 1980 and 1982, translated into [[MAP]] overlays by the author.

## Ecological & Environmental Context

- **Deductive versus inductive modelling:** Standard GIS software can map species and attributes and apply known relationships (deduction), but it lacks capacity to discover spatially varying relationships (induction). The paper frames the climate–distribution problem as an inductive task.
- **Climatic correlates:** Caughley et al. (1987b) suggested that eastern greys are limited by heat, red kangaroos by excess moisture, and western greys by hot summers combined with dry winters.
- **Data set:** Each grid cell is one degree of latitude by one degree of longitude. Each overlay holds 1530 cells (34 rows × 45 columns), of which 686 cover the continent. Twelve climate attributes were used, including annual mean temperature, maximum temperature of the hottest month, annual and seasonal precipitation, and temperature and precipitation of the wettest and driest quarters.
- **Study area limits:** Presence records exist for 482 cells with at least one species; one degree block was excluded because of database revisions.
- **Regional patterns noted:** Models identified a climatic envelope in west and central Australia for eastern greys, a winter-rainfall area in agricultural Victoria with lower kangaroo density, a suitable but unrecorded area in Western Australia, and clay soils in semi-arid woodland as favourable for western greys.

## Key Findings

**Dataset composition**
- Single-species cells: red 204, western grey 56, eastern grey 90.
- Two-species cells: red and western grey 39, eastern grey and red 46, eastern grey and western grey 5.
- All three species present: 42 cells.

**Latitude–longitude CART models**
- Eastern grey: over 96% of presence cells lie east of 142° E; combined error rate 4.8% (2.7% false absences, 5.6% false presences).
- Western grey: over 78% of presence cells lie south of 30° S and west of 146° E.
- Red: only 54% of presence cells correctly classified; two candidate regions identified.

**Climate CART models (error rates)**
- Eastern grey: 2.3% overall (1.5% of presences and 2.6% of absences misclassified).
- Western grey: 3.8% overall (0.7% of presences and 4.6% of absences misclassified).
- Red: 13.3% overall (5.4% of presences and 20.6% of absences misclassified).
- All species combined: 12% error; 13 main rules correctly classified 85% of locations.
- Most significant attributes: precipitation of the driest month and driest quarter (eastern grey); driest-quarter precipitation and annual mean temperature (western grey); annual precipitation and wettest-month precipitation (red).
- Example rules: western grey presence where annual mean temperature is below 18.7° and driest-quarter precipitation is below 86.7 mm (correctly labels 65% of presences, 8% misclassification of cases the rule applies to).

**Climate GLIM logit models**
- Eastern grey: driest-month precipitation, wettest-quarter mean temperature and driest-quarter precipitation; significant at the 0.1% level.
- Western grey: wettest-quarter temperature, annual mean precipitation, annual mean temperature and annual precipitation range; significant at the 0.001% level.
- Red: annual mean precipitation and driest-quarter mean temperature; significant at the 0.01% level.
- Thresholding p at 0.3: eastern grey 97% of absences and 85% of presences correct; western grey 87% and 79%; red 46% of absences and 95% of presences.

**Comparison of methods**
- Both methods identified the same west and central Australian area as climatically suitable for eastern greys, but the logit model predicted a larger area of unrealised occupancy.
- CART correctly predicted absence of red kangaroos in north-west and central Australia, whereas the logit model predicted presence there with p above 0.6.
- Of CART-predicted eastern grey locations, over 56% had logit p above 0.8; of CART-predicted absences, 88% had p below 0.19.

**Methodological conclusions**
- CART advantages: isolates local interactions, tolerates outliers, and yields readily interpretable rules. Disadvantages: sensitivity of tree structure to small changes in the learning sample, and difficulty choosing a correctly sized tree.
- GLM advantages: binomial error structure suits presence/absence data, and output is a probability surface. Limitation: logistic regression cannot model combinations of species directly.
- Suggested extensions: add vegetation, land tenure and land use as binary attributes, and restrict the learning sample to the climate envelope of presence records to separate interpolation from extrapolation.

**Overall conclusion**
- SIMPLE provides an integrated environment for developing and testing hypotheses about spatially varying relationships, and could be applied to habitat definition tasks beyond kangaroos. The author emphasises that the paper is about modelling workflow and tool design rather than definitive kangaroo habitat statements.