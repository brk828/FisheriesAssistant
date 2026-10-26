---
species: Lepidomeda vittata
common_name: Little Colorado Spinedace
family: Cyprinidae
habitat: Freshwater streams and pools (north-flowing tributaries of the Little Colorado River)
ocean_basin: N/A
location: Little Colorado River watershed, Coconino, Apache, and Navajo Counties, Arizona, USA
tags: [ichthyology, marine-biology, cyprinidae, conservation-genetics, afl-p, population-genetics]
title: "An analysis of genetic variation in little Colorado spinedace (Lepidomeda vittata) using AFLP markers"
source_id: "19229"
minckley_id: "19229"
source_citation: "D. Greenberg, D. W. Blinn and P. Keim (n.d.). An analysis of genetic variation in little Colorado spinedace (Lepidomeda vittata) using AFLP markers. A report to Coconino National Forest Flagstaff, AZ. Minckley Library ID: 19229."
source_file: "19229.pdf"
text_extraction: "ocr"
---
# AFLP-Based Analysis of Genetic Variation in Little Colorado Spinedace (*Lepidomeda vittata*)

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This report, prepared for the [[Coconino National Forest]], uses [[AFLP]] (Amplified Fragment Length Polymorphism) markers to measure genetic diversity and population structure in the federally threatened [[Little Colorado Spinedace]]. Samples came from three natural populations in the Little Colorado River (LCR) drainage, [[Rudd Creek]], [[Chevelon Creek]], and [[East Clear Creek]], plus a captive population at the [[Arboretum Pond]] in Flagstaff, Arizona.

The study found substantial population structure among the wild populations (θ = 0.5162; PHIst = 0.555). The captive population was genetically very close to its source population, Rudd Creek (θ = 0.0345; PHIst = 0.023). The authors interpret this as evidence that the captive program succeeded. Their central management recommendation is that stocks from different drainages should not be mixed.

## Background & Description

*Lepidomeda vittata* is a native cyprinid minnow of the tribe Plagopterini. It now occupies disjunct populations in north-flowing LCR tributaries. Surveys from the late 1800s onward indicate the species was once more widely distributed, possibly including the Zuni River system. Its range and numbers declined after 1966.

The authors attribute the decline mainly to two anthropogenic pressures:

- **Water use:** Agricultural and civil withdrawals altered flow patterns and degraded sensitive habitats.
- **Non-native species:** Introduced predators and competitors displaced native fish. [[Rainbow Trout]] are identified as a key threat through predation and habitat displacement.

Other stressors include piscicide use to remove non-natives and pollutant inputs from agriculture and industry.

The species was listed as threatened in 1987. An earlier attempt to establish a captive population with 44 fish from Rudd Creek at the Flagstaff Arboretum pond failed after three years, possibly due to disease. A new captive program was planned for the same site.

The report frames genetic diversity as central to management. Greater diversity is linked to fitness and the ability to respond to environmental change, and the authors argue that a diverse founder population should buffer the bottleneck of captive breeding.

## Ecological & Environmental Context

**Study system.** The LCR spinedace persists in small, semi-isolated stream reaches. Several streams have intermittent flow, so fish concentrate in isolated pools during dry periods. The authors suggest this pooling may increase relatedness among fish within a pool.

**Dry-year dynamics.** Surveys show sporadic annual abundance. The authors propose a cycle of bottleneck events in dry years, followed by population recovery and migration in high-flow years. They argue this cycle may maintain overall diversity.

**Comparative diversity.** Allozyme-based estimates for many fish are low. The report cites a mean heterozygosity of 0.0513 across 51 fish species (Nevo, 1978), and values below 0.05 for 85% of western desert fish samples (Echelle, 1991). By these comparisons, *L. vittata* AFLP values are high.

**Predator-prey relationships.** Trout occupy the upper reaches of streams such as [[Nutrioso Creek]]. Spinedace are pushed into lower, more turbid, sediment-laden habitat. Trout predation has been visually confirmed (Blinn et al., 1993). Competition has not been tested, although diet and habitat overlap are noted.

**Other southwestern fish.** The report notes that native [[Spikedace]] and [[Loach Minnow]] were displaced by [[Red Shiner]]. Declines in [[Sonoran Topminnow]] and [[Desert Pupfish]] were associated with increases in [[Mosquitofish]].

## Key Findings

### Methods

- **Sampling:** Fish were captured by shocking or seining. A small caudal fin clip was preserved in 95% ethanol. Samples were taken under Coconino National Forest licence and an IACUC-approved protocol.
- **Sample sizes:**
  - Rudd Creek (RC): n = 28, collected July 1996
  - Chevelon Creek (CH): n = 26, collected 1997–1998
  - East Clear Creek (ECC): n = 24, collected 1997–1998
  - Arboretum (AB, captive): n = 30, collected summer 1995
  - Total: 108 individuals
