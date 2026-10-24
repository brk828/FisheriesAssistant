---
species: N/A
common_name: N/A
family: N/A
habitat: Freshwater lakes (Great Lakes, Lake Huron, Lake Erie)
ocean_basin: N/A
location: Great Lakes, Canada/USA; Lake Huron (Baie du Doré); western basin of Lake Erie
tags: [limnology, freshwater-ecology, turbulent-diffusion, effluent-dispersal, great-lakes]
title: "Dispersal of foreign matter by the currents and eddies of the Great Lakes"
source_id: "18087"
minckley_id: "18087"
source_citation: "G. T. Csanady (1966). Dispersal of foreign matter by the currents and eddies of the Great Lakes. Great Lakes Research Division, University of Michigan 15: 283-294. Minckley Library ID: 18087."
source_file: "18087.pdf"
text_extraction: "ocr"
---
# Dispersal of Foreign Matter by the Currents and Eddies of the Great Lakes

#limnology #freshwater-ecology #turbulent-diffusion

## Executive Summary

This paper, presented at a Great Lakes research conference, reviews the University of Waterloo group's work on how pollutants spread through the Great Lakes. It argues that effluent concentrations are random variables, so engineering estimates should rely on statistics beyond the mean, chiefly the [[Peak Concentration]] and the standard deviation of fluctuations. Dye-plume experiments in [[Lake Huron]] and [[Lake Erie]] quantify horizontal and vertical [[Eddy Diffusivity]], and the author uses them to estimate the [[Dilution Factor]] for three hypothetical industrial outfalls. The main conclusion is that a large lake is a weak dispersal agent. Even at 1 km from a discharge, dilution for small plants is only about 30:1 or less, and the author calls for a lake "climatology" of currents, deeper study of peak-to-mean behaviour, and full-scale outfall studies.

## Background & Description

The Great Lakes and their connecting channels were widely used for waste disposal, yet until the mid-1960s there was almost no experimental information on how pollutants dispersed in them. The author separates the problem into two parts: (1) a "climatology" of lake currents and eddies, and (2) the dispersal process for a given current and eddy structure. The Waterloo group focused on the second part, studying the fundamental physics of [[Turbulent Diffusion]] with direct engineering relevance.

Because a diffusing cloud's path and spread depend on the eddies it happens to encounter, exact prediction of an individual cloud is impractical. The paper therefore frames the problem statistically:

- **Mean concentration:** Classical turbulent diffusion theory has mostly addressed the mean concentration field, which the author calls only a "very rough and ready" description.
- **Probability distributions:** Full distributions need many replicate releases under identical conditions, which is hard in the natural environment. A mean can be estimated from about 25 observations, but reliable frequencies across 10 concentration intervals need over 100.
- **Peak concentration:** Engineering interest centres on a peak, defined as the value exceeded 90% or 99% of the time. By analogy with [[Gaussian Profile]] wind-gust rules (peak = mean + two standard deviations), the standard deviation of fluctuations is nearly as important as the mean.

Two frames of reference are distinguished. [[Absolute Diffusion]] uses a fixed frame, appropriate for air pollution affecting a fixed receptor. [[Relative Diffusion]] uses a frame moving with the cloud's centre of gravity, which is the natural choice in lakes. The author notes that meandering "smears" the fixed-frame profile, so the relative-frame spread is narrower.

The experimental base is a continuous Rhodamine-B dye plume released from a point source off the [[Baie du Doré]] research station of the Great Lakes Institute, University of Toronto. Fluorometer traces were taken from a boat crossing the plume near the surface. Twenty-five profiles from one 1965 experiment, in a steady current at a fixed distance from the source, were overlapped on their centres of gravity. The author's notation covers the mean profile f̄(y), the mean-square fluctuation s²(y), and the [[Richardson Distance-Neighbour Function]] g(η), which is a smoothing operation related to [[Batchelor Theory]] of relative dispersion.

## Ecological & Environmental Context

The study addresses physical limnology rather than biology, but it has direct ecological implications. Effluent dispersal controls the concentrations that water bodies and their users are exposed to near outfalls.

**Variability in the plume.** Individual profiles differed, and total dye per profile varied from run to run. The author attributes this to random variation in the speed of each parcel discharged by the continuous source, which gives the plume an irregular outline.

**Eddy scales.** Steady, uniform currents in Lake Huron showed a Lagrangian scale of about 10 m and a root-mean-square turbulent velocity of about 0.5 cm/s (about 2.5% of the typical current speed). Dye plumes also showed meandering from very large eddies, several hundred metres across. The author infers a gap in the [[Eddy Spectrum]] between roughly 10 m and 100 m.

**Vertical structure.** Vertical mixing depends on turbulence from [[Wind-Driven Turbulence]] (direct momentum transfer) and surface cooling (convection). A stable [[Thermocline]] suppresses turbulence, creating a [[Diffusion Floor]]. During calm July periods, such floors occurred as close to the surface as 1 m, even with temperature drops of only a few degrees. Light winds in geostrophic or gradient currents, such as those following wind set-up or a [[Seiche]] in a calm evening, can leave turbulence nearly absent, so a low vertical diffusivity is not offset by high lateral diffusivity.

