---
title: "Theoretical Yields at Various Rates of Natural and Fishing Mortality in Stabilized Fisheries"
author: Albert L. Tester
year: 1952/1953
publication: Transactions of the American Fisheries Society (Vol. 82)
species_examples:
  - Pacific herring (Clupea pallasi)
  - Pacific halibut (Hippoglossus stenolepis)
  - North Sea plaice (Pleuronectes platessa)
family: Multiple (Clupeidae, Pleuronectidae)
habitat: Marine — North Pacific, North Sea
ocean_basin: Pacific Ocean, North Sea (Atlantic)
topic: Fisheries population dynamics, yield-per-recruit theory, stock assessment modeling
source_id: "13529"
---

# Theoretical Yields at Various Rates of Natural and Fishing Mortality in Stabilized Fisheries

#ichthyology #marine-biology #fisheries-science #population-dynamics #stock-assessment

## Executive Summary

This 1952 theoretical paper by Albert L. Tester extends earlier work by [[Baranoff]], [[Thompson And Bell]], and [[Ricker]] on modeling sustainable yield in stabilized fish populations. Tester demonstrates mathematically that maximum yield (catch weight) in a stabilized fishery depends not only on the instantaneous rates of natural mortality (q) and fishing mortality (p), but critically on the **shape of the growth curve** — specifically the timing of the inflection point in an S-shaped (sigmoid) growth trajectory. By modeling three growth types (early-, mid-, and late-life inflection) combined with a matrix of natural and fishing mortality rates, the paper shows that yield maxima occur across a much broader range of natural mortality rates than previously reported by Baranoff, and that the growth curve shape systematically shifts where these maxima occur. The work is explicitly framed as a theoretical exploration with acknowledged limited practical applicability due to numerous simplifying assumptions.

## Background & Description

This paper is not concerned with anatomical or morphological traits of fish, but with **growth-in-weight trajectories** as the relevant "morphological" variable feeding into the population model. Three idealized [[Growth Curve]] types were hand-drawn on a scale of 0–100 weight units across 0–18 years of age:

- **Growth Type A** — point of inflection **early in life**; approximates rapid early growth, later deceleration. Empirically approximated by the [[Pacific Herring]] (*Clupea pallasi*).
- **Growth Type B** — point of inflection **about mid-life**; intermediate growth pattern.
- **Growth Type C** — point of inflection **late in life**; slow early growth followed by later acceleration/deceleration. Empirically approximated by the [[Pacific Halibut]] (*Hippoglossus stenolepis*).

All three curves converge to a common asymptotic maximum weight of 100 units by age 18, after which fish are assumed to retain maximum weight indefinitely ("18+" age class).

Notably, prior models used **exponential growth** assumptions (Thompson and Bell; Ricker) or **linear length growth with cubic weight scaling** (Baranoff, based on North Sea plaice), rather than a full sigmoid curve. Tester argues these earlier simplifications disproportionately inflate yield estimates at low mortality rates because they fail to capture the decelerating phase of growth in older/larger fish.

## Ecological & Environmental Context

The paper is a mathematical abstraction rather than a field ecology study, but it draws on the life-history context of three real fisheries to validate/interpret the theoretical curves:

- **[[Pacific Herring]]** (*Clupea pallasi*) — used as a real-world analog for Growth Type A; associated with high assumed natural mortality (q = 0.7–0.9) and moderate fishing mortality range (p = 0.3–0.8). Yield is relatively insensitive to fishing mortality rate across this range, implying that [[Maximum Sustained Yield]] depends primarily on maintaining sufficient spawner supply for recruitment (referencing "Point X" in Tester 1948).
- **[[Pacific Halibut]]** (*Hippoglossus stenolepis*) — used as analog for Growth Type C; associated with low natural mortality (q = 0.1–0.2). Maximum yield predicted at low fishing mortality (p = 0.1–0.2), preserving adequate spawning stock.
- **North Sea plaice** (*Pleuronectes platessa*) — referenced via Baranoff's original dataset, characterized by linear length growth and cubic weight-length relationship.

The model assumes a **Type IB fishery** (Ricker's classification) — a discrete-recruitment fishery with no recruitment during the fishing season — as the primary framework, with 1,000 recruits entering the fishable stock annually prior to the fishing season. A **Type IIA fishery** (continuous, uniform recruitment throughout the year, used by Baranoff and Ricker) was also trial-tested and found to produce maxima at the same fishing mortality rates, differing only in absolute yield magnitude.

## Key Findings

- **Yield magnitude scales with growth type**: for identical mortality rates (e.g., q = 0.10, p = 0.20), yields were 23,614 weight units for Type A, 10,795 for Type B, and 6,494 for Type C — directly reflecting the relative "front-loading" of growth in each curve.
- **All growth-type yield series converge** to the same limiting value (~2,000 weight units) as fishing mortality (p) approaches infinity; at high natural mortality rates, this limit represents maximum yield but **not** maximum *sustained* yield, since it implies zero surviving spawners.
- **Yield maxima persist across a much broader range of natural mortality** than found in Baranoff's original model:
  - Type A growth: maxima persist up to q = 0.9
  - Type B growth: maxima persist up to q = 0.5
  - Type C growth: maxima persist up to q = 0.3
  - (Compare: Baranoff's model showed no maxima above q = 0.30.)
- **Maxima become progressively less pronounced** (flatter) as q approaches these upper limits, and the modal (optimal) fishing mortality rate shifts rightward (higher p) as natural mortality increases — consistent with Baranoff's qualitative pattern but extended across a wider mortality range.
- **Two fishery regimes emerge**:
  1. Where **natural mortality loss exceeds growth gain** → maximum sustained yield requires high fishing intensity (p), constrained only by the need to maintain recruitment.
  2. Where **growth gain exceeds natural mortality loss** → maximum yield occurs at a lower, well-defined optimal fishing mortality rate (the curve's mode).
- The **choice of growth model materially changes fisheries management implications** — using an unrealistic exponential growth assumption (as in earlier models) systematically overestimates yield at low mortality rates by ignoring growth deceleration in older fish.
- The author explicitly cautions that despite the mathematical elegance, these theoretical yield curves have **limited direct practical application** due to numerous simplifying assumptions (constant recruitment, idealized growth curves, no fishery-independent population fluctuations) — citing [[Burkenroad 1951]] regarding real-world complications in marine fishery biology.
- Methodologically, the paper operationalizes Ricker's (1948) standard fisheries statistics: total instantaneous mortality (i = q + p), annual mortality rate (a = 1 − e⁻ⁱ), survival rate (s = 1 − a), and exploitation rate (u = ap/i), applied to a cohort of 1,000 annual recruits tracked through 18+ age classes.

---
**Related concepts:** [[Instantaneous Mortality Rate]] | [[Fishing Mortality]] | [[Natural Mortality]] | [[Yield-Per-Recruit Model]] | [[Sigmoid Growth Curve]] | [[Type IB Fishery]] | [[Type IIA Fishery]] | [[Maximum Sustained Yield]]