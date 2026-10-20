---
name: mark-recapture-open
description: Survival and abundance from open-population models (Cormack-Jolly-Seber, Jolly-Seber), with assumptions, goodness of fit and R workflow.
status: draft
generated: 2026-10-20
---

# mark-recapture-open

## When to use

Unsourced: no supporting source in the brain yet.

## Assumptions and when to use open models

### When open models are needed

Open-population models are appropriate when the population experiences gains or losses between sampling occasions (general). The fundamental distinction from closed models lies in whether the population remains constant or changes through births, deaths, immigration, or emigration [[src:schwarz-arnason-1996]]. In open-model terminology, "birth" encompasses any mechanism adding animals to the catchable population at unknown times, including immigration and recruitment, while "death" refers to all permanent removal processes such as emigration, mortality, and inactivity [[src:schwarz-arnason-1996]].

When the study spans a period long enough that population turnover is expected, or when sampling occasions are sufficiently separated that demographic processes occur between them, open models become necessary (general). The Cormack-Jolly-Seber (CJS) model estimates survival and recapture probabilities [[src:brownie-1993]], while the full Jolly-Seber framework additionally estimates recruitment and population size [[src:schwarz-arnason-1996]].

### Core assumptions of open-population models

Open-population capture-recapture models rest on several foundational assumptions [[src:schwarz-arnason-1996]]. Animals must retain their marks without loss, and marks must be correctly identified upon recapture [[src:brownie-1993]]. Individual animals must behave independently of one another [[src:brownie-1993]]. 

A critical assumption of traditional discrete-occasion models is that sampling events are instantaneous relative to the interval between occasions [[src:barbour-2013]]. This means a cohort should be marked within a short period, a substantial time interval elapses, and subsequent recapture occurs over another brief period [[src:barbour-2013]]. Violating this assumption by treating extended sampling periods as instantaneous can introduce structural bias [[src:barbour-2013]].

### Apparent versus true survival

The CJS model estimates apparent survival (Φ), which confounds true survival with permanent emigration [[src:barbour-2013]]. When emigration occurs, animals leaving the study area appear to have died, making it impossible to separate mortality from emigration using recapture data alone [[src:barbour-2013]]. True survival (s) can only be estimated when emigration is absent or when the study design covers the entire range of marked individuals [[src:barbour-2013]].

### Multistate and non-Markovian extensions

When animals move among discrete strata—such as geographic locations, weight classes, or breeding states—multistate models become appropriate [[src:brownie-1993]]. The Arnason-Schwarz model assumes Markovian transitions, where movement probabilities between strata depend only on the current location [[src:brownie-1993]]. This contrasts with situations where stratum membership is fixed at release or changes predictably, such as aging through age classes [[src:brownie-1993]].

However, the Markovian assumption may fail when animals exhibit site fidelity or memory [[src:brownie-1993]]. Non-Markovian models allow transition probabilities to depend on previous states, accommodating situations where an animal's movement depends on its location in the prior period [[src:brownie-1993]]. Such models proved necessary for Canada geese wintering grounds data, where Markovian assumptions were convincingly rejected [[src:brownie-1993]].

### Continuous detection approaches

The expansion of continuous-resighting technologies—including acoustic receivers and PIT tag antennas—has created data not well-suited to traditional discrete-occasion methods [[src:barbour-2013]] [[src:hewitt-2010]]. Classical capture-recapture models assume instantaneous sampling, but continuous detection systems record encounters throughout the interval between primary sampling periods [[src:barbour-2013]].

The Barker joint-data model addresses this challenge by incorporating both instantaneous primary periods and continuous secondary periods [[src:barbour-2013]]. Secondary periods occur between primary marking occasions and allow marked individuals to be resighted alive or dead continuously [[src:barbour-2013]]. This structure estimates seven parameters compared to the CJS model's two, including true survival when secondary periods cover the population's full range [[src:barbour-2013]].

Simulation studies demonstrate that collapsing continuous detections into discrete bins and applying the CJS model produces substantial bias, particularly for low survival values and time-dependent conditions [[src:barbour-2013]]. The Barker model consistently outperformed CJS across multiple sample sizes when using continuous data [[src:barbour-2013]], though its higher parameter count can create convergence difficulties requiring alternative optimization methods [[src:barbour-2013]].

