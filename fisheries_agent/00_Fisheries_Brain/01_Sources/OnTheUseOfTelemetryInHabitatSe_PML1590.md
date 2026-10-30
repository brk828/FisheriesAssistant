---
species: N/A
common_name: N/A
family: N/A
habitat: Terrestrial and general animal habitats (home ranges, homogeneous and heterogeneous environments)
ocean_basin: N/A
location: N/A
tags: [telemetry, habitat-selection, gps-tracking, autocorrelation, movement-ecology, wildlife-management]
title: "On the Use of Telemetry in Habitat Selection Studies"
source_id: "PML1590"
marsh_id: "PML1590"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. Martin, V. Tolon, B. Van Moorter, M. Basille, C. Calenge (2008). On the Use of Telemetry in Habitat Selection Studies. Marsh Library ID: PML1590."
source_file: "Martin J. et al. 2008. On the use of telemetry in habitat selection studies.pdf"
text_extraction: "text"
---
# On the Use of Telemetry in Habitat Selection Studies

#ichthyology #marine-biology #telemetry

*Note: this is a methodological review of wildlife telemetry; it is not a fish study. The tag line above is retained as required by the template, but the document concerns terrestrial and general vertebrate movement ecology.*

## Executive Summary

This methodological chapter by Martin, Tolon, Van Moorter and colleagues argues that habitat selection should be studied as a dynamic process linked to individual movement rather than as a static description of space occupancy. The authors contend that [[Gps Telemetry]] has made high-frequency relocation data available, which introduces serial autocorrelation that classic [[Habitat Selection Analysis]] methods assume away. They review how autocorrelation has been treated (first as a problem, then as a feature to model), outline movement-based null models such as the [[Correlated Random Walk]] and [[Mixture of Random Walks]], and compare [[Vhf Telemetry]] with GPS in terms of biological question, scale, and cost. The central recommendation is that the biological question, not the technology's data volume, should determine the sampling protocol and tool.

## Background & Description

- **Subject:** Use of telemetry data in habitat selection studies, with emphasis on autocorrelation and movement analysis.
- **Organisms cited:** Examples include brown bears (*Ursus arctos*), woodland caribou (*Rangifer tarandus*), elk (*Cervus elaphus*), moose, bees, albatrosses, wolves, cougars, and red deer. No fish are discussed.
- **Conceptual framework:** Habitat selection is scale-dependent. [[Johnson'S Orders Of Selection]] (1980) distinguishes four levels, from species' geographic range down to food items. Higher levels are governed mainly by population processes; lower levels by individual choices.
- **Technology history:** [[Vhf Telemetry]] appeared in the early 1960s and allowed remote location by homing or triangulation, but required heavy field effort and typically yielded short tracking durations (e.g., one location every 10 minutes for a couple of days). GPS was introduced in the early 1990s and became general around 2000. It allows fix intervals down to one second and long deployments (e.g., one location every 3 hours for a whole year), with accuracy of around 20 m.
- **Key definitions:** Habitat selection is the process by which an animal actually chooses habitat components. Tests compare used locations with "available" locations under a null model of random use. Availability depends on the selection order: population-level for second-order and individual-level for third-order selection.

## Ecological & Environmental Context

- **Autocorrelation problem:** Successive GPS fixes are not independent. Positive autocorrelation underestimates variance, inflating Type I error, so random habitat use is rejected too often. Classic logistic and log-linear models assume independence.
- **Time to Independence (TTI):** [[Swihart And Slade Test]] (1985) uses Schoener's ratio statistic to estimate the smallest time lag at which fixes are statistically independent. Subsampling to the TTI is a common workaround, but it discards expensive data and fails when no stable home range exists.
- **Biological versus statistical independence:** Even at the TTI, animals are not free to move everywhere in their home range at all times because of resting, foraging, and movement constraints.
- **Nonstationarity:** Animal trajectories often change statistical properties with behavioral state (for example, foraging versus transit). This nonstationarity is a major cause of autocorrelation and carries information about behavior.
- **Behavioral state partitioning:** Methods include [[First Passage Time]] (Fauchald and Tveraa, 2003), fractal dimension, and [[State-Space Models]] based on hidden Markov models.
- **Attractive sinks:** Habitats can be selected despite poor performance (Delibes et al., 2001). Detecting them requires performance measures such as lifetime reproductive success, which need long-term, large-scale data rather than fine-scale movement.
- **Cost structure:** GPS devices cost roughly 10 times more per animal than VHF devices, but GPS data collection is automated, reducing operation costs, especially at high fix frequencies.

## Key Findings

1. **Autocorrelation must be modeled, not removed.** The authors recommend integrating autocorrelation into statistical frameworks and moving from static to dynamic habitat selection analysis.
2. **Brown bear case study (Martin et al., 2008).** Two null models gave opposite conclusions. A classic null (random points in the home range) showed strong selection by marginality. A null that preserved trajectory shape showed no selection. Neither approach captured the true autocorrelation structure, so the second is considered overly conservative and the first is invalid.
3. **Discrete-choice and step selection models are a partial step.** [[Step Selection Function]] (Fortin et al., 2005) and related [[Discrete Choice Models]] define availability for each relocation, but consider only first-order autocorrelation and ignore behavioral state.
4. **Recommended approach.** Partition trajectories into homogeneous movement bouts, estimate movement descriptor distributions (step length, turning angle) for each state, and use these to build more realistic null models that include behavioral constraints.
5. **Sampling trade-off (Figure 5).** At fixed cost, [[Vhf Telemetry]] favors many individuals with few relocations (little autocorrelation), whereas [[Gps Telemetry]] favors fewer individuals with many relocations (strong autocorrelation).
6. **Girard et al. (2006) on moose.** Accurate habitat selection was obtained with only 1 to 7 fixes per week, whereas more than 15 individuals were often needed to generalize across the population. For generalist species with high inter-individual variability, more animals matter more than more fixes.
7. **Scale matching.** Small-scale movement questions need high fix frequency (e.g., one point per second for albatross fractal analysis, Fritz et al., 2003). Large-scale distribution questions can use low frequency (e.g., one point every 3 weeks in Mcloughlin et al., 2005).
8. **Choice of tool.** GPS can replicate any VHF protocol, but not the reverse over long periods. The authors recommend VHF plus direct observation for studies linking habitat selection with long-term performance, and GPS for dynamic, fine-scale studies. GPS is also useful for estimating kill sites of large predators (cougar, wolf).
9. **Central warning.** The authors caution that the appeal of GPS data (precision, frequency, automation) often drives data-driven sampling rather than biological questions. This can cause scale mismatches and "data-dredging," so the biological question must come first.
10. **Overall conclusion.** GPS offers new insight into fine-scale, dynamic habitat selection, and the field should shift from static patterns toward dynamic processes, with [[Time Series Analysis]] and state-space methods expected to grow in use.