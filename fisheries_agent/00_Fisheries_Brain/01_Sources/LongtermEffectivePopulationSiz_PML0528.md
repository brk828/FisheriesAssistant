---
species:
  - Gila cypha
  - Gila elegans
  - Xyrauchen texanus
common_name:
  - Humpback Chub
  - Bonytail Chub
  - Razorback Sucker
family: Cyprinidae (Gila spp.); family for Xyrauchen not stated
habitat: Large rivers and canyon-bound reaches of the Colorado River system (freshwater)
ocean_basin: N/A
location: Colorado River basin (Grand Canyon, Lake Mohave, Little Colorado River, Westwater Canyon, Black Rocks, Green River)
tags: [ichthyology, marine-biology, cyprinidae, effective-population-size, conservation-genetics, endangered-species]
title: "Long-term Effective Population size of Three Endangered Colorado River Fishes"
source_id: "PML0528"
marsh_id: "PML0528"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. Garrigan, P. C. Marsh, T. E. Dowling (2002). Long-term Effective Population size of Three Endangered Colorado River Fishes. Marsh Library ID: PML0528."
source_file: "Daniel Garrigan. Marsh P.C. Dowling T.E. 2002. Long-ter effective population size of three endangered colorado rier fishes.pdf"
text_extraction: "mixed"
---
# Long-Term Effective Population Size of Three Endangered Colorado River Fishes

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This study applies a [[Coalescent Theory]]-based maximum likelihood estimator to estimate [[Long-Term Effective Population Size]] (Nf, female effective size) in three federally endangered fishes of the [[Colorado River Basin]]: [[Humpback Chub]], [[Bonytail Chub]] and [[Razorback Sucker]]. Most practical estimators detect only recent drift and miss long-term abundance fluctuations, so the authors use [[Mitochondrial DNA]] (mtDNA) sequences to reconstruct historical demography. Each species shows a different pattern: humpback chub appears to retain its historical equilibrium variation despite recent declines, razorback sucker shows a large, expanding historical population with rare alleles still surviving, and bonytail chub has likely lost much of its historical variation through recent severe decline.

## Background & Description

Effective population size (Ne) is the size of an idealized population that experiences the same magnitude of genetic drift as the observed population. Ne is typically smaller than census size because of factors such as variance in family size and temporal fluctuations in population size. Low Ne raises the risk of inbreeding depression, fixation of deleterious recessive alleles, and reduced capacity to adapt to habitat change, competitors, predators and parasites.

Most existing methods use temporal allele-frequency change and therefore estimate current Ne. The authors instead use DNA sequence data and the coalescent framework of Kingman (1982), implemented in the [[FLUCTUATE]] program (Kuhner et al. 1998), to jointly estimate long-term Nf and the exponential growth rate. Historical demography is classed as stable, expanding, declining or cyclic.

The three species were chosen because all are in critical danger of extinction, their historical distribution and abundance are reasonably well understood, and suitable genetic data existed.

- **Humpback Chub:** restricted to canyon-bound reaches in and upstream of [[Grand Canyon]]. The largest known population, in and near the [[Little Colorado River]], may hold up to 10,000 adults. It is the only one of the three with apparently self-sustaining populations.
- **Bonytail Chub:** once widely distributed in larger streams; now extirpated from most of its range. It is regularly found only in [[Lake Mohave]], and captures are too few for census estimates.
- **Razorback Sucker:** historically the most abundant of the three, distributed basin-wide from Wyoming to the Colorado River delta in Mexico. The largest remaining population, in Lake Mohave, fell from perhaps hundreds of thousands to fewer than 10,000 fish in about 50 years.

Habitat destruction (dams, reservoirs, water diversion, desiccation) and non-native predatory and competitive fishes caused recruitment failure. Captive propagation began in the early 1980s for bonytail and razorback sucker, with hundreds of thousands to millions of young distributed, but stocking outside Lake Mohave was largely unsuccessful. All three species are federally listed as endangered. Lifespans are long (20 to 50 years), so genetic losses from recent declines may be small so far.

## Ecological & Environmental Context

**Population decline and recruitment failure.** All three species show near-total recruitment failure in known populations, mainly from predation on early life stages. This is expected to lead to extinction without intervention. Because adults live long, the genetic consequences of recent declines may lag behind the demographic ones.

**Historical population structure.** Humpback chub decline is attributed mainly to localized reductions and extirpation of historically connected subpopulations. The authors suggest that the relatively isolated Grand Canyon subpopulation sampled may not yet have lost variation through drift and loss of immigrant haplotypes.

**Post-Pleistocene expansion.** Razorback sucker's expansion pattern is consistent with a northward, post-Pleistocene range expansion proposed by Dowling et al. (1996a). Historically it was used as food and fertilizer by Native Americans and early settlers, and commercial fisheries operated at several sites (Minckley 1973).

**Hatchery influence on bonytail.** Hatchery-produced bonytail from a few wild-caught adults were stocked into Lake Mohave from the early 1990s. Hedrick et al. (2000) estimated the effective founding size of this broodstock at 3.5 to 9.5 individuals. This makes it hard to tell whether the observed bonytail variation reflects a founder event, a species-wide decline, or long-term population contraction.

