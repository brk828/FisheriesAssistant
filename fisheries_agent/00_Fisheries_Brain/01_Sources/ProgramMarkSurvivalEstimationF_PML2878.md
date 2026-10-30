---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Colorado State University, Fort Collins, CO, USA
tags: [capture-recapture, survival-analysis, statistical-software, population-monitoring, mark-recapture]
title: "Program MARK: Survival Estimation from Populations of Marked Animals"
source_id: "PML2878"
marsh_id: "PML2878"
library: "Marsh Library"
permission: "public domain"
source_citation: "G. C. White, K. P. Burnham (1997). Program MARK: Survival Estimation from Populations of Marked Animals. Marsh Library ID: PML2878."
source_file: "White G.C. Burnham K.P. 1997. Survival estimation from populations marked animals.pdf"
text_extraction: "text"
---
# Program MARK: Survival Estimation from Populations of Marked Animals

#ichthyology #marine-biology #capture-recapture

## Executive Summary

This draft manual (October 7, 1997) describes [[Program MARK]], a Windows 95 program by Gary C. White and Kenneth P. Burnham for estimating survival and related parameters from marked animals re-encountered alive, dead, or by radio-tracking. The program unifies several model classes in one environment: [[Cormack-Jolly-Seber Model]] live-recapture models, [[Dead Recovery Model]] band or tag recovery models, joint live and dead encounter models, [[Known Fate Model]] radio-telemetry models, and [[Closed Capture-Recapture]] models. It estimates parameters by numerical maximum likelihood, uses a [[Parameter Index Matrix]] and a [[Design Matrix]] to constrain parameters, and ranks models with [[QAICc]]. The document is a software description and user guide rather than a field study. It contains no species-specific or aquatic-habitat data beyond illustrative examples, so the species, family and habitat fields are N/A.

## Background & Description

The paper motivates MARK by noting that monitoring of biological populations has grown in importance, that population viability analyses depend on vital rates usually derived from uniquely marked animals, and that capture-recapture theory supports risk assessment, biodiversity richness estimation and adaptive management. Prior to MARK, no single program combined survival estimation from both live and dead re-encounters or modeled capture and recapture probabilities for closed-population size estimation in a general framework.

The software is operated through a Windows 95 interface with context-sensitive help. Users prepare an ASCII Encounter Histories file (.INP), which MARK converts into a results database (.DBF with associated .FPT and .CDX files). Models are specified through PIMs and the Design Matrix, run through a Run window (choosing link function, fixed parameters, variance method and estimation options), and compared using likelihood ratio tests or Analysis of Deviance (ANODEV) tables. Documentation resides in the on-line Help System; the paper states that the program requires a computer with more than 32 MB of memory for best performance, runs on 8 MB, and needs about 3 MB of disk space.

## Ecological & Environmental Context

The document places survival estimation within population monitoring across terrestrial and avian populations. Its examples are generic or drawn from prior studies:

- A live-recapture example based on Burnham et al. (1987), a fish survival study on release-recapture.
- A dead-recovery example with 15 release occasions and 15 years of recovery data, adults and young in two groups, drawn from the banding framework of Brownie et al. (1985).
- A known-fate example of American black ducks monitored for 8 weeks (Conroy et al. 1989): 48 ducks initially, 1 died in week one, and 4 were lost for other reasons, leaving 41 available in week three.
- Illustrative covariates, such as rainfall (2, 1, 4, 3 cm across four survival intervals) and individual body weight.

The paper notes that, unlike the other types, closed-capture models assume survival of 1.0 over short intervals. The text also describes the statistical background of the logit, Akaike and quasi-likelihood methods but gives no measurements of any aquatic ecosystem.

## Key Findings

- **Scope and capabilities:** MARK handles five re-encounter data types, supports multiple attribute groups and individual covariates, and reports estimates, standard errors and goodness-of-fit diagnostics. Parameters can be constrained by time, age or group through the PIM, and by covariates through the design matrix.
- **Parameter definitions:** In the live-recapture model, the survival term is apparent survival (φ = S(1 − E)), which combines true survival with permanent emigration. In the dead-recovery model, the authors reparameterize reporting as r = (1 − S)·r′ to separate survival from encounter processes. In the joint model, true survival S is estimated because fidelity (F = 1 − E) is included.
- **Identifiability limits:** In the time-effects CJS model, the final survival-recapture product is not separable, and in the dead-recovery model the last S and r are confounded. Users can fix the last p or r to 1.0 to recover the survival estimate.
- **Model selection:** The Multiple Models option generates all combinations of constant (.), group (g), time (t) and group×time (g×t) structures. With two groups and live-recapture data, this gives 16 models (4 for φ times 4 for p). Results are ranked by QAICc and ΔQAICc, with deviance and overdispersion adjustments (ĉ) available.
- **Estimation methods:** Estimation uses numerical quasi-Newton optimization with the sin link as default. Four variance methods are offered (Hessian-based, Observed, Expected, and 2ndPart central differences), with 2ndPart described as the most accurate but slowest. Variance matrix rank determines the parameter count used in QAICc.
- **Limitations:** Closed-capture models cannot include individual heterogeneity or individual covariates. MARK does not manage data, cannot alter an encounter history file after results are generated, and does not estimate population size under the CJS model (unlike POPAN-4 or JOLLY).
- **Program availability:** MARK was available for download from a World Wide Web page, with installation instructions provided there.