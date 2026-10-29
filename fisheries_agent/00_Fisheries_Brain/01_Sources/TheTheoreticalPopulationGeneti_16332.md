---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [population-genetics, evolutionary-theory, theoretical-review]
title: "The theoretical population genetics of variable selection and migration"
source_id: "16332"
minckley_id: "16332"
source_citation: "J. Felsenstein (1976). The theoretical population genetics of variable selection and migration. Annual Review of Genetics 10: 253-280. Minckley Library ID: 16332."
source_file: "16332.pdf"
text_extraction: "ocr"
---
# Theory of Spatial and Temporal Variation in Population Genetics

#population-genetics #evolutionary-theory #theoretical-review

## Executive Summary

This document is a theoretical review by Joseph Felsenstein (Department of Genetics, University of Washington), published in the *Annual Review of Genetics* (1976, vol. 10, pp. 253–80). It covers how temporal variation in selection and spatial structure (migration, subdivision, clines) shape genetic variation in populations. It is not an aquatic or ichthyological study: it names no fish species, habitats, or field sites, and its models are abstract one- and two-locus systems. The first page is reference-list debris from a preceding *Drosophila* article (Gehring, 1976) and is not analyzed.

The review covers five areas: selection varying with time, geographic effects (island and stepping-stone models), clines, genetic drift and migration, and combined drift, migration and selection. Its central themes are that geometric-mean fitness governs fate under random selection, that protected polymorphism requires geometric-mean overdominance, and that migration can swamp local adaptation above a threshold rate.

## Background & Description

The review is framed as a survey of contemporary theoretical [[Population Genetics]] and identifies two active fronts: variable selection coefficients and the effects of geography. It cites related reviews by Christiansen & Feldman (1975), Hedrick (1976) and Gould & Johnston (1972). The reference list contains well over 150 entries, many of them classic papers by Dempster, Haldane, Fisher, Wright, Malécot, Kimura and Maruyama.

The review's formal basis is discrete-generation recursion for haploid and diploid genotypes, with fitnesses (w, v) that vary randomly or cyclically. Its theory of continuous space relies on the [[Stepping-Stone Model]] and related continuum approximations.

## Ecological & Environmental Context

The document addresses environmental variation only in abstract terms: random or cyclic temporal fluctuations in fitness, "coarse-" versus "fine-grained" environments (Levins), and spatially distinct "pockets" of adaptation. It does not discuss any specific ecosystem, water body, species assemblage or environmental measurement, so no aquatic habitat, water chemistry or ecological community data are reported.

Relevant conceptual links to environmental heterogeneity include:
- [[Levins Coarse-Grained Model]], on polymorphism in heterogeneous environments
- [[Environmental Pocket]], in which a locally favored allele persists within a larger region favoring another allele
- [[Isolation By Distance]], the spatial pattern of genetic correlation with distance

## Key Findings

**1. Temporal variation in selection (infinite populations)**
- Under random fitness variation, the allele with the higher geometric-mean fitness is certain to quasi-fix ([[Dempster Result]]). With equal geometric means, the chance of ultimate increase is 50%.
- In continuous time, the allele with the higher arithmetic-mean Malthusian parameter quasi-fixes ([[Gillespie Continuous-Time Model]]). Autocorrelation of fitness does not change this rule.
- In haploids, temporal variation cannot maintain polymorphism.
- In diploids, a [[Protected Polymorphism]] requires [[Geometric Mean Overdominance]]. Arithmetic-mean (marginal) overdominance is a stronger condition.
- Under cyclic selection, the same geometric-mean criterion applies, although Dempster showed polymorphism can also be maintained without arithmetic-mean overdominance.
- Levins' hypothesis that temporal variation favors polymorphism is undercut: geometric-mean overdominance can lower mean fitness, so selection does not maximize it.

**2. Finite populations**
- Kimura's early quasi-fixation formula was withdrawn. Errors in diffusion approximations were identified by Jensen & Pollak and corrected by later authors.
- Hedrick's simulations show that polymorphisms protected against fluctuating selection are poorly protected against genetic drift.

