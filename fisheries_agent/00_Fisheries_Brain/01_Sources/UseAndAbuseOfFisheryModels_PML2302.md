---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: [fisheries-science, stock-assessment, fishery-models, uncertainty, fishmetic]
title: "Use and abuse of fishery models"
source_id: "PML2302"
marsh_id: "PML2302"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. T. Schnute, L. J. Richards (2001). Use and abuse of fishery models. Canadian Journal of Fisheries and Aquatic Sciences, 58: 10-17. Marsh Library ID: PML2302."
source_file: "Schnute J.T. et al. 2001. Use and abuse of fishery models.pdf"
text_extraction: "text"
---
# Use and Abuse of Fishery Models

#ichthyology #marine-biology #fisheries-management

## Executive Summary

Schnute and Richards (2001), published in the *Canadian Journal of Fisheries and Aquatic Sciences* (Vol. 58, Invited Perspectives issue), examine why mathematical models used in [[Fish Stock Assessment]] have failed to prevent stock collapses. The authors argue that models begin with simple accounting arithmetic but must be converted into "fishmetic," a term they coin for the uncertainty introduced by process error, measurement error and model uncertainty. Because unknown states far outnumber observations, models require arbitrary structural assumptions. The paper recommends skepticism, broader knowledge bases, common sense, and robust management strategies, and draws analogies from literature, physics, and finance.

## Background & Description

- **Authors:** Jon T. Schnute and Laura J. Richards, Fisheries and Oceans Canada, Pacific Biological Station, Nanaimo, BC.
- **Publication:** Received January 24, 2000; accepted July 13, 2000; published online September 19, 2000. Cited as Can. J. Fish. Aquat. Sci. 58: 10–17 (2001).
- **Format:** Invited perspective (100th Anniversary Issue) presenting a conceptual and critical review, with no original data set. Includes a French résumé.
- **Core framework:** Fish population change is treated as bookkeeping of debits (mortality), credits (recruitment) and interest (growth), analogous to a bank account transaction log.
- **Key concepts:**
  - **Fishmetic:** the gap between exact arithmetic and practical fishery models, comprising process error, measurement error and model uncertainty.
  - **State space models:** a framework in which hidden states (e.g., abundance) are inferred from observed quantities (e.g., catch, indices, age proportions) via [[Statistical Inference]].
  - **Tolstoy's locomotive and Holmes's "Silver Blaze":** literary analogies used to illustrate competing explanations and the logic of inference.

## Ecological & Environmental Context

The paper addresses populations that are poorly understood and subject to fishing, environmental change and species interactions. The authors frame the three standard explanations for stock collapse as:

1. The fishery destroyed the stock.
2. The environment changed so the stock could not survive.
3. The fish moved to a place where they could not be captured.

Most conventional models address only explanation 1, because their bookkeeping accounts for catch removals. The authors note that environmental regulation, spatial structure, fish movement and [[Multispecies Interactions]] are poorly represented. They also cite [[Wilson 1998 Consilience]] on the complexity of ecological systems and on the emergence of chaotic dynamics in multispecies settings (Wilson et al. 1994). Comparison with [[Physics Modeling]] shows that physical laws (e.g., gravitational constant G) apply universally, whereas biological parameters vary substantially among species, with age and time.

## Key Findings

**Why models fail**

- Models begin with arithmetic but must be qualified by three elements of fishmetic: process error, measurement error and model uncertainty.
- Process and measurement error can be represented through probability distributions. Model uncertainty cannot be quantified and may invalidate the analysis entirely if the underlying arithmetic is wrong.
- Models are typically **underdetermined**: unknowns exceed observations. Statistical theory applies only when observations greatly exceed unknowns.
- Worked example: a fishery operating 20 years on a population with 10 age-classes yields 200 catch observations but depends on 400 unknowns (200 biomass states and 200 fishing mortalities). Two constraints reduce the independent fishing mortality states to 20 (one per year), and biomass dependencies from biological processes reduce the rest.
- These structural assumptions are necessary yet arbitrary, and different choices can strongly change results.
- The Schnute–Richards paper also notes that the same model can be tailored to support any desired explanation for a collapse.

**Four broad remedies**

1. **Maintain skepticism:** Consider a suite of alternative models, use thought experiments, and recognize limitations openly.
2. **Expand the knowledge base:** Use [[Meta-Analysis]] across similar populations, incorporate oceanographic and climate data, fisher knowledge, and [[Shared Data Frameworks]] spanning long time series (analogous to tree-ring and ice-core records).
3. **Apply common sense:** Begin with exploratory data analysis and simple model structures, add complexity only when justified, and maintain quality control (residual analysis, diagnostics, code verification, team diversity). Modelers should avoid losing sight of central issues in complex code.
4. **Implement robust strategies:** Favour control of fishing mortality (e.g., spatial and temporal closures, as in [[Walters and Parma 1996]]) over direct catch control, because it performs better under uncertainty. Evaluate decision rules (model-based versus data-based) through [[Management Strategy Simulation]].

**Policy implications**

- International agreements, including the [[UN Straddling Fish Stocks Agreement]] and the [[FAO Code of Conduct]], require harvest strategies based on reference points and predefined decision rules.
- The authors caution that reference points tied to one version of the bookkeeping may be misguided or deceptive if the model is wrong. Unlike building codes, fishery standards cannot be set as precisely as physical engineering standards.

**Analogies and conclusions**

- [[Gödel's Incompleteness Theorem]] is invoked as a parallel: just as mathematics contains undecidable propositions, fishery models cannot give a unique description of events without ad hoc assumptions.
- Fish stocks and financial stocks share analogous dynamics, risk, and expert debate. Financial markets have daily prices with little measurement error, whereas fishery abundance indices often contain high measurement error and span longer intervals.
- The paper emphasizes that models are best used as tools for thought rather than prescriptive black boxes. Integrating stakeholder information builds acceptance, and the authors conclude that fishery models offer valuable insight but must not be trusted completely.