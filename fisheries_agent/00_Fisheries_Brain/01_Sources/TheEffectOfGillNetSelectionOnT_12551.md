---
species: ["Salvelinus alpinus willughbii (char)", "Perca fluviatilis (perch)"]
family: ["Salmonidae", "Percidae"]
habitat: "Freshwater lake (Windermere, English Lake District)"
ocean_basin: "N/A - Freshwater lacustrine system"
study_type: "Methodological/Statistical Fisheries Science"
gear_studied: "Gill-nets (multiple mesh sizes), seine, traps, angling"
source_id: "12551"
---

#ichthyology #freshwater-biology #fisheries-science #gill-net-selectivity #Salmonidae #Percidae

## Executive Summary

This paper by C. Kipling (Freshwater Biological Association) addresses a critical methodological problem in fisheries science: whether **gill-net-caught samples** provide reliable estimates of the population **weight-length relationship** (W = AL^b). Using data on [[Char (Salvelinus Alpinus Willughbii)]] and [[Perch (Perca Fluviatilis)]] from Windermere, the study demonstrates that gill-nets do not select randomly for length and weight, but rather select by **girth**, which produces a bias closely approximated by **truncation by weight**. This selection systematically flattens (reduces) the regression slope (b) compared to unbiased samples (seine, trap, angling), unless the sample incorporates a wide length range — achieved either by using multiple mesh sizes or by chance capture of "outlier" fish. The work has broad implications for any study relying on gill-net samples to characterize population-level morphometric relationships.

## Background & Description

- **Weight-Length Relationship Model**: W = AL^b, or in log form: log W = log A + b log L, where b (the regression/growth coefficient) ideally approximates 3 for isometric growth.
- **Girth measurements**: Maximum girth and head girth (at pre-opercular bone) were measured via string encirclement.
- **Species-specific measurement points**:
  - Char: snout tip (mouth closed) to caudal fork.
  - Perch: pre-maxilla tip to longest caudal ray tip.
- **Key morphometric relationship (Perch)**: Multiple regression of girth on length and weight jointly gave **multiple correlation coefficient = 0.957**; girth-length correlation alone = 0.904; girth-weight correlation alone = 0.956 — indicating weight is a stronger predictor of girth than length, which underlies why gill-net selection (girth-based) approximates truncation by weight.
- **Illustrative example (Fig. 3)**: A female mature perch caught in a 1¼" bar gill-net: Length 23.8 cm, Weight 151 g, Girth 13.8 cm.
- Mesh sizes tested ranged from ½" bar (1.27 cm) to 2" bar (5.08 cm), plus a 1¼" bar herring gill-net (3.17 cm) of finer cotton twine.

## Ecological & Environmental Context

- **Study system**: [[Windermere]], a lake in the English Lake District, sampled across multiple habitats/depths using gill-nets set in deep water and examined at ≥24-hour intervals.
- **Species and life stages studied**:
  - Immature dwarf char (small morph, <14–27 cm range)
  - Mature/spawning char (both sexes, autumn spawning aggregations, e.g., at Low Wray and Red Nab)
  - Mature perch (both sexes, spring), sampled via traps ([[Fish Trap Sampling]] per Worthington 1950), gill-nets, and angling (paternoster rig with minnow/worm bait).
- **Capture mechanics — two selection modes**:
  1. **Entanglement by jaw/head** — no weight-length selection bias (ignored in theoretical model).
  2. **Meshing by body** (between anterior point A and max girth point B) — the primary source of size-selective bias, central to this paper's analysis.
- **Gear comparison groups**: seines (assumed unselective, worked from shore, graded mesh 1"–3/8" bar), traps, and rod-and-line angling served as reference/unbiased samples against which gill-net-derived slopes were tested.

## Key Findings

1. **Gill-nets bias weight-length slope estimates downward** when only a single mesh size is used and the catch has a narrow length range — this is the dominant pattern (3 of 4 significant discrepancies in Table 1 arose from single-mesh samples, all with smaller b than reference samples).

2. **Truncation by girth ≈ Truncation by weight**: Theoretically, gill-net selection truncates catches by girth, but empirically this closely approximates truncation by weight (angle between constant-girth and constant-weight lines was only 15°30' for perch; weight discrepancy ~3 g in the 50–80 g range — considered negligible).

3. **Truncation by length does NOT bias slope**; truncation by weight DOES bias slope downward. Confirmed via artificial truncation experiments on perch populations (Table 2):
   - Female perch: full population b = 3.43; length-truncated b = 3.72 (not significant); weight-truncated b = 2.50 (very significant reduction).
   - Male perch: full population b = 3.30; length-truncated b = 3.40 (not significant); weight-truncated b = 2.79 (significant reduction).

4. **Artificial weight-truncation closely matches real gill-net results** (Table 3): Weight-truncated male perch (24–42 g) gave b = 2.79, while actual 2" bar gill-net catches across three months gave b = 2.72–2.86 — strong empirical validation that gill-net selection behaves like weight-truncation.

5. **Multiple mesh sizes or "outlier" catches rescue the estimate**: When gill-net samples span a wide length range (via combining multiple mesh sizes, or via chance capture of unusually large/small individuals beyond normal girth-selection limits), the resulting regression slope closely approximates the true unselected population value.
   - Example: Immature dwarf char — combined ½" + ⅜" bar gill-nets gave b = 3.17 vs. seine b = 3.18 (excellent match), despite the two mesh sizes separately catching non-overlapping, biased length groups.
   - Example: Female perch (3/8" bar gill-net) with 23 "outlier" fish >16 cm gave b = 3.26, not significantly different from trapped fish (b = 3.43); but excluding outliers, small fish alone gave a significantly depressed slope.

6. **Biased/selective sub-sampling by researchers can also distort slopes** (rows 6–7): Spawning char samples brought to lab were purposively selected for weight/colour, artificially *increasing* slope beyond the population value — a caution about secondary human-driven selection compounding net selectivity.

7. **Practical recommendation**: A single mesh-size gill-net sample **cannot be relied upon** to give an accurate weight-length regression coefficient for char or perch. Reliable estimates require either (a) multiple mesh sizes fished simultaneously, or (b) verification that the catch's length range is unusually wide due to chance "outliers."

8. This work extends earlier findings on gill-net selectivity for [[Length-Condition Relationship]] ([[Farran 1936]]) and [[Length-Girth Relationship]] ([[Margetts 1954]]) into the specific domain of weight-length allometry, with direct relevance to stock assessment methodology using [[Gill-Net Selectivity]] corrections.