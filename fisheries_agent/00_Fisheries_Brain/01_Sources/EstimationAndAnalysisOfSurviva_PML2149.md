---
species: Anas rubripes
common_name: American Black Duck
family: Anatidae
habitat: Winter study area in New Jersey; habitat type not described
ocean_basin: Atlantic
location: New Jersey, USA
tags:
  - waterfowl
  - survival-analysis
  - radiotelemetry
title: "Estimation and Analysis of Survival Distributions for Radio-Tagged Animals"
source_id: "PML2149"
marsh_id: "PML2149"
library: "Marsh Library"
permission: "not public domain"
source_citation: "K. H. Pollock, S. R. Winterstein, M. J. Conroy (1989). Estimation and Analysis of Survival Distributions for Radio-Tagged Animals. Biometrics 45, 99-109. Marsh Library ID: PML2149."
source_file: "Pollock K.H. et al. 1989. Estimation and analysis of survival distributions for radio tagged animals .pdf"
text_extraction: "text"
---
# Survival Analysis for Radio-Tagged Animals

#waterfowl #anatidae #survival-analysis

## Executive Summary

This methods paper develops a continuous-time framework for estimating survival distributions in [[Radiotelemetry]] studies, where animal death times are often right-censored. The authors adapt [[Kaplan-Meier Estimator|Kaplan-Meier]] product-limit estimation, [[Hazard Function|hazard]]-based regression, and the [[Proportional Hazards Model]] from medical and engineering survival analysis. The approach is illustrated with a first-year dataset of 50 radio-tagged female [[American Black Duck|black ducks]] in New Jersey. The authors conclude that the methods give a more realistic analysis than earlier discrete-time approaches, while stressing the need to check model assumptions, especially random censoring and proportional hazards.

## Background & Description

Radiotelemetry fits a small radio transmitter to a captured animal, releases it, and tracks the signal until the animal dies or is censored. Earlier survival analyses of such data assumed that each survival event was independent and had a constant probability across all periods (for example, [[Trent and Rongstad Method|Trent and Rongstad]] 1974 and [[Bart and Robson Method|Bart and Robson]] 1982). The authors note that these assumptions are often unrealistic. [[Band-Return Models]] and [[Capture-Recapture Models]] offer related discrete-time approaches, and the paper treats them as points of comparison.

The proposed framework uses continuous survival models with right censoring, which are widely used in medicine and engineering (Kalbfleisch and Prentice; Cox and Oakes). An animal's exact survival time is usually known to within 1 or 2 days. Censoring can arise from three causes:

1. A transmitter fails before the animal dies.
2. The animal emigrates from the study area.
3. The animal survives past the end of the study period.

The paper's key assumptions are:

- A random sample of animals from a particular age and sex class.
- Independent survival times among individuals.
- Random censoring, which the authors call "extremely important."
- A defined time origin, since radiotelemetry lacks a natural starting point such as treatment.

## Ecological & Environmental Context

The example is framed around overwintering survival, which the authors describe as a seasonal problem. Survival from a summer origin can differ from survival over the same length of time from a winter origin, so the choice of time origin matters. Seasonal effects are described as usually less important in medical studies.

The example data come from the first year of a multiyear study by the [[U.S. Fish and Wildlife Service]] on movements and overwintering survival of black ducks. Mortality was attributed to hunting and to natural causes. Non-hunting causes listed include predation (by a predator such as a red fox) and emaciation during a winter freeze. The hunting season closed on day 36 of the monitored period, and no mortality was recorded after day 42. The authors link this pattern to both the end of hunting and the weather.

Two stages of the bird's life are compared. Hatch-year birds are those born during the previous breeding season. After-hatch-year birds are older. The authors state that young migratory birds typically do not fare well in their first winter or in their first exposure to hunting.

## Key Findings

**Methodological framework**

- **Kaplan-Meier product-limit estimation** is the main nonparametric tool. It handles censored data and is applied with [[Greenwood's Formula]] for variance and approximate 95% confidence intervals.
- **Exponential survival** was tested by plotting the log of the survival function against time. The linear pattern supports the exponential model, but the authors base most discussion on the nonparametric estimates.
- **Proportional hazards model**: covariates multiply a baseline hazard by a constant factor. Censoring is easily accommodated.
- **Left truncation**, needed when animals enter the study gradually, can be handled by extending the Kaplan-Meier estimator, as described in Cox and Oakes (1984).

**Black duck example**

- **Sample:** 50 female black ducks captured near New Jersey, between 9 November and 14 December 1983. Of these, 31 were hatch-year birds and 19 were after-hatch-year birds.
- **Monitoring:** Birds were located from release until the study ended on 15 February 1984. Analysis used a 63-day window from 15 December 1983 to 15 February 1984, since all birds were known to be alive on 15 December.
- **Mortality:** There were 18 deaths in total. Ten were attributed to hunting, and the rest to natural causes.
- **Battery life:** Transmitter batteries were projected to last about 90 days.
- **Kaplan-Meier survival:** The estimate at the end of the window was 0.5865 (standard error 0.0754).
- **Overall study comparison:** In the broader study (Conroy et al.), hatch-year birds had a lower overall survival rate of 0.60, compared with 0.73 for after-hatch-year birds.

**Age-class comparison**

- The final survival estimates for hatch-year and after-hatch-year birds were almost identical, but the survivor curves had quite different shapes.
- The likelihood ratio test showed no significant age effect.
- The log-rank and generalized Wilcoxon tests did not reject the null hypothesis of identical survival distributions.
- The Breslow, Edler, and Berger scores test, which is sensitive to crossing hazards, gave a significant result (z = 3.1, p = .002). The authors take this as evidence that the two survival curves are not equal and that the proportional hazards assumption fails for these data.

**Condition index**

- Condition index was calculated as body weight (g) divided by wing length (mm).
- For all 50 ducks, survival was related to condition index (χ² = 4.75, p < .05). The authors note this fit was based on a model that also assumes proportional hazards.
- Within age classes, survival of after-hatch-year birds was significantly related to condition index (χ² = 4.91, p < .05; n = 19).
- For hatch-year birds (n = 31), survival was not significantly related to condition index (χ² = 1.06, p > .25). The authors were unable to explain this result biologically and expected condition to affect survival in both age classes.

**Limitations and future needs**

- The authors state that the validity of the assumptions requires further research, particularly random censoring and independence.
- The discussion highlights the risk of informative censoring, where censoring is linked to survival time. Extreme bounds can be used to address it, but they may be very wide when censoring occurs early.
- The authors note that parametric modelling may improve precision in estimating small tail probabilities, though [[Miller Comparison|Miller (1983)]] found that the Kaplan-Meier estimator performed poorly against maximum likelihood in some cases.
- The paper concludes that the choice of time origin is critical in this application and that the extension to left truncation with right censoring will be important as animals enter the study gradually.