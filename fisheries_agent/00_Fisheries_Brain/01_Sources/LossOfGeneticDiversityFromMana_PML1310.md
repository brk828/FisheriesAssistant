---
species: N/A
common_name: N/A
family: N/A
habitat: Captive and managed populations (zoos, intensively managed wildlife parks, nature preserves)
ocean_basin: N/A
location: N/A
tags: [conservation-genetics, population-genetics, captive-breeding, computer-simulation]
title: "Loss of Genetic Diversity from Managed Populations: Interacting Effects of Drift, Mutation, Immigration, Selection, and Population Subdivision"
source_id: "PML1310"
marsh_id: "PML1310"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. C. Lacy (1987). Loss of Genetic Diversity from Managed Populations: Interacting Effects of Drift, Mutation, Immigration, Selection, and Population Subdivision. Conservation Biology 1(2):143-158. Marsh Library ID: PML1310."
source_file: "Lacy R.C. 1987. loss of genetic diversity from managed populations .pdf"
text_extraction: "text"
---
# Loss of Genetic Diversity from Managed Populations

#conservation-genetics #population-genetics #captive-breeding

## Executive Summary

This paper, by Robert C. Lacy of the [[Chicago Zoological Society]] (Brookfield, Illinois), uses a stochastic [[Computer Simulation]] to examine how [[Genetic Drift]], [[Mutation]], [[Immigration]], [[Natural Selection]] and [[Population Subdivision]] interact to control the loss of genetic variation in small, managed populations such as those held in zoos. The model tracks [[Heterozygosity]] for a two-allele locus across 25 replicate populations for 100 generations. Its main conclusions are that drift is the dominant force eroding variation in small captive populations, that immigration from a source population is the most effective counter-measure, and that subdividing a population helps preserve allelic diversity but slows gene flow and increases inbreeding within each unit unless migration is carefully controlled.

## Background & Description

- **Problem:** Natural habitats are shrinking, so many species survive as small populations. Zoo and managed-park populations can be shielded from predation, poor nutrition, severe weather, disease and difficulty finding mates, so they can be kept more stable than wild populations. However, small populations lose genetic variation over time.
- **Mechanisms of loss:** Without directional forces, allele frequencies follow a random walk (genetic drift), which is faster in small populations. Loss of variation increases [[Inbreeding Depression]] (lower viability and fecundity) and reduces evolutionary flexibility. This matters especially in captivity, where relaxed selection and strong selection for survival in a novel environment can rapidly deplete variation.
- **Limits of mutation:** New mutations are very slow to restore variation. The paper estimates only about one new mutation per thousand generations at a given locus in a typical captive population of 100 to 1,000 individuals.
- **Rationale for simulation:** Analytical models rely on approximations that are often too coarse for managers. The paper therefore uses simulation to explore interacting factors and to test conclusions that have not been adequately examined before.
- **Model basics:** The program was written in C for microcomputers. It simulates a constant-size, randomly mating population of hermaphroditic diploids with discrete generations. Parents are chosen according to relative [[Fitness]]. Migration, immigration from an outside population and mutation are applied at each step. Results are reported as expected heterozygosity within subpopulations and total ("gene diversity") heterozygosity across them.
- **Effective size:** Because the model is self-compatible and does not separate sexes, the actual population size equals the [[Effective Population Size]]. Sib-mating, unequal sex ratios or non-random mating reduce effective size, while equal family sizes can approach twice the real size.

## Ecological & Environmental Context

The paper concerns captive and intensively managed populations of organisms, mainly large vertebrates. It explicitly cites the [[Siberian Tiger]] and Speke's gazelle as examples of managed species. Captive environments differ from natural ones in several ways that the paper treats as important:

- Relaxed predation, food abundance and shelter may remove selective pressures that wild populations face.
- Captive populations may be fragmented into partly or wholly isolated subpopulations held by single zoos or groups of nearby zoos.
- Captive conditions may impose new selective pressures, and [[Domestication]] may occur through inadvertent selection.
- Most individuals in managed populations contribute little or nothing to future generations, so effective size can be much smaller than census size without careful management.

The paper's simulated populations are not modeled on any particular fish or aquatic system. Its relevance to aquatic taxa is not addressed in the text.

## Key Findings

**1. Drift and heterozygosity loss**
- In 25 simulated populations of 120 individuals over 100 generations, with no mutation, immigration or selection, three populations lost all heterozygosity at the locus. Six populations returned to their starting allele frequencies and heterozygosity.
- Mean final heterozygosity was 58.25% of the initial value (SE = 7.19%). This did not differ significantly from the 66% predicted by the standard drift equation H_t = (1 - 1/2N_e)^t H_0.
- The author stresses that these are statistical "expected" trajectories. Individual populations vary widely, so they should not be used to predict a specific population.

**2. Effect of population size**
- Simulated populations of 20, 40, 60, 120, 240 and 500 individuals were compared. Mean final heterozygosities did not differ significantly from theoretical values for any size.
- Smaller populations lost variation faster, as expected under drift.

