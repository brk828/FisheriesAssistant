---
species:
  - Agosia chrysogaster
  - Catostomus insignis
  - Catostomus latipinnis
  - Cottus bairdii
  - Crenichthys baileyi
  - Cyprinodon macularius
  - Gila cypha
  - Gila elegans
  - Gila intermedia
  - Gila nigra
  - Gila robusta
  - Gila seminuda
  - Lepidomeda mollispinis
  - Meda fulgida
  - Moapa coriacea
  - Oncorhynchus apache
  - Oncorhynchus gilae
  - Plagopterus argentissimus
  - Poeciliopsis occidentalis
  - Ptychocheilus lucius
  - Rhinichthys osculus
  - Tiaroga cobitis
  - Xyrauchen texanus
  - "31 native fishes and 49 exotic species (full lists in Appendix 1)"
common_name:
  - Longfin dace
  - Sonoran sucker
  - Flannelmouth sucker
  - Mottled sculpin
  - Springfish
  - Desert pupfish
  - Humpback chub
  - Bonytail chub
  - Gila chub
  - Headwater chub
  - Roundtail chub
  - Virgin River chub
  - Virgin River spinedace
  - Spikedace
  - Moapa dace
  - Apache trout
  - Gila trout
  - Woundfin
  - Gila topminnow
  - Colorado pikeminnow
  - Speckled dace
  - Loach minnow
  - Razorback sucker
family: "Cyprinidae, Catostomidae, Cottidae, Cyprinodontidae, Poeciliidae, Salmonidae, Cyprinidae (multiple families)"
habitat: Freshwater rivers, streams, springs, canals and reservoirs
ocean_basin: N/A
location: Lower Colorado River Basin, southwestern USA and northwestern Mexico (Great Basin and New Mexico partially covered in point database only)
tags:
  - ichthyology
  - marine-biology
  - freshwater-fish
  - gis
  - biogeography
  - conservation
  - data-manual
title: "GIS Manual for use with the Lower Colorado Basin Fish Database"
source_id: "PML2551"
marsh_id: "PML2551"
library: "Marsh Library"
permission: "public domain"
source_citation: "P. J. Unmack (2002). GIS Manual for use with the Lower Colorado Basin Fish Database. Arizona State University, Biology Department. Marsh Library ID: PML2551."
source_file: "Unmack. 2002. ASU GIS manual for Lower Colorado Basin fish database.pdf"
text_extraction: "text"
---
# Arizona State University GIS Manual for the Lower Colorado Basin Fish Database

#ichthyology #marine-biology #freshwater-fish

## Executive Summary

This manual, authored by [[Peter J. Unmack]] of Arizona State University and dated May 2002, documents a [[GIS Database]] of western North American fishes begun in 1994 by [[W.L. Minckley]]. It describes two products: a point database of almost 36,000 individual native and introduced fish records, and a user-friendly [[Summary Database]] summarizing occurrence by watershed and river reach for the [[Lower Colorado River Basin]]. The document covers data sources, completeness, errors, geographic coverage, field definitions, and step-by-step instructions for using the shapefile in [[ArcView]] 3.x, including two worked examples on creating derived conservation fields. Funding came from the [[US Bureau of Reclamation]] and the [[US Fish and Wildlife Service]].

## Background & Description

The project was initiated to integrate existing data on southwestern fishes into one resource for studying decline, conservation priorities, biogeography, ecology and evolution. It began in 1994 with support from American Rivers to examine the [[Gila River Basin]], then expanded to most of the Lower Colorado Basin. A graduate student, Heidi Blasius, built a database for northwestern Mexican drainages. Contributors included American Rivers, the Bureau of Reclamation, the US Forest Service, the US Fish and Wildlife Service and the National Science Foundation (1994–2002).

Data sources were:
- Museum specimens from roughly two dozen institutions, including [[Arizona State University]] and the [[University of Arizona]]
- Primary literature (Appendix 2 lists the works included; the list spans the 1861–1992 period)
- Gray literature (agency reports and memos, only a fraction of available items)
- The [[Arizona Game and Fish Department]] Non-Game Fish Branch database (as of mid-1999)

Database completeness: over 99% of museum records were incorporated. Little primary literature after 1973 was included, though this likely represents only a few unique records. Errors may arise from misidentification, data manipulation, and digitizing. Points were digitized from 1:250,000 USGS topographic maps, and most fall within 1 km of their true locality.

Nine archaeological records (Miller 1955; Minckley & Alger 1968) are included. Native fish reintroductions are excluded. Several native records absent from the point database were added directly to the summary database (Table 1, 11 records). Introduced-fish records with incomplete or hybrid identifications were reassigned to the most common species in their genus (Table 2).

## Ecological & Environmental Context

Watersheds in the summary database were delineated somewhat arbitrarily: small catchments with many native records were split, while areas with few records were merged, balancing manageability against spatial resolution. Native records span 1840–2001; current records span 1981–2001, with exceptions for [[Apache Trout]] (2001 only) and [[Gila Trout]] (1999–2001).

Geographic coverage:
- The point database focuses on the Lower Colorado Basin (excluding the [[Salton Sea]]) and northwestern Mexican drainages from the Mayo River north. Both are considered largely complete.
- The Great Basin and New Mexico are only partially covered and were excluded from the summary release.
- The summary database covers the entire Lower Colorado Basin except the Salton Sea.

The point database holds 19,369 native and 16,339 exotic fish records for the Lower Colorado Basin. Perennial stream and land-use layers from the [[Arizona Land Resources Information System]] are approximate only and considered inaccurate or incomplete.

Derived conservation metrics use these fields: total native richness, present richness, threatened richness, percentage threatened, absolute and percentage decline, and total exotic richness. Threatened status is a broad, unofficial designation reflecting perceived current risk rather than any formal list.

## Key Findings

- **Dataset scale:** The point database contains nearly 36,000 records. The summary dataset uses watersheds as its unit of analysis.
- **Native fauna:** 31 native fishes are recorded in the Lower Colorado Basin from 1840–2001, and 28 remain extant in 1981–2001. Summary fields include [[Total Native Richness]], [[Present Native Richness]], and [[Percentage Decline]].
- **Exotic fauna:** 49 exotic species remain present in the basin. The summary field "Total exot" sums them per watershed.
- **Museum coverage:** Over 99% of museum records were included. Literature coverage is weaker, especially after 1973.
- **Known gaps:** Many widespread species are probably underrepresented. Federally listed species are said to have complete, current coverage.
- **Conservation example 1:** A derived field distinguishes watersheds with no [[Longfin Dace]] records (0), historical-only records (1), and present-day records (2).
- **Conservation example 2:** A priority field combines fauna intactness with percentage of threatened species. Codes range from 9999 (no native fishes recorded) and -1 (extirpated) through 0–21, with higher codes indicating more threatened species and a non-intact fauna.
- **Limitations:** The author stresses that errors are possible, requests reports of mistakes, and notes that projection changes require ArcInfo.
- **Usage:** The shapefile must be used with ArcView 3.x. Exported .dbf tables should be saved in a separate directory to prevent corruption of the shapefile.