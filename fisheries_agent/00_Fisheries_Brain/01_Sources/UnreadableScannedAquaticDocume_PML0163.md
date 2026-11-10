---
species: Salvelinus alpinus; Oncorhynchus mykiss
common_name: Arctic char; Rainbow trout
family: Salmonidae
habitat: Freshwater rivers and lakes (Wood River system; Kenai River)
ocean_basin: N/A
location: Alaska, USA (Wood River system; Kenai River)
tags: [ichthyology, marine-biology, salmonidae, fish-growth, mark-recapture, growth-modelling]
title: "A General Growth Model for Mark-Recapture Data"
source_id: "PML0163"
marsh_id: "PML0163"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Baker et al. (1991). A General Growth Model for Mark-Recapture Data. Marsh Library ID: PML0163."
source_file: "Baker et al. 1991. General Growth Model for Mark-Recapture Data.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# A General Growth Model for Mark-Recapture Data

#ichthyology #marine-biology #salmonidae

## Executive Summary

Baker, Lafferty and Quinn (1991, *Fisheries Research* 11: 257–281) extend [[Schnute Growth Model]], a general four-parameter size-age growth model that contains many classical curves (von Bertalanffy, Gompertz, Richards, logistic, linear, power) as submodels, to [[Mark-Recapture Data]]. Mark-recapture data contain only three distinct parameters because true fish age is absent, so a growth model can be determined only if one parameter, usually size at the starting age, is specified beforehand. The model was applied to two Alaskan datasets: [[Arctic Char]] in the Wood River system and [[Rainbow Trout]] in the Kenai River. Different growth formulations were selected for age-size and mark-recapture data within each species, and the von Bertalanffy model was selected in only one of the four comparisons.

## Background & Description

Growth information underpins fisheries management in Alaska, informing stock structure, [[Sustainable Yield]], and the efficacy of minimum, maximum and slot size limits. Growth overfishing can readily occur in both commercial and sport fisheries, making growth status central to stock assessment.

Historically, growth models (von Bertalanffy, Gompertz, Richards, logistic, linear, exponential) and estimation methods (e.g., Walford 1946; Fabens 1965; Allen 1966; Gallucci and Quinn 1979; Misra 1980, 1986) have been chosen subjectively. [[Schnute Growth Model]] (Schnute 1981) resolved this by casting these models as submodels of one framework derived from a linear growth-acceleration principle. The two common data sources are:

- **Age-size data** (age-length, age-weight): cheap and easy to collect, but ageing methods are often inaccurate.
- **Mark-recapture data**: more expensive and time-consuming, and marking may affect growth, but they measure individual growth over the interval between marking and recapture without requiring known age.

Previous mark-recapture approaches were limited: Ebert (1980) required equal time at large for all marks; McCaughran (1981) fitted a two-parameter allometric model; Kirkwood (1983) and Francis (1988) fitted the three-parameter von Bertalanffy model. None matched the flexibility of Schnute's model.

## Ecological & Environmental Context

**Study systems**

- **Wood River system, Alaska:** a lake and river system used by [[Arctic Char]] for feeding and spawning. Char larger than 300 mm were considered capable of significant predation on [[Sockeye Salmon]] smolts, which motivated the study.
- **Kenai River, Alaska:** the source of [[Rainbow Trout]] growth data, collected during 1986–1987 (Lafferty 1989).

**Ageing and data-quality issues**

- Arctic char ages from sagittal otoliths may be underestimated; the authors note controversy in the literature (Barber and McFarlane 1987).
- Rainbow trout ages from scales may be overestimated (Fig. 6 interpretation).
- Marking can reduce growth (McFarlane and Beamish 1990), which may explain divergence in older rainbow trout.

**Temporal and sampling factors**

- Arctic char mark-recapture data were collected 1975–1979, while age-length data came from 1985, so growth may have changed between periods.
- Most Arctic char mark-recapture observations fell between 350 and 600 mm, so the fit is weighted toward mid-size fish.

## Key Findings

**Methodological results**

- Schnute's age-size model has four parameters (a, b, γ1, γ2). The mark-recapture equivalent has three (a, b, k), because subtracting times eliminates a parameter. Equation (11) gives the mark-recapture asymptotic growth law: Y_m = [Y_m^{…}] form with k = γ2^b.
- Size at the youngest age (γ1) must be fixed from age-length data; mark-recapture data alone cannot determine a definite size at a prescribed age.
- Additive and multiplicative error structures gave similar parameter estimates and model selections in all four datasets. Additive error converged more readily.
- Case 1 with multiplicative error gave unstable estimates from varied starting values, possibly indicating an unstable model structure.
- The authors chose not to combine likelihoods from the two data types (as in [[Kirkwood Method]]), because growth parameters estimated from age-size and mark-recapture data may not be comparable (Francis 1988).

**Arctic char, Wood River system (age-length n = 536; mark-recapture n = 2695)**

- Age-length data (ages 5–16): the most parsimonious model was Case 3, a 1/1.5 root curve (b = 1.55 additive; 1.58 multiplicative). γ1 = 319 mm (additive) and 318 mm (multiplicative); γ2 = 678 mm.
- Mark-recapture data: the von Bertalanffy submodel (LVB 1) was selected, with γ2 = 585 mm (additive; a = 0.19) and 584 mm (multiplicative), with γ1 fixed at 319 mm.
- Mark-recapture growth was slower than age-length growth, particularly for older fish. The authors argue this supports the view that otolith-based ages underestimate true age.

**Rainbow trout, Kenai River (age-length n = 998; mark-recapture n = 2742 tagged, 302 growth observations)**

- Age-length data (ages 2–12): the most parsimonious model was Case 2 (Gompertz), with γ1 = 234 mm, γ2 = 729 mm and a = 0.19 (additive); γ2 = 728 mm and a = 0.19 (multiplicative).
- Mark-recapture data: Case 3, a 1/2.8 root curve (b = 2.83 additive; 2.79 multiplicative), with γ2 = 729 mm (additive) and 705 mm (multiplicative). This curve has no asymptote.
- Mark-recapture growth was faster for young fish and slower for older fish than age-length growth.

**Overall conclusions**

- Schnute's model selected three different submodels across the four datasets, with the von Bertalanffy curve chosen only once, supporting the use of more flexible growth models.
- Individual variation can be incorporated by fitting per-fish parameters (following McCaughran 1981), with length-weight data fixing b and age-length data fixing γ1, though this requires age information. Without age, one parameter must be fixed.
- Proposed explanations for divergence between data sources include variability in individual growth, growth reduction from marking, temporal change, and ageing error.