---
species:
  - "Multiple taxa (about 50 species and generic codes; see Key Findings)"
common_name: "Multiple (e.g., Gila Chub, Largemouth Bass, Common Carp, Channel Catfish)"
family: "N/A"
habitat: "Freshwater rivers, creeks, canals, and pools (riffles, runs, connected and isolated pools)"
ocean_basin: "N/A"
location: "Arizona, USA: Gila, Salt, and San Pedro rivers; Aravaipa and Cienega creeks; Central Arizona Project canals"
tags: [fish-monitoring, data-entry, central-arizona-project, freshwater, database]
title: "Data Entry Guide for the Central Arizona Project Fish Monitoring Program"
source_id: "PML1276"
marsh_id: "PML1276"
library: "Marsh Library"
permission: "public domain"
source_citation: "B. R. Kesner, P. C. Marsh (2010). Data Entry Guide for the Central Arizona Project Fish Monitoring Program. Marsh & Associates, LLC, prepared for U.S. Bureau of Reclamation (Contract R09PD32013). Marsh Library ID: PML1276."
source_file: "Kesner B.R. et al. 2010. Data entry guide for the CAP fish monitoring program .pdf"
text_extraction: "text"
---
# Central Arizona Project Fish Monitoring Database: Data Entry Guide

#ichthyology #marine-biology #freshwater-fish-monitoring

## Executive Summary

This document is a data entry guide for the [[Central Arizona Project]] (CAP) Fish Monitoring Program, prepared by Brian R. Kesner and Paul C. Marsh of Marsh & Associates, LLC for the [[U.S. Bureau of Reclamation]] under Contract Number R09PD32013. It accompanies a final report (June 14, 2010) on the development and design of the program's electronic [[Microsoft Access Database]], and a companion guide dated July 30, 2010. The guide explains how field datasheets are transcribed into the "CAP monitoring.mbd" database, covering stream and station coding, habitat types, gear types, bait types, catch records, and the data verification workflow. It contains no ecological results of its own; its value lies in standardizing how fish survey data from Arizona rivers and canals are recorded.

## Background & Description

The program monitors fish in several regional waterways and water-delivery structures associated with the CAP system. Its database is organized around five coded lookup sets:

- **Streams and reaches:** Nine stream codes (Table 1), including the [[Gila River]], [[Salt River]], [[San Pedro River]], [[Aravaipa Creek]], [[Cienega Creek]], the CAP Canal, [[SRP South]] and [[SRP North]] canals, and the [[Fort Cobb Gila Canal]] (FCG). The Gila River has four reaches, the CAP Canal three, and the SRP and FCG canals two each, coded from upstream to downstream.
- **Habitat types:** Four codes (Table 2): Connected Pool, Riffle, Run, and Isolated Pool.
- **Gear types:** Codes 1 to 28 (Table 3), covering gill, trammel, hoop, fyke, and trap nets, several seine types, angling methods, electrofishing devices, and two special codes (27 for visual observation and 28 for dry site).
- **Bait types:** Codes 1 to 8 (Table 4), such as live bait, hot dogs, stink bait, cut bait, pellet fish food, and pet food.
- **Species codes:** Roughly 50 four-letter codes with common and scientific names (Table 5).

Station locations on SRP and FCG canals are recorded as distances in miles downstream of [[Electrical Fish Barrier]]s (SRP) or dams (FCG), to the nearest tenth of a mile (for example, 2.5).

## Ecological & Environmental Context

The guide records several sampling conventions that affect how catch data should be interpreted:

- **Fixed versus opportunistic sampling:** Records are flagged as part of the standard fixed-station program (Y) or as additional opportunistic sampling (N). Samples below the electrical fish barriers in the SRP and SRPn canals, and the entire sample in the FCG Canal, are always opportunistic. Samples between the barriers in the Aravaipa Creek are also opportunistic.
- **Electrofishing:** Gear types 7, 8, and 18 to 22 (electroshock methods) require pulse rate, voltage, amperage, water temperature (which must be between 0 and 50), and conductivity.
- **Effort calculation:** Passive gears (nets, traps, trotlines) use paired "date/time in" and "date/time out" fields to calculate effort hours automatically.
- **Age classes:** For large-bodied fish, age 0 denotes young-of-year and age 1 denotes one year old or older. Small-bodied fish are not aged.
- **Sampling timing:** Some sampling, such as on the SRPn canal, occurs in January of the year after the nominal sample year, so the sample year must be entered separately.
- **Stream habitat coverage:** For fixed-station seines and nets, the percent of habitat sampled must be recorded.

## Key Findings

**Data entry procedure**
- Data are entered in Microsoft Access, starting from the Main Switchboard's Data Entry button. Navigation uses Enter, Tab, Shift+Tab, and Ctrl+Tab.
- Only numeric codes are entered for stream, reach, station, habitat, gear, bait, and species fields. Unlisted values require contacting the database administrator.
- Date and time are entered as numeric values in a standard date format and 24-hour time (for example, 5:55 PM is entered as 17:55). Slashes and colons are added automatically.
- Each sampling effort should be entered in a separate data entry session if it involves different data types, such as fixed versus opportunistic efforts. The guide states that these sessions should not be combined.

**Field requirements by gear**
- Seines and nets (gear 1 to 13, 25, 26): mesh size, length, and depth are required. Number of hauls applies to seines and dip nets only.
- Angling (gear 14 to 17): bait type and number of hooks are required.
- Fixed-station seines and nets (gear 7 to 13, 18 to 26): percent habitat sampled is required.
- Electrofishing (gear 7, 8, 18 to 22): electroshock parameters are required.

**Catch records**
- Catch data include species, age, number of fish, number of vouchers, and comments.
- The species code 0000 indicates no fish were caught. In that case, the age field is blank and the number of fish and vouchers remain at 0. The database automatically adds "No fish captured" to the notes.
- Vouchers are fish retained for scientific purposes.
- The species list includes common sport and game fish (for example, [[Largemouth Bass]], [[Smallmouth Bass]], [[Bluegill]], [[Rainbow Trout]], and [[Channel Catfish]]), native or sensitive species (for example, [[Gila Chub]], [[Gila Topminnow]], [[Loach Minnow]], [[Desert Sucker]], and [[Sonora Sucker]]), and non-native species (for example, [[Common Carp]], [[Grass Carp]], [[Blue Tilapia]], [[Mosquitofish]], and [[Threadfin Shad]]).
- Generic codes exist for undetermined or hybrid sunfish, undetermined cichlids, undetermined frogs, and unknown fish species.

**Verification**
- Every field must be checked against the datasheet in the Data Verification form.
- The station name derived from stream, reach, and station codes must match the datasheet.
- Each record is marked VERIFIED before it is considered complete. Missing records in the Data Review form usually indicate an unchecked VERIFIED box.
- Previously verified datasheets must not be re-entered when a session is interrupted.

**Documentation gaps and inconsistencies**
- The guide says bait types run from 1 to 8, but Table 4 lists only seven types.
- Several species entries contain duplicate common names (for example, two codes for blue tilapia and two for American bullfrog) and multiple scientific name spellings, which may need reconciliation before analysis.