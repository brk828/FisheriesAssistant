---
species: N/A
common_name: N/A
family: N/A
habitat: Riverine and levee sites (per handwritten notes, uncertain)
ocean_basin: N/A
location: N/A (a "Cibola Revisited" label appears, unverified)
tags: [ichthyology, marine-biology, fish-field-survey, circular-statistics]
title: "Scanned Field Notebook Pages and Circular Statistics Lecture (Largely Illegible)"
source_id: "PML2771"
marsh_id: "PML2771"
library: "Marsh Library"
permission: "not public domain"
source_citation: "USGS (2003). Scanned Field Notebook Pages and Circular Statistics Lecture (Largely Illegible). Marsh Library ID: PML2771."
source_file: "USGS 2003. Ciabola HCP telemtry .pdf"
text_extraction: "mixed"
---
# Scanned Field Notebook Pages and Circular Statistics Lecture (Largely Illegible)

#ichthyology #marine-biology #fish-field-survey

## Executive Summary

This document is a scanned bundle of mostly handwritten field-notebook pages, plus a printed lecture on circular statistics (Robson, Alford & Jones, *Lecture Notes 2004*, Lecture 35, "When the world is circular..."). Most handwritten pages are too degraded to transcribe reliably. Legible fragments suggest fish tag-and-count records, organised by tag ID, size class and [[Quadrant Sampling|quadrant]] tallies, with site notes mentioning levees, rivers and lakes. The only fully legible scientific content is the lecture, which covers the analysis of angular data and works through a four-angle example. No species identities, habitat measurements or population estimates can be confirmed from the text.

## Background & Description

**Field notebook pages (approx. 60+ scans).** Many pages carry handwritten tag numbers (e.g., Tag 246, 333, 345, 357, 364, 375, 444, 555, 666) with columns of size classes (e.g., "2-3", "4-5", "6-7", "8-10") and per-quadrant counts. Several pages are headed "Fish.shp", suggesting a shapefile or GIS-linked fish dataset. The site descriptions use terms such as "levee", "river", "lake", "pool" and "Movin' around", but the place names are largely unreadable.

**Lecture notes (approx. pp. 137–150).** A teaching sequence on [[Circular Statistics]]. It covers:
- The distinction between linear and circular measurements (compass bearings, angles, times of day and year).
- Plotting methods: [[Circular Scatterplot]], [[Circular Histogram]] and [[Radar Plot]], with guidance that scatterplots suit small samples (roughly fewer than 50) and histograms or radar plots suit large ones.
- Descriptive statistics: mean angle, [[Mean Vector Length]] (a measure of concentration), and [[Angular Variance]] and [[Angular Deviation]], which are analogous to linear variance and standard deviation.
- Inferential tests: [[Rayleigh Test]] for significant mean direction, and [[Watson-Williams Test]] for comparing mean angles across two or more samples. For large samples, a chi-square homogeneity test is suggested.
- Sources: [[Zar Biostatistical Analysis]] (chapters 26–27) and Batschelet's [[Batschelet Angular Variance]] formula.

## Ecological & Environmental Context

The notebook pages suggest a repeated field survey in which individually tagged animals were counted and sorted by size class across sampling quadrants. The text does not state the species, the water body, the sampling dates, the gear or the sampling design, so no ecological inference is supported beyond this. The lecture's circular methods could apply to directional data in such work (e.g., movement bearings or orientation of fish), but the document does not link them to any fish dataset.

## Key Findings

- **Worked example (lecture).** Four angles are analysed: 30°, 90°, 330° and 60°.
  - Sum of sines = 1.866; sum of cosines = 2.232.
  - Mean sine = 0.467; mean cosine = 0.558.
  - Mean vector length *r* = 0.728 (the lecture gives √0.529 ≈ 0.728).
  - Mean angle ≈ 40.0°, calculated as sin(α) = 0.641 and cos(α) = 0.766.
- **Method emphasis.** The lecture stresses that the mean angle is meaningless if directions are uniformly distributed over 360°, and that variance and deviation vary inversely with *r*.
- **Notebook tallies (OCR uncertain).** One "Fish.shp" page lists quadrant counts of approximately Q1 = 211, Q2 = 17 and Q4 = 25. Other pages give similar per-quadrant tallies, but the digits are often illegible.
- **Size classes.** Several pages use recurring size-class bins (e.g., 1–2, 3–6, 7–13, 14–23 for one page), which may reflect a length-frequency protocol, but the units are not stated.
- **Data limitations.** Species, measurement units, dates, site names and sampling effort cannot be verified from the scans. Any quantitative claim about fish abundance or distribution would be speculative.