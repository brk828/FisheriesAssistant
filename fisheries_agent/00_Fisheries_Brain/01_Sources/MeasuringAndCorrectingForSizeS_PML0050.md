---
species: Salmo trutta
common_name: Brown trout
family: Salmonidae
habitat: Freshwater stream (spring-fed, naturalized population)
ocean_basin: N/A
location: West Indian Creek, southeastern Minnesota, USA
tags: [ichthyology, marine-biology, salmonidae, electrofishing, mark-recapture, size-selectivity, population-estimation, freshwater]
title: "Measuring and Correcting for Size Selection in Electrofishing Mark-Recapture Experiments"
source_id: "PML0050"
marsh_id: "PML0050"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. S. Anderson (1995). Measuring and Correcting for Size Selection in Electrofishing Mark-Recapture Experiments. Transactions of the American Fisheries Society 124:663-676. Marsh Library ID: PML0050."
source_file: "Anderson 1995. Measuring and Counting for Size Selection in Electrofishing Mark-Recap Experiments.pdf"
text_extraction: "text"
---
# Measuring and Correcting for Size Selection in Electrofishing Mark-Recapture Experiments

#ichthyology #marine-biology #salmonidae

## Executive Summary

This methods paper addresses size-selective bias in [[Electrofishing]] surveys. Electrofishing captures a disproportionately large share of big fish, so [[Capture Probability]] varies with body length and the standard [[Chapman-Petersen Estimate]] tends to underestimate population size. The author proposes [[Smoothing Splines]], a nonparametric regression that lets the data reveal the form of [[Size Selectivity]], as a way to estimate capture probability as a continuous function of size. The method is applied to a two-sample [[Mark-Recapture]] experiment on [[Brown Trout]] in [[West Indian Creek]], Minnesota, and compared with Chapman-Petersen, [[Parametric Logistic Model]] and [[Depletion Estimate]] approaches. [[Monte Carlo Simulation]] of known populations then evaluates bias, coverage and root mean squared error (RMSE). Spline-based estimates generally had less bias and better coverage than Chapman-Petersen estimates for the size-group where capture probability changed rapidly, and for the total population.

## Background & Description

**Problem.** Electrofishing selectivity has no established parametric form, unlike [[Gill Net]] selectivity (normal, lognormal or logistic functions), [[Trawl]] selectivity, or hook selectivity. Capture probability is the product of several conditional probabilities: the fish is encountered, is incapacitated by the current, is seen, and is netted. Each step may depend on size. Electrofishing therefore under-samples small, young or slow-growing fish, biasing estimates of abundance, length distribution, growth and production (Reynolds 1983).

**Traditional remedies.** Analysts often split data into length-groups to reduce bias (Sullivan 1956; Vincent 1971; Bohlin and Sundstrom 1977). This approach has drawbacks:
- Estimates change erratically with the choice of groups, especially when group sizes are small.
- The bias-variance trade-off is obscured.
- Restricting analysis to sizes with roughly constant capture probability discards information.

**Prior models.** [[Otis Model Family]] (Otis et al. 1978) tests equal catchability over time, behavioral response and individual heterogeneity, but it requires more than two sampling occasions. [[Miller Logistic Extension]] (Miller 1988) derived size-group variances but offered no covariance terms for total-population variance.

**Study aims.** The paper:
1. Estimates capture probability as a smooth function of size with smoothing splines.
2. Calculates population estimates from several models: Mt (heterogeneity by size, the simplest estimate), Mo (constant capture), Mt-sample-time differences, and Mh-depletion.
3. Compares bias and RMSE of spline, parametric and Chapman-Petersen estimates through simulation.

**Study site and field methods.** The data were collected by Thorn (1992) in West Indian Creek, a spring-fed stream in southeastern Minnesota with a naturalized brown trout population. Key features:
- Study reach: 0.77 km long, mean width 5.2 m, late-summer discharge 0.21 m³/s, alkalinity 220-250 mg/L as CaCO₃.
- Overhead bank cover installed in 1981 to improve habitat.
- September 1988: reach electrofished with pulsed DC power by three people. Fish from the first pass were anesthetized with MS-222, measured for total length, batch-marked by clipping the top of the caudal fin, and released.
- The reach was re-sampled 3 days later. Total length and mark status were recorded for each fish.

## Ecological & Environmental Context

- **Closure and stress.** The 3-day interval and the short reach were judged sufficient for population closure. Fish recovered quickly after release, so stress-induced catchability change was considered minimal (Peterson and Cederholm 1984).
- **Measurement quality.** Remeasurement error was small, so length could identify individually marked fish. Of 198 recaptures, 158 matched marked fish exactly, 38 were within 2 mm, and the remainder differed by 3 mm.
- **Size dependence and management.** Large fish, which are rare and often a management goal, are the hardest to sample. Grouping large fish with smaller ones underestimates their capture probability, overestimates their abundance and yields unrealistically narrow confidence intervals.

## Key Findings

### Field Results (West Indian Creek, Brown Trout)

