---
species: Poecilia reticulata
common_name: Guppy
family: Poeciliidae
habitat: Freshwater streams and isolated pools in the Northern Mountains of Trinidad
ocean_basin: N/A
location: Trinidad (41 sample sites, Trinidad and Tobago National Grid)
tags: [ichthyology, marine-biology, poeciliidae, color-polymorphism, population-genetics, biostatistics]
title: "Quantitative matrix comparisons in ecological and evolutionary investigations"
source_id: "19083"
minckley_id: "19083"
source_citation: "M. E. Douglas and J. A. Endler (1982). Quantitative matrix comparisons in ecological and evolutionary investigations. Journal of Theoretical Biology 99(4): 777-795. Minckley Library ID: 19083."
source_file: "19083.pdf"
text_extraction: "ocr"
---
# Quantitative Matrix Comparisons in Ecological and Evolutionary Investigations

#ichthyology #marine-biology #poeciliidae

## Executive Summary

Douglas and Endler (1982) apply the [[Mantel Test]], a non-parametric method for comparing data matrices, to male color polymorphisms of [[Poecilia Reticulata]] (guppy) from 41 stream sites in [[Trinidad]]. They test four evolutionary models: response to an environmental gradient, localized environmental patches, [[Isolation By Distance]] with genetic drift, and historical factors. The main result is that spot polymorphisms covary significantly with altitude and with predator community differences, supporting selectionist models (I and II). Geographic distance and the historical/connectivity matrices showed no positive relationship. The authors conclude that the Mantel procedure allows quantitative testing of ecological and evolutionary questions that were previously hard to address statistically.

## Background & Description

**Study organism.** Male guppies show highly variable spot patterns (number, size, color, and position). Pattern genes are sex-linked and not expressed in females, and the color patterns are described as following simple Mendelian inheritance. Endler (1978) had proposed that male coloration reflects a compromise between [[Sexual Selection]] favoring bright males and [[Predation]] favoring [[Crypsis]]. Bright males mate more often but are more susceptible to predators.

**Statistical method.** Matrix correlations between cophenetic matrices lack independence among cells, so standard permutation tests cannot assess their significance (Farris, 1969, 1973). Mantel (1967) addressed this with a permutation-based comparison of cross-products between matrices. The authors used the GEOVAR library for the Mantel tests and NT-SYS for the pairwise taxonomic distances (Rohlf et al., 1972). Significance was assessed with a [[Bonferroni Correction]].

**Sampling and data.** At each of the 41 sites the authors recorded:
- Density estimates for predators, scored from 0 (absent) to 4 (abundant).
- Seven phenotypic measures of male color: mean spot size for six colors plus total spot number.
- Elevation (m) and Trinidad National Grid coordinates.

Table 1 lists seven predator taxa, although the text refers to six predators.

**Model construction.** Four models were tested:
- **Model I:** Clinal response to an environmental gradient (selection).
- **Model II:** Localized environmental patches (selection).
- **Model III:** [[Isolation By Distance]] and [[Genetic Drift]] (stochastic).
- **Model IV:** Historical factors such as [[Founder Effect]] or [[Gene Flow]] (historical).

Six distance matrices were built to represent these models:
1. ALT: altitudinal differences.
2. GEO: kilometric distances.
3. ASM: an [[Asymptotic Distance Matrix]] for contiguous sites, built on a [[Gabriel Network]].
4. STR: a binary stream-connectivity matrix (same watershed).
5. PRD: predator distances.
6. SPT: spot-polymorphism distances (the response matrix).

## Ecological & Environmental Context

- **Predator gradient.** Predator numbers decline in a regular sequence as altitude increases (Endler, 1978, as cited). Predator communities are classed from A (Aequidens pulcher only) up to A+K+C (A. pulcher, characins, and [[Crenicichla Alta]]). Classes R+M (Rivulus hartii plus Macrobrachium crenulatum) appear at lower sites. Predator rankings were altered by agriculture, lumbering, and mining at some sites.
- **Stream structure.** Waterfalls and isolated pools occur more often as altitude (stream gradient) rises. Geographically adjacent sites occur most often at higher elevations.
- **Gene flow.** Gene flow between sites is considered reduced or absent, as suggested by Endler (1978).
- **Laboratory support.** Long-term laboratory experiments with wild-caught guppies showed that, under visually hunting predators, color polymorphisms shifted over a few generations to match background patch type. Without predation, sexual selection increased male conspicuousness and color diversity.

## Key Findings

**Pairwise Mantel comparisons (15 in total).** Five tested the four models directly, and ten were ancillary. The adjusted significance threshold was p < 0.0033 (t ≥ +2.940, df = infinity), derived from 0.05/n.

| Model | Comparison | Result |
|---|---|---|
| I | ALT vs SPT | t = 4.7827; significant positive covariation. H0 rejected. |
| II | PRD vs SPT | t = 3.607; significant positive covariation. H0 rejected. |
| III | GEO vs SPT | t = 0.854; no relationship. H0 cannot be rejected. |
| IV | ASM vs SPT | t = -6.6127; significant negative covariation. H0 cannot be rejected. |
| IV | STR vs SPT | t = -3.1077; significant negative covariation. H0 cannot be rejected. |

**Interpretation.**
- The selectionist models (I and II) are supported. Spot polymorphisms track altitude and predator community composition.
- Model III (isolation by distance) is not supported for spot patterns. However, predator communities become more dissimilar with geographic distance, which the authors say is consistent with isolation by distance.
- Model IV is not supported. The strongest phenotypic differences occurred between geographically contiguous and same-watershed sites. The authors attribute this to low-order negative spatial autocorrelation, which they link to strong selection on a plastic species in patchy habitats.

**Ancillary results.**
- ALT vs PRD gave t = 2.40 (p < 0.025), which is not significant at the adjusted level.
- Mean pairwise distances: predator distances averaged 1.721 and spot distances 1.174 (n = 820 site pairs), so predator distances are larger and more variable.
- Both matrices nonetheless show significant positive covariation.

**Methodological points.**
- The Mantel test with a permutational distribution avoids the independence problem of matrix correlations.
- A toy 5 × 5 example in Appendix 1 gives observed Z = 440 against an expected Z of 605, showing a negative association, though the example is artificial.

**Conclusions.** Predation pressure, interacting with altitude, is the most likely primary determinant of color-pattern origin and maintenance in Trinidadian guppies. The authors caution that their models are idealized, single-cause simplifications of nature. They argue that the Mantel test is a useful way to evaluate competing ecological and evolutionary hypotheses quantitatively.