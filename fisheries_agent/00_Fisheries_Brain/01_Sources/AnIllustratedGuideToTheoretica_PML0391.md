---
species: "Linepithema humile; Ondatra zibethicus"
common_name: "Argentine ant; Muskrat"
family: "N/A"
habitat: "Old-field and wetland systems (Argentine ant spread in an old field; muskrat in Bohemian waterways); general population models"
ocean_basin: "N/A"
location: "Prague, Bohemia; San Diego, California; Olympic Peninsula, Washington; Baltimore/Washington, D.C.; North America"
tags: [population-ecology, theoretical-ecology, mathematical-modelling]
title: "An Illustrated Guide to Theoretical Ecology"
source_id: "PML0391"
marsh_id: "PML0391"
library: "Marsh Library"
permission: "not public domain"
source_citation: "T. J. Case (2000). An Illustrated Guide to Theoretical Ecology. Marsh Library ID: PML0391."
source_file: "Case T.J. 2000. theoretical ecology.pdf"
text_extraction: "mixed"
---
# Exponential and Geometric Population Growth, Dispersal, and Variation in Vital Rates

#population-ecology #theoretical-ecology #mathematical-modelling

## Executive Summary

This note covers chapters 1 and 2 of [[An Illustrated Guide to Theoretical Ecology]] by Ted J. Case (Oxford University Press, 2000), together with the publisher's errata list. The chapters develop the mathematics of unrestricted population growth in discrete and continuous time, then extend the models to spatial spread through [[Diffusion]] and to variability in birth and death rates. The errata page lists corrections to equations, worked answers, figure captions and references, dated last updated 14 February 2004. The text is not a fish or aquatic research study. Its aquatic content is limited to the [[Muskrat]] invasion in Bohemia, and the [[Argentine Ant]] spread appears as an example of invasion.

## Background & Description

The book is organised in parts, with Part I covering population ecology. Chapter 1 introduces [[Exponential Growth]] and [[Geometric Growth]]. Chapter 2 covers [[Random Walk]] movement, diffusion, and the effects of individual and temporal variation.

Two modelling frameworks are compared:
- **Discrete time** uses a difference equation, N(t+1) = R·N(t), with net per-capita rate R. The geometric rate is λ = R + 1 and N(t) = N₀λᵗ (Eq. 1.3a).
- **Continuous time** uses a differential equation, dN/dt = rN(t), with intrinsic rate r. The solution is N(t) = N₀eʳᵗ (Eq. 1.3b).

Case notes that most species lie between these extremes, and either framework can be used with minor error if the approximation is recognised.

## Ecological & Environmental Context

**Exponential growth in practice.** Exponential growth is approximated only temporarily, when species are introduced to new places with abundant resources and few natural enemies. The text uses US population growth (1790 to 1995) as a case: after log transformation, the regression slope of about 0.02 (~2% per year) shows that the growth rate has been declining.

**Diffusion and spread.** Dispersal by random walk produces a Gaussian spread. Mean displacement scales with the square root of time, and the occupied area grows linearly with time in two dimensions.

**Patchy habitat.** Favourable patches can act as source populations, subsidising sink populations in unfavourable surrounding cells. Small patches with high dispersal and high isolation can drive populations to extinction, which makes highly motile species hard to conserve in small reserves.

**Environmental variation.** Temporal variability in growth rate (for example, a population multiplying by 1.5 in one year and 0.5 in the next) lowers the geometric mean, which governs long-term persistence, even when the arithmetic mean exceeds 1.

## Key Findings

### Growth models and worked examples

- **Continuous versus discrete rates:** R = eʳ − 1 converts a continuous rate to a discrete one. For r = 0.2, R = 0.2214 (22.14%). Annual yield 22.14% corresponds to an annual rate of 20%.
- **Doubling time:** For exponential growth, t₂ = ln2 / r. At 2% per year the doubling time is 34.7 years. At 1% per year it is 69 years. Doubling time is independent of initial population size.
- **Rabbit introduction:** 100 rabbits with λ = 1.35 per year, starting in 1995, give 371 rabbits in 2000 and 1379 in 2005. The discrete and continuous forms agree when e^r = λ.
- **Mountain goats (Olympic Peninsula):** Population rose from 12 individuals (1929) to 1175 (1983) per Houston et al. (1994). This is a textbook exercise, and no value of r is given in the text.
- **Lily pads:** Doubling daily from one pad fills a pond holding 10⁸ pads on day 30 and is still not full on day 29.
- **Petroleum depletion:** With consumption growing 2% per year and r = 0.0198 per year, the text estimates reserves of 11.11 billion barrels would be exhausted by about 2027 (consumption 17.163 billion barrels per year as of 1995).

