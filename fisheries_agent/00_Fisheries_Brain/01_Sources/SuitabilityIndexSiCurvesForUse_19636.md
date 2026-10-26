---
species: [Ptychocheilus lucius, Gila cypha]
common_name: [Colorado squawfish, Humpback chub]
family: Cyprinidae
habitat: Freshwater riverine (large river channels, backwaters, deep canyon reaches)
ocean_basin: N/A
location: Colorado River Basin, USA (Colorado, Green, Yampa, and White rivers)
tags: [ichthyology, cyprinidae, instream-flow, habitat-suitability, endangered-species]
title: "Suitability Index (SI) curves for use in the instream flow imcremental methodology"
source_id: "19636"
minckley_id: "19636"
source_citation: "P. C. Nelson (1984). Suitability Index (SI) curves for use in the instream flow imcremental methodology. . Minckley Library ID: 19636."
source_file: "19636.pdf"
text_extraction: "ocr"
---
# Suitability Index Curves for the Instream Flow Incremental Methodology

#ichthyology #marine-biology #cyprinidae

## Executive Summary

This document combines two U.S. Fish and Wildlife Service products. The first is a 1984 working paper by Patrick C. Nelson that explains how [[Suitability Index Curves]] (SI curves) are built, used, and documented in the [[Instream Flow Incremental Methodology]] (IFIM). The second is a November 1984 compilation of habitat utilization curves for endangered fishes of the upper [[Colorado River]] Basin, mainly [[Colorado Squawfish]] and [[Humpback Chub]]. Together they set out a standard method for turning field observations of fish microhabitat into quantitative habitat indices that flow models can use.

## Background & Description

**Purpose of SI curves.** SI curves are graphs that show the relative suitability (0 to 1.0) of a habitat variable for a fish species. They are a core input to the [[Physical Habitat Simulation System]] (PHABSIM), the main component of IFIM, and also to Habitat Suitability Index models. In PHABSIM, curves are stored as x,y coordinate pairs and interpolated by the computer.

**Variables.** Microhabitat variables are water velocity, depth, substrate, and cover. These define the living space available at a given flow. Macrohabitat variables include water quality, food supply, and associated fish species. Any variable that affects growth, survival, reproduction, or population density is treated as important.

**Curve types.**
- [[Habitat Utilization Curves]] are built from observed fish locations, shown as frequency histograms. They may not transfer between streams because habitat use varies with space, time, activity, and associated species.
- [[Habitat Preference Curves]] are utilization curves with habitat availability removed. In theory they apply to all streams, but the paper notes that existing techniques for building them are "suspect."

**Sources for curves.** Curves can come from scientific literature, expert opinion, or field data. The paper gives a brown trout example from 235 observations in Spruce Creek.

## Ecological & Environmental Context

**Field methods.** Fish locations should be measured at the exact point where each fish was seen. Velocity is taken at 0.6 depth for mean column velocity, or at 0.2 and 0.8 depth for water deeper than 2.5 ft. Nose velocity is measured at the fish's position. Substrate and cover are characterized in a circle or quadrat centered on each fish. Recommended methods include snorkeling, SCUBA, wading, and electroshocking, with seining or [[Radio Telemetry]] for low-clarity water.

**Habitat availability.** Availability is sampled using systematic or random grids, cell-based measurement, or stream mapping, ideally at the same time as utilization sampling.

**Sample size.** The paper states that 150 to 200 observations are "necessary in most cases" for stable curves.

**Documentation.** Each curve set should include the investigator's details, study purpose, dates and times of sampling, methods and assumptions, site conditions (water quality, food, associated species, width, discharge, and availability of velocity, depth, substrate, and cover), and target-species life stage and activity definitions.

**Example calculations (illustrative).**
- Composite suitability index: CSI = 0.6 × 0.3 × 1.0 × 0.2 = 0.036.
- Cell weighted usable area: 0.036 × 50 ft² = 1.8 ft².
- Total habitat: 600 ft² × 0.5 × 1.0 = 300 ft².

The paper stresses that WUA and total habitat are relative indices only.

## Key Findings

