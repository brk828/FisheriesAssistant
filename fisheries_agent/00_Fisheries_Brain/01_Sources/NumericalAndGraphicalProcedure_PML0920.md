---
species: N/A
common_name: N/A
family: N/A
habitat: Experimental stream channels (field channels) at the Monticello Ecological Research Station
ocean_basin: N/A
location: Monticello, Minnesota, USA
tags: [aquatic-ecology, stream-metabolism, dissolved-oxygen, primary-productivity]
title: "Numerical and Graphical Procedures for Estimation of Community Photosynthesis and Respiration in Experimental Streams"
source_id: "PML0920"
marsh_id: "PML0920"
library: "Marsh Library"
permission: "public domain"
source_citation: "J. S. Gulliver, T. W. Mattke, H. G. Stefan (1982). Numerical and Graphical Procedures for Estimation of Community Photosynthesis and Respiration in Experimental Streams. U.S. Environmental Protection Agency, Environmental Research Laboratory, Duluth, EPA-600/S3-82-052. Marsh Library ID: PML0920."
source_file: "Gulliver J.S. et al. 1982. numerical and graphical procedures for estimation of community photosynthesis and respiration in experimental streams.pdf"
text_extraction: "text"
---
# Numerical and Graphical Procedures for Estimation of Community Photosynthesis and Respiration in Experimental Streams

#aquatic-ecology #stream-metabolism #dissolved-oxygen

## Executive Summary

This EPA Environmental Research Laboratory (Duluth) report, authored by John S. Gulliver, Tedd W. Mattke, and Heinz G. Stefan, develops and tests methods for estimating total [[Community Photosynthesis]] (P) and [[Community Respiration]] (R) in streams from [[Dissolved Oxygen]] (D.O.) measurements. The core tool is the [[DORM Model]] (Dissolved Oxygen Routing Model), a numerical routing model that uses the full D.O. transport equation. It is applied to the experimental channels at the [[Monticello Ecological Research Station]] (MERS). The study also presents a simplified [[Graphical Routing Method]] and new equations for [[Surface Exchange Coefficient]] (reaeration) that include wind effects. The work is an EPA research report (EPA-600/S3-82-052, December 1982), not a fish study. It concerns whole-community stream metabolism. No fish species are addressed.

## Background & Description

Dissolved oxygen is a key indicator of stream water quality. Photosynthesis by aquatic plants produces most oxygen in many aquatic systems, while community respiration consumes it. For streams without large chemical waste loads, the oxygen budget is described as photosynthesis minus respiration plus surface exchange. Photosynthesis occurs only during daylight, so the [[Diel Curve Analysis]] of D.O. typically shows concentrations falling overnight and rising during the day. Traditional graphical approaches, such as the [[Odum Method]], estimate productivity from this diel cycle. The authors argue that these approaches often neglect [[Longitudinal Dispersion]], [[Surface Exchange Coefficient]] variation, and temperature and D.O. dependence of respiration.

The DORM model is driven by the following inputs:

- Initial longitudinal D.O. profile
- Segment lengths, cross-sectional areas, and surface widths
- Segment orientation and water surface slope
- Channel flow rate and day of year
- Latitude and longitude of the site
- Measured D.O. and water temperature at upstream and downstream stations
- Wind velocity, wind direction, and air pressure

The study pursued four objectives:

1. Develop DORM to include surface exchange, dispersion, respiratory inhibition at low D.O., and temperature dependence of respiration.
2. Develop a theory for air-water oxygen exchange that includes wind shear and [[Secondary Currents]], and test it against MERS experiments.
3. Apply DORM and the graphical method to MERS diel data and compare results.
4. Partition the stream D.O. budget among subcommunities, including [[Macrophytes]], [[Periphyton]], and [[Phytoplankton]].

## Ecological & Environmental Context

The MERS experimental channels were studied across seasons and under different water temperature, solar radiation, and pH conditions. Thirty-two diel D.O. surveys were conducted in four stream reaches during late summer and fall of 1978 and spring and summer of 1979. Water temperature during the predawn respiration calibration ranged from 15 to 24 °C. Water supplied to the channels came from the [[Mississippi River]]. Its biochemical oxygen demand was under 12 g/m³, which the authors judged to contribute negligibly to R, given residence times of 2 to 5 hours and the settling effect of the first pool.

Three channel reaches with different pH levels (8.0, 6.3, and 5.4) were compared. The low-pH reaches reached maximum P and R earlier in the growing season. The authors attribute this mainly to differences in vegetation history and shading by emergent vegetation rather than to pH alone.

