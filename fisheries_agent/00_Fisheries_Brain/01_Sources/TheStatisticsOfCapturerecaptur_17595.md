---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [capture-recapture, population-estimation, statistics, fisheries-science, review]
title: "The statistics of capture-recapture methods"
source_id: "17595"
minckley_id: "17595"
source_citation: "R. M. Cormack (1968). The statistics of capture-recapture methods. In: Oceanography and Marine Biology: an annual review, Vol. 6, (H. Barnes, A. Ansell and R. Gibson, eds). London:George Allen and Unwin Ltd. , 455-506. Minckley Library ID: 17595."
source_file: "17595.pdf"
text_extraction: "ocr"
---
# The Statistics of Capture-Recapture Methods

#ichthyology #marine-biology #fisheries-statistics

## Executive Summary

This review by R. M. Cormack (University of Edinburgh), published in the *Oceanography and Marine Biology: An Annual Review* (1968, vol. 6), surveys the statistical theory behind [[Capture-Recapture Methods]] for estimating animal population size, survival, mortality, and migration. It is primarily a historical and unifying survey that adopts one consistent notation across the field. It covers closed-population models (single and multiple marking), deterministic and stochastic open-population models including the [[Jolly-Seber Method]], commercially exploited fish populations, and tests of basic assumptions. Cormack's central message is that statistical refinement cannot compensate for violated biological assumptions: "an approximately right answer is always preferred to a highly precise but wrong answer." Fish examples (salmon, plaice, sardines, pond fish) are used throughout to illustrate both successes and failures.

## Background & Description

The document opens with historical anecdotes: [[Izaak Walton]] (1653) recorded [[Francis Bacon]]'s salmon marking with ribands, and Beverton and Holt (1957) stated the purpose of marking experiments. Marking methods yield two kinds of information: recovery of marked individuals alone (useful for mortality, migration, and movement), and comparison of marked with unmarked individuals captured at the same time (which allows population size to be estimated).

Key historical contributors include:
- [[Laplace]] (1786), the first recorded use, estimating the population of France from birth registrations.
- [[Petersen]] (1896), who proposed the proportion-of-marks approach for fish; Dahl (1919) first applied it.
- [[Lincoln Index]] (Lincoln, 1930), based on waterfowl band returns, though Le Cren (1965) argues for the name "Petersen estimate."
- Chapman, Bailey, Jackson, Leslie, Darroch, Jolly and Seber, who developed the main models.

Cormack reports that the subject has been developed in several fields with "a mass of different and inconsistent notation." Table I in the source compares symbols across Bailey, Chapman, Darroch, Jolly, Leslie and Seber; the table itself is not reproduced here. The review is organised by population type: closed populations (single and multiple marking), deterministic models allowing for mortality, stochastic models, commercially exploited populations, and tests of assumptions.

## Ecological & Environmental Context

The review frames capture-recapture as applicable across animal groups. Examples include:
- **Fish:** salmon, sockeye and coho salmon, plaice, pond fish, sardines, whelks (a commercial shellfish).
- **Insects:** ants, flies, locusts, larval stages with moulting.
- **Birds:** wildfowl, shearwaters, blue tits, [[Fulmar]] (*Fulmarus glacialis*).
- **Mammals:** small mammals, mice.
- **Amphibians:** frogs.

Two classes of population are distinguished. A **closed population** is one where birth, death, immigration, and emigration are negligible over the study period. An **open population** is subject to these processes, which must be included in the model. Fisheries workers face additional complications: marking often involves removing fish from their environment, and commercial recovery of tags is incomplete.

