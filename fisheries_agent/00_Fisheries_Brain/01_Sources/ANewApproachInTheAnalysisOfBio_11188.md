---
species: N/A
common_name: N/A
family: N/A
habitat: Marine mesopelagic and midwater fish assemblages; insular terrestrial herpetofauna (Puerto Rican shelf islands)
ocean_basin: Atlantic Ocean; Pacific Ocean (Eastern South Pacific)
location: Atlantic transect from southeast to northwest (R/V Chain, cruise 17, 1961); off the west coast of South America (R/V Anton Bruun, cruise 13, 1966); Puerto Rican shelf islands, Caribbean
tags:
  - ichthyology
  - marine-biology
  - biogeography
title: "A new approach in the analysis of biogeographic data"
source_id: "11188"
minckley_id: "11188"
source_citation: "J. A. Peters (1971). A new approach in the analysis of biogeographic data. Smithsonian Contributions to Zoology 107: 1-28. Minckley Library ID: 11188."
source_file: "11188.pdf"
text_extraction: "ocr"
---
# A New Approach in the Analysis of Biogeographic Data

#ichthyology #marine-biology #biogeography

## Executive Summary

James A. Peters (National Museum of Natural History, Smithsonian Institution) proposes a new method for analyzing [[Biogeography|biogeographic]] data. Instead of relying on a single [[Similarity Coefficient]] per locality, the method ranks all similarity coefficients for each locality in descending order and compares these ranked columns across every pair of localities. The number of positional differences, the [[Discrepancy Count]], indicates biotic affinity when low and a possible [[Biotic Barrier]] when high. The method is tested on fish collections from two Pacific and Atlantic transects and on herpetological data from the [[Puerto Rican Shelf]]. The paper also critiques [[Numerical Taxonomy]] techniques, particularly [[Cluster Analysis]] as applied to biogeography, and includes the BASIC program [[JPFRF Program]] used for the analysis.

## Background & Description

The paper is a methodological study published in the *Smithsonian Contributions to Zoology* series (number 107, 1971, 28 pages, 16 figures). Peters frames biogeography as a field in which data are voluminous and analysts often take shortcuts. He identifies two recurring problems:

- **Circular reasoning:** New data are interpreted in light of earlier area boundaries, and taxonomic recognition of material from new areas can reinforce those boundaries.
- **Arbitrary primary areas:** Results of quantitative analyses depend heavily on how primary areas are chosen. [[Hagmeier And Stults]] (1964) and their revision (Hagmeier, 1966) illustrate this, as does the work of [[Holloway And Jardine]] (1968).

The review of prior methods covers:

- **Webb (1950):** Similarity coefficients computed between neighboring points across Texas, with contour-style mapping of transitional zones.
- **Huheey (1965):** A divergence measure (taxa in one area but not both, divided by total taxa) applied to a grid, producing "isometabases."
- **[[Kikkawa And Pearse]] (1969):** Analysis of 121 Australian sites and 464 bird species using divisive information analysis, which the author found hard to follow and possibly information-losing.

The paper also details the [[Chain Gang Study]] of mesopelagic fishes, which the author uses as a comparison dataset.

## Ecological & Environmental Context

The fish data come from two oceanic transects. The first, the [[Atlantic Ocean Transect]], was made by [[R/V Chain]] in 1961. The second, the [[Anton Bruun Cruise 13]], was made off South America in 1966. The main environmental explanations discussed are:

- **Water masses:** The [[Chain Gang Study]] linked a faunal boundary near station 807 to the boundary between the South Atlantic Central Water and North Atlantic Central Water masses. This was associated with deepening and divergence of the 15° and 20° isotherms, a degraded [[Thermocline]], and a thicker surface isothermal layer.
- **Upwelling and currents:** Peters concludes that the first two groups of Anton Bruun stations lie within the area of influence of the [[Humboldt Current]]. The fourth group probably represents a large, well-defined water mass.
- **Island endemism:** On the Puerto Rican shelf, St. Croix has high endemism, which masks its similarity to neighboring islands in conventional similarity tables.

