---
species: ["Salmo salar", "Salmo trutta", "Oncorhynchus kisutch", "Micropterus dolomieu"]
common_name: ["Atlantic Salmon", "Brown Trout", "Coho Salmon", "Smallmouth Bass"]
family: ["Salmonidae", "Centrarchidae"]
habitat: "Freshwater streams (shallow, wadeable and deeper stream sections)"
ocean_basin: "N/A"
location: "Michigan, USA (publisher); small streams in northern Norway; streams in Wisconsin, USA"
tags: ["fisheries-methods", "population-estimation", "mark-and-recapture", "depletion-sampling", "electrofishing"]
title: "Stream Fish Population Estimates by Mark-and-Recapture and Depletion Methods"
source_id: "PML1374"
marsh_id: "PML1374"
library: "Marsh Library"
permission: "public domain"
source_citation: "R. N. Lockwood, J. C. Schneider (2000). Stream Fish Population Estimates by Mark-and-Recapture and Depletion Methods. Michigan Department of Natural Resources, Fisheries Special Report 25 (Manual of Fisheries Survey Methods II, Chapter 7). Marsh Library ID: PML1374."
source_file: "Lockwood R.N. 2000. Stream fish population estimates by mark recapture and depletion methods.pdf"
text_extraction: "mixed"
---
# Stream Fish Population Estimates by Mark-and-Recapture and Depletion Methods

#ichthyology #marine-biology #salmonidae

## Executive Summary

This chapter from the [[Manual of Fisheries Survey Methods II]] (Michigan Department of Natural Resources, Fisheries Special Report 25, January 2000) explains how to estimate the total number of fish in a discrete stream section by subsampling. It covers two approaches: [[Mark-and-Recapture Method]] and [[Depletion Method]]. Both rely on capturing a portion of the population, typically with [[Electrofishing]] gear. The chapter gives the governing assumptions, the step-by-step field procedures, the core equations with worked examples, and guidance on checking assumptions and choosing methods. It was originally written in 1976 by G. P. Cooper and J. R. Ryckman and rewritten in 1998 by Roger N. Lockwood and James C. Schneider.

## Background & Description

The chapter is a technical methods manual rather than a research study. It provides no new field dataset. Its numerical content consists of worked examples with hypothetical catch numbers, plus statistical tables.

Population estimation in this chapter has three main components:

- **Mark-and-recapture estimates** (Section 7.1), recommended over depletion when conditions allow. The [[Chapman-Petersen Estimator]] is the preferred form because it gives a statistically unbiased estimate for finite inland populations. The [[Bailey Modification]] is similar and also in use.
- **Depletion estimates** (Section 7.2), also called the [[Zippin Method]]. These use either [[Two-Pass Depletion]] or [[Multiple-Pass Depletion]] removal sequences.
- **Statistical support**, including [[Poisson Distribution]] confidence coefficients (Table 7.1), Student's *t* values, and chi-square percentiles (Table 7.2).

Estimates are calculated separately for each species and size group to account for [[Gear Selectivity]], then summed to a total. Variances are combined the same way.

The example species named in the text are [[Atlantic Salmon]] (*Salmo salar*), [[Brown Trout]] (*Salmo trutta*), [[Coho Salmon]] (*Oncorhynchus kisutch*), and [[Smallmouth Bass]] (*Micropterus dolomieu*). Trout in inch groups 8, 9, and 10+ are used as a worked example of combining estimates.

## Ecological & Environmental Context

**Suitable conditions.** Both methods suit shallow, wadeable streams that can be thoroughly sampled with electrofishing. Mark-and-recapture can also be used in deeper streams sampled from a boat, provided that all targeted fish are vulnerable to capture (either all stream parts are sampled, or marked fish mix randomly with unmarked fish).

**Choosing a method.**
- Depletion suits very small streams, where all sampling can be completed within about one day and the population is small (roughly fewer than 2,000 individuals).
- If fish are likely to migrate into or out of the study section within about one week, depletion is preferred because its sampling period is shorter.

**Movement and mixing.** Emigration and immigration must be negligible during sampling. Blocking nets greatly reduce fish movement on small streams. Where nets are impractical, sampling longer sections reduces the effect of movement. Marked fish should have at least one day to recover and mix before recapture. If more than one pass is made per day, marked fish may not have mixed, which violates the mark-and-recapture assumptions.

**Behavioural effects of shocking.** Capture probability can change after electrofishing:
- In two small Norwegian streams, [[Heggberget and Hesthagen 1979]] estimated young Atlantic Salmon and Brown Trout populations with two-pass depletion. They suggested populations were underestimated by as much as 50% because fish avoided the electrical current on the second pass.
- [[Peterson and Cederholm 1984]] found that for shocked juvenile Coho Salmon in small streams, capture probability was similar to earlier capture rates after a minimum recovery time of one hour.

