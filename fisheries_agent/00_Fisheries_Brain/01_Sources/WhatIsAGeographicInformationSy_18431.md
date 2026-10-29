---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: "Western United States (Bureau of Land Management context); Fort Collins, Colorado; continental Africa and lower 49 U.S. states cited as examples"
tags: [geographic-information-systems, spatial-data-handling, resource-management, gis-technology]
title: "What is a geographic information system?"
source_id: "18431"
minckley_id: "18431"
source_citation: "H. D. Parker (n.d.). What is a geographic information system?. 72-80. Minckley Library ID: 18431."
source_file: "18431.pdf"
text_extraction: "ocr"
---
# Geographic Information Systems in Natural Resource Management: A Resource Manager's View

#geographic-information-systems #spatial-data-handling #resource-management

## Executive Summary

This is a non-research essay by H. Dennison Parker of the [[Bureau of Land Management]] (BLM) and the Department of Fishery and Wildlife Biology, [[Colorado State University]]. It argues that a [[Geographic Information System]] (GIS) is best understood as an information technology, not a single software product or a special kind of information system. The author takes the view of a resource manager rather than a cartographer. The essay covers how spatial data must be reduced to points, lines and polygons, how cadastral and geodetic referencing creates discrepancies, how [[Topology]] and the juxtaposition of habitat components relate to GIS design, and how GIS is used in BLM planning, simulation and remote sensing. It is not about fish or aquatic taxa. Aquatic features such as lakes and streams appear only as examples. The text ends with an appendix fragment describing a microcomputer GIS system.

## Background & Description

**Definition debate.** Parker notes that GIS definitions vary widely. Synonyms include "geo-base information system," "natural resource information system," "geo-data system," "spatial information system," "geographic data system," "land information system" and "geographical information system." Other authors describe it as a spatial data handling system (Marble et al., 1983), an "internally referenced, automated, spatial information system" (Berry, 1986), or "simply a device to expand the use of maps" (Devine and Field, 1986). Parker's own working definition is that a GIS is "an information technology which analyses, stores, and displays both spatial and non-spatial data."

**Multipurpose cadastre.** Parker argues that a [[Multipurpose Cadastre]] is "nothing more than a GIS containing a few highly accurate cadastral data planes." He therefore recommends keeping the term "geographic information system."

**Spatial data.** In resource management terms, [[Spatial Data]] has physical dimensions and a location on the ground. It is represented on maps as features. Parker states that spatial data occurs in three forms: points (wells, stream intersections, eagle nests), lines (rivers, roads) and polygons or areas (soil types, forest stands). A street address is a label attached to a land parcel, and the parcel is the spatial data.

**Three requirements for the computer.** Parker says that each feature must be specified by:
1. Its geographic location.
2. Its attributes (what it is). A lake, for example, can carry attributes such as depth, water quality, fish populations, salinity and ownership.
3. Its relationships to other features ([[Topology]]).

**Historical referencing.** The [[Public Land Survey System]] (PLSS), established by Congress in 1785, is a range-township system. It is not based on geodetic coordinates. Parker notes that the technology for measuring longitude was new in 1785, and that John Harrison, who built the first marine timepiece accurate enough for longitude determination, died in 1776 (Wilford, 1981). Cadastral survey data is the basis for official legal land descriptions, which creates discrepancies when it is inserted into latitude/longitude-based databases. The BLM is developing a [[Geographic Coordinate Data Base]] (GCDB), which may take many years to complete.

## Ecological & Environmental Context

**Juxtaposition and topology.** Parker draws an analogy with wildlife habitat. A food source alone does not constitute habitat. Cover and water must also be present, and all must be located in relation to one another as defined by a species' life requirements. This concept of [[Juxtaposition of Habitat Components]] translates into map topology, which asks whether features are adjacent, close, or distant, and how one travels between them. Parker says the treatment of topology separates modern GIS from older systems and from most other computer graphics systems. The BLM's [[MOSS]] (Map Overlay and Statistical System) uses an older, simple polygon data structure that does not meet modern topological standards (Alberts et al., 1986).

**Resource management as science and art.** Parker describes resource management as "part science and part art," dependent on local ecology, the manager's background, management history and objectives, all of which vary in space and time. This complicates automation, which he addresses by first automating the discrete, repeatable parts of the process.

**Global assessment.** The author argues that GIS and remote sensing could support global environmental and resource assessments. Detailed spatial databases at continental scale are expected to become feasible through new storage technologies, especially [[Optical Disk]] storage.

## Key Findings

