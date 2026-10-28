---
title: "A Geographical Information System for Some Mediterranean Benthic Communities"
authors: R. Méaille, L. Wald
year: 1990
journal: International Journal of Geographical Information Systems
taxon_focus: Mediterranean benthic communities (non-fish; habitat/biocoenosis mapping)
key_taxa: [Posidonia oceanica, Cymodocea nodosa, Zostera noltii, photophilic algae, coralligenous assemblages]
habitat: ["infralittoral", "circalittoral", "muddy sand", "littoral sand", "coralligenous substrate", "seagrass meadows", "coastal detritus", "offshore detritus"]
ocean_basin: Mediterranean Sea
region: "Southeast France, between La Ciotat and Giens"
method: Geographical Information System (GIS), fuzzy set theory synthesis
tags: [ichthyology, marine-biology, benthic-ecology, seagrass-communities, coralligenous-habitat]
source_id: "12354"
---

# A Geographical Information System for Some Mediterranean Benthic Communities

#ichthyology #marine-biology #benthic-ecology

> **Note on scope:** This source does not address fish taxonomy or physiology directly. It is a methodological paper on synthesizing multi-source cartographic data describing [[Mediterranean Benthic Communities]] — including [[Posidonia Oceanica]] meadows, [[Coralligenous Habitat]], and soft-sediment assemblages — via a raster-based [[Geographical Information System]] using [[Fuzzy Set Theory]]. The note below is adapted to reflect this ecological/habitat-mapping focus rather than a fish-specific one.

## Executive Summary

This 1990 paper by Méaille and Wald describes a low-cost, PC-based Geographical Information System (GIS) developed to integrate and reconcile decades of heterogeneous benthic community maps for a stretch of the French Mediterranean coast (La Ciotat to Giens). Twenty-six pre-existing maps — produced using airborne surveys, direct submarine observation, and dredging-based bionomic sampling — were digitized, standardized into 25 classes (10 groups) following the classification scheme of [[Pérès and Picard (1964)]], and geometrically corrected to a common Lambert III reference grid at 1/25000 scale with 25×25 m pixels. Because all layers described the *same* ecological theme (benthic community distribution) rather than different themes, the authors treated the map stack as repeated, potentially conflicting observations of a single random variable. They devised a fuzzy-set-based synthesis method that weights each pixel according to survey date, sampling technique, and original map scale, producing both a synthesis map (most plausible community per pixel) and conflict maps (quantifying disagreement between sources). The work is foundational for spatially explicit historical monitoring of Mediterranean seagrass and hard-substrate biocoenoses.

## Morphological / Habitat Classification Characteristics

Rather than organismal morphology, the paper's core "characteristics" are the **standardized habitat/biocoenosis classes**, reduced from ~100 heterogeneous names in source maps to 25 classes within 10 groups (Table 1):

- **Unmapped area** (code 0)
- **Photophilic algae** group — including degraded photophilic algae (APd) and algae on submarine scree (APe)
- **Port / highly polluted areas** (code 10)
- **Muddy sand communities** — including [[Zostera Noltii]] meadows and [[Cymodocea Nodosa]] meadows growing on muddy sand substrate (SVMC), and coastal mud (V4C)
- **Littoral sand communities** — sand (SFHN, SFBC), raw sand influenced by bottom currents (SGCF)
- **Posidonia Oceanica meadows** — healthy (HP), degraded (HPD), and dead meadows recolonized by photophilic algae (MM, "matte morte")
- **Coralligenous communities** — coralligenous sediments (C) and pre-coralligenous sediments (PC)
- **Coastal detritus communities** — multiple sub-types (DC, DC/c, DC/p, DC/m, DC/i)
- **Offshore detritus communities** (DE, DL)
- **Emerged/land areas** (COTE)

These classes represent depth-zonation and substrate-driven assemblages typical of Mediterranean infralittoral and circalittoral zones, ranging from shallow photophilic algal belts to deep offshore detrital communities.

## Ecological & Environmental Context

- **Depth stratification**: Airborne survey techniques are only reliable to ~35 m depth in this region; beyond this, maps are extrapolated, reflecting the known depth limits of aerial detection of submerged vegetation such as [[Posidonia Oceanica]].
- **Substrate specificity**: Distinct biocoenoses are tied to specific sediment types — muddy sand supports [[Zostera Noltii]] and [[Cymodocea Nodosa]] meadows; hard substrates support coralligenous and pre-coralligenous assemblages; different detritus grades (coastal vs. offshore) support distinct detrital communities.
- **Successional/degradation states**: The classification explicitly captures degraded states of key habitats (e.g., degraded photophilic algae, degraded *P. oceanica*, dead *P. oceanica* meadows overgrown by algae), indicating sensitivity of these communities to anthropogenic pressure and enabling temporal tracking of habitat decline.
- **Anthropogenic interface**: A dedicated class for ports/highly polluted areas acknowledges direct human impact zones within the broader benthic community mosaic.
- **Spatial interaction and conflict**: The GIS conflict maps reveal where classification boundaries between adjacent community types (e.g., photophilic algae vs. offshore detritus, littoral sand vs. coastal detritus, coralligenous vs. coastal/offshore detritus) are ambiguous across independent surveys — likely reflecting real ecotonal/transitional zones as well as methodological discrepancies.

## Key Findings

- **Data heterogeneity problem**: Multiple independent surveys of the same coastal area produced conflicting classifications due to differing sampling techniques (aerial, submarine, dredging), scales, projections, and non-standardized nomenclature (~100 original class names collapsed to 25 standardized classes).
- **Weighting scheme**: A credit/weight (0–20) was assigned to each pixel in each layer based on cartographic error, sampling method reliability, map scale, bathymetry, and survey age (Table 2). E.g., weight = 8 for questionable mapping (isobath-based inference of *Posidonia* lower limit at 30 m); weight = 20 for sub-pixel mapping accuracy.
- **Fuzzy set synthesis method**: Applying [[Fuzzy Set Theory]] (Zadeh 1965; Kaufmann 1977), each class within each layer is treated as a fuzzy subset; the union across layers (taking maximum plausibility per pixel) generates the synthesis map, while intersections identify and quantify inter-layer conflicts.
- **Conflict mapping as novel output**: Unlike traditional manual synthesis, this method generates explicit, quantified conflict maps showing both the *location* and *magnitude* of disagreement between source maps — useful for identifying areas needing further field verification and for revealing implicit assumptions of individual oceanographers.
- **Recency preference**: When conflicting classifications of equal weight occur at a pixel, precedence is given to the most recently surveyed map, supporting temporal-change detection of benthic communities such as *Posidonia oceanica* meadow regression.
- **System design**: Implemented on an IBM PC-compatible system with WORM optical disk raster storage, structured into eight overlapping geographic sectors (max. 440×360 pixels each) for computational tractability, using Lambert III projection at 1/25000 reference scale — aligned with the EU CORINE programme standards.
- **Future direction**: The authors flag that pixel-weight assignment is currently heuristic and propose incorporating artificial intelligence / expert-knowledge encoding, plus additional variables (sedimentology, inter-community spatial relationships), to make weighting more objective and dynamically updatable.

---
### Related Concepts
[[Posidonia Oceanica]] · [[Coralligenous Habitat]] · [[Cymodocea Nodosa]] · [[Zostera Noltii]] · [[Fuzzy Set Theory]] · [[Geographical Information System]] · [[Mediterranean Benthic Communities]] · [[Bionomic Mapping]]