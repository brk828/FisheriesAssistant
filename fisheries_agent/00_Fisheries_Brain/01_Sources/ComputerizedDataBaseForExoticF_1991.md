---
title: "Computerized Data Base for Exotic Fishes: The Western United States"
authors: [James D. Williams, Dawn P. Jennings]
year: 1991
journal: California Fish and Game
volume: "77(2):86-93"
species: "Multiple exotic species (126+ species documented)"
family: "Multiple families (Cyprinidae, Cichlidae, Poeciliidae, Salmonidae, etc.)"
habitat: "Open freshwater systems (rivers, lakes, drainages) of the western United States"
ocean_basin: "N/A (freshwater/inland aquatic systems)"
tags: [ichthyology, marine-biology, exotic-species, invasive-species, freshwater-ecology, database-methodology]
source_id: "12008"
---

#ichthyology #marine-biology #exotic-species #invasive-species #freshwater-ecology

## Executive Summary

This paper describes the creation and structure of a **computerized database** (built in dBASE III Plus) developed by the U.S. Fish and Wildlife Service's National Fisheries Research Center (Gainesville, FL) to track [[Exotic Fish Introductions]] in open waters of the continental United States, with particular focus on the western states. Since 1978, researchers have documented at least **126 species of exotic fishes** collected from U.S. open waters, of which **46 have established populations** nationally. In the western United States specifically, **80 species are established** and **68 have been collected but are not confirmed established**. The database compiles taxonomic, geographic, temporal, and management data for each collection record, drawing from state/federal agencies, museum collections, and published/unpublished literature. As of publication, roughly 600 records had been entered nationally (with ~150 from western states), and the authors anticipated reaching 1,000 records by 1991. The paper emphasizes the ecological risk exotic species pose to native [[Threatened and Endangered Species]] in the arid/subtropical Southwest (Arizona, Southern California, Nevada), where climate favors survival of non-native aquarium and aquaculture escapees.

## Background & Description

This paper is a **database/methodology report** rather than a morphological study, so detailed anatomical descriptions of individual species are not provided. However, the database schema captures **taxonomic identity fields** relevant to morphological classification for each specimen record, including:

- **GROUP** – broad taxonomic group (fish, mollusk, etc.)
- **FAMILY / GENUS / SPECIES / SUBSPECIES** – full taxonomic hierarchy
- **COM_NM** – common name(s)
- **ID_BY** – identifying authority (person/institution)
- **MUS_NO** – museum voucher number, enabling future morphological re-examination of preserved specimens

Represented taxa span diverse morphological/functional groups, including:
- **Cyprinids** (common carp *Cyprinus carpio*, grass carp *Ctenopharyngodon idella*, [[Silver Carp]] *Hypophthalmichthys molitrix*, [[Bighead Carp]] *H. nobilis*, goldfish *Carassius auratus*)
- **Cichlids** ([[Tilapia]] spp., *Cichlasoma* spp., oscar *Astronotus ocellatus*, peacock cichlid *Cichla ocellaris*)
- **Poeciliids** (guppy *Poecilia reticulata*, mollies, swordtails *Xiphophorus* spp., platyfish)
- **Salmonids** (brown trout *Salmo trutta*, Ohrid trout *Salmo letnica*)
- **Gobiids** (yellowfin goby *Acanthogobius flavimanus*, chameleon goby *Tridentiger trigonocephalus*)
- **Predatory/large-bodied exotics** (Nile perch *Lates niloticus*, bigeye lates *Lates mariae*, pacu *Colossoma* sp., piranha *Serrasalmus* sp.)

## Ecological & Environmental Context

The database is structured to capture **ecological and biogeographic context** for each exotic introduction via standardized fields:

- **Geographic fields**: Country, State, County, Drainage basin, USGS quadrangle, Township-Range-Section, UTM coordinates, Latitude/Longitude, verbal locality description
- **Temporal fields**: Year, Month, Day of collection
- **HABITAT**: descriptive habitat type where specimen was taken
- **TYPE_INTRO**: pathway of introduction — aquarium release, aquaculture escape, baitfish contamination, sport fish stocking, or unknown
- **STATUS**: establishment status — established, possibly established, localized, or unknown
- **AGENCY / STK_SOURCE**: responsible stocking agency and source of stock

### Introduction Pathways
Most collected exotic species originate from:
1. **Aquarium releases** (e.g., cichlids, poeciliids, gobies)
2. **Aquaculture escapes** (e.g., tilapia, carp species, [[Armored Catfish]] *Hypostomus* sp.)
3. **Purposeful government introductions** for biological control (e.g., grass carp for aquatic vegetation control) or sport fishing (e.g., brown trout)

### Regional Hotspots
- **[[Southwestern United States]]** (Arizona, Southern California, Nevada) and **Florida** are identified as primary concern areas due to subtropical/warm climates supporting survival and reproduction of tropical exotic species.
- Climate is explicitly linked to exotic species diversity — warmer regions support significantly more established non-native taxa than northern states (e.g., Alaska has zero established or collected exotics; Wyoming and Montana have minimal counts).

### Conservation Concern
The paper links exotic species establishment to **declines, range reduction, and local extirpation of native fish species**, citing potential adverse impacts on indigenous **threatened and endangered species** in the western U.S. (Taylor et al. 1984).

## Key Findings

- **National scope**: At least 126 exotic fish species collected from open U.S. waters; 46 established nationally (Courtenay et al. 1991).
- **Western U.S. scope**: 80 species established; 68 collected but not confirmed established.
- **State-by-state establishment counts** (selected):
  - **California**: 18 established / 19 collected — highest diversity among western states, including estuarine/euryhaline exotics like [[Yellowfin Goby]], [[Orangemouth Corvina]] (*Cynoscion xanthulus*), and [[Bairdiella]] (*Bairdiella icistia*)
  - **Arizona**: 8 established / 10 collected — notable for *Tilapia* spp. establishment
  - **Nevada**: 10 established / 13 collected — includes African cichlid mbunas (*Melanochromis*, *Pseudotropheus zebra*) likely from aquarium trade
  - **Texas**: 10 established / 10 collected — includes large predatory exotics (*Lates niloticus*, *Cichla* spp.)
  - **Idaho, Colorado, Montana, Oregon, Utah, Washington, Wyoming**: lower diversity (3–10 established), dominated by common carp, goldfish, brown trout, and tench
  - **Alaska**: zero established or collected exotic fishes — attributed to climatic unsuitability
- **Common widespread established exotics** across nearly all western states: *Carassius auratus* (goldfish), *Cyprinus carpio* (common carp), *Salmo trutta* (brown trout), *Tinca tinca* (tench)
- **Database utility**: Designed as a **centralized, dynamic information exchange system** for tracking distribution, dispersal rates, and range expansion of exotic species, intended to support management decisions by state/federal agencies.
- **Data gaps**: Authors note many historical records remain unreported in museum collections or buried in unpublished agency reports, underscoring the need for continued data consolidation.
- **Call to action**: Authors actively solicited state agency contributions to expand and correct the western U.S. species list.

### Related Concepts
[[Biological Invasion Pathways]] | [[Aquarium Trade and Fish Introductions]] | [[Aquaculture Escapes]] | [[Grass Carp as Biological Control]] | [[Native Fish Decline Southwestern US]] | [[Tilapia Introductions in North America]] | [[dBASE Wildlife Data Management]]