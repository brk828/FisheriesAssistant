---
species: N/A
common_name: White-tailed deer
family: Cervidae
habitat: Mixed forest and early-successional habitat (aspen, clearcut, plantation, spruce)
ocean_basin: N/A
location: Minnesota, USA
tags: [ichthyology, marine-biology, statistical-ecology, resource-selection, log-linear-models]
title: "Analyzing selection experiments with log-linear models"
source_id: "PML1016"
marsh_id: "PML1016"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. M. Heisey (1985). Analyzing selection experiments with log-linear models. Ecology, vol. 66, no. 6, pp. 1744-1746. Marsh Library ID: PML1016."
source_file: "Heisey D.M. 1985. Analyzing selection experiments with log linear models.pdf"
text_extraction: "text"
---
# Analyzing Selection Experiments with Log-Linear Models

#ichthyology #marine-biology #statistical-ecology

## Executive Summary

This methodological paper by [[Dennis M. Heisey]] shows how [[Manly's Selectivity Index]] can be analyzed with [[Log-Linear Models]] to test hypotheses about resource selectivity. The approach is applied to a radio-telemetry dataset on [[White-Tailed Deer]] habitat use reported by [[Nelson 1979]]. The paper argues that log-linear analysis offers computational convenience, flexible hypothesis testing and improved statistical efficiency relative to large-sample tests proposed by [[Manly 1974]]. The source is a terrestrial mammal study, not a fish or marine study; the marine and ichthyological taxonomy tags are retained only because the system requires them.

## Background & Description

- **Selectivity measure:** Manly's selectivity index (α) weights resource use against resource availability. Under [[Type One Selection]], users choose items with replacement, which occurs when use is nonconsumptive, consumed items are immediately replaced, or the resource population is effectively infinite.
- **Model structure:** Selectivity can be constant across factors, or multiplicative across factors (for example, male selectivity three times that of females, and adult selectivity two times that of juveniles, giving six times for adult males relative to juvenile females).
- **Factors:** Resource users may be classified by attributes such as age, sex, time of observation or individual animal. The paper uses three factors (resource type i, factor j, factor k) in the general formulation.
- **Estimation methods:** Two main approaches are compared: [[Iterative Proportional Fitting]] (IPF), which is simple and runs on small computers but cannot readily produce standard errors, and [[Iterative Weighted Least Squares]] (IWLS), implemented in [[GLIM]], which provides standard errors directly.

## Ecological & Environmental Context

The worked example concerns habitat use by white-tailed deer (*Odocoileus virginianus*) across four habitat types: aspen, clearcut, plantation and spruce. Habitat use is the number of relocations in each habitat; habitat availability is the relative area of each habitat type within the deer's study area. Observations were split into midday and morning-and-evening periods, across two individual deer (Deer 68 and Deer 342). Data from June were excluded because only one deer was observed that month. The paper's assumptions require that resource availabilities and user selectivities remain constant during the study, and that data be recorded by individual so between-individual variation can be tested.

## Key Findings

- **Model selection:** Goodness-of-fit (likelihood ratio G²) was computed for all possible models. Models with habitat-specific selectivity that were time- and deer-dependent, and the model with time-dependent selectivity constant among deer, fit the data well (large P values). Models with no habitat-specific selectivity, and some constancy models, fit poorly (P < .001 for several).
- **Conditional test:** Adding the multiplicative α term to the simpler model improved fit by ΔG² = 2.19 on 3 df (P = .534), so the simpler model was preferred.
- **Best model estimates:** Time-specific selectivity estimates were reported for aspen (0.571 midday), clearcut (0.153), plantation (0.276) and spruce (0.000), with standard errors and normalized values summing to 1 within each time period.
- **Linear comparisons:** The paper shows how to test contrasts among selectivity parameters with a standard normal statistic, including the difference between two parameter estimates.
- **Methodological conclusions:** Log-linear models handle hypotheses that are analytically intractable, allow standard-error estimation via GLIM, and are more statistically efficient than Manly's 1974 large-sample tests. Manly's index is presented as a biologically interpretable and probabilistically grounded measure, though the paper cautions that any measure must actually capture the phenomenon being studied.
- **Assumptions and caveats:** Estimated availabilities introduce error, which the authors consider manageable because the methods are robust to small errors. Data should be recorded at the individual level to avoid pooling across individuals with different selectivities.