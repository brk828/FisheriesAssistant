---
species: Branta canadensis
common_name: Canada goose
family: N/A
habitat: Wintering grounds (overwintering sites) of the Atlantic flyway
ocean_basin: N/A
location: Mid-Atlantic, Chesapeake, and Carolinas wintering regions, eastern United States
tags: [capture-recapture, multistate-models, waterfowl, statistical-ecology, movement-ecology]
title: "Capture-Recapture Studies for Multiple Strata Including non-Markovian Transitions"
source_id: "PML0304"
marsh_id: "PML0304"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. Brownie, J. E. Hines, J. D. Nichols, K. H. Pollock, J. B. Hestbeck (1993). Capture-Recapture Studies for Multiple Strata Including non-Markovian Transitions. Biometrics 49, 1173-1187. Marsh Library ID: PML0304."
source_file: "Brownie C. et al. 1993. Capture-recapture studies for multiple strata including non markovian transitions.pdf"
text_extraction: "mixed"
---
# Multistratum Capture-Recapture Studies including Non-Markovian Transitions

#ornithology #waterfowl #capture-recapture

## Executive Summary

This statistical paper extends [[Capture-Recapture Analysis]] to multiple strata, such as geographic locations or physiological states, where animals move between strata with unknown probabilities. The authors describe a computer routine that implements the [[Arnason-Schwarz Model]] (a [[Markovian Transitions]] model) and its reduced-parameter versions using the [[SURVIV]] program. They also introduce a "memory" model in which transition probabilities depend on the previous stratum, estimated with a [[Conditional Likelihood]] approach. The methods are illustrated with [[Canada Goose]] banding data from three wintering regions. The Markovian assumption is rejected convincingly, and the authors interpret this as evidence of long-term [[Site Fidelity]].

## Background & Description

**Problem.** The classic [[Jolly-Seber Model]] assumes a homogeneous population segment. Studies that group animals into strata raise two situations. In the first, stratum membership set at release is fixed (for example, age class), and existing methods apply. In the second, animals move among strata by an unknown chance process, so stratum is unknown whenever an animal is not captured. The paper focuses on this second case, which the authors say had received little attention.

**Prior work.** Arnason (1972, 1973) and Seber (1982) developed estimators for movement probabilities, which are inefficient when there are more than three capture occasions. Schwarz et al. (1993) gave the likelihood for the Arnason-Schwarz model and a FORTRAN program aimed at band-recovery data. Hestbeck et al. (1991) studied Canada geese with multiple recaptures and proposed a model in which transitions depend on the previous location.

**Notation and data structure.** The model uses matrices of transition probabilities (φ) and capture probabilities (p) indexed by stratum and time. Release-recapture data are arranged in product-multinomial form. The paper's illustrative examples use 3 strata and 4 to 6 capture occasions.

**Software.**
- The authors wrote a conversion routine, CNVMEMOV (by J. E. Hines), that feeds data to a modified SURVIV program, [[MSSURVIV]].
- Capture histories use stratum integers in place of 1s, so the history 012103 means a bird first captured at time 2 in stratum 1, then recaptured in strata 2, 1, and 3.
- MSSURVIV is compiled in FORTRAN for a minicomputer. The authors note that the PC-DOS 640K memory limit restricts it to very small data sets.

**Derived parameters.** Total survival and between-stratum movement rates are derived from transition probabilities, since survival and movement cannot be separated without strong assumptions.

## Ecological & Environmental Context

**Study system.** Canada geese were banded with individually coded neckbands in three wintering regions of the mid-Atlantic flyway: the mid-Atlantic (stratum 1), the Chesapeake (stratum 2), and the Carolinas (stratum 3).

**Biological motivation.**
- Movement is the least understood of the three determinants of population change (survival, reproduction, movement). Movement is central to hypotheses about population regulation, but poor rate estimates have prevented rigorous tests.
- Fidelity to breeding and wintering areas varies with age and sex, which is relevant to theories of animal social systems.
- Habitat fragmentation has increased interest in [[Metapopulation Models]], where between-patch movement matters.
- Strata can also represent body mass classes (as in a meadow vole study cited by the authors), reproductive status, or other physiological states. These support tests of the cost of reproduction and estimation of stage-based population projection parameters.

## Key Findings

1. **Markovian transitions are rejected.** For the three-region example, the [[Arnason-Schwarz Model]] (Model A) showed important lack of fit. Pearson χ² values were about 129.55 (df = 39) for Model A, 245.05 (df = 65) for Model B, and 279.55 (df = 77) for Model D. Likelihood-ratio tests favoured Model A over B and D, but the authors say these comparisons are not very meaningful given the lack of fit.

2. **Preliminary transition estimates show fidelity.** Averaged across years for the [[Canada Goose]] data (k = 5, a = 3, 45 parameters), the diagonal transition probabilities were the largest in each row (approximately 0.49, 0.58, and 0.47). This suggests short-term fidelity to overwintering sites.

3. **Memory model improves fit (Mid-Atlantic and Chesapeake, 1984–1989).** Stratum 3 was excluded because transitions into it were rare. The memory model with 38 parameters gave a substantially better fit than the no-memory model with 22 parameters. Pearson χ² fell from about 350.71 (df = 44) to about 45.12 (df = 21), and log-likelihood rose from about −315.46 to −193.44. The authors caution that pooling and sparse data make the P-values approximate.

4. **Long-term fidelity is indicated.** In Table 8, the probability of moving to the stratum occupied two years earlier (column a) exceeds that of moving to a different stratum (column b) in every row. Birds in stratum 1 at time i − 1 are more likely to be found in stratum 1 at time i + 1 than birds that were in stratum 2 at time i − 1. The authors conclude there is strong evidence that the model's inadequacy reflects a tendency to return to previously occupied sites.

5. **Three-region analysis (1986–1989).** This analysis used 57 parameters for the full memory model and 18 multinomials in the conditional likelihood.
   - No-memory model: likelihood-ratio G² = 297.96 (df = 60, 21 parameters).
   - [[Model MV2]] (Hestbeck et al.): G² = 59.35 (df = 42, 39 parameters).
   - Full memory model: G² = 34.45 (df = 24, 57 parameters).
   - The Markovian assumption is again rejected. MV2 fits comparably to the full memory model (P = 0.13 for the MV2 vs. memory test).

6. **Caution on sparse data.** Zeros in the recapture matrices produce estimates of 0 for some transition probabilities. Standard errors and goodness-of-fit P-values from MSSURVIV may be inaccurate under sparse data, so the authors advise caution.

7. **Methodological contribution.** The conditional likelihood uses only histories with consecutive captures. It fits the product-multinomial framework of the Arnason-Schwarz model and can handle more capture occasions and strata than other easily implemented methods. The estimates are not maximum-likelihood estimates, and the authors note a small loss of information.

8. **Conclusion.** The multistratum framework allows direct estimation of movement, fidelity, and heterogeneity in survival and capture probabilities. The authors describe the approach as another step toward biological realism in capture-recapture models.