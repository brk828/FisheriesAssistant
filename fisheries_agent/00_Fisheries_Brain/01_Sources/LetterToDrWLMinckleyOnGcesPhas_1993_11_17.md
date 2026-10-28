---
species: "Humpback Chub (Gila cypha); Rainbow Trout (Oncorhynchus mykiss, implied)"
family: "Cyprinidae (Humpback Chub); Salmonidae (Trout studies)"
habitat: "Colorado River mainstem (Glen and Grand Canyon); Little Colorado River (LCR); Lees Ferry"
ocean_basin: "N/A - Freshwater riverine system (Colorado River Basin)"
document_type: "Administrative/Data Status Letter"
date: "1993-11-17"
project: "Glen Canyon Environmental Studies (GCES) Phase II"
source_id: "11267"
---

#ichthyology #freshwater-biology #cyprinidae #salmonidae #riverine-ecology #humpback-chub

## Executive Summary

This document is an administrative status letter from the Arizona Game and Fish Department (AGFD) to Dr. W.L. Minckley, detailing the progress of datafile compilation and reporting for the **[[Glen Canyon Environmental Studies]] (GCES) Phase II** research program. Rather than presenting novel morphological or ecological findings, the letter serves as a data management record, cataloging fish collection datasets, tagging records, and ecological monitoring efforts on the Colorado River system, with a specific focus on the endangered **[[Humpback Chub]]** (*Gila cypha*) and non-native **[[Rainbow Trout]]** populations in the **[[Glen Canyon]]** and **[[Little Colorado River]] (LCR)** reaches. It outlines the structure of major relational databases (e.g., MASTER6.DBF, TAGSALL.DBF) used to track fish distribution, length/weight relationships, and long-term mark-recapture data from 1980–1993.

## Background & Description

While this letter is primarily administrative, the underlying datafile structures reveal the specific morphological and biological metrics being systematically collected by AGFD researchers on native and non-native fishes:

- **Total Length (mm):** Recorded for all captured specimens (field: `LENGTH`).
- **Weight (g):** Recorded for all captured specimens (field: `WEIGHT`).
- **Sex determination:** Coded field (`SEX`) for reproductive tracking.
- **Maturity Codes:** Numeric classification of reproductive stage (`MATURITY`).
- **Parasite Load:** Categorical assessment of parasitism (`PARASITE` code).
- **Pigmentation (`PIG`):** Likely used to distinguish [[Larval Fish]] developmental stages or hybrid identification (relevant to hybridization concerns between *Gila* species).
- **Hooking Injury (`HOOK_INJ`):** Assessed for angling-related mortality/stress in the [[Lees Ferry]] trout fishery.
- **Viscera/Stomach Analysis:** Dedicated "Viscera Header" and "Viscera Detail" files (e.g., VISH9101.DBF) indicate systematic dietary/gut-content dissection protocols for young native fish.

## Ecological & Environmental Context

The datasets referenced map distinct ecological monitoring efforts across the Colorado River ecosystem, segmented by species guild and habitat type:

- **[[Humpback Chub]] Spawning Habitat:** Primary monitoring focus in the **[[Little Colorado River]]**, tracking spawning cues, early life history, and juvenile recruitment (Work Task 3.2).
- **Thermal Ecology:** Specific studies (Task 3.9–3.10) evaluated **[[Thermal Tolerance]]** of young Humpback Chub (YOY HBC), including survival as a function of thermal conditions and thermal shock experiments comparing mainstem vs. LCR temperature regimes — critical given the cold-water discharge from **[[Glen Canyon Dam]]**.
- **Food Web Studies:** Investigated diet composition of young native fish via zooplankton sampling, benthic invertebrate surveys, and digestive tract analysis of juveniles (Task 3.5).
- **Water Chemistry & Hydrology:** Datasonde measurements and water sampling were used to correlate hydrological events (dam releases) with distribution and abundance of native fish (Task 3.8).
- **Behavioral Ecology:** Radio-telemetry ("RADIOTRAC") was used to study behavioral responses of trout to environmental conditions (Task 2.4) and young native fish behavioral responses in the mainstem (Task 3.6).
- **Propagation:** Active refugial propagation efforts for native fish were underway using "bubbling ponds" to develop protocols and provide progeny for augmentation (Task 3.3).
- **Habitat Use:** Larval habitat availability and use were quantified in the LCR (Studies 29208–29298), assessing microhabitat selection by young natives.

## Key Findings

- **Long-term Tagging Dataset:** The compiled `TAGSALL.DBF` integrates tagging records for **Humpback Chub** spanning **1980–1993**, sourced from multiple agencies/researchers (Bio/West, [[Arizona State University]], [[U.S. Fish and Wildlife Service]], and AGFD), including Lynn Kaeding's foundational 1980 tagging data.
- **Data Provisionality:** All datasets (e.g., MASTER6.DBF) are explicitly marked "**PROVISIONAL, DO NOT CITE**," reflecting the ongoing QA/QC verification (double keypunch verification) status typical of active long-term monitoring programs.
- **Extensive Native Fish Sampling Effort (Study 2 - LCR):** Over 20 discrete monthly fish collection studies were conducted in 1991 alone (Studies 29101–29219) in the LCR, capturing detailed header, detail, and substrate records for each sampling event.
- **Mainstem Sampling Intensity:** The mainstem native fish study (Study 3) logged distinct research trips at regular intervals from March 1991 through March 1993 (Trips 301–31560), indicating a sustained, high-frequency monitoring regime tied to experimental flow regimes from **[[Glen Canyon Dam]]**.
- **Multi-Agency Data Integration Challenge:** The letter highlights the complexity of harmonizing fish collection and tagging records across at least four contributing agencies/institutions into unified relational databases (`MASTER6.DBF`, `TAGSALL.DBF`), a foundational step toward the eventual archiving effort requested by Dr. Minckley.
- **Trout vs. Native Fish Programmatic Split:** Research tasks were organizationally divided between **[[Rainbow Trout]] Studies** (spawning, growth, movement in Glen Canyon) and **Native Fish Studies** (focused on the imperiled **[[Humpback Chub]]** and other **[[Colorado River Native Fish]]** in the LCR and mainstem), reflecting the dual management mandate of balancing a recreational trout fishery against native species recovery under the **[[Endangered Species Act]]**.