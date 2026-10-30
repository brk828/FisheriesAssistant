---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [survival-analysis, mark-recapture, telemetry, statistical-ecology, simulation]
title: "Apparent survival estimation from continuous mark-recapture/resighting data"
source_id: "PML0171"
marsh_id: "PML0171"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. B. Barbour, J. M. Ponciano, K. Lorenzen (2013). Apparent survival estimation from continuous mark-recapture/resighting data. Wiley (DOI 10.1111/2041-210X.12059; journal name not stated in text). Marsh Library ID: PML0171."
source_file: "Barbour A.B. et al. 2013. Apparent survival estimation fom continuous mark recapture resighting data.pdf"
text_extraction: "text"
---
# Apparent Survival Estimation from Continuous Mark-Recapture/Resighting Data

#ichthyology #marine-biology #statistical-ecology

## Executive Summary

This methodological simulation study examines how [[Survival Estimation]] should be performed when mark-resighting data are collected continuously (e.g., [[Acoustic Telemetry]] receivers or [[PIT Tag]] antennae) but analysed with discrete-time models. The authors simulated a population whose survival and detection occurred on a near-daily basis, collapsed the detections into monthly or 10-day bins, and compared two estimators: the [[Cormack-Jolly-Seber Model]] (CJS) and the [[Barker Joint Data Model]]. The Barker model performed better overall, particularly across sample sizes and under time-dependent survival, though it was harder to fit and required simulated annealing optimization. The authors conclude that the Barker model is the preferred option for continuous data, while calling for new methods tailored to continuous mark-resighting data.

## Background & Description

Survival inference depends on stochastic process models that are fitted to capture-recapture or resighting data. Structural errors in model formulation can bias survival estimates and lead to misleading conclusions. Model formulation must account for the data structure (discrete versus continuous sampling), data type (capture, resighting, or dead recovery), and the biology of the study system (open versus closed populations).

Discrete-time models such as the CJS assume that sampling occasions are instantaneous relative to the interval between them. Continuous resighting data violate this assumption. Earlier studies, including [[Heupel and Simpfendorfer 2002]], [[Adams et al. 2006]], [[Camerón et al. 1999]] and [[Hewitt et al. 2010]], collapsed continuous resightings into weekly, monthly or seasonal bins and applied discrete models without evaluating the resulting bias. Some later studies accounted for this issue, but the authors note that the bias in studies that did not is unknown.

The study uses [[Model Structure Adequacy]] (MSA), an approach that links a mechanistic simulation model of the true process to candidate estimation models. MSA allows separation of structural error (approximation), estimation error (parameter uncertainty), and formulation error (mismatch between the simulation and the true process).

## Ecological & Environmental Context

The simulated system was a closed population with no emigration and no tagging mortality. Survival and detection were modelled as daily Bernoulli processes, and the simulation was run for 180 days. The authors state that the parameter ranges covered biologically plausible conditions. The study was motivated by field work on an [[Estuarine-Dependent Fish]] (the juvenile [[Common Snook]] system) at the authors' research site, where initial estimates of survival and detection were near 0.9. Current empirical work on emigration rates at that site was planned as an extension. The authors also note that the same discretization problem may apply to spatial data, such as [[GIS Spatial-Abundance Distributions]] and skipjack tuna movement models.

## Key Findings

**Simulation design**
- Static parameters: n = 1,000 marked individuals, d = 180 days.
- Variable parameters: monthly survival (s) from 0.5 to 1.0 (50 values) and monthly recapture probability (p) from 0.02 to 1.0 (50 values), giving 2,500 combinations.
- Each combination was run 100 times in Simulation 1, for 250,000 total iterations.

**Simulation 1: structural error**
- CJS with method one (marking event included in the first monthly bin) gave moderate underestimation of survival and rarely achieved acceptable coverage.
- CJS with method two (marking event as a separate primary period) gave relatively unbiased estimates, with acceptable coverage except at low survival combined with high recapture probability.
- Switching to 10-day bins did not substantially change CJS results.
- The Barker model showed a consistent, minor positive bias. Newton-Raphson optimization failed to converge in multiple cases, probably because of local minima from the high number of parameters. Simulated annealing achieved 100% convergence, with coverage consistently between 90% and 98%.
- With 10-day bins, Barker performance declined at low recapture probabilities, with coverage approaching 0% and relative bias below -10.0%.

**Simulation 2: estimation error**
- Survival and detection were fixed at 0.9. Marked individuals ranged from n = 50 to 1,000 in steps of 50, with 1,000 iterations per value.
- The Barker model covered the true survival in approximately 95% of iterations at every n, with relative bias near 0.0%.
- CJS coverage was about 95% at low n but fell below 86% as n reached 1,000. The authors attribute this to confidence intervals narrowing faster than bias decreases, with bias held constant at about 0.005%.
- Parametric bootstrap intervals reduced CJS coverage further (from 92.4% to 88.4% at n = 200, and from 88.8% to 81.4% at n = 500).

**Simulation 3: formulation error**
- A severe disturbance was added in month three (days 61–90), with survival dropping from 0.90 to 0.30.
- For the CJS, AIC selected the fully time-dependent model in every iteration (100% of 1,000), and the truth-generating model received no support.
- For the Barker model, the truth-generating model was selected in 89.9% of iterations. The time-dependent model had 10.1% AIC support.
- Under the truth-generating model, the CJS covered the disturbance survival in 31.7% of iterations (relative bias 33.3%), while the Barker model covered it in 93.8% (relative bias 2.5%).
- Under the time-dependent model, the CJS covered the disturbance survival in 1.1% of iterations (relative bias 14.27%), and the Barker model in 76.4% (relative bias 5.6%).
- The CJS attributed much of the month-three decline to month two. It still approximated overall survival well, so it may suit studies aiming at mean survival.

**Conclusions and recommendations**
- The authors recommend the Barker model for continuous-data survival analysis because it outperformed the CJS over a biologically reasonable parameter range.
- Its practical limitations (seven parameters, convergence problems, need for expert model specification) justify developing new methods for continuous mark-resighting data.
- Future work should investigate the robustness of the Barker model to emigration (parameters F and F′), the constant bias correction for parametric bootstrap intervals, and continuous-time Markov approximations of the discrete Barker structure.