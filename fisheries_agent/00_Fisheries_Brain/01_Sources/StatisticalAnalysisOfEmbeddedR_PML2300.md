---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Pacific coast of North America (CWT salmon data context); author affiliation Nanaimo, B.C., Canada
tags: [mark-recovery, coded-wire-tag, embedded-replicates, statistics, salmon, fisheries-science]
title: "Statistical Analysis of Embedded Replicates in Mark-Recovery Experiments"
source_id: "PML2300"
marsh_id: "PML2300"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. T. Schnute (1992). Statistical Analysis of Embedded Replicates in Mark-Recovery Experiments. Canadian Journal of Fisheries and Aquatic Sciences, 49: 432-442. Marsh Library ID: PML2300."
source_file: "Schnute J.T. 1999. Statistical analysis of embedded replicates in mark recovery experiments.pdf"
text_extraction: "text"
---
# Statistical Analysis of Embedded Replicates in Mark-Recovery Experiments

#ichthyology #marine-biology #salmonidae

## Executive Summary

This methodological paper by [[Jon T Schnute]] (Department of Fisheries and Oceans, Pacific Biological Station, Nanaimo, B.C.; published in the *Canadian Journal of Fisheries and Aquatic Sciences*, 1992, vol. 49, pp. 432–442) examines whether **embedded replicate** codes can improve variance estimation in [[Coded Wire Tag]] (CWT) experiments on juvenile Pacific salmon. Embedded replicates are several random subgroups created when a single roll of CWT wire carries multiple repeated codes. The author argues that these subgroups provide no information beyond treating the marked group as one unit, and that using them for variance estimation can be misleading. The paper supports this with intuitive arguments and analytic proofs for two cases, then reviews alternative methods for quantifying uncertainty in recovery and contribution estimates.

## Background & Description

- **Tagging technology:** Since the early 1970s, CWTs have been used extensively to mark juvenile Pacific salmon. Each tag is a stainless steel segment with an etched binary code, cut sequentially from a wire spool and inserted into the nose cartilage of juveniles. The adipose fin is removed as a visual marker, so fish with missing adipose fins can be scanned for tags at recovery.
- **Uses of CWT data:** Information supports hatchery operations, fishery management and scientific research. Hatchery managers can assess juvenile survival to adulthood, and fishery managers can assess the impact of hatchery fish on a given fishery.
- **Data sources:** [[Kuhn et al. 1988]] and [[Lapi et al. 1990]] review CWT data collected on the North American Pacific coast.
- **Embedded replicates:** Some Pacific coast agencies began using special rolls with several codes embedded repetitively. Marked fish then form equal groups, each with a distinct tag, and random selection for marking makes each group a random sample of the whole.
- **Worked example:** A baseline calculation assumes a 1-in-10 marking rate and a 1-in-4 sampling rate, giving a total expansion factor of 40 per marked fish. Seven tags recovered from a 25% fishery sample yield an estimate of 280 hatchery fish. Splitting the marked fish into two embedded groups gives two estimates (320 and 240) with a mean of 280.
- **Problem context:** Variance is harder to measure than the point estimate because sampling may be stratified and measurement errors, such as lost or misread tags, can enter the data. Only one estimate is available from a single-code experiment, while several are needed to measure variance.

## Ecological & Environmental Context

The paper is a statistical treatment of mark-recovery data rather than an ecological field study, so it contains no species population data beyond juvenile Pacific salmon as the tagged organism. Relevant contextual points include:

- Marked fish are recovered in commercial fisheries, so recovery probabilities depend on fishery sampling, catch and selectivity.
- The analysis assumes the fishery is not selective between marked and unmarked fish.
- Fish clustering behaviour could create correlations among recoveries, which affects model adequacy.
- The paper cites [[Bilton et al. 1982]], a study on coho salmon (*Oncorhynchus kisutch*) showing how time and size at release affect adult returns, to illustrate the value of replicated ponds in measuring hatchery practices.
- Related CWT studies cited include [[Clark and Bernard 1987]] (microwire tag recovery from southeast Alaska salmon catches), [[Geiger 1990]] (parametric bootstrap intervals), [[Newman 1990]] (variance estimation from sample recoveries) and [[Penny et al. 1990]] (comparing replication methods).

