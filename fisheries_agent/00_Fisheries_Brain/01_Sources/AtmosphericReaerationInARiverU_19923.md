---
species: N/A
common_name: N/A
family: N/A
habitat: Freshwater stream (small river, Piedmont)
ocean_basin: N/A
location: Mechums River, Albemarle County, Virginia (Piedmont)
tags: [limnology, stream-ecology, water-quality, reaeration]
title: "Atmospheric reaeration in a river using productivity analysis"
source_id: "19923"
minckley_id: "19923"
source_citation: "G. M. Hornberger and K. G. Mahlon (1975). Atmospheric reaeration in a river using productivity analysis. Journal of the Environmental Engineering Division 101(5): 729-739. Minckley Library ID: 19923."
source_file: "19923.pdf"
text_extraction: "ocr"
---
# Atmospheric Reaeration in a River Using Productivity Analysis

#limnology #stream-ecology #water-quality

## Executive Summary

This 1975 *Journal of the Environmental Engineering Division* paper by George M. Hornberger and Mahlon G. Kelly (University of Virginia) presents two methods for estimating the [[Reaeration Coefficient]] (K), the rate at which [[Atmospheric Reaeration]] exchanges oxygen between air and river water. Both methods use nearly continuous, automatically recorded [[Dissolved Oxygen]] and temperature data, with the reaeration coefficient derived from the same data used to calculate [[Net Community Productivity]]. The methods were tested on the Mechums River in Virginia's Piedmont. The authors conclude that K can be determined reliably from the light–productivity relationship and, under many conditions, from night-time oxygen changes. This avoids reliance on empirical formulas from the literature.

## Background & Description

**Purpose.** Accurate reaeration estimates are needed for predicting the effects of waste disposal and for measuring [[Photosynthesis]] and [[Respiration]] in streams. Stream productivity is a key indicator of [[Eutrophication]]. Because excess productivity from nutrient enrichment is a pressing water quality problem, continuous productivity monitoring is useful. Reaeration uncertainty has been seen as a limit on free-oxygen productivity methods.

**Theory.** Oxygen exchange is modeled as diffusion across a thin water film. The rate of change in dissolved oxygen is proportional to the deficit from saturation (Eq. 1). The oxygen mass balance adds a net productivity term, (P − R), to the reaeration term (Eq. 2). Earlier methods used:
- The finite-difference solution of [[Odum Method]] (1956), which is subject to important errors.
- An exact solution by the authors, in which (P − R) is represented as a [[Fourier Series]].

**Earlier K-measurement methods reviewed:**
- Dome method (Copeland and Duffer)
- Sulphite method
- Tracer methods (Tsivoglou et al.)
- Empirical formulas relating K to velocity and depth (e.g., [[O'Connor-Dobbins Formula]], [[Churchill Formula]], [[Owens Formula]])

The authors judged the first three unsuitable for automated, continuous monitoring. They considered formula-based estimates potentially inaccurate, since even small K errors can be intolerable in productivity measurement.

**Study setting.** Dissolved oxygen, temperature, and incident radiation have been recorded on the [[Mechums River]] near Charlottesville, Virginia, since August 1972. Data collection and site details are given in an earlier reference (Ref. 9). The two stations used for comparison were 3/4 mile (1.2 km) apart.

## Ecological & Environmental Context

- **Heterotrophic dominance.** Natural streams are usually heterotrophic, with production (P) less than respiration (R). Nutrient enrichment raises P and the P:R ratio.
- **Gas exchange.** Estimating air–water gas exchange is the main source of uncertainty in free-oxygen productivity methods.
- **Temperature dependence.** Literature K values for 20 °C were corrected at 1.6% per degree. The study-day water temperature was 23.5 °C.
- **Hydraulics.** On August 4, 1973, mean velocity was 1.1 fps (0.34 mi/s) and mean depth was 1.3 ft (0.40 m).
- **Assumptions.** The methods assume (1) productivity is linearly related to incident light, (2) night-time respiration is constant, and (3) K is constant over one day. This implies steady flow and reasonably constant water temperature. The authors note that the first assumption was validated for the Mechums River and appears to hold in other rivers, and that the others were met in this work.
- **Single-station analysis.** Diurnal curves at the two stations were almost identical, which justified single-station (Eulerian) analysis, in which local temporal change dominates.

## Key Findings

**Method 1: Night-time oxygen (Eqs. 5–14).**
- Assumes constant night-time respiration, with K and R estimated by least squares from measured oxygen and saturation values.
- Gives a K value from a sequence of night-time measurements, in contrast with Odum's two-point (sunset/sunrise) approach.
- Works poorly when the oxygen deficit (c_s − c) barely changes overnight. The authors cite a dark-period change of only 0.03 mg/L on May 16, 1973, and 0.05 mg/L on June 12, 1973, where respiration was also not constant.
- On the other study nights the average night-time change in (c_s − c) was 0.14 mg/L, with fairly constant calculated respiration.

**Method 2: Light–productivity relationship (Eqs. 15–28).**
- Assumes P − R is linearly related to incident radiation (P = αI) and solves simultaneously for K, α, and R.
- A K value exists (K*) for which the productivity–light plot is a near-perfect straight line. Lower K produces a hysteresis loop in one direction, and higher K produces a loop in the opposite direction.
- The authors argue that an incorrect K would very unlikely compensate exactly for another factor to produce a false linear fit. A possible artifact, respiration linearly related to oxygen concentration, would overestimate K by less than 10% for the study river.

**Worked example, August 4, 1973:**
- Light method: K = 0.35 hr⁻¹
- Night-time method (midnight to 0600): K = 0.34 hr⁻¹
- The c_s − c difference rose from 0.93 mg/L at midnight to 1.04 mg/L at 0600.
- Literature formulas (corrected to 23.5 °C):
  - O'Connor and Dobbins: 0.40 hr⁻¹
  - Churchill et al.: 0.36 hr⁻¹
  - Owens et al.: 0.61 hr⁻¹
- The authors state these are reasonably close to their values. They plan to compare formulas across many days.

**Table 1. Reaeration coefficient (hr⁻¹) from two methods**

| Date | Night-time method | Light–productivity method |
|---|---|---|
| May 13, 1973 | 0.65 | 0.65 |
| May 16, 1973 | 1.41 | 0.60 |
| June 12, 1973 | 0.14 | 0.80 |
| June 27, 1973 | 1.40 | 1.10 |
| July 27, 1973 | 0.35 | 0.35 |
| August 4, 1973 | 0.34 | 0.35 |
| August 9, 1973 | 0.22 | 0.30 |
| August 10, 1973 | 0.20 | 0.25 |

The two methods agree on days with fairly constant respiration and sufficient variation in (c_s − c). The disagreements on May 16 and June 12 are attributed to the adverse conditions described above. The light method is most reliable on clear-sky days, so days with rapid radiation variation were excluded.

**Conclusions.**
- K for a small river can be reliably determined from the productivity–light relationship and, under many conditions, from nearly continuous night-time measurements.
- Linearity of the light–productivity relationship is not strictly necessary. Any easily parameterized relationship can be used.
- The agreement between the two methods makes them preferable to the empirical formulas in the literature.
- Once K is known, it can be applied to any dissolved oxygen budget problem, such as the response of a stream to a [[Biochemical Oxygen Demand]] input.
- Planned work includes comparing K values across methods and testing the automated approach in other rivers.

**Funding.** The work was supported by National Science Foundation Grant GB-32914, funds from the U.S. Department of the Interior under the Water Resources Research Act of 1964, and NOAA Grant N22-9-72(N).