---
species: Branta canadensis
common_name: Canada goose
family: Anatidae
habitat: Wintering grounds (three wintering regions; specific habitat types not described)
ocean_basin: N/A
location: Three wintering regions in North America (exact sites not specified in the document)
tags: [ornithology, capture-recapture, multistate-models, goodness-of-fit, anatidae]
title: "A Proposal for a Goodness-of-Fit Test to the Arnason-Schwarz Multisite Capture-Recapture Model"
source_id: "PML2163"
marsh_id: "PML2163"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. Pradel, C. M. A. Wintrebert, O. Gimenez (2003). A Proposal for a Goodness-of-Fit Test to the Arnason-Schwarz Multisite Capture-Recapture Model. Biometrics 59, 43-53. Marsh Library ID: PML2163."
source_file: "Pradel R. et al. 2003. A proposal for a goodness of fit test to the amason schwarz multisite capture recapture model.pdf"
text_extraction: "mixed"
---
# Goodness-of-Fit Test for the Arnason-Schwarz Multisite Capture-Recapture Model

#ornithology #anatidae #branta-canadensis #capture-recapture #statistical-ecology

## Executive Summary

This methodological paper (Pradel, Wintrebert, and Gimenez, *Biometrics* 59, 43-53, March 2003) proposes a goodness-of-fit (GOF) test for multisite, or multistate, [[Capture-Recapture Models]]. Reliable GOF tests were lacking for these models. The authors extend the "peeling-pooling" logic of the single-site [[Cormack-Jolly-Seber Model]] to the [[Arnason-Schwarz Model]] (AS) and to its more general alternative, the [[JMV Model]]. They build two test families, Test3G and TestM, and propose a likelihood ratio test of AS against JMV. The method is illustrated with a re-analysis of wintering [[Canada Goose]] movement data. The analysis finds that JMV fits poorly, while AS is accepted once the variability detected under JMV is accounted for. A partitioned sub-test, TestWBWA, captures most of the lack of fit and points to a "memory" effect, in which geese return to previously visited sites.

## Background & Description

Repeated observations of individually marked animals are a primary source of information on population dynamics (Seber, 1982; Lebreton, Pradel, and Clobert, 1993). Standard analyses rely on multinomial sampling models, and identifying at least one model that fits the data remains critical even under information-theoretic model selection. An omnibus GOF test that compares observed and expected counts for every capture history becomes impractical as the number of sampling occasions *k* grows, because sparse cells multiply faster than the number of animals.

The single-site reference model, the CJS model, assumes common survival and capture probabilities and independence among individuals. Its GOF test can be partitioned into components with biological meaning. [[Burnham Peeling-Pooling Method]] (1991) derives this test using a "peeling and pooling" procedure. The authors ask whether the same approach extends to the AS model, which is the direct multisite generalization of CJS.

Key definitions:
- **Release batch:** animals released simultaneously. Animals may belong to several batches, so "batch" is preferred over "cohort."
- **Subbatch:** animals within a batch sharing the same previous capture history.
- **Parameters:** survival over a time interval (φ) and capture probability at each occasion (p). In the (α, β) reparameterization, α is the probability of being recaptured and β the probability of remaining at risk.

## Ecological & Environmental Context

The authors frame the case study around wintering site choice. Canada geese (*Branta canadensis*) move among geographic wintering regions across years, a classic situation for multistate models that track transitions among states. Earlier analyses of this data set (Hestbeck, Nichols, and Malecki, 1991; Brownie et al., 1993) found that geese tend to return to a site visited in an earlier year, though not necessarily the most recent one. This violates the AS assumption that movement depends only on the current location. It motivated the [[Memory Model]] of Brownie et al. (1993), a non-Markovian alternative.

The full data set covers three wintering regions and six years of observations. Some expected cell counts were small, so pooling was required.

## Key Findings

**Theoretical results**

