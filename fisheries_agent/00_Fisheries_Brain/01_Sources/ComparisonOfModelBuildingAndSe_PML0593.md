---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [mark-recapture, model-selection, population-ecology, simulation-study]
title: "Comparison of model building and selection strategies"
source_id: "PML0593"
marsh_id: "PML0593"
library: "Marsh Library"
permission: "not public domain"
source_citation: "P. F. Doherty, G. C. White, K. P. Burnham (2010). Comparison of model building and selection strategies. Journal of Ornithology (EURING Proceedings), DOI 10.1007/s10336-010-0598-5. Marsh Library ID: PML0593."
source_file: "Dohery P.F. et al. 2010. comparison of model buliding and selection strategies.pdf"
text_extraction: "text"
---
# Comparison of Model Building and Selection Strategies

#wildlife-population-ecology #mark-recapture #model-selection

## Executive Summary

This methods paper, by [[Paul F. Doherty]], [[Gary C. White]] and [[Kenneth P. Burnham]] and published in the *Journal of Ornithology* (EURING Proceedings), asks how analysts should limit the number of a priori models in complex [[Mark-Recapture]] analyses. It uses a [[Simulation Study]] of [[Cormack-Jolly-Seber Model]] data to compare an all-combinations model building strategy against two ad hoc, stepwise strategies, and tests whether [[Model Averaging]] improves results. The paper finds that the strategy had little effect on parameter bias and precision, that model averaging helped slightly, and that ad hoc strategies gave misleading [[Variable Importance]] weights. The authors recommend the all-combinations strategy with model averaging.

## Background & Description

Model selection is central to mark-recapture analysis, but a model set must exist before selection can occur. These models have several apparent survival (φ) and detection (p) parameters in one likelihood, each modeled with separate covariates. Model selection acts on the whole likelihood, yet biologists usually think about each parameter separately.

Current guidance is limited. [[Burnham and Anderson]] (2002) advise a concise candidate set of about 4 to 20 models, warn that examining "all possible models" with stepwise selection risks spurious results, and note that the number of models should not exceed the sample size. The authors observe that this advice conflicts with modern practice, because highly structured models, large data sets and fast computers allow sets of hundreds of models. Multi-state models make the number of higher-level parameters effectively unlimited.

The historical reference is [[Lebreton et al. 1992]], who proposed a "step-down" approach: fix a high-dimensional survival structure, select the capture-probability model, then select the survival model. Lebreton et al. favored this order but noted that the reverse order could yield a different model. They gave no guidance when more than two higher-order parameters are present.

Other concepts include:
- [[Akaike's Information Criterion]] (AIC) and AIC model weights
- Model averaging, in which parameter estimates are weighted by AIC weights across the model set (following Burnham and Anderson 2002)
- [[Cumulative AIC Weight]], the sum of weights of all models containing a variable, used to rank variable importance
- [[Stepwise Selection]] and [[Step-Down Selection]]

The authors note that "all possible models" would technically be infinite, so they use "all combinations" to mean combinations of a limited set of predictors.

## Ecological & Environmental Context

The study is a simulation, not a field study, and no real species or site is analyzed. The authors focus on the [[Cormack-Jolly-Seber Model]] and say that more complex models, such as the [[Barker Model]], [[Multi-State Model]] and robust design, would add difficulty for ad hoc strategies, because choosing the order in which parameters are modeled becomes tenuous. Examples cited include mallard breeding-ground fidelity, wintering sparrow survival and [[Adelie Penguin]] flipper-band effects, but these are references and not analyzed data.

The paper also raises a general point about [[Statistical Versus Biological Importance]]. Large sample sizes can make weakly relevant variables appear important, which parallels problems with hypothesis testing.

## Key Findings

**Simulation design**
- A study with 15 occasions was simulated, giving 14 φ and 14 p parameters. The generating model was (φ, p), with covariates included in the generating model but not explaining all variation.
- Each parameter was a function of four covariates (eight in total). Covariates had mean 4 and SD 1, and were correlated with the true parameter values to differing degrees.
- Three parameter sets were chosen from more than 1,000 screened sets to give a range of realized correlations.
- For each set, 1,000 data sets were simulated. Each had 100 animals released at occasion 1 and 20 releases on each later occasion, keeping the population near 100.
- Extra simulations raised the number released tenfold and 100-fold to test how sample size affects behavior.

**Three strategies and six variants**
- **φ-first:** Hold φ at full additive covariate dimensionality, select the best p model, then fix p and model φ. This gives 31 models.
- **p-first:** The reverse order, also giving 31 models.
- **All combinations:** Every covariate combination for φ and p, giving 256 models.
- Each strategy was run with minimum AIC selection and with model averaging, for six variants in total.

**Estimator bias and precision**
- The three strategies gave nearly identical RSS values and rankings. None of the selected minimum-AIC models approached the minimum possible RSS, but all were roughly the same distance from it.
- Model-averaged estimates always had smaller RSS values and smaller SDs, so model averaging was consistently advantageous.
- Selected AIC models had fewer parameters than the minimum-RSS model.
- The fully time-specific model had larger RSS than all selection strategies at these sample sizes, because about 27 parameters were poorly estimated. At larger sample sizes it had smaller RSS than the selection strategies.

**Variable selection**
- The strategies differed markedly in cumulative variable weights. The φ-first strategy often gave weights above 0.5 to weakly correlated p covariates, while all-combinations gave lower weights and p-first gave the lowest.
- The reverse pattern held for weakly correlated φ covariates: p-first gave the highest weights and φ-first the lowest.
- Strongly correlated covariates received similar weights under all three strategies.
- Unbalanced model sets (where variables appear in different numbers of models) were a likely cause. In the ad hoc strategies, the parameter held at high dimensionality was forced to absorb variation in the data.

**Sample size effects**
- Increasing sample size drove all cumulative variable weights toward 1, including for covariates with little real correlation. With infinite sample size, all variables with any predictive influence reach weight 1.
- The authors argue that statistical importance, which depends on sample size, must be distinguished from biological importance.
- In mark-recapture, the relevant sample size is closer to the number of releases than to the number of individuals.

**Conclusions and recommendations**
- The all-combinations strategy with model averaging is recommended. A balanced all-combinations model set is considered best for estimating variable weights.
- If an ad hoc strategy is used to reduce computation, parameter estimates will generally be comparable to all-combinations, but variable weights will not.
- Barbieri and Berger (2004) suggest that variables with cumulative weight above 0.5 be treated as most important, and the authors warn that the ad hoc strategies could then yield spurious conclusions.
- The authors mention an untested measure of variable support for unbalanced model sets, suggested by MacKenzie, which adjusts cumulative weights by how often each variable appears in the model set. The authors do not validate it.
- The authors call their work "a small step" and identify further needs: other parameter values, correlation structures, and more complex models such as multi-state models.