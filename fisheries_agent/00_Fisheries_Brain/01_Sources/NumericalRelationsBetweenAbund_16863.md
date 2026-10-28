---
species: "Multiple (predatory and prey fishes, birds, invertebrates)"
family: "Various (Salmonidae, Cyprinidae, Odontaspididae birds excluded; primarily Salmonidae and associated predators)"
habitat: "Freshwater rivers, lakes, and coastal marine spawning areas"
ocean_basin: "North Pacific / North Atlantic (Canada - British Columbia, New Brunswick)"
source_id: "16863"
---

#ichthyology #marine-biology #predator-prey-dynamics #fisheries-management #population-ecology

## Executive Summary

This theoretical paper by W.E. Ricker (Fisheries Research Board of Canada, 1952) develops a conceptual and mathematical framework for understanding how predator abundance influences prey survival, with direct application to fisheries management and predator control programs. Ricker identifies three fundamental types of numerical predator-prey relationships (Types A, B, and C) and derives quantitative relationships—particularly for Type B (random-encounter) predation—showing that the benefits of predator reduction depend strongly on the initial survival rate of prey. The work draws on empirical case studies including [[Sockeye Salmon]] predation at Cultus Lake, British Columbia, and [[Atlantic Salmon]] parr survival in New Brunswick rivers, providing a foundational model still relevant to modern predator control and fisheries stock assessment.

## Background & Description

This is a theoretical/quantitative ecology paper and does not describe specific morphological traits of species in detail. However, it notes a key **physiological distinction** relevant to predation type:

- **Warm-blooded predators** (birds, mammals): Fairly constant food requirements due to thermoregulation needs; high mobility (especially birds) allows rapid relocation to areas of temporary prey abundance (favoring Type A) or abandonment of depleted areas (favoring Type C).
- **Cold-blooded predators** (predatory fishes): Much lower minimum ration requirements per unit body weight; greater flexibility in food consumption; tend to establish Type B (random encounter) predation dynamics, taking prey opportunistically as encountered.

Prey species discussed include:
- **[[Pacific Herring]]**: Forms dense spawning schools (relevant to Type A predation).
- **[[Pink Salmon]]** and **[[Chum Salmon]]**: Newly-emerged fry undergo mass downstream migration, creating temporary high-density aggregations vulnerable to Type A predation.
- **[[Sockeye Salmon]]**: Fingerlings studied at Cultus Lake under Type B predation from squawfish, char, coho, and trout.
- **[[Atlantic Salmon]]**: Parr studied in New Brunswick rivers (Pollett River), exhibiting Type C-like predation dynamics.
- **Cod** (Gadidae): Cited as example of high-fecundity species (~1,000,000 pelagic eggs/female) subject to extreme (~99.9%) larval predation losses.

## Ecological & Environmental Context

Ricker's framework classifies predator-prey ecological interactions into three distinct dynamical regimes based on habitat context and behavioral ecology:

### Type A: Satiation-Limited Predation
- Predators take a **fixed number** of prey regardless of prey abundance (predators become satiated).
- Occurs when prey are **temporarily massed** in unusual densities (e.g., spawning herring schools, migrating salmon fry).
- Cannot persist long-term as the sole predation mode; unsustainable, as consistent Type A pressure would drive predator population growth, shifting the system to Type B or C, or cause prey extermination.

### Type B: Random Encounter (Density-Dependent Proportional) Predation
- Predators consume a **fixed fraction** of available prey, consistent with random encounter rates.
- Can persist over extended periods and constitute a major portion of predator diet.
- **Case study**: [[Cultus Lake]] system (British Columbia) — predation by squawfish, char, coho, and trout on fingerling [[Sockeye Salmon]] across a wide range of prey abundance (Foerster & Ricker, 1941).
- This is the dynamic most amenable to Ricker's mathematical modeling (see Key Findings).

### Type C: Threshold/Refuge-Limited Predation
- Predators remove prey **in excess of a fixed minimum number** that can survive (e.g., due to limited secure habitat/territorial refugia, or predators abandoning areas once foraging becomes unrewarding).
- Survival is **largely independent of initial prey abundance** — analogous to Errington's bobwhite quail studies in Iowa.
- **Case study**: [[Atlantic Salmon]] parr in New Brunswick rivers (Elson, 1950) — large increases in stocked juvenile salmon produced only marginal increases in surviving smolts, consistent with Type C dynamics.
- Predators in Type C systems typically have **ample alternative food sources** and high mobility, allowing area abandonment once local prey is depleted.
- Predator removal (e.g., shooting mergansers and kingfishers in the Pollett River) can shift a system from Type C toward Type B/A, substantially improving prey survival (4-5 fold increase observed).

## Key Findings

### Mathematical Model for Type B Predation
- Prey decline follows the exponential mortality equation: **N = N₀e^(-it)**, where *i* is the instantaneous mortality rate, proportional to predator abundance.
- **Doubling predator abundance doubles instantaneous mortality rate**, but does NOT proportionally double actual (realized) mortality — the relationship is non-linear.
  - Example: i = 0.8 over a season → baseline survival 44.9%; doubling predators → survival drops to 20.2% (mortality increases from 55.1% to 79.8%, a 45% relative increase, not 100%).

### General Survival-Predator Abundance Relationship
- Derived formula: **P₀/P₁ = log(s₀)/log(s₁)**, relating two predator abundance levels (P₀, P₁) to corresponding prey survival rates (s₀, s₁).
- **Critical insight**: The benefit of predator reduction is highly dependent on the *initial survival rate*:
  - Halving predators only **doubles survival** if initial survival was ≤25% (i.e., mortality ≥75%).
  - If initial mortality exceeds ~45%, halving predators **more than doubles** survivor numbers.
  - At very low initial survival (e.g., 0.01%–1%), even **modest predator reductions** (7.5%–15%) can **double survival rate** — highlighting outsized returns on predator control in high-mortality systems.

### Practical and Management Implications
- Predator control is **most cost-effective** when natural survival rate is low (i.e., in high-fecundity species or life stages with heavy natural mortality), consistent with the "medium" survival range of 1–10% relevant to Canadian salmon management efforts.
- High-fecundity species (e.g., cod, with ~10⁶ pelagic eggs/female and ~99.9% larval mortality) show **extreme sensitivity** to small changes in predator abundance — a mere 10% decrease in predators could double year-class strength.
- **Instability implication**: Systems with large gains from small predator reductions are equally vulnerable to reversal — small *increases* in predator abundance (e.g., due to improved predator recruitment) can rapidly erase survival gains.
- These relationships **only hold when predation is the dominant/sole source of mortality**; when other mortality sources are significant, the benefit of predator reduction diminishes proportionally.
- Type A and Type C situations require conversion toward Type B dynamics (via substantial predator reduction) before Ricker's quantitative model becomes applicable — demonstrated empirically in the [[Pollett River]] merganser/kingfisher removal experiment.

### Cited Empirical Studies
- **Foerster & Ricker (1941)**: *J. Fish. Res. Bd. Canada* 5(4):325-336 — [[Cultus Lake]] sockeye salmon predator reduction experiment (Type B).
- **Elson (1950/1956)**: Fish. Res. Bd. Canada Prog. Repts. (Atlantic), No. 51:12-15 — [[Pollett River]] Atlantic salmon parr, merganser/kingfisher control (Type C → B transition).