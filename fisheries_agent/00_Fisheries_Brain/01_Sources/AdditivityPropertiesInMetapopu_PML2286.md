---
species: "Bluefin tuna (Thunnus thynnus); Swordfish (Xiphias gladius); Grouper and snapper (examples only); Red sea urchin (Mesocentrotus franciscanus, California fishery, example only)"
common_name: "Bluefin tuna; Swordfish; Grouper; Snapper; Red sea urchin"
family: N/A
habitat: "Marine; coastal reef and patchy exploited habitats; pelagic examples"
ocean_basin: "Pacific and Atlantic (examples cited)"
location: "USA: Channel Islands (southern California), Tortugas (Florida Keys), California red sea-urchin fishery; general theoretical model"
tags: [marine-reserves, metapopulation, fisheries-economics, bioeconomics, additivity]
title: "Additivity properties in metapopulation models: implications for the assessment of marine reserves"
source_id: "PML2286"
marsh_id: "PML2286"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. N. Sanchirico (2005). Additivity properties in metapopulation models: implications for the assessment of marine reserves. Journal of Environmental Economics and Management 49 (2005) 1-25. Marsh Library ID: PML2286."
source_file: "Sanchirico J.N. 2003. Additivity properties in metapopulation models implications for the assessment of marine reserves.pdf"
text_extraction: "text"
---
# Additivity Properties in Metapopulation Models: Implications for the Assessment of Marine Reserves

#ichthyology #marine-biology #fisheries-economics

## Executive Summary

This paper develops a spatially explicit [[Bioeconomic Metapopulation Model]] to test how assumptions about [[Larval Dispersal]] and [[Adult Dispersal]] change the predicted benefits of [[Marine Reserves]]. Reserves raise aggregate catches only when dispersal benefits (spillovers) exceed the opportunity cost of closing an area to fishing. The author classifies models by their **additivity properties**: whether system-wide biological production with patch connections is greater than (supraadditive), equal to (additive), or less than (subadditive) the sum of isolated patch production.

Three models are compared: [[LARLOC]] (all larvae retained locally, used as benchmark), [[PREDIS]] (density-dependent larval production) and [[POSTDIS]] (density-independent larval production with local density-dependent settlement). Only POSTDIS can be supraadditive, and that model is the most optimistic about reserves producing win-win outcomes for fishers and fish populations.

## Background & Description

**Motivation.** A 2001 [[Scientific Consensus Statement on Marine Reserves]], signed by more than 150 marine scientists, highlighted conservation and fishery-enhancement benefits of closed areas, including enhanced biodiversity, additional larvae and biomass, higher catches, and a hedge against management failure. Proposals to close up to 90% of fishable habitat were noted, raising concerns among current users about losing future access. The paper argues that policymakers need ex ante predictions of costs and benefits, and that existing research does not show how modeling assumptions alter results.

**Model structure.** The author builds a metapopulation framework with discrete patches:
- Patch biomass evolves through local logistic growth, adult dispersal, and implicit larval dispersal (Eqs. 1-4).
- Fleet effort in each patch adjusts sluggishly to net rents relative to outside opportunities and to rents in connected patches. The model draws on empirical support from the [[California Red Sea Urchin Fishery]].
- Net rents are gross profits minus an opportunity cost per vessel. The paper assumes a [[Schaefer Production Function]] with linear costs and a common ex-vessel price.

**Life-history examples.** The paper cites contrasting cases:
- A sedentary species such as sea urchins, whose larvae mix in a common pool with no adult migration.
- Species with about half of larvae retained locally, the other half entering larval pools (a = 0.5).
- Pelagic species such as [[Bluefin Tuna]] and [[Swordfish]], and reef fish such as [[Grouper]] and [[Snapper]], which have both adult and larval dispersal phases.

**Density-dependence framing.** Carr and Reed are cited to argue that larval-dispersal models suit recruitment overfishing, while adult-juvenile dispersal models suit growth overfishing. The author notes that marine larval fecundity can show increasing returns to scale, but reef settlement is limited by density dependence through competition for coral habitat.

## Ecological & Environmental Context

- **Dispersal is poorly understood.** Larval and adult dispersal depend on species, connectivity, and currents. Improvements in genetic analysis, mark-recapture, and [[Otolith Geochemistry]] are expected to clarify it. Otoliths are fish ear bones whose chemical signatures reveal the environments fish have occupied.
- **Habitat heterogeneity.** Patches differ in productivity, and some act as larval pools with no inherent productivity. The author notes that these structures govern how reserve placement affects dispersal benefits and opportunity costs.
- **Carrying capacity is spatially endogenous** in PREDIS, where multiple unexploited equilibria are possible, including one patch above and another below its carrying capacity.
- **Oceanographic influence.** Currents, gyres, and [[Coastal Upwelling]] shape larval dispersal. Larval survival (m) is more variable in marine systems than the optimistic m = 1 case used in parts of the analysis.
- **Model limits.** The lumped-parameter model is highly stylized. It omits age- and size-specific mortality, selectivity, and egg production per recruit. The author conjectures that its qualitative results are robust.

