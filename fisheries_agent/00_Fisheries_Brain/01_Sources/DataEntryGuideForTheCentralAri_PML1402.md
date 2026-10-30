---
species:
  - "Gila intermedia"
  - "Gila robusta"
  - "Tiaroga cobitis"
  - "Agosia chrysogaster"
  - "Rhinichthys osculus"
  - "Catostomus insignis"
  - "Pantosteus clarkii"
  - "Poeciliopsis occidentalis"
  - "Gambusia affinis"
  - "Micropterus salmoides"
common_name: "Gila chub, roundtail chub, loach minnow, longfin dace, speckled dace, Sonora sucker, desert sucker, Gila topminnow, mosquitofish, largemouth bass (among 50+ coded taxa)"
family: "Multiple (Cyprinidae, Catostomidae, Poeciliidae, Centrarchidae, Ictaluridae, Cichlidae and others)"
habitat: "Freshwater: rivers, creeks, canals, connected and isolated pools, riffles and runs"
ocean_basin: "N/A"
location: "Arizona, USA (Phoenix area and Central Arizona Project corridor)"
tags: [ichthyology, marine-biology, cyprinidae, fish-monitoring, data-management, freshwater]
title: "Data Entry Guide for the Central Arizona Project Fish Monitoring Program"
source_id: "PML1402"
marsh_id: "PML1402"
library: "Marsh Library"
permission: "public domain"
source_citation: "B. R. Kesner, P. C. Marsh (2010). Data Entry Guide for the Central Arizona Project Fish Monitoring Program. Marsh & Associates, LLC. Marsh Library ID: PML1402."
source_file: "M&A. 2010, Data entry guide CAP fish monitoring program.pdf"
text_extraction: "text"
---
# CAP Fish Monitoring Data Entry Guide

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This technical guide, prepared by Brian R. Kesner and Paul C. Marsh of [[Marsh & Associates]] for the [[Bureau of Reclamation]], explains how field fish-monitoring data from the [[Phoenix Area Office]] are entered, coded, and verified in the "CAP monitoring.mbd" [[Microsoft Access Database]]. It covers the [[Central Arizona Project]] Fish Monitoring Program across Arizona rivers, creeks, and canals. The document is a procedural manual rather than a research study. Its central output is a standardized, code-based workflow for recording stream, reach, station, habitat, gear, effort, and catch data, followed by a two-step verification process against paper datasheets.

## Background & Description

- **Document type:** Data entry guide submitted in partial fulfillment of U.S. Bureau of Reclamation Contract Number R09PD32013.
- **Date:** July 26, 2010.
- **Submitted to:** Robert W. Clarkson, U.S. Bureau of Reclamation, Glendale, Arizona.
- **Submitted by:** Marsh & Associates, LLC, Tempe, Arizona.
- **Scope:** Entry of sampling records from fixed-station and opportunistic surveys, including effort (passive gear hours), habitat, gear, electroshocking parameters, bait, and species catch.

The guide is organized as a field-by-field walkthrough of the database, supported by five lookup tables: stream codes (Table 1), habitat types (Table 2), gear types (Table 3), bait types (Table 4), and species codes (Table 5).

## Ecological & Environmental Context

**Monitored waters.** Stream codes cover nine systems: the [[San Pedro River]], [[Gila River]], [[Salt River]], [[Aravaipa Creek]], and [[Cienega Creek]], plus the [[CAP Canal]], the [[SRP South Canal]] (SRPs), the [[SRP North Canal]] (SRPn), and the [[FCG Canal]]. Streams are divided into one to four reaches, coded from upstream to downstream. The CAP Canal has three reaches, and the Gila River has four, although the uppermost reach has not been sampled in recent years.

**Fixed versus opportunistic sampling.** Standard fixed-station samples are flagged Y. Samples below the [[Electrical Fish Barrier]] on the SRPs and SRPn canals, all FCG Canal samples, and samples on Aravaipa Creek between fish barriers are always treated as opportunistic (N). The SRP canals are measured as miles downstream of electrical barriers or dams, coded to tenths of a mile.

