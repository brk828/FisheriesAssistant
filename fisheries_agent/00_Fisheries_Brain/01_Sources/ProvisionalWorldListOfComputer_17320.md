---
species: "N/A (multi-taxon catalogue; examples include Illex squid, Cape hakes, spiny lobsters and shrimp)"
common_name: "N/A"
family: "N/A"
habitat: "Marine and coastal fisheries (general)"
ocean_basin: "Multiple (global catalogue)"
location: "Global: Australia, Canada, FAO (Rome), France, Kenya, Kuwait, New Zealand, Philippines, South Africa, Spain, UK, USA, USSR"
tags: [fish-stock-assessment, fisheries-software, computer-programmes, catalogue]
title: "Provisional world list of computer programmes for fish stock assessment and their availability by country and fisheries institute"
source_id: "17320"
minckley_id: "17320"
source_citation: "J. F. Caddy (1982). Provisional world list of computer programmes for fish stock assessment and their availability by country and fisheries institute. FAO Fisheries Circular Rome:Food and Agriculture Organization of the United Nations. Minckley Library ID: 17320."
source_file: "17320.pdf"
text_extraction: "ocr"
---
# Provisional World List of Computer Programmes for Fish Stock Assessment

#ichthyology #marine-biology #fish-stock-assessment

## Executive Summary

This document is FAO Fisheries Circular No. 746 (April 1982), edited by J.F. Caddy of the [[FAO Fisheries Department]]'s Marine Resources Service. It is an annotated, provisional catalogue of computer programmes used in [[Fish Stock Assessment]] that participating fisheries institutes are willing to make available to outside users. It was compiled from questionnaire responses and was intended as an interim resource, replacing the out-of-print [[Abramson Programme Compilation]] (1971). FAO does not test the programmes, does not guarantee their accuracy, and does not provide problem-solving support; responsibility for correct use rests with the user, and donor institutes may assist at their discretion.

## Background & Description

The catalogue arose from repeated requests to FAO for programmes after the 1971 Abramson compilation went out of print. In 1980 an in-house review noted that no comprehensive international initiative had followed it. A questionnaire was sent to institutes that had previously supplied FAO with scientific computing input. It asked for programme name, documentation state, programming language, and soft- and hardware requirements. Responses are reproduced in annotated tables in the language of each donor institute, so that correspondence goes directly to the donor.

The listing covers institutes in the following countries and organisations:

- [[CSIRO Division of Fisheries and Oceanography]] (Australia)
- Department of Fisheries and Oceans, [[Bedford Institute of Oceanography]], and the Invertebrates and Marine Plants Division (Canada)
- [[FAO Fisheries Department]] (Italy)
- ISTPM (La Rochelle and Sète) and CNEXO/COB Brest (France)
- Ecosystems Ltd (Kenya)
- [[Kuwait Institute for Scientific Research]]
- Ministry of Agriculture and Fisheries, Fisheries Research Division (New Zealand)
- [[ICLARM]] (Philippines)
- Department of Sea Fisheries (South Africa)
- Instituto Español de Oceanografía (Spain)
- Department of Agriculture and Fisheries for Scotland (UK)
- [[National Marine Fisheries Service]] Woods Hole and Fisheries Analysis Center, University of Washington (USA)
- [[VNIRO]] and ATLANTNIRO (USSR)

Entries are classified by computation type (for example, [[Virtual Population Analysis]], [[Cohort Analysis]], growth fitting, yield per recruit, production modelling) and by language (FORTRAN, BASIC, APL, HP and Texas Instruments programmable calculators). Standard key codes indicate whether a programme has comments in English (E), Spanish (S) or French (F), a separate theory description, a card deck, or a test deck.

## Ecological & Environmental Context

The catalogue is not biological research, but it documents the analytical tools used to model exploited fish and shellfish populations. Methods listed include:

- **Growth:** [[Von Bertalanffy Growth Equation]] fitting to length-at-age, tag-recapture and unequally spaced data; Gompertz growth; seasonally oscillating growth models ([[ELEFAN]] and related programmes).
- **Mortality and cohort analysis:** [[Pope Cohort Analysis]], Gulland's VPA, Fry's virtual population method, Brander's weighted Z estimation, and catch-curve analysis after [[Robson and Chapman Method]].
- **Yield and stock-recruitment:** [[Yield Per Recruit]] (Thompson and Bell, [[Beverton and Holt Method]], Ricker's method), isopleth diagrams, and stock-recruitment curves (Ricker, Beverton-Holt, Shepherd).
- **Production models:** [[Schaefer Model]], [[Fox Model]], [[Pella-Tomlinson Model]] and other [[Surplus Production Model]] variants.
- **Population size and tagging:** [[Jolly-Seber Method]], Schnabel and Schumacher estimators, and multiple-marking experiments.
- **Size structure:** [[Length-Frequency Analysis]], Hasselblad mixture analysis, and Jones's length-based cohort method.
- **Data management and survey analysis:** acoustic and sonar survey processing, trawl-survey stratified means, and oceanographic and multivariate data routines.

Taxa mentioned in examples include Illex squid on the Scotian Shelf, spiny lobsters, Cape hakes, and Kuwaiti shrimp. Most entries are general-purpose and not tied to a single species.

## Key Findings

- **Purpose and scope:** The catalogue gives an interim list of available stock-assessment programmes and their donor institutes, pending new standard packages in BASIC, FORTRAN and for programmable calculators.
- **Replacement of earlier work:** It updates Abramson (1971, FAO Fisheries Technical Paper 101, 148 p), which had become widely used as a standard FORTRAN base but had grown out of date.
- **Scale:** Institute-level counts range from one or two programmes at smaller centres to 33 at [[Kuwait Institute for Scientific Research]], 27 at the USA [[National Marine Fisheries Service]] (Woods Hole), 13 at Canada's Department of Fisheries and Oceans, and 12 at CNEXO/COB Brest. ISTPM Sète lists 15 programmes.
- **Language mix:** Programmes are written in FORTRAN, BASIC (including extended and RT11 variants), APL (Canadian DFO functions run in APL on terminals), HP desk-top and calculator languages, and TI calculator programmes. Many of the most-used programmes run on HP 9825, 9845 or 9815 machines.
- **Notable systems:**
  - CSIRO's AFZIS, a fisheries data-management system (CDC 7600, about 12,000 statements).
  - Canada's APL package (37 functions, about 3,000 statements).
  - ICLARM's ELEFAN I and II and the ETAL growth programme, by D. Pauly.
  - Spain's HP-based stock-assessment package (VPA, cohort analysis, Ricker, Beverton-Holt, Von Bertalanffy).
  - The USSR VNIRO complex programmes, which compare Schaefer, Fox, Doi, Beverton-Holt and regression estimates of maximum equilibrium catch.
- **Documentation and access:** Many entries are available as listings, examples or theory notes, and some with test decks. Users must state their computer type and compiler language when requesting programmes, and should not ask for listings incompatible with their machine unless they can translate them.
- **Limits:** FAO did not test the programmes and cannot resolve problems arising from their use. Feedback from users is welcomed for future updates.