- **Marker generation:** AFLP used EcoRI and MseI restriction enzymes with two selective PCR steps. Fifteen +3/+3 primer combinations were used. Products were separated on 6% denaturing polyacrylamide gels and scored as presence or absence.
- **Analyses:**
  - Jaccard similarity with UPGMA clustering (NTSYS-pc)
  - Population statistics in TFPGA, including Nei heterozygosity and proportion polymorphic
  - Reynolds coancestry distances with bootstrapping (1000 replicates)
  - [[AMOVA]] in WINAMOVA
  - [[Weir and Cockerham Theta]] with jackknife and bootstrap confidence intervals
  - Monte Carlo Fisher's exact tests per locus, combined with Fisher's combined probability test

### Marker Quality

- 70 scoreable polymorphic markers came from 15 primer combinations, averaging 5 polymorphic bands per gel (range 2–8).
- 18 replicates were run to test scoring error. Eight showed differences, with a maximum of 5% and a mean of 1% (variance 0.0078).

### Genetic Diversity

| Population | n | Percent polymorphic (P) | Heterozygosity (H) |
|---|---|---|---|
| Rudd Creek (RC) | 28 | 65.71% | 0.2410 |
| Arboretum (AB) | 30 | 61.43% | 0.2186 |
| Chevelon Creek (CH) | 26 | 42.86% | 0.1604* |
| East Clear Creek (ECC) | 24 | 37.14% | 0.1531 |
| All four populations | 108 | 94.29% | 0.3492 |

*The Results text gives 0.1573 for CH, while Table 2 and the Discussion give 0.1604. The table value is reported here.

- RC has the highest diversity and ECC the lowest.
- AB is nearly as diverse as RC, and CH is similar to ECC.
- Heterozygosity across the four wild and captive populations averaged 0.1925.
- The authors conclude there is no evidence of inbreeding depression.

### Population Structure

- **UPGMA (all individuals):** AB and RC cluster closely. This pair separates from CH and ECC, which are themselves further differentiated.
- **Reynolds distances:**

| Comparison | Distance |
|---|---|
| RC vs. AB | 0.0351 |
| RC vs. CH | 0.8098 |
| RC vs. ECC | 0.9651 |
| CH vs. ECC | 0.4837 |
| AB vs. ECC | 1.0185 |

- **Bootstrap support:** The AB+RC versus CH+ECC split was recovered 100% of the time. The CH+ECC grouping was recovered 99.2% of the time.
- **AMOVA, four populations:** 55.51% of variation was among populations and 44.49% within (PHIst = 0.555).
- **AMOVA, AB versus RC:** 2.32% of variation was among populations (PHIst = 0.023).
- **Weir and Cockerham θ:**
  - All four populations: 0.5162 (jackknife SD 0.0378)
  - AB versus RC: 0.0345 (SD 0.0116)
- **Exact tests:** Every population pair differed significantly in marker frequencies (all p < 0.0001) except RC versus AB (χ² = 113.5715, df = 140, p = 0.9506). Combined over all loci, χ² = 922.652, df = 140, p < 0.0001.
- **Loci differing significantly (Table 6):** RC–AB 3, RC–CH 47, RC–ECC 56, AB–CH 51, AB–ECC 61, CH–ECC 23.
- **Comparison with prior work:** Tibbets et al. (1993) reported θ = 0.5542 from mtDNA haplotypes, which the authors take as consistent with the AFLP result.

### Captive Breeding Assessment

- The captive population grew rapidly, reaching about 9000 individuals, which the authors suggest swamped drift and inbreeding effects.
- Captive and source fish showed little genetic differentiation after three years (θ = 0.0345), which the authors read as program success.
- The original founder number of 44 fish is described as ideal, provided fish are collected from several pools to limit relatedness.

### Conservation Recommendations

1. **Do not mix stocks among drainages.** Each population appears genetically distinct, and mixing could homogenize populations and reduce overall fitness.
2. **Use RC or upper LCR stock for a single captive population,** since these have the highest diversity. Upper LCR populations also appear more stable and offer more transplant sites.
3. **Prioritize ECC,** given its very low numbers and sporadic distribution. The report's most recent plan was a captive population from ECC.
4. **Collect from several pools** within a stream system to reduce relatedness among founders.
5. **Protect all populations and their habitats,** because local adaptation and drift make each population a reservoir of unique alleles.
6. **Mix populations only as a last resort,** if a local population faces extinction.

The authors note that establishing three separate captive populations, one each from ECC, CH, and the upper LCR, would be ideal but may be infeasible due to funding and space.