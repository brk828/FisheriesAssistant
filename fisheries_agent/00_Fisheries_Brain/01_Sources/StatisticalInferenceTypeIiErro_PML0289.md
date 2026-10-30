---
species:
  - Zapus hudsonius preblei
common_name: Preble's Meadow Jumping Mouse
family: N/A
habitat: N/A
ocean_basin: N/A
location: Colorado and Wyoming, USA; Klamath River (Oregon and California), USA; Grand Canyon, USA
tags:
  - conservation-biology
  - statistics
  - endangered-species-act
  - type-II-error
  - mammalogy
title: "Statistical inference, Type II error and decision making under the US Endangered Species Act"
source_id: "PML0289"
marsh_id: "PML0289"
library: "Marsh Library"
permission: "not public domain"
source_citation: "B. J. Brosi, E. G. Biber (2009). Statistical inference, Type II error and decision making under the US Endangered Species Act. Frontiers in Ecology and the Environment 7 (doi:10.1890/080203). Marsh Library ID: PML0289."
doi: "10.1890/080@3"
source_file: "Brosi B.J. et al. 2009. Frontiers in Ecoloy and the environment statistical interference, type 2 error, adn decision making under the US endangered species Act.pdf"
text_extraction: "mixed"
---
# Statistical Inference, Type II Errors, and Decision Making under the US Endangered Species Act

#mammalogy #conservation-biology #zapus-hudsonius-preblei

## Executive Summary

