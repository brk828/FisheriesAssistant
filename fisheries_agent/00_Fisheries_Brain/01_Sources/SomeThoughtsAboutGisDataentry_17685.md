---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Pacific Southwest Region, USDA Forest Service (USA)
tags: [gis, data-entry, forest-service, cartography, geospatial-data]
title: "Some thoughts about GIS data-entry"
source_id: "17685"
minckley_id: "17685"
source_citation: "D. A. Blakeman (1987). Some thoughts about GIS data-entry. In: Proceedings of the Proceedings of Second Annual International Conference, Exhibits and Workshops on Geographic Information Systems, 1987. San Francisco, Vol. 1. Place Published: American Society for Photogrammetry and Remote Sensing, 226-233. Minckley Library ID: 17685."
source_file: "17685.pdf"
text_extraction: "ocr"
---
# Some Thoughts About GIS Data-Entry

#gis #data-entry #forest-service

## Executive Summary

This essay by David A. Plakeman, a resource specialist with the [[Forest Service]] [[Pacific Southwest Region]], argues that the [[Geographic Information System]] (GIS) industry has stayed with costly [[Manual Digitizer]] data entry for too long. Plakeman states that data entry accounts for about 80% of the cost of purchasing, implementing and running a GIS, and he contends that [[Automated Scanning]] would remove this barrier and widen access to GIS. He supports the claim with the Region's own production experience using [[Wildland Resource Information System]] (WRIS) and its successor [[DWRIS87]]. The document is an opinion piece with no aquatic, ecological or species data.

## Background & Description

The author describes a 1980s GIS landscape in which vendors emphasize graphics output while data entry remains manual and expensive. He observed a commercial manual digitizing installation that relied on roughly 150 programs, which he regards as a piecemeal approach rather than sound systems design.

The essay has three main parts:
- **Critique of industry attitudes:** the author argues that industry clients accept four fallacies:
  1. Maps can be hand-digitized as easily as they can be drawn.
  2. Scanners are too expensive.
  3. Scanners suit only large users.
  4. Manual digitizers suit routine, day-to-day work.
- **Technical explanation:** data entry converts analog maps to digital form through [[Rasterization]], which can be performed by a person (manual digitizing) or by a computer (scanning).
- **Historical account of Region 5 systems:** the Region's GIS history, from the early WRIS to DWRIS87, and its production throughput.

The author also states that manual digitizing is "a draconian task" and that the industry's reluctance to automate is puzzling.

## Ecological & Environmental Context

The document does not address ecology, aquatic habitats, species or water chemistry. Its environmental context is land management. It covers the [[Forest Service]] planning process, in which resource specialists prepare thematic maps (timber stand or vegetation maps, soil maps, land status and administrative constraints) for forest management decisions. The maps used are typically [[USGS Quadrangle]] sheets at 1:24,000 scale. Examples given include the [[Stanislaus National Forest]] (first production run in 1971, for a timber inventory and management plan) and a vegetation layer on a Region 5 national forest.

## Key Findings

**Cost and industry claims**
- Data entry is cited as about 80% of the total cost of GIS purchase, implementation and operation. The author calls this a figure that "has been floating around for years."
- Scanners were reported to range from about $200 to as much as $1,000,000, with several models around $2,000, several near $10,000, and others between $10,000 and $20,000.
- The author estimates that the savings from scanning would have paid for a scanner several times over in the last fifteen years, at least for large federal or state users.
- Hand-digitizing a vegetation layer on one forest in a six-month period was cited as costing $250,000. The author argues that updating the same layer over ten years would cost more, because setup overhead repeats with each partial update.

**Technical contrasts**
- A manual digitizer captures vectors directly but makes editing and overlay slower. Vector overlay on a [[Univac 1100]] took twenty minutes to an hour or more, while raster overlay on a super-minicomputer took about two minutes.
- Vector overlay introduces more sliver artifacts than raster overlay because of point thinning.
- A scanner processes all maps of the same size in roughly the same time regardless of complexity, whereas manual digitizing time grows with the number of features.
- Automated scanning requires a more careful, up-front system design, including a deliberate [[Vectorization]] scheme and data structure.

**Scanning method (WRIS/DWRIS87)**
- Maps are photographically reduced (typically 10x) to a 4" x 6" negative, producing an image of about 1.75" x 2.5" (44 mm x 59 mm).
- The scanner uses a diode array with a sampling spot of 16 to 60 microns. At 50-micron pixels, a 10x-reduced quadrangle yields about 1,200 x 900 pixels.
- Density values range over 256 grey levels (0 to 255). A frequency distribution is bimodal, and a threshold between the two modes is chosen per batch of negatives to produce a binary line/background map (see [[Binary Thresholding]]).
- Post-scan steps include interactive editing, automatic gap closing, thinning lines to one bit, vectorizing, polygon extraction and labeling, then overlay and analysis.

**Historical performance**
- 1971: the PSW station introduced a [[Microdensitometer]] for automated map conversion.
- 1974: the microdensitometer took 9 to 13 hours per map. A scanning drum microdensitometer reduced this to 5 to 20 minutes.
- 1982: a faster scanner brought scan time to 1 to 2 minutes.

**Typical DWRIS87 operation times for an 800-polygon map (wall-clock, varying with computer load)**
- Scanning: 2 to 4 minutes
- Editing: 15 to 30 minutes
- Vectorization: 9 to 20 minutes
- Calculations: 12 to 30 minutes
- Overlay: 2 to 4 minutes

**Throughput**
- In its first production run of the latest WRIS version, one person with some peripheral help scanned and edited 119 vegetation maps in fourteen working days. Maps averaged 500 polygons, ranging from 10 or 20 to 1,100 or 1,200. The author states that the system is now menu-driven and could be faster.

**Recommendations and conclusions**
- The Region is seeking a low-cost scanner for each forest and district, and plans to scan full-size maps without the negative reduction step. The author notes that earlier scanners could not accept full quadrangle sizes, and that the negatives were stored centrally for future reference.
- The author argues that the [[Forest Service]] must decide whether required GIS technology is available commercially or must be developed in-house or by contract.
- He concludes that automated data entry is essential for the Service as a whole, since manual entry would cost "hundreds of millions of dollars."
- He describes manual digitizing as an "outmoded" method and says that a mature GIS industry cannot rely on it.