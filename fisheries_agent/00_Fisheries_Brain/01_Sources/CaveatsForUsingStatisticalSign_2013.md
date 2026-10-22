---
species: ["N/A"]
target_species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: "N/A"
ocean_basin: "N/A"
location: "N/A"
tags: ["scientometrics", "statistical_inference", "research_assessment", "citation_analysis", "null_hypothesis_significance_testing"]
analytical_category: ["critique of statistical methods", "research assessment methodology", "citation indicator normalization"]
model_framework: "Null Hypothesis Significance Testing (NHST); frequentist inference; confidence intervals; effect size estimation"
software_environment: ["Not reported"]
data_requirements: ["probability samples or random assignment", "well-defined populations", "independence of observations", "plausible null hypotheses"]
key_assumptions: ["randomness (random sampling or random assignment)", "null hypothesis is true in the population", "independence of observations", "correct statistical model for confidence interval construction"]
keywords_stubs: ["#NHST", "#p_values", "#effect_size", "#confidence_intervals", "#statistical_power", "#Type_I_error", "#Type_II_error", "#citation_normalization", "#research_evaluation"]
title: "Caveats for using statistical significance tests in research assessments"
source_id: "X-339a9a30"
doc_type: "analyses_and_modeling"
source_citation: "J. W. Schneider (2013). Caveats for using statistical significance tests in research assessments. Journal of Informetrics 7(1): 50-62."
doi: "10.1016/j.joi.2012.08.005"
source_file: "Statistical significance review 2010.pdf"
text_extraction: "text"
---
# Caveats for using statistical significance tests in research assessments

#scientometrics #statistical_methods

## Analytical Objective & Scope

**Core Problem Addressed**: This article critiques the use of statistical significance tests (specifically Null Hypothesis Significance Tests, NHST) in research assessments based on citation indicators, responding to proposals by [[Opthof and Leydesdorff]] (2010) that advocate for normalization procedures enabling significance testing. The author argues that NHST are "highly problematic and detrimental to critical thinking" when applied to research evaluation.

**Methodological Classification**: Critical methodological review and conceptual analysis. This is not a novel method development but rather a systematic critique of existing statistical practices, drawing on decades of criticism from psychology, sociology, economics, medicine, epidemiology, and statistics. The article demonstrates flaws in the application of NHST to citation indicators through examination of published examples, particularly from [[Opthof and Leydesdorff]] (2010) and related scientometric literature.

## Mathematical & Statistical Framework

**Model Formulation**: The article addresses the standard NHST framework without proposing alternative equations. Key statistical concepts discussed include:

