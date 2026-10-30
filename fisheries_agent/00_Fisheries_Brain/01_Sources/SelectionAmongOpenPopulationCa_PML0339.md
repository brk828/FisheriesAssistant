---
species: "Strix occidentalis (northern spotted owl, used as the data example); simulated capture-recapture data (no real species)"
common_name: "Northern Spotted Owl (example); Simulated Capture-Recapture Data"
family: "N/A"
habitat: "N/A"
ocean_basin: "N/A"
location: "Colorado, USA (Colorado Cooperative Fish and Wildlife Research Unit; Colorado State University, Fort Collins)"
tags: [capture-recapture, model-selection, akaike-information-criterion, biostatistics, open-population-models]
title: "Selection among open population capture-recapture models when capture probabilities are heterogeneous"
source_id: "PML0339"
marsh_id: "PML0339"
library: "Marsh Library"
permission: "not public domain"
source_citation: "K. P. Burnham, D. R. Anderson, G. C. White (1995). Selection among open population capture-recapture models when capture probabilities are heterogeneous. Journal of Applied Statistics, Vol. 22, Nos 5&6, pp. 611-624. Marsh Library ID: PML0339."
source_file: "Burnham et al. 1995. Selection Among Open Population Capture-Recapture Models when Capture Probabilities are Heterogeneous.pdf"
text_extraction: "text"
---
# Selection Among Open Population Capture-Recapture Models When Capture Probabilities Are Heterogeneous

#aves #biostatistics #capture-recapture

## Executive Summary

This methodological paper by [[Burnham]], [[Anderson]] and [[White]] (1995) examines how well two information-theoretic criteria choose parsimonious models for open-population capture-recapture data when individual capture probabilities vary. The authors compare [[Akaike's Information Criterion]] (AIC) and a dimension-consistent criterion (CAIC) using Monte Carlo simulation of nested [[Cormack-Jolly-Seber Model]] (CJS) structures. Model quality is judged by the expected [[Residual Sum of Squares]] (RSS) of survival and recapture estimates. The central result is that heterogeneity in capture probabilities has a negligible effect on model selection under either criterion. Selected model size grows with sample size under both AIC and CAIC, with CAIC consistently choosing smaller models. The paper is a statistical study rather than an ichthyological one; it contains no fish data.

## Background & Description

The paper addresses the problem of model selection in open-population capture-recapture analysis, where survival (φ) and recapture (p) probabilities must be estimated from marked animals. The authors motivate the problem with a data set on the threatened [[Northern Spotted Owl]], which has males and females in two to four age classes, 14 large study sites, and 4–9 occasions. A [[Global Model]] for these data might contain 400–500 parameters, so a parsimonious reduced model is needed for interpretable inference.

The authors frame model selection around the [[Kullback-Leibler Discrepancy]] (K-L), which measures the divergence between the true sampling distribution and an approximating model. AIC estimates this discrepancy as:

- AIC = −2 log L(θ̂) + 2K

where K is the number of estimated parameters. AIC balances fit (bias) against model size (variance). CAIC uses a heavier penalty, log(n) + 1 per parameter, and was derived from a Bayesian viewpoint ([[Bayesian Information Criterion]]). The authors argue that CAIC's assumption of a fixed true model dimension is poorly supported for field biology, where more data reveal more structure.

Earlier work by the same group ([[Burnham et al. 1995]]; [[Anderson et al. 1994]]) showed that AIC and CAIC outperform hypothesis testing in selecting low-RSS models, and that quasi-likelihood adjustments are needed when data are overdispersed.

## Ecological & Environmental Context

The simulations are built around a treatment-control experiment with marked animals over six capture occasions. The three generating models were:

- **H0:** a null model with no treatment effect.
- **H2p:** a treatment affecting the first survival and first recapture probabilities.
- **H36:** a chronic treatment effect with many small effects, using 10 occasions and 34 parameters. Its dampened-effect variant is used to test dimension as a function of sample size.

Capture histories were generated individually with the program [[Program RELEASE]] using Bernoulli events for survival and capture. Heterogeneity in capture probability was introduced with a [[Beta Distribution]]. The authors note that the results are not specific to treatment-effect models and that the parameter values reflect many annual vertebrate sampling situations. The paper also refers to fisheries data in its citations, as in the reference to fish survival experiments (Burnham et al. 1987), but no fish populations are analyzed.

## Key Findings

**Study design**

- A 3^6 factorial design was used: six factors (sample size of new releases u, occasions k, survival φ, mean capture probability p, heterogeneity γ, and true model) with three levels each. The 729 treatment combinations ran 1000 repetitions each.
- Simulated levels included p = 0.4, 0.6 and 0.8; φ = 0.5, 0.7 and 0.9; releases u = 50, 100 and 300; and γ = 0, 0.25 and 0.5. The 243 base cases (3^5) took about 12 days of CPU time.
- Closed-form MLEs were used because numerical methods would have increased computing time five to ten fold.

**Heterogeneity effect**

- Heterogeneity in capture probability had a negligible effect on model selection under AIC or CAIC.
- In ANOVA rankings, factors such as φ, p, u and the true model were far more important than γ. γ was about as unimportant as the number of occasions k. For the MINRSS comparison, the F-values for γ and k were two orders of magnitude smaller than those of the other four factors.
- Average RSS ratios relative to the minimum RSS (MINRSS) were close to 1 at all heterogeneity levels (roughly 1.05–1.09 in the reported table). Increasing heterogeneity slightly favored smaller RSS values for the selected models.

**Model size increases with sample size**

- For H36 (34 parameters at 10 occasions), AIC-selected models averaged 26.1 parameters (SD = 3.9) at 50 releases per occasion, rising to 29.5 (SD = 1.9) at 300 releases.
- CAIC-selected models averaged 17.7 parameters (SD = 0.77) at 50 releases and 19.9 (SD = 2.0) at 300 releases.
- Increasing capture probability made little difference to model size under CAIC.
- CAIC selected about eight to ten fewer parameters than AIC, roughly 32% fewer in these cases.

**Conclusions and recommendations**

- The authors favor an AIC-based strategy over hypothesis testing, particularly for non-nested models and for studies without a formal experimental treatment.
- When several models lie within about two AIC units of the minimum, inference should be drawn from that subset rather than a single model. In nested cases the simplest model may be chosen.
- CAIC may achieve low RSS through large bias and small variance, so confidence-interval coverage for CAIC-selected models is a priority for future research.
- The global model should stay well below the study's sample size.