**Shear effects.** Where the current direction changes with depth, lateral diffusivity may rise by a factor of 2 to 3. However, the associated poor vertical mixing reduces the vertical diffusivity, so the two effects largely cancel in their influence on peak concentrations.

## Key Findings

**1. Statistical framing.** Pollutant concentrations are random. Engineering estimates should combine mean concentration, standard deviation (variance) of fluctuations, and some information on the probability distribution.

**2. Plume profile.** In the 25-run Lake Huron experiment, the mean profile was close to Gaussian in shape with the same zeroth and second moments as the observed data. The author considers a Gaussian working hypothesis "very good." Deviations were irregular and attributed to the small sample.

**3. Peak estimate.** The maximum mean concentration was f̄(0) = 5.06 fluorometer units. The maximum root-mean-square fluctuation was about 60% of this value. Using peak = maximum mean + two standard deviations gives a predicted peak of 11.1 units. The observed peak reading was 10.3 units, about 2.0 f̄(0). The author accepts "peak ≈ 2 × maximum mean" for engineering estimates, while noting that more data are needed.

**4. Fluctuation near the fringes.** The ratio of root-mean-square fluctuation to local mean rises steeply near the plume edges, which the author links to laboratory observations. Fringe fluctuations are therefore dominant.

**5. Spread with distance.** The [[Relative Diffusion]] phases proceed as follows. Initial spread is slow, then accelerates into a "quasi-asymptotic" phase (growing as x^(3/2) per the cited theory). The quasi-asymptotic phase ends near x ≈ 500 m, when the plume's lateral standard deviation S_y is about 25 m. After that, a nearly constant eddy diffusivity applies. Estimates from mass-balance checks were typically within a ratio of 3:2.

**6. Effective diffusivities.**
- Lake Huron, 1–2 km from source, steady uniform currents: K_y ≈ 500 cm/s (horizontal).
- Western basin of Lake Erie, moderate distances: K_y ≈ 1000 cm/s.
- Shear-induced lateral increase: factor of 2 to 3.

**7. Jet initial dilution.** For a jet discharged at 5 ft/s into a 0.5 ft/s background, the jet must slow about tenfold. Standard deviations at the end of this initial mixing are approximately six times the initial jet width and depth. Dispersion parameters scale linearly with discharge velocity for other velocity ratios.

**8. Dilution estimate.** The dilution factor at 1 km is c/c_j = α·D/(U·σ_y·σ_z), where α ≈ 0.64 (Gaussian profiles with peak = 2 × maximum mean). Table 1 gives typical Lake Huron values at 1000 m:

| Lake condition | U (cm/s) | S_y (cm) | S_z (cm) |
|---|---|---|---|
| (a) Stable stratification, calm July days | 10 | 4500 | 100 |
| (b) Gradient current, no cooling (calm-evening seiche) | 20 | 1750 | 100 |
| (c) Good surface cooling (brisk, cool wind) | 20 | 2250 | 350 |

**9. Plant comparison.** Three hypothetical plants were assessed. Table 2 gives dilution factors (fraction of initial concentration) at 1 km:

| Plant | Efflux velocity | Channel | (a) Calm July | (b) Seiche | (c) Brisk wind |
|---|---|---|---|---|---|
| 1 | 5 ft/s | 26 × 13 ft | 0.101 | 0.214 | 0.198 |
| 2 | 1 ft/s | 10 × 10 ft | 0.0130 | 0.0310 | 0.0252 |
| 3 | 10 ft/s | 2 × 2 ft | 0.0147 | 0.0363 | 0.0245 |

The text states that even the smallest plants dilute only about 30:1, and that the large-discharge plant achieves about 5:1. Dilution factors are nearly constant across conditions. Condition (a) gives the most favourable results, partly because diffusion floors were ignored.

**10. Practical guidance.** The author recommends that outfalls in quiet currents might use grid-like structures to generate turbulence. Large volumes of cooling or process water could be pumped through to achieve dilution before discharge. The author stresses that the rules of thumb rest on incomplete evidence.

**11. Research priorities.**
1. Establish a "climatology" of currents and eddies for the Lakes, differing by lake and by portion of each lake, through government agencies.
2. Study the fundamental mechanics of turbulent diffusion, especially peak-to-mean ratios, and diffusion constants at 10 km or more from the source.
3. Conduct full-scale outfall studies, including at [[Douglas Point Power Station]] with [[Atomic Energy of Canada Limited]] support, and controlled studies on efflux channels of varying size and velocity.

**Acknowledgments.** The work used facilities of the [[Great Lakes Institute]] and was supported by Atomic Energy of Canada Limited and the [[National Research Council of Canada]] (grant A 1820).