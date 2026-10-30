---
species: N/A
common_name: N/A
family: N/A
habitat: Polar sea ice (Arctic and Southern Ocean pack ice)
ocean_basin: Arctic Ocean
location: Svalbard region, Fram Strait, East Greenland Current, Greenland Sea
tags: [sea-ice, remote-sensing, polar-oceanography, earth-observation, automated-monitoring]
title: "Development of a sea-ice workstation for the automated monitoring of sea ice"
source_id: "PML0242"
marsh_id: "PML0242"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. Boardman, D. Darwin, J. Martin, N. McIntyre, K. Sullivan (1995). Development of a sea-ice workstation for the automated monitoring of sea ice. Polar Record 31(177): 155-160. Marsh Library ID: PML0242."
source_file: "Boardman et al. 1995. Development of a Sea-Ice Workstation for the Automated Monitoring of Sea Ice.pdf"
text_extraction: "text"
---
# Development of a Sea-Ice Workstation for the Automated Monitoring of Sea Ice

#ichthyology #marine-biology #sea-ice

## Executive Summary

This paper describes the development of the Sea-Ice Workstation (SIWS), a prototype software system for automated retrieval of sea-ice information from satellite data. The project was commissioned by the UK's [[Defence Research Agency]] under the [[British National Space Centre]] and led by Earth Observation Sciences Ltd. The SIWS integrates [[Synthetic Aperture Radar]] (SAR), [[AVHRR]], and [[SSM/I]] data to produce charts of ice edge, ice type, ice concentration, ice motion, and sea-surface temperature with minimal operator intervention. The workstation was completed in July 1994, and validation against independent measurements and four planned end-user evaluations form the next stage.

## Background & Description

Sea ice is highly dynamic: its extent varies by a factor of four seasonally, reaching a maximum of 26 million square kilometres each March, which is more than the area of North America. Users in research, meteorological forecasting, and offshore operations need parameters such as ice age (first-year versus multiyear floes), ice motion, open water (polynyas or leads), and ice concentration. Information requirements were grouped by scale:

- **Close range:** continual updates within areas up to 200 km.
- **Tactical:** daily, regional coverage.
- **Strategic:** typically monthly hemispheric surveys.

Existing ice-chart services are essentially tactical, usually issued every one to seven days, and ice forecasts are less common.

The SIWS was designed as a modular system with a graphical interface and five sub-systems:

1. **SAR Swath Predictor:** calculates spatial and temporal coverage of [[ERS-1]] SAR data and aids data planning.
2. **Pre-Processing (Data Preparation):** ingests data, deletes unwanted imagery, converts to a standard format, and generates geolocation information.
3. **Data Browse:** enables spatial and temporal searches and overlays SAR outlines on AVHRR data.
4. **Geophysical Processing:** runs five algorithm chains, with default or user-customised parameters.
5. **Results Display:** overlays vector and raster data and produces the final chart.

The consortium included the Scott Polar Research Institute, Mullard Space Science Laboratory, Oceanroutes Ltd, and Noctix Research Inc (Canada).

## Ecological & Environmental Context

Each satellite source has recognised limitations. [[AVHRR]] is the most widely used source for manual ice charting but is strongly affected by cloud and, for some channels, darkness. [[Passive Microwave Radiometry]] (SSM/I) provides hemispheric coverage with almost continuous operation over several years, but its resolution is poor (about 15 km at best). SAR offers high-resolution, all-weather imaging suited to navigation in ice-infested waters, but its spatial and temporal coverage is limited, and its processing load is high. The text notes that the rapidly changing nature of sea ice in some regions makes SAR coverage particularly constraining. The system was designed so that other data sources could be added later.

The SIWS validation example focused on the Fram Strait, near Svalbard, and the East Greenland Current. The test area was the northwest of Svalbard (about 81°N, 15°E) in March 1993.

## Key Findings

- **Ice-edge and concentration (SAR):** Pixels are classified into ice and water using texture measures (mean and standard deviation of Roberts and Sobel gradients), followed by fuzzy or discrete clustering. A confidence threshold makes the fuzzy results discrete. The ice edge is derived from a user-defined concentration isoline. The algorithm was newly developed because no existing method was considered robust enough.
- **Ice classification (SAR):** First-year and multiyear ice are separated by mean backscatter intensity. Multiyear ice is rougher and backscatters more strongly. Small sinuous leads in first-year ice were reliably identified.
- **Ice motion (SAR):** Based on an enhanced version of the [[Fily and Rothrock Method]] (1987). It uses multi-resolution matching, rotation handling, and quality control, and calculates mean ice-motion vectors on a 5 km grid.
- **SSM/I classification:** Derived from the [[NASA Team Algorithm]] using 19 GHz and 37 GHz brightness temperatures to estimate percentages of open water, first-year ice, and multiyear ice.
- **AVHRR sea-surface temperature:** Uses cloud/water/ice classification, then a simple coefficient-based calculation with channels 4 and 5, using default [[Maul Coefficients]] (1983).

**Validation:**
- The independent dataset came from a cruise of the German icebreaker *Polarstern* to the Greenland Sea in spring 1993. Helicopter photographs were classified visually, with more than 1000 photographically recorded surface types.
- SAR classification was compared with manual classification by glaciologists using confusion matrices. For a Fram Strait scene from 15 March 1993, more than 85% of the automatic classification was correct.
- In interior pack ice, or where waves had little influence on the ice edge, the algorithm reached a typical success rate of 70 to 80%. Multiyear ice and open water, including small leads, were accurately identified.
- A larger comparison set of more than 51,000 comparisons was also used for validation.
- SAR ice motion, SSM/I classification, and AVHRR sea-surface temperature were evaluated qualitatively, since their underlying methods had been validated previously.

**Status and outlook:**
- SIWS acceptance testing was completed in July 1994.
- Four end-user evaluations are underway with EOS and partners in the UK and USA. Users include national meteorological services, live shipping operations, and research communities.
- The authors expect a marked increase in radar data from ERS-2 and Radarsat, with launch planned for 1995. This will improve all-weather coverage of sea ice beyond what ERS-1 alone provides.