### PIT tag remote detection advantages

Remote PIT tag antenna systems substantially enhance inference from capture-recapture studies by increasing encounter probabilities [[src:hewitt-2010]]. For endangered Lost River suckers monitored between 1999 and 2007, traditional trammel net sampling yielded consistently low encounter probabilities below 0.2, resulting in poor precision for apparent annual survival estimates [[src:hewitt-2010]]. After deploying remote antennas at spawning locations beginning in 2005, encounter probabilities approached 100% [[src:hewitt-2010]].

The enriched encounter histories from remote detection enable more robust inferences about survival dynamics and support exploration of more realistic models and hypotheses [[src:hewitt-2010]]. This technology has made large-scale tagging studies practicable in systems where they were previously infeasible [[src:hewitt-2010]], though investigators must address the continuous-data characteristics when selecting appropriate analytical models.

## Survival and capture probability structure

Open-population mark-recapture models estimate survival, capture probability, and abundance when individuals can enter or leave populations between sampling occasions [[MultistateRecaptureModelsModel_2002]]. The Cormack-Jolly-Seber (CJS) model is the canonical framework for estimating survival and recapture probabilities [[MultistateRecaptureModelsModel_2002]].

Survival and capture probability can be structured to account for temporal, spatial, and individual variation [[EvaluationOfALongtermPredatorR_2016]]. Survival rates may be modeled with effects of location (reach), time interval, and individual covariates such as fish length using linear and quadratic terms [[EvaluationOfALongtermPredatorR_2016]]. Capture probability can vary by year, location, sampling pass, and individual characteristics [[EvaluationOfALongtermPredatorR_2016]].

Individual heterogeneity in capture probability can be addressed using the Huggins closed-capture model, which allows inclusion of individual covariates [[EvaluationOfALongtermPredatorR_2016]]. Length-dependent capture probability may exhibit threshold effects, such as constant capture probability above 600 mm total length [[EvaluationOfALongtermPredatorR_2016_X-6cf6a615]]. Temporary emigration parameters can be incorporated or fixed at zero to reflect no-movement assumptions [[EvaluationOfALongtermPredatorR_2016]].

Multistate extensions of the CJS model (Arnason-Schwarz model) estimate survival, movement, and transition probabilities when individuals can move among a finite set of geographical sites or states between sampling occasions [[MultistateRecaptureModelsModel_2002]]. These models address spatial population dynamics, dispersal estimation, and heterogeneity in capture probability [[MultistateRecaptureModelsModel_2002]].

## Tag loss and detection

Tag loss can confound survival and abundance estimation in mark-recapture studies. Fish should be scanned with PIT tag readers at multiple time points: immediately after tagging to verify insertion and unique ID, before placement in study enclosures, and at study end [[EffectOfPassiveIntegratedTrans_2025]]. Fish without detectable tags should be scanned multiple times and inspected for tagging scars to distinguish between control fish and fish that ejected tags [[EffectOfPassiveIntegratedTrans_2025]].

Study areas should be scanned with portable antennas to locate ejected tags [[EffectOfPassiveIntegratedTrans_2025]]. Tag loss should be attributed to specific causes when possible based on physical evidence such as healed scars [[EffectOfPassiveIntegratedTrans_2025]].

Detection probability varies by tagging technology and study design. PIT tag detection probability at submersible antennas has been estimated at 0.6–0.9 [[MovementEcologyOfImperilledFis_2020_X-49b0cb00]] [[RazorbackSuckerMovementStrateg_2020]]. Lower detection rates for recently tagged fish compared to previously tagged fish may result from tag loss, mortality, or lack of movement, though causes cannot always be distinguished [[RazorbackSuckerMovementStrateg_2020]]. Tag malfunction may also contribute to failed detections [[RazorbackSuckerMovementStrateg_2020]].

## Goodness of fit and model selection

Model fitting uses maximum likelihood estimation via iterative minimization of deviance (-2×log-likelihood) [[MultistateRecaptureModelsModel_2002]]. Parameters are estimated within a generalized linear model framework with logit link functions and design matrices for linear constraints [[MultistateRecaptureModelsModel_2002]].

