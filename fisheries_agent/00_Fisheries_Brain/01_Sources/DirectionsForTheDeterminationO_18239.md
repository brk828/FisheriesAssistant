---
species: N/A
common_name: N/A
family: N/A
habitat: Marine and freshwater natural waters (sea water, lakes, ponds, streams, experimental microcosms)
ocean_basin: N/A
location: Port Aransas and Austin, Texas; Woods Hole, Massachusetts (sea water sample); Oklahoma State University
tags: [methods, carbon-dioxide, pH, metabolism, limnology, marine-biology]
title: "Directions for the determination of changes in carbon concentration from changes in pH"
source_id: "18239"
minckley_id: "18239"
source_citation: "R. J. Beyers, J. L. Larimer, H. T. Odum, R. B. Parker and N. E. Armstrong (1963). Directions for the determination of changes in carbon concentration from changes in pH. Publications of the Institute of Marine Science 9: 454-489. Minckley Library ID: 18239."
source_file: "18239.pdf"
text_extraction: "ocr"
---
# Directions for the Determination of Changes in Carbon Dioxide Concentration From Changes in pH

#ichthyology #marine-biology #limnology

## Executive Summary

This methods paper by Beyers, Larimer, Odum, Parker and Armstrong (The University of Texas, Institute of Marine Science, 1963) describes a [[Tonometer Burette]] apparatus and titration procedure for converting measured pH changes in natural waters into changes in total dissolved carbon dioxide. Where pH shifts arise from metabolic addition or removal of CO₂, the method yields continuous estimates of metabolism from pH recordings. The paper supplies calculation tables, a sample titration of [[Sea Water]], and a [[Diurnal Graph Computer Program]] for the [[Control Data Corporation 1604]] computer.

## Background & Description

The pH of most natural waters tracks dissolved carbon dioxide, and the relationship has underpinned many field and laboratory studies of [[Metabolic Carbon Dioxide Changes]] (over 40 cited works, roughly 1919 to 1963). The authors note that earlier efforts were sometimes flawed because the pH–CO₂ relationship is nonlinear. Two conversion routes exist:

- **Theoretical:** computation from alkalinity and dissociation constants. This assumes simple carbonate equilibria, which is questionable given the many published dissociation constants.
- **Empirical:** titration with strong acids and bases, or gas analysis. Earlier work (Beyers and Odum, 1959, 1960; Lyman, 1961) showed that strong acids or bases cannot simulate CO₂ over some pH ranges.

The method therefore titrates sample water with CO₂-saturated distilled water, which acts as a gaseous CO₂ titrant with distilled water as carrier. The paper reports that about 300 diurnal CO₂ rate-of-change curves had been computed at the Institute of Marine Science, with a similar number at Oklahoma State University. The method was also applied to [[Chironomid Larvae]], [[Decapod Crustacea]] and small minnows.

## Ecological & Environmental Context

The method targets aquatic metabolism, including [[Primary Production]] and respiration in whole ecosystems and [[Aquatic Microcosms]]. Diurnal pH swings in productive waters reflect photosynthetic CO₂ uptake by day and respiratory CO₂ release at night. The authors stress that the buffering capacity of the water controls the slope of the titration curve. Hard water gives a shallow curve and requires longer nitrogen or CO₂-free air treatment to raise pH. Soft water gives a steeper curve. The procedure is suited to work where water is scarce, since the sample is altered only by a few ml of distilled water.

Worked-example water characteristics:
- Sea water sample from the vicinity of Woods Hole, Massachusetts
- Salinity 31.8‰
- Initial CO₂ concentration X = 0.001424 mM/ml at pH 8.93 (determined by Dr. K. G. Wood)
- Observed barometric pressure 765.2 mm Hg; barometer and titrant at 24.4 °C; M value 0.03347

## Key Findings

**1. Apparatus and preparation of CO₂-saturated water**
- Pure CO₂ flows at about 555 cc/min through a copper coil (264 cm long, 0.75 cm inside diameter), then through two Fisher-Milligan gas washers (274 cc volume each) in series.
- About 60 cc of distilled water goes into the bulb of a standard 50 ml burette, which is rotated at 30 rpm for 20 minutes to saturate the water.
- Specifications: bulb outside diameter 10.14 cm; barrel total length 77.19 cm; total tonometer length 104.00 cm; barrel slope in cradle 6°. Motor model SG15–30 RPM (Merkle-Korff Gear Co.).

**2. Titration**
- Sample volumes are 100, 200 or 300 ml. Titrant is added in 0.1 or 0.2 ml increments under the surface, and pH is read after each increment.
- Stable pH is reached within 10 to 15 seconds with gentle stirring.
- An average 300 ml titration uses about 15 ml of CO₂-water, which alters alkalinity by at most 5%.
- Volume changes are corrected with F factors before plotting.

**3. Calculations**
- Millimoles of CO₂ per ml of titrant are calculated as M = (B − b_t − w_t)(α)/(B₀)(ml/mM).
- Table 3 gives M values for barometric pressures of 550–799 mm Hg and temperatures of 19.0–26.8 °C. Standard barometric pressure is 760 mm Hg and gas volume is 22.4 ml/mM.
- The core relation is Δ[CO₂] = F(M − X), which simplifies to Δ[CO₂] = FM when FX is small.
- Table 4 lists F factors for 0.1 ml increments up to F = 99.0991 for 100, 200 and 300 ml samples.

**4. Sample titration results (Table 2)**
- pH fell from 8.93 to 6.12 as titrant rose from 0.0 to 22.0 ml.
- Actual CO₂ rose from 1.424 mM/l to 3.614 mM/l over that range.
- Example points: pH 8.93 at 1.424 mM/l; pH 7.00 at about 2.155 mM/l (7.0 ml titrant); pH 6.50 at 2.853 mM/l (14.0 ml).

**5. Diurnal computer program (PRBYPH)**
- Input: NTRA and NTRB counts, a 10-digit identification NAME, 84 PHC values (CO₂ at 0.1 pH steps from 14.0 down to 5.7), 25 hourly pH values, two light-change times (KTIME), a light-sequence code (KCODE 1 or 2), and DEPTH in meters.
- Output: production and respiration in mM CO₂/L and g CO₂/m² per period, and the P/R ratio.
- Run time is about 7 seconds per data set, compared with under one second for the program (M2 UTEX PRBYPH) described in the paper. A separate program (M2 UTEX CARBON) is noted as performing the same tasks while also plotting pH and rate-of-change values.

**6. Validation**
- Dr. K. G. Wood's Van Slyke determinations on a duplicate sample (Wood, 1963) were plotted against the titration curve in Fig. 2 for comparison.
- The paper notes that, for accuracy within 5%, X need not be measured. X may be estimated from total alkalinity in high-pH water if carbonate and bicarbonate are the only buffer components.

**Conclusion:** The authors present a procedure for converting pH records into total CO₂ changes that avoids assumptions about dissociation constants and avoids strong acid/base titrants. It is intended for continuous metabolic measurement in natural waters and microcosms.

---

**Cross-links:** [[Carbon Dioxide Titration]] · [[pH-CO2 Titration Curve]] · [[Tonometer Burette]] · [[Diurnal Graph Computer Program]] · [[Control Data Corporation 1604]] · [[Van Slyke Method]] · [[Sea Water]] · [[Primary Production]] · [[Aquatic Microcosms]] · [[Chironomid Larvae]] · [[Decapod Crustacea]] · [[Alkalinity]] · [[Buffer Capacity]] · [[Metabolic Carbon Dioxide Changes]]