**3. Geographic structure: island models**
- Haldane's one-island model: a locally favored allele is swamped when migration rate m exceeds the selective advantage s. Local differentiation is most robust for autosomal dominant or sex-linked recessive alleles.
- Levene's model (random mating among all islands, then random redistribution of offspring): a sufficient condition for protected polymorphism is harmonic-mean overdominance, which is weaker than marginal overdominance.
- Two-island models: Moran (1959) showed polymorphism is maintained below a critical migration rate. Maynard Smith, Bulmer, Deakin and Christiansen extended the conditions to multi-island cases.
- Karlin & McGregor's "method of small parameters" supports the principle that two locally adapted alleles can coexist if migration is sufficiently restricted. Increasing migration can cause a threshold collapse of polymorphism.
- Gillespie (1975) found that spatial variation maintains polymorphism more readily than temporal variation.

**4. Linkage effects**
- Migration generates linkage disequilibrium when populations differ in gene frequency (Nei & Li 1973; Li & Nei 1974).
- Christiansen & Feldman (1975) found that modifiers reducing migration are favored even without fitness or frequency differences, if the phase of disequilibrium differs between populations.
- Gillespie & Langley's additive model produces no linkage disequilibrium because epistasis cancels the coupling disequilibrium created by migration.

**5. Clines**
- Fisher (1937) described a wave of advance for a favorable allele. The wave front length scales with σ/√s (rendered as "o/vs" in the scan), and the solution selected is the one with minimum speed of advance.
- Haldane (1948) modeled a step cline; Fisher (1950) modeled a ramp. Fisher's ramp cline shape lies between a logistic curve and the integral of the normal distribution.
- Slatkin (1973) defined a characteristic cline length, λ = σ/√s. Ramp widths smaller than λ have little effect on cline slope.
- Nagylaki (1975) showed that pocket collapse above the migration threshold is absolute, so Hanson's (1966) persistence at low frequency was a numerical artifact. For recessive alleles, the maximum pocket frequency approaches about 0.5 before abruptly falling to zero.
- Karlin & Richter-Dyn (1976) analyzed clines of finite total length in a generalized two-range environment.

**6. Genetic drift and migration**
- Wright's one-island model: the island gene frequency distribution is U-shaped if both 4Nm·Q and 4Nm·(1−Q) are less than 1. The island matches the continent when 4Nm ≫ 1.
- Moran (1959) showed that in a haploid island model with Nm/(n−1) ≥ 1 immigrants per population, heterozygosity is lost at the rate of a panmictic population of size Nn.
- For stepping stones, a transition occurs at a threshold migration rate. Above it, the population behaves as panmictic with heterozygosity loss rate 1/(2N_T), where N_T is total species population size.
- Rates of fixation below the threshold (n = number of colonies, m = migration rate):
  - one-dimensional circle: approximately π²m/n²
  - line: half the circle value
  - two-dimensional torus: approximately m/(2n)
  - two-dimensional rectangle: approximately m/(4n)
- The critical value of Nm is n/m for a line but 1 for a rectangle. Maruyama (1972/1973) concluded that a sufficiently widely distributed one-dimensional species will show local differentiation, whereas a two-dimensional species under Nm > 1 behaves as panmictic.
- Felsenstein's critique (1975, "A Pain in the Torus"): continuum models rely on a fallacious probability term 1/(ρ dx) that is infinite, so these models are approximations at best. He calls for a proper model of continuously distributed organisms with finite density and migration.

**7. Drift, migration and selection combined**
- Slatkin & Maruyama (1975) and Felsenstein (1975) found that drift adds random wobble to clines and causes a small tendency to flatten the cline of average gene frequencies.
- Pollak (1974) showed that the conditions for a single mutant to establish are not yet known to match the conditions for persistence of a locally adapted pocket.

**Overall conclusion:** Geometric-mean fitness governs fixation under varying selection. Migration relative to selection sets both the maintenance of polymorphism and a threshold beyond which local adaptation collapses. Drift is a secondary modifier of these deterministic results.

---

Cross-links: [[Population Genetics]], [[Protected Polymorphism]], [[Geometric Mean Overdominance]], [[Dempster Result]], [[Gillespie Continuous-Time Model]], [[Quasi-Fixation]], [[Haldane Cline]], [[Fisher Wave Of Advance]], [[Levene Model]], [[Island Model]], [[Stepping-Stone Model]], [[Isolation By Distance]], [[Linkage Disequilibrium]], [[Genetic Drift]], [[Gene Flow]], [[Environmental Pocket]], [[Karlin Mcgregor Method]], [[Slatkin Characteristic Length]], [[Nagylaki Migration Threshold]], [[Maruyama Fixation Rates]]