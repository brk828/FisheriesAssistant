---
species: "Gila cypha; Gila elegans; Gila sp."
common_name: "Humpback Chub; Bonytail; Flannelmouth Sucker (native Colorado River fishes, Grand Canyon)"
family: "Cyprinidae"
habitat: "Colorado River mainstem, Little Colorado River, and tributaries in Grand Canyon; also Shinumo, Kanab, Bright Angel, and Havasu creeks, and the Paria River"
ocean_basin: "N/A"
location: "Grand Canyon, Arizona (Lees Ferry RM 0 to Lake Mead, RM 280)"
tags: [ichthyology, marine-biology, cyprinidae, grand-canyon, fisheries-database, gcfin, glen-canyon-dam]
title: "Grand Canyon fisheries integrated database draft report"
source_id: "13021"
minckley_id: "13021"
source_citation: "L. I. Brown, T. R. Hougaard, K. A. McHugh, R. A. P. D. Valdez and I. Bio/West (1995). Grand Canyon fisheries integrated database draft report. XXXXX:Bio/West, Inc. Minckley Library ID: 13021."
source_file: "13021.pdf"
text_extraction: "ocr"
---
# Grand Canyon Fisheries Integrated Database (GCFIN) Draft Report

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This draft report from [[BIO/WEST]] (Logan, UT, June 23, 1995) for the [[Glen Canyon Environmental Studies]] (GCES) program proposes a prototype **Grand Canyon Fisheries Integrated (GCFIN) Database** and a [[Geographic Information System]] (GIS) interface for native and endangered fish data. Fisheries data from six investigating groups were catalogued, their file structures compared, and integration templates drafted for six datasets. The core motivation is that data from different agencies were collected with different methods, codes and location standards, so they could not be analysed together. The report centres on [[Humpback Chub]] studies, which drive many of the objectives, and on the effects of [[Glen Canyon Dam]] operations on native fishes.

## Background & Description

**Program context.** GCES began in December 1982 to assess effects of Glen Canyon Dam operations on Grand Canyon resources. Phase I ran 1982–88 and Phase II 1988–95. The Native and Endangered Fish Studies (NEFS) component of the Draft Integrated Research Plan (DIRP) guided fisheries work.

**Scope of the database effort.** The report has three phases:
- **Phase 1 (Chapter 2):** A catalogue of databases, objectives and file specifications.
- **Phase 2 (Chapter 3):** Integration templates and translation filters.
- **Phase 3 (Chapter 4):** GIS application using B/W data.

**Participating investigators:** [[Arizona State University]] (ASU), [[U.S. Fish and Wildlife Service]] (USFWS), [[University of Arizona]] (U of A), [[Arizona Game and Fish Department]] (AGFD), Northern Arizona University (NAU), and [[BIO/WEST]] (B/W). The Navajo Natural Heritage Program was building a parallel database for the Little Colorado River.

**Target species and studies.**
- [[Humpback Chub]] (*Gila cypha*) was the focus of ASU, USFWS, AGFD and B/W work. ASU sought to quantify juvenile and adult movement and residency in the Little Colorado River, and basic reproductive biology.
- Other native species named include [[Bonytail]] (*Gila elegans*) and [[Flannelmouth Sucker]]. Historical records were kept for *Gila* sp.
- Non-native fishes were studied for interactions with natives, particularly piscivorous species that prey on young natives (B/W Hualapai studies).

**Study areas.** B/W's mainstem humpback chub study ran from Lees Ferry (RM 0) to Diamond Creek (RM 226). Its Hualapai study ran from National Canyon (RM 166.4) to below Pierce Ferry at Lake Mead (RM 280).

**Database inventory (Chapter 2).** Each investigator's database was described by software, file names, record counts, record lengths and anticipated sizes:
- **ASU:** three flat ASCII files, one per year (1991–1993), about 9,120–10,151 records each. Stored on an IBM 3090 mainframe; analysed in SAS.
- **USFWS:** incorporation pending.
- **U of A:** incorporation pending; no file structures available.
- **AGFD:** dBASE IV/FoxPro files. The Little Colorado River set has about 20 files (e.g., MASTERFC.DBF, 20,982 records). The mainstem set has about 10 files (e.g., FISH_ALL.DBF, 19,323 records).
- **B/W:** dBASE IV files. The mainstem set has 16 files (e.g., FISH.DBF, 26,542 records; DATASOND.DBF, 43,586 records). The Hualapai set has 7 files.
- **Past collections:** eight dBASE files (e.g., MILLER.DBF, R.R. Miller *Gila* morphometric/meristic data from the 1940s).

