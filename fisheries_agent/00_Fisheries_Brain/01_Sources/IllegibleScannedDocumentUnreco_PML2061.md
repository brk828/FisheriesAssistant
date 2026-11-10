---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [capture-recapture, population-estimation, closed-populations, statistics, wildlife-biology]
title: "Statistical Inference from Capture Data on Closed Animal Populations"
source_id: "PML2061"
marsh_id: "PML2061"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. L. Otis et al. (1978). Statistical Inference from Capture Data on Closed Animal Populations. Wildlife Monographs. Marsh Library ID: PML2061."
source_file: "Otis D.L. et al. 1978. Wildlife moographs.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Statistical Inference from Capture Data on Closed Animal Populations

#ichthyology #marine-biology #capture-recapture

## Executive Summary

This Wildlife Monograph (No. 62, October 1978) by David L. Otis, Kenneth P. Burnham, Gary C. White, and David R. Anderson presents statistical methods for estimating the size (N) and density (D) of closed animal populations from multiple-occasion capture-recapture and removal data. The monograph is a comprehensive treatment of [[Closed Population Models]] in which capture probabilities may vary by time, behavioral response to capture (trap shy or trap happy), and individual heterogeneity. It develops eight models (M0, Mt, Mb, Mh, Mtb, Mth, Mbh, Mtbh), associated estimators, a sequential model selection procedure, guidance on study design, and a density estimator for grid trapping. Accompanying computer program CAPTURE is central to its use. The taxonomic examples are mostly small mammals, with one fish example (whitefish) and one aquatic insect example (mayfly).

## Background & Description

The estimation of animal abundance has been a long-standing problem in biology. Serious methodological development began in the 1950s, and over 200 papers had been published, yet no unified approach existed. The authors note the need for estimates in research, environmental assessment, and Environmental Impact Statements required under the National Environmental Policy Act of 1970.

The monograph covers:
- **Multiple capture-recapture studies** (livetrapping, visual sightings of marked animals, electrofishing) and **removal studies** (kill traps, temporary removal).
- **Closed populations only**; open-population methods (e.g., [[Jolly-Seber Method]]) are excluded.
- Two-occasion (Petersen/Lincoln) designs are excluded because they are covered in the literature; the authors suggest five or more trapping occasions for grid data.
- Stratification, sequential sampling, Bayesian schemes, change-in-ratio estimation, and index-only methods are not treated.

Funding was provided by the U.S. Fish and Wildlife Service (Coal Program and Oil Shale Program) and the Federal Interagency Energy/Environmental Research and Development Program (U.S. EPA). Research was performed under the [[Utah Cooperative Wildlife Research Unit]], Utah State University.

## Ecological & Environmental Context

The monograph situates population estimation within environmental impact and biological inventory work. Examples are drawn from diverse habitats:
- Meadow voles (*Microtus ochrogaster*), tall-grass prairie, Kansas.
- Least chipmunks (*Eutamias minimus*), sagebrush and snowberry bottomland, Colorado.
- Deer mice (*Peromyscus maniculatus*), sagebrush-rabbitbrush and drainage-bottom habitats, Colorado.
- Great Basin pocket mice (*Perognathus parvus*), desert community, Curlew Valley, Utah.
- Feral house mice (*Mus musculus*), southern California salt marsh.
- Snowshoe hares (*Lepus americanus*), black spruce forest, Alaska.
- European hares (*Lepus europaeus*), experimental hunting grounds, Poland.
- Taxicabs of Edinburgh (Carothers 1973a), a known-size population used for validation.
- Aquatic examples: mayflies (Ephemeroptera) sampled from 0.25 m² benthic areas in the Poudre River, Colorado, and whitefish (*Coregonus clupeaformis*) removed by gillnetting from Shakespeare Island Lake, Ontario.

Behavioral response is noted as common in small mammals, and the authors observe that grids may attract animals from surrounding areas, violating closure, particularly in removal trapping.

## Key Findings

**Assumptions for capture-recapture models**
- Four assumptions apply in the most restrictive case: (1) population closure, (2) permanent marks, (3) correct recording of marks, (4) constant and equal capture probability on each occasion, with no effect of capture or marking on catchability.
- The monograph's focus is relaxing assumption 4. Closure can be approximately met in short studies; tests for closure are weak and confounded with behavioral response.

