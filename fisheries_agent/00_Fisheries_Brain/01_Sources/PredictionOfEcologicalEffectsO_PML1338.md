---
species: N/A
common_name: N/A
family: N/A
habitat: Aquatic ecosystems (generic, not site-specific)
ocean_basin: N/A
location: N/A
tags: [ecotoxicology, aquatic-ecology, ecosystem-modeling, element-cycling, epa-report]
title: "Prediction of Ecological Effects of Toxic Chemicals: Overall Strategy and Theoretical Basis for the Ecosystem Model"
source_id: "PML1338"
marsh_id: "PML1338"
library: "Marsh Library"
permission: "public domain"
source_citation: "Ray R. Lassiter (1983). Prediction of Ecological Effects of Toxic Chemicals: Overall Strategy and Theoretical Basis for the Ecosystem Model. U.S. Environmental Protection Agency, Environmental Research Laboratory, Athens GA, EPA-600/S3-83-084. Marsh Library ID: PML1338."
source_file: "Lassiter R.R 1983. Predictiopn of ecological effects of toxic chemicals.pdf"
text_extraction: "text"
---
# Prediction of Ecological Effects of Toxic Chemicals: Overall Strategy and Theoretical Basis for the Ecosystem Model

#aquatic-ecology #ecotoxicology #ecosystem-modeling #element-cycling

## Executive Summary

This [[Environmental Protection Agency]] project summary, prepared by the [[Environmental Research Laboratory]] in Athens, Georgia (EPA-600/S3-83-084, November 1983), presents a strategy for modeling aquatic ecosystems so that the effects of toxic chemicals on [[Element Cycling]] and other ecosystem processes can be estimated. The author is [[Ray R. Lassiter]]. The approach combines [[Multi-Species Representation]] of biotic communities with mathematical descriptions of the processes that drive aquatic ecosystems. Direct toxicant effects are assigned to species, and ecological effects are calculated as the normalized difference between an unaffected ("nominal") model run and a run with the toxicant present. The author describes these outputs as heuristically useful predictions, not quantitative forecasts for any real water body.

## Background & Description

The report separates two questions in chemical risk analysis. [[Environmental Fate]] asks what the environment does to a chemical, while ecological effects ask what the chemical does to the environment. The research focuses on effects that alter element cycles, a class of effects the author says had received little prior study.

Element cycling depends on redox reactions between reduced and oxidized forms of elements. [[Photosynthesis]] is the main source of the chemical disequilibria that drive these reactions, and other biotic processes use that disequilibrium. The report notes that the major geochemical pools, including atmospheric gases, ocean composition, dissolved constituents of fresh water, and soils, have been stable over geological time. It also states that no comparative analysis of the relative roles of abiotic and biotic processes in maintaining these pools has been made.

The modeling strategy rests on three components:

- **Process representation:** Element cycling is treated as a system phenomenon. Processes are grouped by whether they are carried out by microorganisms or macroorganisms and by autotrophs or heterotrophs.
- **Population descriptors:** Each population is defined by traits such as size, energy source, source of biosynthetic materials, and motility. For example, one population may use microbial biomass for both energy and biosynthesis, while another uses NH4+ and O2 for energy and inorganic chemicals for biosynthesis.
- **Parameterization:** Because descriptive data are not available for every organism, a large initial set of species is described, and the model is allowed to select the populations that persist. The author expects the persistent set to be internally compatible and "adapted" to the environment, but unlikely to match real populations closely.

## Ecological & Environmental Context

**Effect definition.** An effect is a deviation from a nominal state or rate. The model first runs without the toxicant to obtain the nominal condition, then runs again with the toxicant added. The difference is divided by the nominal value so that units do not affect the magnitude. Because the only difference between runs is the chemical, any change can be attributed to it. The author stresses that these values are predictions of [[Ecological Effects]] in the heuristic sense and do not describe an expected effect at a specific site or time.

**Species redundancy.** The report observes that concentrations of rapidly turning-over chemicals are often stable even when the species that use or produce them fluctuate widely. This suggests [[Species Redundancy]] and compensation among species performing the same function. The author argues that representing a functional group as one variable would likely make element cycling appear more fragile than it is.

**Autotrophic and heterotrophic processes.**
- [[Photoautotrophy]] uses solar energy, and its energetics and material limitation are modeled together.
- [[Chemoautotrophy]] uses energy from redox reactions between reduced compounds and oxygen. It shares biosynthetic pathways with photoautotrophs but uses a wider range of terminal electron acceptors. Oxidized element forms are used in anaerobic zones.
- [[Heterotrophy]] uses organic compounds for energy and synthesis. Microorganisms use O2 in aerobic zones and oxidized element forms in anaerobic zones. Growth is modeled as the energy and materials gained, minus maintenance and activity costs.
- Growth limitation is set to the minimum of the potential growth rates for each limiting factor, which is the [[Limiting Factors]] approach the report uses for all organisms.

**Macroorganism feeding.** Macroorganisms are limited to aerobic environments. The model includes [[Filter Feeding]] and [[Pursuit Predation]]. Consumption rates are calculated from predator and prey characteristics, with coupling constants assigned for each interaction. The model is general and applies to any number of consumers feeding on any number of prey.

**Uncertainty and validation.** The author acknowledges that predicted effects are unlikely to match observed effects in any particular system. Because no specific real system is represented, validation is difficult. The proposed test uses [[Laboratory Ecosystems]], which can be run repeatedly under the same conditions with and without a toxicant. Their distributions and effects would then be compared with those from the model. The report also says that a measure of uncertainty can be derived from the distribution of descriptors and of direct toxicant effects, provided those distributions are realistic.

## Key Findings

- **Modeling strategy exists, but needs development.** The report says the modeling strategy and the theory needed to carry it out already exist. Substantial work remains before the approach reaches the maturity of ecosystem modeling theory. Fermentation was flagged as an ecological process that still needs to be added.
- **Effects are defined as normalized deviations.** Ecological effects are the difference between nominal and toxicant-affected model outputs, divided by the nominal value.
- **Multi-species representation is central.** Compensation among functionally similar species may stabilize element cycling. Single-variable representations are expected to overstate fragility.
- **Direct effects are assigned from toxicology.** Direct toxicant effects are assigned to species within the range suggested by available toxicological information.
- **Results are heuristic.** The author states that calculated effects are not quantitative predictions. They are meant as a learning tool for identifying ecological effects that are too indirect to be apparent without a model.
- **Validation is proposed, not completed.** Comparisons with laboratory ecosystems are suggested, but the report does not present any tests or numerical results.
- **Source information.** The complete report, "Prediction of Ecological Effects of Toxic Chemicals: Overall Strategy and Theoretical Basis for the Ecosystem Model," is available through the [[National Technical Information Service]] in Springfield, Virginia. The EPA project officer is at the Environmental Research Laboratory in Athens, Georgia. The summary also includes mailing information for the Center for Environmental Research Information in Cincinnati, Ohio.