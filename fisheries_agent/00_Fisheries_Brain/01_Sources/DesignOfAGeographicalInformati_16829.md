---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: United Kingdom
tags: [gis, geographic-information-systems, natural-environment-research-council, data-architecture, spatial-data]
title: "Design of a geographical information system for a heterogeneous scientific community"
source_id: "16829"
minckley_id: "16829"
source_citation: "D. W. Rhind and N. P. A. Green (1988). Design of a geographical information system for a heterogeneous scientific community. International Journal of Geographical Information Systems 2(2): 171-189. Minckley Library ID: 16829."
source_file: "16829.pdf"
text_extraction: "ocr"
---
# A GIS for a Heterogeneous Scientific Community: Conceptual Design for the Natural Environment Research Council

#gis #geographic-information-systems #spatial-data-architecture #natural-environment-research-council

## Executive Summary

This paper, by D. W. Rhind and N. P. A. Green of [[Birkbeck College]], University of London, reports a study financed by the [[Natural Environment Research Council]] (NERC) that ran from 1984 for about 18 months. Its aim was to design a unified [[Geographic Information System]] (GIS) for a scientifically diverse, internally varied organization. The study assessed user needs, data volumes, [[Spatial Data Models]] and data structures, and user interface requirements, then proposed a distributed, workstation-based architecture. The authors conclude that a single monolithic NERC GIS is neither feasible nor desirable, and that the Council should adopt standardized hardware and software, selecting or jointly developing a commercial GIS rather than building one in-house.

The document is a research article, not a proposal or budget, so its "Key Findings" section summarizes results and recommendations.

## Background & Description

NERC employed about 2,700 scientists and support staff, organized into three scientific directorates: Earth sciences, terrestrial and freshwater sciences, and marine sciences. Major institutes included the [[British Antarctic Survey]], the [[British Geological Survey]], the [[Institute of Terrestrial Ecology]] and the [[Institute of Oceanographic Sciences]]. The organization spanned many sites across the United Kingdom and supported units in universities, including the NERC Unit for Thematic Information Systems at Reading University.

The study's methodology comprised:
- Assessment of current and future user needs, through face-to-face meetings, site visits and a questionnaire sent to university users.
- Estimation of database sizes and review of candidate data structures.
- Evaluation of man/machine interface options.
- Definition of a unified system for NERC.

The study also documented a corporate decision, taken partway through, to standardize on the [[Oracle]] relational database management system.

## Ecological & Environmental Context

The subject is not an organism or habitat. Relevant environmental context concerns the nature of NERC's data holdings:
- **Oceanographic data** were often more temporal than spatial in character, requiring three-dimensional modelling and space/time storage that commercial systems handled poorly.
- **Historical paper records**, such as [[British Geological Survey]] records dating to the 1830s, including borehole logs and maps, held locational references that would greatly increase GIS value if indexed.
- **Imported data** came from the [[Ordnance Survey]] (digitized topographic data at 1:50,000 and 1:10,000 scales), military sources and remote sensing projects.
- **Oceanographic submissions** were routed through the [[Marine Information Advisory Service]].

## Key Findings

**User needs**
- Appreciation of GIS was limited in 1984, roughly halfway between two review papers (Rhind 1981, 1987). Expertise varied from world-class to none.
- NERC was not a "closed system": it exported and imported data and drew on extensive contract research, which generated about 40% of its income in 1985/86.
- Contract projects were often short-term, requiring robust software and a "tool-kit" of modules.
- All 19 GIS functionality groups were found necessary at some venues, though no single site needed all of them.
- Oceanographers differed, arguing that data validation and modelling were discipline-specific rather than generic GIS functions.

**Data sharing and standards**
- Little spatial data was shared, partly because no catalogue of holdings existed. NERC subsequently established one and began developing dissemination guidelines.
- Idiosyncratic encoding methods across agencies hindered reuse.
- The team recommended common access for NERC scientists and NERC-funded external projects, via the [[Joint Academic Network]] (JANET).
- Error propagation analysis was identified as a serious unresolved problem, and the team recommended R&D on it.
- The ARCDEMO demonstrator, an instructional GIS tool, had been accessed via JANET more than 1,000 times.

**Data structures**
- Five levels of spatial abstraction were defined, extending [[Peuquet]] (1984): reality, analogue model, data model, data structure and file structure.
- Evaluation criteria were completeness, robustness, efficiency, versatility, ease of generation, functionality and utility. Versatility, robustness and functionality were prioritized.
- Vector structures (non-topological, topological, directed and hierarchical, plus hybrid forms such as geo-relational) and tessellated structures (regular, irregular and nested) were reviewed.
- The paper highlights a paradox: topological structures are the most useful but least available, while regular grid data are readily available from remote sensing and scanning.
- Data can generally be "decanted" between structures, but multi-structure support was judged necessary, and no existing commercial system met the requirements beyond a rudimentary level.

**User interface**
- No single interface suits every situation. The system should offer multiple access paths, build user profiles, and provide consistent terminology, feedback on six aspects of performance, and equal function in interactive and batch modes.

**Recommended architecture**
- Fully configured GIS on workstations at major NERC sites, linked by a high-speed LAN (e.g., 10 Mbit/s or faster) to file servers.
- Off-site users connect via the X.25 network. Research council supercomputers run subsets of the functionality for intensive work.
- Database administrators catalogue data for each file store, and a "sign-posting" service directs users to GIS expertise.
- A proposed "data restructuring box" built from transputers, which the authors estimated could reach about 100 times the speed of a MicroVAX II, requires experimental validation.

**Caveats and conclusions**
- Off-site users will have poorer but functionally identical facilities. Physically distributed databases will not appear as a single database until commercial solutions emerge.
- The [[Institute of Terrestrial Ecology]] and the [[British Geological Survey]] had already purchased incompatible systems, which NERC should supplement and eventually replace with standardized GIS.
- The Council was strongly recommended to review commercial offerings at purchase time and either select the best available GIS or pursue joint development with a commercial firm. Building a new GIS solely in-house was judged "a great mistake."