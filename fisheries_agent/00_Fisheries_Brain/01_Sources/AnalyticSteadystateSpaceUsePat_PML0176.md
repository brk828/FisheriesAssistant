---
species: "Canis latrans (coyote); Cervus canadensis (elk)"
common_name: "Coyote; Elk"
family: N/A
habitat: "Mesic grassland and valley habitats (Lamar Valley, Yellowstone); general heterogeneous landscapes"
ocean_basin: N/A
location: "Yellowstone National Park, USA"
tags: [mammalogy, mathematical-biology, home-range, animal-movement, steady-state]
title: "Analytic steady-state space use patterns and rapid computations in mechanistic home range analysis"
source_id: "PML0176"
marsh_id: "PML0176"
library: "Marsh Library"
permission: "not public domain"
source_citation: "A. H. Barnett, P. R. Moorcroft (2008). Analytic steady-state space use patterns and rapid computations in mechanistic home range analysis. Journal of Mathematical Biology, 57:139-159. Marsh Library ID: PML0176."
source_file: "Barnett A.H. et al. 2007. Analytic steady state space use patterns and rapid computations in mechanistic home range analysis.pdf"
text_extraction: "text"
---
# Analytic Steady-State Space Use Patterns and Rapid Computations in Mechanistic Home Range Analysis

#mammalogy #mathematical-biology #canidae

## Executive Summary

This mathematical biology paper develops a stochastic, spatially explicit model of animal movement, the mechanistic RSA (MERSA) model, in which an individual's next move is biased by the habitat preference of its local surroundings within a length scale L. The authors derive a closed-form steady-state probability density function (pdf) for space use using a factorization of the redistribution operator. The formula shows that space use scales linearly with habitat preference when L is large relative to habitat features, and quadratically when L is small. The factorization also permits very fast numerical simulation, which the authors expect will speed up parameter fitting. The study is theoretical, with no new field data; its examples draw on coyote movement and small-mammal prey data from [[Yellowstone National Park]].

## Background & Description

- **Motivation:** Habitat shapes food, shelter, mate and predation risk, so space use reflects the spatial layout of habitat types. The paper addresses how to model this relationship mechanistically rather than descriptively.
- **Existing approach:** [[Resource Selection Analysis]] (RSA) is a statistical regression of space use against habitat availability. It treats movement speed only implicitly and typically defines available habitat as a fixed area or a buffer around the animal.
- **Alternative approach:** [[Mechanistic Home Range Model]]s simulate individual movement as a Markov process and yield a pdf of space use. Long-term predictions usually require evolving a continuous-time partial differential equation to steady state, which is computationally costly.
- **Prior work:** A [[Coyote]] home range model in Yellowstone used a "prey availability plus conspecific avoidance" (PA+CA) formulation. Earlier work by the same authors reconciled MERSA with RSA for one-dimensional movement, using an [[Advection-Diffusion Equation]] limit.
- **Model structure:** The redistribution kernel is an advection-free jump kernel multiplied by the preference function and normalized. The kernel is exponential in both 1D and 2D. The authors note that a typical sampling interval for coyotes is 10 min.

## Ecological & Environmental Context

- **Scale dependence:** The key parameter is the kernel width L, which is both the typical step length and the perceptual distance over which the animal senses habitat. Results depend on whether L is large or small compared with the spatial scale of habitat features.
- **Small-L limit:** Fine-scale habitat features are smoothed out, and steady-state use is proportional to the square of preference. This reproduces the advection-diffusion result.
- **Large-L limit:** Space use is proportional to preference, which matches traditional RSA with no restriction on available habitat.
- **Habitat discontinuities:** At boundaries between habitat types, the pdf jumps by a ratio equal to the square of the preference ratio when viewed on fine scales (within about L of the boundary). On larger scales the jump is a ratio of the preference values. The authors derive effective matching conditions for coupled advection-diffusion equations.
- **Case study setting:** A 2D preference function is built from small-mammal biomass (mice, ground squirrels, pocket gophers and red-backed voles) across six habitat types in the Lamar Valley region. A mesic grassland strip following the valley floor has the highest abundance.

## Key Findings

1. **Closed-form steady state:** The steady-state pdf is u* ∝ w(x)·z(x), where z is the preference function smoothed by the kernel. This is valid for any preference function and any symmetric kernel, provided preference is positive everywhere.
2. **Operator factorization:** The redistribution operator factors as W Φ W⁻¹ Z, where Φ is symmetric. This gives detailed balance and real eigenvalues.
3. **Geometry-dependent scaling:** Space use is linear in preference when L is large compared with habitat features and quadratic when L is small.
4. **1D results:** For a 1D preference function on the unit interval, the analytic formula was computed in a few thousandths of a second on a grid of N = 400 points. Time stepping with dense matrix multiplication took 0.0005 s per step.
5. **2D results:** On a grid of N = 8,591 points (0.1 km spacing over a 7 km × 12 km domain), a steady-state solve took 0.009 s using FFT convolution. This is 10 to 1,000 times faster than iterative eigenvector computation, where one dense matrix application takes 0.45 s. A 200 × 200 grid (N = 40,000) required 0.025 s; the dense-matrix alternative would need about 12 GB of memory.
6. **Time evolution:** A 2D simulation with N ≈ 10⁴ ran at 0.008 s per time step, fast enough for interactive animation at 30 frames/s.
7. **Parameter effects in 2D:** Decreasing L (6, 0.7, 0.1) concentrates space use more strongly in high-preference grassland. With L = 0.7, use in the wider western grassland rises while the narrower eastern section changes little. This geometric effect is not captured by traditional RSA.
8. **Discontinuities:** At a sharp habitat boundary, the local steady-state shape equilibrates in about one time step. Effective boundary conditions are proposed on the basis of separation of length and time scales. The authors state that this argument is non-rigorous and suggest matched asymptotic expansions as future work.
9. **Implication for RSA:** Using too large a buffer in RSA overestimates the strength of habitat preference. The authors suggest that fitting unified mechanistic models, such as those of Forester et al., would address this.
10. **Limitations and future work:** The paper does not perform inference from real animal location data. It notes that the factorization is special to the algebraic structure of the model and does not extend to general kernels. Extensions to non-linear models, such as density-dependent diffusion and chemotaxis, are proposed but not tested.