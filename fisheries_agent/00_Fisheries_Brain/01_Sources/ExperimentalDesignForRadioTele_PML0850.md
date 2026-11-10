---
species: ["Cervus elaphus", "Molothrus ater"]
common_name: ["Elk", "Brown-headed Cowbird"]
family: N/A
habitat: "Forest and range landscapes (meadows, open and closed forest, clear-cuts, mature timber, old growth); terrestrial, not aquatic"
ocean_basin: N/A
location: "Starkey Experimental Forest and Range, northeast Oregon, USA; Clearwater Drainage, northern Idaho; North America"
tags: [radiotelemetry, wildlife-biology, experimental-design, study-design, sample-size, location-error, cervidae, terrestrial-mammals]
title: "Experimental design for radio telemetry studies"
source_id: "PML0850"
marsh_id: "PML0850"
library: "Marsh Library"
permission: "not public domain"
source_citation: "E. O. Garton et al. (2001). Experimental design for radio telemetry studies. Marsh Library ID: PML0850."
source_file: "Garton E.O. et al. 2001. Experimental design for radio telemetry studies.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Experimental design for radio telemetry studies

#wildlife-biology #radiotelemetry #cervidae

**Scope note:** This chapter addresses terrestrial wildlife radiotelemetry in general. It does not address fish or other aquatic taxa, except that the chapter's reference list mentions a collection covering fish and crustacea.

## Executive Summary

This book chapter, by [[Edward O. Garton]], [[Michael J. Wisdom]], [[Frederick A. Leban]], and [[Bruce K. Johnson]], is a guide to planning [[Radiotelemetry]] studies of wildlife. It works through a series of "critical questions" covering study purpose, inference population, sample unit, sampling design, sampling intensity, sampling bias, [[Location Error]], [[Observation Rate]] bias, and biological significance. The authors argue that most radiotelemetry studies are observational, that the individual animal should be the sample unit, and that current sample sizes are often too small. They propose linking animal choices with demographic outcomes such as [[Individual Fitness]] and [[Metapopulation Dynamics]]. The chapter is mainly based on [[Elk]] studies at [[Starkey Experimental Forest and Range]].

## Background & Description

The chapter opens by pointing readers to earlier handbooks and reviews: [[Amlaner and Macdonald (1980)]], [[Kenward (1987)]], [[White and Garrott (1990)]], [[Priede and Swift (1992)]], and [[Samuel and Fuller (1994)]].

The authors frame study design as a set of decisions made before fieldwork. These include:

- **Purpose:** movement, migration, dispersal, space use, home range, habitat use, resource selection, population size, survival, or fecundity.
- **Design type:** observational (descriptive or correlative) or manipulative.
- **Analytical goal:** testing hypotheses or building models. Model selection uses [[Akaike's Information Criterion]].
- **Inference population:** the group to which results apply.
- **Sample unit:** the individual animal, not each location.
- **Sampling scheme and intensity:** stratified, systematic, clustered, or random, and how many animals and locations are needed.

Two example species appear in the text. [[Elk]] (*Cervus elaphus*) are used for most worked examples. [[Brown-headed Cowbird]] (*Molothrus ater*) is the example for biological significance, where annual survival is given as 0.57 versus 0.51 under two conditions.

The chapter's closing material is the start of [[Chapter 3]], "Effects of Tagging and Location Error in Wildlife Radiotelemetry Studies" (by John C. Whitey, Thomas D. Bloxton, and John M. Marzluff). Its contents list covers transmitter effects on waterfowl, upland game birds, raptors, shorebirds, seabirds, mammals, aquatic mammals, and bats, along with location and mapping error.

## Ecological & Environmental Context

**Movement and dispersal.** The authors note that simple random-walk dispersal models predict a normal distribution of dispersers, and they give a [[Chi-Squared Distribution]] confidence interval for dispersal variance. Uneven sampling over distance biases such models. [[Porter and Dooley (1993)]] reviewed 15 field studies and found that 13 sampled unevenly over distance. Only one of five studies had simple models that fit the observed movements.

**Home range.** Common estimators include minimum convex polygons, ellipses, nonparametric contours, and [[Kernel Density Estimation]]. The authors say home range size is analogous to variance estimation, which is hard to do well and needs large samples.

**Resource selection.** Habitat is typically classified into categories such as vegetation cover types, vegetation habitat types (e.g., *Abies grandis*), topographic position, and successional stage. The authors favor [[Compositional Analysis]] and other multivariate methods over simple percent-use comparisons.

**Terrain and signal effects.** Steep canyons and dense vegetation can cause signal bounce and diffraction, which increase location error. Automated systems also show lower observation rates in dense canopy and on concave, steep slopes.

**Aerial versus ground sampling.** Aerial sampling covers large areas quickly but has coarse location precision and visually estimated habitat. Ground sampling gives detailed behavioral and habitat data but is biased against long-distance movements and can disturb animals.

## Key Findings

1. **Design decisions come first.** Purpose, observational versus manipulative design, hypothesis testing versus model building, inference population, and sample unit should be settled before fieldwork.

2. **Most radiotelemetry studies are observational.** This limits cause-effect inference, even though many such studies make causal claims anyway.

3. **Inference space is often poorly specified.** Of 31 radiotelemetry studies published in [[The Journal of Wildlife Management]] during 1991–1996, only 8 (26%) described the population to which inferences were intended. Of the 23 that did not, all 23 made generalized inferences beyond their study areas, and 12 (52%) made inferences to all populations across the species' range.

4. **The individual animal is the sample unit.** Individual locations are subsamples. Animals from the same social group are not independent, so they should not be treated as separate sample units. This is the basis of the [[Pseudoreplication]] argument.

5. **Home range sample-size requirements are large.** Using the [[Bivariate Normal Estimator]] (Dunn and Brisbin 1982), the authors give these sample sizes (Table 2.1):

| Confidence (%) | Bound (%) | Sample size required |
|---|---|---|
| 95 | 10 | 386 |
| 90 | 10 | 271 |
| 95 | 20 | 98 |
| 95 | 30 | 45 |

6. **Elk simulation results (Starkey).** The authors used 42 radio-marked adult female elk, about 15% of the adult female population at Starkey, each with 300 or more locations during spring–summer 1994.
   - With the adaptive kernel, up to 200–250 locations per animal with at least 20 animals may be needed to estimate home range within ±10%.
   - With the bivariate normal, about 10 locations per animal with 30 animals, or 20 animals with 20 locations each, may be enough for the same ±10% target.

7. **Resource selection sample size.** Based on [[Leban et al. (Chapter 11)]] and Leban (1999), at least 20 radio-marked animals with at least 50 locations per animal are needed for accurate resource selection estimates within a season. The authors recommend compositional analysis for this.

8. **Composite guidance.** Accurate estimates of resource selection and survival need at least 20–25 radio-marked animals. Home range estimates may need 50–200 or more locations per animal per season, with 20 or more animals. [[Powell et al. (2000b)]] suggested at least 25 animals per season and geographic stratum for survival, movement, and capture rate estimates.

9. **Sampling intensity is rarely met.** Almost no published radiotelemetry studies reached both 20 animals and 50 locations per animal. Home range studies typically have far fewer than 200 locations per animal.

10. **GPS studies tend to track few animals.** GPS collars are expensive, so studies often collar few animals intensively. Such designs suit individual home ranges but are usually insufficient for population inference. The [[LORAN-C]] system described by [[Rowland et al. (1998)]] tracked up to 118 animals per month, averaging more than 235 locations per animal per month, from 1992 to 1996.

11. **Biased capture sites.** Traps placed along roads can oversample animals near roads and undersample those far from them. This matters for any study of roads or human activity.

12. **Marking and relocation can change behavior and survival.** Effects vary by species and marking method. Relocation attempts can cause nest abandonment or increase predation on avian nests. The authors call for a literature review before each study.

13. **Location error must be measured.** Error estimates reported in the chapter include:
   - Direct observation with hand-held GPS: as small as 1 m.
   - Triangulation: up to 500–1000 m.
   - LORAN-C automated system: mean 53 m (SE = 5.9) ([[Findholt et al. (1996)]]).
   - GPS tracking: median 51–74 m ([[Rempel et al. (1995)]]).
   - Small satellite transmitters: up to 3500 m ([[Britten et al. (1999)]]).

14. **Location error should be mapped and accounted for.** Point estimates from automated locations usually gave accurate resource use estimates. Weighting resource values by the probability distribution of location error is also possible. In the authors' example, Habitat 2 had the highest probability of containing the location (75%), followed by Habitat 1 (15%) and Habitat 3 (10%).

15. **Habitat map errors need validation.** Habitat maps can have classification errors of 50% or higher. Classification accuracy of 70% or more is often considered acceptable for landscape-scale mapping. Errors from mapping and from locations should be analyzed together.

16. **Observation rate varies spatially.** Observation rates for automated systems can range from 0% to 100%.
   - [[Rempel et al. (1995)]]: GPS observation rates of 10–92%, lower in dense forest.
   - [[Rumble and Lindzey (1997)]]: GPS rates usually under 10% in the densest stands and often over 50% in the least dense.
   - [[Johnson et al. (1998)]]: LORAN-C observation rates decline with canopy closure, slope, and concave topography. Kriging models predicted this bias reliably.

   The authors describe a five-step correction: place transmitters in a representative random or stratified design, attempt locations with the planned sampling scheme, model observation rate spatially, validate the model, and correct each pixel or polygon.

17. **Biological significance matters more than statistical significance.** The authors say studies should ask three questions: whether the response reflects demographic, social, or economic quantities; what magnitude of change is biologically important; and what broader research context gives that change meaning. For the cowbird example, a survival difference of 0.57 versus 0.51 would need a population model to judge its importance.

18. **Link animal choice to demographic outcomes.** The authors propose combining resource selection and home range data with survival, reproduction, and [[Individual Fitness]] to estimate population growth by habitat. They note this approach needs more resources, longer studies, larger spatial scales, automated tracking, and new analytical skills.

19. **Metapopulation framing.** Using [[Levins (1969)]] and [[Pulliam (1988)]], source habitats produce emigrants that sustain sink habitats. Radiotelemetry can help map and validate sources and sinks, which would be more informative than labeling habitats as "selected" or "avoided."

20. **Summary of priorities.** Study purpose, degree of manipulation, unbiased sampling, a clear sample unit, adequate sample size, bias removal, and explicit biological significance are the central design factors. The authors urge practitioners to pursue integrated analyses of animal choice and demographic consequences.