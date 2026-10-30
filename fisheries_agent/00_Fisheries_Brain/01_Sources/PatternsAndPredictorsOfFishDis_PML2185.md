---
species: "N/A (62 freshwater fish species across 11 families; salmonids, cyprinids and centrarchids most represented; Salmo trutta cited as worked example)"
common_name: "River fishes (general); Brown Trout (example)"
family: "Salmonidae, Cyprinidae, Centrarchidae, Fundulidae, Cottidae, Catostomidae, Ictaluridae, Percidae and others"
habitat: "Rivers and streams (stream orders 1 to 9)"
ocean_basin: "N/A"
location: "16 countries across five continents (specific sites not itemised)"
tags: [fish-dispersal, freshwater-ecology, meta-analysis, leptokurtic-dispersal, fish-movement]
title: "Patterns and predictors of fish dispersal in rivers"
source_id: "PML2185"
marsh_id: "PML2185"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. Radinger, C. Wolter (2013). Patterns and predictors of fish dispersal in rivers. Fish and Fisheries (DOI: 10.1111/faf.12028). Marsh Library ID: PML2185."
source_file: "Radinger J. et al. 2013. Patterns adn predictors of fish dispersal in rivers.pdf"
text_extraction: "text"
---
# River Fish Dispersal: Patterns and Predictors of Movement in Rivers

#ichthyology #marine-biology #salmonidae #cyprinidae #centrarchidae

## Executive Summary

This quantitative [[Meta-Analysis]] synthesises 160 empirical data sets from 71 studies covering 62 freshwater stream fish species to describe how fish populations disperse. Using fitted [[Leptokurtic Dispersal Kernel]] models, the authors separate each population into a stationary component (high central peak, linked to [[Home Range]] concepts) and a mobile component (long tail). Median movement distances were 36.4 m for the stationary component and 361.7 m for the mobile component, while the median stationary share was 66.6%. Movement distance rose with fish length, caudal fin aspect ratio, stream size and study duration, and differed among taxonomic families. The authors argue that fish populations are heterogeneous rather than sedentary, and that the parameters can inform recolonisation time lags, founder population sizes and range-shift predictions.

## Background & Description

Fish movement research has long debated how mobile or resident fish are. Classic positions ranged from Gerking's (1959) [[Restricted Movement Paradigm]], which treats fish as largely sedentary, to views that fish are wholly mobile. Dispersal theory from [[Island Biogeography]] and [[Metapopulation Dynamics]] links dispersal to emigration, immigration, gene flow and species turnover. Dispersal is defined as a one-way movement away from a site, arising from individual behavioural decisions across life stages.

Despite its ecological importance, quantitative data on dispersal distances, speeds and the share of mobile individuals remain scarce, which hampers prediction of range shifts under global change, invasion rates and recovery of endangered species. The study builds on heterogeneous-movement concepts (Skalski and Gilliam 2000; Rodriguez 2002) that treat populations as mixtures of stationary and mobile individuals.

The dispersal kernel is a mixture of two normal distributions:
- σ_stat: mean movement distance of the stationary component
- σ_mob: mean movement distance of the mobile component
- p: share of the stationary component

Curves were fitted by least squares, with upstream and downstream movement pooled and p set to zero in the fitted function.

## Ecological & Environmental Context

**Data sources and inclusion.** Studies were drawn from peer-reviewed and grey literature via ISI Web of Knowledge, Scopus and Google Scholar, plus cited reports. Inclusion required a river setting, recapture or detection in more than three distance classes, and exclusion of obligate life-cycle migrations such as spawning runs.

**Study designs.** Mark-recapture (n = 119), telemetry (n = 31) and traps (n = 10) were used. Study method had no detectable effect on results.

**Morphometric predictors.** Total length ranged from 39 to 810 mm (median 192.5 mm). Caudal fin aspect ratio ranged from 0.51 to 2.29 (median 1.41) and is used as a proxy for swimming mode and performance.

