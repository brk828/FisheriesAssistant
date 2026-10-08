---
species: ["Coho Salmon", "Chinook Salmon", "Rainbow Trout", "Lake Trout", "Kamloop Trout", "Splake", "Cutthroat Trout", "Steelhead"]
family: Salmonidae
habitat: "Hatchery raceways, ponds, and tanks (freshwater aquaculture systems)"
ocean_basin: "N/A (freshwater hatchery study; species anadromous/Pacific Northwest origin)"
source_id: "12413"
---

# Water Requirements of Salmonids

#ichthyology #marine-biology #Salmonidae #aquaculture #fish-hatchery-science

## Executive Summary

This 1971 engineering paper by Paul B. Liao (Kramer, Chin & Mayo Consulting Engineers) establishes a quantitative model for determining the water supply requirements of salmonid fish hatcheries. Based on over 300 individual field tests conducted at hatcheries in Washington, Oregon, Idaho, Colorado, and Minnesota, the author derives empirical equations relating **oxygen uptake rate**, **water temperature**, **fish size**, **dissolved oxygen saturation**, and **altitude** to the **carrying capacity** (lbs. fish/gpm) of a hatchery water supply. The work critiques and builds upon earlier models (Elliott 1969; Burrows & Combs 1968; Willoughby 1968; Westers 1970), arguing that prior methods neglected key variables such as initial dissolved oxygen content, altitude, and hydraulic pond patterns. The paper provides worked examples and design graphs ([[Figure 1 Oxygen Consumption Curves]], [[Figure 2 Required Flow Volume Chart]]) intended for direct use in [[Salmonid Hatchery Design]].

## Background & Description

This paper is not a morphological study; it does not describe anatomical features of salmonids. Physiological parameters relevant to respiration and metabolism are covered instead:

- **Fish size range tested**: 0.05 lb./fish and broader ranges implied by Table 1 constants; Elliott's referenced work covered 1.85–17.5 g/fish for [[Chinook Salmon]].
- **Species tested**:
  - **Salmon**: [[Coho Salmon]], [[Chinook Salmon]]
  - **Trout**: [[Rainbow Trout]], [[Lake Trout]], [[Kamloop Trout]], [[Splake]], [[Cutthroat Trout]], [[Steelhead]]
- **Loading density range observed**: 0.069 to 2.24 lbs./cu.ft. water (average across 300 tests: 0.433 lbs./cu.ft.); 2.0 lbs./cu.ft. is cited as the generally accepted upper limit due to hydraulic and biological constraints.
- Oxygen consumption was found to be systematically **higher in trout than in salmon**, supporting the need for species-specific design criteria (see Table 1 constants below).

## Ecological & Environmental Context

Although framed around artificial hatchery systems rather than natural habitat, the paper documents key physiological-environmental relationships germane to [[Salmonid Respiratory Ecology]]:

- **Water temperature**: Oxygen uptake rate is *directly proportional* to water temperature — higher temperatures drive higher metabolic oxygen demand and thus greater water flow requirements.
- **Fish size**: Oxygen uptake rate (per unit body weight) is *inversely proportional* to fish size — smaller fish have higher mass-specific metabolic rates.
- **Dissolved oxygen (DO) & saturation**: DO concentration in hatchery water is governed by both water temperature and **altitude (elevation)**; higher elevations reduce achievable saturation DO, directly limiting carrying capacity.
- **Activity level**: Modulated by loading density, ambient oxygen concentration, pond hydraulic pattern (e.g., flow-through velocity), and hatchery operations (feeding, cleaning). Higher flow-through velocities (as in modern recirculating raceways) increase fish activity and thus oxygen demand.
- **Catabolic products** (CO₂, NH₃): Elevated CO₂ reduces hemoglobin's oxygen affinity, lowering effective oxygen consumption/uptake — a confound in oxygen-based water requirement models. The paper assumes catabolic products are flushed rapidly under normal hatchery flow conditions.
- **Sex and season**: Oxygen consumption in trout fluctuates seasonally, peaking near spawning; male [[Brook Trout]] show standard oxygen uptake peaks ~1 month before females, reaching levels roughly double that of early spring baseline (cited from Beamish & Dickie 1967 and related sources).
- **Ambient oxygen depletion**: Active oxygen consumption decreases as ambient oxygen is reduced; Basu (1959) demonstrated log-linear decrease in active O₂ consumption with increasing pCO₂.

