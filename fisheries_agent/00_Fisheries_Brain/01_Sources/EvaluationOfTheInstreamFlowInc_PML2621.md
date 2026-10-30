---
species: ["Oncorhynchus mykiss", "Salmo trutta", "Micropterus dolomieu", "Ambloplites rupestris"]
common_name: ["Rainbow Trout", "Brown Trout", "Smallmouth Bass", "Rock Bass"]
family: ["Salmonidae", "Centrarchidae"]
habitat: "Rivers and streams (regulated and unregulated lotic systems)"
ocean_basin: "N/A"
location: "United States and Canada; Colorado, Michigan, West Virginia, Virginia, Alabama, California (South Platte River, Huron River, three hydroelectric-affected streams)"
tags: [instream-flow, IFIM, habitat-modeling, fisheries-management, survey]
title: "Evaluation of the Instream Flow Incremental Methodology by U.S. Fish and Wildlife Service Field Users"
source_id: "PML2621"
marsh_id: "PML2621"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. L. Armour, J. G. Taylor (1991). Evaluation of the Instream Flow Incremental Methodology by U.S. Fish and Wildlife Service Field Users. Fisheries 16(5): 36-43. Marsh Library ID: PML2621."
source_file: "USFWS - Armour and Taylor 1991. Instream Flow Methodology.pdf"
text_extraction: "text"
---
# Evaluation of the Instream Flow Incremental Methodology by U.S. Fish and Wildlife Service Field Users

#ichthyology #freshwater-biology #salmonidae #centrarchidae

## Executive Summary

Armour and Taylor (1991, *Fisheries* 16(5)) report a 1988 mail survey of [[U.S. Fish and Wildlife Service]] (FWS) Fish and Wildlife Enhancement field offices on their experience with the [[Instream Flow Incremental Methodology]] (IFIM), a habitat-based framework for comparing alternative river flows. Of 57 offices surveyed, 35 (61%) responded. Twenty-five offices reported a combined 616 IFIM studies. Most applications were performed by non-FWS entities, and few were followed by monitoring. Respondents judged IFIM technically too simplistic and, at the same time, too complex and costly to apply. The authors recommend that future work emphasize [[Suitability Index Curves]] and the biological meaning of [[Weighted Useable Area]], and that negotiated flows be followed by post-project monitoring.

## Background & Description

IFIM was developed by the FWS in the early 1980s (Bovee 1982) to help biologists and water managers compare alternative flows for protecting or enhancing aquatic habitat in rivers and streams. Flow changes can result from water withdrawals for irrigation, domestic and industrial use, dam construction and operation, and channel alteration. The framework includes scoping, field data collection, habitat simulation, and negotiation among water users (Table 1). Its key advance was allowing quantitative habitat comparisons among flow regimes, where earlier assessments were only qualitative.

The central tool is the [[Physical Habitat Simulation Model]] (PHABSIM). It applies suitability index (SI) curves, scored from 0.0 to 1.0, for velocity, depth, substrate, or cover, specific to each target species and life stage. Cell area multiplied by a composite SI score gives weighted useable area (WUA), which is summed across the study site. WUA is then distributed over an annual time series to define flows for each life stage (Figure 2).

Table 1 lists the software components compiled by K. Bovee. Examples include:
- Institutional analysis (LIA.INST)
- Habitat modeling (PHABSIM variants such as IFG4, WSP, HEC-2)
- Temperature models (SRTEMP, SNTEMP; shade-based)
- Water quality (QUAL2E)
- Habitat time series and network models (HABTS, HABNET, LNK12H)
- Effective and equivalent adult habitat (EFFHAB, ANEQTS)

Technical concerns have been raised about SI curves and the link between WUA and fish biomass or abundance. Mathur et al. (1985) found insufficient evidence that WUA correlates with fish biomass, and Orth (1987) cautioned against assuming WUA and abundance are always positively correlated. Defenders such as Orth and Maughan (1986) and Gore and Nestler (1988) agreed the concern was legitimate in some cases but defended the method. Lamb (1989) framed the dispute as an institutional decision-making problem and advised users to understand its assumptions.

## Ecological & Environmental Context