- **Sample sizes:** 418 fish marked and released (M). Of 485 fish captured in the second sample (C), 198 were recaptured (R). Total lengths ranged from 101 to 395 mm.
- **Chapman-Petersen estimates:** Because equal catchability was violated, data were split into up to 14 length-groups. Estimates varied erratically with group number, ranging roughly from 918 to 1,459 fish, with variances from about 3,000 to 16,500. Estimates approached the spline-bootstrap value as the number of groups increased.
- **Batch-mark smoothing spline (Mt, first-sample capture):** Capture probability rose sigmoidally with size. Deviance = 191.8. The null model P = 0.41 had deviance 222.5. The change in deviance was 30.7 (P < 0.001), and the bootstrap goodness-of-fit test also gave P < 0.001, confirming size dependence. The population estimate was **N̂ = 1,137**, with bootstrap variance 8,882 and a skewed percentile confidence interval (skewness and kurtosis both significant). The 95% interval is reported in the source, but its digits are unreadable in the OCR text.
- **Parametric logistic model (batch mark):** N̂ = 1,236, variance 4,187. The fitted curve resembled the spline curve, so the logistic model was judged a reasonable choice.
- **Individually marked (longitudinal) spline:** The second-sample capture function sat slightly higher than the first-sample function and did not level off at the largest sizes. Deviance = 348.32. The null model P = 0.50 had deviance 335.35. The change in deviance was 27.6 (P < 0.001). The estimate was N̂ = 1,139, and the model Mt estimate was **1,138**. Model Mt fitted significantly better than Mo (P < 0.001; 95% CI 1,030-1,279).
- **Logistic model (longitudinal):** Its curve was more sharply sigmoidal, with a lower upper asymptote than the spline, so it was judged a poor fit. N̂ = 1,188, variance 10,747.
- **Depletion model (Mh):** The depletion-based capture curve was lower than the batch-mark spline. Estimates for fish shorter than 130 mm were implausibly low, meaning the second pass was more efficient than the first. The depletion model was judged inappropriate, and no total-population estimate was made.
- **Precision:** The coefficient of variation of the weighting factors (1/P(z)) showed reasonable precision for all but the smallest fish. Length-frequency correction shifted the observed distribution toward the estimated true one (Figure 2).

### Simulation Results

- **Design:** Populations of N = 124, 250, 500 and 1,000 were built from two equal-sized age groups: age-1 (mean 140 mm, SD 20) and age-2 (mean 240 mm, SD 30). Capture probability followed a three-parameter logistic function. Each population size had 100 simulations. Estimates were kept only when a size-group had at least four recaptures (Ricker 1975) and all P(z) > 0.02.
- **Small-sample limits:** Most samples were adequate for age-2 estimates. Far fewer were adequate for age-1, especially at N = 124 (226 usable samples) and N = 250 (467 usable samples).
- **Age-1 fish:** The spline-based estimate had less negative bias than Chapman-Petersen, a wider dispersion, better coverage and similar RMSE. The parametric model had the least bias (usually positive) but the widest dispersion, a strongly biased SE, poor coverage and the highest RMSE.
- **Age-2 fish:** Each method had smaller bias and RMSE. Chapman-Petersen underestimated SE(N̂) and had slightly low coverage. Spline model Mt and the parametric model overestimated SE(N̂), the parametric model greatly so, and both had high coverage.
- **Total population:** Spline bias and SE generally fell between those of the other methods. The spline model Mt had the best coverage at all population sizes, with relatively low RMSE. The parametric model yielded lower RMSE for age-2 fish at N ≥ 124 and for totals at N ≥ 4,000 (additional simulations at 8,000). Parametric coverage was 95-97% for age-2 fish.
- **Bias correction:** The difference between the mean bootstrap estimate and the original estimate was weakly negatively correlated with the actual error for age-1 and total estimates. Using it to correct bias would make the error worse.

### Methodological Conclusions

- The spline approach identifies the form of size selectivity well and reduces bias in N̂ and in length distributions. Its assumptions match those of the Chapman-Petersen method, except that capture probability is a smooth function of size rather than a constant.
- Key assumptions: a closed population; capture probability is a smooth function of size; fish of the same size mix randomly between samples or have equal capture probability; marking does not affect later capture; marks are not lost; and all marks and sizes are reported.
- Bootstrapping is the preferred route for confidence intervals on the spline and, even for parametric models, because delta-method SEs were often strongly biased and the distribution of N̂ was non-normal.
- Splines can develop multiple peaks and valleys when capture probabilities are low. Maximum-likelihood methods generally perform poorly when capture probabilities fall below about 0.1 (Otis et al. 1978).
- Although the spline is computationally simple, bootstrapped confidence bounds are intensive. For the parameter range simulated, a single parametric model offered few advantages over the spline, but a parametric model may be preferable when capture probability is uniformly low and an appropriate form is known.

### Management Recommendations

- Record the length of every fish in each sample. Without size data, size-based analysis is impossible.
- Size-correction can yield good abundance estimates for small fish that are often excluded from analyses.
- Document capture probabilities of large fish carefully, since they are the most difficult to estimate and often the target of management.
- Use the spline to guide the choice of length-groups and parametric forms, and plot smoothed functions for different smoothing parameters to show the bias-variance compromise.
- Future work: extend [[Otis Model Family]] and Miller (1988) models to include size-selective functions in multiple-occasion designs, potentially using multivariate splines.