Typical violations of assumptions include:
- Loss of marks or non-reporting of recovered marks (for example, Clark and Janssen's sardine plant experiment, where reporting depended on rewards).
- Additional mortality caused by marking.
- Unequal vulnerability to capture, such as homing behaviour, schooling, or trap-shyness.
- Lack of random mixing of marked and unmarked animals.

## Key Findings

**Closed-population estimators**
- The [[Petersen Estimate]] is N̂ = Mn/m, where M is the number marked, n is the second-sample size, and m is the number of recaptures. It rests on assumptions about mark retention, correct classification, population closure (or equal mortality and emigration in marked and unmarked animals), and random sampling.
- Chapman's modified estimate, N_c = [(M+1)(n+1)/(m+1)] − 1, reduces the bias from m = 0 and has a smaller expected mean square error than the Petersen estimate.
- Bailey's modification (M+1)(n+1)/(m+1) has bias of order e^(−m). Inverse sampling (Haldane, 1945) is unbiased but "little used in practice."
- The [[Schnabel Estimate]] extends the method to multiple recapture samples. The Schumacher and Eschmeyer weighting is preferred by DeLury. Ricker found that Schumacher-Eschmeyer is most efficient when half the population is marked, while Schnabel's method is most efficient when marking is negligible; the two estimates have equal efficiency when about 1/4 of the population is marked.
- Robson and Regier (1964) suggest that the unmodified Petersen estimate is almost unbiased if M + n > N or Mn > 4N. They recommend a precision target of ±10% for careful research, while Cooper and Lagler aimed at ±5%.

**Single and multiple recapture designs**
- Multiple recapture designs allow mortality and recruitment to be detected, but as the authors note, "a Schnabel-type census may be preferable" when marking itself adds immediate mortality.
- Cormack's judgement is that a single-release Petersen-type study is less affected by violated assumptions, provided enough animals can be released for acceptable precision.

**Open-population and deterministic models**
- Jackson's positive and negative methods, Bailey's maximum-likelihood approach, and the Leslie and Chitty multinomial models are deterministic and have been superseded.
- The "catch curve" approach (Chapman and Robson, 1960) estimates survival from the age distribution of recaptures.

**Stochastic models (the Jolly-Seber method)**
- Jolly (1965) and Seber (1965) independently developed a general stochastic framework that Cormack suggests "should be known as the Jolly-Seber method." Cormack concludes that stochastic models "should totally supersede" deterministic ones.
- The method estimates population size, survival, and dilution (immigration) at each sampling occasion. Cormack notes that the Jolly-Seber estimate is the most efficient one when no specific failure of the assumptions is known.
- Worked examples:
  - Jolly (1965), an entomological study with 13 occasions and 120–250 animals caught per occasion. About 60% of the living population was estimated to be marked, despite an estimated 1500 immigrants compared with a maximum population of about 1000. The standard error of population estimates was about 10%.
  - Dunnet, Anderson and Cormack (1963), a study of *Fulmarus glacialis* over 13 years with fewer than 250 birds marked. Annual survival standard error was about 4%, achieved at roughly 60% sampling intensity (compared with 30% in Jolly's study).
  - Parr (1965) compared several estimators on insect data. The Jolly-Seber estimate for July 1 was 715 ± 263 and for July 2 was 449 ± 105, against much more variable estimates from earlier methods.

**Commercially exploited fish populations**
- Beverton and Holt (1957) model the reduction of marked fish as instantaneous total mortality Z = F + M, where F is fishing mortality and M is natural mortality.
- Gulland (1955) gives maximum-likelihood estimates of M and F for a continuous fishery, and Seber (1962) introduced a time-lag correction.
- Paulik (1963a) provides a full stochastic treatment with an error analysis.
- Ricker (1958) classifies systematic errors into Type A (affect fishing mortality only), Type B (affect total mortality), and Type C (first-year behaviour anomalies).

**Tests of assumptions**
- Heterogeneity of catchability cannot be detected within a single experiment of unknown population size. Only a special experiment with a population of known size can address it (Cormack, 1966).
- Seber (1962, 1965) developed likelihood-ratio tests for whether marking affects capture risk and for equal catchability of marked and unmarked animals.
- Leslie's tests of random sampling of marked animals and goodness-of-fit tests for dilution are also described.

**Main conclusions**
- Cormack emphasises that biological knowledge must be combined with statistics. He notes that "the difficulties of capture-recapture studies are those of random sampling, proper mixing, equal vulnerability and other behavioural factors."
- Fish-specific cautions from the historical record include Petersen's (1894) low recapture rate, attributed to mark loss and non-reporting, and his later finding of excess recaptures, attributed to size-selective marking. Pond studies by Buck and Thoits (1965) found Petersen estimates "considerably biased" due to unequal vulnerability, and Krumholz (1944) and Carlander and Lewis (1948) found poisoning recoveries varied widely across species.
- Cormack's closing advice: "no capture-recapture study will give accurate estimates unless the sampling technique is specifically aimed at the particular species under study."