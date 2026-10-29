---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [conservation-biology, population-viability-analysis, simulation-software, metapopulation, demography]
title: "NEMESIS: Conservation Biology Simulations"
source_id: "10954"
minckley_id: "10954"
source_citation: "M. Gilpin (1993). NEMESIS: Conservation Biology Simulations. Minckley Library ID: 10954."
source_file: "10954.pdf"
text_extraction: "ocr"
---
# NEMESIS: Conservation Biology Simulations User's Guide

#ichthyology #marine-biology #population-viability-analysis

## Executive Summary

This is the User's Guide for NEMESIS Version 1.0, a shareware package of True BASIC simulation programs written by Michael Gilpin (1993) for teaching and for exploratory conservation biology. The guide introduces the [[Conservation Biology]] field as a decision science, explains the role of models and discrete-time systems, and then walks the reader through roughly 40 programs covering deterministic and stochastic growth, [[Demography]], [[Population Genetics]], [[Island Biogeography]], [[Metapopulation Dynamics]] and [[Population Viability Analysis]] (PVA). The author stresses that NEMESIS is an educational "box of tools" and is not adequate for a robust PVA on its own.

The document contains no fish or aquatic data. Its aquatic relevance is limited to passing examples, such as the [[Concho River Water Snake]] PVA and fish-population growth in the Ricker model. The non-fish content is therefore summarized below.

## Background & Description

- **Author and scope:** Michael Gilpin, Bozeman, Montana. Programs were developed at the University of California, San Diego, and in workshops for graduate students and managers. Source code was about 500 KB and was developed on Macintosh because it was too large to compile on DOS.
- **Platforms:** Written in True BASIC; runs on DOS (640 KB RAM, EGA/VGA preferred, sluggish below 16 MHz) or Macintosh (640 x 480 monitor). Black-and-white monitors are adequate.
- **Licensing:** Shareware fee of $30.00; site licenses for classroom use. No copy protection. Source code is compiled and not user-accessible, though some code excerpts are printed in the guide.
- **Interface:** A pop-out control box offers keys C (continue), R (repeat), B (back), S (start), E (exit), I (information) and H (help). Mouse input is used to reshape lines in several programs.
- **Structure:** Programs are grouped into submenus: Mathematical Background, Population Dynamics, Population Trend and Size Estimation, Patch Dynamics and Island Biogeography, Stochastic Growth, Demography, Community Ecology, Genetics, and Space and Metapopulations.
- **Origin of the name and side notes:** The author notes that the "animolecule" screen saver was developed with developmental biologist William Loomis, illustrating stochastic genomic change.
- **Acknowledgments:** Support came from Southern California Edison, the U.S. Fish and Wildlife Service, the Wilderness Society, UC and Montana State University.

## Ecological & Environmental Context

**Conservation as decision science.** The author discusses definitions of [[Conservation Biology]] from Soulé (1980, "crisis science"), Beissinger (1989/1990), Hall (1987) and Naess (1985, deep ecology). He frames conservation biologists as people who make decisions at local-to-intermediate scales, such as which species to list as endangered, how to prioritize research, and what reserve configuration a species needs.

**The "Evil Quartet."** Following Diamond, the document identifies four main drivers of damage to natural systems: habitat loss and fragmentation, overharvesting, introduced predators and competitors, and the indirect consequences of these through ecological networks.

**Levels of decision making.** Genetic decisions are the most tractable and are mainly applied to captive or small populations. Population viability is described as a "tractable" middle level. Community and biodiversity-level predictions are much harder, with the author noting that a room-sized granivory experiment took 11 years to show major consequences.

**Lack of data and conservative bias.** The guide repeatedly argues for conservative models that may overestimate extinction risk, using examples such as the [[Northern Spotted Owl]] (studied for about a decade, generation time of several years) and [[Desert Tortoise]] reserve sizing (100,000 to 250,000 acres proposed by the author).

