---
species: "Notropis, Campostoma, Nocomis, Exoglossum, Rhinichthys, Phenacobius, Erimystax, Diononda, Cyprinella, Alburnops, Hybognathus (North American minnows; 145 species measured)"
common_name: "North American minnows (chubs, daces, shiners)"
family: Leuciscidae
habitat: "Freshwater rivers and streams; benthic (bottom) and pelagic (open-water) microhabitats"
ocean_basin: N/A
location: "North America, with diversity concentrated in southeastern United States rivers"
tags: [ichthyology, evolution, leuciscidae, benthic-pelagic-axis, macroevolution, speciation]
title: "Pelagic zone is an evolutionary catalyst, but an ecological dead end, for North American minnows"
source_id: "PML0343"
marsh_id: "PML0343"
library: "Marsh Library"
permission: "not public domain"
source_citation: "E. D. Burress, P. B. Hart (2024). Pelagic zone is an evolutionary catalyst, but an ecological dead end, for North American minnows. Evolution (Society for the Study of Evolution). Marsh Library ID: PML0343."
source_file: "Burress and Hart. 2024. Pelagic Zone is an evolutionary catalyst, but ecological dead end, for North American minnows.pdf"
text_extraction: "text"
---
# Pelagic Zone as an Evolutionary Catalyst but an Ecological Dead End for North American Minnows

#ichthyology #marine-biology #leuciscidae

## Executive Summary

This study tests how two macroevolutionary predictions, that colonizing a new geographic area and increasing habitat complexity both promote evolution, behave when they point in opposite directions. Using the North American minnow radiation ([[Leuciscidae]]), the authors examine the ancestral shift from benthic (bottom-dwelling) to pelagic (open-water) microhabitats. Pelagic species showed more similar body shapes and slower rates of [[Phenotypic Evolution]], but faster [[Speciation]] rates than benthic species. The authors interpret these as two independent, opposing responses to specialization along the [[Benthic-Pelagic Axis]]. The pelagic zone therefore acted as an evolutionary catalyst for diversification but an ecological dead end for morphological diversity.

## Background & Description

Minnows (Leuciscidae) include chubs, daces, and shiners. Most eastern North American leuciscids form a clade defined by a small opening at the base of the skull, the [[Open Posterior Myodome]]. This clade contains about 250 species and is particularly diverse in southeastern US rivers, where up to 15 species may co-occur in one assemblage. Much of this diversity followed an ancestral benthic-to-pelagic microhabitat shift.

The authors frame two competing hypotheses:

- **Hypothesis 1 (Competitive release):** Pelagic lineages escape competition with a saturated benthic assemblage, so phenotypic evolution and speciation should both be elevated in pelagic species.
- **Hypothesis 2 (Reduced niche availability):** The pelagic zone is relatively homogeneous, offering fewer niches, so phenotypic evolution and speciation should both be reduced in pelagic species.

The study relates to the broader idea of [[Ecological Opportunity]], which predicts rapid evolution when lineages colonize novel environments. Complex habitats such as [[Coral Reefs]] are thought to promote evolution through many available niches. The minnow system provides a case where these expectations conflict.

## Ecological & Environmental Context

- **Benthic vs. pelagic zones:** Benthic habitats are structurally complex and taxonomically rich, while the pelagic zone is sparsely inhabited by other small-bodied lineages. Pelagic minnows occupy a higher trophic position, consuming less algae and more terrestrial insects.
- **Terrestrial subsidies:** Pelagic minnows often feed on insects at or near the water surface. Because these subsidies are ephemeral and unpredictable, they may reduce competition and allow species-rich assemblages to coexist, a pattern tied to [[Competitive Release]] and [[Terrestrial Subsidies]].
- **Mouth angle as an ecological proxy:** Minnows with larger mouth angles consume more terrestrial insects and less benthic prey such as aquatic insects and algae. Mouth angle therefore indexes specialization along the benthic-pelagic axis.
- **Broader analogues:** The authors compare the pattern with [[Cave Fishes]] (Amblyopsidae), where surface-to-cave transitions increased species richness but not phenotypic evolution, and with marine systems, where deep-sea and pelagic lineages show similar decoupling of depth and benthic-pelagic axes.
- **Continental vs. insular radiations:** Continental radiations, such as those of [[Cichlids]] in lakes and rivers, diversify across drainages and tributaries, unlike insular systems such as [[Stickleback]] lakes.

## Key Findings

### Sampling and measurements
- Body shape was measured on **684 individuals** representing **145 species** (1 to 5 individuals per species), accessioned at the Auburn University Museum of Natural History. This is about **58%** of described species.
- Twelve linear dimensions were measured with digital calipers to **0.01 cm** precision. Body size was controlled using [[Phylogenetic Residuals]] from a log-log regression against standard length.
- The phylogeny was a multi-locus tree of **223 species** (about **90%** of described species), from [[Phylogenetic Comparative Methods]] work by Hollingsworth et al. (2013).

### Morphology and disparity
- Mouth angles ranged from **10° to 53°**, reflecting a continuum from inferior (benthic) to superior (pelagic) mouths.
- Benthic species tended to have wider and elongated bodies, longer heads, shorter jaws, and smaller eyes.
- [[Body Shape Disparity]] declined across mouth-angle quartiles. The lowest (most benthic) quartile had **two- to 2.5-fold higher** morphological disparity than the other quartiles, indicating that pelagic species are more similar in body shape.

### Rates of phenotypic evolution
- Rates of body shape evolution were state-dependent (posterior probability **PP = 1.0**). The highest (most pelagic) quartile had the **slowest** rates.
- This result held across different priors on the number of rate shifts (25, 50, 75, and 100) (all PP = 1.0) and across different numbers of discrete character states (all PP > 0.966).

### Tip rates and correlations
- **Phenotypic tip rates** were negatively correlated with mouth angle (t = -4.909; p < .0001).
- **Speciation tip rates** were positively correlated with mouth angle (t ≈ 2.56; p = .012).
- **Phenotypic and speciation tip rates** were not correlated (p = .525). The authors take this as evidence that the two parameters respond independently and in opposite directions to benthic-to-pelagic transitions.

### Interpretation
- The pelagic zone promotes speciation, consistent with the mobility of pelagic fishes. These fishes may be more prone to [[Allopatric Speciation]] after geographic isolation.
- The pelagic zone funnels species into specialized ecologies associated with a limited range of phenotypes. The authors describe this as a singular adaptive peak, a pattern in which high speciation is not paired with exceptional morphological evolution.
- The results challenge the interpretation of coincident speciation bursts and reduced morphological evolution as [[Adaptive Radiation]]. Minnows therefore show that ecological opportunity can produce decoupled signals across different dimensions of biodiversity.
- Minnows contrast with the coral-reef paradigm, in which structural complexity drives rapid evolution. In minnows, the simpler pelagic zone may have limited ecological diversity.

### Methods summary
- Phylogenetic analyses used a state-dependent, multivariate, relaxed [[Brownian Motion Model]] implemented in RevBayes, with MCMC runs of 500,000 generations and 10% burn-in.
- Speciation rates were estimated with a [[Birth-Death-Shift Model]] (K = 4 rate categories), which was used only for speciation because extinction cannot be reliably estimated from extant phylogenies.
- Mouth angle was measured from photographs using tpsDIG2. Relationships between tip rates and mouth angle were tested with phylogenetic generalized least squares.

### Data availability
- Data are archived in the Dryad repository.