**3. Mutation**
- Mutation can offset drift only at rates far higher than those observed in nature (typically 10⁻⁴ to 10⁻⁵ per locus per generation for eukaryotes, and 10⁻⁶ to 10⁻⁸ for some other groups).
- At a mutation rate of 10⁻⁴, mutation-drift equilibrium was reached at a heterozygosity of about 0.0048, roughly 1% of the initial value. This is about an order of magnitude lower than commonly observed in natural vertebrate populations.
- The minor variation added by mutation over human time spans may be counterproductive for preserving the genetic uniqueness of a founding population.

**4. Immigration**
- Immigration is more effective than mutation because immigration rates can be much higher and, importantly, reintroduce alleles that existed in the founding stock.
- A rate of 0.1 immigrants per generation had no biologically significant effect. Rates as low as 0.5 per generation were beneficial for many captive programs.
- A population of 20 individuals receiving one immigrant per generation retains almost as much variation as a population an order of magnitude larger.
- One immigrant every two generations is beneficial, and five or more per generation virtually halts drift in the captive population.
- Sporadic immigration at the same long-term average rate can be as effective as regular immigration.

**5. Selection**
- Strong directional selection (fitness differential of 20%) and symmetrical disruptive selection fix alleles rapidly, depleting variation. Balancing selection maintains allele frequencies and heterozygosity.
- A 5% fitness differential has little effect over 5 to 10 generations.
- Weak selection (for example, fitness differences of 1% to 2%) affects heterozygosity only slightly, against the background noise of drift. Selection is effective over drift when the product of effective population size and selection coefficient is much greater than one.
- Because drift overwhelms weak selection in small populations, selection on captive populations is generally inefficient, so some captive-breeding concerns may not be realized.

**6. Population subdivision**
- Dividing 120 individuals into 1, 3, 5 or 10 fully isolated subpopulations sharply reduces within-subpopulation heterozygosity. Total gene diversity is better maintained, because between-subpopulation differences preserve variation.
- As few as 0.5 inter-subpopulation migrants per generation (overall, not per subpopulation) substantially reduce inbreeding within subpopulations.
- Five migrants per generation were not sufficient to bring a subdivided population to effective panmixia. Twenty migrants per generation also failed to prevent loss of diversity within and divergence among subpopulations in simulations (not shown).
- Ten subpopulations of 12 individuals with 5 to 10 migrants per generation may lose no more total diversity than a single panmictic population of the same overall size, while showing moderate inbreeding within each unit.
- Subdivision helps preserve rare alleles. The probability that at least one of 10 subpopulations retains a neutral allele with initial frequency 0.01 is about 10 times that for a single panmictic population.

**7. Interaction of selection and subdivision**
- Subdivision increases drift within subpopulations, which weakens selection's effectiveness and can slow inadvertent domestication.
- Subdivision can, however, make balancing selection less effective and can drive populations away from balanced equilibria, causing loss of adaptive variation through inbreeding depression.

**8. Management implications**
- The simulations are intended to inform decisions, not prescribe a fixed population size or structure.
- Captive populations should aim to maintain effective size, because individuals not contributing to future generations reduce it.
- Current proposals for minimum sizes, such as an effective size of 500 for mutation-drift balance (Franklin 1980) and a target of 90% retained heterozygosity for 200 years (Soulé et al. 1986), are discussed critically. The mutation-drift equilibrium model may be misleading because equilibrium maintains heterozygosity but not the genome itself.
- Fuerst and Maruyama argue that allelic diversity is lost faster than heterozygosity during bottlenecks, so larger founding populations are needed to preserve rare alleles. Lacy notes that subdivision may be the only way to preserve allelic diversity in small populations.
- The paper suggests that the optimal plan depends on time scale. Subdivision carries a genetic cost in early generations, because inbreeding is especially rapid over the first 10 to 20 generations. Its benefits appear only after 10 to 20 generations.
- For short-term plans, subdivision offers no genetic advantage, although isolating smaller groups may help prevent catastrophic disease outbreaks. For very long-term management (30 or more generations), the paper suggests dividing the population into units of roughly 20 breeding individuals and carefully regulating migration between them.
- Foose et al. (1986) recommended effective population sizes above 25, preferably 50 to 100, though the extract's wording on these values is partly garbled.
- Migration rates must be strictly controlled. Two or three unplanned movements per generation could turn genetic benefits into costs.
- Periodic immigration from wild stock can counter drift in captive populations. Migration from a large captive population into a small wild one can help endangered wild populations that would otherwise suffer excessive inbreeding.
- The author concludes that computer models such as the one presented can be used immediately to compare alternative management strategies, and that empirical data on genetic responses in target species are still needed.

**Cross-links:** [[Genetic Drift]], [[Heterozygosity]], [[Allelic Diversity]], [[Effective Population Size]], [[Inbreeding Depression]], [[Mutation]], [[Gene Flow]], [[Balancing Selection]], [[Directional Selection]], [[Population Subdivision]], [[Captive Breeding]], [[Computer Simulation]], [[Hardy-Weinberg Equilibrium]], [[Siberian Tiger]], [[Franklin Estimate]], [[Zoo Management]], [[Domestication]], [[Conservation Biology]]