---
species: ["Microtus spp. (example data)", "Clethrionomys spp. (example data)"]
common_name: ["Vole", "Mouse (burn-area example)", "Frog (Delta Marsh example)"]
family: N/A
habitat: N/A
ocean_basin: N/A
location: "Rodri Tarn (Seber 1982 example); Delta Marsh (frog data title); burn area (summer 1974 mouse example)"
tags: [mark-recapture, population-ecology, jolly-seber, popan, software-manual]
title: "POPAN-5 User Manual: Mark-Recapture Data Maintenance and Jolly-Seber Analysis"
source_id: "PML0074"
marsh_id: "PML0074"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Arnason (1998). POPAN-5 User Manual: Mark-Recapture Data Maintenance and Jolly-Seber Analysis. Marsh Library ID: PML0074."
source_file: "Arnason 1998. POPAN-5 user manual.pdf"
text_extraction: "text"
---
# POPAN-5 User Manual: Mark-Recapture Data Maintenance and Jolly-Seber Analysis

#population-ecology #mark-recapture #popan

## Executive Summary

This document is the user manual for **POPAN-5**, a general-purpose program for maintaining, selecting, summarizing and analyzing capture-mark-recapture (CMR) data from animal sampling studies. It is not a fish-specific study. Its example datasets involve [[Microtus]] and [[Clethrionomys]] voles, a summer 1974 mouse dataset, and [[Delta Marsh Frog]] data. The manual covers the statistical framework ([[Jolly-Seber Model]]), the data file format, the task command language, and the program's analysis, simulation and customized-model tools. It also gives guidance on which models and tests to use and how to prevent input and modeling errors.

## Background & Description

POPAN-5 is designed to estimate population properties such as population size at each sample time, emigration or mortality rates (losses, which cannot always be separated), and births or recruitment (dilution). It also tests behavioural assumptions, including whether births or losses occur, whether loss rates differ among groups, and whether animals are equally catchable. The manual states that these tests matter as much as the estimates because they guide model choice and reveal sources of bias.

The manual classifies marking experiments in five ways:

1. Two-sample (Petersen) versus multi-sample designs, including continuous sampling.
2. Open versus closed populations.
3. [[Band Recovery Experiment]] designs versus multiple recapture-and-release designs.
4. Stratified versus non-stratified designs, where migration among strata is of interest.
5. Designs that include resighting data as well as recovery and recapture data.

POPAN provides analyses for many, but not all, of these situations. Its core analyses are of the Jolly-Seber type. The essential Jolly-Seber features are:

- The population is sampled on K > 2 occasions, and sample intervals need not be equal but must be known.
- Parameters include capture probability (p_i), survival probability (φ_i), net births (B_i) and derived population size (N_i) and number of marked animals alive (M_i).
- Core assumptions are no mark loss with correct mark identification, homogeneous capture probability, and homogeneous survival.

The Jolly-Seber family includes five model classes:

- **(a) Full model:** all parameters vary by sample; often imprecise because of the large number of parameters.
- **(b) Closure models:** φ or B fixed (no death or no birth); more precise but more sensitive to assumption failures such as tag loss.
- **(c) Constant-parameter models:** constant capture or survival, with adjustment for unequal intervals.
- **(d) Generalized models:** age, history or group effects, such as sex-specific survival with equal catchability.
- **(e) Covariate models:** auxiliary variables such as sampling effort or weather explain the parameters.

The manual also refers to related software: SURGE, MARK, and SURPH for Cormack-Jolly-Seber models.

**Data structures.** Capture histories use either a variable-length POPAN format (identifier, up to 8 attribute characters, number of captures T, injection flag C, and capture times) or a fixed-length CMR format with one status code per sample (1 injected, 1 captured and returned, 2 lost on capture, 0 not captured). Identifiers can be up to 14 digits or up to 8 characters. Sample time codes must span no more than 512 values.

**Task command language.** The program is run through paragraphs and keywords modeled on the BMDP system. The main paragraphs are:

- [[CREATE Paragraph]] (build a data file)
- [[ADD Paragraph]] (add histories or capture times)
- [[SELECT Paragraph]] (choose subsets and renumber samples)
- [[LIST Paragraph]] (list histories)
- [[STATISTICS Paragraph]] (collect counts using English-like phrases, up to 14 per pass)
- [[ANALYSIS Paragraph]] (run preprogrammed estimators)
- [[SIMULATE Paragraph]] (simulate sampling experiments)
- [[UFIT Paragraph]] (fit constrained models)
- [[TEST Paragraph]] (hierarchical log-linear model fitting)

## Ecological & Environmental Context

The manual discusses several factors that affect whether the estimates reflect the real population:

- **Stratification and movement:** Estimates are biased by non-permanent emigration, meaning animals that leave a stratum and return. Strata defined by age or size are acceptable because movement among them is permanent. Strata defined by geographic area need well-defined, separated areas or animals known to be fairly immobile. Highly mobile populations in poorly defined areas can produce large bias (Brussard and Ehrlich, 1970).
- **Age-dependent survival:** Bias can be reduced by specifying heterogeneous losses.
- **Tag loss and temporary emigration:** These can be modeled in [[SIMULATE Paragraph]] to see how much bias they produce.
- **Sampling design:** Early estimates can guide effort allocation and the spacing of future samples.

The manual also notes that the [[Pooling Methods]] used for precision generally do not increase bias, based on a study by Hargrove and Borland (1995).

## Key Findings

- **Model set:** POPAN-5 offers 30 models plus a general 2×2 contingency table test. Ten are variations of the three standard Jolly-Seber (1965) models (full, birth-only, death-only). Fourteen are based on Jolly-Dixon (1980) models that hold capture or survival constant. Four are closed models based on Otis et al. (1978). Model choice depends on the keywords EFFORT, DILUTION, LOSSES and POOLING. The invalid combination is EFFORT = present with LOSSES = fixed.
- **Subset selection:** Histories can be filtered by attributes, time of first capture, injection status, or identifier. Sample times can be omitted or grouped, and grouped captures are treated as a single capture at the midpoint.
- **Simulation:** Replicate runs (up to 999) report means and standard deviations of estimates. Survival and capture rates can be made heterogeneous, and models can be deliberately mismatched to measure bias. The output includes true population values for comparison.
- **Mean Value Analysis:** New in POPAN-5, this lets expected sufficient statistics from SIMULATE feed UFIT. It shows bias and precision without replication.
- **Constrained likelihood (UFIT):** Uses a logit parameterization (Schwarz and Arnason 1996). Net births are normalized to sum to 1, and the model provides derived gross births (B_GD), which are useful for salmon run-size estimation. Model comparison uses likelihood ratio tests or AIC.
- **Limits of TEST:** Storage grows with 2^K, so TEST suits small studies (K < 10). It also gives no standard errors and makes some constraints hard to impose.
- **Data checking:** CREATE and ADD reject or flag invalid histories. Checks cover unique identifiers, valid attribute codes (ACHECK), ordered and in-range capture times (TCHECK), and loss-on-capture only at the last capture. Errors in the T field are a common cause of misreads.
- **Worked examples:** The manual includes CREATE examples for a 449-history mouse dataset with 24 sample times and a 2-sample Rodri Tarn example (three possible histories), plus an ADD example extending the mouse file with new sample times 25 and 26 and a fourth attribute (area). It also lists 26 ADD cards, of which cards 1–12 are valid and 13–26 demonstrate specific error traps.
- **Recommended practice:** Use the ENTRY program or FORMAT=FREE for data entry, keep the raw (.RAW) file as the master copy and re-create the binary file when data change, and run LIST to check every history against the original data sheets.