---
species: "Salvelinus alpinus"
common_name: "Arctic char"
family: "Salmonidae"
habitat: "Anadromous river-lake system (freshwater lake wintering, marine feeding migration)"
ocean_basin: "Norwegian Sea (North Atlantic)"
location: "Vardnes River, Senja Island, Troms, Northern Norway (~69°N, 16°E)"
study_period: "1956-1963"
tags: [ichthyology, marine-biology, salmonidae, anadromous-fish, growth-rate-studies]
source_id: "15166"
---

# Growth Rates of the Char *Salvelinus alpinus* in the Vardnes River, Troms, Northern Norway

#ichthyology #marine-biology #Salmonidae

## Executive Summary
This study by Mathisen & Berg quantifies the instantaneous growth rates in weight and length of anadromous [[Arctic Char]] (*Salvelinus alpinus*) in the Vardnes River system, Northern Norway, using multi-year tag-recapture data (1956–1963). Char in this system exhibit a distinctive **oscillating growth pattern**: rapid weight gain during a short (~40-day) marine feeding period in summer, followed by a **net weight loss** during a long (~320-day) freshwater overwintering/spawning period in [[Vardnes Lake]]. This contradicts the smooth, monotonic growth-in-weight functions typically assumed in fisheries yield models, indicating that such models are inappropriate for repeatedly-spawning [[Diadromous Fish]] like this char stock.

## Background & Description
- **Measurement protocol**: Total live length measured to nearest cm; live weight measured to nearest 10 g.
- **Sex determination**: Only possible when secondary sexual characteristics had developed (via [[Carlin Tag]] recapture observations); growth rates reported are therefore for **combined sexes**.
- **Size classes**:
  - Average weight of downstream (seaward) migrants (all years): **195.7 g**
  - Average weight of upstream (returning) migrants (all years): **374.3 g**
  - Reference initial length used for growth curve modeling: **27.5 cm**
- **Age determination**: No scale samples were collected; thus no direct age-at-length data, and growth parameters are size/maturity-based rather than age-based.
- Growth in length was much slower than growth in weight during the marine feeding period; mature fish showed little to no length increase during winter freshwater residence, while small immature fish continued to grow in both length and weight even in winter.

## Ecological & Environmental Context
- **Life history**: Anadromous, iteroparous char that migrate to sea in spring after lake ice breakup and rising temperatures, feed in the sea through summer, then return to the [[Vardnes River]] in early fall to spawn and overwinter in **Vardnes Lake** (~30 ha surface area, 2–3 m average depth).
- **Migration timing** (pooled across years, 1957–1963, via logistic curve fitting):
  - Downstream (seaward) migration: 50% passage by early-mid June (range across years: late April–June)
  - Upstream (return) migration: 50% passage by mid-late July
  - Combined 50% passage window for both directions: June 4 – July 15 (41 days)
- **Feeding season in sea**: standardized to **40 days**
- **Freshwater residence (wintering + spawning)**: standardized to **320 days**
- **Trap catch totals (1956–1963)**: 2,388 downstream migrants; 1,372 upstream migrants (grand total 3,760)
- **Tagging/recapture summary**: 1,657 fish tagged with sex undetermined, 131 males, 296 females tagged; recaptured (one or more times): 849, 233, 594 respectively.
- **Fishing pressure**: Angling permitted in the lake; river closed to fishing; main commercial catch occurs at sea during the marine feeding phase.
- Ecologically, this pattern is considered likely typical of other repeat-spawning [[Diadromous Fish]] species that alternate between marine feeding and freshwater reproductive/wintering habitats.

## Key Findings
1. **Marine feeding season** duration estimated at **40 days**; **freshwater lake residence** duration estimated at **320 days**.
2. **Instantaneous growth rate in weight**:
   - Summer (marine) growth rate: **g_w = 0.01547/day** (weight gain)
   - Winter (freshwater) growth rate: **g_w = −0.00039/day** (net weight LOSS)
   - All-years combined data: 706 fish (summer, marine residence), 568 fish (winter, freshwater residence)
3. **Instantaneous growth rate in length**:
   - Summer (marine): **g_l = 0.00311/day**
   - Winter (freshwater): **g_l = 0.00018/day** (much smaller than summer, near-zero for mature fish)
4. **Significant year-to-year variation** in growth rate and duration of marine/freshwater residence observed (Tables 4–5), likely driven by environmental/climatic factors (not modeled as covariates here).
5. **Oscillating (non-monotonic) growth pattern**: Weight increases sharply each summer at sea and decreases each winter in freshwater — this seasonal "sawtooth" pattern is not captured by standard smooth growth curves used in fisheries yield calculations.
6. **Growth model equation** (based on initial spring weight of 195.7 g):
   `w = 195.7 · e^[0.01547(40i) − 0.00039(320j)]`, for successive summer(i)/winter(j) cycles.
7. **Multi-season verification**: Growth rates calculated over combined summer+winter periods (Table 6) and over multi-year periods (Table 7) were compared against single-season estimates.
   - Agreement between observed and calculated growth was **good for ~1 year** periods.
   - For periods **beyond one year**, calculated (predicted) growth rates **overestimated** observed rates — attributed to age-related decline in growth rate not accounted for by the pooled (younger-fish-dominated) mean estimates.
8. **Case study** (individual tagged char, 1958–1962): Demonstrates increasing overestimation of weight by the model over time; by the fourth year, no further length increase was observed, and final weight was 1,600 g (vs. calculated 2,294 g).
9. **Conclusion**: The estimated growth parameters are valid primarily for **mature fish during their most active growth period** and become biased upward (overestimating growth) when extrapolated over two or more years. Age- and sex-specific analyses were recommended for future refinement but were not possible in this dataset due to lack of scale-based aging.

## Related Concepts
- [[Salvelinus Alpinus]]
- [[Arctic Char]]
- [[Salmonidae]]
- [[Diadromous Fish]]
- [[Anadromy]]
- [[Instantaneous Growth Rate]]
- [[Carlin Tag]]
- [[Fish Tagging and Recapture Methods]]
- [[Vardnes River]]
- [[Vardnes Lake]]
- [[Fisheries Yield Models]]
- [[Logistic Migration Curve]]