The survey was designed to document applications and experiences in offices responsible for environmental impact assessment. Its five objectives were to: (1) count known IFIM applications; (2) document field checks of SI curve accuracy; (3) identify application difficulties; (4) solicit recommendations for the [[National Ecology Research Center]] (NERC); and (5) assess monitoring studies verifying whether negotiated flows were adequate. The survey was not intended to statistically represent all IFIM use.

Regulatory context matters. Under FERC licensing, hydropower applicants must conduct or contract instream flow studies. The authors expect demand for flow studies to grow as competition for water increases for recreation, agriculture, domestic and industrial use, and hydropower.

Target taxa in the cited studies include [[Rainbow Trout]], [[Brown Trout]], [[Smallmouth Bass]], and [[Rock Bass]]. Reiser et al. (1989) reported that IFIM was the most frequently used method for setting instream flows in 35 U.S. states and Canadian provinces.

## Key Findings

**Survey response and applications**
- 35 of 57 offices (61%) responded; 10 reported no IFIM applications and 25 reported applications.
- The 25 offices reported 616 IFIM studies. About 70% were in the Pacific Coast region (FWS Region 1; the text gives 435 applications, 71%).
- Twenty offices fully conducted 108 applications (about 18%). Of these, 73 (68%) produced flow recommendations.
- 276 studies (45%) were performed by non-FWS personnel at FWS request; 232 (38%) were independent of FWS requests.
- Responding offices averaged 3.1 applications each they conducted themselves.

**Reported success**
- Of the 24 offices applying IFIM, half rated success as 1 or 2 (on a 1-to-5 scale, where 1 is "extremely successful").
- 16.7% were neutral, and 33.3% reported low success (4 or 5).
- The overall average was 2.9.

**Monitoring and verification**
- Respondents listed 27 sites with believed monitoring; follow-up interviews confirmed monitoring at six.
- Only six of the 616 studies (about 1%) were verified as having follow-up monitoring.
- Ten testing, verification, or validation studies were confirmed: four on curve verification, two on the biological meaning of WUA, and four on other topics, including PHABSIM accuracy, mussel habitat, hydropower peaking dams, and cross-site curve transferability.

**Stumbling blocks**
- Respondents from 35 offices listed up to five obstacles, weighted by priority.
- The two dominant categories were "technically too simplistic" (about 40%, with SI curves and models the largest subgroup) and "too complex to apply" (about 41%, including expense, training, and time).
- IFIM being unaccepted or biased (about 9%) and legal and political constraints (about 11%) were smaller concerns.

**Recommendations for NERC**
- 26 of 35 offices gave recommendations, weighted toward research (about 76%) over education and training (about 24%).
- Research priorities: improving SI curves, computer models and compatibility, validating the biological meaning of WUA, adapting IFIM to hydropower peaking flows, reducing application time, adding temperature routines, and integrating with other assessment methods.
- Some recommendations were already underway, such as making IFIM compatible with personal computers and adding temperature parameters.

**Discussion and related studies**
- Non-FWS entities conducted most applications; the authors attribute this to workloads exceeding FWS field office capacity and to regulations assigning study responsibility to license applicants.
- Hubert et al. (1990) evaluated 119 negotiated-flow projects in Colorado, Montana, and Wyoming. Post-project data existed for 61 sites. At 89% (54) of these monitored sites, flows fell below negotiated levels at least once. At 28 sites, flows were 25% or less of the agreed minimum at least once. Adequate biological response data existed for very few sites.
- Ongoing NERC and partner work includes: a California study of fish population responses to altered flows on three hydropower-affected streams (Pacific Gas and Electric); a Colorado study of SI curve transferability on the South Platte River; a Michigan study developing SI curves for smallmouth and rock bass; cooperative unit SI curve work for smallmouth bass in West Virginia and Virginia; and an Alabama study of regulated flows for warmwater stream fish (Bain and Boltz 1989).
- Cheslak and Jacobson (1990) developed a model linking WUA to temporal changes in rainbow trout carrying capacity.

**Conclusions and recommendations**
- IFIM is widely accepted, but with little post-project monitoring, the degree of resource protection it achieves is uncertain.
- Field users should negotiate post-project monitoring as an integral part of each IFIM study.
- Research should continue on the relationship between WUA and fish population responses, on the geographic transferability of SI curves, and on the ecological validity of SI curves across species and life stages.