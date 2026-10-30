---
species:
  - "Strix occidentalis caurina"
  - "Sturnus vulgaris"
  - "Salmo spp."
  - "Oncorhynchus spp."
  - "Oncorhynchus kisutch"
  - "Gopherus agassizii"
  - "Falco peregrinus"
  - "Pelecanus occidentalis"
  - "Somateria fischeri"
  - "Anas rubripes"
  - "Accipiter gentilis"
  - "Brachyramphus marmoratus"
common_name:
  - "Northern spotted owl"
  - "European starling"
  - "Salmonids (trout and salmon)"
  - "Coho salmon"
  - "Desert tortoise"
  - "Peregrine falcon"
  - "Brown pelican"
  - "Spectacled eider"
  - "Black duck"
  - "Northern goshawk"
  - "Marbled murrelet"
  - "Northern pintail (common name only in source)"
family: N/A
habitat: "Old-growth coniferous forest; fragmented forest habitat; large river systems; hatchery and captive-release settings (as described)"
ocean_basin: "Pacific (implied by salmonid downstream migration to the ocean)"
location: "Pacific Northwest, USA (Columbia and Snake River systems, Oregon, Washington, California); Patuxent Wildlife Research Center, Maryland, USA"
tags: [risk-assessment, population-ecology, capture-recapture, radio-telemetry, hydroelectric-impacts, vertebrate-conservation]
title: "Some specialized risk assessment methodologies for vertebrate populations"
source_id: "PML0056"
marsh_id: "PML0056"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. R. Anderson, G. C. White, K. P. Burnham (1995). Some specialized risk assessment methodologies for vertebrate populations. Environmental and Ecological Statistics, 2, 91-115. Marsh Library ID: PML0056."
source_file: "Anderson et al 1995. Specialized Risk Assessment Methodologies for Vertebrate Populations.pdf"
text_extraction: "ocr"
---
# Specialized Risk Assessment Methodologies for Vertebrate Populations

#ichthyology #marine-biology #salmonidae

## Executive Summary

This methodological review (Anderson, White and Burnham, *Environmental and Ecological Statistics*, 1995) presents three empirical approaches to [[Risk Assessment]] in field studies of free-ranging vertebrates. The first uses statistical inference on recruitment or mortality from [[Capture-Recapture Analysis]], band-recovery and [[Radio-Tracking]] data. The second estimates the [[Finite Rate of Population Change]] (λ) with a [[Leslie-Lefkovitch Matrix]] to judge whether a population is replacing itself. The third uses [[Treatment-Control Experiments]] on marked animals to measure the effect of a specific stressor. The paper stresses [[Model Selection]] by [[Akaike Information Criterion]] (AIC), explicit treatment of uncertainty, and the distinction between sampling and process variance.

The authors illustrate the methods with a meta-analysis of [[Northern Spotted Owl]] populations on five study areas, which found declining adult female survival and a population not replacing itself. Experimental examples cover pesticide effects on [[European Starling]] nestlings and the mortality of juvenile salmon passing [[Hydroelectric Dams]] on the [[Columbia River]].

## Background & Description

The paper takes a broad working definition of ecological risk assessment, drawing on the US Environmental Protection Agency's Risk Assessment Forum (1992): evaluating the likelihood that adverse ecological effects occur from exposure to one or more stressors. The authors apply it to populations of higher vertebrates, and the methods are said to be relevant to many free-ranging vertebrate and invertebrate species.

The source is a methods paper, not a single-species study. It treats the species below as case studies:

- **Northern spotted owl** (*Strix occidentalis caurina*): the main case study; threatened under the [[Endangered Species Act]], associated with old-growth forest.
- **European starling** (*Sturnus vulgaris*): pesticide exposure of nestlings.
- **Juvenile salmonids** (*Oncorhynchus* and *Salmo* spp.), including **coho salmon** (*Oncorhynchus kisutch*): mortality during passage through dam turbines.
- **Northern pintail** ducks: lead ingestion (described by common name only).
- Species cited as examples of declining populations: [[Desert Tortoise]], peregrine falcon, brown pelican, spectacled eider, black duck, northern goshawk and marbled murrelet.

## Ecological & Environmental Context

The authors state that forest management in the Pacific Northwest over the past century has nearly eliminated old-growth forest suitable for the northern spotted owl. Clear-cut logging was the dominant land use on the study areas, and the remaining habitat was highly fragmented. Intensive timber management has also led to the listing of the marbled murrelet as threatened and of many salmonid stocks as endangered.

For the desert tortoise, the paper describes several interacting stressors: habitat loss and fragmentation, drought, disease, recreation, shooting, overgrazing and vegetation spraying. The authors note that the key stressor is not always clear. Desert tortoise subpopulations appear to be declining, but grazing by domestic cattle has not been shown to be the main cause.