## Key Findings

### Methods

- **Sampling:** Humpback chub (n = 18) from the confluence of the Little Colorado and Colorado rivers in Grand Canyon, Coconino Co., Arizona. Bonytail chub (n = 16) and razorback sucker (n = 49) from Lake Mohave, Mohave Co., Arizona.
- **Genetic markers:** Humpback and bonytail chub were assayed for two single-stranded conformation polymorphism (SSCP) fragments from the NADH dehydrogenase subunit 2 (ND2) gene. Razorback sucker was assayed for a single fragment from the 3' end of the cytochrome b gene. Direct sequencing followed.
- **Analysis:** FLUCTUATE estimated Nf and growth rate by a two-step maximum likelihood approach, using a Metropolis-Hastings sampler (10 short chains of 100,000 steps and 2 long chains of 200,000 steps). A constant-size (growth rate = 0) model served as the null. Assumptions included a transition/transversion ratio of 2.0 and a mutation rate of 2 × 10⁻⁸ per nucleotide. Summary statistics (singletons, average pairwise differences, [[Tajima's D]]) were computed with DnaSP, and significance of Tajima's D was tested by coalescent simulation with 1,000 replicates.

### Summary of Results (Table 1)

| Parameter | Humpback Chub | Bonytail Chub | Razorback Sucker |
|---|---|---|---|
| Sample size | 18 | 16 | 49 |
| Sites | 790 | 763 | 311 |
| Alleles (haplotypes) | 5 | 3 | 10 |
| Mutations | 6 | 6 | 13 |
| Singletons | 1 | 0 | 4 |
| Nf, constant size | 97,500 | 89,500 | 669,000 |
| Nf, growth model | 148,966 | 61,900 | 940,300 |
| Growth rate (± CI) | 440.78 ± 501.49 (not significant) | −394.12 ± 232.86 | 380.92 ± 198.67 |

### Humpback Chub

- Five composite ND2 haplotypes and six transitional mutations, one of them a singleton. No amino acid changes.
- Average of 1.54 nucleotide substitutions between pairwise sequence comparisons.
- Tajima's D was non-significant (about −0.39, p = 0.359). Polymorphism fits a constant-size population at mutation-drift equilibrium.
- Long-term Nf is approximately 150,000 under the growth model and about 97,500 under constant size. The two estimates overlap within confidence intervals, so they do not differ significantly. The growth rate does not differ significantly from zero.
- Under a faster teleost mutation rate (five times the mammalian rate, per Kocher et al. 1989), Nf would be higher.

### Bonytail Chub

- Three ND2 haplotypes with nearly equal frequencies. Six transitional mutations, none singletons, and one amino acid substitution.
- Average of 2.92 nucleotide substitutions per pairwise comparison, almost double that of humpback chub for a similar number of mutations.
- Tajima's D was significantly positive (about 1.91, p = 0.029), consistent with a population bottleneck or possibly balancing selection. The authors favour a bottleneck, since rare alleles are lost and the surviving divergent alleles should be at relatively even frequencies.
- Nf is approximately 62,000 under the growth model and about 89,500 under constant size. The growth rate is significantly negative, and the two Nf values differ significantly.

### Razorback Sucker

- Ten cytochrome b haplotypes, 13 mutations (four singletons), and two amino acid substitutions.
- Average of 1.50 nucleotide substitutions per pairwise comparison, similar to humpback chub.
- Tajima's D was −1.46 (p = 0.058), marginally non-significant but indicative of an excess of rare mutations, consistent with population expansion or directional selection.
- Nf is approximately 940,300 under the growth model, significantly higher than the constant-size estimate of about 669,000. The growth rate is significantly positive.

### Interpretation

- The three species illustrate three possible outcomes of long-term Ne analysis: retained historical variation (humpback chub), expansion with rare alleles still present (razorback sucker), and loss of substantial historical variation (bonytail chub).
- The results agree with known natural history. The authors note that the expansion signal conflicts with recent census declines, which they reconcile by the species' large, widely dispersed pre-human population. For razorback sucker, rare alleles surviving in the declining Lake Mohave population may mean the estimate is conservative, and some variation may already have been lost.
- For bonytail chub, the authors caution that hatchery founder effects, species-wide decline and long-term contraction cannot be separated with these data.

### Methodological Points

- Long-term Ne estimated from mtDNA and current Ne from temporal allele-frequency methods cover very different time scales, so the two approaches are complementary.
- Coalescent-based estimators make more efficient use of sequence data and have lower variance than summary-statistic estimators. This matters for small samples typical of endangered species (Felsenstein 1992).
- The probability that adding one more sample would change the final coalescence time was 0.006 (humpback chub), 0.007 (bonytail chub) and 0.001 (razorback sucker).
- More polymorphic sites improve the reliability of the estimate, because the pattern of polymorphisms ultimately resolves genealogical relationships (Kuhner et al. 1995).