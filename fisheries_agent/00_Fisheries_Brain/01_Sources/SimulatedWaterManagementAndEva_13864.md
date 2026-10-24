---
species:
  - "Chasmistes cujus"
  - "Catostomus commersoni"
  - "Catostomus catostomus"
  - "Xyrauchen texanus"
common_name: "Cui-ui; white sucker; longnose sucker; razorback sucker"
family: "Catostomidae"
habitat: "Lacustrine adults in Pyramid Lake; fluvial spawning in the lower Truckee River"
ocean_basin: "N/A"
location: "Truckee and Carson River basins, Nevada and California; Pyramid Lake, Nevada"
tags: [ichthyology, marine-biology, catostomidae, endangered-species, water-management, population-modeling]
title: "Simulated water management and evaluation procedures for cui-ui (Chasmistes cujus )"
source_id: "13864"
minckley_id: "13864"
source_citation: "C. C. Buchanan and T. A. Strekal (1988). Simulated water management and evaluation procedures for cui-ui (Chasmistes cujus ). US Fish and Wildlife Service. Minckley Library ID: 13864."
source_file: "13864.pdf"
text_extraction: "ocr"
---
# Simulated Water Management and Evaluation Procedures for Cui-ui (Chasmistes cujus)

#ichthyology #marine-biology #catostomidae

## Executive Summary

This 1988 report by [[Chester C. Buchanan]] (U.S. Fish and Wildlife Service) and [[Thomas A. Strekal]] (U.S. Bureau of Reclamation) documents two computer subroutines added to the [[Truckee-Carson Hydrologic Model]]: the [[Stampede Subroutine]], which schedules releases from [[Stampede Reservoir]] for [[Cui-ui]] spawning, and the [[Cui-ui Population Index Subroutine]] (CPI), which simulates the reproductive response of the endangered [[Cui-ui]] population of [[Pyramid Lake]] to river flow and lake elevation. The authors illustrate CPI by comparing three water management plans (A, B and C) over an 80-year hydrologic record (1901-80). Plan A produced the highest simulated population index and Plan C the lowest. The authors conclude that diversion amount matters more than diversion timing, and that CPI has been verified but not validated.

## Background & Description

The [[Cui-ui]] is a large, omnivorous sucker endemic to [[Pyramid Lake]], Nevada, listed as federally endangered in 1967. Diversions for agriculture and urban use, combined with droughts, caused a sharp population decline. Females can live up to 45 years and mature between 6 and 12 years of age. Adults are obligate stream spawners that run up the lower [[Truckee River]], mainly within the lower 6 miles, where they deposit eggs over gravel in 0.8 to 4.0 feet of water. Average fecundity rises from about 20,000 eggs (16-inch female) to about 105,000 (26-inch female). Egg viability appears to fall sharply after about age 30.

The [[Truckee-Carson Hydrologic Model]] simulates reservoir storage, instream flows and diversions using monthly data. Its key inputs are historical data for water years 1901-1980. [[Stampede Reservoir]] storage is dedicated to threatened and endangered fish and can only be released for that purpose.

The [[Stampede Subroutine]] sets four fish-flow regimes:
- **Regime 1A:** Attraction flows January-April (60,000 acre-feet minimum); May flows of 1,000 cfs or more (not to exceed 2,500 cfs); June flows equal to May.
- **Regime 1B:** Same as 1A, plus a July flow of 391 cfs (about 24,000 acre-feet) for late larval migration.
- **Regime 2:** Minimum flows that allow operation of the [[Pyramid Lake Fishway]] and collection of eggs at [[Marble Bluff Fish Facility]].
- **Regime 3:** No flow requirement, because there is insufficient water to run the fishway.

The regime is chosen monthly from forecasts of [[Pyramid Lake]] elevation, Stampede storage and runoff. Key thresholds are 3784 feet (minimum for fishway access) and 3812 feet (minimum for delta passage).

CPI combines elements of a [[Leslie Matrix Model]] (discrete-time age-structured model) with the [[Effective Habitat Time Series Analysis]]. Only females are modeled, because they limit reproduction. The model is initialized with a 1987 population estimate, an April 1988 lake elevation of 3812.4 feet, and 90,000 acre-feet in Stampede storage.

