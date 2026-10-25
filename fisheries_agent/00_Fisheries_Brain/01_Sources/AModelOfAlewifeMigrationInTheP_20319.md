---
species: Alosa pseudoharengus
common_name: Alewife
family: Clupeidae
habitat: Anadromous; estuary, river, shallow headwater ponds, and coastal marine waters
ocean_basin: North Atlantic
location: Parker River, Essex County, Massachusetts; Gulf of Maine
tags: [alewife, anadromous-fish, fish-migration, population-modeling, stock-management, Massachusetts]
title: "A model of alewife migration in the Parker River, Massachusetts for simulating an optimal anadromous fish stock management program"
source_id: "20319"
minckley_id: "20319"
source_citation: "G. Libey, C. F. Cole and J. E. Johnson (1975). A model of alewife migration in the Parker River, Massachusetts for simulating an optimal anadromous fish stock management program. Water Resources Research Center University of Massachusetts. Minckley Library ID: 20319."
source_file: "20319.pdf"
text_extraction: "ocr"
---
# Alewife Migration Model for the Parker River, Massachusetts

#ichthyology #marine-biology #clupeidae

## Executive Summary

This completion report (Water Resources Research Center, University of Massachusetts Amherst, September 1975) presents a simulation model of [[Alewife]] (*Alosa pseudoharengus*) migration in the [[Parker River]], Essex County, Massachusetts. The model is intended as a decision aid for the [[Massachusetts Division of Marine Fisheries]] and other agencies managing anadromous fish stocks in the Parker and similar Massachusetts rivers. Field data were gathered from 1971 onward through run counts, tagging, scale-based age analysis, and limnological monitoring. The model is a compartment model with five compartments (ocean, estuary, two river ponds, and spawning ponds), fitted to observed data by minimizing a mean-square error. The authors describe its current status as qualitative rather than predictive, with the escapement and production phases still under development.

## Background & Description

**Purpose and rationale.** The Parker River population was chosen as a study system because it is easily studied and manipulated at low "pilot plant" cost, baseline data existed from 1971, the run is small, and the dams require little money for repair or modification. Much of the data came from graduate theses ([[Mayo 1974]], [[Rideout 1974]], [[Beltz 1975]]).

**Species importance.** The report describes the alewife as the least valuable of the major east coast anadromous species under study (alongside Atlantic salmon and American shad), but important for three reasons:
- *Historical:* a staple food of early New England settlers, closely tied to coastal town prosperity from the 1700s.
- *Commercial:* historically exploited as a dried, salted product under town control. [[Field 1913]] estimated Massachusetts alewife production had declined 75% by 1913. In 1973, over 25,000 metric tons were harvested, mainly by foreign fleets in the Gulf of Maine.
- *Ecological:* annual spawning migrations transport marine-derived nutrients and energy inland, supporting freshwater predators and forage species.

**Biology.** The species ranges from Nova Scotia to North Carolina. Spawning migrations begin in early March in the south, late April to early May in the north, and mid-April in the Parker River. Southern fish spawn once per life cycle, whereas northern adults may spawn three to five times. Recruitment to spawning occurs from age II (south) to age V (north), with males maturing earlier than females. Young-of-the-year remain in fresh water feeding on zooplankton until late summer or early fall, then migrate to sea.

**Study system.** The Parker River flows eastward 25.8 km from two headwater ponds, [[Rock Pond]] (23.1 ha) and [[Pentucket Pond]] (34.0 ha), to Plum Island Sound, dropping 21.33 m. A third headwater, [[Baldpate Pond]] (26.7 ha), drains via Penn Brook but has too little flow to sustain an alewife run. The ponds are shallow (maximum depths 6.1 m and 8.8 m; mean depths 3.65 m and 3.75 m) and stratify by mid-May, with hypolimnia lacking measurable dissolved oxygen through summer. The river is interrupted by six low-head dams, originally built for industrial water power. All but Dam 3 are abandoned; Dam 3 still powers a snuff plant. Fishways are pool-and-weir type except Dam 6, which has a Denil fishway. Only at Dam 6 can alewife ascend the dam itself. The estuary is a positive type, with salinities of 6–31 ‰ at high tide and 0–21 ‰ at low tide, extending 13.4 km from the mouth to [[Dam 1]], the estuary-freshwater barrier.

