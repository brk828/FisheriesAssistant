---
species: N/A
common_name: N/A
family: N/A
habitat: Freshwater rivers, streams, and tributaries
ocean_basin: N/A
location: Ohio, USA; EPA Region 5 (North Central U.S.)
tags: [ichthyology, freshwater-ecology, bioindicators, environmental-informatics, ohio]
title: "A Computerized System for the Evaluation of Aquatic Habitats Based on Environmental Requirements and Pollution Tolerance Associations of Resident Organisms"
source_id: "PML0533"
marsh_id: "PML0533"
library: "Marsh Library"
permission: "public domain"
source_citation: "C. L. Dawson, R. A. Hellenthal (1986). A Computerized System for the Evaluation of Aquatic Habitats Based on Environmental Requirements and Pollution Tolerance Associations of Resident Organisms. U.S. Environmental Protection Agency, Environmental Research Laboratory, Corvallis, OR; Project Summary EPA/600/S3-86/019. Marsh Library ID: PML0533."
source_file: "Dawson C.L. et al. 1986. A computerized system for the evaluation of aquatic habitats based on environmental requirements and pollutio tolerance associations of resident organisms.pdf"
text_extraction: "mixed"
---
# ERAPT: A Computerized System for Evaluating Aquatic Habitats via Environmental Requirements and Pollution Tolerance Associations

#ichthyology #marine-biology #freshwater-fish-assemblages

## Executive Summary

This EPA Project Summary (EPA/600/S3-86/019, April 1986) describes the [[Environmental Requirements and Pollution Tolerance]] (ERAPT) system, a computerized retrieval and analysis tool for environmental information on aquatic organisms. The system predicts environmental conditions from the organisms present, describes the habitats of specific taxa, and flags inconsistencies that may indicate misidentified organisms or erroneous habitat data. Its databases cover diatoms, [[Blue-Green Algae]], [[Ephemeroptera]], [[Plecoptera]], [[Chironomidae]], and the fishes of [[Environmental Protection Agency Region 5]].

The system was validated by comparing habitat conditions predicted from the five numerically dominant fish species at each site with field-survey habitat data from 64 sites on three Ohio river systems. The overall successful prediction rate was 95%. Most disagreements occurred between similar tolerance ranges or habitat types.

## Background & Description

Aquatic organisms are useful indicators of habitat condition and water quality. They integrate the effects of many environmental factors over time and can show the effects of disturbances after the physical and chemical environment appears normal again. The source notes that organisms play a relatively minor role in aquatic assessment. Reasons given include:

- Difficulty comparing data gathered by different researchers.
- Variable environmental requirements among species.
- Inconsistent collection and analysis methods.
- Scattered publication outlets, often unpublished progress reports.
- Uneven quality control of species identifications, which depend mainly on individual researchers' competence, since independent verification by taxonomic experts is costly and exceeds available expertise.

ERAPT was built to address these problems. It stores environmental requirements and pollution tolerance data in a standardized, hierarchical form that allows queries by taxonomic association, environmental parameter, or both. The system runs interactively on an IBM 370/3033 at the [[University of Notre Dame]]. Its data are encoded on tabular forms, digitized as X-Y coordinates, and standardized into a searchable database.

**Database scale:** The abstract reports 57,345 characteristics. The body text reports 57,660 parameter values, representing 402 genera and 1,694 species (the abstract gives 1,691 species). The values were derived from 883 data sources, mostly published literature, giving a mean of 34 environmental parameters, six sources per species, and four species per genus. Fish characterizations were compiled for this project. The other taxa were drawn from the EPA Environmental Monitoring and Support Laboratory in Cincinnati.

**Structure:** The system uses 21 heading categories divided into 303 specific parameters. Headings include stage, abundance, pollution tolerance, reproductive season, feeding behavior, hardness, salinity, nutrients, [[Dissolved Oxygen]], pH, temperature, turbidity, current, general habitat, specific habitat, bottom type, ecosystem regions, and political geography. The categories were adapted from a macroinvertebrate and diatom framework and expanded for fish and other organisms.

