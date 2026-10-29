---
species: Hierodula crassa, Mantis religiosa, Musca domestica, Phormia regina
common_name: Praying mantid, European mantis, housefly, blowfly
family: Mantidae, Muscidae, Calliphoridae
habitat: Laboratory cultures and cages; praying mantids also collected in nature
ocean_basin: N/A
location: Forest Research Laboratory, Victoria, British Columbia, Canada
tags: [functional-response, predation, invertebrate-predators, hunger, mantid, components-analysis]
title: "The functional response of invertebrate predators to prey density"
source_id: "20475"
minckley_id: "20475"
source_citation: "C. S. Holling (1966). The functional response of invertebrate predators to prey density. Memoirs of the Entomological Society of Canada 98(48): 1-86. Minckley Library ID: 20475."
source_file: "20475.pdf"
text_extraction: "ocr"
---
# The Functional Response of Invertebrate Predators to Prey Density

#ichthyology #marine-biology #mantidae

## Executive Summary

This Memoir of the Entomological Society of Canada (No. 48, 1966) by C. S. [[Holling]] extends a [[Components Analysis]] of predation by adding [[Hunger]] as a component affecting the [[Functional Response]] of predators to prey density. The work uses the praying mantid *Hierodula crassa* preying on houseflies (*Musca domestica*) as the main experimental system. The author derives fragmental equations for hunger, reactive field size, pursuit, capture success, eating time and digestive pauses, then synthesizes them into a computer-run attack-cycle model. The model predicts independent laboratory attack data well and generates a Type 2 functional response, which the author argues describes all invertebrate predators examined.

Note: the document is a research monograph on invertebrate predation. It contains no fish-specific research. Fish appear only in passing comparisons, such as [[Stickleback Predation]] and Ivlev's work on fish feeding.

## Background & Description

- **Scope:** Predation is analyzed as a whole system, with emphasis on realism, precision, wholeness and generality.
- **Method:** The [[Experimental Components Analysis]] builds models in small steps, with theory and experiment feeding each other. Components are classed as basic (universal) or subsidiary (sporadic), giving 2^5 = 32 possible response types from five subsidiary dichotomies.
- **Functional vs numerical response:** Following [[Solomon]] (1949), the functional response concerns prey consumption and the numerical response concerns predator density. The functional response is the focus of this paper.
- **Experimental animal:** *Hierodula crassa* was chosen as a "hunger analogue" for invertebrate predators. Mated females aged 11 to 40 days were the "standard mantid." These are ambush predators, so their speed of movement is zero, a limiting case.
- **Prey:** Adult female houseflies, averaging 0.0245 ± 0.0003 g (N = 379).
- **Rearing conditions:** 27 °C, 60 to 70% relative humidity, 16 h light and 8 h dark. Feeding follows a strong diurnal rhythm, so attack measurements were confined to 0700 to 2300 h.

## Ecological & Environmental Context

- **Earlier models compared:** [[Lotka-Volterra Model]] and [[Volterra Model]] (linear), [[Thompson Model]] and [[Nicholson-Bailey Model]] (exploitation), [[Gause Model]] and [[Ivlev Model]] (hunger), [[Rashevsky Model]] (hunger with energy loss), and [[Watt Model]] (most complete, empirical). Holling argues all share three drawbacks: too few components, reliance on calculus, and untested assumptions.
- **Disc equation:** An earlier artificial system (blindfolded human searching for sandpaper discs) gave the basic "disc" equation, Na = aTrNo/(1 + aTuNo).
- **Invertebrate vs vertebrate models:** The invertebrate model produces a Type 2 response. Adding learning and prey inhibition gives a [[Vertebrate Functional Response]] with an S-shaped Type 3 curve.
- **Other taxa referenced:** Blowfly (*Phormia regina*), locust, salamander, rat, spider (*Achaearanea tepidariorum*), backswimmer (*Notonecta glauca*), coccinellid (*Coccinella septempunctata*) and chaetognath (*Sagitta hispida*).

## Key Findings

**Hunger**
- Hunger is defined operationally as grams of food required to satiate a mantid, with satiation criterion of three consecutive refusals.
- Hunger equation: H = HK(1 − e^(−AD·TF)), with HK = 1.001 g and AD = 0.05013 when forced through the origin.
- For *M. religiosa*, HK = 0.109 g and AD = 0.146. For *Phormia regina* (sucrose, two methods), HK = 21.2 and AD ≈ 0.129 to 0.134.

**Reactive field and rate of search**
- Hunger threshold for attack HT = 0.369 g (regression intercept); later averaged to 0.341 g.
- Maximum distance of stalk or strike: rm = GM(H − HT), with GM = 11.73 (later corrected to 24.63). No response occurs less than 8 h after satiation.
- Field area: A = KA·rA², with KA = 0.8064 for *H. crassa*. Area also depends on hunger, A = KA[GM(H − HT)]².
- Capture success SC = (SR)(SS)e^(−8.17·TP), with SR assumed 0.80, SS = 0.630 (freely moving flies; 0.7885 on threads).
- Pursuit velocity VP = 210.6 cm/h (51 stalks). Fly velocity declines with density via VY = 223e^(−139.3·N0) + 92.

**Handling time**
- Eating rate KE = 0.760 h/g, unaffected by hunger (n = 3468). Time to eat one fly, TE = 0.0186 h.
- Digestive pause TD is derived from the hunger equation and occurs only when hunger falls below HT.
- Strike success did not depend significantly on hunger (slope 0.0939, P = 0.7 to 0.8).

**Attack cycle and validation**
- Model cycle: TI = TD + TS + TP + TE, implemented in Fortran on an IBM 1620 with an iterative solution for TS.
- Predicted attack rates matched observed rates across three prey density ranges (Fig. 28), and the model reproduced attacks over 16 h (Fig. 29).
- Predicted end-of-feeding hunger was overestimated; a "stop-eating" threshold lower by 0.222 g after the feeding period explains the discrepancy. Regression slope was 1.07, not significantly different from 1.00.
- Attack threshold check: 115 feedings gave 0.3131 ± 0.0154 g versus 0.3693 g from Fig. 7.

**Simulation and applications**
- Type 1 response (linear rise to plateau) arises when reactive field size is constant; Type 2 (negatively accelerated) is the general case.
- Under the *M. religiosa* simulation, daily consumption was 12 flies predicted versus 10.81 ± 0.68 flies observed (N = 36).
- Stomach contents can estimate predation: number attacked per day is linear in food in gut (NA = c′G). For small prey, this allows field estimates, but for *M. religiosa* the variability is large (5.2 to 8.9 flies for 0.06 g).

**Generality**
- Of ten invertebrate species examined (orthopterans, hemipterans, coleopterans, crustaceans, mites), the Type 1 and Type 2 responses cover all examples.
- The author concludes that the model applies to invertebrate predators and describes major parts of vertebrate attack.

**Conclusion**
- An integrated model can be realistic, precise, whole and general at once. Its main strength is that thresholds, time lags and discontinuities can be preserved only when the model is coded as a computer program.