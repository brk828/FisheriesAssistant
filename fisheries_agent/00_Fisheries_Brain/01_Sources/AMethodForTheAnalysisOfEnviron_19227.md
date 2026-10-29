---
species: ["Diaptomus oregonensis", "Diaptomus minutus", "Diaptomus leptopus", "Cyclops bicuspidatus", "Epischura lacustris", "Cyclops edax", "Senecella calanoides", "Bosmina longirostris", "Daphnia lacustris"]
common_name: "Zooplankton (calanoid and cyclopoid copepods, cladocerans); Carboxymethyltartronate (CMTT) for the detergent-builder fragment"
family: "Diaptomidae; Cyclopidae; Temoridae; Daphniidae; Bosminidae"
habitat: "Freshwater lakes; activated sludge (wastewater treatment)"
ocean_basin: "N/A"
location: "Experimental Lakes Area, northwestern Ontario, Canada"
tags: [limnology, community-ecology, zooplankton, copepoda, multivariate-statistics, pollution-monitoring]
title: "A method for the analysis of environmental factors controlling patterns of species composition in aquatic communities"
source_id: "19227"
minckley_id: "19227"
source_citation: "R. H. Green and G. L. Vascotto (1978). A method for the analysis of environmental factors controlling patterns of species composition in aquatic communities. Water Research 12(8): 583-590. Minckley Library ID: 19227."
source_file: "19227.pdf"
text_extraction: "ocr"
---
# A Method for the Analysis of Environmental Factors Controlling Patterns of Species Composition in Aquatic Communities

#zooplankton #copepoda #limnology

## Executive Summary

This methods paper by [[Roger H. Green]] and [[Gian L. Vascotto]] (University of Manitoba, 1978) reviews how aquatic ecologists can link spatial patterns of species composition to environmental variables. The authors critically assess [[Ordination]], [[Classification Analysis]] and [[Diversity Indices]], and recommend a two-step procedure: classify samples by their species assemblages, then test and display how those groups separate on environmental variables using [[Discriminant Analysis]]. The procedure is demonstrated on zooplankton from 34 lakes in northwestern Ontario, which fell into four assemblage groups that differed mainly in lake area and depth. A short fragment on a separate detergent-builder study, a microbial sludge test for a substitute for [[Nitrilotriacetate]], is also included, but only its abstract and introduction are present.

## Background & Description

The authors frame the problem as a "samples-by-taxa" matrix, with samples keyed to a study map and paired with measured environmental variables. They seek methods that (1) reduce species-abundance data efficiently and (2) relate the reduced biological data to environmental data so that the environment explains or predicts the biota.

Ordination methods reduce *p* species variables to *k < p* axes. The authors stress that linear models such as [[Principal Components Analysis]] and factor analysis are inappropriate for species that have unimodal responses along environmental gradients. This mismatch produces the [[Horseshoe Effect]], a curved pattern in ordination space that makes axes hard to interpret as environmental factors. Non-linear alternatives reviewed include [[Gaussian Ordination]] (limited to one dominant gradient) and [[Non-Metric Multidimensional Scaling]], which assumes only monotonic relationships but still does not fully remove the horseshoe.

Classification (cluster) analysis is appropriate when the population is assumed to consist of "partly-dissociated sub-populations," which the authors consider typical of aquatic communities in heterogeneous areas. Software options noted include SAS, NT-SYS, BASIC programs from Orloci (1975), and CLUSTAN, the last useful for testing whether clusters are robust across methods.

The authors are critical of [[Diversity Indices]]. They argue that diversity has no agreed definition, depends on seasonal, latitudinal and spatial factors, and is not reliably linked to pollution or environmental quality. They suggest that the number of species per sample (S) is a simpler and less ambiguous measure if one is needed for comparison.

Regression, canonical correlation and PCA, when they include both biotic and environmental variables, all assume linear relationships, which the authors consider unrealistic for species responses. They note that non-parametric monotonic methods, such as the Mantel test, may still be too restrictive.

