---
species: N/A
common_name: Butterflies (Lepidoptera, unspecified species in excerpt)
family: N/A
habitat: Terrestrial; county-level records across Oregon
ocean_basin: N/A
location: Oregon, USA
tags: [biodiversity, butterflies, lepidoptera, sampling-effort, conservation-biology, species-richness]
title: "Using compiled species lists to make biodiversity comparisons among regions: a test case using Oregon butterflies"
source_id: "16298"
minckley_id: "16298"
source_citation: "w. Fagan and P. Kareiva (1997). Using compiled species lists to make biodiversity comparisons among regions: a test case using Oregon butterflies. Biological Conservation 80: 249-259. Minckley Library ID: 16298."
source_file: "16298.pdf"
text_extraction: "ocr"
---
# Using Compiled Species Lists to Make Biodiversity Comparisons Among Regions: A Test Case Using Oregon Butterflies

#lepidoptera #conservation-biology #biodiversity

## Executive Summary

This study by [[William F. Fagan]] and [[Peter M. Kareiva]] (University of Washington) tests two statistical methods for correcting [[Sampling Effort]] bias in species lists compiled from museum and conservation databases. The test database is a set of about 11,994 [[Butterfly]] records from Oregon, assembled from the [[Northwest Lepidoptera Survey]]. The two methods are a phenomenological saturating-curve fit and a [[Lognormal Distribution]] model of species abundances. The authors find that the lognormal approach is more reliable at small sample sizes and generally avoids overestimating diversity. Corrected estimates change the apparent geography of high-diversity areas. The authors also conclude that protecting Oregon's most butterfly-rich regions would not normally protect most rare or endangered species. The excerpt ends partway through the Results section.

## Background & Description

**Problem.** Resource managers and conservation biologists increasingly rely on regional species lists. These lists are often built from a mixed set of museum records, local collecting trips, and private enthusiasts' records, which were not designed as a comprehensive basis for management decisions. The main problem is that regions are sampled at different intensities. Some areas are well enough sampled to record most resident species, while others record only a small fraction. Poorly sampled regions can appear species-poor when they are simply undersampled. This matters because species-rich regions often receive priority in management resources, as in the [[GAP Analysis Program]] in the United States and tropical conservation efforts.

**Dataset.** The [[Evergreen Aurelians]], a lepidopterists' society, maintains a database of roughly 24,000 Oregon butterfly records. The authors analyzed a computerized subset of 11,994 records from the last 100 years, comprising identification, date, and locality data. Records were analyzed at the county level because Oregon has 36 counties and county data are widely available. The data were not edited. Range gaps were not filled, habitat was not used to infer presence, vagrant records were kept, and all specimen identifications were assumed correct. Subspecies were counted as "species" for convenience, and "diversity" means species richness.

**Study design.** The authors compared two correction methods, tested their sensitivity with a half-data cross-validation, and then examined how well county-level diversity overlapped with three definitions of rarity.

## Ecological & Environmental Context

- **Sampling and hotspots.** Uneven collecting effort can make certain counties look like biodiversity hotspots or coldspots. The paper argues that corrected estimates are needed before resources are allocated on the basis of species richness.
- **Rarity definitions.** Three definitions of rarity were used:
  1. Endangered or threatened species, based on [[United States Fish and Wildlife Service]] listings, Category 1 and 2 candidates, and species at risk of extinction in Oregon, following Lists 1 and 2 of the [[Oregon Natural Heritage Program]].
  2. Numerically rare species, defined as present in five or fewer specimens in the database.
  3. Regionally restricted species, defined as present in three or fewer of Oregon's 36 counties.
- **Community structure.** The authors invoke the [[Lognormal Distribution]] of species abundances, which arises because a few species are very common or very rare while most are intermediate. Abundance is grouped into [[Octave Classes]] on a log₂ scale, following [[Preston]] (1948). This is a widely observed pattern in ecological communities, which is why the authors consider it a sound basis for correction.
- **Related methods.** The approach parallels [[Species-Area Curves]] and rarefaction-type analyses, which also seek to separate truly species-poor regions from undersampled ones.

## Key Findings

**Methods and model performance**

1. **Phenomenological fits.** Two saturating curves were fitted to cumulative species-versus-specimen data for each county: the [[Michaelis-Menten Model]] (eqn 1a) and the [[Negative Exponential Model]] (eqn 1b). The fitted asymptote is the estimate of true diversity.
2. **Lognormal model.** A discretized normal curve was fitted to octave-class abundances (eqn 2). Missing species were estimated with the May (1975) correction using the [[Error Function]] (eqns 3–4). Goodness of fit was tested with a G-test, or a [[Kolmogorov-Smirnov Test]] when there were too few categories.
3. **Cross-validation.** Half-data estimates were compared with full-data estimates. Phenomenological estimates from half the data were often higher than full-data estimates, sometimes substantially, indicating overestimation at low sample sizes. This bias persisted even in counties whose sampling curves visibly saturated. The lognormal estimates were consistently lower than full-data estimates when half the data were used. They were therefore more conservative and less erratic at low sample size.
4. **Lognormal fit.** About 75% of counties had abundance distributions consistent with a lognormal distribution. Excluding counties with significant deviations did not change the overall pattern.
5. **Preferred method.** The authors recommend the lognormal approach because it offers substantial improvement over raw data and generally avoids overestimation.

**Results for Oregon butterflies**

6. **Species total.** The database contains 214 butterfly species. Most have specimens spanning at least 50 years of collecting, with 1987–88 records the most recent. Only nine species were not recorded after 1970.
7. **Estimates versus raw counts.** For the lognormal estimator, all but two counties had estimated diversity above their sampled diversity. Ten counties had predicted asymptotic diversities double their sampled values, which is the maximum the method can produce. Four of these are coastal counties (3, 6, 11, 12), and four are adjacent north-central counties (21, 22, 23, 28).
8. **Rank changes.** Correction substantially reshuffled county rankings. Morrow County (23) ranked eighteenth on raw data but first on the asymptotic estimate.
9. **Raw-data pattern.** Without correction, the Siskiyou Range counties of Jackson (14) and Klamath (33) stood out as the most diverse. Coastal counties and those along the Columbia River appeared least diverse.
10. **Corrected pattern.** After lognormal correction, several additional counties appeared highly diverse. Six counties (17, 23, 26, 28, 31, 36), mostly central and eastern Oregon, shifted into the high-diversity group.
11. **Rare species and hotspots.** The abstract states that the distribution of endangered and numerically rare butterflies rarely coincides with diversity hotspots. Protecting Oregon's most diverse regions would therefore not normally protect most rare or endangered species.

**Correlations (Table 1, read from OCR)**

- Sampled richness correlated strongly with the phenomenological estimates (Estimate 1A r = 0.819; Estimate 1B r = 0.958) and less strongly with the lognormal estimate (Estimate 2 r = 0.715).
- Estimate 1A and Estimate 1B correlated at r = 0.947. Estimate 2 correlated only modestly with each (0.644 and 0.701).
- Sampled richness was essentially uncorrelated with endangered species (Rare 1, r = 0.036). Estimate 2 was slightly negatively correlated with Rare 1 (r = −0.157).
- Correlations with numerically rare (Rare 2) and regionally rare (Rare 3) species were moderate for the sampled and corrected richness measures, roughly 0.4–0.6.

**Note on the excerpt.** The document ends mid-sentence in the Results section, so the full conclusions and the remaining county comparisons are not included.