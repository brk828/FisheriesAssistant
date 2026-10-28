---
species: "Gila elegans (Mohave tui chub) — referenced only as an example species; no fish-specific data reported"
family: "Cyprinidae (tui chub)"
habitat: "Lower Colorado River (LCR) riparian corridor, floodplain, and associated tributaries"
ocean_basin: "N/A — freshwater riverine system (Lower Colorado River watershed; Arizona, California, Nevada)"
document_type: "Program planning / GIS methodology memo"
program: "Lower Colorado River Multi-Species Conservation Program (LCR MSCP)"
date: "November 1997"
source_id: "12191"
---

#ichthyology #marine-biology #conservation-planning #Cyprinidae #freshwater-ecology

## Executive Summary

This document is **not a primary fish biology or ecological research paper**; it is an internal planning memorandum/agenda package for the **Lower Colorado River Multi-Species Conservation Program (LCR MSCP)**, dated November 1997. It outlines the GIS data architecture, vegetation classification framework, study area boundary definitions, and — most relevant to ichthyological interest — the **criteria for selecting "target species"** to be evaluated for regulatory coverage (Section 7/Section 10 ESA compliance) under the MSCP habitat conservation plan. The only fish species explicitly named is the **Mohave tui chub** (*Siphateles bicolor mohavensis*, historically classified under *Gila*), cited as an example of a species that should be **excluded** from the target species list because it occurs primarily via secondary, off-corridor projects rather than within the core LCR study area. No morphological, physiological, or population data for any fish species are presented in the source text. The document is valuable primarily as a window into the **methodological and regulatory framework** used to structure species conservation data (including fish) along the LCR corridor.

## Background & Description

No morphological data are provided in this source. The document contains no anatomical, physiological, or taxonomic descriptions of any fish species. The only structural content resembling "characteristics" pertains to a **Species Summary Template** (see Key Findings) intended for future compilation of species-specific biological data, including a field for "Habitat and Special Considerations" — but this template is unpopulated for any species in the provided text.

## Ecological & Environmental Context

While no direct ecological data on fish are given, the document defines the **spatial and habitat framework** within which fish species' ecological niches would eventually be assessed under the MSCP:

- **Study Area Structure**: A tiered spatial hierarchy — **Watershed** (1:250,000 scale, tri-state LCR watershed context) → **River** (1:24,000 scale, ~30 km buffer along the LCR mainstem, 190 USGS quads) → **Site-Specific/Reach** (1:2,400 scale, parcel-level detail) — used to characterize habitat at increasing resolution.
- **Reach-Based Data Integration**: Multi-disciplinary data (flow, sediment type, ownership, riparian vegetation) are summarized by river "reach" to allow integrated queries such as habitat suitability by flow regime and substrate — directly relevant to defining aquatic/riparian niches for covered fish species.
- **Vegetation Classification**: A hierarchical riparian/upland vegetation classification (using **Anderson and Ohmart structural types** at the site-specific level) is intended to serve as a habitat proxy for species distribution modeling, including for aquatic and riparian-dependent species.
- **Mohave Tui Chub Exclusion**: Explicitly cited as occurring in habitats associated with **secondary projects outside the defined LCR study area boundary**, illustrating how the corridor-focused scope of the MSCP could exclude range-restricted or isolated freshwater fish populations from coverage despite their conservation significance elsewhere in the region. This exemplifies the tension between corridor-scale planning and the [[Isolated Population]] conservation needs of narrowly distributed freshwater fishes.
- **Habitat-Based Species Evaluation**: The plan proposes using vegetation community/habitat type as a **surrogate for actual species occurrence data** where survey data are incomplete — a methodology with direct implications for data-poor fish species in the LCR system (e.g., [[Razorback Sucker]], [[Bonytail Chub]], [[Colorado Pikeminnow]] — none directly named in this excerpt but typical LCR MSCP target taxa).

## Key Findings

- **GIS Framework**: LCR MSCP data are built in ARC/INFO (GRID, TIN, ArcView 3.0) on UNIX/SUN workstations, projected in UTM NAD83 Zone 11, with metadata standardized to FGDC requirements — establishing the technical infrastructure for all subsequent species distribution and habitat mapping in the LCR corridor.
- **Data Usability Criteria for Biological Data**: Species occurrence data must be documented with observation date, observer/author, source, and mapping scale; data from recognized species "authorities" are prioritized; recent data are weighted over historic data, though historic data remain valuable for habitat suitability baselines.
- **Target Species Selection Criteria**:
  - Must occur **within** the defined LCR study area (excludes species tied to secondary/off-corridor projects, e.g., **Mohave tui chub**, alongside non-fish examples like light-footed clapper rail and California clapper rail).
  - Must be federally/state listed, proposed for listing, or a likely near-term listing candidate.
  - Excludes transient species and species with **poorly defined distribution or life history data**, to avoid controversy that could undermine coverage decisions for better-studied species — a policy with direct relevance to data-poor LCR fish taxa.
- **Coverage Standard Debate**: Tension identified between ESA Section 7/10 "no jeopardy" standards (minimum: no net decline) versus emerging USFWS policy favoring **net benefit/recovery contribution** standards for HCP-covered species — a framework that would apply to any covered fish species in the final MSCP.
- **Species Summary Template**: A standardized format was proposed for future species accounts, requiring: legal status (federal/state), other status ratings, distribution (regional → local), habitat and special considerations (e.g., reproductive/migratory requirements), reasons for decline, current threats, and documented management needs. This template — while unpopulated here — represents the intended structure for future [[Species Account]] entries for LCR fish species such as those in [[Catostomidae]] and [[Cyprinidae]].
- **Scale Note**: The referenced scales in the source metadata (1:24,000 river-level and 1:2,400 site-specific reach-level, corresponding roughly to areas of ~11,200–112,000 acres depending on need) reflect the tiered spatial resolution used for habitat and species mapping, not fish-specific density or population metrics.

> **Note to reader**: This source contains no direct fish population counts, morphometric data, water chemistry, or habitat quality metrics. It is a planning/methodology document; substantive fish science for LCR target species (e.g., [[Razorback Sucker]], [[Bonytail Chub]], [[Mohave Tui Chub]]) would be found in the (unpopulated) Species Summary documents this memo describes, not within the memo itself.