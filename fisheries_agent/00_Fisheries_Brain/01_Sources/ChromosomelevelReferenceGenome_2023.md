---
species:
  - "Meda fulgida"
  - "Tiaroga cobitis"
common_name:
  - "Spikedace"
  - "Loach Minnow"
family: "Leuciscidae"
habitat: "Freshwater; desert-stream riffles and high-velocity microhabitats"
ocean_basin: "N/A"
location: "Aravaipa Creek, Graham County, Arizona; Gila River Basin (Arizona and New Mexico)"
tags:
  - ichthyology
  - genomics
  - conservation-genomics
  - leuciscidae
  - freshwater-fish
  - reference-genome
title: "Chromosome-level reference genomes of two imperiled desert fishes: spikedace (Meda fulgida) and loach minnow (Tiaroga cobitis)"
source_id: "X-ae8d7290"
source_citation: "N. M. Alexandre, A. C. Cameron, D. Tian, K. Chatla, S. R. R. Kolora, N. K. Whiteman, T. F. Turner, P. N. Reinthal (2023). Chromosome-level reference genomes of two imperiled desert fishes: spikedace (Meda fulgida) and loach minnow (Tiaroga cobitis). G3: Genes, Genomes, Genetics 13(10)."
doi: "10.1093/g3journal/jkad157"
source_file: "Chromosome-level_reference_genomes_of_two_imperile.pdf"
text_extraction: "text"
---
# Chromosome-level Reference Genomes of Spikedace and Loach Minnow

#ichthyology #marine-biology #leuciscidae

## Executive Summary

This genomics paper reports chromosome-scale reference genome assemblies for two endangered, co-distributed desert minnows, [[Spikedace]] (*Meda fulgida*) and [[Loach Minnow]] (*Tiaroga cobitis*), both endemic to the [[Gila River Basin]] in Arizona and New Mexico. The assemblies were built from [[Pacbio Sequel Ii]] long reads, Illumina short reads, and Dovetail Omni-C proximity-ligation data, then annotated with transcriptome evidence. The authors aim to fill a gap in genomic resources for [[Leuciscidae]], a family that is under-represented in reference assemblies despite its conservation concern. Comparative analyses against cyprinid genomes revealed structural rearrangements, expanded gene families, and genes showing episodic positive selection in both species.

## Background & Description

- **Taxonomy:** Spikedace and Loach Minnow are monotypic genera within Leuciscidae (Cypriniformes: Cyprinoidei). Loach Minnow belongs to Pogonichthyinae and Spikedace to Plagopterinae, and the two lineages are phylogenetically distant within Cypriniformes.
- **Distribution:** Both species have overlapping but restricted ranges and have been extirpated from more than 80% of their historic range (Propst 1999). Both are listed as endangered under the [[Endangered Species Act]].
- **Loach Minnow:** A benthic, obligate riffle species with large pectoral fins and a reduced swim bladder. It forages and spawns within the interstices of stream substrate in riffle microhabitat.
- **Spikedace:** Has a streamlined body and occupies a wider range of microhabitats than Loach Minnow, though it still shows affinity for higher water velocity.
- **Shared life history:** Both are small-bodied (maximum standard length 76 mm; >70 mm cited), short-lived (24 months or 36 months, depending on source), and sexually dimorphic, with male breeding coloration.
- **Sampling location:** Specimens were collected from upper [[Aravaipa Creek]] (UTM 12S 556711 3638121), Graham County, Arizona.
- **Reference comparison:** The zebrafish assembly ([[Zebrafish]], GRCz11) served as the model benchmark throughout.

## Ecological & Environmental Context

- **Habitat specialization:** Both species depend on high-velocity riffle habitats in arid-land streams. The authors link genomic signals to this ecology.
- **Water chemistry:** Expanded ion-binding gene families are discussed as potentially related to adaptation to higher conductivity, which is characteristic of arid-land streams (Griffith 2014).
- **Temperature and oxygen:** A gene related to low oxygen and high temperature in aquatic environments ([[Sod3A]]) was found in expanded families.
- **Desert adaptation:** Episodic positive selection is proposed as convergent adaptation to extreme desert environments, although the authors describe these links as hypotheses.
- **Threats:** Anthropogenic declines of native desert fishes have increased isolation, extirpation risk, and extinction risk (Meffe and Vrijenhoek 1988).
- **Conservation management:** Native Gila Basin fish conservation has focused on the least-disturbed habitats (Hickerson et al. 2022). The authors argue that per-population estimates of standing genetic diversity and inbreeding can further inform management and population-risk forecasts.

