---
species: N/A
common_name: N/A
family: N/A
habitat: Alluvial stream channel (pool-riffle sequences in a small meandering stream)
ocean_basin: N/A
location: Mansfield Creek, western New York, USA (approx. 65 km south of Buffalo)
tags: [fluvial-geomorphology, stream-channel, pool-riffle, freshwater-ecology]
title: "Objective identification of pools and riffles"
source_id: "PML2037"
marsh_id: "PML2037"
library: "Marsh Library"
permission: "not public domain"
source_citation: "M. P. O'Neill, A. D. Abrahams (1984). Objective identification of pools and riffles. Water Resources Research. Marsh Library ID: PML2037."
source_file: "O'neill M.P. et al. 1984. Objective identification of pools and riffles.pdf"
text_extraction: "text"
---
# Objective Identification of Pools and Riffles in Alluvial Channels

#fluvial-geomorphology #freshwater-ecology #pool-riffle-sequence

## Executive Summary

This paper, by O'Neill and Abrahams (Department of Geography, State University of New York at Buffalo), proposes an objective method for identifying [[Pool-Riffle Sequence|pools and riffles]] in alluvial stream beds. The [[Regression Technique]] commonly used for this purpose is shown to misidentify bed features because it cannot separate large-scale from small-scale undulations. The authors introduce the [[Bed Form Differencing Technique]], which classifies bed forms from cumulative elevation changes against a tolerance value set as a multiple of the [[Standard Deviation]] of successive bed-elevation differences. The method is tested on a 519 m reach of [[Mansfield Creek]]. The tolerance of 0.25 SD gave the most realistic results on that reach. The authors describe the findings as tentative because they rest on a single data set.

## Background & Description

Pools (deeper sections) and riffles (shallower sections) alternate along many alluvial channels and are a basic morphological feature of them. Their spacing is often cited at about 5 to 7 channel widths. Pool-riffle sequences are widely thought to develop best in gravel-bed channels.

The regression technique fits a line or polynomial to bed elevation against channel distance. Pools are identified where residuals are negative and riffles where residuals are positive. It is objective and simple, but the authors argue it has an inherent flaw:
- Undulations at a scale larger or smaller than pools and riffles produce isolated residuals of either sign.
- Milne's (1982) study of [[Kingledoors Burn]] shows three such small positive residuals, which Milne disregarded. That step introduced subjectivity.
- The problem is common in published bed profiles from [[Leopold and Wolman]], [[Richards]] and others, so the regression technique is unreliable for identifying bed forms objectively.

Higher-order [[Polynomial Regression]] fits gave nearly the same residual series as the linear fit and did not improve identification.

## Ecological & Environmental Context

**Study reach (Mansfield Creek):**
- Reach length: 519 m
- Drainage area: 5.15 km²
- Slope: 0.0027
- Bankfull width: about 3 m
- Planform: sinuous, with a straight section created by a [[Meander Cutoff]] in the central reach
- A well-developed pool-riffle sequence runs the full length of the reach, including the cutoff section

**Sediment (Particle Size Analysis):**
- Bed material in a typical pool: 17.9% gravel, 45.1% sand, 28.1% silt, 8.9% clay
- Bed material in a typical riffle: 46.1% gravel, 33.0% sand, 15.5% silt, 5.4% clay
- Bank material: 21.0% sand, 53.4% silt, 25.6% clay
- Gravel was rarely larger than −5 φ (32 mm)

The authors note that pool-riffle sequences here formed with only modest gravel on a bed whose banks are mainly silt and clay. This makes the site a useful test of whether the method works outside gravel-bed channels.

**Field survey:** In July 1982, during low flow, planimetric and longitudinal form were surveyed with a standard level, leveling pole and compass. Bed elevations were measured at 174 points at 3 m intervals along the channel centreline. The 3 m interval was chosen because it roughly equals the mean channel width, which is the measured length L used in the method.

## Key Findings

**1. Bed Form Differencing Technique (proposed method)**
- Input: bed elevations at a fixed interval (L ≈ channel width) along the channel. Successive differences (δ₁, δ₂, …) are computed, and their standard deviation (SD) is calculated.
- A "series" is an uninterrupted run of same-sign differences. A series elevation change (Ξ) is the sum of differences within the series.
- A [[Cumulative Elevation Change]] (Σ Ξ) is accumulated since the last identified bed form.
- A bed form is identified when |ΣΞ| ≥ T, where T is the [[Tolerance Value]]. The series endpoint is then an absolute minimum (pool) or maximum (riffle).
- If |ΣΞ| < T, the end point is only a local extremum, and the analysis continues.
- Because it relies on cumulative change rather than individual amplitudes, the method handles superimposed undulations better than the regression technique.
- Only simple arithmetic is required. The method can be applied to other bed forms, such as bars and dunes, by changing L and T to suit their scale.

**2. Choice of tolerance (T)**
Four values were tested: 0.25 SD, 0.50 SD, 0.75 SD and 1.00 SD.
- **T < 0.25 SD:** pools or riffles often split into two or more separate forms. Some are spurious.
- **T ≈ 0.25 SD:** the authors judged this the most realistic result. It identifies all major bed-profile undulations and avoids wrongly identifying minor ones (Figure 5D).
- **T ≥ 0.75 SD:** genuine undulations are overlooked, producing occasional very long bed-form spacings. Mean spacing is large at 0.75 SD and close to the upper limit of the generally accepted range at 1.00 SD.
- The identified bed forms at 0.25 SD had a mean spacing of 6.14 channel widths.
- The authors tentatively recommend a value of T when L = W. The scanned text is partly illegible at this point, so the exact recommended value should be checked against the original paper. Because the result comes from one data set, they call for further tests before the recommendation can be generalised.
- Where L ≠ W, the authors state that the appropriate T cannot be determined without further data.

**3. Comparison with the regression technique (Mansfield Creek)**
- Both methods agree on the major pool-riffle sequence, but the regression technique also identifies small-scale undulations as separate bed forms.
- Between about 230 and 290 m, the regression technique gives an unrealistically long riffle. Field observations show several pools and riffles here, and the differencing technique locates them accurately.
- Between about 130 and 170 m, the regression technique gives a series of negative residuals that merge distinct pools. The differencing technique separates them correctly.

**4. Frequency distributions of spacing**
- Spacing distributions for pools, riffles and pool-riffle pairs were compared across tolerance values (Figures 6 and 8).
- Spacing from the regression technique has a longer tail and a smaller modal value than the differencing technique's distribution. This reflects the extra spurious bed forms it produces.

**5. Conclusions and limitations**
- The regression technique is objective in form but depends on subjective judgement when small residuals appear, and it is not reliable for identifying bed forms in general.
- The bed form differencing technique gives consistent, objective results in this study, but the optimum tolerance has been tested on only one reach. Additional data sets are needed, especially for different stream types, sediment regimes and reach lengths.
- The authors argue that a standardised, objective method would make comparisons of pool-riffle spacing across streams more meaningful.