For salmonids, the concern is mortality during downstream migration past hydroelectric turbines, bypass systems and spillways in the Columbia and Snake river systems.

Habitat is defined as the ensemble of resources an animal needs to survive and reproduce. These resources can be reduced directly, or stressed in ways that lower their quality or quantity.

## Key Findings

**Methodological framework**

- Six components for an objective impact assessment: (1) estimation of effects, (2) estimation of uncertainty, (3) statement and tests of assumptions, (4) critical review of supporting evidence, (5) critical review of conflicting evidence, (6) weighing of all evidence. The paper concentrates on components 1–3.
- Survival is estimated from capture histories. Unique marks are required, and capture probabilities are nuisance parameters that must be modelled to avoid biased survival estimates.
- Permanent emigration biases survival estimates downward. Heterogeneity and non-independence do not bias parameter estimates but make sampling variances too small.
- Survival from radio-tracking is modelled with logistic, complementary log-log or [[Kaplan-Meier Estimator]]-type methods. Radio failure requires censoring, and sample sizes are often too small by an order of magnitude.
- Variance for λ is computed with the [[Delta Method]]. The authors report it performs well when the separate demographic parameters have coefficients of variation under about 20%.
- For [[Population Viability Analysis]], sampling variance should not be treated as process variance. Only year-to-year variation in the parameters belongs in Monte Carlo trials.
- Under [[Model Selection]], AIC is computed as −2ln(L) + 2K. A quasi-likelihood version (QAIC) adjusts for overdispersion using ĉ = χ²/df.

**Northern spotted owl case study**

- Over 2300 owls were marked on five large study areas. Adult resighting probability was about 0.8–0.9.
- Individuals marked by area (Table 1): Northwest California 400 (1985–91), H. J. Andrews 358 (1987–91), Medford 703 (1985–91), Roseburg 589 (1985–91), Olympic Peninsula 302 (1987–91).
- The finite rate of change λ was below 1 on every area (Table 4): Northwest California 0.9153, H. J. Andrews 0.9276, Medford 0.8444, Roseburg 0.9405, Olympic Peninsula 0.8828. The simple average was 0.9021 (the text gives 0.9022). Every test rejected λ ≥ 1 in favour of λ < 1.
- The population of resident, territorial females was therefore not replacing itself on any study area, with an average decline of about 10% per year over 1985–91.
- Adult female survival is the most influential parameter for λ, more so than juvenile survival or fecundity.
- The meta-analysis of 64 candidate models selected a model with a linear time trend in logit-scale survival. Adult female survival fell from 0.888 (1985–86) to 0.793 (1990–91). Survival was found to decrease over time in all five areas, and no significant study-area effect was detected. The authors estimate the population declined by about 7.5% per year over 1985–91 and that the decline probably accelerated.
- Individual data sets could not demonstrate this trend, which the joint analysis did.
- The authors call for continued monitoring and say emergency risk management should be considered if declines continue.

**Experimental case studies**

- **Pesticide and starlings:** Stromborg et al. (1988) gave 60 treated and 41 control nestlings an organophosphate pesticide or corn oil. Capture probability was 0.78. The treatment/control survival ratio was 0.906 (SE 0.1036), not significantly different from 1. Statistical power was only about 0.17, so the null result is weak.
- **Dams and coho salmon:** Long et al. (1975) released 12 treatment–control pairs at Lower Monumental Dam, with recapture at three dams (k = 3). Treatment groups totalled 258,090 fish and controls 130,159. The average survival ratio (risk) was 0.817 (SE 0.0329), significantly below 1 (χ² = 39.1, P < 0.0001). A goodness-of-fit ratio of 13.1/10 gave ĉ = 1.31, so the adjusted SE is 0.0377.
- **Rocky Reach Dam (May 1993):** Turb'N Tags achieved recapture probabilities of 0.9–0.95, with lots of 100–200 fish found adequate.
- **Pintail ducks and lead:** Deuel (1985) dosed birds with two lead pellets. Over 8600 birds were banded in seven lots. The survival ratio was 1.008 (SE 0.070), so no treatment effect was detected.

**Conclusions**

- Risk assessment must often rely on marked-animal samples, and the theory and software (for example RELEASE, SURVIV, SURGE and SURPH) are well developed.
- Treatment–control experiments are preferred where feasible, because they establish causal links rather than relying on correlative inference.
- Because λ is driven by adult survival and the processes of birth, death, immigration and emigration are the mechanism, λ can detect population trends without a population count.
- Ecosystem-level risk is difficult to study directly. Indicator species may still help if several trophic levels are represented.
- Risk assessment is often retrospective, and risk management should be adaptive. Clear separation of science, management and policy is recommended.