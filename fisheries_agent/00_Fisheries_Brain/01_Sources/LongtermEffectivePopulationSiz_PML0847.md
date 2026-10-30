---
species:
  - "Gila cypha"
  - "Gila elegans"
  - "Xyrauchen texanus"
common_name:
  - "Humpback chub"
  - "Bonytail chub"
  - "Razorback sucker"
family: "Cyprinidae (humpback and bonytail chub); Catostomidae (razorback sucker)"
habitat: "Freshwater; large river channels, canyon-bound reaches, and reservoir habitats (e.g., Lake Mohave)"
ocean_basin: "N/A"
location: "Colorado River basin, USA (Arizona, Nevada, Utah, Wyoming, Colorado; Grand Canyon; Lake Mohave; Little Colorado River; Gila River system; Colorado River delta in Mexico)"
tags:
  - ichthyology
  - marine-biology
  - cyprinidae
  - catostomidae
  - population-genetics
  - conservation-genetics
  - endangered-species
title: "Long-term Effective Population Size of Three Endangered Colorado River Fishes"
source_id: "PML0847"
marsh_id: "PML0847"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. Garrigan, P. C. Marsh, T. E. Dowling (2001). Long-term Effective Population Size of Three Endangered Colorado River Fishes. Marsh Library ID: PML0847."
source_file: "Garrigan D. et al. 2001. Long term effective population size of thre endangered colorado river fishes.pdf"
text_extraction: "mixed"
---
# Long-term Effective Population Size of Three Endangered Colorado River Fishes

#ichthyology #marine-biology #cyprinidae #catostomidae

## Executive Summary

This study applies a maximum likelihood estimator of [[Long-Term Effective Population Size]], built on [[Coalescent Theory]], to mitochondrial DNA (mtDNA) data from three endangered [[Colorado River Fishes]]: [[Humpback Chub]], [[Bonytail Chub]], and [[Razorback Sucker]]. Unlike common temporal-allele-frequency methods, which capture only recent drift, this approach reconstructs historical demography. The three species show three different outcomes: the humpback chub retains historical equilibrium variation despite recent declines, the razorback sucker shows signs of a historically large, expanding population with rare alleles surviving, and the bonytail chub shows a bottleneck signal suggesting recent losses of variation. The authors conclude the results match known natural history and are useful for endangered species management.

## Background & Description

Effective population size (N_e) is the size of an idealized population experiencing the same genetic drift as the observed population. N_e is typically smaller than census size because of factors such as variance in family size and temporal fluctuations. Low N_e raises the risk of inbreeding depression and reduces the capacity to adapt to environmental change, which makes it central to endangered species management.

The authors use the [[Fluctuate Software]] package, which implements the coalescent framework of Kuhner et al. (1998) to jointly estimate long-term female effective size (N_ef) and an exponential growth rate. Historical demography is classified as stable, expanding, declining, or cyclic.

The three species were chosen because all are critically endangered, their historical distribution and abundance are reasonably well understood, and adequate genetic data existed.

- **Humpback chub:** Historically restricted to canyon-bound reaches in and above Grand Canyon. The largest known population, in and near the Little Colorado River, may hold roughly 10,000 adults. It is the only one of the three with apparently self-sustaining populations.
- **Bonytail chub:** Once widespread in large streams but extirpated from most of its range. It is seen regularly only in [[Lake Mohave]], and census estimates cannot be made because captures are so few.
- **Razorback sucker:** Historically the most abundant of the three. The largest remaining population, in Lake Mohave, fell from perhaps hundreds of thousands to fewer than 10,000 fish in about 50 years.

Captive propagation of bonytail chub and razorback sucker began in the early 1980s, with hundreds of thousands to millions of young distributed. Repatriates are routinely recaptured in Lake Mohave, but recruitment failure remains nearly total across known populations. Lifespans of 20 to 50 years mean historical genetic variation may have been only modestly lost so far.

## Ecological & Environmental Context

The main drivers of decline were habitat destruction (dam and reservoir construction, water diversion, desiccation) and the introduction of predatory and competitive non-native fishes. These caused recruitment failure and reduced both abundance and distribution (Minckley 1990; Minckley et al. 1991). Predation on early life-history stages is identified as a primary obstacle to recovery.

Historical distribution for razorback sucker extended basin-wide, from Wyoming to the Colorado River delta in Mexico, and throughout the Gila River system of central Arizona and New Mexico. Native Americans and early settlers used it as food and fertilizer, and commercial fisheries operated at several sites.

