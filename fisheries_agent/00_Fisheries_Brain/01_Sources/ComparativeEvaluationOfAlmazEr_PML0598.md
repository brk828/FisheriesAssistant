---
species: N/A
common_name: N/A
family: N/A
habitat: Wet tundra (Arctic coastal plain, Prudhoe Bay oil field, northern Alaska)
ocean_basin: N/A
location: Prudhoe Bay oil field, Arctic coastal plain, northern Alaska, USA
tags: [remote-sensing, wetland-ecology, tundra, synthetic-aperture-radar, landcover-classification]
title: "Comparative evaluation of ALMAZ, ERS-1, JERS-1, and Landsat-TM for discriminating wet tundra habitats"
source_id: "PML0598"
marsh_id: "PML0598"
library: "Marsh Library"
permission: "not public domain"
source_citation: "G. I. Belchansky, G. K. Ovchinnikov, D. C. Douglas (1995). Comparative evaluation of ALMAZ, ERS-1, JERS-1, and Landsat-TM for discriminating wet tundra habitats. Polar Record 31(177): 161-168. Marsh Library ID: PML0598."
source_file: "Douglas 1995. Comparative evaluation of ALMAZ, ERS-1, JERS-1 and Landsat-TM for discriminating.pdf"
text_extraction: "text"
---
# Comparative Evaluation of ALMAZ, ERS-1, JERS-1, and Landsat-TM for Discriminating Wet Tundra Habitats

#ichthyology #marine-biology #remote-sensing

*Note: The source is a remote-sensing and landcover study rather than a fish or species study. No fish taxa are reported; the taxonomic tag above reflects the document's content as a wetland/landscape ecology study.*

## Executive Summary

This study compares the information content of three synthetic aperture radar (SAR) satellite systems ([[Almaz Sar]], [[Ers-1 Sar]], [[Jers-1 Sar]]) with multispectral [[Landsat-Tm]] imagery for mapping [[Wet Tundra]] habitats in the [[Prudhoe Bay Oil Field]] on Alaska's Arctic coastal plain. Using standardized unsupervised classification and a minimum-loss labeling procedure, the authors found that SAR data can concurrently detect roughly four or five landcover classes. Combining SAR images from different satellites improved detection of water bodies, but adding full-resolution SAR to Landsat-TM did not improve on Landsat-TM alone.

## Background & Description

Regional-scale mapping tools support documentation of environmental conditions and long-term monitoring. Optical multispectral scanners such as Landsat-TM provide synoptic coverage but are limited in polar regions by prolonged darkness and persistent cloud cover. SAR systems operate in all weather, penetrate haze, rain, snow, cloud, and smoke, and respond to surface structure, soil composition, and moisture. Each SAR system used a different combination of wavelength and polarization:

- ALMAZ: 10.0 cm wavelength, HH polarization, 10 m resolution (31 Jul 1992)
- ERS-1: 5.7 cm wavelength, VV polarization, 25 m resolution (13 Jul 1992)
- JERS-1: 23.5 cm wavelength, HH polarization, 18 m resolution (9 Aug 1992)
- Landsat-TM: six optical bands (0.45–2.35 µm), 30 m resolution (2 Aug 1985)

All images were full-resolution, geometrically and radiometrically corrected (Level 1b) and co-registered to UTM coordinates, resampled to 10 m pixels.

## Ecological & Environmental Context

The study area is wet tundra with numerous shallow lakes, interspersed mosaics of sedges, mosses, lichens, and low shrubs. The Arctic climate features short cool summers and very cold winters. Permafrost underlies the region, and the active layer thaws to 10–100 cm each summer. Annual precipitation averages about 200 mm, roughly two-thirds as snow. Petroleum development since the late 1960s has altered the landscape through roads, pipelines, gravel pads, excavations, and redistributed hydrology.

Ground truth came from three previously published geobotanical maps (W22, W32, W34; Walker and others 1986), each covering about 21 km² and together containing more than 11,000 polygons. Polygons were grouped into three generalized schemes:

- **Scheme A:** 23 vegetation-based classes
- **Scheme C:** 8 vegetation-based classes
- **Scheme D:** 17 surface-form classes

Classes covering less than 1 ha in total area were excluded, and mixed pixels along polygon boundaries were removed.

## Key Findings

**Methods**
- Maximum statistically distinct image-class signatures were generated for each image database, then merged using Euclidean distance (ED) thresholds (ED = 0, 1, 2, 3...).
- W34 served as training data and W32 as validation. An ED was rejected if agreement was unstable between the two areas; otherwise it was applied to the full study area.
- Class labels were assigned with a minimum-loss function that weighted all ground classes equally.
- Agreement (AGREE) and commission (COMM) statistics were calculated, and kappa statistics were used to correct for chance agreement.

**Results**
- SAR data were best at separating a subset of about four to five classes. For Scheme A, the most separable classes were water (A1), gravel pads (A17), and wet sedge tundra (A6), with continuous flooding (A18) also included except for JERS-1.
- For the ALMAZ water class, 43% of the 117,188 water pixels were correctly classified, with 46% commission.
- Landsat-TM achieved the closest representation of Scheme A. The combined ERS-1+JERS-1+Landsat-TM result was slightly inferior to Landsat-TM alone.
- Combining two or more SAR images improved water detection compared with single SAR datasets, likely because of multi-wavelength and multi-polarization information.
- JERS-1, with its longer wavelength, was less affected by wind-roughened water surfaces.
- Under Scheme C, optimal separation covered four classes along a moisture gradient from water (C1) to wet and aquatic sedge combinations (C4), wet sedge and moist-sedge shrub tundra (C5), and gravel pads (C8). Kappa analysis showed that improved agreement under Scheme C exceeded chance expectations.
- Under Scheme D (surface form), SAR best discriminated water (D8) and gravel pads (D14). Landsat-TM again showed higher overall agreement, and combining SAR with Landsat-TM gave little improvement.

**Discussion and Recommendations**
- SAR shows potential for discriminating up to four or five geobotanical classes in Prudhoe Bay wet tundra. Low agreement should not be read as a precise measure of SAR capability; the results compare the satellite systems only under the methods used.
- Sources of error include unknown map error, vegetation growth between the July–August 1992 SAR acquisitions, and soil moisture changes since the 1986 ground maps.
- Speckle filtering (Lee filter) raised water-class agreement in ALMAZ from 43% to 74%, with commission falling from 46% to 19%.
- Averaging SAR to 30 m pixels improved all Scheme A combined-data classifications by an average of about 10%, suggesting that merging SAR and Landsat data can perform better once speckle is reduced.
- Future work should test texture-based classifiers (second-order statistics, neural networks) and alternative SAR focusing methods, which may change detection capability.