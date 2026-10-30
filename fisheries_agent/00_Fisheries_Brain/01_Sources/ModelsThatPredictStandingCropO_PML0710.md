---
species:
  - "Oncorhynchus kisutch"
  - "Oncorhynchus tshawytscha"
  - "Oncorhynchus gorbuscha"
  - "Salmo trutta"
  - "Salvelinus fontinalis"
  - "Oncorhynchus clarki"
  - "Micropterus dolomieu"
  - "Salmo salar"
common_name:
  - "Coho salmon"
  - "Chinook salmon"
  - "Pink salmon"
  - "Brown trout"
  - "Brook trout"
  - "Cutthroat trout"
  - "Smallmouth bass"
  - "Atlantic salmon"
family: "Salmonidae (with Centrarchidae and Cyprinidae in some models)"
habitat: "Freshwater streams and rivers"
ocean_basin: "N/A"
location: "United States (Rocky Mountain, Pacific Northwest, Great Lakes, Ozark, and Southeastern regions) and Canada (Ontario, Quebec, Alaska)"
tags:
  - ichthyology
  - stream-ecology
  - predictive-models
  - habitat-assessment
title: "Models that predict standing crop of stream fish from habitat variables: 1950-85"
source_id: "PML0710"
marsh_id: "PML0710"
library: "Marsh Library"
permission: "public domain"
source_citation: "K. D. Fausch, C. L. Hawkes, M. G. Parsons (1988). Models that predict standing crop of stream fish from habitat variables: 1950-85. USDA Forest Service, Pacific Northwest Research Station, General Technical Report PNW-GTR-213. Marsh Library ID: PML0710."
source_file: "Fausch et al. 1988. Stream fish models.pdf"
text_extraction: "mixed"
---
# Models That Predict Standing Crop of Stream Fish From Habitat Variables

#ichthyology #marine-biology #salmonidae #stream-fish #habitat-models

## Executive Summary

This USDA Forest Service General Technical Report (PNW-GTR-213) by [[Kurt Fausch]], [[Clifford Hawkes]], and [[Milton Parsons]] reviews mathematical models that predict the standing crop of stream fish (number or biomass per unit length or area of stream) from characteristics of the environment. The authors compiled 99 models developed since about 1950 and sorted them into five categories by the type of independent variable: drainage basin variables, channel morphometry and flow variables, habitat-structure/biological/physical/chemical variables, combinations of variable types, and tests of [[Weighted Usable Area]] (WUA). The review concludes that most models are statistically imprecise, poorly tested, and lack generality, and it recommends experimental work and ecoregion-based model development for fishery managers.

## Background & Description

The report addresses a long tradition of searching for habitat variables linked to stream fish abundance, dating to about 1930. The authors set out to review these models, organize them by variable type, mathematical structure, and model quality, and discuss how models should be built, tested, and applied.

Model searches were broad: the authors reviewed sources including the primary literature, state and federal agency reports, theses, and personal communications. Because many models appeared only in unpublished reports, the authors acknowledge that some models were likely missed. They note that [[Habitat Evaluation]] is a young, dynamic science with few measurement standards (citing Wesche 1993).

**Mathematical structure.** Most models were simple or multiple linear regressions of the form SC = a + bX1 + cX2 + ... + nXn, where SC is standing crop. Others used exponential or power functions, linearized with logarithms. Model fit was usually reported as the coefficient of determination (r² or R²).

**Variable types.** Independent variables were grouped as:
- **Drainage basin variables** (coarse scale, from topographic maps): basin area, mean basin elevation, total stream length, drainage density, stream order, and gradient.
- **Channel morphometry and flow variables** (intermediate scale, measured on transects): discharge, width, depth, mean velocity, wetted area, pool volume, and substrate percentages.
- **Habitat-structure, biological, physical, and chemical variables** (finest scale, microhabitat): cover, streambank stability, depth and velocity, invertebrate drift, substrate, temperature, and water chemistry.

## Ecological & Environmental Context

The report emphasizes that physical habitat, particularly many forms of cover, is most closely related to salmonid abundance (after Hall and Knight 1981). Flow regimes also strongly affect populations: high flows during incubation or emergence reduced year classes of brown and rainbow trout in several Colorado rivers ([[Nehring and Anderson]]), while inadequate base flows limited salmonids by reducing suitable microhabitat. Groundwater-fed streams with stable base flows and water hardness supported higher trout standing crops.