The humpback chub decline is attributed mainly to localized reductions and extirpation of historically connected subpopulations (Gerber et al., in press). Loss of immigrant haplotypes and genetic drift in isolated subpopulations are cited as relevant processes.

Bonytail chub was extirpated from central Arizona and became functionally extinct in the upper Colorado River system by the 1980s. Hatchery broodstock for the Lake Mohave stock were founded from a very small effective number, estimated at 3.5 to 9.5 individuals (Hedrick et al., 2000).

## Key Findings

**Methods and data**
- Sample sizes: humpback chub (n = 18, Little Colorado/Colorado confluence, Grand Canyon); bonytail chub (n = 16, Lake Mohave); razorback sucker (n = 49, Lake Mohave).
- Humpback and bonytail chub were assayed for two ND2 fragments by single-stranded conformation polymorphism (SSCP) and direct sequencing. Razorback sucker was assayed using a single cytochrome b fragment.
- Models assumed a transition/transversion ratio of 2.0 because no transversions were observed. Significance was assessed using 95% confidence intervals of likelihood curves, and Tajima's D was tested with 1,000 coalescent simulation replicates.
- The authors assumed equal sex ratios, so N_e = 2N_ef.

**Humpback chub**
- Five composite ND2 haplotypes, six mutations (one singleton), and all transitions with no amino acid changes.
- Average of 1.54 nucleotide substitutions between pairwise comparisons.
- Tajima's D = -0.3935 (p = 0.359), not significant: consistent with constant size at mutation-drift equilibrium.
- N_ef ≈ 150,000 under the growth model (mutation rate 2 × 10⁻⁸ per nucleotide), and ≈ 97,500 under constant size; the two estimates do not differ significantly.

**Bonytail chub**
- Only three ND2 haplotypes, with frequencies of 31.3%, 25.0%, and 43.7%.
- Average of 2.92 nucleotide substitutions between pairwise comparisons, nearly double that of humpback chub, with six mutations (none singletons) and one amino acid change.
- Tajima's D = 1.909 (p = 0.028), significantly positive, interpreted as a possible population bottleneck or balancing selection.
- N_ef ≈ 62,000 with size change and ≈ 89,500 under constant size; the growth rate is significantly negative.

**Razorback sucker**
- Ten cytochrome b haplotypes, 13 mutations (four singletons), and two amino acid substitutions.
- The most frequent haplotype accounts for 59.2% of individuals.
- Average of 1.50 nucleotide substitutions between pairwise comparisons.
- Tajima's D = -1.46 (p = 0.058), marginally non-significant but indicative of a trend toward an excess of rare mutations, consistent with expansion.
- N_ef ≈ 940,000 under size change, significantly higher than ≈ 669,000 under constant size; the growth rate is significantly positive.

**Synthesis (Table 1 summary)**

| Species | Gene | Sample size | Mutations | Singletons | N_ef (constant) | N_ef (growth) | Growth rate |
|---|---|---|---|---|---|---|---|
| Humpback chub | ND2 | 18 | 6 | 1 | 97,500 | 149,966 | 440.78 ± 501.49 |
| Bonytail chub | ND2 | 16 | 6 | 0 | 89,500 | 61,900 | -394.12 ± 232.86 |
| Razorback sucker | cyt b | 49 | 13 | 4 | 669,000 | 940,300 | 380.92 ± 198.67 |

**Interpretation**
- **Humpback chub:** Historical equilibrium variation is retained despite recent decline, possibly because the Grand Canyon subpopulation has been relatively isolated and has not yet lost variation.
- **Razorback sucker:** The excess of rare mutations points to a historically large, expanding population (consistent with a post-Pleistocene northward expansion; Dowling et al., 1996a). Rare alleles survive in the steadily declining Lake Mohave population, so the N_e estimate may be conservative.
- **Bonytail chub:** The bottleneck signal suggests recent losses of historical variation. Managers have little room to retain historical diversity. The authors cannot rule out a hatchery founder effect, a recent species-wide decline, or a long-term contraction.

**Methodological conclusions**
- Coalescent estimators make more efficient use of sequence data and have lower variance than summary-statistic methods, which matters for small endangered-species samples (Felsenstein 1992).
- Coalescent methods estimate N_e over a long evolutionary window and do not provide a current N_e. Temporal allele-frequency methods estimate current N_e. The authors argue the two approaches complement each other.
- Adding more polymorphic DNA sites improves the reliability of the estimate.