---
species: Timarcha lugens
common_name: N/A
family: Chrysomelidae
habitat: High-altitude alpine zone on Hormathophylla spinosa host plant patches
ocean_basin: N/A
location: San Juan Valley, Sierra Nevada, southeastern Spain
tags: [metapopulation, spatial-autocorrelation, chrysomelidae, coleoptera, spatially-explicit-models, sierra-nevada]
title: "Consequences of spatial autocorrelation for the analysis of metapopulation dynamics"
source_id: "PML0884"
marsh_id: "PML0884"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. González-Megías, J. M. Gómez, F. Sánchez-Piñero (2005). Consequences of spatial autocorrelation for the analysis of metapopulation dynamics. Ecology, 86(12): 3271-3277. Marsh Library ID: PML0884."
source_file: "Gomez J.M. et al. 2005. Consequences of spatial autocorrelation for the analysis of metapopulation dynamics.pdf"
text_extraction: "text"
---
# Consequences of Spatial Autocorrelation for the Analysis of Metapopulation Dynamics

#ichthyology #marine-biology #chrysomelidae

*Note: this document concerns an insect (Coleoptera) and not a fish; the tag above reflects the taxon named in the source, as the system format requires the specific family or taxon.*

## Executive Summary

This study examines how [[Spatial Autocorrelation]] affects the statistical analysis of [[Metapopulation Dynamics]] in the high-altitude beetle *Timarcha lugens*, an apterous chrysomelid endemic to the [[Sierra Nevada]] of southeastern Spain. The authors compare conventional spatially implicit causal models with [[Spatially Explicit Models]] that include [[PCNM]] spatial base functions. Their central claim is that ignoring spatial structure can change which factors appear to control beetle density, sex ratio and extinction, with potential consequences for conservation management.

## Background & Description

- **Study organism:** *Timarcha lugens* Rosenh. (Coleoptera: Chrysomelidae), a high-altitude apterous beetle occurring at 2400–3200 m a.s.l. It is active from late June until the end of September.
- **Host plant:** The beetle is monophagous on *Hormathophylla spinosa* (Cruciferae), a long-lived stunted shrub with a patchy alpine distribution. This patchiness structures the beetle population into a metapopulation with rare immigration and local patch extinctions.
- **Study area:** San Juan Valley (about 4 × 3 km; 37°04′ N, 3°22′ W), sampled from 2400 m to 3000 m over five years (1998–2002). Twenty host-plant patches were tagged and GPS-located.
- **Sampling design:** Two 10 × 2 m transects per patch, placed haphazardly each year, with beetles counted by sex and stage. Censuses were timed to the same plant phenological stage (late June to early July).
- **Response variables:** Beetle density (beetles per m²), extinction (binary: 1 = extinct in at least one year), and sex ratio (males/females).
- **Explanatory variables:** Altitude, patch area, river position (left, right, centre), aspect, isolation (mean distance to three nearest occupied patches), plant density, and average plant size (estimated volume as a hemisphere).

## Ecological & Environmental Context

The authors argue that metapopulation models are mostly spatially implicit, even though nearby populations usually resemble each other more than expected by chance. Spatial autocorrelation arising from environmental variation, dispersal limitation, or biotic interactions can inflate the spatial scale of population synchrony, raise extinction risk, and impede recolonisation. Parametric methods that assume independent data are violated under autocorrelation, which distorts degrees of freedom and inflates Type I error.

The study area is small (no more than 3 km between the farthest patches), so the authors infer that the steep valley, altitude differences and the river likely create a climatic gradient. Limited dispersal in *Timarcha* is proposed as a further source of spatial structure.

## Key Findings

**Methods**
- Causal models were fitted using the d-sep test (Shipley) and structural equation models (SEM) with Monte Carlo procedures.
- Model selection used goodness-of-fit (χ²/df), Akaike Information Criterion, Schwarz's Bayesian Criterion and Browne–Cudeck cross-validation.
- Spatial structure was tested with [[Moran's I]] and correlograms, using Sturge's rule for distance classes and Bonferroni correction.
- PCNM was used to create spatial base functions. Eleven PCNM variables were generated for extinction and sex ratio (19 sites), and 12 for beetle density (20 sites). The first four fine-scale variables were retained, following [[Borcard and Legendre]].

**Spatial patterns**
- Altitude, river position, patch area, plant density and plant size were non-randomly distributed in space.
- Beetle density, sex ratio and extinction events were spatially autocorrelated, with positive correlations at the nearest distance classes.
- After multiple regression, autocorrelation persisted for sex ratio, extinction and plant size. None remained for beetle density or plant density.

**Factors affecting beetle distribution (summary of models)**
- **Beetle density:** The spatially implicit model identified river position, plant size, area (non-significant) and altitude. Density was higher in the centre of the river than on either bank. The spatially explicit model gave a similar set of variables, but altitude's effect was stronger.
- **Sex ratio:** The implicit model included altitude, plant size, river position and area. Sex ratio was lower in central patches and in patches with larger plants. The explicit model added isolation and space, and isolation was important only in this model.
- **Extinction:** The implicit model included altitude, plant density and area, with extinction more likely at lower altitudes and higher plant density. The explicit model retained river position, isolation, plant size and a spatial variable. Extinction concentrated on left-bank patches with small plants, and increased with isolation.

**Main conclusions**
- Spatially explicit and implicit models differed for all dependent variables, in both the relative importance and the identity of variables.
- Isolation, a key predictor in metapopulation theory, was significant for sex ratio and extinction only after controlling for spatial location.
- Plant density was important only in the implicit extinction model. Plant size and river position (a proxy for resource availability and microclimate) emerged only in the explicit model.
- Conservation priorities would differ depending on the model: implicit models focus on high plant density patches, whereas explicit models point to plant size, isolation and microhabitat.
- The authors conclude that including space can change conclusions about the nature and importance of factors controlling abundance, extinction and occurrence, and recommend spatially explicit analysis for managing endangered species.