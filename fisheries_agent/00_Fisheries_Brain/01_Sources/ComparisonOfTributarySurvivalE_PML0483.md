---
species: "Oncorhynchus mykiss"
common_name: "Steelhead (anadromous Rainbow Trout); Resident Rainbow Trout"
family: "Salmonidae"
habitat: "Freshwater tributary streams (rearing and resident movement); anadromous migration to the ocean"
ocean_basin: "Pacific"
location: "Murderers Creek, South Fork John Day River, Oregon; Columbia River basin, USA"
tags: [ichthyology, marine-biology, salmonidae, fish-survival, mark-recapture, pit-tags, steelhead, columbia-river-basin]
title: "Comparison of Tributary Survival Estimates of Steelhead using Cormack-Jolly-Seber and Barker Models: Implications for Sampling Efforts and Designs"
source_id: "PML0483"
marsh_id: "PML0483"
library: "Marsh Library"
permission: "not public domain"
source_citation: "M. M. Conner, S. N. Bennett, W. C. Saunders, N. Bouwes (2015). Comparison of Tributary Survival Estimates of Steelhead using Cormack-Jolly-Seber and Barker Models: Implications for Sampling Efforts and Designs. Transactions of the American Fisheries Society 144:34-47. Marsh Library ID: PML0483."
source_file: "Conner M.M. et al. 2015. Comparisons of tributary survival estimates of steelhead using cormack jolley seber and barker models, implications for sampling efforts and designs.pdf"
text_extraction: "text"
---
# Comparison of Tributary Survival Estimates of Steelhead using Cormack-Jolly-Seber and Barker Models

#ichthyology #marine-biology #salmonidae

## Executive Summary

This simulation study compares two [[Capture-Mark-Recapture]] approaches for estimating juvenile [[Steelhead]] survival in tributary streams: the traditional [[Cormack-Jolly-Seber Model]] (CJS) and the [[Barker Model]], which can incorporate [[Resight Data]] from [[PIT Tag]] interrogation sites. Simulations were parameterized from field data on steelhead and resident [[Rainbow Trout]] in [[Murderers Creek]], a tributary of the [[South Fork John Day River]] in Oregon. The Barker model produced more precise survival estimates than the CJS model under almost all sampling intensities, site sizes and movement scenarios, with equal or lower bias. The authors conclude that the Barker model is preferable when resight data are available, that resighting efforts should be prioritized in low-survival seasons, and that permanent emigration to the ocean remains a source of bias that sampling intensity cannot correct.

## Background & Description

**Study species.** The focal taxon is [[Oncorhynchus mykiss]], represented by anadromous steelhead and resident Rainbow Trout. Resident fish move locally within a tributary without leaving it. Migratory fish move locally for a period and then leave the tributary, similar to juveniles migrating to the ocean. Tributary rearing time ranges from days to multiple years, and movements range from nearly sedentary (<100 m) to nomadic movements of 1 to 100 km.

**Monitoring context.** Advances in [[Passive Integrated Transponder Tags]] have enabled large-scale tagging in the [[Columbia River Basin]]. The document reports that over 35 million Pacific salmon and steelhead were PIT-tagged between 1987 and 2013. Most of this work has focused on juvenile survival through the [[Hydrosystem]] of dams. Interest has grown in tributary survival because millions of dollars are being invested in [[Habitat Restoration]] intended to increase freshwater production of salmonids listed under the [[Endangered Species Act]]. An infrastructure of more than 224 [[Interrogation Sites]] in 33 subbasins has been established to monitor restoration effectiveness.

**Methodological gap.** Tributary studies differ from hydrosystem studies. Fish are often tagged in small groups at multiple sites, sites are revisited across seasons, and movement is more complex. Resight data collected at interrogation sites during high-capture periods cannot be incorporated into the CJS model without binning, which violates its assumptions. Earlier work by [[Horton and Letcher]] (2008) on Atlantic Salmon used a small-scale simulation with a single interrogation site and a fixed resight rate of 0.75, which limited assessment of trade-offs between marking effort and resight rate.

## Ecological & Environmental Context

**Study site and data.** Empirical data were collected from October 2004 to October 2006 in Murderers Creek, which contains both resident and migratory steelhead. Juvenile steelhead were captured by seining, electroshocking and night snorkeling at permanent sites 500 to 1,000 m long. All steelhead greater than 70 mm were PIT-tagged and released at the capture site. Sites were sampled on two consecutive days and revisited in four seasons. The capture period averaged 1 to 2 weeks.

