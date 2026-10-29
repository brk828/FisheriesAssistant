---
species: N/A
common_name: N/A
family: N/A
habitat: Surface waters (lakes, streams, watersheds) of the eastern United States
ocean_basin: N/A
location: Northeastern U.S.A., Mid-Appalachian Region, Southern Blue Ridge Province; Ontario, Canada (referenced)
tags: [gis, acid-deposition, surface-water-chemistry, watershed-science, environmental-policy]
title: "The role of a geographical information system in a large environmental project"
source_id: "17367"
minckley_id: "17367"
source_citation: "W. G. Campbell, M. R. Church, G. Bishop, D. Mortenson and S. Pierson (1989). The role of a geographical information system in a large environmental project. International Journal of Geographical Information Systems 3(4): 349-362. Minckley Library ID: 17367."
source_file: "17367.pdf"
text_extraction: "ocr"
---
# Role of a Geographical Information System in the Direct/Delayed Response Project

#ichthyology #marine-biology #freshwater-acidification

## Executive Summary

This paper (Campbell et al., *International Journal of Geographical Information Systems*, 1989, vol. 3, no. 4, pp. 349-362) describes how a [[Geographical Information System]] (GIS) supports the [[Direct/Delayed Response Project]] (DDRP), a regional U.S. Environmental Protection Agency (EPA) study of the long-term chemical response of surface waters to [[Acidic Deposition]]. The GIS aggregates, analyses and displays environmental data at multiple scales and projections, and is used mainly to communicate findings to scientists, policymakers and the public. The paper is a methods and applications account; it presents no new fish, invertebrate or ecological survey data.

## Background & Description

**Problem.** "Acid rain" (acidic deposition) has acidified some surface waters in the northeastern U.S. ([[Sullivan et al. 1988]]) and Ontario, Canada ([[Neary and Dillon 1988]]), driven by sulphur emissions from fossil fuel combustion. Open questions include whether further effects will occur, how extensive and how rapid they will be, and what deposition levels will limit them.

**Study design.** The DDRP uses a regional "top-down" approach: define the population at risk, select a representative sample of watersheds, characterise their response times to acidic deposition, and extrapolate to the target population with a known level of certainty. Three regions are studied:
- Northeast Region (glaciated northeastern U.S.)
- Mid-Appalachian Region (upland Mid-Atlantic)
- [[Southern Blue Ridge Province]] (mountainous southeast)

**Source surveys.** Sampling draws on the [[National Surface Water Survey]] (NSWS), comprising the [[National Lake Survey]] and the [[National Stream Survey]], which target lakes and streams most vulnerable to acidification (lowest [[Acid Neutralizing Capacity]], ANC).

**GIS platform.** The DDRP bought an ARC/INFO GIS in March 1985, operational by October 1985 on a VAX 11/750, later moved to a VAX 785/8650 cluster. Hardware included two digitising workstations, a Calcomp 5845 colour electrostatic plotter, a Calcomp 1075 four-pen plotter and multiple graphics terminals.

## Ecological & Environmental Context

- **Sample selection.** In the Northeast, 145 lake/watershed systems from the National Lake Survey were selected; lakes with ANC > 400 µeq/l, depth < 1.5 m, or cultural disturbance were excluded, as were watersheds over 3000 ha. In the Southern Blue Ridge Province, 35 watersheds under 3000 ha from the Pilot Phase of the National Stream Survey were selected. In the Mid-Appalachian Region, 36 watersheds were retained (figure 2) after excluding low-interest streams (ANC > 200 µeq/l, acid mine drainage, or cultural disturbance), Piedmont and Coastal Plain sites (focus on mountain trout streams), and sites duplicating the glaciated Northeast.
- **Soils and hydrology.** Watersheds were mapped by the USDA Soil Conservation Service for soils, vegetation, depth to bedrock and drainage. Random pedon sampling characterised soil sampling classes.
- **Terrain and runoff.** Digitised contours, blue-line streams and 1:250 000 digital elevation models were combined with permeability and bedrock depth to drive [[TOPMODEL]], which estimates soil-water contact time and flow-path partitioning. Quickly responding systems allow fewer interactions with soils and less acid neutralisation than slower ones. Runoff was interpolated from expert-drawn regional runoff maps because watersheds were selected randomly, not by gauge availability.
- **Buffers.** Linear buffers of 30 m and 100 m around perennial streams were used in the Mid-Appalachian and Blue Ridge regions. In the Northeast, elevational buffers (areas bounded by a selected contour) better captured low-lying wetlands. At Long Pond, New Hampshire, wetlands made up 36% of the elevational buffer versus 7% of the whole watershed, tied to high colour and dissolved organic carbon, placing the lake near the 90th percentile of the NSWS population.
- **Sulphur retention and acidification potential.** Sulphur retention (the fraction of deposited sulphur retained in a watershed) was mapped by MLRA region. An index of potential acidification combined retention with ANC, as the difference between theoretical steady-state sulphate and current sulphate, divided by ANC.

## Key Findings

1. **GIS as a regional integration tool.** The GIS combines site-level soil pedon data, watershed-level mapped data and regional sulphur deposition, and supports spatial analysis, modelling display and map production (see [[Spatial Analysis]]).
2. **Data quality control.** The GIS verified sample-site coordinates by overlaying recorded latitude/longitude on soil maps and comparing them with mapper descriptions (e.g., nearby highways). Discrepancies were resolved and final maps were generated.
3. **Scale trade-off.** Bedrock geology was digitised from state maps at 1:250 000 to 1:500 000. This sacrificed watershed-specific detail for regional consistency of legends, which the authors judged necessary for evaluating regional geology's role in surface water chemistry.
4. **Proximity matters.** Land units close to a lake or stream may control its chemistry more than distant ones; elevational buffers outperformed linear buffers in the Northeast.
5. **Deposition-sulphate link.** Plots of lake sulphate against wet sulphate deposition (figure 5, after Sullivan et al. 1988) and GIS maps (figure 6) show a clear relationship between atmospheric sulphur deposition and surface water sulphate.
6. **Regional acidification potential.** The index of potential acidification (figure 8, MLRA regions; sites with ANC > 200 µeq/l or sulphate > 400 µeq/l excluded) identifies eastern regions where acidification risk may be greatest. The authors note the GIS can rapidly regenerate these maps under alternative deposition scenarios.
7. **Policy relevance.** The authors state that DDRP results are likely to influence U.S. legislation on sulphur emissions, and argue that GIS capabilities increased the defensibility, timeliness and validity of the results.
8. **Limitations.** The GIS is not a process model. It supports existing watershed models (TOPMODEL) and statistical procedures by building datasets and displaying outputs.