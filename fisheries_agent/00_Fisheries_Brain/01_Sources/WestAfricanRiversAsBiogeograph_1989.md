---
species: "Multiple freshwater fish species (39 West African + adjacent river systems)"
family: "Multiple families (whole-community ichthyofauna analysis)"
habitat: "Freshwater rivers, tributaries, and catchment/drainage basins"
ocean_basin: "Atlantic Ocean (Senegal to Zaire mouths); Mediterranean (Nile)"
study_type: "Biogeographic / macroecological analysis"
geographic_scope: "West and Central Africa (39 rivers, 11 tributaries)"
source_id: "14506"
---

# West African Rivers as Biogeographic Islands: Species Richness of Fish Communities

#ichthyology #marine-biology #freshwater-biogeography #island-biogeography #west-african-ichthyofauna

## Executive Summary

This study by Bernard Hugueny (1989) tests whether [[Insular Biogeography]] theory (MacArthur & Wilson) applies to West African river fish communities, treating rivers as "islands" isolated by barriers impassable to strictly aquatic fauna. Using data from 39 rivers (and a subset of 26 with additional habitat variables), the analysis found that species richness (SR) scales with catchment surface area via a power function (exponent z = 0.32), consistent with insular species-area predictions (Preston 1962; May 1975). A multivariate model combining ln(catchment surface area) and ln(mean annual discharge) explained ~90% of variance in ln(species richness), outperforming models based on surface area or habitat/vegetation diversity alone. Critically, when this river-based model was applied to 11 "continental" tributaries (which have free faunal exchange with the larger river system), it significantly **underestimated** their observed species richness — supporting the hypothesis that insular systems (rivers) suffer higher population extinction rates than continental systems (tributaries). Spatial autocorrelation analysis of model residuals revealed three regions with anomalously high species richness (Guinea/Gambia, eastern Ivory Coast–Benin, and Cameroon–Gabon–Zaire), partially consistent with proposed Quaternary rainforest refuge zones, suggesting a role for historical climatic factors in shaping present-day diversity patterns.

## Background & Description

- **Conceptual framework**: Rivers, being separated by barriers that strictly aquatic organisms cannot cross, are analogous to biogeographic islands (following [[MacArthur And Wilson Island Biogeography Theory]]), unlike terrestrial "continents" (tributaries within a single connected river system) where fish circulate freely.
- **Historical context**: Prior African studies (Daget & Iltis 1965; Welcomme 1979; Livingstone et al. 1982) established species-area relationships in African rivers but were limited by underestimated species lists, mixing of rivers/tributaries, and use of catchment area (not true water surface area) as a proxy.
- **Data source**: Species lists compiled from ORSTOM's decade-long Onchocerciasis Control Programme fish-monitoring effort (anti-simuliid insecticide impact studies), museum collections (Paris, Tervuren, London), and unpublished reports — substantially improving on earlier, incomplete species inventories.
- **Study design**:
  - 39 rivers analyzed for species richness (SR) vs. surface area (S).
  - Subset of 26 rivers analyzed with four predictors: surface area (S), mean annual discharge (AD), vegetation diversity (DV, Shannon index of terrestrial vegetation types), and percent lowland rainforest cover (PF).
  - 11 tributaries (from Niger, Volta, Sassandra, Bandama systems) used as "continental" controls to test insularity effects.
  - Exclusions: catadromous/marine-tolerant species (rivers not "islands" for them) and lacustrine species (different speciation dynamics, high endemism).

## Ecological & Environmental Context

