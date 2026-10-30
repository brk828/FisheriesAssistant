---
species: Chasmistes cujus
common_name: Cui-ui
family: Catostomidae
habitat: Lacustrine adults in Pyramid Lake; fluvial spawning in the lower Truckee River
ocean_basin: N/A
location: Pyramid Lake and lower Truckee River, Nevada; Truckee and Carson River basins, Nevada/California
tags: [ichthyology, marine-biology, catostomidae, cui-ui, water-management, population-modeling, endangered-species]
title: "Simulated Water Management and Evaluation Procedures for Cui-ui (Chasmistes cujus)"
source_id: "PML0312"
marsh_id: "PML0312"
library: "Marsh Library"
permission: "public domain"
source_citation: "C. C. Buchanan, T. A. Strekal (1988). Simulated Water Management and Evaluation Procedures for Cui-ui (Chasmistes cujus). U.S. Fish and Wildlife Service and U.S. Bureau of Reclamation. Marsh Library ID: PML0312."
source_file: "Buchanan and Strekal 1988. Simulated Water Management and Evaluation Procedures for Cui-ui.pdf"
text_extraction: "mixed"
---
# Simulated Water Management Evaluation Procedures for Cui-ui (Chasmistes cujus)

#ichthyology #marine-biology #catostomidae

## Executive Summary

This September 1988 report by Chester C. Buchanan (U.S. Fish and Wildlife Service, [[Great Basin Complex]], Reno) and Thomas A. Strekal (U.S. Bureau of Reclamation, Lahontan Basin Project Office, Carson City) documents two computer subroutines added to the [[Truckee-Carson Hydrologic Model]] to evaluate water management effects on the endangered [[Cui-Ui]] of [[Pyramid Lake]], Nevada. The [[Stampede Subroutine]] sets flow regimes for spawning releases from [[Stampede Reservoir]], and the [[Cui-Ui Population Index Subroutine]] (CPI) simulates the cui-ui population response to river flows and lake elevation. The model was not formally validated, since the calibration data (1980–1987) were used to build present relations. Applied to three water management plans over 80 years of hydrologic record, Plan A produced the highest population index, and the authors judged it the most beneficial to the species.

## Background & Description

- **Species:** [[Cui-Ui]] (*Chasmistes cujus*), a large, omnivorous [[Catostomidae|Catostomid]] sucker endemic to [[Pyramid Lake]]. Listed as federally endangered in 1967. Females can live up to about 40 years (age reported as "~40" in OCR-affected text; males reportedly into the late twenties). Maturity is reached between 6 and 12 years.
- **Life history:** An obligatory stream spawner in the lower [[Truckee River]]. Spawning runs begin in April or May and last 4 to 9 weeks, with most fish entering in a 1- to 2-week period. Adults spend up to 16 days in the river and return to the lake quickly after spawning. Spawners probably attempt to spawn only once every 3 or 4 years. Eggs are broadcast over gravel in 0.9 to 4.0 ft of water at velocities of 1 to 2 ft/s.
- **Fecundity:** Average fecundity rises from about 20,000 eggs for a 16-inch female to almost 105,000 for a 25-inch female. Egg viability declines sharply after about 30 years of age.
- **Historical context:** Large diversions from the Truckee River, combined with droughts, caused a dramatic decline. Historic spawning runs were probably in the hundreds of thousands. Between 1950 and 1980 only two major year classes (1950 and 1969) were produced; the 1969 class dominates the adult population.
- **Management:** The [[U.S. Fish and Wildlife Service]] leads research and management under the 1978 [[Cui-Ui Recovery Plan]]. Stampede releases supplement flows below Derby Dam, and [[Marble Bluff Fish Facility]] provides passage over the delta and Marble Bluff Dam.
- **Study system:** The [[Truckee-Carson Hydrologic Model]] is a monthly river-system simulation using historic hydrology (80 water years, October to September). It covers Truckee River reservoirs ([[Lake Tahoe]], [[Prosser Creek Reservoir]], [[Boca Reservoir]], [[Stampede Reservoir]]) and the Carson River at Fort Churchill.

## Ecological & Environmental Context

- **Access:** Cui-ui reach the spawning area either over the [[Truckee River Delta]] (preferred, since runs are larger and earlier and fish are less stressed) or through the [[Pyramid Lake Fishway]]. Delta passage requires lake elevation above 3,812 ft m.s.l., and fishway passage requires elevation above 3,784 ft m.s.l.
- **Egg and larval survival:** Survival depends on water temperature, redd scouring and dewatering, predation, fertilization, and substrate. A 1985 survey found 10.5% of potential eggs survived to yolk-sac larvae. Survival falls at high temperatures; a 1987 high-air-temperature event gave 1.4% survival versus 8.5% predicted.
- **Flow regimes:** Four flow regimes (1A, 1B, 2, 3) govern releases. Regime 1A requires attraction flows of about 60,000 acre-feet from January to April, May flows of at least 1,000 cfs, and June flows equal to May flows up to 2,500 cfs. Regime 3 applies when no spawning is expected.
- **Hatchery:** Millions of hatchery-reared larvae were stocked from 1972 to 1987. Only 5% of adults returned to a spawning run, compared with 28% of wild-captured adults. [[Pyramid Lake Fisheries]] has shifted from larval production to extended rearing.
- **Companion species:** The [[Lahontan Cutthroat Trout]] shares the same passage facilities and Stampede releases.

## Key Findings

- **Model structure:** CPI combines the logic of a Leslie matrix with the [[Effective Habitat Time Series Analysis]] approach. It tracks females only, since they limit reproduction. Simulation begins in summer 1987 with 1969 year-class adults estimated at 82,550 females.
- **Run size relations:** Run size depends on lake elevation, passage route, and attraction inflow. At lake elevations above 3,812 ft, 4.8% of adult females enter the run at 60,000 acre-feet and 23.5% at 715,000 acre-feet or more. Through the fishway, fewer than 0.1% enter at 51,000 acre-feet and 5.0% at flows above 349,000 acre-feet.
- **Capacity limits:** The fishway passes at most 20,000 females, and the river trap 100,000. Spawning runs drop back 12.5% over the Marble Bluff spillway.
- **Survival assumptions:** Annual survival is set at 0.75 for yearlings, 0.95 for ages 2 to 6, and 0.85 for adults. Egg-to-yolk-sac survival is adjusted for temperature and flow consistency.
- **Validation status:** Verification relies on literature comparison and logic checks, not formal validation. Table 1 compares simulated adult females (for example, 156,000 in 1982 and 51,000 in 1985) with prespawning aggregate estimates. A release-recapture estimate gave about 200,000 adults, or roughly 113,000 females at a sex ratio of 1.3 females per male. CPI correctly predicted no spawning run in 1988 under very low attraction flows.
- **Water management comparison:** Plans A and B have identical mean annual inflow to Pyramid Lake. Plan A's index was 61,848, and Plan C's index was 58,178 (a factor of 15.9 lower than Plan A in the reported comparison). Plan A produced four more year classes than Plan B.
- **Key conclusion:** Diversion amount matters more than timing for cui-ui persistence. Plan A appears most beneficial to the species, Plan B is more beneficial than Plan C, and CPI is useful for comparing alternatives and can be updated as new data arrive.
- **Broader applicability:** The authors suggest CPI procedures could be adapted to other fish species in other basins.