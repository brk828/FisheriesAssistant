---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [fisheries-science, population-dynamics, mortality-estimation, virtual-population-analysis]
title: "Errors in estimates of mortality obtained from virtual populations"
source_id: "17651"
minckley_id: "17651"
source_citation: "Y. M. M. Bishop (1959). Errors in estimates of mortality obtained from virtual populations. Journal of the Fisheries Research Board of Canada 16(1): 73-90. Minckley Library ID: 17651."
source_file: "17651.pdf"
text_extraction: "ocr"
---
# Errors in Estimates of Mortality Obtained from Virtual Populations

#ichthyology #marine-biology #fisheries-population-dynamics

## Executive Summary

This methodological paper by Yvonne M. M. Bishop (Inter-American Tropical Tuna Commission, La Jolla, California; published 1959 in the *Journal of the Fisheries Research Board of Canada*, vol. 16, no. 1) analyses the bias in individual estimates of the natural mortality coefficient (M) derived from [[Virtual Population Analysis]]. The author shows algebraically that this bias is unchanged whether one or several year-classes are used, provided mortality coefficients are constant across exploitable fish. Using graphical families of curves for M = -0.2 and M = -0.4 and fishing mortality (F) from 0 to -2.0, the paper concludes that the method generally underestimates natural mortality and overestimates the fishing mortality coefficient (c), with the exception of periods of gradual decline in fishing effort.

## Background & Description

Virtual populations estimate total mortality, and hence survival, of a fish stock from the annual catch of each age-group and relative annual fishing effort. The method was championed by [[Fry 1957]], who argued that it needs no iteration to correct for changes in effort and is insensitive to drift in fish vulnerability. Fry compared his results with those of [[Beverton 1954]], who used an iterative method on [[Opeongo Lake Trout]] data spanning ten years of fluctuating effort (from 22.4 down to 5.7, then up to 17.4 hundred boat-hours).

Fry's estimates were c = -0.0262 and M = -0.0818, against Beverton's c = 0.0260 and M = -0.1000. The difference in M was small in this case, though consistent with a low intercept predicted at a 1957 ICES/FAO/ICNAF workshop in Lisbon, which concluded that varying fishing mortality with constant natural mortality tends to exaggerate total mortality change and bias the intercept of M low.

The paper defines the framework: fishing mortality is F_r = c·f_r (with f_r a measure of effort), M and F are negative by Fry's convention, and vulnerability is assumed age-independent for fish of age a or older. Each virtual population is the sum of fish of a year-class still to be caught, and the estimator log(z_r) is taken as an estimate of M + F_r, where z_r is the inverse ratio of successive virtual populations.

## Ecological & Environmental Context

The analysis is theoretical and applies to any exploited population whose mortality can be modelled as constant natural mortality plus variable fishing mortality. The paper's examples are a [[Lake Trout]] fishery and [[Fishing Effort]] histories affected by wartime curtailment. The author notes that the method is independent of recruitment size (R) for each year-class, and that changes in stock vulnerability act like errors in the effort index (f_r).

The key ecological driver of bias is the relative size of fishing mortality to natural mortality. Bias grows when fishing mortality is low compared with natural mortality, and when fishing effort fluctuates strongly. Higher natural mortality also increases the bias of individual estimates.

## Key Findings

- **Bias is invariant to year-class number:** Using multiple year-classes reduces random error but does not change the bias, which equals the logarithm term in equation (4) of the paper.
- **Direction of error:** With effort stable or increasing, the regression intercept underestimates M and the slope overestimates c. A declining effort period reverses these errors.
- **Maximum bias conditions:** Bias is largest with large effort fluctuations, low F relative to M, and higher M.
- **Increasing effort:** Gradual or abrupt increases yield underestimates of M. The steady-state case (a) always underestimates M, with error increasing with |D|.
- **Decreasing effort:** A sudden drop followed by cessation (case b) gives overestimates of M that can be much larger than possible underestimates. The paper states that a great decrease in effort in the third year gives a far larger E than a violent increase.
- **Effect of M:** For M between -0.2 and -0.4, the steady-state error E rises slightly with M, particularly at low F; for the sudden-drop case, E falls as M increases across the F range 0 to 2.0.
- **Regression behaviour:** Even if c is known, the mean of individual M_r estimates is probably an underestimate of M, because errors are larger at small |F|.
- **Fry's example:** His greatest deviations from the regression occurred when fishing trends were changing. Gradual decline followed by gradual increase can yield a close estimate of M and an accurate c, as Fry obtained.
- **General conclusion:** The virtual population method generally underestimates natural mortality and overestimates the fishing mortality coefficient, except during gradual declines in effort.
- **Stock vulnerability:** Changes in vulnerability produce the same effect as errors in the effort index f_r, and the method remains independent of recruitment size.