**Data handling:**
- Lower-level parameters roll up into all higher categories. For example, the salinity heading has 11 categories, with the Mesohalobous and Oligohalobous categories subdivided further.
- A [[Logical Sum]] summary includes every parameter reported by any source for a taxon.
- A [[Logical Product]] summary includes only parameters reported by all sources.
- Inconsistencies are found by taking the exclusive OR of the sum and product, and the number of sources is recorded for each taxon and category.
- Search statements can be saved, recalled, and transferred between organism groups with compatible data.

## Ecological & Environmental Context

The validation study used survey data from the Ohio Environmental Protection Agency for 64 sites on 20 rivers, streams, and tributaries. The sites were in three systems:

- [[Cross Creek]] and [[Yellow Creek]] (southeastern Ohio)
- [[Blanchard River]] (northwestern Ohio)
- [[Tuscarawas River]] (northwestern Ohio)

Each site had a fish species list with abundances and habitat descriptions covering dissolved oxygen, temperature, pH, turbidity, bottom type, and general and specific habitat. Current, degradable organics, and pollution data were available for only some sites.

The five numerically dominant species at each site accounted for at least half of all fish collected. They were treated as representative of local conditions. The ERAPT compare function identified the environmental characteristics shared by each fish community. These predictions were then compared with the habitat data recorded in the field. Agreement was scored when the two shared any common parameter. For example, a predicted "lake or large river" habitat agreed with an observed "large river" habitat.

## Key Findings

**Validation results (300 environmental characteristics compared):**

- **Overall agreement:** 285 of 300 characteristics agreed, a 95% successful prediction rate.
- **Agreement by river system:** Cross & Yellow Creek 95%, Blanchard River 97%, Tuscarawas River 93%.
- **Perfect agreement (100%)** for temperature, current, and degradable organics across all three systems.
- **Lower agreement by parameter:**
  - General habitat: 98%
  - Dissolved oxygen: 96%
  - Specific habitat and bottom type: 95%
  - pH and turbidity: 88%
- **Site discrepancies:** Only one site, site 1 on Yellow Creek, showed disagreement in more than one parameter type (specific habitat and bottom type).

The source notes that most disagreements were among very similar tolerance ranges or habitat types. The Ohio EPA staff judged most of them minor given the precision of the original measurements. The authors concluded that ERAPT predictions from dominant fish assemblages "closely approximated" the field survey data at all sites evaluated.

**Applications and future development:**

- **Regional indicator systems:** Regional assessment based on local fauna is described as particularly promising. Local or regional databases can be built within ERAPT's capabilities.
- **Microcomputer versions:** A prototype microcomputer version of the retrieval and analysis programs was under development for platforms such as the IBM PC and Apple Macintosh.
- **Data screening and quality control:** Inconsistent tolerances among organisms collected together at a site can flag errors in data collection or identification. Flagged cases can then be checked by taxonomic experts, which the authors present as a cost-effective way to assess biological data quality.
- **Source evaluation:** Data sources that frequently contradict other workers can be identified and removed.
- **Interfacing:** ERAPT can accept file input, so it could be linked to ongoing monitoring programs to detect probable environmental changes.
- **Broader use:** Because the programs are independent of the organisms and data types they process, the authors suggest applications to terrestrial or marine environments, microbes, higher vertebrates, and behavioral, physiological, or genetic data.

**Publication details:** The full report, "A Computerized System for the Evaluation of Aquatic Habitats Based on Environmental Requirements and Pollution Tolerance Associations of Resident Organisms," was authored by [[Clyde L. Dawson]] and [[Ronald A. Hellenthal]] of the University of Notre Dame, with Phil Larsen as EPA Project Officer at the Environmental Research Laboratory in Corvallis, Oregon. It is available from the [[National Technical Information Service]] in Springfield, Virginia. This document also includes a reference to the EPA Center for Environmental Research Information in Cincinnati.