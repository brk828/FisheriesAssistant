---
species: N/A
common_name: N/A
family: N/A
habitat: River (illustrative Stella example only)
ocean_basin: N/A
location: N/A
tags: [simulation-modeling, system-dynamics, educational-technology, computer-modeling]
title: "Stella, a simulation construction kit: Cognitive process and educational implications"
source_id: "14749"
minckley_id: "14749"
source_citation: "M. Steed (1992). Stella, a simulation construction kit: Cognitive process and educational implications. Journal of Computers in Mathematics and Science Teaching 11: 39-52. Minckley Library ID: 14749."
source_file: "14749.pdf"
text_extraction: "ocr"
---
# Stella: A Simulation Construction Kit and Its Cognitive and Educational Implications

#simulation-modeling #system-dynamics #educational-technology

## Executive Summary

This document is a 1992 journal essay by Marlo Steed on **Stella**, a graphical simulation construction kit for building continuous, system-dynamics models. It is not a fish, ecological, or field study. Its only aquatic element is an illustrative river-pollution model (a "NoBug" concentration from periodic river dumps, with decomposition) used to demonstrate the software's equations and output. The essay argues that building and testing models in Stella makes assumptions explicit, encourages causal thinking about feedback loops, and supports deeper understanding, while cautioning about oversimplification, correlation mistaken for causation, and over-reliance on models.

## Background & Description

- **Software lineage:** Stella is described as a graphical interface on the Dynamo language, which [[Jay Forrester]] developed at MIT. It uses simultaneous differential equations. The essay also names [[Extend]] as a related package that lets users create their own icons.
- **Core building blocks:**
  - **Stocks (levels):** accumulations that build up over time, usually the key actors in a simulation.
  - **Flows (rates):** control incoming and outgoing material. Flows that are not tied to a stock are sent to "clouds," meaning an unspecified source or sink.
  - **Converters:** generate outside influences, calculate ratios, and hold graphical relationships.
  - **Connectors:** show the direction of relationships.
- **Tools:** a hand (select and move), a ghost (duplicate icons), and a stick of dynamite (break connections).
- **Built-in functions:** testing functions (Pulse, Ramp, Step), mathematical, trigonometric, and logical functions, and special functions (Delay, Smooth, Trend, and others).
- **Interface:** follows the Macintosh model with pull-down menus, drag-and-drop icons, animated stock levels, and a table of values over time.
- **Core equation example:** New Level = Old Level + dt × (InRate − OutRate).
- **Conceptual framing:** the essay separates a *model* (a representation of structures) from a *simulation* (the process of interaction that produces behavior). It contrasts discrete tools such as [[Spreadsheet]] applications with continuous, system-dynamics simulation.

## Ecological & Environmental Context

The essay has no ecological field data, species, or habitat studies. Its environmental content is limited to a worked example, which should be read as a teaching illustration rather than a real-world assessment:

- **River dump scenario:** a "NoBug" (pesticide-like) substance is released into a river every 5 days (Days_between_Dumps = 5). Decomposition takes 5 days (Days_to_Decompose = 5). The starting amount is 450 (Amount_of_NoBug = 450).
- **Decomposition logic:** decomposition flow is conditional on the concentration being above zero, and the decomposition fraction is the amount divided by the decomposition time.
- **Outputs:** the model produces time-series graphs and tables of concentration and decomposition flow. The essay gives no interpretation of those results in ecological terms.
- **Scope:** no organisms, water chemistry measurements, or regulatory standards are discussed.

## Key Findings

1. **Structure drives behavior.** The essay argues that system behavior comes from internal structure (feedback loops), and that external shocks only reveal latent patterns. Its Slinky analogy illustrates this.
2. **Feedback loops:** positive loops produce runaway growth or collapse, negative loops drive equilibrium, and balanced loops produce no change. Shifts in loop dominance generate much of a system's dynamics, and computer simulation is needed to observe them.
3. **Quantifying qualitative variables:** the authors argue that qualitative factors (the example is fear on an arbitrary 0–1 scale) can be quantified rigorously without claiming measurement accuracy. The key requirement is internal consistency among variables.
4. **Elegant simplification:** citing Einstein ("as simple as possible but not simpler"), the essay advises including only the factors that matter, since the appropriate level of detail depends on the situation.
5. **Limitations and risks:**
   - Chaos-like sensitivity to small changes (citing [[Gleick]]).
   - Compensating loops can hide causal factors.
   - Correlation is not causation, and students may over-simplify causal claims.
   - Models should be "taken seriously but not literally" (citing [[Ost]] 1987).
   - The time cost of model building must be weighed against the insight gained.
6. **Educational benefits:** the essay claims Stella supports prediction, hypothesis testing, analytical reasoning, explanation, metacognition, and higher-order skills in [[Bloom'S Taxonomy]]. It also argues that models make mental models explicit and reveal ambiguity in textbook language.
7. **Six classroom levels of use** are proposed, ranging from predefined templates with hidden relationships, through discovery labs, building models from scratch, class demonstrations, and translating textbook concepts, to students constructing and testing their own theories.
8. **Conclusion:** the central value lies in the modeling process itself, which the author describes as "disciplined thinking." Good science begins with good questions, and model building parallels the learner's construction of understanding.