**Model structure**
- **M0**: constant capture probability. Most restrictive; estimator N0 is nonrobust to heterogeneity and behavioral response. Useful mainly as a null model. Bias negligible when p ≥ 0.10 and t ≥ 5; 15–20% positive bias for smaller p.
- **Mt**: capture probability varies by time (Darroch 1958 ML estimator). Simulations showed bias negligible when average p ≥ 0.1. Seber (1973) advised against routine use.
- **Mb**: behavioral response (Zippin-type removal equivalence). Estimator is nonrobust to heterogeneity; bias direction depends on trap shy or trap happy behavior. Useful when p ≥ 0.2.
- **Mh**: individual heterogeneity. Jackknife estimator (Burnham) is the most robust available, though confidence interval coverage is poor (0 to 87% in simulations). Requires many occasions.
- **Mtb, Mth, Mbh, Mtbh**: no satisfactory estimator for Mtb, Mth, and Mtbh; a generalized removal estimator (Mbh) performs reasonably, but confidence interval coverage averaged about 0.50.

**Estimation and precision**
- Maximum likelihood (ML) estimators were used; several (e.g., Mt) lack closed-form solutions and require numerical methods.
- Approximate 95% confidence intervals use N ± 1.96√Var(N); the authors acknowledge limitations, especially for small capture probabilities, where lower limits can be negative or fall below the number of animals seen.

**Model selection**
- A seven-test sequence (specific tests against M0 plus goodness-of-fit tests) feeds a discriminant function classifier implemented in CAPTURE.
- Classifier trained on 1,600 simulated cases (100 per population type across eight models). Performance on good data (average p ≈ 0.35) was strong; on poor data (average p ≈ 0.05), the correct model was selected far less often and estimates were unreliable.
- The authors recommend that field biologists generally accept the algorithm's recommended model, but that users with statistical expertise may refine it.

**Worked examples and results**
- Simulated M0 data (N = 100, t = 5, p = 0.5): estimate 102, 95% CI 87–107.
- Meadow vole (Larsen): M0 estimate 173, 95% CI 137–209, p ≈ 0.17.
- Least chipmunk (Reid, Colorado): Mb-type analysis, estimate 50 animals, 95% CI 44–56.
- Deer mouse (Larsen, Mbh removal data): estimate 72, CI 50–... (lower limit reported as 69 in text).
- Deer mouse (Reid): Mbh estimate 41, 95% CI 38–47.
- Taxicab population (Carothers, known N = 420): Mh estimate about 12% above truth, but the CI contained 420.
- Snowshoe hare (Burnham and Cushwa, Alaska): 74 different animals caught; lower 95% CI limit of 75.
- Pocket mouse (Larsen, Utah): Mbh estimate 77, 95% CI 28–126 (Mbh model selected for k = 2).
- Whitefish removal (Ricker 1958, gillnetting): generalized removal estimate N = 138, 95% CI 109–167; close to Ricker's 136.
- European hare (Andrzejewski and Jezierski 1966): generalized removal estimate 1,039 ± 7.66, versus 1,010 from the regression method; 1,018 hares actually removed.
- Aquatic mayfly (Raleigh, Poudre River): removal estimate N = 207 ± 3.70, 95% CI 199–215; lower limit below animals seen, so truncation to the actual number removed is recommended.
- Feral house mouse (Coulombe, California salt marsh): 173 distinct animals; model selection did not yield a usable estimator, so the authors suggested 173 as the best estimate because nearly all animals were caught.

**Closure test**
- A z-based test using Model Mh statistics; for Coulombe's data, z = −0.403 (P = 0.34362), so closure was not rejected. The authors caution that behavioral response can mimic closure failure.

**Density estimation (grid trapping)**
- Approach: joint estimation of density D and boundary strip width W using nested subgrids and weighted nonlinear least squares. At least four nested grids are recommended; 9 × 9 grids are considered a minimum, with 15 × 15 preferred.
- In the California salt marsh example, estimated W was 4.65 m (SE 0.578), with a significant result (Z = 4.30). A home-range-based estimate of W gave 3.63 m.

**Study design recommendations**
- Prefer livetrapping over removal when possible, since removal estimators are a special case of livetrapping analysis.
- Keep studies short to protect closure; avoid migration and recruitment periods.
- Hold trapping effort constant (same traps, time of day, bait) to reduce time variation; weather should be as constant as possible.
- Aim for the simplest adequate model and maximum captures.
- Use roughly four traps per home range to reduce heterogeneity of access.
- Validate with an independent estimate of the proportion of marked animals where feasible.

**Software and use**
- Program CAPTURE (with user's manual) computes estimates, test statistics, simulations, and model selection. The authors advise biologists with few datasets to submit data to the authors rather than run the program themselves.