---
species: Colinus virginianus
common_name: Northern Bobwhite
family: Odontophoridae
habitat: Agricultural and mixed grassland-woodland landscape (grassy field borders, woodlots, fencerows, row crops, burned fields)
ocean_basin: N/A
location: Mississippi, USA
tags: [ichthyology, marine-biology, habitat-analysis, radiotelemetry, bird-ecology]
title: "A comparison of distance-based and classification-based analyses of habitat use"
source_id: "PML0482"
marsh_id: "PML0482"
library: "Marsh Library"
permission: "not public domain"
source_citation: "L. M. Conner, M. D. Smith, L. W. Burger Jr. (2003). A comparison of distance-based and classification-based analyses of habitat use. Ecology 84(2): 526-531. Marsh Library ID: PML0482."
source_file: "Conner L.M. et al. 2003. A comparison of distance based and classification basd analyses of habitat use.pdf"
text_extraction: "text"
---
# A Comparison of Distance-Based and Classification-Based Analyses of Habitat Use

#ichthyology #marine-biology #odontophoridae

## Executive Summary

This Ecology "Notes" article compares two families of methods for quantifying habitat use: classification-based approaches, which assign animal locations to habitat categories, and distance-based approaches, which measure Euclidean distances from animal locations to habitat features. The authors apply [[Compositional Analysis]] (CA) as the classification benchmark and a [[Distance-Based Analysis]] (DA) to radiotelemetry data from 62 [[Northern Bobwhite]] (*Colinus virginianus*, hereafter "quail") tracked in Mississippi during 1997 and 1998. Because the original locations were error-free, the authors simulated location error to test sensitivity. The study is a methodological comparison; it reports no fisheries or marine data, and the species is a terrestrial upland game bird rather than a fish.

## Background & Description

- **Study species:** Northern Bobwhite (*Colinus virginianus*), a ground-dwelling quail used as a model for habitat selection analysis.
- **Sample:** 62 radio-tracked individuals, only those with more than 30 locations included in analysis.
- **Tracking method:** Locations were obtained by homing (walking toward the strongest signal), so location error did not occur in the original data. Locations were treated as serially independent.
- **Study area:** A 710 ha site (given as "7100-ha" in the scanned text; treat as OCR-affected) in Mississippi.
- **Terminology:** "Habitat selection" is defined as observed use relative to expected use from a null model, following [[Johnson Third-Order Habitat Selection]] (Johnson 1980). Habitats used more than expected are "preferred," those used less are "avoided."
- **Criteria:** Aebischer et al. (1993) proposed that a selection metric should use individuals as sampling units, avoid the unit-sum constraint, allow group comparisons, and work at multiple spatial scales. CA was introduced to meet these criteria.

## Ecological & Environmental Context

**Habitat classes** (delineated from management regimes and vegetation similarity):

- **GRASS:** pasture/hay fields, Conservation Reserve Program fields, grassy field borders (undisturbed).
- **BURN:** fields with prescribed burns in the previous fall or winter.
- **WOODY:** woodlots, fencerows, ditches, and road rights-of-way with woody vegetation.
- **ROWCROP:** soybean and corn fields and food plots.
- **ODD:** roads, buildings, and water, grouped due to rarity.

Mean patch sizes were reported for WOODY, GRASS, ROWCROP, ODD, and BURN (values given in the source as 4.2, 14.2 to 14.7, 17.0, and 4.2 ha respectively, with OCR ambiguity). Edge density was reported as approximately 11 km/km².

**Data handling:** Habitat maps were digitized in ARC/INFO from scanned, georeferenced 1:24,000 aerial photographs. Home ranges were 95% adaptive kernel estimates derived in HOME RANGER.

**Simulated location error:** Noisy locations were generated uniformly within 50 m of real fixes. Error circles of 50 m radius were then drawn around each noisy location to model error distribution, with the authors noting that 50 m is probably smaller than typical triangulation error.

## Key Findings

- **Classification-based results (CA):**
  - Real data: habitat selection occurred (P = 0.001). WOODY was most preferred, significantly above all other habitats; GRASS and BURN were preferred over ROWCROP and ODD.
  - Noisy data without error correction: habitat selection still occurred, but the ranking changed and the importance of edge was not detected.
  - Error-circle approach: habitat selection occurred (P = 0.006), with WOODY preferred over GRASS, ROWCROP, and ODD.
- **Distance-based results (DA):**
  - Real data: habitat selection occurred. All mean distance ratios except ROWCROP were below 1.0 (P = 0.001 for most), indicating quail were closer to those habitats than expected. WOODY was preferred over ODD and ROWCROP.
  - Noisy data: selection still detected, and the ranking remained substantially the same as with real data.
- **Edge detection:** DA identified edge as an important habitat feature. CA did not.
- **Error sensitivity:** Location error did not alter DA conclusions. It did alter CA conclusions. Modeling error distributions within CA did not reliably reduce this sensitivity.
- **Methodological advantages of DA:** DA is not restricted to linear or point features, requires no explicit error handling, and can extract more information from the same data. It can also be analyzed with standard multivariate tools (such as logistic and linear regression) and can use linear, point, and areal features in one framework. CA requires explicit measures to incorporate non-areal components.
- **Caveat:** DA depends on randomly generated points to estimate expected distances, which introduces sampling error. The authors argue that modern GIS makes availability mapping more accurate, which reduces this concern.
- **Conclusion:** The authors argue that distance-based methods are a valid and more flexible alternative to classification-based methods for analyzing habitat use. They emphasize that the two approaches can rank habitats differently, so the choice of method affects management conclusions, including the assessment of conversion of ROWCROP to other habitat types.