Model selection employs AIC and likelihood ratio tests [[MultistateRecaptureModelsModel_2002]] [[EstimatingAnimalAbundance_X-e15b3990]]. AICc model selection can identify top-ranked models based on Akaike weight [[EvaluationOfALongtermPredatorR_2016]]. Analysis of Northern Pike produced a top model carrying 72% of Akaike weight with 108 estimable parameters [[EvaluationOfALongtermPredatorR_2016]].

Goodness-of-fit assessment uses χ² tests when the number of states and sampling occasions are small, comparing observed versus expected capture histories [[MultistateRecaptureModelsModel_2002]]. For larger models, parametric bootstrap (Monte Carlo simulation) provides goodness-of-fit evaluation [[MultistateRecaptureModelsModel_2002]].

Convergence diagnostics include profile deviance plots to detect local minima and non-identifiability of parameters [[MultistateRecaptureModelsModel_2002]].

## Bayesian and software implementation

### When Bayesian and hierarchical approaches help

Bayesian and hierarchical formulations address key challenges in mark-recapture analysis, particularly when data are sparse or parameters vary across multiple spatial or temporal groupings [[src:calvert-2009]]. Conventional frequentist mark-recapture estimates are sensitive to low survival and capture probabilities, small sample sizes, and limited sampling intervals, such that sparse data greatly constrain precision [[src:calvert-2009]]. The Bayesian framework offers greater analytical power by treating parameters as random variables, explicitly recognizing uncertainty, and enabling hierarchical structures that "borrow" information across related replicates (years, sites, or taxonomic groups) [[src:calvert-2009]].

Hierarchical Bayes is especially advantageous when parameter variation requires partitioning across several spatial or temporal replicates, accommodating stochasticity at multiple levels in a manner similar to random-effects models [[src:calvert-2009]]. Multi-state models in particular benefit from this approach: when estimating movement and survival across sparse daily encounters nested within years, hierarchical structuring simultaneously models complex multi-scale decisions while balancing between ignoring inter-year variance and analyzing years entirely independently [[src:calvert-2009]].

### NIMBLE model organization

The NIMBLE framework extends the BUGS language for flexible model specification and provides a system for programming algorithms that adapt to different model structures [[src:devalpine-2017]]. NIMBLE comprises three main components: BUGS code as a model declaration language, the `nimbleFunction` system for programming with models, and a compiler for models and functions [[src:devalpine-2017]].

When building a NIMBLE model (general), the workflow proceeds as follows: (unsourced)

1. **Model block**: BUGS code declares the hierarchical structure, specifying stochastic nodes (prior distributions) and deterministic nodes (derived quantities). (unsourced)
2. **Constants**: Fixed structural elements such as the number of capture occasions, individuals, or sites. (unsourced)
3. **Data**: Observed encounter histories and covariates. (unsourced)
4. **Inits**: Starting values for latent variables (e.g., true states, activity centers) and parameters. (unsourced)
5. **Monitors**: Parameters and derived quantities to track in MCMC output. (unsourced)
6. **Building and running MCMC**: Create the model object, configure MCMC samplers, compile to C++ via the Eigen library, and run chains [[src:devalpine-2017]].

NIMBLE allows specialization of samplers to particular nodes or blocks. The first evaluation stage adapts a function to a specific model structure (e.g., creating a Metropolis-Hastings sampler for a block), while the second stage executes repeated computations efficiently using compiled code [[src:devalpine-2017]].

### Hierarchical and spatial extensions

Spatial capture-recapture models for camera-trapping exemplify hierarchical structures where individual activity centers are latent random effects [[src:royle-2009]]. A point process model describes the distribution of home-range centers in space, and an observation model links trap-specific capture probabilities to the distance between centers and trap locations [[src:royle-2009]]. The models adopt a Bayesian framework using data augmentation, formulated as zero-inflated binomial or Poisson regression with random effects [[src:royle-2009]].