**Species-specific limits.** Smallmouth Bass are difficult to recapture, and [[Lyons and Kanehl 1993]] (Wisconsin streams) concluded that mark-and-recapture methods are not recommended for them.

**Where assumptions are most suspect.** Depletion assumptions are weakest in large streams (which have more refuges) and for large, agile or wary fish. The chapter therefore recommends designing sampling so that mark-and-recapture estimates remain possible while depletion sampling is under way.

**Software.** [[CAPTURE Software]] (White et al. 1982) is available from the Institute for Fisheries Research. It handles cases where capture probabilities differ between passes.

## Key Findings

**1. Mark-and-recapture is generally preferred.** The chapter states it has been shown to be unbiased when more than 50% of a population is marked (Jensen 1992; the source OCR is garbled here). Its five conditions are:
1. Marked and unmarked fish have the same mortality rates.
2. They are equally vulnerable to capture.
3. Marks are retained and all recaptured marks are recognized.
4. Marked fish mix randomly with unmarked fish.
5. Emigration and immigration are negligible during recapture.

**2. Chapman-Petersen procedure and variance.** The chapter recommends the Chapman modification of the Petersen equation (Ricker 1975). For variance of a single estimate, binomial charts or the Poisson-based limits in Table 7.1 are preferred over the standard variance formula. Those limits are asymmetrical, and 68% limits (one standard error) may be adequate for management, while 95% limits suit research. Ricker (1975) states that bias can be ignored if there are 34 or more recaptures. Where needed, data from adjacent size groups should be pooled to reach that number.

**3. Worked mark-and-recapture example (Example 7.1).** With 100 fish marked, 80 in the second sample, and 10 recaptures:
- N = 744 fish; standard error = 200 (68% limits).
- Approximate 95% limits (N ± 2 SE): 344 to 1,144.
- Ricker-based 95% limits (R = 5.42 and 18.42): 421 to 1,274.

The source concludes "421 to 1,271" in one place and "1,274" in the calculation. The discrepancy appears in the source text and is reported here as printed. The chapter also notes that these limits reflect random error only, and that systematic errors such as avoidance of recapture by marked fish are unknown.

**4. Combining size-group estimates (Example 7.2).** Inch group 8 (N = 357, variance 20,392), group 9 (N = 293, variance 12,100), and group 10+ (N = 153, variance 3,935) give:
- Total N = 803 trout.
- Combined variance = 36,427; standard error = 191.
- Approximate 95% limits: 421 to 1,185.

**5. Two-pass depletion.** Estimates are unbiased when capture probability p > 0.80 and unreliable when p < 0.20 (fewer than 20% of the population caught per pass). In Example 7.3 (200 fish on pass one, 95 on pass two): p = 0.525, N = 381, variance = 876, standard error = 30, and approximate 95% limits of 321 to 441.

**6. Multiple-pass depletion.** This requires three or more passes and assumes constant catchability across passes. It is solved iteratively, using a maximum likelihood estimate and spreadsheet setup. In Example 7.4 (catches of 300, 130, and 69; total 499), the estimate is N = 546, p = 0.5496, standard error = 11.7, and approximate 95% limits of 523 to 569.

**7. Testing equal capture probability.**
- *Plotting method:* with more than two passes, plot each catch against the sum of previous catches (Seber and Le Cren 1967).
- *Chi-square test:* in Example 7.7, χ² = 1.234 with df = 1, against a critical value of 3.841 at 95% certainty. The difference in capture probability is therefore not significant, and the multiple-pass equations are appropriate.
- *Comparison with mark-recapture:* in Example 7.5, a mark-recapture estimate and a depletion estimate can agree when the two passes have equal catch probabilities. Example 7.5 (120 marked, then 60 marked and 60 unmarked) gives 240 by both methods. The chapter also warns that depletion analysis is only valid when one or more days separate passes.

**8. Bias from unequal catchability.** If marked fish are easier to catch on the second pass, the population is underestimated. If they are harder to catch, it is overestimated.

**9. Recommended practice.** Keep effort constant across passes. Stratify estimates by species and size group. Use blocking nets or longer sections where movement is likely. For severe variation in capture probability, use the more intensive methods of [[Schnute 1983]] or White et al. (1982).

**Reference list.** The chapter cites 12 references, including Ricker (1975), Seber and Le Cren (1967), Zippin (1958), Carle and Strub (1978), Jensen (1992), Snedecor and Cochran (1991), and Schnute (1983).