- **p value definition**: p(Data | H₀) = probability of observed data plus more extreme data across all possible random samples, given the null hypothesis H₀ is true, randomness, sample size n, and all test assumptions are satisfied
- **Statistical power**: 1 - β, where β is the probability of Type II error; power is a function of significance level α, sample size n, effect size, and the relationship: each is a function of the other three
- **Confidence intervals**: Under repeated realizations, a 95% CI would cover the true parameter 95% of the time (frequentist interpretation); a 68% CI corresponds roughly to ±1 standard error
- **Effect size measures**: Standardized (e.g., Cohen's d, r, R²) and unstandardized measures; Cohen's d benchmarks: "small" ≈ 0.20, "medium" ≈ 0.50, "large" ≈ 0.80

**Variables & Covariates**: The article discusses citation indicators as response variables, specifically:
- Relative citation impact scores (e.g., 0.91 ± 0.11 in [[Opthof and Leydesdorff]] example)
- Journal impact factors (example: 0.611 vs. 0.913, yielding w statistic = 1.98)
- Field-normalized citation scores using sum of ratios vs. ratio of sums approaches
- Spearman rank correlations (n=7, p=0.052 example)
- Kruskal-Wallis tests with Bonferroni corrections at 5% significance level

**Fit Diagnostics & Metrics**: The article critiques rather than endorses specific metrics. Examples of problematic applications include:
- Arbitrary significance levels (α = 0.05, 0.01)
- Dichotomous decisions based on whether p < α
- Use of standard errors as surrogates for significance tests (checking if CI subsumes null value)
- Correlation coefficients tested at 1% and 5% levels
- F statistics and t statistics evaluated for "significance"
- Example: citation count differences (108.82, 95.26, 37.08) with F test p = 0.09 treated as "not significant"

The article emphasizes that convergence and model assumptions (randomness, independence, correct distributional forms) are rarely verified in practice.

## Data Requirements & Preprocessing

**Input Data Schema**: The article argues that valid NHST requires:

- **Probability samples**: Random sampling from well-defined finite populations with known nonzero selection probabilities, OR random assignment to treatment/control groups
- **Sample size considerations**: Must be adequate for statistical power; underpowered studies fail to detect important effects, overpowered studies detect trivial effects as "significant"
- **Independence**: Observations must be independent; lack of independence yields incorrect standard errors and misleading p values
- **Well-defined populations**: Not "imaginary super-populations" or convenience samples
- **Minimal bias**: Even well-designed probability samples are imperfect; bibliometric data are "selective, packed with potential errors" affecting document matching

**Problematic data types identified**:
- **Convenience samples**: Most observational studies; bias expected, independence problematic, NHST becomes "category mistake"
- **Apparent populations**: All available observations (e.g., all 65 publications for one PI, 1997-2006); no sampling error exists, parameters are known, NHST is meaningless
- **"Super-populations"**: Imaginary populations defined circularly as "the population from which data would have come if data were a random sample"; inferences to imaginary populations are imaginary

**Example from [[Opthof and Leydesdorff]]**: 232 scholars at [[Academic Medical Centre]] (AMC); 65 publications for one principal investigator. The article questions: (a) Are these probability samples? (b) How are populations defined? Likely these constitute apparent populations or convenience samples indexed in specific databases, not random draws.

**Sampling Cross-References**: #probability_sampling #random_assignment #convenience_samples #apparent_populations #super_populations #bibliometric_data_quality #measurement_error

## Code Logic

Not reported. The article is a conceptual and methodological critique; no code, pseudocode, or computational algorithms are provided. Statistical formulas are presented in standard mathematical notation (e.g., p(Data | H₀), 1 - β) but no implementation details are given.

## Biological & Management Synthesis

**Model-to-Decision Mapping**: The article argues that NHST should NOT be used to map citation indicators to research assessment decisions. Key points:

**Flawed decision process identified**:
1. **Dichotomous decisions**: Treating "significant" vs. "not significant" as binary criterion for importance is uninformed and arbitrary
2. **Conflation of statistical and substantive significance**: "Statistically significant" does not mean "important"; 90% of management research papers fail to distinguish these concepts
3. **Mechanical ritual**: Researchers rely on NHST to avoid "hard thinking about differences that make a difference"
4. **Neglect of effect sizes**: Statistical significance is a function of sample size and effect magnitude; identical p values can arise from large effect/small n or small effect/large n
5. **Implausible null hypotheses**: Nil null hypotheses (exactly zero difference) are almost always false in observational studies; rejecting them is "unimpressive and uninformative"

**Example consequences**:
- Journal impact factors 0.611 vs. 0.913 (w = 1.98, p < 0.05): Declared "significantly different" but effect size d ≈ 0.24 (small), CI: -0.01 to 0.48 (zero to medium effect). Is this important? Depends on context.
- AMC researcher citation score 0.91 ± 0.11: Declared "not significantly different" from world average of 1.0 because CI includes 1.0. But this is likely Type II error due to low power (small sample, Bonferroni correction).
- Citation counts by academic origin (108.82, 95.26, 37.08, p = 0.09): Authors conclude no difference exists, but p = 0.09 does not mean null hypothesis is true; may be underpowered study.

**Recommended decision framework**:
1. **Informed human judgment**: Decisions about importance must be subjective, context-dependent, goal-oriented
2. **Effect size estimation**: Calculate and interpret effect sizes with confidence intervals
3. **Prior knowledge**: Relate results to empirical findings and theoretical insights
4. **Context-specific thresholds**: No universal standard; each case judged on merits
5. **Costs and benefits**: Consider consequences of assessment decisions
6. **Uncertainty acknowledgment**: Accept that measurements are imprecise; sharp thresholds (p = 0.049 vs. 0.051) are absurd

**Alternatives to NHST**:
- **Confidence intervals and standard errors**: More informative than p values but still require randomness assumptions and frequentist interpretation
- **Resampling techniques** (bootstrap, jackknife): Useful for interval estimation and sensitivity analyses (e.g., [[Leiden Ranking]] "stability intervals") but do not fix problems with non-random, biased, or small samples; not substitute for external replication
- **Exploratory data analysis**: Box-whisker plots, descriptive statistics
- **Bayesian inference**: Assesses degree of support data provide for hypotheses; yields p(H₀ | Data) rather than p(Data | H₀)
- **Model-based inference** (information theory, AIC)
- **Likelihood inference**

**Best practices for research assessment**:
1. Statistical inference only valid with probability samples or random assignment
2. Formulate research aims as "how much?" or "to what extent?" (estimation framework)
3. Base interpretation on point and interval estimates, not dichotomous significance
4. Calculate effect sizes and confidence intervals; interpret via informed judgment
5. If NHST used: report power, ensure null hypothesis is plausible
6. Report effect sizes and CIs for all effects, whether "significant" or not
7. Report exact p values, not just p < 0.05
8. Never describe results solely in terms of statistical significance
9. Use "significant" without "statistically" only for truly noteworthy results
10. Explain why results have substantive significance; statistical tests inadequate for this
11. Replication is best way to address sampling error

**Ethical concerns**: Research assessments affect funding, promotion, hiring, firing. Basing such decisions on a "mechanical tool known to be deeply controversial" is problematic. The "null ritual" creates cognitive illusion that assumptions have "elapsed" from researchers' minds, and results are treated as objective decision statements about importance when they are not.