- **Geographic scope**: Rivers draining into the Atlantic from the [[Senegal River]] to the [[Zaire River]] (Congo), plus the [[Nile River]] (Mediterranean-draining outlier).
- **Vegetation/habitat classification**: Based on White's (1983) African vegetation map; "Sudanian" (savanna) vs. "Guinean" (forest) faunal zones per Daget & Iltis (1965).
- **Hydrological drivers**: Discharge is proportional to surface area × precipitation; also linked to terrestrial primary productivity, which contributes allochthonous organic matter to tropical rivers — a key energy source given high [[Allochthonous Organic Matter]] inputs in tropical river systems.
- **Historical/paleoclimatic context**: Quaternary alternation of dry/humid periods in Africa is invoked to explain anomalous residuals — particularly the species-poor [[Nile River]] fauna (the "Greenwood paradox," Greenwood 1976) relative to the species-rich [[Zaire River]] (Congo) of comparable size.
- **Proposed Pleistocene forest refuge zones** (per Endler 1982; Mayr & O'Hara 1986), relevant to fish diversity anomalies:
  1. Liberia and Sierra Leone
  2. Cameroon and Gabon
  3. Eastern Zaire (Congo)

## Key Findings

### Species-Area Relationships (39 rivers)
- Best-fit model: **ln(SR) = 0.84 + 0.32·ln(S)**, r = 0.899 (P<0.001) — power function exponent **z = 0.32**.
- This z-value falls within the theoretically expected insular range of 0.15–0.39 (May 1975), and close to Preston's (1962) predicted 0.25.
- Residuals from this model showed **no significant spatial autocorrelation**, indicating the model adequately captured geographic variation via surface area alone.
- Comparison of z-values across regions: West Africa (0.32) vs. Welcomme's (1979) broader African sample (0.43, mixed rivers/tributaries) vs. European rivers (0.19–0.24) vs. South America (0.552) — suggesting tropical systems show steeper species-area scaling than temperate systems, possibly reflecting greater tropical habitat/inter-habitat diversity.

### Multiple Regression Analysis (26 rivers)
- High collinearity among predictors (max VIF = 23.53) required [[Ridge Regression]] to stabilize coefficient estimates.
- Forward stepwise selection and ridge trace analysis both converged on retaining only **ln(surface area)** and **ln(mean annual discharge)** as predictors; vegetation diversity (DV) and forest percentage (PF) were eliminated (near-zero or unstable coefficients).
- **Final model**: ln(SR) = 1.504 + 0.135·ln(S) + 0.245·ln(AD)
  - Multiple R = 0.947, VIF = 5.15 (acceptable)
  - Both predictors significant (P = 0.021 for S; P = 0.001 for AD)
  - Model accounted for ~90% of variance in ln(species richness).
- **Habitat diversity hypothesis** (Williams 1964): Vegetation diversity showed a *negative* coefficient under least-squares regression but became *positive* under ridge regression (from k=0.2) — inconclusive evidence, no statistically robust positive effect detected once surface area was included.
- **Habitat productivity hypothesis** (Livingstone et al. 1982): This study's data **did not confirm** Livingstone et al.'s claim that discharge (as a productivity proxy) alone explains species richness with surface area contributing nothing independently — both variables retained independent, significant effects in this West African sample.

### Insularity Effect: Rivers vs. Tributaries
- The river-derived predictive model, when applied to 11 tributaries, **underestimated observed species richness in 9 of 11 cases** (sign test P<0.05).
- Interpreted as support for **area-dependent extinction rate** hypothesis: insular systems (rivers) have higher local extinction risk due to limited immigration/recolonization compared to "continental" tributaries embedded within a freely-connected river system.
- Caveat: small sample size (n=11); alternative predictive models might yield different conclusions.

### Spatial Patterns in Residuals (Historical/Refuge Hypothesis)
- Significant positive spatial autocorrelation detected in residuals of the surface area + discharge model (Moran's I = 0.239, P<0.05), indicating unmodeled geographic structure.
- Three regions showed higher-than-predicted species richness:
  1. **Gambia and Guinea** ([[Gambia River]], [[Konkouré River]]) — near proposed refuge zone 1 (Liberia/Sierra Leone).
  2. **Eastern Ivory Coast to Benin** (Boubo to Oueme rivers) — not explained by known climatic history; likely artifact of incomplete faunal surveys in small western rivers.
  3. **Cameroon–Gabon–Zaire** ([[Nyong River]], [[Ntem River]], [[Ogowe River]], [[Zaire River]]) — strongly consistent with refuge zones 2 and 3.
- **Nile River** and **Sahelian rivers** ([[Senegal River]], [[Niger River]]) showed *fewer* species than predicted, potentially reflecting reduced discharge and fish community attrition during the last Quaternary dry period, with insufficient time for recolonization given fishes' poor overland dispersal ability.
- Overall conclusion: data support presence of Central African forest refugia effects on fish diversity, but validation of the **Pleistocene forest refuge hypothesis** for fish requires additional phylogenetic, distributional, and endemism data beyond species richness counts alone.

### Methodological Notes
- [[Ridge Regression]] was essential given high multicollinearity (VIF > 10) between surface area, discharge, and vegetation diversity.
- [[Moran's I]] spatial autocorrelation testing confirmed unexplained geographic clustering in model residuals, pointing to missing historical/geographic covariates.
- Species richness values used substantially updated and exceeded those employed in earlier studies (Daget & Iltis 1965; Livingstone et al. 1982), underscoring the importance of survey completeness in island-biogeographic analyses of freshwater fish.