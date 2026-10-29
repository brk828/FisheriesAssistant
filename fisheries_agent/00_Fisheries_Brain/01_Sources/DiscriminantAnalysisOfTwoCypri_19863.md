---
species: "Phoxinus eos, Phoxinus erythrogaster"
common_name: "Northern redbelly dace, Southern redbelly dace"
family: "Cyprinidae"
habitat: "Freshwater streams, headwater streams, lakes (Quebec lakes referenced for hybrids)"
ocean_basin: "N/A"
location: "North America: Minnesota (sympatry), lower Mississippi drainage, Quebec lakes, Nebraska headwater streams"
tags: [ichthyology, marine-biology, cyprinidae, morphometrics, discriminant-analysis, hybridization]
title: "Discriminant analysis of two cyprinid fishes Phoxinus eos and Phoxinus erythrogaster (Pisces: Cyprinidae)"
source_id: "19863"
minckley_id: "19863"
source_citation: "G. R. Joswiak and W. S. Moore (1982). Discriminant analysis of two cyprinid fishes Phoxinus eos and Phoxinus erythrogaster (Pisces: Cyprinidae). American Midland Naturalist 108(2): 398-401. Minckley Library ID: 19863."
source_file: "19863.pdf"
text_extraction: "ocr"
---
# Discriminant Analysis of Two Cyprinid Fishes: *Phoxinus eos* and *Phoxinus erythrogaster*

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This note by [[Joswiak]] and [[Moore]] (Wayne State University, 1982) applies linear discriminant analysis to morphometric data from [[Phillips 1969]] to separate two very similar North American minnows, the northern and southern [[Redbelly Dace]] species, *Phoxinus eos* and *P. erythrogaster*. The discriminant function correctly classified over 95% of specimens, substantially better than univariate classification. The authors also discuss the limits of discriminant analysis for identifying putative hybrids, drawing on [[Legendre 1970]], [[Butcher 1980]], and [[Neff and Smith 1979]], and on allozyme evidence ([[Allozyme Analysis]]) showing no diagnostic alleles between the two species.

## Background & Description

- **Taxonomic history:** [[Jordan and Everman 1896]] and [[Fowler 1909]] treated the two forms as subspecies. [[Mahy 1975]] proposed three geographical races including *P. oreas*. [[Phillips 1969]] found no evidence of intergradation in areas of sympatry in Minnesota.
- **Morphological similarity:** Only two characters from Phillips (1969) gave misidentification probabilities below 50%. No diagnostic alleles were found at 27 presumptive loci ([[Joswiak 1980]]).
- **Morphometric dataset:** Phillips measured 115 specimens of each species for nine characters, selected to represent size classes and drainages. This study used eight: standard length (SL), orbit length (OL), snout length (SNL), postorbital head length (POL), head length (HL), head depth (HD), mouth length (LM), and mouth angle (MA).
- **Analytical approach:** Two stepwise discriminant analyses maximizing Mahalanobis' distance were run in [[SPSS]] (Version H, Release 8.1). Analysis A included all eight variables. Analysis B removed mouth angle, which Phillips identified as the most important character. Individual group covariance matrices were used, and [[Box's M Test]] assessed covariance equality.

## Ecological & Environmental Context

- **Sympatry and allopatry:** The species co-occur in places, such as the lower Mississippi drainage and Minnesota, where they are often hard to tell apart. Specimens with intermediate scores tended to be small and came from allopatric localities where hybridization is very unlikely.
- **Hybridization in Quebec lakes:** [[Legendre 1970]] reported that *P. eos* and *P. neogaeus* form apparently Mendelian hybrid populations in three Quebec lakes, with some hybrids possibly affected by lake poisonings and stocking in the early 1950s.
- **Hybridization in Nebraska streams:** Presumptive hybrids of *P. eos* and *P. neogaeus* from headwater streams in Nebraska had allozyme patterns characteristic of F1 hybrids ([[Joswiak et al. 1982]]).
- **Plasticity:** Environmental influences on morphology were noted as a further confounding factor.
- **Size effect:** Misidentification probability declined with standard length (r = .24, P < .01), attributed to measurement error in very small fish and similarity in early ontogeny.

## Key Findings

- **Classification performance:** Analysis A, which included mouth angle, correctly classified 95.7% of *P. eos* and 95.7% of *P. erythrogaster*. Five of 115 *P. eos* (4.3%) were misclassified. Only one of these came from the lower Mississippi drainage, where sympatry is possible.
- **Variable selection:** In Analysis A, [[Snout Length]] was excluded by stepwise selection. In Analysis B, none of the seven remaining variables was removed, but correct classification dropped about 10% (84.3% *P. eos*; 87.0% *P. erythrogaster*).
- **Covariance:** Box's M tests for individual group covariance matrices were highly significant (P < .000001). Canonical correlation coefficients were 0.86 (Analysis A) and 0.69 (Analysis B).
- **Key conclusion:** Variables that were not significantly different in univariate t-tests can still discriminate well when covariance is considered.
- **Practical use:** Unknown specimens can be classified by multiplying raw measurements by the function coefficients, summing, and adding a constant. *P. erythrogaster* scores are mostly negative, and *P. eos* scores are mostly positive.
- **Hybrid identification caveat:** Discriminant analysis can inflate apparent variance among unknowns, and it cannot reliably establish introgression. Allozymes, with known Mendelian codominant inheritance, are the better tool, but they are unlikely to detect hybridization between *P. eos* and *P. erythrogaster* because they lack diagnostic alleles.
- **Overall conclusion:** Discriminant analysis is adequate to separate the species into distinct groups, but it is of little use in resolving hybridization between them.