## Key Findings

### Biological Materials and Sequencing
- Single individuals of unknown age and sex were collected for the genome assemblies. Tissue was flash-frozen in the field and sent to Dovetail Genomics for Omni-C libraries.
- RNA-seq was performed on two Loach Minnow individuals (one male, one female) and three Spikedace individuals (two males, one female) for annotation.
- Spikedace PacBio data: 65 Gb from one cell on the [[Pacbio Sequel Ii]]; polymerase reads averaged 19 kb, polymerase N50 35.2 kb, subread N50 31.3 kb. An additional 10 Gb of paired-end data was generated on the NovaSeq 6000 for error correction.
- Loach Minnow PacBio data: 161 Gb across two cells. Polymerase N50 was 175 kb and 184 kb per cell; subread N50 was 14 kb and 16 kb.
- Both RNA-seq libraries were sequenced to ~37M reads on the NovaSeq 6000 S4.
- Expected genome size was 1–1.5 Gb, based on cyprinid C-values.

### Genome Assembly Quality

| Metric | Spikedace | Loach Minnow | Zebrafish (GRCz11) |
|---|---|---|---|
| Total length | 882,120,208 bp | 1,320,521,697 bp | 1,679,203,469 bp |
| Number of scaffolds/contigs | 83 | 550 | 1,923 |
| N50 | 34,805,954 bp | 48,679,909 bp | 52,186,027 bp |
| N75 | 32,365,017 bp | 42,382,842 bp | 42,172,926 bp |
| L50 / L75 | 11 / 18 | 13 / 20 | 14 / 23 |
| Largest contig | 52,739,976 bp | 67,399,795 bp | 78,093,715 bp |
| GC (%) | 39.33 | 40.28 | 36.60 |
| N's per 100 kbp | 8.14 | 3.02 | 279.51 |

- The abstract reports Spikedace as 882.1 Mb in 83 scaffolds, and Loach Minnow as 1.3 Gb in 550 scaffolds. Initial Spikedace Falcon Unzip assembly was 1.18 Gb before haplotig purging.
- Assembly contiguity for both species is slightly below zebrafish, which the authors attribute partly to smaller chromosome and genome sizes.
- Spikedace gap sequence totals ~70 kb (mean ~500 bp, minimum 50 bp). Loach Minnow gap sequence totals ~40 kb (mean ~100 bp, minimum 1 bp). Maximum gap size was similar (~1–1.4 kb).

### BUSCO Completeness (Actinopterygii database)

| Metric | Spikedace | Loach Minnow | Zebrafish |
|---|---|---|---|
| Complete | 96.90% (3529) | 97.70% (3556) | 95.90% (3494) |
| Single-copy | 95.60% (3481) | 94.50% (3441) | 78.50% (2859) |
| Duplicated | 1.30% (48) | 3.20% (115) | 17.40% (635) |
| Fragmented | 1% (35) | 0.90% (32) | 1.70% (61) |
| Missing | 2.10% (76) | 1.40% (52) | 2.40% (85) |

- Text summary: ~97% (Spikedace) and ~98% (Loach Minnow) complete BUSCOs, versus ~96% for zebrafish. Both new assemblies show fewer duplicated, fragmented, and missing BUSCOs than zebrafish.

### Contamination
- Bacterial contamination was low: found on 8 scaffolds, representing 0–0.006% of chromosome length, or up to 2% of unplaced scaffold length. It was softmasked.
- Mitochondrial contamination occurred only in the Loach Minnow Hifiasm assembly, on six scaffolds representing 40–90% of scaffold length. These were removed.
- No viral contamination was detected.

### Repeat Content
- Loach Minnow: ~48% of the genome masked.
- Spikedace: ~60% masked.
- In both, retroelements made up 13–15%, DNA transposons ~17–20%, rolling circles ~1–3%, and ~10–12% was unclassified.
- LTR/DIRS elements were the largest class in Spikedace. Simple repeats were the largest class in Loach Minnow (excluding unknown repeats).

### Gene Annotation