**Seasonal grouping.** For modeling, data were condensed into three seasons with similar recapture, resight and survival rates:
- Summer (June to September)
- Fall (October to December)
- Winter/spring (January to May)

**Simulation parameters.** Key input ranges, as reported in the study's parameter table:
- Number of marked fish (n): 50 to 500 per sampling occasion
- Recapture probability (p): 0.10 to 0.50 (summer and fall); 0.10 (winter)
- Resight probability (R): 0.10 to 0.50 (summer and fall); estimated at 0.09 (winter)
- Survival (S): 0.90 (summer and fall); 0.10 (winter)
- Fidelity (F): 0.75 for all seasons

The simulated system included five hypothetical interrogation sites. Each scenario was run with 1,000 data sets. The Barker model was reduced to a CJS formulation by fixing the temporary-emigration and resight parameters at zero for comparison.

**Movement and site-size scenarios.** Four scenarios were tested:
1. Resident fish, small sample site, with resights only at the site
2. Resident fish, large sample site, with resights over the entire range
3. Mixed resident and migratory fish, with a downstream antenna detection probability (p*) of 0.66
4. As scenario 3, but with p* = 0.95

Migrants were treated as permanent emigrants that could no longer be resighted. This violates a key Barker assumption and produces bias in both models.

**Performance metrics.** Precision was measured as the coefficient of variation (CV = SD/mean). Bias was measured as relative bias, (estimated value minus known value) divided by the known value.

## Key Findings

**1. The Barker model outperforms CJS on precision.**
- For resident-only scenarios (1 and 2), Barker precision was 31 to 46% higher than CJS across seasons.
- For mixed-movement scenarios (3 and 4), Barker estimates were 17 to 35% more precise.
- Increasing p* from 0.66 to 0.95 produced only slight precision gains for either model.

**2. Sampling intensity effects differ by parameter.**
- Precision of Barker survival estimates improved most when the number of marked fish increased from 50 to about 200. Gains beyond 200 fish were smaller.
- Increasing p improved CJS precision but had little effect on Barker precision.
- Increasing R improved Barker precision, which the authors attribute to the use of resights regardless of where they occur.

**3. Bias patterns.**
- Under scenario 1, CJS survival was biased low by 19 to 23% because fish that moved off the sample site could not be recaptured. Barker bias was near zero in summer (about -1%) and about 10% in winter.
- Adding resights across the range (scenario 2) reduced Barker bias in winter and kept summer bias similar between models.
- Under mixed movement (scenarios 3 and 4), bias was similar for both models and negative in all cases. Higher p* reduced summer bias.

**4. Seasonal differences.**
- Summer estimates were roughly twice as precise as winter estimates for both models at p = R = 0.3 and n = 75.
- Winter bias appeared larger when few fish were marked (fewer than 150), because of wide variation and many overestimates that averaged out.

**5. Recommended sample sizes.**
- Precise (CV 10 to 20%) and unbiased survival estimates were obtained by marking about 75 to 100 fish per sample period when survival and re-encounter rates are high (summer).
- About 300 fish per sample period were needed when survival and re-encounter rates are low (winter).

**6. Binning resights is not a valid workaround.**
- Counting resights as recaptures at the start of the next period produced a 10 to 20% positive bias in survival estimates.
- Counting them at the start of the capture period produced about a 15% negative bias.

**7. Permanent emigration is a design problem, not a sampling problem.**
- Bias from emigration cannot be reduced by increasing n, p or R. The authors state it must be addressed through study design or analysis, such as direct estimation of emigration with radiotelemetry or antenna efficiency data, or multistate models ([[Horton et al. 2011]]).

**8. Management recommendations.**
- Select site sizes that allow capture of about 100 to 300 fish per sample period, depending on expected survival and re-encounter rates.
- Tag fish during low-emigration, high-survival periods with moderate to high recapture. For interior Columbia Basin steelhead, summer and fall meet these criteria.
- In winter and spring, focus on increasing resights through interrogation sites, mobile surveys or both.
- Maximize detection of migrants leaving the study area and remove encounter histories for which survival cannot be assessed.
- Results apply to steelhead, which spend more years rearing in tributaries than other Pacific salmon. Alternative strategies are needed for [[Chinook Salmon]], which tend to migrate downstream soon after hatching.

**9. Acknowledged limitations.** The authors note that their estimate of the temporary-emigration parameter (F') was crude. Tests with extreme survival and resight values suggested this had limited effect on the other parameters, likely because of few interrogation sites, limited summer and winter movement, and short intervals between captures.