The second fragment, on a detergent-builder study, concerns the restriction of sodium tripolyphosphate-type builders and the search for alternatives to NTA. It describes [[Carboxymethyltartronate]] (CMTT), a new large-volume builder with three carboxyl groups that bind Ca²⁺ and Mg²⁺ and whose molecule carries only sodium salts. The text notes the study's aim of evaluating biodegradation under sludge conditions and cites earlier reports, but no results survive in the excerpt.

## Ecological & Environmental Context

The example uses data from [[Patalas 1971]], a survey of crustacean plankton in Experimental Lakes Area lakes. The biological data are abundances (individuals per cm³) of 27 zooplankton species in 34 lakes. The environmental data cover 11 variables: area, maximum depth, conductivity, total dissolved solids, Ca, Mg, Na, K, Fe, N and P. Lakes with incomplete environmental data were dropped, and for four lakes sampled twice only the first date was used. Patalas's original survey covered 45 lakes, and [[Sprules 1977]] analysed 49.

The authors describe the lakes as a morphometric series, with the three larger-lake groups having basins that allow good wind-generated circulation. Group B lakes are very small (less than a third of the surface area of Group D lakes on average) but more than twice as deep as Group D lakes on average. Some Group B lakes are meromictic, meaning they have poor circulation. The authors consider the series morphometric rather than successional.

## Key Findings

**Recommended procedure**
- Classify samples into assemblage groups, plot the groups on the study map to check for spatial contiguity, and test separation on environmental variables.
- Use [[Multiple Discriminant Analysis]] to test and display group separation, and judge group separation visually on ecologically interpretable discriminant functions. The authors argue this is a more conservative and convincing approach than relying on significance tests alone.
- Use the unrotated discriminant solution, which the authors found most interpretable.
- Log-transform environmental variables where appropriate (e.g., pH, sediment particle size in phi units).

**Zooplankton example results**
- Hierarchical classification of the 34 lakes, using a mutual-information similarity coefficient (Orloci 1968), produced four groups: A (*Diaptomus minutus* lakes), B (depauperate *Diaptomus leptopus* lakes), C (*D. minutus–Cyclops bicuspidatus* lakes) and D (*Diaptomus oregonensis* lakes).
- Among the most discriminating species by F-statistic, *Diaptomus oregonensis* had F = 41 (p < 0.01) and *Diaptomus minutus* had F = 35 (p < 0.01). Group D's geometric mean for *D. oregonensis* was 1.6 individuals per cm³ (0.68–3.8, 95% CL).
- A dichotomous key based on indicator species was presented in Table 2. It misclassified lakes 165, 251, 163, 189 and 265 at various steps, and lakes 67 and 164 were borderline between Groups A and D.
- The first two discriminant functions explained 54% and 39% of among-group variance (93% cumulative).
- MANOVA showed that area and depth alone gave significant separation of the groups (p < 0.01). The nine water-chemistry variables added no significant separation beyond area and depth (p > 0.05). The interpretation therefore rests on area and depth alone.
- Discriminant Function I separated Groups D, A and C along a gradient of increasing lake size. Discriminant Function II separated Group B, which has small, deep, poorly circulating basins.
- Patalas's four lake types broadly matched the four groups, with some lakes differing. The main distinction between Types I and II was the presence of *Limnocalanus macrurus* and *Senecella calanoides* in Type I.

**Comparison with Sprules (1977)**
- Sprules used principal components on species percentage abundance and found that only the first component was meaningful, separating large, deep, clear lakes from small, shallow, turbid ones.
- The authors argue that Sprules's second component mainly reflects the non-linear "horseshoe" trend. It did not capture the independent basin-shape factor that separated Group B lakes.

**Methodological conclusions**
- Reducing 11 environmental variables to two interpretable dimensions gave clear visual separation of assemblage groups. The authors argue this visual evidence is persuasive to lay audiences who "will believe their eyes."
- In impact studies, a "pollution species-assemblage" would show up as a group confined to the impacted area and separated mainly by pollutant variables. The authors suggest this could serve as a quantitative indicator for monitoring.
- Extensions to temporal sampling are suggested. Classification works well where temporal change is strong relative to spatial pattern, and a different approach is needed where spatial pattern dominates (Green 1977).