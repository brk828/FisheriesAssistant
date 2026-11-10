---
species: N/A
common_name: N/A
family: N/A
habitat: Terrestrial and freshwater animal populations (small mammals, birds, reptiles, amphibians, fish, invertebrates)
ocean_basin: N/A
location: Patuxent Wildlife Research Center (Laurel, Maryland); Tall Timbers Research Station (Leon County, Florida); Alice Holt Forest Research Station (Surrey, England); Dryden (New York); Cobscook Bay (Maine); Falkner Island (Connecticut); Marshy Point (Manitoba); River Frome (Dorset, England); Lake Ellis Simon (North Carolina)
tags: [capture-recapture, population-ecology, statistics, wildlife-monograph, open-population-models]
title: "Coefficient of Variation Tables from a Scanned Aquatic Biology Document"
source_id: "PML2150"
marsh_id: "PML2150"
library: "Marsh Library"
permission: "not public domain"
source_citation: "K. H. Pollock et al. (1990). Coefficient of Variation Tables from a Scanned Aquatic Biology Document. Wildlife Monographs. Marsh Library ID: PML2150."
source_file: "Pollock K.H. et al. 1990. Wildlife monographs.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Coefficient of Variation Tables from a Scanned Aquatic Biology Document

#ichthyology #marine-biology #capture-recapture

Note on scope: the source is a statistical monograph on wildlife population ecology. Fish appear only as case studies (northern pike, electrofishing, fisheries tag loss), so the taxonomic tags above follow the system instruction for non-fish-focused material.

## Executive Summary

This Wildlife Monograph (No. 107, January 1990, The Wildlife Society) by [[Pollock]], [[Nichols]], [[Brownie]] and [[Hines]] presents a practical, detailed treatment of the design, analysis and interpretation of [[Capture-Recapture]] studies. It covers the [[Lincoln-Petersen Method]] and [[Closed Population Models]] briefly, then develops the [[Jolly-Seber Model]] for open populations in depth. It also covers enumeration estimators, constant-survival restrictions, temporary trap response, cohort analysis, an [[Age-Dependent Model]], and the [[Robust Design]] that combines closed and open models. The authors strongly recommend abandoning the enumeration ("calendar of captures") method in favour of Jolly-Seber-based analyses, and they provide the [[JOLLY]] and [[JOLLYAGE]] computer programs.

## Background & Description

The monograph is one of the Wildlife Monographs series, which the Wildlife Society began in 1957 to publish longer papers than the Journal of Wildlife Management accepts. Sponsors normally fund printing, and the series is editor-supervised (Roy L. Kirkpatrick, Editor; consulting editors Lyman L. McDonald and Gary C. White).

Capture-recapture experiments sample a population k times (usually k > 2). Unmarked animals are uniquely marked on capture, previously marked animals have captures recorded, and animals are released. Batch marks are discouraged because they do not provide full capture histories. Models are classed as:

- **Closed populations:** no permanent additions or deletions during the study.
- **Open populations:** births and/or immigration and deaths and/or emigration occur.

The monograph notes that these definitions differ from usage in other contexts. Parameters of interest are population size, survival, and recruitment (birth plus immigration) at each sampling period. Band-recovery models are mentioned as a related approach, with a recommendation to consult [[Brownie et al. 1985]] for detail.

## Ecological & Environmental Context

The authors frame capture-recapture as a way to test ecological theory against field data. They note that much population theory has weak empirical foundations (citing [[Pielou]]), and that abundance and demographic rates are difficult to measure in nature.

Key assumption violations the monograph addresses:

- **Heterogeneity of capture probability:** variation among individuals (age, sex, social status, trap location). It typically causes negative bias in population size.
- **Trap response:** trap-happy (baited traps) or trap-shy behaviour. Trap-happiness causes negative bias in abundance; trap-shyness causes positive bias. Permanent trap response does not bias survival estimates.
- **Tag loss:** causes underestimation of survival and, in closed models, positive bias in abundance. Double marking is recommended for correction, a method common in [[Fisheries Studies]].
- **Temporary emigration:** likely to be serious in practice, and hard to detect.
- **Non-independence of captures:** in social species such as [[Bobwhite Quail]], captures occur in coveys, so variance estimates are biased low.

