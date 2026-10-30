---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Closed population model; example systems include lakes (smallmouth bass case) and invasive species literature (general)
tags: [ecology, population-control, harvest, overcompensation, invasive-species, nuisance-species, population-modeling]
title: "When can Efforts to control Nuisance and Invasive species Backfire?"
source_id: "PML2949"
marsh_id: "PML2949"
library: "Marsh Library"
permission: "not public domain"
source_citation: "E. F. Zipkin, C. E. Kraft, E. G. Cooch, P. J. Sullivan (2009). When can Efforts to control Nuisance and Invasive species Backfire?. Ecological Applications, Vol. 19, No. 6 (Sep. 2009), pp. 1585-1595. Marsh Library ID: PML2949."
source_file: "Zipkin E.F. et al. 2009. When can efforts to control nuisance and invasive species backfire .pdf"
text_extraction: "text"
---
# When Can Efforts to Control Nuisance and Invasive Species Backfire?

#ichthyology #marine-biology #population-ecology

## Executive Summary

This theoretical and empirical study, by Elise F. Zipkin and co-authors (Cornell University, USGS Patuxent Wildlife Research Center), examines when harvest-based control of [[Nuisance Species]] and [[Invasive Species]] can produce unintended results: [[Overcompensation]] (increased abundance in response to harvest) and [[Population Instability]] (cycling or chaos). The authors built a stage-structured, density-dependent model with juvenile and adult classes and tested three [[Recruitment Functions]] (linear, compensatory/Beverton-Holt, and overcompensatory/Ricker). Overcompensation requires an overcompensatory recruitment function, and the key driver is maximum per capita fecundity. The paper proposes cautionary guidelines for predicting the risk of backfire from life-history traits.

## Background & Description

Harvest (removal of individuals by hunting, fishing, trapping, shooting or [[Biocontrol]]) is a widely used control method for vertebrates, invertebrates, and plants. The intended outcome is to reduce abundance, but increased mortality can, in theory and in some empirical cases, increase total abundance. The phenomenon was first described by [[Ricker (1954)]] and has since been termed the "hydra effect," "paradoxical increase," and "overcompensation" in theoretical work.

The model is a first-order difference equation with an annual time step, a pre-breeding census, harvest before breeding, and separate harvest proportions for juveniles (h_j) and adults (h_a). Vital rates are juvenile survivorship (s_j), adult survivorship (s_a), and fecundity (c or γ). The authors also treat [[Carrying Capacity]] as the equilibrium abundance in the absence of harvest.

## Ecological & Environmental Context

- Overcompensation has been documented in plants, insects, fish and mammals, typically where reproductive potential is high at low abundance.
- A cited empirical example is a closed [[Smallmouth Bass]] population in a lake, where an intensive seven-year removal of more than 53,000 individuals (no other species targeted) led to higher estimated bass abundance, mainly via more juveniles.
- Recruitment density dependence is a common mechanism: it is established in plants, insects, fish, birds and small mammals.
- Predators and consumer-resource systems can also show increased abundance under higher mortality, suggesting species interactions matter in control design.
- Harvest of nuisance mammals (e.g., [[Feral Goats]], island eradications) has been broadly successful; control of nuisance birds (e.g., [[Double-Crested Cormorant]]) has been considered less successful.
- Immigration into a target population requires larger control effort and may make complete eradication impossible.

## Key Findings

- **Fecundity is decisive.** Overcompensation and instability were possible mainly when maximum per capita fecundity was high and stage-specific survivorship was fairly low. Instability was rarer and required both high fecundity and high adult survivorship.
- **Recruitment shape matters.** Only the overcompensatory (Ricker-type) recruitment function can cause instability or overcompensation through harvest. Linear and compensatory (Beverton-Holt) models gave stable dynamics, with a compensatory population needing less harvest than an overcompensatory one for the same target.
- **Overcompensation mostly shows up as more juveniles.** Juvenile-only harvest could produce overcompensation in total population, adult-only harvest could increase both juveniles and adults, and equal-proportion harvest also could overcompensate.
- **Survivorship scenarios (equilibrium parameters).** Low survivorship for both stages (s_j = s_a = 0.2) could still give near-equal reductions in abundance. With high juvenile and low adult survivorship, harvest had to be larger than under the opposite scenario. With high survivorship in both stages (s = 0.8), the required harvest depended on the recruitment form: for c = 7, 60% harvest of both stages was needed to reach 50% of carrying capacity under overcompensatory recruitment, versus 22% under compensatory recruitment.
- **Collapse thresholds.** The minimum total harvest needed to collapse a population was the same for compensatory and overcompensatory recruitment (for equivalent parameters), because per capita recruitment approaches c as population size falls.
- **Model variations.** Density dependence in juvenile survivorship alone, or in adult survivorship alone, produced far less overcompensation than recruitment-based density dependence, so empirical overcompensation is poorly matched by survivorship-only models. Delayed maturation (a subset of juveniles remaining juveniles, m < 1) reduced the maximum overcompensation and the total harvest needed for collapse, though intermediate harvest levels could show larger overcompensation.
- **Risk table by fecundity.** Small maximum recruitment (<3 offspring per adult) carries no overcompensation risk at any harvest level. Medium (3–10) and high (10–20) values carry increasing risk, and values above 20 carry risk across all survivorship combinations. Examples cited include [[Alewife]], [[Rusty Crayfish]], [[Northern Pike]], [[Zebra Mussel]], [[Garlic Mustard]] and [[Prussian Carp]].
- **Guidelines proposed by the authors:**
  1. Determine whether population density affects recruitment.
  2. If so, estimate maximum per capita fecundity; values of three or fewer surviving offspring per adult per year are low-risk.
  3. Estimate annual stage-specific survivorship and its variability to gauge effort. When adult survivorship is high, target adults; when it is low, target both stages.
- **Trade-off.** Reducing adults can increase juveniles, which may or may not be desirable depending on the impact of each stage. In the smallmouth bass case, adult reduction (which drives impacts on the fish community) coincided with more juveniles, and juveniles may provide forage for native predators.
- **Practical threshold.** Pardini et al. (2009) estimated that control of [[Garlic Mustard]] would fail unless more than 95% of adults or 98% of rosettes were removed annually. The authors conclude that eradication of high-risk species requires strong commitment to remove nearly every individual.
- **Limitations and future work.** The model assumes a closed population, equilibrium dynamics, and constant survivorship. Stochasticity, transient dynamics, and timing of removal are not fully explored. The authors call for field experiments that harvest at varying densities and monitor responses.