## Key Findings

**1. The ranking method.** Similarity coefficients for each locality are ranked in descending order and paired with the identities of the other localities. For each pair of ranked columns, the positional displacements are counted and totaled as the discrepancy value. Few discrepancies indicate close biotic relationship; many indicate a possible barrier.

**2. Rank correlation coefficient.** Peters derives a coefficient from the discrepancy count D and the number of localities N:

- Even N: 2D = N²
- Odd N: 2D + 1 = N²
- Formula: 1 − s = 2D / N², giving values from 0 (no similarity) to 1 (complete agreement).

The author chose to maximize differences rather than treat maximum discrepancy as negative correlation, because the goal is to identify units, not to test correlation.

**3. Manual counting is impractical.** Counting discrepancies by hand for 42 localities took about 30 minutes per comparison. Forty localities would need about 800 comparisons, so the task was automated with JPFRF. All 800 comparisons could then be done in less time than one manual comparison.

**4. Atlantic transect (Chain Gang data).** The data cover localities 800–813, with 116 species recorded. The Chain Gang reduced this to 44 species. Results:

- Using only actual occurrences, the first run did not clearly reveal relationships, except possibly among localities 11, 12, and 13.
- Assuming a species occurs at any station between its first and last captures, a distinct change appeared between localities 6 and 8.
- Combining localities 806 and 807 gave a sharp boundary. Adding 807 to 808 increased crossovers and displacements, supporting the 806–807 combination.
- The Chain Gang's own statistic (chi-square 3.79) placed the boundary near 807, with odds of about 19 to 1 against sampling error.

Peters notes that reproducing the Chain Gang results required assuming occurrence at unsampled stations. He argues this is a product of the linear cruise design and would be risky in non-linear studies.

**5. Puerto Rican shelf (herpetofauna).** Heatwole and MacKenzie (1967) data for 11 islands were run using Preston's coefficient, with zeros set to 0.01 and uncalculable values set to 0.99. Monito was excluded because only two species are known from it.

- St. John, St. Thomas, and Tortola formed a very close group, with Culebra closely related.
- Puerto Rico, Caja de Muertos, Vieques, and perhaps Mona formed another group.
- Anegada was intermediate with most islands, which Peters interprets as dissimilarity rather than an intermediate fauna.
- St. Croix, which has 8 species (4 endemic), showed very low discrepancy counts with St. John, Tortola, and St. Thomas. Peters suggests its fauna derives from this group or that all share a common source.
- Puerto Rico has 45 species, while the other islands have at most 14, several with fewer than ten. The method still worked, which Peters attributes to thorough sampling.

**6. Anton Bruun Cruise 13 (independent test).** This dataset had no sequence information, so only presence-absence data were used. It contained 133 species from 42 stations, with no assumptions about occurrence. The analysis found four groups:

- Groups 1 and 2 are less sharply distinct but internally cohesive, and lie within the Humboldt Current's influence.
- Group 3 is set off from the first two, with a minimum between-group discrepancy of 14.
- Group 4 is sharply distinct: within-group discrepancies are very low, and its minimum discrepancy with any outside station is 41.

Craddock and Mead (1970) reported a faunal break at about 80° W, which Peters considers consistent with his boundaries.

**7. Critique of cluster analysis.** Peters argues that [[Weighted Pair Group Method]] (WPGM) clustering is biologically indefensible for biogeography because:

- Averaging species counts produces impossible values. For example, a combined unit of "S" (55 species) and "T" (50) would be recorded as 53 species, though it must have at least 55.
- WPGM relies on averages of averages, which compound error.
- Clustering uses only the single coefficient between two localities and ignores the rest of each locality's relationships.

Recalculating shared taxa from original data after each merge yields a pattern that matches the Chain Gang and JPFRF boundaries. However, similarity values then increase with merging, so a standard phenogram cannot be built.

**8. Limitations acknowledged.** The author notes that the Chain Gang assumption of presence between sampled stations is risky outside linear transects. Tied ranks are treated flexibly, and the author argues that the minimization of discrepancies has little effect on the final result.