Study-area examples cover small mammals (meadow voles, gray squirrels, Nuttall's cottontails), birds (bobwhite quail, rock doves, roseate terns, semipalmated sandpipers, black-capped chickadees, Canada geese), reptiles (American alligators), and fish (northern pike and the River Frome electrofishing study).

## Key Findings

**Methodological recommendations**

- The enumeration ("minimum number known alive" / calendar of captures) method is strongly discouraged. Its survival estimator is only unbiased if every capture probability equals 1, and its population estimator always assumes the unmarked portion is zero. The authors judge that Jolly-Seber estimates perform better even under heterogeneity and trap-happiness.
- The Jolly-Seber model is central. It estimates population size, survival, and recruitment in each period, but cannot separate migration from births and deaths without extra information.
- Restricted models (Deaths Only, Births Only, Constant Survival, Constant Capture) can give large gains in precision when their assumptions are reasonable. Model selection among nested models is recommended, for example using the roseate tern data, where the constant-survival model (B) was judged the simplest adequate model.
- The [[CAPTURE]] program (Otis et al. 1978) provides closed-model estimators (M0 to Mtbh), with jackknife estimators (Burnham and Overton) generally most robust for Mh. Its model selection is recommended with caution because tests have low power in small populations.
- The [[Robust Design]] (Chapter 7) combines closed-model population estimates within primary periods with open-model survival estimates across primary periods. This avoids sampling correlation between N and survival, and it allows estimation of births and immigration separately when there are two or more age classes.

**Worked examples and reported results**

- **Lincoln-Petersen (Nuttall's cottontail, Oregon, 1974):** n1 = 87, n2 = 14, m2 = 7. Chapman estimate N = 164, approximate 95% CI 94–234.
- **Bobwhite quail (Tall Timbers, Florida, 1982):** n1 = 148, n2 = 82, m2 = 39. Chapman estimate N = 308 (SE 29.7), 95% CI 250–366. CAPTURE estimates were almost uniformly lower than Lincoln-Petersen estimates, suggesting negative bias from trap-happiness and heterogeneity.
- **Meadow vole (Patuxent, October 1981, five trapping days):** 102 animals captured; the heterogeneity model Mh was chosen; jackknife N = 189 (SE 10.85), 95% CI 117–161 (as printed). Average daily capture probability 0.44.
- **Gray squirrel (Alice Holt, 1972–74):** a precise Jolly-Seber study with high capture and survival probabilities. Estimates were not reported where captures were fewer than about 5 per period. Heterogeneity and trap-happiness probably caused underestimation of population size.
- **Rock dove (Dryden, New York, 1981):** Jolly's overall test showed significant lack of fit, so high-precision estimates should be treated with caution.
- **Juvenile wood ducks (Montezuma Refuge, 1974):** the Deaths Only model gave a precise N1 = 1,033.17 (SE 64.95) and survival 0.65 (SE 0.080). The overall goodness-of-fit test was marginal (P = 0.09), with the second component significant (P = 0.04).
- **Roseate terns (Falkner Island, 1978–84):** the constant-survival model (B) was selected. Jolly-Seber goodness-of-fit was P = 0.22; Model D was rejected (P < 0.001 versus B).
- **Semipalmated sandpipers (Cobscook Bay, 1982):** Model 2 (one-period marking effect) was strongly preferred over Jolly-Seber (χ² = 27.2, 9 df, P < 0.01), supporting the idea that capture increased departure from the stopover area.
- **Black-capped chickadees (Litchfield, Connecticut, 1958–83):** first-year birds had a survival increase of 0.23 (SE 0.036) over second-year birds when compared with a paired t-test. Adult survival declined about 3.5% per year of age (mean slope −0.0354, SE 0.0174). The authors note that heterogeneity simulations showed negligible bias for these effects.
- **Giant Canada geese (Marshy Point, Manitoba, 1968–70):** age-dependent Model B2 was selected. Unadjusted survival was about 0.52 for young and 0.68 for adults. Collar loss (about 25%/year) would adjust these to roughly 0.69 and 0.91.
- **Northern pike (River Frome, Dorset, 1971–79):** age dependence in survival and capture was supported with a one-tailed test (Z = 1.60, P = 0.055 for Model D2; Z = 1.73, P = 0.042 for Model B2). Estimated adult population was about 30–50 fish, and tag loss about 0.095/year.
- **Alligators (Lake Ellis Simon, 1976–79):** the jackknife estimate for 1978 (140, SE 28.5) was roughly double the Jolly-Seber estimate (69, SE 12.6), consistent with strong heterogeneity.
- **Meadow vole robust design (Patuxent, June–December 1981):** closed-model population estimates were consistently higher than Jolly-Seber estimates. Average daily capture probability from M_h ranged 0.35–0.56, and the Jolly-Seber capture probability averaged 0.91.

**Design guidance (Chapter 8)**

- Study design should satisfy as many model assumptions as possible. Sampling should be spatially even, and trap spacing should be smaller than the average home-range radius.
- Two sampling methods are a good way to avoid heterogeneity bias in Lincoln-Petersen studies, but open models need at least three samples and usually more.
- Prebaiting may reduce trap-happiness, and resighting-only designs avoid trap response.
- Simulation (for example with POPAN-3) is recommended at the design stage.
- A rough rule of thumb is that a coefficient of variation of about 20% is reasonable. The authors' figures show that precision improves with more samples, higher capture and survival probabilities, and larger populations. For a population of about 100 with survival 0.75 and 10 samples, a capture probability of about 0.38 gives CV = 20% for population size and survival, but about 0.76 is needed for birth numbers.
- Telemetry and direct mortality methods are discussed as alternatives. Band-recovery models are preferred when permanent emigration is likely and hard to estimate, but they are less precise.

**Conclusions**

The authors conclude that the Jolly-Seber framework, its restricted and generalised variants, and the robust design together give a practical toolkit for biologists. They also stress that goodness-of-fit tests have limited power in small populations, and that a non-significant result does not guarantee that assumptions hold.