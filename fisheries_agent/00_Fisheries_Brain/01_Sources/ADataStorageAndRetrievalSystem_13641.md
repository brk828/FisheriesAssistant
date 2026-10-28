---
species: ["Colorado squawfish (Ptychocheilus lucius)", "Humpback chub (Gila cypha)"]
family: ["Cyprinidae"]
habitat: "Large turbid rivers; Colorado River mainstem and tributaries"
ocean_basin: "N/A - Freshwater riverine system (Colorado River Basin)"
subject_type: "Data management system / fisheries informatics"
source_id: "13641"
---

#ichthyology #marine-biology #Cyprinidae #fisheries-data-management #endangered-species

## Executive Summary

This paper, authored by [[Richard A. Valdez]] and [[J. Curtis Wilcott]] under the U.S. Fish and Wildlife Service, does not present novel fish biology findings but instead describes **MANAGE**, an interactive computer database management system (DBMS) developed by the [[Western Energy and Land Use Team]] (WELUT) and applied by the [[Colorado River Fishery Project]] (CRFP) to store, retrieve, and analyze habitat and life-history data on endangered [[Colorado River Basin]] fishes. The system was designed to handle large volumes of numeric and alphanumeric (English-language) field data collected on species such as the [[Colorado Squawfish]] and [[Humpback Chub]], with the ultimate ecological goal of developing habitat suitability ("electivity" or probability) curves to inform recommended instream flow regimes for endangered fishes.

## Background & Description

This source is a data-systems paper rather than a morphological study; however, it specifies the biological and morphometric parameters routinely recorded for individual endangered/threatened fish specimens under the **CRFP*RARE** dataset, which serve as proxies for morphological characterization in the field:

- **Length** (standard/total length, recorded per individual)
- **Weight**
- **Sex**
- **Tag size and number** (for mark-recapture identification, e.g., [[Tag Number 0558]] referenced for a recaptured [[Humpback Chub]])
- **Parasite load**
- **Age category** (used in the CRFP*CATCH dataset to classify catch by species and life stage, e.g., adult vs. juvenile)

Species identification in the field was streamlined using a two-letter alphanumeric coding system (e.g., 'CS' = [[Colorado Squawfish]]), which MANAGE automatically translates into full English-language species names during data retrieval and reporting.

## Ecological & Environmental Context

The datasets described reveal the key habitat and environmental variables considered critical to characterizing the ecological niche of endangered Colorado River fishes:

**Physical/Chemical Habitat Parameters** (CRFP*PHYSICAL dataset):
- Water and air temperature
- Dissolved oxygen
- Conductivity
- Salinity
- Turbidity
- Stream width and depth

**Catch and Habitat-Association Data** (CRFP*CATCH dataset):
- Sample time and duration
- Gear type
- Habitat type
- Area sampled
- Depth (recorded to nearest 0.1 ft)
- Water velocity (recorded to nearest 0.1 ft/s)
- Substrate type (e.g., coded 'SA' for sand)

**Rare/Endangered Fish-Specific Data** (CRFP*RARE dataset):
- All of the above catch/habitat variables plus sex, length, weight, tag data, and parasite load, linked to individual specimens of endangered/threatened species.

These variables collectively define the microhabitat niche (depth, velocity, substrate, temperature) occupied by adult, juvenile, and spawning [[Humpback Chub]] and [[Colorado Squawfish]] populations along specific river miles (RMI) of the [[Colorado River]], supporting downstream analyses such as [[Habitat Suitability Curves]] and flow-regime recommendations.

## Key Findings

- **MANAGE** enables storage and retrieval of both numeric and alphanumeric data via an interactive, password-protected, multi-terminal system usable by minimally computer-trained field technicians.
- Three core datasets were developed to structure CRFP field data: **CRFP*PHYSICAL**, **CRFP*CATCH**, and **CRFP*RARE**, corresponding to physical/chemical, general catch, and endangered-species-specific data respectively.
- A simplified two-letter alphanumeric coding system (e.g., 'CS' for [[Colorado Squawfish]], 'SA' for sand substrate) sped up field data recording and reduced technician training time; MANAGE automatically expands these codes into full English-language terms during output.
- The system supports **single-record retrieval** (e.g., pulling all data for a specific tag number, such as tag #0558 for a recaptured [[Humpback Chub]]) and **multiple-record retrieval** (e.g., pooling all humpback chub habitat records — depth, velocity, substrate — within a specified river section).
- Data can be entered either interactively online or via a cheaper batch/card-deck process, with a Database Administrator (DBA) defining field names, data types, lengths, and searchability for each dataset.
- The primary intended ecological application of MANAGE is the aggregation of habitat association data (depth, velocity, substrate) across life stages (e.g., adult humpback chub during spawning) to build **habitat electivity/probability curves**, which are described as key to establishing reliable recommended flow regimes for endangered fishes in the [[Colorado River]].
- The paper underscores a broader institutional problem: the U.S. Fish and Wildlife Service manages over 15 Servicewide programs across 30+ Area Offices and 6 Regional Offices, generating large volumes of field data that were previously handled manually and often remained inaccessible to other personnel — a gap MANAGE was designed to close.