**Habitat types.** Four categories are used: [[Connected Pool]] (low velocity, near-zero gradient), [[Riffle]] (fast, turbulent, steep gradient, large substrate), [[Run]] (rapid, non-turbulent, deeper than riffles), and [[Isolated Pool]] (as connected pools, but without surface connection to the stream).

**Native and focal taxa in the species list.** Table 5 includes several native or conservation-relevant Arizona fishes, notably the [[Gila Chub]] (GILN), [[Roundtail Chub]] (GIRO), [[Loach Minnow]] (TICO), [[Gila Topminnow]] (POOC), [[Sonora Sucker]] (CAIN), [[Desert Sucker]] (PACL), [[Longfin Dace]] (AGCH), and [[Speckled Dace]] (RHOS). Non-native and sportfish taxa include [[Largemouth Bass]] (MISA), [[Smallmouth Bass]] (MIDO), [[Channel Catfish]] (ICPU), [[Common Carp]] (CYCA), [[Mosquitofish]] (GAAF), and several tilapia and sunfish species.

## Key Findings

### Structure and scale of the coding system

- **Stream codes (Table 1):** 9 systems (1 = San Pedro through 9 = Cienega).
- **Habitat codes (Table 2):** 4 habitat types.
- **Gear codes (Table 3):** 28 codes. Code 27 is visual observation and code 28 is dry site. Codes 7, 8, and 18–22 (electroshock) trigger the ELECTROSHOCK fields.
- **Bait codes (Table 4):** 8 types, from artificial lure (1) to other (8), including cut bait, pellet fish food, and pet food.
- **Species codes (Table 5):** more than 50 four-letter codes, with 0000 meaning no fish caught and UNKN meaning unknown fish species. The table also maps codes to common and scientific names, some of which are garbled in the source and should be verified against a current taxonomic reference.

### Data entry rules

1. **Numeric codes only.** Stream, reach, and station fields accept numeric codes only, even though datasheets carry names and text descriptions. Unlisted codes must be referred to the database administrator.
2. **Date and time.** The DATE/TIME IN field is required for all sampling. DATE/TIME OUT is required for passive gears (nets, traps, trotlines) and is used to calculate effort hours, so OUT must be later than IN.
3. **Electroshock parameters.** Pulses per second, volts, amps, temperature (°C, must be between 0 and 50), and seconds are recorded for electroshocking gears.
4. **Netting parameters.** Mesh size (inches), length (feet), and depth (feet) are required for all seines and nets. NO. OF HAULS applies only to seines and dip nets.
5. **Baited gear and angling.** Baited netting uses the BAIT TYPE field. All angling gears (codes 4–7) require BAIT TYPE and NO. OF HOOKS.
6. **Percent habitat sampled.** Required for fixed-station efforts with appropriate gear codes (7–13 and 18–26).
7. **Catch records.** SPECIES, AGE (0/1), NO. OF FISH, NO. OF VOUCHERS, and COMMENTS are entered per catch line. Age 0 denotes young-of-year and 1 denotes age one or older, applied only to large-bodied fishes. NO. OF FISH must be greater than zero except for 0000. Voucher counts record fish retained for scientific purposes.
8. **Sample year.** Entered at session close as a four-digit year. This matters because some sampling, such as SRPn canal work, occurs in January of the following year.

### Verification protocol

- Each record is checked field by field against the paper datasheet.
- The station name generated from stream, reach, and station codes must match the datasheet.
- Calculated effort is confirmed against the datasheet.
- Each record is marked VERIFIED before the session closes.
- Records missing from the Data Review form most likely lack the VERIFIED checkbox. Reopening the Data Verification form should show a blank form when all records are verified.
- Previously verified datasheets must not be re-entered if a session is interrupted and restarted.

### Session rules

- Data from different sample years must be entered in separate sessions.
- Unverified records remain editable if a session closes early.

### Overall conclusion

The guide establishes a consistent, code-driven pipeline for Central Arizona Project fish monitoring data. Its controls (mandatory codes, effort calculation, and a dual-check verification step) are designed to keep data from multiple reaches, gears, and years comparable and accurate for long-term monitoring of native and non-native fish populations in Arizona.