### General method (Nelson 1984)
- SI curves are most useful when target species, life stage, season, activity, and associated species are defined before fieldwork.
- Utilization and availability data should be collected together and kept separate by life stage, season, activity, and stream where appropriate.
- Curves may be normalized to 1.0 and reported with equations, standard errors, and x,y coordinate pairs.
- Histograms can represent categorical variables such as substrate and cover.

### Colorado squawfish (endangered)
Curves were built from Colorado, Green, Yampa, and White River captures and radio telemetry, mostly 1979–1984. Each curve has explicit data-inclusion rules, assumptions, and constraints.

- **Nonspawning adult depth (1 Sep–30 Apr):** Suitability is near zero below about 2.95 ft and reaches 1.0 at 2.95 ft and deeper. Depth above 2.95 ft is treated as non-limiting.
- **Nonspawning adult velocity:** Mean column velocity was doubled to match modeled hydraulic velocities, because microhabitat velocities used by the fish are "only about 1/2" of the cell mean column velocity. The curve peaks (SI 1.0) from about 0.2 to 2.0 fps.
- **Spawning (staging) depth, Yampa River RM 4–31 (1 Jul–31 Aug):** SI 0.0 at 2.0 ft, 1.0 at 5.0 ft and deeper, based on deep runs and eddies.
- **Spawning (staging) velocity, Yampa River RM 16.4:** Optimum velocity ranges from about 1.2 to 2.6 fps (SI 1.0), with SI 0.75 at 0.5 fps. Values come from a hydraulic model, not direct measurements.
- **Spawning (deposition) depth and velocity:** Curves were developed for cobble bars and gravel/cobble spawning reaches (RM 4–31 and RM 16.4). Spawning deposition depth was limited to waters less than 5.5 ft deep.
- **Spawning substrate:** Not developed for staging. Substrate codes for deposition range from 1 (silt and clay) to 6 (bedrock).
- **Post-larval YOY:** Strong preference for backwaters over shoreline and other habitats. Curves apply only to backwater habitats and only to models that include backwaters. Substrate SI is 1.0 for codes 1–2 and 0.05 for codes 3–4.
- **Juvenile (60–249 mm and 250–449 mm):** Depth and velocity curves come from RARE file capture data for 1979–1983. For 60–249 mm, depth SI is 1.0 at about 0.6–1.8 ft and velocity SI is 1.0 at 0.0–0.5 fps. Substrate curves are shared across both juvenile size classes.
- **Temperature:** The juvenile, adult, and YOY temperature preference curve is based on laboratory growth-temperature data from Black (1982, Utah State University). It peaks near 25 °C. Spawning migration and spawning temperature curves are tied to specific USGS gauges.
- **Prespawning temperature:** Curves were built from monthly mean temperatures at gauges on the Colorado (Stateline), Green (Jensen, Green River UT), Yampa (Maybell), and White (Ouray) Rivers. The upper limit of 32 °C is set below the critical thermal maximum of 35 °C cited from Berry et al. (1980).
- **Spawning temperature:** Optimum (SI 1.0) for the Colorado River is 22–30 °C, with absolute limits of 16–32 °C. Green River optimum is 24–26 °C (limits 20–28 °C). Yampa River optimum is 22–26 °C (limits 18–28 °C).

### Humpback chub (adult, >200 mm TL)
- **Depth:** Based on 1979–1981 Colorado River captures. Green and Yampa River data were excluded because of small sample sizes.
- **Velocity:** SI 1.0 from about 0.2 to 0.7 fps (mean column), with SI 0.5 at 0.9 fps and 0.1 at 1.6 fps. The paper warns that great depths and variable velocities may cause significant measurement error.
- **Substrate:** Codes 2 and 6 are preferred (SI 1.0). Code 1 is 0.5.
- Curves apply only to deep canyon reaches.

### Cross-cutting points
- Curves that were not developed (for example, adult Colorado squawfish nonspawning substrate and staging substrate) are explicitly justified: substrate could not be accurately characterized at depth and did not appear to be a major factor.
- Several curves are limited to the gauges, reaches, or habitat types from which they were derived.

[[Fathead Minnow]], [[Sand Shiner]], [[Brown Trout]], and [[Rainbow Trout]] appear only as worked examples in the general methods section.