Substrate also matters. Fine sediment and embeddedness, often increased by timber harvest and related land use, reduced salmonid density ([[Hawkins and Others]]; [[Stowell and Others]]). Models of sediment yield (for example [[Cline and Others]]) were linked to fish models to estimate cumulative effects.

Fish are not always limited by habitat alone. The authors note that predation, competition, fishing mortality, and food supply can limit standing crop below carrying capacity, and that these factors are seldom incorporated into models.

## Key Findings

**Scope and sample.** Of the models reviewed, 99 are tabulated in Tables 1–5: 59 were based on samples of more than 20 observations and 40 on 20 or fewer, with several cases where sample size was not reported.

**Model quality.**
- Only 18 of the 59 models with more than 20 observations accounted for 75 percent or more of the variation in standing crop.
- Of 64 models with fewer than 20 degrees of freedom, 20 accounted for 75 percent or more of the variation, indicating that precise models often lack generality.
- Most models reported only r² or R²; few reported standard errors, confidence intervals, or prediction intervals.

**Most frequently significant variables** (among reviewed models, excluding WUA tests): instream overhead cover (22 models), alkalinity/hardness/conductivity (14 models), width (14 models), and surface area (12 models).

**Notable models.**
- Model 4.09 — [[Habitat Quality Index]] (Binns 1979), a complex power function of 10 rated variables, explaining 95 percent of variation in the initial 20 sites and 93 percent when tested on eight new sites, with 12.5 percent average prediction error.
- Model 2.03 — Hunt (1971): brook trout standing crop in a Wisconsin stream, with six morphometric and cover variables explaining 58–95 percent of variation.
- Model 3.15 — Gordon and MacCrimmon (1982) and Model 3.02-type multiple regressions relating trout biomass to instream cover.
- Model 3.23–3.25 — [[McClendon and Rabeni]] (1985) on Ozark centrarchids; best two- or three-variable models explained about 60 percent of variation.
- Models 3.18–3.22 — [[Stowell and Others]] (1983), explaining 87–99 percent of variation in juvenile steelhead and chinook standing crop from embeddedness.
- Models 4.10–4.12 — [[Nickelson and Others]] (1979), with 95 percent prediction intervals; testing on 20–318 new observations found only 48, 57, and 88 percent within the interval.
- Models 5.01–5.13 — [[Weighted Usable Area]] tests (within the [[Instream Flow Incremental Methodology]]); WUA explained 81 percent of brown trout biomass in Wyoming streams (Stalnaker 1979) and 82 percent in large Wyoming reaches (Wesche 1980), but correlations were low for some species.

**Major problems identified by the authors.**
1. **Inadequate sample size** — most models used too few observations and too many variables.
2. **Error in measuring habitat variables** — the standard assumption of error-free predictors is often violated; measurement repeatability is poor.
3. **Poor model selection** — most authors chose models on r² alone, which inflates with added variables; the authors recommend "all subsets" regression with Mallows' Cp or adjusted R².
4. **Lack of testing** — only about ten investigators tested their models on new data.
5. **Inductive leap** — because most habitat data are observational, predictions about changed habitat assume causal relationships that were never experimentally verified. Only Hunt (1971), Kraft (1972), and Randolph and White (1984) manipulated habitat variables.
6. **Estimation of standing crop** — mark-recapture and removal estimates often rest on unrealistic assumptions (closed populations, equal catchability).
7. **Biological assumptions** — models assume fish populations are limited by habitat alone.

**Recommendations.**
- Conduct experiments that manipulate habitat variables to test mechanisms.
- Use rigorous cycles of model building and independent testing in defined ecoregions, which may improve precision and generality.
- Report prediction intervals, standard errors, and the ranges of measured variables, and avoid extrapolating beyond them.
- Select models by objective criteria and consider the cost and feasibility of measuring variables.
- Choose variables that management can actually influence; elevation, for example, is unsuitable for evaluating range management.

**Management uses.** The authors identify six uses: predicting current standing crop, identifying limiting habitat, predicting changes from habitat alteration, linking to cumulative-effects and timber-harvest models, assessing fishing mortality (for example, Stuber 1985; Nehring and Anderson 1984), and comparing management alternatives on the [[Siuslaw National Forest]] (Parsons and others 1981).