This review argues that conservation decisions are often based on the mistaken belief that "no statistically significant difference between two groups means the groups are the same." The authors illustrate the problem with the listing debate over the [[Preble's Meadow Jumping Mouse]], a federally endangered subspecies in the US. They show that a non-significant result from a [[Null Hypothesis Significance Testing]] framework cannot prove that populations are homogeneous, because the risk of a [[Type II Error]] is unknown. The commonly recommended fix, reporting post hoc [[Statistical Power]], is itself flawed, since observed power is necessarily low whenever no difference is found. The authors propose [[Equivalence Testing]] and [[Bayesian Statistics]] or likelihood methods as alternatives. They also argue that courts should require federal agencies to explain the risks of both Type I and Type II errors in litigated [[Endangered Species Act]] decisions.

## Background & Description

The [[Endangered Species Act]] (ESA) is the main US law protecting biodiversity. Its unit of protection includes species, subspecies and [[Distinct Population Segment]]s of vertebrates. Listing carries high stakes: it consumes limited conservation funds and triggers habitat protections that can restrict economic activity. Agencies increasingly rely on genetic differences to define protected taxa, so scientists' conclusions about genetic distinctiveness directly affect regulatory outcomes.

The authors identify two kinds of error:

- **Type I error (false positive):** protecting a "spurious" subspecies that is not biologically distinct, diverting resources from other taxa.
- **Type II error (false negative):** failing to protect a distinct taxon, which can lead to irreversible extinction.

Because extinction is irreversible and the ESA reflects the [[Precautionary Principle]], the authors argue that both error types deserve explicit attention.

The Preble's case study concerns a subspecies whose listing affected development in a rapidly growing region. A 2004 report by Ramey and colleagues compared genetic and morphometric data between the Preble's jumping mouse and more widespread subspecies, including *Z. h. campestris*. It found no statistically significant genetic differences and concluded that the mouse was not a unique taxon. A later study with more specimens and additional genetic sequence data, by King and colleagues, concluded that the Preble's mouse was indeed a separate subspecies. The authors note that the case also involved other disputes, including possible genetic contamination. They explicitly do not take sides in the controversy. They use it because many parties, including the study authors, US Fish and Wildlife Service (FWS) officials, interest groups, and most peer reviewers, made the same inferential error.

## Ecological & Environmental Context

The authors show that the inferential problem extends beyond this one case:

- **Klamath River, Oregon and California:** FWS required a statistically significant link between low water flows and endangered fish mortality before committing to increase flows. The authors note that a non-significant result would provide little or no information about whether such a correlation existed.
- **Grand Canyon:** FWS planned to reduce ESA protection for the [[Humpback Chub]] (*Gila cypha*) absent a statistically significant population decline. Again, a non-significant result would reveal little about whether the population was declining.

In applied contexts, the authors argue that the classical hypothesis-testing framework may be inappropriate for conservation questions. Decision makers are left with little information when results are non-significant, and major policy choices with irreversible risks may rest on unsound conclusions.

Sample size also plays a central role. With small samples, power is low and real differences are often missed. With very large samples, trivially small differences become statistically significant. The authors note that large samples are rarely available in ecological studies, and they recommend a priori power analyses to set appropriate sampling effort.

## Key Findings

**1. Non-significance does not mean equivalence.** A non-significant result supports only the statement that researchers "cannot reject the null hypothesis." It does not support "accept the null hypothesis as true." The authors note that a non-significant difference may be caused by low sample size rather than true homogeneity.

**2. Error rates are asymmetric in hypothesis testing.** When a test is significant at α = 0.05, the researcher can be at least 95% confident of a correct result. When it is not significant, there is no reliable way to estimate the probability of a Type II error.

**3. Post hoc power is uninformative.** Statisticians argue that observed power should not be used in data analysis. When P > 0.05, observed power is nearly always 0.5 or lower; at P = 0.05, observed power equals 0.5. Observed power therefore adds no information beyond the P value, though a priori power analysis remains useful for study planning.

**4. Equivalence testing offers a better alternative.** Equivalence testing reverses the conventional hypotheses by setting the null as a difference between groups and testing whether they are the same. This requires an explicit minimum difference (Δ) to be set. The authors state that, properly applied, equivalence testing reduces the risk of a Type II error to 5% or less. Setting Δ is subjective, but this subjectivity forces researchers to state their assumptions openly.

**5. Bayesian and likelihood methods are alternatives.** These frameworks avoid the hypothesis-testing paradigm and reduce some problems of [[Frequentist Statistics]]. The authors recommend Bayesian equivalence testing, and note that likelihood ratio tests can be adapted for likelihood-based equivalence testing. They acknowledge that many scientists and agency officials are reluctant to adopt these methods, so frequentist approaches will remain necessary for the foreseeable future.

**6. The error is widespread.** A review of papers from 2003 in *Conservation Biology* and *Biological Conservation* found that nearly two-thirds of manuscripts with non-significant results interpreted them as evidence of homogeneity (Fidler et al. 2006). Despite repeated warnings, the problem persists.

**7. Institutional incentives discourage attention to Type II errors.** In basic research, the scientific establishment emphasizes avoiding Type I errors to reduce spurious findings, while the costs of Type II errors fall mostly on progress. In applied regulation, Type II errors can lead to species loss, but protective restrictions impose concentrated, visible economic costs on small groups. Those groups have strong incentives to lobby agencies and Congress, creating systematic pressure against regulation.

**8. Courts could require explanation of both error types.** The authors propose that courts require agencies relying on quantitative statistics to explain uncertainty in both directions, including the risk of false negatives. Agencies that cannot do this clearly and accessibly would be required to reconsider. The authors cite precedent: a court struck down a National Oceanic and Atmospheric Administration (NOAA) decision to weaken "dolphin-safe" tuna labeling because the agency's sample sizes were too small to provide adequate power (*Earth Island Institute v. Hogarth*, Ninth Circuit, 2007). The authors stress that they do not ask courts to mandate specific statistical methods, only that agencies explain the risks of missing differences that could have led to a different policy. Where quantification is impossible, a clear qualitative assessment should be provided.

**9. Better inference brings the debate to values beyond genetics.** Setting a threshold of genetic difference for protection is inherently a value judgment. A very low threshold could yield many conservation units with economic and political costs. A high threshold risks losing genetic diversity, associated ecosystems, and cultural and aesthetic values, illustrated by species such as bald eagles, grizzly bears and gray wolves. The authors argue that the Preble's debate focused too narrowly on genetics.

**10. Recommendations for each group.**
- **Scientists:** Consider both Type I and Type II errors, avoid post hoc power, and use equivalence testing where appropriate. Communicate statistical risks to lawyers and courts, including through amicus briefs.
- **Editors and reviewers:** Scrutinize submissions for these inferential errors and encourage alternative techniques.
- **Educators:** Teach the limits of statistical analysis in this area.
- **Courts:** Require agencies to explain the risks of both error types.

**Conclusion.** The authors conclude that scientists bear the greatest responsibility for correcting interpretation errors. Better statistical inference would support more balanced and productive debate about conservation priorities. Relying only on Type I errors and significance levels lets policymakers and scientists avoid these difficult value-laden discussions, a choice the authors believe will ultimately harm biodiversity conservation.