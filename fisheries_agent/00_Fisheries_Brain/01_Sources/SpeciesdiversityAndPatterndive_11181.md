---
species:
  - Acer rubrum
  - Populus grandidentata
  - Pinus strobus
  - Betula papyrifera
  - Abies balsamea
  - Pinus resinosa
  - Populus tremuloides
  - Picea glauca
  - Pinus banksiana
  - Acer saccharum
  - Quercus rubra
  - Picea mariana
  - Tilia americana
  - Fagus grandifolia
  - Ostrya virginiana
  - Betula alleghaniensis
  - Quercus macrocarpa
common_name: Red Maple, Largetooth Aspen, Eastern White Pine, White Birch, Balsam Fir, Red Pine, Trembling Aspen, White Spruce, Jack Pine, Sugar Maple, Red Oak, Black Spruce, American Basswood, American Beech, Eastern Hophornbeam, Yellow Birch, Bur Oak
family: Aceraceae, Salicaceae, Pinaceae, Betulaceae, Fagaceae, Malvaceae (Tilia), Corylaceae (Ostrya)
habitat: Young, naturally regenerating temperate forest stands following fire (Laurentian Section, Hemlock-White Pine-Northern Hardwoods Forest Region)
ocean_basin: N/A
location: Petawawa Forest Experiment Station, Ontario, Canada
tags: [plant-ecology, forest-succession, diversity-indices, information-theory, natural-thinning]
title: "Species-diversity and pattern-diversity in the study of ecological succession"
source_id: "11181"
minckley_id: "11181"
source_citation: "E. C. Pielou (1966). Species-diversity and pattern-diversity in the study of ecological succession. Journal of Theoretical Biology 10(2): 370-383. Minckley Library ID: 11181."
source_file: "11181.pdf"
text_extraction: "ocr"
---
# Species-Diversity and Pattern-Diversity in the Study of Ecological Succession

#plant-ecology #forest-succession #diversity-indices

## Executive Summary

This 1966 theoretical and empirical paper by E. C. Pielou in the *Journal of Theoretical Biology* proposes a method for measuring **[[Pattern-Diversity]]**, the degree to which species are intermingled spatially in a sessile community, and pairs it with an information-theoretic measure of **[[Species-Diversity]]**. The method is applied to six permanent sample plots of young, naturally regenerating forest trees at the Petawawa Forest Experiment Station in Ontario. Over intervals of five to ten years, natural thinning through competition was associated with an increase in pattern-diversity in all five plots that were initially segregated, which the author interprets as evidence that intraspecific competition within single-species clumps was the dominant mechanism of change during [[Ecological Succession]].

## Background & Description

**Diversity concepts.** Diversity in a collection is commonly quantified with indices that depend only on the number of individuals per species. The paper argues that for sessile organisms such as plants the spatial arrangement also matters. A community of single-species clumps has low pattern-diversity, whereas a community with intermingled species has high pattern-diversity.

**Information-based species-diversity.** Two forms are discussed:
- The [[Brillouin Index]]-based measure H, the information per individual (Equation 2), which is appropriate when the collection itself is the object of study.
- The [[Shannon Index]] H′ (Equation 3), which is appropriate when the collection is a sample from a larger, homogeneous parent population.

The author prefers H because nearly all biological collections contain several species represented by very few individuals, and enlarging a collection tends to add new rare species rather than simply increasing the counts of known ones. For a given number of species, H is maximal when individuals are distributed as evenly as possible across species, increases with the number of species, and increases with collection size N. The paper also shows that random removal of individuals lowers expected H, because the expected decrease in information is always positive. This is a consequence of the collection-size dependence of H.

**Units.** Using logarithms to base s (the number of species) yields s-ary units such as "decits" for ten species. In that case the H′ measure becomes an evenness index, H/H_max, with a maximum of 1 when all species are equally abundant. The paper compares this with the [[Margalef Index]] (D_Mg) and notes that the ratio H/H_max is a suitable evenness measure for finite collections.

**Pattern-diversity.** Pattern-diversity is quantified as D = B(n)/E[B(n)], where B(n) is the mean observed information content of groups of n neighbouring individuals and E[B(n)] is the expected value for a simple random sample of the same size. Groups of n = 3 nearest trees were used, sampled in three non-overlapping 120° sectors around random points. D equals 1 in randomly mingled communities, is significantly below 1 in segregated communities, and is theoretically above 1 under [[Negative Segregation]]. The author notes that D is an arbitrary measure because it depends on the choice of n and sampling rule, but it is valid for comparisons when the same methods are used throughout.

