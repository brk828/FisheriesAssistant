---
species: Etheostoma gracile
common_name: Slough Darter
family: Percidae
habitat: pools, oxbows, backwaters, bayous, sloughs, swamps, ponds, lakes
ocean_basin: N/A
location: western Alabama to central Texas, Mississippi Embayment, Interior Low Plateau, central Illinois, southwestern Indiana, southeast Kansas, northeast Oklahoma
tags: [freshwater, darter, habitat-suitability-index, HSI-model, riverine, lacustrine, lowland-streams]
title: "Habitat suitability index models: Slough darter"
source_id: "15765"
minckley_id: "15765"
source_citation: "E. A. Edwards, M. Bacteller and O. E. Maughan (1982). Habitat suitability index models: Slough darter. OBS-82/10.9:US Fish and Wildlife Service. Minckley Library ID: 15765."
source_file: "15765.pdf"
text_extraction: "ocr"
---
# Habitat Suitability Index Models: Slough Darter

#ichthyology #freshwater-ecology #Percidae #darter #habitat-modeling

## Executive Summary

This U.S. Fish and Wildlife Service technical report presents Habitat Suitability Index (HSI) models for the [[Slough Darter]] (*Etheostoma gracile*), a small [[Percidae]] species inhabiting lowland aquatic systems across the south-central United States. The models synthesize literature on habitat requirements into mathematical indices scaled from 0 (unsuitable) to 1 (optimal habitat). Two models are provided: a comprehensive riverine model incorporating food-cover, water quality, and physical habitat components, and a simplified lacustrine model focusing on water quality parameters. The species is characterized by its preference for warm, turbid, slow-moving or standing waters with mud/silt substrates and minimal current. These models are designed for impact assessment and habitat management, though they represent hypotheses of species-habitat relationships requiring field validation.

## Background & Description

The [[Slough Darter]] (*Etheostoma gracile*) is a small percid fish native to lowland areas from western Alabama to central Texas, extending northward through the former Mississippi Embayment and Interior Low Plateau to central Illinois and southwestern Indiana, with populations in southeast Kansas and northeast Oklahoma. The species reaches a maximum standard length of 48 mm at age IV, with maturation occurring at age I. Natural hybridization with the [[Blackside Darter]] (*Percina maculata*) has been documented.

Slough darters are primarily benthic feeders, consuming insect larvae, microcrustaceans, and some snails throughout the year. Fry initially feed on diatoms and plankton before transitioning to insects and microcrustaceans. The spawning season extends from March to early June, with females laying eggs singly on substrates such as twigs or leaf petioles. Laboratory observations indicate a 5-day incubation period at 22.8°C, with females spawning only once and providing no post-spawning parental care. Field spawning observations are lacking due to turbid water conditions.

## Ecological & Environmental Context

The [[Slough Darter]] occupies a specialized ecological niche in lowland aquatic systems characterized by minimal flow and fine sediments. Optimal habitat consists of pools and oxbows in lowland streams, backwaters, bayous, sloughs, swamps, and lentic waters (ponds or lakes). The species demonstrates strong habitat selectivity for:

**Physical Habitat**: Low gradient streams (< 0.5 m/km), high pool-to-riffle ratios, sluggish or quiet water (< 10 cm/sec velocity), and mud or silt substoms (most consistent habitat characteristic). Occasionally found over bedrock, clay, sand, detritus, or gravel. Vegetation and debris may provide cover and spawning substrate, though only about half of collection sites had aquatic vegetation.

**Water Quality**: Moderate to highly turbid waters (typical habitat characteristic), though occasionally found in clear or slightly turbid conditions. Turbidity provides cover for all life stages but very high levels may limit food production. Minimum dissolved oxygen of 1.7 mg/l recorded at collection sites, though 5.0 mg/l considered optimal for growth and survival. Maximum summer temperature of 26.5°C recorded; pH of 6.7-7.2 documented in Louisiana bayou. The species is subject to oxygen deficit mortality events when dissolved oxygen becomes critically low.

**Distribution Patterns**: The species avoids areas with gradients averaging 3.5 m/km or more and is not found in upstream areas with current-swept channels. Adults may overwinter in deep sand or mud-bottomed pools. Turbidity appears to be an important limiting factor alongside current velocity.

## Key Findings

**HSI Model Structure - Riverine**: The riverine model incorporates three components:
- **Food-Cover Component** (C_fc): Based on turbidity (V₁) and percent pools (V₂). Equation: C_fc = (V₂ + V₁)/2
- **Water Quality Component** (C_wq): Based on dissolved oxygen (V₁), pH (V₅), turbidity (V₁), and average water temperature (V₄). Equation: C_wq = (V₁² × V₅² × V₁² × V₄)^(1/7), with special conditions if any variable < 0.4
- **Other Component** (C_ot): Based on stream gradient (V₃), substrate type (V₆), and average velocity (V₇). Equation: C_ot = (V₃ × V₆² × V₇²)^(1/5), with special conditions if any variable < 0.4
- **Final HSI**: HSI = (C_fc × C_wq × C_ot²)^(1/4), with special conditions if C_ot or C_wq ≤ 0.4

**HSI Model Structure - Lacustrine**: Simplified model using water quality component only: C_wq = (V₁² × V₅² × V₁² × V₄)^(1/7), where HSI = C_wq

**Variable Suitability Indices**: Eight habitat variables with specific suitability curves:
- V₁ (Dissolved oxygen): Optimal at ≥ 5 mg/l, unsuitable below 2 mg/l
- V₂ (Percent pools): Optimal at 75-100%, declining linearly to 0% pools
- V₃ (Stream gradient): Optimal at < 0.5 m/km, unsuitable above 3.5 m/km
- V₄ (Substrate type): Ranked A (>75% mud/silt) = 1.0, B (>50% sand/detritus) = 0.6, C (>75% gravel/sand/detritus) = 0.5, D (clay/bedrock) = 0.1
- V₅ (Water temperature): Optimal at 20-26°C
- V₆ (Turbidity): Optimal at 50-150 JTU, declining at extremes
- V₇ (Surface velocity): Optimal at < 10 cm/sec, unsuitable above 30 cm/sec
- V₈ (pH): Optimal at 6.5-8.0, unsuitable below 5.5 or above 9.5

**Simplified Habitat Model**: Optimal riverine habitat characterized by five criteria: moderate to highly turbid waters (50-150 JTU), sluggish waters (< 10 cm/sec), low gradient (< 0.5 m/km), high pool-to-riffle ratio (> 50%), and mud/silt substrate. HSI = (number of criteria present)/5.

**Sample Data Set Results**: Three riverine data sets yielded HSI values of 0.02, 0.57, and 0.92, demonstrating model sensitivity to habitat variation. Three lacustrine data sets produced HSI values of 0.87, 0.67, and 0.83. The models successfully generate indices between 0 and 1 believed to correlate positively with habitat carrying capacity.

**Model Limitations and Applications**: The models represent complex hypotheses of species-habitat relationships, not proven cause-effect relationships. HSI values should be interpreted comparatively rather than as absolute population predictors. The models are applicable throughout the species' native range in North America for riverine, palustrine, and lacustrine habitats. No minimum habitat area has been established. Model verification relied on sample data sets rather than field validation, meeting the acceptance goal of producing indices with expected positive relationships to carrying capacity.