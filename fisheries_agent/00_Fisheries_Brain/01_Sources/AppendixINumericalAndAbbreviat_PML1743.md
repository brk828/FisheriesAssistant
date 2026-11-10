---
species: N/A
common_name: N/A
family: N/A
habitat: Aquatic and semi-aquatic habitats of the Lower Colorado River, including mainstream channel, backwaters, reservoirs, lakes, canals, and drains
ocean_basin: N/A
location: Lower Colorado River Basin, including Arizona and Yuma Valley sites
tags: [freshwater-ecology, aquatic-ecology, data-coding, habitat-classification]
title: "Appendix I: Numerical and Abbreviated Codes Used in Aquatic and Semi-aquatic Systems of the Lower Colorado River Basin Studies"
source_id: "PML1743"
marsh_id: "PML1743"
library: "Marsh Library"
permission: "not public domain"
source_citation: "Minckley (1976). Appendix I: Numerical and Abbreviated Codes Used in Aquatic and Semi-aquatic Systems of the Lower Colorado River Basin Studies. Marsh Library ID: PML1743."
source_file: "Minckley 1976. Appendix 1 Numerical and Abbreviated Codes Used in Aquatic and Semi-Aquatic.pdf"
text_extraction: "reocr (300 dpi, rotation)"
rebuilt: "2026-11-10"
---
# Appendix I: Numerical and Abbreviated Codes Used in Aquatic and Semi-aquatic Systems of the Lower Colorado River Basin Studies

#freshwater-ecology #aquatic-ecology #data-coding #habitat-classification

## Executive Summary

This appendix is a coding manual, not a field study. It defines the numerical and abbreviated codes used to store data from [[Aquatic And Semi-Aquatic Systems Of The Lower Colorado River Basin]] studies. The codes cover habitat parameters, sampling devices, sampling localities, field data sheets, and stomach analyses. The coding system was compiled under a [[Bureau Of Reclamation]] contract (1974–75) for the [[Colorado River Project]]. Its basic spatial reference is river mile, following the [[Colorado River Maps]] publication. The element was created on 25 June 1975 and the sampling-device element on 2 July 1975, both by [[W. L. Minckley]]. The document reports no species abundances, sample counts, or statistics. Its value is in the standardized vocabulary it defines.

## Background & Description

The code system is organized into six elements:

- **Codes1:** Habitat parameters, such as current, bottom type, bank type, cover, aquatic vegetation, and human use.
- **Codes2:** Sampling devices, including gill nets, hoop nets, seines, trammel nets, dredges, plankton nets, and drift nets.
- **Codes3:** Sampling localities, a list of about 45 codes for lakes, backwaters, canals, drains, and reservoirs.
- **Codes4 and Codes5:** Elements within the disk file and programs. These are referenced but not detailed in this excerpt.
- **Codes6:** Field data sheets, identified by control numbers.

The element **GROUPNUMS** assigns arbitrary numerical designations to organism groupings. The disk file **DIC*SPECIESCODE** holds codes for the taxa on which data were compiled or were being compiled. The taxa themselves are not named in this excerpt.

The river is divided into ten divisions, running from roughly river mile (RM) 422 to RM 704:

1. [[Mohave Valley]] (RM 422–464)
2. [[Topock Gorge]] (RM 464–478)
3. [[Havasu Division]] (RM 478–524.5)
4. [[Parker Division]] (RM 524.5–568.8)
5. [[Palo Verde Division]] (RM 568.8–598.6)
6. [[Cibola Division]] (RM 598.6–619.9)
7. [[Imperial Division]] (RM 619.9–657.2)
8. [[Laguna Division]] (RM 657.2–662.6)
9. [[Yuma Valley]] (RM 662.6–683.7)
10. [[Limitrophe Division]] (RM 683.7–704.2)

Positions relative to the mainstream are coded as follows:

- **LC:** left bank, looking downstream
- **CC:** center of channel
- **RC:** right bank, looking downstream
- **BR:** backwater connected to the mainstream
- **BI:** backwater independent of the mainstream
- **DR:** drain of inflow, wastewater, or return water
- **CA:** canal, at its departure point or at a distant point from intake (positioned as east or west of a river mile)

## Ecological & Environmental Context

**Habitat parameters (Codes1)** describe the physical setting in detail:

- **Currents** combine velocity and turbulence. Categories are: unknown, none, slow (less than 0.5 m/s), moderate (0.5–1.0 m/s), and fast (greater than 1.0 m/s). Each speed class is further split into laminar channel, turbulent channel, and torrential chute.
- **Bottom types** run from sapropelic and mud through silt, sand, gravel, boulder, and bedrock. Each may be stable or moving, and some are coded as cut or uncut.
- **Banks** include marshland, backwater, and mud, with cut or uncut status.
- **Bank modifications** include rip-rap, jetties, and armored points, each marked as heterogeneous or homogeneous, and dressed or filled. Human-use intensity is coded as sparse, moderate, or intense.
- **Aquatic vegetation** covers submergent algae (encrusting and filamentous), submergent higher plants, emergent rooted and floating plants, and flooded terrestrial grasses, brush, trees, and riparian zones. Each is scored as sparse, moderate, or dense.
- **Cover** includes allochthonous debris, brush through logs, inorganic debris, undercut banks, and overhanging riparian vegetation, each also scored by density.

**Sampling devices (Codes2)** span about 37 numbered codes:

- Gill nets (conventional experimental, Swedish, and various mesh sizes from 1/2 to 3 inches, 100 to 300 feet long)
- Hoop nets (large and small mesh)
- Seines (small mesh 1–2 m and 3–6 m; larger seines 3–9 m and 9–19 m)
- Trammel nets (1- and 2-inch inner mesh)
- Hook and line
- Benthic samplers: Ekman dredge, Peterson dredge, Clark-Bumpus sampler, Surber sampler, metric grab, and 1 cm scrapes of natural and artificial substrates
- Plankton and drift nets (#10, #20, #40 mesh)
- Vertical nets (1/2-, 1.5-, and 3-inch mesh)
- Methods without nets: ichthyotoxins, visual observation, dip net, and hand catch

**Sampling localities (Codes3)** include about 45 named sites. Examples include:

- Salt River Project lakes in central Arizona: [[Apache Lake]], [[Canyon Lake]], [[Roosevelt Lake]], and [[Saguaro Lake]]
- Havasu Division: [[Moovaylla Lake]], [[Moovaylla Pond]], and [[Moovaylla Cove]]
- Cibola and Imperial divisions: oxbows, dredged backwaters, [[Imperial Reservoir]], and access lakes such as [[Ferguson Lake]] and [[Martinez Lake]]
- Laguna Division: [[Laguna Settling Basin]]
- Yuma Valley: many canals and drains, including the [[West Main Canal]], [[East Main Canal]], [[Central Canal]], and [[Main Drain]]

The document lists the code WC twice, for both Walter's Camp Oxbow and West Canal. The duplicate is not resolved in this excerpt.

## Key Findings

- **The document is a standardized data dictionary.** It sets common codes so that field records from different studies and personnel can be compared and combined.
- **Habitat is described in detail.** The system codes current speed, flow regime, bottom substrate, bank type, cover, vegetation density, and human disturbance. Density is always graded sparse, moderate, or dense, which makes records comparable across sites.
- **Sampling effort is recorded by device and locality.** Each catch record links to a specific device, site, and habitat condition, supporting [[Catch Per Unit Effort]] calculations.
- **Field data sheets have fixed control numbers.** Control number 2001 is a header for a catch at a locality, 2002 records a captured animal, and 2003 records an unsuccessful set with no catch. Control numbers 2011–2013 cover areal catches (seines, dredges, quadrats), with 2011 as the header, 2012 for organisms taken, and 2013 for empty attempts. Control numbers 2601–2603 cover [[Stomach Content Analysis]].
- **Individual animal data are coded in detail.** Records include:
  - length (standard or fork length, in metric units) and weight (in grams)
  - preservation and retention status
  - sex
  - maturity, on a six-stage scale from unknown to senile
  - gut and scale status
  - visceral fat, on a five-level scale
  - parasites, with nine categories such as anchorworm, blackspot, yellow grub, roundworms, flukes, and tapeworms
- **Stomach contents are measured by volume or weight.** The document assumes 1 cc equals 1 g, since most aquatic animals have a density close to 1.0. Food items are coded by developmental stage, from egg and larva through pupa and adult.
- **Rules for changing the code set are fixed.** Any user who modifies the elements must record their name, the date, and the change directly below the explanatory statement. Existing control numbers must not be changed. Codes are expected to expand as new habitat parameters, sampling devices, and sites are added.