**1. GIS manufactures new information.** Parker rejects the saying that computers only return what is put in. Using a GIS, a manager can combine, add, subtract, multiply and divide many layers, which is the core of GIS analytical methods and the main difference from [[Computer-Assisted Cartography]] (Burrough, 1986). Before computers, only two or three overlays could be mentally registered at once. A GIS can hold as many maps as the hardware allows, which Parker puts at hundreds or thousands.

**2. Example of complex routing query.** Parker gives a hypothetical query: find all possible pipeline corridors between Denver and Los Angeles that stay below 8,300 ft elevation, are at least 75% on public land, stay more than 1 mile from known endangered wildlife populations, cross no streams at angles under 80 degrees, and include no grades over 7%. The results would then be ranked by private land crossed, required pumping stations, and station locations.

**3. Primary versus compound operations.** Primary operations include area and distance measurement, buffer generation, reclassification and Boolean operations. Parker calls these spatial data handling "primitives" (Berry, 1986). Compound procedures are built from them. Primary analyses are routine in a significant number of BLM field offices, but compound procedures remain experimental.

**4. Detection of illegal drainage.** Parker cites one notable BLM application: detecting illegal oil and gas drainage from public lands by wells on private lands. Geologic, administrative and related data are combined through macro software, reducing the process from several days of manual work to a few hours.

**5. Planning as the main BLM application.** The BLM must produce [[Resource Management Plan]]s (RMPs) that weigh land uses, environmental protection and public opinion. GIS is used to evaluate alternatives for environmental impact, economic implications, land area and use conflicts. An average of 50 thematic maps may be digitized during an RMP process (Zulick, 1986). Parker notes that digitizing is expensive but permanent, and the data remain in use after the plan is completed.

**6. Simulation modeling.** Parker identifies [[Simulation Modeling]] as one of the most powerful GIS applications. Managers can evaluate competing land uses, coal leases, scenic area designations, timber sales, fence construction and utility corridors. He states that "mistakes in the computer are much less painful and expensive than mistakes on the ground."

**7. Reported applications.** Other natural resource GIS applications cited include modeling forest pest impacts (White, 1986), water quality monitoring (Welch et al., 1986), modeling narcotic crop sites (Waltz and Holm, 1986), waste site assessments (Buckley and Hendrix, 1986), and analysis of carbon dioxide development effects on elk (Brekke, 1986).

**8. GIS and remote sensing.** Parker argues that [[Remote Sensing]] is best seen as an external array of information sources feeding a GIS, not as a separate technology. Remote sensing data is usually not the primary data source. Digital image processing overlaps heavily with GIS functions, so Parker asks whether the distinction matters and concludes that it is less important than the gains in utility. Cibula and Nyquist (1987) used topographic and climatological data in a GIS to increase the number of landcover classes distinguished in [[Landsat]] MSS data from 9 to 21 for Olympic National Park. Parker notes that remote sensing data is now more accurately called "ancillary" to the GIS, since the GIS may contain many layers, only one or a few of them from remote sensing.

**9. Integrated framework.** Dahlberg and Jensen (1986) combined cartography, surveying, geodesy, photogrammetry, geography and related fields into an Integrated Spatial Information System (ISIS) for educational purposes.

**10. Storage feasibility.** Light (1986) estimated the storage needed for a digital database covering all 54,000 7.5-minute quadrangles for the lower 49 states. At a ground resolution of 1.7 meters, the data could fit on 4,000 optical disks, each smaller than a phonograph record. Parker estimates that a hectare-resolution database for the whole African continent could fit on 5 optical disks. (The exponent in Light's bit count is garbled in the scan and is not reported here.)

**11. Drivers of advancement.** Parker identifies three converging factors: rapid advances in microprocessor-based hardware and storage; spatial data processing reaching the level needed for natural resource challenges, even at global scale; and a political climate of reduced federal spending that is pushing agencies toward more efficient, lower-cost approaches. He concludes that the basic tools are in place, and that the main challenge is advancing the use of the technologies rather than the technologies themselves.

**12. Conclusion.** Parker states that GIS "is not a passing fad" and is already useful. He argues that agencies, the planet's resources and taxpayers will lose if managers do not take advantage of it.

**Appendix fragment.** The document ends with an incomplete, OCR-damaged description of a microcomputer GIS system (GIAS) developed at what appears to be Oak Ridge National Laboratory. It is said to integrate facility and environmental data, with initial development focused on imagery, scanned maps, feature chains, land use and land cover, and aerial photography. The fragment is too garbled to report further detail.