## Key Findings

**1. Embedded replicates add no useful information.** The author contends that embedded replicate groups provide nothing beyond treating marked fish as a single group. Variance estimates from replicate-based calculations can be deceptive.

**2. Replicates are not true replicates.** Embedded groups are not repeated, independent experiments under the same controls. They are random subdivisions of one population exposed to identical conditions, so standard calculations may be inappropriate. The author compares them to interpenetrating subsamples: a nonrandom result cannot be attributed to a known source.

**3. Only two outcomes are possible.** Either the embedded codes are distributed randomly among recoveries, which only confirms the laws of chance, or they are not, which reveals a departure from randomness the experiment cannot explain. The analysis is therefore uninformative either way.

**4. Simulation argument.** A computer simulation can generate the same statistical results using one code and then assign embedded codes randomly to marked recoveries afterward. Extra data from embedded replication are therefore redundant.

**5. Replicates cannot detect all variability.** Example: if 100 marked fish are caught by five boats, an even split of 20 per boat indicates low variability, whereas one boat catching 100 indicates high variability. Embedded codes, applied at release, cannot reveal such recovery-phase variation.

**6. Binomial case (Section 2).** For M marked fish released and N recovered with recovery probability p, the two-code experiment has a likelihood equal to the one-code binomial likelihood multiplied by a hypergeometric factor independent of p. The totals M and N are sufficient for p. The result proves that assigning codes before release or after recovery gives identical statistics. If the two groups have different recovery probabilities, the model is inappropriate for clustering behaviour and tests of model adequacy using embedded codes are not valid.

**7. Sampled catch case (Section 3).** For X marked fish recovered in a sample S from a catch C, the one-code likelihood is a compound binomial-hypergeometric distribution. With two embedded codes, the likelihood factors into the total-recovery likelihood times a conditional binomial (X₁ given X, with probability ½ each). The total X is sufficient for M, so embedded codes add nothing.

**8. Inference methods reviewed (Section 4).** The paper frames two questions: (1) estimating the recovery probability p from M released and N recovered fish, and (2) estimating the total hatchery contribution M from X recovered fish in a sample. Methods compared are:
- **Analytic variance (AV):** standard error from closed-form moments, giving approximate confidence intervals.
- **Exact interval (EI):** based on F-distribution limits for question 1.
- **Likelihood variance (LV) and likelihood interval (LI):** based on the likelihood function and a chi-square cutoff, with asymptotic normality of the estimate.
- **Approximate AV (AAV) and approximate LI (ALI):** simplified variants using binomial approximations.

**9. Empirical comparison (Section 5).** Six illustrative examples were analysed (1a–1c for question 1, 2a–2c for question 2). All methods gave similar point estimates and, when standardised to 95% intervals, similar widths. Some intervals were asymmetric, especially for LI. For example 2a (the 280-fish case), LI and ALI intervals were close to each other. Where estimates exceeded the total catch constraint, the upper limit was truncated at the catch size (400 in the examples), and a one-sided form of the interval was used.

**10. Conclusions.** The author concludes that embedded replication, though mechanically feasible, should not be adopted as a valid CWT technique until its proponents articulate clear statistical models for analysing the data. Uncertainty should instead be assessed with the methods described above, such as AV, EI, LV and LI.

**Acknowledgements and references:** The work benefited from discussion within the International Working Group on Mark Recovery Statistics, organised by the [[Pacific Salmon Commission]]. The reference list includes classic statistics texts (Abramowitz and Stegun 1966; Mood and Graybill 1963; Kendall and Stuart 1979; Pollard 1977), the Nelder and Mead (1965) simplex method, and Schnute's own removal-method paper (1983).