**Stream size.** Stream order ranged from 1st to 9th (median 3); 61% of data sets came from order ≤3 streams and only 5% from orders ≥7. Most streams had discharge below 15 m³ s⁻¹ (81%) and width below 10 m (62%). Stream order, discharge and width were highly intercorrelated (r = 0.78–0.86) and were therefore modelled separately.

**Study duration.** Ranged from 0.25 to 3285 days (median 150.5 days).

**Regional scope.** The studies came from 16 countries across five continents. The regional list is not itemised in the document.

**Analytical methods.** Analyses used single and multiple linear regressions on log-transformed variables (Box-Cox guided), subsampling with 999 replicates to avoid pseudo-replication, [[Regression Tree Analysis]], [[Linear Mixed-Effects Models]] with family, species and study as random effects, and ANCOVA with Tukey HSD. Software was R 2.15.2 with packages including lme4, rpart and car. An R package, "RdispeRsal", was developed to compute dispersal parameters from the predictors.

## Key Findings

**Population structure**
- Stationary share (p) median was 66.6% (range 11.3–97.6%), with high variation among studies. Mobile individuals on average made up about one-third of the population but reached over 85% in some cases.
- Share p was unrelated to movement distance and showed only a weak relation to fish length (R² = 0.03, P = 0.06).

**Movement distances**
- Stationary component (σ_stat): median 36.2 m (range 0.01–39,760 m).
- Mobile component (σ_mob): median 361.7 m (range 2.22–166,400 m).
- The mobile distance was about 13.7 times the stationary distance (median ratio), a fixed proportion that the authors found surprisingly constant. The correlation between the two was strong (r = 0.91, P < 0.001).

**Predictors (single regressions, all significantly positive, P < 0.01)**
- Fish length: strongest single predictor (R² = 0.46 for σ_mob; 0.44 for σ_stat).
- Aspect ratio: weakest but significant (R² = 0.09 and 0.07).
- Stream size, width, discharge and study duration were also positive predictors.

**Multiple regression**
- The full model (length, aspect ratio, stream order, discharge, width, time) best predicted σ_mob (adjusted R² = 0.78).
- The four-parameter model with stream order as the size proxy best predicted σ_stat (adjusted R² = 0.65).

**Regression trees**
- For σ_stat, one split at 424.5 mm total length produced two terminal nodes.
- For σ_mob, three splits (length 273.5 mm, study time 62.5 days, length 424.5 mm) produced four terminal nodes.
- The authors interpret the 424.5 mm threshold as evidence of an asymptotic relationship: above roughly that length, larger fish disperse less relative to body length.

**Taxonomic differences**
- Cottids moved less than average; fundulids moved more.
- Family differences were significant for σ_stat (ANCOVA F₅,₂₀ = 2.38, P < 0.05) and σ_mob (F₅,₂₅ = 2.75, P < 0.05).

**Mixed models**
- The full model performed best for both components (AIC based on log-likelihood 331.62 for σ_stat; 285.99 for σ_mob).
- The study itself was the largest random-effect variance, consistent with substantial between-study heterogeneity.

**Time**
- Movement distance increased with study duration. The stationary and mobile components expanded at a similar rate, contrary to initial expectations. This supports theory that variance in convoluted normal distributions adds over time.

**Conservation application**
- Using the 50/500 rule (Soulé 1980; Franklin 1980), the authors illustrate that about 50 effective migrants would require a founder population of around 150 spawners, or more if the probability of reaching a site is lower.

**Conclusions**
- Fish populations are heterogeneous, with a mobile and stationary component in every family examined. The authors argue that fish "cannot at all be considered sedentary".
- Movement predictors enable estimation of recolonisation time lags, founder population size, invasion potential and range shifts under climate change.
- Barriers such as dams and weirs truncate dispersal kernels. Dispersal models can incorporate fish passage efficiency to quantify fragmentation effects.