Multi-state hierarchical models employ latent state variables **z** representing the true (unobserved) states of individuals, distinct from the observed encounter histories **x** [[src:calvert-2009]]. Data augmentation addresses the unknown population size *N* by introducing auxiliary indicator variables for whether each augmented individual is real or pseudo-absent [[src:royle-2009]]. This zero-inflation approach enables MCMC sampling over both latent states and abundance [[src:royle-2009]].

(General): In hierarchical capture-recapture, random effects can model site-level variation in survival or detection, with hyperparameters describing the distribution of site-specific parameters. NIMBLE's flexibility supports adding nodes to transform alternative parameterizations automatically [[src:devalpine-2017]].

### Convergence and posterior checks

(General): Standard MCMC diagnostics—trace plots, Gelman-Rubin statistics, effective sample size—verify convergence. NIMBLE provides tools to query model structure and calculate log probability values for posterior predictive checks [[src:devalpine-2017]].

### Goodness of fit by calibrated simulation

For integrated or Bayesian population models, goodness of fit can be assessed through calibrated simulation, motivated by Bayesian *P*-values [[src:besbeas-2014]]. The method simulates replicate datasets from the fitted model, drawing parameter values from the asymptotic multivariate normal distribution of maximum-likelihood estimates (or from the posterior in fully Bayesian settings) [[src:besbeas-2014]]. For each simulated parameter vector θ*ᵢ* and corresponding data *xᵢ*, a discrepancy measure *D*(*xᵢ*; θ*ᵢ*) is calculated and compared to *D*(*x*; θ*ᵢ*) from the real data [[src:besbeas-2014]]. If the model fits well, approximately half the simulated discrepancies should exceed the observed values [[src:besbeas-2014]].

Different discrepancy measures highlight different aspects of fit: for time-series components, one might compare observed versus expected counts or examine prediction-error quantiles; for capture-recapture components, one might compare observed versus expected individual encounter frequencies [[src:besbeas-2014]]. Calibration is necessary when test statistics may appear extreme, and is achieved by repeated simulation from the fitted model to generate the reference distribution [[src:besbeas-2014]].

### NIMBLE sketch: CJS state-space form

```r
# Sketch (unexecuted) of Cormack-Jolly-Seber in NIMBLE state-space form
# Verify against package documentation before use

library(nimble)

cjs_code <- nimbleCode({
  # Priors
  phi ~ dunif(0, 1)    # Survival probability
  p ~ dunif(0, 1)      # Detection probability
  
  # State-space model for each individual
  for (i in 1:M) {
    # True alive/dead state (latent)
    z[i, first[i]] <- 1  # Alive at first capture
    for (t in (first[i] + 1):T) {
      z[i, t] ~ dbern(z[i, t-1] * phi)
    }
    
    # Observation process
    for (t in first[i]:T) {
      y[i, t] ~ dbern(z[i, t] * p)
    }
  }
})

# Caveat: for an individual first captured on the last occasion the loop range (first[i] + 1):T is empty or reversed; drop such
# individuals (they carry no survival information) or guard the loop before building the model.
# Constants: M individuals, T occasions, first[i] = first capture
# Data: y[i,t] encounter matrix (0/1)
# Inits: starting z, phi, p
# Build model, configure MCMC, compile, run (details omitted)
```

[[src:devalpine-2017]] [[src:calvert-2009]] [[src:royle-2009]] [[src:besbeas-2014]]

## Workflow in R

1. Organize capture history data with individual covariates (e.g., length, location) [[EvaluationOfALongtermPredatorR_2016]]
2. Fit Cormack-Jolly-Seber or Jolly-Seber models using Program MARK via RMark [[web:cran-RMark]] [[EvaluationOfALongtermPredatorR_2016]] or marked [[web:cran-marked]]
3. Specify survival and capture probability structures with temporal, spatial, and individual covariate effects [[EvaluationOfALongtermPredatorR_2016]]
4. Conduct model selection using AIC [[MultistateRecaptureModelsModel_2002]]
5. Assess goodness-of-fit using parametric bootstrap [[MultistateRecaptureModelsModel_2002]]
6. Examine convergence with profile deviance plots [[MultistateRecaptureModelsModel_2002]]

## Supplement
See `SUPPLEMENT.md` in this folder for a worked workflow drawn from developer-supplied sources (draft).
