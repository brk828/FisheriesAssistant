---
species: "N/A"
common_name: "N/A"
family: "N/A"
habitat: "Lentic wetlands (seasonally or permanently inundated) on the Macleay Valley floodplain"
ocean_basin: "N/A"
location: "Macleay Valley floodplain, coastal northern New South Wales, Australia"
tags: [conservation-biology, reserve-selection, wetlands, biodiversity, botany, algorithms]
title: "Selecting networks of reserves to maximise biological diversity"
source_id: "19373"
minckley_id: "19373"
source_citation: "C. R. Margules, A. O. Nicholls and R. L. Pressey (1988). Selecting networks of reserves to maximise biological diversity. Biological Conservation 43(1): 63-76. Minckley Library ID: 19373."
source_file: "19373.pdf"
text_extraction: "ocr"
---
# Selecting Networks of Reserves to Maximise Biological Diversity

#ichthyology #marine-biology #wetland-botany

## Executive Summary

This paper by [[Margules]], Nicholls and Pressey presents explicit numerical algorithms for selecting the smallest set of sites that represents the maximum number of species within a biological domain. The case study uses the 432 wetlands of the [[Macleay Valley Floodplain]] in coastal northern [[New South Wales]], Australia, where complete lists of higher plant species were available. Two approaches are compared: a [[Species Representation Algorithm]] that maximises species richness at a specified number of representations, and a [[Habitat Representation Algorithm]] that ensures every wetland type (nine [[Habitat Types]] from hierarchical classification) and every species is represented. The authors conclude that protecting maximum diversity requires a large number of reserves, and that 5% or 10% of wetland area would be hopelessly inadequate.

Note: the source is a research article, not a fish study. No fish species are reported; the organisms analysed are higher plants of wetlands.

## Background & Description

**Study system.** The 118 higher plant species recorded across all 432 wetlands included 98 native species (Pressey, 1984). Wetlands were delineated by the presence of plants adapted to waterlogging. All are lentic waterbodies that are seasonally or permanently inundated.

**Conservation criteria.** Margules & Usher (1981) recognised 18 classes of conservation criteria, eight of them scientific. The most widely used scientific criteria, namely [[Biological Diversity]], rarity, naturalness, size and representativeness, all share the underlying goal of maintaining diversity in perpetuity. The authors argue that identifying a minimum set of sites that encompasses maximum diversity is an essential prerequisite for conservation evaluation, one largely neglected in recent [[Reserve Design]] literature.

**Methodological basis.** The approach is conceptually similar to that of [[Kirkpatrick]] (1983) and Kirkpatrick & Harwood (1983), but species were not weighted. Wetland types were defined by similarity of species complements using the [[Bray-Curtis Coefficient]] and weighted pair group averaging.

## Ecological & Environmental Context

- **Species–area relationship.** Wetlands were plotted on a species–area curve using the fitted equation log S = 2.275 + 0.110 log(area) + 0.009[log(area)]². All but one of the wetlands selected to represent each species at least once lay above the average line, meaning they were more species-rich per unit area than average. Small, species-poor wetlands with unique species were absent from the selected sets.
- **Rarity and large wetlands.** Wetland 353 was included because it held three unique species. Wetland 69 was included because it held a species found in only two wetlands. Wetland 350, the largest and second-richest wetland, was excluded until four representations were required because it had no unique species and few uncommon ones.
- **Multi-stemmed mallee comparison.** In a parallel study of [[Mallee Remnants]] on the Eyre Peninsula, South Australia, 12 of 101 patches (about 12%) gave a 95% chance of representing six plant communities at least once. Representing every community five times required 45 patches, nearly half.
- **Croplands and wheat belt.** Logistic regression was used to predict occurrence probabilities of plant communities in unsampled patches in South Australian croplands. The approach was being field-tested in the New South Wales wheat belt.
- **Tasmanian wetlands.** Kirkpatrick & Harwood (1983) assessed [[Tasmanian Wetlands]] using a richest-first selection, which tends to add wetlands with unique species late.

## Key Findings

**1. Species representation (Algorithm 1).**
- Representing all 98 native species at least once required 20 wetlands. Rule 1 selected 15 wetlands covering 87 species; five more covered the remaining 11.
- Representation counts rose with each level: 31 wetlands for two representations, 40 for three, 52 for four and 65 for five.

**2. Habitat representation (Algorithm 2).**
- Nine habitat types were classified hierarchically. The first step selected one wetland per type, covering 68 species.
- A minimum set of 29 wetlands represented all 98 species and all nine types. Alternative selection orders required 30 wetlands; 27 wetlands were common to all four orders.
- Eighteen of the 20 wetlands from Algorithm 1 were included in the 29-wetland set. However, only four of the nine habitat types were represented by those 18. Types 3, 5, 7, 8 and 9 were species-poor and were missed.
- Additional species after step 1 became progressively more costly: new species per step were 68, 12, 7, 5, 2, 2, 1, 1, and average new species per wetland fell from 7.6 to 1.

**3. Area requirements (Table 4).**

| Conservation goal | Wetlands (%) | Wetland area (%) |
|---|---|---|
| All species at least once | 4.6 | 44.9 |
| All species at least twice | 7.2 | 45.4 |
| All species at least 3 times | 9.3 | 45.7 |
| All species at least 4 times | 12.0 | 77.1 |
| All species at least 5 times | 15.0 | 78.5 |
| Once plus all wetland types | 6.7 | 75.3 |

Representing species three times required little more area than once. Moving to four or more representations increased the area needed by nearly one third.

**4. Policy implications.**
- Figures of 5% or 10% of land area are inadequate, even for single representation of all species.
- The belief that biological diversity is secure with one or a few well-chosen reserves is "unfounded"; a very large number of reserves appears necessary.
- Multiple representation may guard against extinctions caused by species turnover in wetlands subject to water-level change.

**5. Methodological notes.**
- Order-dependence in tie-breaking was acknowledged. Alternatives such as fewest exotics or largest wetland would introduce naturalness or size criteria.
- Constraints (e.g. minimum populations, proximity, abundance) can make the algorithms multi-objective.
- Rare species were prioritised by starting with wetlands holding unique species, which yields smaller sets than richest-first selection.
- Sacrificing the last six species could cut the set, but that requires an extra-regional context.

**6. Book review (pp. 77–80).** The issue also contains a review of *Deforestation in Uganda* by A. C. Hamilton (Oxford University Press with East African Wildlife Society, 1984, 92 pp.). The reviewer notes that about 570,000 ha of moist tropical forest (roughly 3% of the land area) is reserved, plus about 500,000 ha of mountain protection forest. Many reserves are small and surrounded by dense settlement, and the book covers forestry from 1898 to 1982.