Surface exchange is strongly affected by [[Wind Effects]] and stream hydraulics. The authors found that empirical surface exchange equations depend on secondary water movement and surface waves, so they do not transfer readily between streams.

## Key Findings

**Model performance and sensitivity**
- A sensitivity analysis showed that computed P and R are most sensitive to [[Residence Time]] and surface exchange (reaeration) coefficients.
- Neglecting surface exchange substantially changed results, typically by about 8% for P and 16% for R.
- Neglecting longitudinal dispersion in the MERS channels produced only small (under 2%) changes in P and R.
- Using linear interpolation between upstream D.O. measurements taken at two-hour intervals was acceptable. Finer curve fitting changed P and R by only about 0.4%.
- Incorrect residence times (±20%) changed P and R significantly (about ±18%).
- A diel temperature variation of 5 °C would cause about a 7% error in respiration rates.

**Graphical method**
- The simplified graphical routing method (advection, photosynthesis, and respiration only) gave P and R values that were on average 89% and 82% of the complete DORM values, with a standard deviation of less than 5%. The abstract lists these percentages as 82% and 89% for P and R, respectively. The report text assigns 89% to P and 82% to R, so the attribution should be checked against the full report.
- The graphical P/R ratio averaged about 0.04 units different from DORM's, with a standard deviation of 0.04.

**Productivity and respiration values in the MERS channels**
- Maximum P was about 14.9 g O₂ m⁻² day⁻¹ (the OCR text is partly garbled here).
- Maximum R was 10.7 g O₂ m⁻² day⁻¹, observed in August 1979.
- R ranged from 2.6 g O₂ m⁻² day⁻¹ (October 1978) to 10.7 g O₂ m⁻² day⁻¹.
- P/R ratios ranged from 0.3 (September 1978) to 2.1 (May 1979).
- Seasonal dependence of P and R was found, as expected.
- The respiration temperature coefficient (θ) was 1.045, derived from predawn data from September 1978. The authors note that θ may vary seasonally.

**Surface exchange theory**
- The authors developed relationships for surface exchange coefficients (K_a) for streams with and without wind effects. These account for bed shear, wind shear on the water surface, wave effects, and secondary currents.
- Literature equations applied to the MERS channels predicted K_a values spanning three orders of magnitude. The authors attribute this scatter mainly to the omission of secondary currents.
- MERS-calibrated parameters gave better predictions than literature equations. These parameters are specific to the MERS channels.

**Hysteresis in light response**
- Plots of hourly P against [[Photosynthetically Active Radiation]] (PAR) were nonlinear and frequently showed hysteresis.
- Counterclockwise hysteresis appeared on a cloudy day in July 1979 and a clear day in mid-September 1979. Other surveys in May, June, and August generally showed clockwise hysteresis.
- Sensitivity tests indicated that physical parameters cannot explain the hysteresis, which the authors believe is biological in origin. Further study is needed. See [[Hysteresis]].

**Subcommunity contributions (August 1978, Pool 14)**
- Macrophytes and periphyton contributed on average 5.3 g O₂ m⁻² day⁻¹ to photosynthesis and 10.5 g O₂ m⁻² day⁻¹ to respiration.
- Phytoplankton contributions were much smaller.
- In Riffle 13, the benthic subcommunity's photosynthetic rate (9.9 g O₂ m⁻² day⁻¹) was higher than in the pool. Its respiration rate was about equal to the pool's.

**Auxiliary tests**
- Nutrient supply in the inflow water was judged adequate, so nutrient limitation was not considered a constraint.
- [[Sediment Oxygen Demand]] in a pool bed was estimated at 0.01 to 0.04 g m⁻² h⁻¹. It was negligible in the routing process given residence times of 2 to 5 hours.
- Macrophyte respiration limitation was observed below about 3.5 g/m³ D.O.

**Recommendations**
1. Analyze diel D.O. data with a complete routing model such as DORM to minimize error.
2. Measure surface exchange coefficients in each reach of interest, along with wind speed and direction.
3. Use the Winkler method for D.O. measurements, since it is more reliable than sensors in this application.
4. Document channel geometry, orientation, and flow rates precisely, and check residence times carefully, including effects of diurnal thermal stratification.
5. Include longitudinal dispersion in highly dispersive systems, but not in the MERS channels.
6. Include temperature dependence of respiration when diel water temperature variation is 2 °C or greater.
7. Include respiratory inhibition at low D.O. when concentrations fall below 4 g/m³.
8. Investigate the causes of hysteresis in photosynthesis-light relationships.
9. Further research the D.O. limitation and temperature effects on respiration parameters.