## Ecological & Environmental Context

**Study system.** Six forest plots from the [[Petawawa Forest Experiment Station]] of the Canadian Department of Forestry were studied. All had been left undisturbed since they regenerated after fires, and they belong to the [[Laurentian Section]] of the [[Hemlock-White Pine-Northern Hardwoods Forest Region]] (after Braun, 1950).

- Plot ages at first mapping ranged from 20 to 73 years.
- Plot areas ranged from 0.30 to 1.00 acre.
- Tree density ranged from more than 2500 trees per acre in the youngest plot to fewer than 500 per acre in the oldest.
- Trees with a diameter at breast height above half an inch were mapped between 1926 and 1945.

**Natural thinning.** Deaths exceeded ingrowth, so natural thinning reduced the high initial densities of trees that had colonized the burned land. The study tracks only trees that survived, so the analysis focuses on changes within a fixed starting population rather than on new recruitment.

**Mechanisms considered.** The paper weighs two possible causes of the observed change in segregation:
1. Habitat variability, in which each species survives mainly in localities suited to it. This would decrease pattern-diversity over time.
2. [[Intraspecific Competition]] within initial single-species clumps, which would progressively intermingle species and increase pattern-diversity over time.

## Key Findings

**Species composition and survival**
- The 17 tree species listed in Table 1 include common taxa such as [[Red Maple]], [[Largetooth Aspen]], [[Eastern White Pine]] and [[Sugar Maple]]. Species richness per plot ranged from 4 to 13.
- Total initial individuals per plot ranged from roughly 380 to 977, depending on the plot.
- Plots were numbered in decreasing density and increasing age: Plot 1 was the densest and youngest, and Plot 6 the oldest.
- Later censuses were five years after the first mapping for Plots 1–3 and nine to eleven years for Plots 4–6.

**Table 3: species-diversity, evenness and pattern-diversity** (values as reported)

| Plot | H earlier | H later | H/H_max earlier | H/H_max later | D earlier | D later | D_later − D_earlier |
|---|---|---|---|---|---|---|---|
| 1 | 1.235 | 1.199 | 0.622 | 0.605 | 0.5977 | 0.7501 | 0.1524 |
| 2 | 2.168 | 2.189 | 0.781 | 0.791 | 0.7756 | 0.8171 | 0.0415 |
| 3 | 2.048 | 2.071 | 0.696 | 0.707 | 0.9890 | 0.9620 | −0.0270 |
| 4 | 2.709 | 2.661 | 0.745 | 0.734 | 0.8593 | 0.9094 | 0.0501 |
| 5 | 1.668 | 1.548 | 0.535 | 0.499 | 0.8845 | 1.0301 | 0.1456 |
| 6 | 1.383 | 1.445 | 0.544 | 0.570 | 0.8798 | 0.9862 | 0.1064 |

Sampling: 200 random points for Plots 1, 2, 4 and 5; 100 points for Plots 3 and 6. Standard errors of D are reported in parentheses in the source (for example, 0.0545 to 0.0845).

**Species-diversity**
- Species-diversity and evenness decreased in Plots 1, 4 and 5 and increased in Plots 2, 3 and 6.
- The author concludes that the pattern across all plots gives no consistent trend toward rare species becoming rarer or common species becoming commoner.

**Pattern-diversity**
- Plots 1, 2, 4, 5 and 6 showed significant segregation at the earlier date (D significantly below 1). Plot 3 did not, and its species were randomly mingled from the start.
- In all five initially segregated plots, D increased over time. The increase was statistically significant only in Plots 1 and 5.
- Taking all five plots together, the probability of D increasing in all five by chance is (1/2)^5 = 0.031, which the author interprets as a significant tendency.
- By the later date, D in Plots 5 and 6 no longer differed significantly from 1, while Plots 1 and 2 still showed significant segregation.

**Conclusion on mechanism**
- Competition within single-species clumps (mechanism ii) was the predominant process in these plots. Natural thinning therefore reduced segregation and increased pattern-diversity.

**Methodological notes**
- The author stresses that D, and any pattern measure, is conditional on the observational method (choice of n and sampling rule), so comparisons must use consistent protocols.
- Calculating E[B(n)] is feasible for n = 2 or 3 but becomes computationally prohibitive for n > 4.