## Ecological & Environmental Context

**Historical record.** The earliest fish evidence came from skeletal remains in about 4,000-year-old flood deposits in Stanton's Cave (RM 31.5). Cultural remains at Catclaw Cave date to about 1100 A.D. Major John Wesley Powell (1869) did not describe the fish. The first written description was of "bony tail" by Ellsworth and Emery Kolb in 1908. Table 2-6 summarises 30-odd historical records. Most are reported occurrences; a few are complete data sets or museum specimens.

**Water quality parameters.** Instruments (Hydrolab Datasonde, Surveyor, secchi discs, turbidimeters) measure temperature, conductivity, dissolved oxygen, pH, oxidation–reduction potential, salinity and turbidity. These are the parameters linked to fish condition and occurrence.

**Habitat and invertebrates.** Habitat is classified by channel type (mainstem, side channel, tributary), hydraulic type (eddy, run, riffle, pool, backwater) and shoreline type (sand, vegetation, cobble). Invertebrate and food-base sampling used benthos, drift and zooplankton methods, and algal chlorophyll analyses.

**Parasites.** Discovery of an Asian tapeworm in several Grand Canyon fish species made parasite monitoring a priority for humpback chub.

**Location standards.** Sites are referenced by USFWS transect codes (Little Colorado River), meters from the tributary mouth, or river miles from [[Belknap River Guide]] and [[Stevens River Guide]] standards. Different river mile standards are not exactly compatible.

## Key Findings

**1. Compatibility of data fields.**
- Water quality and fish capture data are largely compatible after numeric format translation. The main differences are field length and decimal places.
- Morphometric data are compatible in many fields, but some measurements, such as body depth, are not. Miller's body depth was taken over the pectoral insertion, while B/W measured maximum depth. Miller's caudal peduncle measurement point is undocumented.
- Drift and food habits data are hard to compare. AGFD uses a multiple-record format (one row per taxon and life stage). B/W uses a single-record format (taxon and life stage encoded in field names such as SIMADU).
- Fish sampling data were the least similar, but were kept for integration because of their analytical importance (catch-per-effort).

**2. Location is the main integration problem.** Location fields cannot be combined by simple translation. The report recommends four standard fields: river, river mile, tributary meters, and side of river (facing downstream). It recommends a user-selectable river mile standard, and a river mile equivalency table.

**3. Recommended file structure.** Single-record formats suit CPE analysis but become unwieldy for many taxa. Multiple-record formats are space-efficient for sparse data. Relational formats minimise redundancy but are harder for novices. The report recommends a flexible user interface that builds files on demand, rather than one fixed structure.

**4. Relational links.** Linking fields include DATE, TIME, RM, INVESTIGTR, TAG_NUM and KEY (a composite of TYPE+TRIP+SAMPLE_NUM+REACH+CLIPBOARD). The AGFD mainstem files share a STUDY field for linking.

**5. GIS as the integrating tool.** Geography was identified as the common element linking all DIRP components. Using [[ArcView]] 2.0 (released 1994), B/W tabular dBASE data were joined to geographic data via link items (such as NET_ID and MNTRP_ID) without altering the source files. Abstract river-mile referencing was linked to a river centerline route. The report defines six levels of geographic accuracy, from surveyed (sub-centimetre) to historical.

**6. Recommendations.**
- *Immediate:* gather outstanding databases and documentation; compile user needs; develop a river mile equivalency table; generate calibrated river centerlines for each agency; map other agencies' geographic information.
- *Eventual:* develop a user interface (ArcView or Paradox/dBASE for Windows); adopt a standard data storage protocol modelled on the Upper Colorado River Basin Database (USFWS 1989); set a data collection protocol with quality control; require metadata; and build a Colorado River geographic referencing system based on stream segment identifiers (the Washington State model), using EPA Reach File 3 as a starting point.

**7. Limitations.** The report notes that data and documentation were incomplete at the time: USFWS and U of A incorporation was pending, U of A file structures were unavailable, and some past-collection methods were undocumented. The GIS interface for the full GCFIN database was yet to be built and tested.