**Examples of species used:** [[Grizzly Bear]] (Greater Yellowstone Ecosystem, about 160 animals), Florida panther (about 40), [[California Condor]] (43 in 1991), [[Kentish Plover]] (Swedish island population, censused for almost 30 years), [[Stephens Kangaroo Rat]], [[California Gnatcatcher]], Colorado River squawfish, and [[Przewalski's Horse]] (GeneDrop pedigree of 45 animals from 12 founders). Among aquatic taxa, the Concho River water snake is the central PVA case.

**Fisheries note.** The Ricker model is said to apply to fish populations; the guide also says maximal sustainable harvest in fisheries is tied to locating the point of maximum growth density.

## Key Findings

1. **Model-based decisions are unavoidable.** Managers always rely on a model, whether it is an analogy with a similar species or a formal projection. The document argues that species W is only a model for species Z, possibly invalid.

2. **Population projections are fragile.** In the California condor example, a fitted exponential decline (r ≈ -0.03) from 1940 to 1980 projects reaching 2 animals in the year 2057.

3. **Extinction risk should be described as a distribution.** The author proposes that the best measure of population health is the cumulative distribution of time to extinction, summarized by T10, T50 and T90 (Table 4.1). Species A is the normal case (T50 = 100, T90 = 1,000); Species B shows a deterministic downward trend; Species C is safe for about 25 years then recovers.

4. **Stochastic demography can produce surprising extinction timing.** In the DemStochasticity example (b = 0.2, d = 0.1, clutch size 1, starting at N = 2), about 20% of cases go extinct within 64 years, with a median extinction time of about 40,300 years; a 99.8% extinction probability is reached only near generation 500,000.

5. **Environmental stochasticity lowers typical population size.** With lambda equal to 0.9 or 1.1 with equal probability, the arithmetic mean growth is 1.0 but most populations shrink, because the geometric mean growth rate is below 1.0 (Lewontin and Cohen 1969). The Lewontin-Cohen example (lambda 0.6 or 1.5) gives an arithmetic mean of 1.05 and a geometric mean of 0.94.

6. **Sampling error can mislead trend detection.** In the Trend program, a population dropping from 50 to 45 was judged to be increasing in 7 of 20 trials (35%) at 50% sighting efficiency. In PopProject, guesses about growth were frequently wrong with a small sample of eight years.

7. **Demography can be misapplied.** The desert tortoise case shows that a lambda below 1.0 from lumped data supported expansion of a tank training base, which the author argues was reversed after consultation with the USFWS.

8. **Reproductive value matters for introductions.** The author suggests releasing 7-year-old grizzly bears would give better growth than 2- or 20-year-old bears (RVDemo, GrizDemography).

9. **Grizzly bear demographic stochasticity.** With lambda adjusted to 1.0 and a carrying capacity, demographic stochasticity still causes problems over a 500-year horizon.

10. **Effective population size is much smaller than census size.** For Greater Yellowstone grizzlies, Ne/N is about 20%, so 200 bears behave genetically like an ideal population of about 40. Non-Poisson family size (about 75% of females produce zero daughters, variance about 5.0 at a mean of 1.0) drives this result.

11. **Metapopulation dynamics and heterozygosity.** Patch extinction and recolonization accelerate heterozygosity loss. The author argues that cheetah-like near-zero polymorphism can arise without a bottleneck in fragmented metapopulations. Levins' equation gives p* = (c - e)/c; with c = 0.2 this predicts 0.5 for infinite patches, and the Winking program tests its accuracy for finite grids.

12. **Concho River water snake PVA.** A 105-patch metapopulation model was used to evaluate a dam that would limit the snake's range to the Concho River. The authors concluded that the range would shrink and vulnerability to catastrophe would rise, though the extinction probability on the remaining stretch would not change noticeably. The Army Corps of Engineers proposed artificial transport of snakes. The snake is now on the USFWS endangered list and managed for recovery.

13. **Kinship and inbreeding are computed recursively.** The kinship function uses kinship(x,y) = 0.5*kinship(x,m(y)) + 0.5*kinship(x,f(y)). A worked example gives an inbreeding coefficient of 0.25 for animal 5 and a self-kinship of 0.625.

14. **Gene dropping on the Przewalski's horse pedigree.** The pedigree (12 founders, 24 alleles, 45 animals) has a bottleneck of eight animals; the GeneDrop trial shows only 6 of the original 24 alleles surviving in one realization.

15. **Practical advice.** The author recommends PVA rather than single-issue tools, that stochastic models are a data stratum for risk assessment, and that small populations such as the Gulf of California dolphins (estimated at about 320 under a 10% sighting rate) warrant full protection until recovery is demonstrated.