- **Biological Property 2 (multisite):** animals present at the same time and site are indistinguishable. Unlike the single-site case, the multisite peeling-pooling method stops after the first step. The conditional multinomials cannot be pooled across batches with different release sites.
- **Biological Property 3 (mixture property):** an animal released earlier that is alive and not captured at time *i* behaves, from that time on, like an animal released at time *i* at one of the *s* sites. Consequently, conditional multinomials from earlier batches are mixtures of those from batches released at time *i*−1. This property is the basis of the new test for mixtures, TestM.
- **Characterization 1:** AS is the model in which survival-movement (α) probabilities depend on interval, departure site, and arrival site, and the ratio of β parameters does not depend on the departure site.
- **Characterization 2:** JMV is the model in which all subbatches of a batch share cell probabilities, and first reobservations from one batch are mixtures of those from the batches released at the next occasion. JMV has a simpler characterization than AS in the (α, β) parameterization.

**Proposed tests**

- **Test3G:** a generalization of the unisite Test3, built as a sum of contingency-table tests of homogeneity for each release batch (*s* sites × *k* occasions). The paper notes that for *k* = 6 and *s* = 3, there are 12 tests Test3(i, l) and 3 mixture tests M_i.
- **TestM:** tests whether first reobservations from earlier batches are mixtures of those from current-release bases. It is computed for *i* = 2, ..., *k*−2.
- **Likelihood ratio test (AS vs JMV):** the paper suggests this as a complement. It is intended to assess AS fit once JMV fit is established.
- **TestWBWA ("where before" vs "where after"):** a partition of Test3G that tests whether an animal's previous and next sites are associated. It is a targeted test of the memory alternative.

**Canada goose results**

- **JMV model:** clearly rejected, χ²(150) = 854.2385, P < 0.0001.
- **AS model:** accepted after accounting for the variability detected under JMV, by analysis of deviance, F(24, 150) reported as 0.74 with P = 0.81. The printed value is partly garbled by OCR and should be checked against the original.
- **Test3G overall:** χ² = 760.4179 (P < 0.0001), with component-level tests all significant at P < 0.0001 or nearby. Several components (e.g., Test3(2,3) and Test3(5,1)) showed strong departures.
- **TestM overall:** χ² = 93.8206 on 54 df, P = 0.0006. Component tests range from P = 0.1470 (TestM2) to P = 0.0006 for the combined test.
- **Likelihood ratio, AS vs JMV:** reported as χ² ≈ 107 with P < 0.0001. The printed digits are unclear in the source.
- **TestWBWA:** shows a strong positive relationship between where an animal was last seen and where it will next be seen, "whatever the present location." It strongly supports memory in wintering-region choice. Under the WBWA residual deviance, the AS vs JMV difference is not significant (F(24, 26) = 0.22, P = 1). This indicates JMV offers no improvement over AS once memory is partitioned out.

**Methodological conclusions**

- Combining Test3G and TestM assesses JMV fit. Adding a likelihood ratio test of AS vs JMV allows assessment of AS.
- Pooling is necessary to keep expected cell values above 2. Fisher's exact test or Monte Carlo methods are alternatives for Test3G.
- Pooling for the geese followed a "here" versus "elsewhere" logic.
- For *k* > 3, moment-type estimators of JMV (Brownie et al., 1993) are not maximum likelihood estimators. The minimal sufficient statistics for mixtures of multinomials have greater dimensionality than the parameters.
- The tests are implemented in the software program U-CARE version 2.0, which is freely available from the CEFE/CNRS FTP site.

**Conclusions and recommendations**

The authors argue that AS is the natural biological generalization of CJS, whereas JMV is more appropriate methodologically. Because JMV is hard to interpret biologically, the authors recommend partitioning and pooling strategies tailored to broad classes of data. Their intent is to make Test3G and TestM more informative and more efficient. The memory model is likely a more biologically plausible alternative to AS than JMV, so partitioning should target memory-type departures.