## Key Findings

1. **Additivity classification.**
   - [[LARLOC]] is additive when there is no adult-dispersal mortality. The adding-up restriction requires symmetric dispersal (d_ij = d_ji) so that whatever leaves one patch arrives in another. It becomes subadditive if adult dispersal involves mortality.
   - [[PREDIS]] is at best additive (zero dispersal mortality). With m < 1 and interior population levels, it is subadditive (Proposition 2), because patches lose larvae to a common pool that does not fully return.
   - [[POSTDIS]] is the only model that can be supraadditive. With two patches, equal growth rates, zero adult dispersal, and m = 1, the aggregate gain is proportional to the squared difference in patch densities (Proposition 3).

2. **Sign of the effect depends on density differences.** For POSTDIS with m = 0.95, a contour map shows three regions, two supraadditive and one subadditive. The gain from linkages rises with the difference in patch densities, not with absolute population levels.

3. **Unexploited equilibrium is additive** in all models. Exploitation keeps populations below this equilibrium, so the subadditive or supraadditive properties persist in managed systems.

4. **Catch implications.** In steady state, additivity maps directly into equilibrium catches. A supraadditive system has higher sustainable catches than a subadditive one, all else equal.

5. **Win-win likelihood.** The supraadditive (POSTDIS) model is the most optimistic about reserves producing win-win outcomes. The PREDIS model is the most pessimistic. LARLOC lies between them.

6. **Effort allocation.** Total effort is identical in PREDIS and LARLOC. Effort in POSTDIS may be higher or lower than in LARLOC, depending on parameter configuration.

7. **Reserve effects on density and dispersal.** In LARLOC, reserve density falls as the dispersal rate b rises, because adult spillover is offset by emigration. In PREDIS and POSTDIS, larval mixing lets the reserve contribute to open-area growth, which mutes the effect of b.

8. **Aggregate catch condition (Table 3).** Reserves raise aggregate catch when dispersal benefits exceed the forgone catch. In LARLOC, the condition is b(x₁ − w₂) > r₁w₁(1 − w₁). In PREDIS, dispersal benefits can fall below LARLOC's, and in POSTDIS both benefits and costs are larger.

9. **Without adult dispersal.**
   - In LARLOC, the aggregate condition is never satisfied when dispersal is zero.
   - In PREDIS, larval spillover alone is insufficient to outweigh forgone catch. This is consistent with [[Tuck and Possingham]].
   - In POSTDIS, reserves can increase aggregate catches even with zero adult dispersal, because of larval spillover.

10. **Dispersal-to-growth ratio.** The paper shows that the aggregate-catch condition depends on the ratio of the dispersal rate to the intrinsic growth rate. The growth rate only scales the condition. Figure 2 uses a dispersal-to-growth ratio of 0.2 in Figure 3.

11. **Site selection.**
   - With all larvae retained locally (LARLOC), closing low-cost patches is more likely to yield win-win outcomes. These patches are the most heavily exploited, so their opportunity cost is low.
   - Under POSTDIS, closing high-cost patches may be better. The feasible subregion for win-win outcomes can cover as much as 75% of the unexploited patch when the reserve is the high-cost patch. Even an unexploited area could raise aggregate catches if closed.
   - The author notes that fishers supporting closure of low-cost areas is counterintuitive and depends on open-access conditions.

12. **Policy implications.**
   - Supraadditive systems favor policies that create large density differentials across space, since reserves do exactly that.
   - In PREDIS, aggregate production is maximized near MSY. Reserves deviate from this and are less likely to deliver win-win results.
   - Policymakers should consider biology and economics together from the outset, and select patches based on dispersal mode and cost structure.

13. **Caveats.** Results use best-case assumptions, including perfect larval mixing, uniform larval distribution, and full larval survival (m = 1) in some cases. The author notes that intermediate cases should approach LARLOC results.

14. **Future research.** The author highlights the need for n-patch analysis with biological heterogeneity, analogues to economies of scope and scale, and optimal spatial management.

---

**Concepts:** [[Marine Reserves]] · [[Metapopulation]] · [[Additivity Properties]] · [[Supraadditivity]] · [[Subadditivity]] · [[Larval Dispersal]] · [[Adult Dispersal]] · [[Spillover]] · [[Density Dependence]] · [[Bioeconomic Model]] · [[Open-Access Fishery]] · [[Opportunity Cost]] · [[Win-Win Outcome]] · [[Site Selection]] · [[Maximum Sustainable Yield]] · [[California Red Sea Urchin Fishery]]