This positions the salmonid hatchery as an engineered analog of a lotic (flowing-water) ecological niche, where [[Dissolved Oxygen Dynamics]] and [[Water Temperature]] jointly regulate stocking density and fish welfare, echoing constraints found in natural riverine salmonid habitats.

## Key Findings

### Core Empirical Equations

**1. Oxygen Uptake Rate:**
$$O_2 = K \cdot T^n \cdot W^m$$
- $O_2$ = oxygen uptake rate (lbs. O₂/100 lbs. fish/day)
- $T$ = water temperature (°F)
- $W$ = fish size (lb./fish)
- $K, m, n$ = empirically derived species/temperature-specific constants

**2. Dissolved Oxygen Concentration vs. Temperature & Altitude:**
$$C_e = \frac{S \times 132 \times 760}{\left(\frac{0.625T}{T-32.8}\right)\left(760 + \frac{E}{32.8}\right)}$$
- $C_e$ = dissolved oxygen concentration (mg/l) at temperature $T$, altitude $E$
- $S$ = saturation factor of dissolved oxygen
- $E$ = altitude (feet)

**3. Carrying Capacity:**
$$Q = \frac{1.2 (C_e - C)}{O_2}$$
- $Q$ = carrying capacity (lbs. fish/gpm)
- $C$ = minimum acceptable dissolved oxygen in effluent (mg/l)

### Table 1 — Derived Constants (K, m, n) by Species and Temperature

| Group | Temp. Condition | K | n | m |
|---|---|---|---|---|
| **Salmon** | T ≤ 50°F | 7.20 × 10⁻⁵ | -0.194 | 2.120 |
| **Salmon** | T > 50°F | 4.90 × 10⁻⁵ | -0.194 | 2.120 |
| **Trout** | T ≤ 50°F | 1.90 × 10⁻⁶ | -0.138 | 1.855 |
| **Trout** | T > 50°F | 3.05 × 10⁻⁴ | -0.138 | 1.855 |

### Worked Example (from paper)
For 5,000 lbs. of trout (0.05 lb./fish) at 55°F, 90% initial DO saturation, elevation 1,300 ft, minimum effluent DO = 4 mg/l:
- Computed $O_2$ uptake ≈ 0.779 lb. O₂/100 lbs. fish/day
- Computed $C_e$ ≈ 9.25 mg/l
- Computed $Q$ ≈ 8.08 lbs. fish/gpm
- **Total required flow ≈ 619 gpm**

### Critique of Prior Models
- **[[Elliott 1969]]**: Valid only for [[Chinook Salmon]] in narrow size range (1.85–17.5 g); loading density not specified.
- **[[Burrows and Combs 1968]]**: Carrying capacity inversely proportional to temperature, proportional to fish size; disadvantages previously noted by Westers (1970).
- **[[Willoughby 1968]]**: Based on food consumption rates (via Haskell 1955 assumptions); food composition variability introduces inconsistency; species/loading density unspecified.
- **[[Westers 1970]]**: Most complete prior model (relates loading density, carrying capacity, and water exchange rate) but **omits initial oxygen content** and does not account for hydraulic pattern effects on activity/oxygen consumption (e.g., recirculating raceways vs. conventional ponds).

### Design Implications
- Author's equations uniquely incorporate **altitude**, **initial oxygen saturation**, and **species-specific metabolic differences** (trout > salmon in oxygen demand), which prior methods neglected.
- Figures 1 and 2 provide direct design charts for hatcheries at 1,300 ft elevation, 95% initial DO saturation, and minimum effluent DO ≥ 5.0 mg/l; for other conditions, Equations 1–3 with Table 1 constants must be applied.
- Model assumes **acceptable incoming water quality**; effects of poor incoming water quality on requirements were explicitly excluded from scope.

### Related Concepts
[[Dissolved Oxygen Saturation]] · [[Carrying Capacity (Aquaculture)]] · [[Loading Density]] · [[Hatchery Raceway Design]] · [[Fish Metabolic Rate]] · [[Progressive Fish-Culturist]]