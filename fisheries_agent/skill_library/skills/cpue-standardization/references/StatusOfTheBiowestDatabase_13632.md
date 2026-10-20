---
species: "Gila cypha"
common_name: "Humpback Chub"
family: "Cyprinidae"
habitat: "Colorado River mainstem, eddies, shorelines, tributary confluences"
ocean_basin: "N/A"
location: "Grand Canyon, Colorado River, Lees Ferry (RM 0) to Diamond Creek (RM 226), Arizona, USA"
tags: [database, GCES, Glen_Canyon_Dam, endangered_species, radiotelemetry, life_history, population_monitoring]
title: "Status of the Bio/West database"
source_id: "13632"
minckley_id: "13632"
source_citation: "R. A. Valdez (1993). Status of the Bio/West database. Minckley Library ID: 13632."
source_file: "13632.pdf"
text_extraction: "ocr"
---
# BIO/WEST Grand Canyon Database Status Report

#ichthyology #cyprinidae #endangered-species #database-management #Grand-Canyon

## Executive Summary

This document describes the comprehensive database structure developed by BIO/WEST, Inc. for the [[Glen Canyon Environmental Studies]] (GCES) investigation of [[Humpback Chub]] (*Gila cypha*) in [[Grand Canyon]]. The database encompasses 36 monthly field trips from October 1990 through November 1993, documenting fish biology, habitat relationships, and environmental conditions in the [[Colorado River]] mainstem between [[Lees Ferry]] (RM 0) and [[Diamond Creek]] (RM 226). The database is organized into seven major datasets stored in dBASE IV format, with provisional data availability scheduled for December 20, 1993, and final archival data upon completion of the Final Report in October 1994.

## Background & Description

The BIO/WEST fishery investigation was conducted under Bureau of Reclamation Contract No. 0-CS-40-09110 to characterize the life history and ecology of the endangered [[Humpback Chub]] as affected by [[Glen Canyon Dam]] operations. The investigation was coordinated with the [[Glen Canyon Environmental Studies]] (GCES) and directed by the Aquatic Coordination Team (ACT). BIO/WEST's responsibilities included sampling adults, juveniles, and young fish in all mainstem habitats except backwaters (sampled by [[Arizona Game and Fish Department]]). Additional sampling was extended downstream of [[Diamond Creek]] in June 1992 through an Aquatic Resources Investigation for the [[Hualapai Indian Tribe]].

The database design reflects 10 years of collective experience by BIO/WEST biologists and is structured to be compatible with the [[Upper Colorado River Basin Recovery Implementation Program]] database. Data structures are field-specific and optimized for computerization from standardized field data sheets. The database is stored and analyzed primarily in dBASE IV, version 2.0, with data transferable to other software through direct export or ASCII format.

## Ecological & Environmental Context

The study area encompasses the [[Colorado River]] corridor through [[Grand Canyon]], a system dramatically altered by [[Glen Canyon Dam]] operations. The investigation addresses how dam-controlled flow regimes affect the endangered [[Humpback Chub]] population, including impacts on habitat availability, food resources, movement patterns, and population demographics. The database captures relationships between fish populations and multiple environmental variables including flow stage, water temperature, turbidity, habitat type (runs, riffles, pools, eddy return channels, rapids), substrate composition, and invertebrate drift.

Water quality monitoring included continuous recording at strategic locations using dataloggers (Datasonde) and periodic field measurements (Hydrolab Surveyor2) documenting temperature, pH, conductivity, and dissolved oxygen. Habitat mapping at six study areas documented surficial area of macrohabitats across flow ranges from approximately 4,000 to 16,300 cfs. Superhydro bathymetry surveys provided detailed depth and velocity isopleths for selected eddy complexes used by adult [[Humpback Chub]].

## Key Findings

**Database Structure and Content:**

The BIO/WEST [[Grand Canyon]] Database comprises seven major datasets:

