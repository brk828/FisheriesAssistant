---
species: ["Theragra chalcogramma", "Merluccius gayi", "Sebastes alutus"]
common_name: ["Walleye pollock", "Pacific hake", "Pacific ocean perch"]
family: ["Gadidae", "Merlucciidae", "Sebastidae"]
habitat: "Continental shelf and offshore marine waters; also a freshwater lake (Fern Lake) used for a temperature model"
ocean_basin: "North Pacific; South Pacific (Chile)"
location: "Bering Sea; Pacific coast of Chile; Washington coast; Fern Lake (temperature model)"
tags: [ichthyology, marine-biology, fisheries-science, computer-graphics, gadidae, merlucciidae, sebastidae]
title: "Three-Dimensional Computer Graphics in Fisheries Science"
source_id: "PML0302"
marsh_id: "PML0302"
library: "Marsh Library"
permission: "not public domain"
source_citation: "D. J. Brown, L. L. Low (1974). Three-Dimensional Computer Graphics in Fisheries Science. Journal of the Fisheries Research Board of Canada, vol. 31, no. 12, pp. 1927-1935. Marsh Library ID: PML0302."
source_file: "Brown and Low 1974. Three Dimensional Computer Graphics in Fisheries Science.pdf"
text_extraction: "mixed"
---
# Three-Dimensional Computer Graphics in Fisheries Science

#ichthyology #marine-biology #gadidae #merlucciidae #sebastidae

## Executive Summary

This 1974 methods paper by D. J. Brown and L. L. Low, of the [[University of Washington]] Center for Quantitative Science in Fisheries, Forestry, and Wildlife, presents a collection of three-dimensional computer-generated graphics for fisheries science. The authors argue that perspective and orthographic projections of connected data points turn voluminous, complex model output and survey statistics into images that people can interpret quickly. The examples cover spatial catch distributions, survey mosaics, age-length frequencies, equilibrium yield surfaces, and a lake temperature model. The main species are [[Walleye Pollock]] and [[Pacific Hake]], with [[Pacific Ocean Perch]] referenced in one figure.

## Background & Description

The paper introduces a visual technique that simulates biological processes and analyzes fisheries data. The authors say the images help analysts form ideas and communicate multidimensional results. They state that many biological models depend on variables that change across three-dimensional space and time. Applications named in the text include fish behavior, survey biomass calculations, and [[Catch-Effort Statistics]] analysis.

The paper is Contribution No. 406 from the College of Fisheries, University of Washington. It was received on January 25, 1974, and accepted in August 1974. It appeared in the *Journal of the Fisheries Research Board of Canada*, vol. 31(12), pages 1927–1935. A French abstract is included.

The graphics were produced with the PICTURE program, written in [[FORTRAN]] and developed at the [[Los Alamos Scientific Laboratory]]. The images were generated on a CDC 6400 system using a remote display terminal.

## Ecological & Environmental Context

**Bering Sea fisheries.** Much of the spatial material comes from the [[Japanese Mothership Fishery]] in the [[Bering Sea]]. The text also mentions longline-gillnet and independent trawl fisheries. Catch data are from the [[National Marine Fisheries Service]]. The authors note that walleye pollock catch follows the edge of the [[Continental Shelf]], shown against [[Bathymetry]] of the same area.

**Pacific halibut surveys.** Survey data come from the [[International Pacific Halibut Commission]] for the southeastern flats of the Bering Sea.

**Hake off Chile.** Length and age samples of Pacific hake were collected off the central coast of Chile and analyzed by Ehrhardt (1973a, 1973b).

**Rockfish off Washington.** A yield model was applied to a rockfish species off the Washington coast. The species name in the scanned figure caption is partly illegible.

**Lake ecosystem.** A water temperature model of [[Fern Lake]] (Fowler 1973) uses weekly mean air temperature and solar insolation.

## Key Findings

- **Purpose of the method.** Three-dimensional graphics make multidimensional fisheries results easier to interpret and communicate. They also help modelers judge whether a model's predictions match real data.

- **Walleye pollock catch distribution.** Figure 1 maps total walleye pollock catch by the Japanese mothership and independent trawl fisheries in the Bering Sea for 1963–1971 combined. The predominant catch areas follow the continental shelf edge.

- **Dynamics of the groundfish fishery.** Figure 2 shows time-series geographic distributions of annual total groundfish catch in the Bering Sea from 1964 to 1971 for three fleet types.

- **Data handling.** The system summarized about 12,000 records of 80 BCD characters each. Catch and effort arrays can be printed to accompany the graphics. The authors say any combination of spatial-temporal plots by gear type or species can be produced.

- **Halibut survey mosaics.** Figure 4 shows [[Pacific Halibut]] catch in numbers from three International Pacific Halibut Commission surveys, for 1965, 1967, and 1972. Figure 5 shows mosaics for the 1965 survey.

- **Pacific hake growth and longevity.** Age-length frequency graphs for male and female [[Pacific Hake]] show that females live longer. Males do not appear at age 6. Females are longer than males at the same age. The spread of length peaks narrows with age, which the authors link to decreasing growth rate as predicted by the [[Von Bertalanffy Equation]].

- **Equilibrium yield surfaces.** Yield-per-recruit surfaces were built from the [[Beverton-Holt Yield Model]] (Paulik and Gales 1964), using [[Natural Mortality]] (M), [[Fishing Mortality]] (F), and age at entry. Figure 7 shows four views of the male hake surface at M = 0.40. Figure 8 shows a two-dimensional yield surface for female hake at M = 0.4. Figure 9 shows yield-per-recruit surfaces for a rockfish species over a range of natural mortality rates (read as 0.1 to 0.35) and fishing mortality rates (0 to 2.5).

- **Management implications.** The authors say that as natural mortality rises, equilibrium yields fall and the age at entry for maximum yield should also decrease. The surfaces are presented as tools for management decisions.

- **Lake temperature model.** Figure 10 shows predicted Fern Lake temperature profiles. The surface peaks in the hottest weeks, while the bottom peaks a few weeks later. The rear view shows thermal stratification changing to even temperatures in autumn. The authors note that predicted profiles closely match profiles from real data.