## Ecological & Environmental Context

**Passage and lake elevation.** Cui-ui must spawn in fresh water. They can reach the river over the [[Truckee River Delta]] (preferred, because runs are larger, earlier and less stressful) or through the [[Pyramid Lake Fishway]]. Delta passage needs at least 3 feet of water above 3812 feet; fishway passage needs one foot over the terminal weir above 3784 feet. Dredging or armoring the river was rejected as impractical.

**Run size.** Run size depends on Jan-Apr inflow (attraction flow), adult female numbers, lake elevation and passage route. The 1980-1987 Marble Bluff data give percentages of females entering the run. Through the fishway, these are under 0.1% at 51,000 acre-feet, 1.5% at 176,000 acre-feet and 5.0% above 349,000 acre-feet. Over the delta, they are 4.8% at 60,000 acre-feet, rising to 23.5% at 715,000 acre-feet or more. Passage limits cap runs at 20,000 females through the fishway and 100,000 through the river trap. A 12.5% drop-back over the spillway is applied.

**Egg and larval survival.** Survival depends on water temperature and flow. Embryo survival falls when daily maximum temperatures exceed 63°F. The adjusted temperature-survival relation gives 13.9% survival at 59°F and 8.6% at 68°F (laboratory-derived values adjusted to the 1985 river survey, which found 10.5% survival). Survival is penalized for flows above 3,500 cfs, and for May-June flow differences.

**Hatchery and stocking.** Hatchery-reared larvae and juveniles have been stocked since 1972. Only 5% of adults captured near shore in 1980-1981 returned to a spawning run by 1987, compared with 28% of 2,098 adults captured and released near shore in 1982-1983. Hatchery larvae are assumed to survive at one-third the rate of river larvae. The hatchery program is shifting to extended rearing.

**Life stages and survival.** Model survival rates, most of which are assumptions, are: yolk-sac larvae to age 1 at 0.001; yearlings at 0.75; ages 2-6 at 0.95; and adults (age 7 onward) at 0.85.

## Key Findings

- **Historic and recent runs.** From 1980 through 1987 there were seven spawning runs, averaging 12,470 fish (range 5,000-36,300). The authors consider these small relative to historic runs.
- **Dominant year class.** Only two major year classes were produced between 1950 and 1980 (1950 and 1969). The 1969 class (about 100,000 individuals) dominates the adult population; the model estimates 82,550 adult females from it in 1985.
- **Population estimate.** A Petersen-type estimate gave about 146,000 adults in 1983 (95% CI 122,000-181,000). The upper limit (181,000) was used for initialization. Release-recapture data imply about 200,000 adults, or about 113,000 females, in the 1983-1987 period.
- **Verification versus validation.** CPI was verified (logic, data and assumptions) but not validated. CPI correctly predicted no spawning run in 1988, because attraction flows were extremely low.
- **Model output comparison.** CPI adult female estimates for 1982-1986 (156,000; 133,000; 114,000; 99,000; 84,000) are broadly similar to prespawning aggregate estimates derived from tagging.
- **Plan comparison.** Plans A and B have identical average inflows to Pyramid Lake (427,300 acre-feet/year). Plan A has 31,600 acre-feet/year more inflow than Plan C. Simulated year-80 indexes were: Plan A 61,848; Plan B 47,942; Plan C 3,657 (in thousands, as shown in Figure 4). Plan A is 29% greater than Plan B and 15.9 times Plan C.
- **Drought effects.** An extended drought in the 1920s and 1930s sharply cut spawning flows. Plan C never recovered, because it allowed lake levels to drop below delta passage thresholds in many years and gave fewer spawning opportunities.
- **Management conclusion.** Diversion amount was judged more important than timing. Plan A was judged most beneficial to the species, Plan B more beneficial than Plan C.
- **Data gaps and caveats.** The authors state that the model uses deterministic historical series for illustration only. Stochastic series are needed to judge adequacy against risk. The temperature prediction model was found in February 1988 to use Fernley rather than Reno air-temperature data. Egg viability is assumed to decline linearly with age and to reach zero at age 38.
- **Broader applicability.** The authors suggest CPI methods could be adapted to other fish species in other basins.