## Ecological & Environmental Context

- **Trophic links:** Alewife eggs were found in all stomach samples of resident minnows (*Notropis hudsonius* and *N. atherinoides*). Yellow perch, white perch, largemouth bass, and pickerel prey on larvae and young-of-the-year. Bluefish and striped bass are major marine predators of young leaving fresh water.
- **Temperature control:** Water temperature is the dominant factor governing movement rate. Light acts as a switch that starts migration in the morning and ends it at night.
- **Factors with no significant effect on movement:** river discharge, tidal stage, dissolved oxygen, pH, and light intensity.
- **Monitoring:** A Ryan submersible thermograph recorded water temperature at Dam 1. A Hydrolab thermometer recorded air and water temperature during each count, with sky condition on a 0–5 scale. Discharge came from a USGS gauge 427 m below Dam 3. Pond limnology covered temperature and oxygen profiles, CO₂, pH, alkalinity, hardness, and transparency.
- **Related species noted:** [[White Perch]] and [[Striped Bass]] appear in the study context, along with [[Atlantic Salmon]] and [[American Shad]] as comparison anadromous species.

## Key Findings

**Methods**
- *Run counts:* visual ten-minute counts per hour at Dams 1, 5, and 6 were multiplied by six for hourly estimates, then summed from sunrise to dark.
- *Age and sex:* scale-based ageing, with run composition extrapolated by weighting daily samples by run size.
- *Tagging:* three-inch color-coded spaghetti dart tags were released above Dam 1 and observed at Dams 5 and 6.
- *Downstream traps:* suspended on Dams 5 and 2. They retained 90–95% of downstream-migrating adults alive in 1975.

**Population structure**
- Run sizes were estimated at 38,102 (1973) and 34,638 (1974). No run estimate was made in 1971.
- The 1969 year-class made up 81.64% of the 1973 run and 46.42% of the 1974 run. The 1970 year-class made up 49.25% in 1974. The 1971 year-class was much weaker.
- Male:female ratios were 1.6:1.0 (1972), 1.25:1.0 (1973), and 0.73:1.0 (1974).
- Males recruit at ages III–IV, females at IV–V, similar to [[Havey 1961]] in Maine.
- No fish that first spawned at age III was older than six years. Mortality is high enough to eliminate a year-class after four repeat spawnings.

**Movement**
- Upstream movement is unimodal, peaking between 1500 and 1800. No night movement was detected, which contrasts with [[Richkus 1974]] and [[Tyus 1974]].
- Tagged fish reached Dam 5 with 50% passing within three active-run days, and Dam 6 with 50% passing within four days. 95% of observed tag passage occurred within eight days.
- Early-run fish moved as a cohesive group, while later-tagged fish dispersed.

**Temperature index**
- A hour-degree index (Ta) accumulates water temperature above a base passage temperature (Tb) over 0700–1900, with Tb adjusting for acclimation ([[Beltz 1975]]).

**Model structure**
- Five compartments: Ocean, Estuary, Pond 1 (Dam 1 to Dam 5), Pond 2 (Dam 5 to Dam 6), and Pond 3 (Rock and Pentucket Ponds and tributaries, the spawning areas).
- Each compartment has three exits: onward migration, return to sea without spawning, or death. Exit rates are proportional to population size and may depend on temperature.
- Transit delays between dams follow skewed arrival distributions fitted with four polynomial equations, each covering a 7-day period.
- Model fitting minimizes the mean-square difference between simulated and observed data across all data for each spawning migration.

**Status and conclusions**
- The model is judged qualitatively, by how well plots of simulated and observed data match, because the statistical error structure is not yet known and the model is not yet sophisticated enough to pass a formal goodness-of-fit test.
- Escapement and production of young fish are the next components to be completed, using ongoing data on larval and juvenile production, early mortality, competition, and predation.
- The report concludes that alewife restoration is feasible in more than 100 Massachusetts streams, that large-scale shad restoration is underway in the Connecticut River, and that restoration is feasible in the Merrimack River. It argues that modeling can replace the costly "try and see" approach to planning.