### Spatial spread and diffusion

- **Diffusion:** Under discrete diffusion with fraction d = 0.1 moving each way per time step, the population distributes evenly over time. With 2000 individuals initially in two central cells, the distribution flattens to 100 individuals per cell.
- **Scaling:** Mean displacement ∝ √t. Range (95% of individuals) = 2σ = 2√(2Dt). The occupied area is proportional to time in two dimensions.
- **Diffusion coefficient:** D = d in discrete space, and D = ⟨r²⟩/4t in two dimensions. For a small molecule in water, D ≈ 10⁻⁵ cm²/s.
- **Diffusion with growth:** The asymptotic rate of spread of the radius is 2√(rD). The occupied radius grows at a constant rate, while doubling D does not double the rate of advance.
- **Muskrat invasion:** Muskrats escaped near Prague in 1905. Spread was roughly constant, about 11.8 km/yr per the Figure 2.10 legend, which the text rounds to "about 12 km/yr".
- **Argentine ants:** Spread in an old field near San Diego, California (Erickson 1971) averages about 100 m per year, because colonies bud rather than disperse by flight. Table 2.1 lists observed velocities for other invasions, for example gypsy moth (*Lymantria dispar*), cabbage butterfly (*Pieris rapae*), and muskrat, ranging from 0.9 to about 400 km/yr. The table and text disagree on the Argentine ant rate, so the text value should be checked against the table.

### Patch size and dispersal

- Emigration from a patch scales with its edge (perimeter), so larger patches have proportionally fewer emigrants.
- For a circular patch, S = 2(πA)^0.5. The population grows only if λ(1 − ke·w/√A)... exceeds 1. Growth is easier to achieve as area increases and as the emigration rate e decreases.

### Individual and temporal variation

- **Geometric mean criterion:** When λ varies over time, the geometric mean (not the arithmetic mean) gives net growth. Example: two populations with λ = 1.5 in both years but different sequences: population A (λ = 1 then 2) reaches 2N₀, while population B reaches 2.25N₀ even though both have arithmetic mean 1.5.
- **Extinction example:** A bird population has a 50% chance of +20% and a 50% chance of −20% per year. The geometric mean is 0.9798, so the population becomes extinct.
- **Uniform λ between 0.5 and 1.5:** The arithmetic mean is 1 and the geometric mean is about 0.956 (exact) or 0.959 (approximation).
- **Uniform λ between 0.55 and 1.65:** The arithmetic mean is 1.1 and the geometric mean is about 1.055. Populations tend to increase even though some still decline.
- **Uniform λ between 0.1 and 2.1:** The arithmetic mean is 1.1 but the geometric mean is below 1. Starting from 2 individuals, the mean expected N after 50 years is 234.7 (realized mean 277.4), yet most replicates go extinct. Expected mean growth can coexist with near-certain extinction.
- **Environmental variance:** Higher temporal variance in λ lowers the geometric mean growth rate. Small populations face greater chance-extinction risk.
- **Central Limit Theorem:** The sum of N independent individual rates is approximately normal, and the standard error of the mean is σ/√N.

### Errata (2004 update)

The errata page lists roughly 60 corrections to the first printing. Most are typographical, but several affect results or worked answers. Key corrections include:
- The first Chapter 1 worked answer should be 1091 years, not the printed figure.
- Equation 4.16 exponent, Box 5.1 logistic denominator (K, not N).
- Box 9.10 and 9.11 subscript and notation fixes.
- Muskrat and other dispersal rates should be checked against the errata for Table 2.1.
- Dennis and Taper reference should read *Ecological Monographs* 64: 205–224.
- Several question answers for Chapter 2 and 10 exercises, including a corrected catchability constant C = 0.001 per boat.

Users should consult the original errata page for the full list and corrected equations.

---
*Note: Obsidian cross-links for this note: [[Exponential Growth]], [[Geometric Growth]], [[Random Walk]], [[Diffusion]], [[Muskrat]], [[Argentine Ant]], [[Geometric Mean]], [[Doubling Time]], [[Environmental Variance]], [[Patch Size]], [[Emigration]], [[Central Limit Theorem]].*