| Metric | Spikedace | Loach Minnow |
|---|---|---|
| Annotated genes | 38,671 | 37,413 |
| Mean gene length | 7,432.71 bp | 10,252.93 bp |
| Genome covered by genes | 32.58% | 29.04% |
| Total exons | 278,879 | 281,170 |
| Mean exons per mRNA | 7.25 | 7.01 |
| Mean introns per mRNA | 6.25 | 6.02 |
| Single-exon genes removed | 282 | 11,419 |

- Spikedace annotation used MAKER, AUGUSTUS, and SNAP, with RNA-seq hints and Swiss-Prot evidence. Only genes predicted by both SNAP and AUGUSTUS were retained.
- Loach Minnow annotation used BRAKER2 with an OrthoDB vertebrate protein set and RNA-seq. Single-exon genes were retained only if supported by InterProScan hits.

### Comparative Genomics: Synteny and Structural Variation
- Reference for comparison: [[Sunbleak]] (*Leucaspius delineatus*), chosen over [[Fathead Minnow]] because its genome is chromosome-level and may reveal rearrangements unique to North American cyprinids.
- Other taxa: [[Common Carp]], [[Goldfish]], and the zebrafish.
- Syntenic regions: 574.4 Mb (66.2%) of Spikedace; 655.2 Mb (54.4%) of Loach Minnow.
- Structural rearrangements: 62.4 Mb (7.2%) in Spikedace; 87.9 Mb (7.3%) in Loach Minnow.
  - Inversions: 57.2–75.6 Mb (114–123 events).
  - Translocations: 2.7–9.1 Mb (1,896–5,483 events).
  - Duplications: 2.5–3.2 Mb (1,962–2,243 events).
- Shared between the two species: 17.8 Mb of inversions, 90 kb of translocations, and 4.0 Mb of duplications. The authors suggest inversions may contribute to speciation, adaptation, or gene regulation.

### Gene Family Expansions
- Spikedace: no significantly enriched GO terms. Enriched protein domains in the two largest orthogroups included leucine-rich repeat N-terminal (SM00013; p = 0.0184), leucine-rich repeats subfamily (SM00369; p = 0.0184), Transposase (PF01498; p = 0.00021), and Homeodomain-like (PF13384; p = 0.00021).
- Loach Minnow: one gene family was enriched for GO terms and three protein domains, including serine-type endopeptidase inhibitor activity (GO:0004867; p = 2.77e-14), extracellular space (GO:0005615; p = 1.19e-06), A-macroglobulin receptor (SM01361; p = 1.17e-08), Alpha 2-macroglobulin family (SM01360; p = 2.78e-15), and Alpha 2-macroglobulin (SM01359; p = 2.78e-15).
- No functional enrichment was found in families expanded in both species.
- Expanded families in both species tended to associate with transposable elements, retrotransposons, and ion-binding orthologs in zebrafish.

### Positive Selection
- 1,465 genes were single-copy orthologs across all six assemblies.
- 371 of these showed evidence of episodic selection (p < 0.05) on the Spikedace or Loach Minnow branches, tested with [[Busted Selection Test]] in HyPhy.
- 11 Biological Process terms were enriched in StringDB, mostly related to cellular metabolic processes.
- Genes with reported associations were grouped as:
  - Oxidative stress (peroxisomes): p67phox, urate oxidase, ATM, PEX6p, SQSTM1, TRIM37.
  - Folate deficiency: MTHFD1, ABCC1, FOLR1, ALDH7A1, Lrp2.
  - Muscle development: tspan34, popdc2, top2a, tmod1.
  - DNA repair: XRCC3, XRCC1, FANCG, NTHL1, ATM.
- The authors suggest these may relate to the unique ecology of the two species. These associations are interpretive and were not directly tested.

### Data Availability and Funding
- Raw sequence data and genome FASTA files were deposited in GenBank under BioProject PRJNA947235.
- The GFF3 annotation file is hosted on the authors' GitHub repository.
- Specimens were collected under Arizona Game and Fish Department Permit SP406938, New Mexico Department of Game and Fish Permit 3015, and USFWS permits TE038055-0 and TE676811-11.
- Funding: Bureau of Land Management Cooperative Agreement Grant 140L6418P0085. Logistics were provided by The Nature Conservancy.