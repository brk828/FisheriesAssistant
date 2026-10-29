---
species: Strix occidentalis lucida
common_name: Mexican Spotted Owl
family: N/A
habitat: Mixed-conifer and ponderosa pine forest patches embedded in desert, grassland and pinyon-juniper matrix
ocean_basin: N/A
location: Southwestern United States (Arizona, Colorado, New Mexico, Utah)
tags: [landscape-ecology, habitat-connectivity, percolation-theory, conservation-biology, strix-occidentalis-lucida]
title: "Detecing critical scales in fragmented landscapes"
source_id: "17917"
minckley_id: "17917"
source_citation: "T. H. Keitt, D. L. Urban and B. T. Milne (1997). Detecing critical scales in fragmented landscapes. Conservation Ecology (online) 1(1): 4. Minckley Library ID: 17917."
source_file: "17917.pdf"
text_extraction: "ocr"
---
# Detecting Critical Scales in Fragmented Landscapes

#conservation-ecology #landscape-ecology #strix-occidentalis-lucida

## Executive Summary

This methodological paper develops a multiscale framework for quantifying [[Habitat Connectivity]] and for ranking habitat patches by their contribution to it. The habitat mosaic is represented as a mathematical [[Landscape Graph]], and [[Percolation Theory]] is extended to non-uniform, distance-dependent connections. Using forest cover data from the southwestern United States, the authors show that connectivity is strongly scale dependent, with an abrupt transition at a characteristic distance. Landscape sensitivity to patch removal also peaks near that transition, and a small set of "[[Stepping Stone Patches]]" can disproportionately affect connectivity. The work was motivated by the recovery planning of the [[Mexican Spotted Owl]].

## Background & Description

The authors argue that landscape pattern acts as a scale-dependent filter on animal movement. Species with long-range dispersal perceive a given habitat arrangement as more connected than species with short-range dispersal. In highly fragmented landscapes, this filter may act abruptly, isolating species on individual patches when the perceived scale falls below a critical value (Merriam 1984; Gardner et al. 1989; Noss 1991).

Connectivity also depends on configuration, including heterogeneity in habitat quality, patch shape and size, and isolation (Gustafson and Gardner 1996). The authors note that landscape-wide averages are useful for comparing ecosystems but give little insight into local connectivity structure. The study therefore combines:

- aggregate measures of landscape connectivity;
- patch-based measures of individual contributions;
- sensitivity analysis of connectivity to configuration change; and
- the relationship between sensitivity and scale.

**Study area and data.** The study region covered roughly 1.5 × 10^5 km² across Arizona, Colorado, New Mexico and Utah. The region is mostly desert, rocky canyons, semiarid grassland and pinyon-juniper woodland, with mountain ranges supporting conifer and deciduous forest. From a digital cover map (Evans et al. 1993; Evans and Zhu 1993), two forest types were selected as habitat: [[Mixed-Conifer Forest]] (dominated by Douglas-fir, white fir and several pines) and [[Ponderosa Pine Forest]] (dominated by *Pinus ponderosa*, possibly including pine-oak woodland). All other cover types were treated as nonhabitat. The grid resolution was 1 km × 1 km.

The forest type selection approximated suitable nesting habitat for the Mexican Spotted Owl, and the data were used in its recovery plan (Keitt et al. 1995; USDI Fish and Wildlife Service 1995).

**Graph construction.** Habitat cells were grouped into patches using four-directional and diagonal adjacency. Each patch became a graph vertex, placed at its geometric center. Edges were added between patches whose minimum separation fell below a threshold. Connected sets of vertices form subgraphs, or habitat clusters. The authors describe this as an objective alternative to earlier subjective graph assignments (Cantwell and Forman 1993).

**Noise filtering.** The initial labeling produced more than 6,000 patches, many of them single cells likely caused by classification error. Using [[Neutral Models]] (Gardner et al. 1987), the authors found that the forest data covered about 38% of the map, and that roughly 50% of its patches were single-cell patches. A random map with 18% cover produced the same proportion, so an 18% error rate could account for all single-cell patches. Forest and random-noise patch-size distributions matched up to about 10 km² (based on 100 random maps at 18% density). Only patches larger than 10 km² were retained.

**Connectivity measures.**
- *Radius of gyration* gives cluster size in distance units, computed from cell coordinates.
- *Correlation length* is the size-weighted average cluster radius across the landscape, interpreted as the average distance an individual can disperse before reaching a barrier. It increases as connectivity increases.
- *Normalized importance index* measures the change in correlation length when a patch is removed, relative to the full landscape value.
- *Per-area importance index* divides the patch's importance by its number of habitat cells, giving a per-area measure of contribution.

## Ecological & Environmental Context

Standard lattice percolation places occupied cells with probability p, and a spanning cluster emerges at a critical probability. For four-directional connections the critical value is 0.5928 (Stauffer and Aharony 1985). The authors extend this to [[Bond Percolation]] on graphs, where connection probability depends on inter-patch distance. The critical threshold therefore becomes a critical mean dispersal distance rather than a critical habitat density.

Two dispersal formulations are used:

1. **Threshold (step) function.** Patches are connected if their minimum distance is at or below a threshold d_thresh. Each threshold yields exactly one graph.
2. **Cumulative negative exponential.** The probability of dispersing at least distance d is e^(−kd), where k is the dispersal coefficient and 1/k is the mean dispersal distance. Because many graph configurations are possible, the authors use a [[Monte Carlo Simulation]] approach with 100 random configurations per k. They vary k from 1.0 (mean dispersal 1 km) to 0.01 (mean dispersal 100 km).

Connectivity at a given scale is thus a function of dispersal capacity, and the authors frame this as a "filter" effect on species with different [[Dispersal Ability]] (vagility).

## Key Findings

**1. Connectivity is strongly scale dependent, with a phase transition.**
- At a 20 km threshold, the landscape was largely independent patches and small clusters.
- At 40 km, larger subgraphs formed but the landscape remained divided.
- Above 40 km most habitat became connected. At 50 km nearly all habitat was joined, but only one edge linked the large northeastern and southwestern subgraphs.
- At 80 km the graph was highly interconnected, with many alternative pathways.
- Between 40 and 45 km the correlation length nearly doubled, from about 150 km to about 275 km. The authors interpret this as a geometric phase transition, dividing the landscape into connected and disconnected phases.

**2. Landscape sensitivity is scale dependent and peaks at the transition.**
- At short thresholds (0 km, all patches independent), patch removal effects were dominated by the largest patch, with shape possibly contributing.
- At 30 and 40 km, several of the largest patches drove large changes when removed. Patch size was the main determinant of importance.
- At 45 and 50 km, the pattern changed abruptly. Several much smaller patches produced large sensitivity spikes. These patches act as **stepping stones** and correspond to articulation points in the graph. Their importance reflects connective role, not size.

**3. Averaging across scales gives a more robust ranking.**
Because the appropriate scale is uncertain, the authors averaged importance over thresholds from 0 to 100 km in 5-km steps. The averaged pattern resembled that at 45 km but included a broader set of patches, reflecting local percolation transitions at other scales.

**4. Connectivity under stochastic dispersal is nonlinear.**
Varying the dispersal coefficient from k = 0.01 (long-range) to k = 1.0 (short-range) produced a strongly nonlinear relationship with connectivity, with a clear inflection at intermediate values. The distribution of correlation lengths also split into connected and disconnected phases.

**5. Implications for conservation.**
The authors conclude that habitat preservation for threatened species should account for critical scales and for stepping-stone patches, because removing a small number of key patches can disproportionately fragment the landscape. Landscape-wide indices alone can miss these local structures.