1. **Fish and Drift Samples Dataset** - Four file structures (Net/Trap, Electrofishing, Seine, Drift Net) containing 36 monthly trip files per gear type, aggregated annually. Each record documents catch per unit effort, species composition by age class (YOY, juvenile, adult), habitat conditions, water quality, and weather. Drift net files contain invertebrate densities and dry weight volume of drift material (primarily *Cladophora glomerata*).

2. **Fish Statistics Dataset** - Four file structures documenting individual fish data: (a) Individual Fish Statistics files containing length, weight, PIT tag numbers, sex, ripeness, capture/release locations for all native fish and key non-native species; (b) Chub Meristics files with detailed morphological measurements (nuchal depth, caudal peduncle dimensions, ray counts) linked to photographs and video footage; (c) Stomach Analysis files (FISHFOOD.dbf) containing food item counts by taxon for 296 fish stomachs; (d) Scale Aging files (SCALES.dbf) with 91 records of scale radius, annular ring measurements, and backcalculated lengths for [[Humpback Chub]] less than 200 mm TL.

3. **Radiotelemetry Dataset** - Three file structures tracking adult [[Humpback Chub]] movements: (a) Observations files documenting movement in meters during 24-72 hour intensive tracking periods; (b) Surveillance files recording locations (0.05 river mile precision) during periodic day/night/crepuscular surveys; (c) Remote Telemetry files from three automated stations (KILR, KLCR, KRSH) recording radio frequencies to detect fish movement near [[Little Colorado River]] confluence and surface occurrence (signal extinction at approximately 4 m depth).

4. **Fish Habitat Dataset** - Three components: (a) Juvenile Habitat files (JUVHAB.DBF) with 282 records containing depth, velocity, substrate measurements from ten transects along four shoreline types (talus, sand, vegetated cutbank, vertical cliff); (b) Stage Flow Habitat Mapping GIS files digitized from acetate overlays on 1:1200 aerial photographs at six study areas (~400 m each) across flow ranges; (c) Superhydro Bathymetry files providing depth and velocity isopleths for four eddy complexes (RM 58.5, 60.1, 60.8, 64.7).

5. **Water Quality Dataset** - Two file structures: (a) Datasonde files from continuous recording dataloggers at strategic locations documenting temperature, pH, conductivity, dissolved oxygen at 0.5-hour intervals; (b) Surveyor2 files from periodic Hydrolab measurements at camp locations and selected sites.

6. **Photographic Records** - 35mm color slides and VHS video documenting individual [[Humpback Chub]] morphology (left lateral view on labeled grid board), suspected [[Razorback Sucker]] specimens, sampling activities, fish habitat, and conditions. Includes panoramic photo sets (6-8 frames) from established shoreline points during flow stage habitat mapping. A Microtech Scanner is being tested for digitizing images.

7. **Log Books and Data Sheets** - Senior Field Biologist log books providing written records of activities, sampling conditions, and clarifications; Surveyor2 and remote telemetry station logs documenting sampling conditions and identifying aberrant observations; original formatted field data sheets stored in fireproof filing cabinet as permanent legal record.

**Data Management and Quality Control:**

Provisional data undergo computerization and electronic checking for accuracy and consistency. Final archival data will be produced after complete analyses for the Final Report, as data analyses typically reveal relational problems undetected by initial checking. The database uses standardized eight-digit alphanumeric file naming (Project_Year_Trip_GearType.suffix) with annual aggregate files used for analyses. Original trip files are archived but not used in analyses. Multiple links exist between data files relating field-specific data (e.g., Net/Trap files link to Individual Fish Statistics files).

**Biological and Habitat Relationships Captured:**

The integrated database structure enables analyses of: population abundance and distribution; individual length-weight relationships, growth rates, and condition factors; mark-recapture movement patterns; habitat use patterns by life stage; sex ratios and reproductive condition; food habits and availability of drifting invertebrates; morphological characterization of the [[Grand Canyon]] [[Humpback Chub]] population; identification of environmental variables affecting population demographics; flow-to-habitat relationships; and eddy complex morphology changes over time.