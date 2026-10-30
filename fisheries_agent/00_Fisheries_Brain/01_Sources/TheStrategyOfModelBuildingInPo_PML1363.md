---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Puerto Rico (Drosophila niche breadth data)
tags: [population-biology, theoretical-ecology, model-building, niche-breadth, drosophila]
title: "The Strategy of Model Building in Population Biology"
source_id: "PML1363"
marsh_id: "PML1363"
library: "Marsh Library"
permission: "not public domain"
source_citation: "R. Levins (1966). The Strategy of Model Building in Population Biology. American Scientist, 54(4), 421-431. Marsh Library ID: PML1363."
source_file: "Levins R. 1966. The strategy of model building in population biology.pdf"
text_extraction: "mixed"
---
# Strategy of Model Building in Population Biology

#population-biology #theoretical-ecology #drosophila

## Executive Summary

This is a theoretical essay on how to build mathematical models in [[Population Biology]]. It argues that the field arose from the merger of [[Population Genetics]], [[Population Ecology]], and [[Mathematical Biogeography]], which treat time, genetics, and environment differently. The author contends that a faithful, one-to-one model of a multispecies, evolving, heterogeneous system is neither measurable nor solvable, so models must simplify. Simplifications should be chosen to yield **robust theorems**, results that hold across several models with different assumptions. The essay gives two examples: a robust theorem on the evolution of broad niches under environmental uncertainty, and a non-robust theorem linking intrinsic growth rate to population size. It also introduces **sufficient parameters**, such as niche breadth and uncertainty, and presents a small dataset on niche breadth in Puerto Rican [[Drosophila]] populations.

## Background & Description

The essay opens by noting that [[Population Biology]] combines three bodies of theory. Population genetics specifies populations by genotype frequencies, assumes a constant environment, and treats one population or species at a time. Population ecology tracks multispecies systems, age distributions, physiological states, and densities, but treats species as genetically homogeneous and ignores evolution. The author argues that ecological and evolutionary timescales are commensurate, so both must be handled together.

Three difficulties block a full model. First, there are too many parameters, some unmeasurable within a lifetime. Second, the equations (possibly about 100 simultaneous partial differential equations with time lags) are analytically insoluble and exceed computing capacity. Third, even a solution would be expressed as quotients of sums of products of parameters with no clear meaning.

The author cites the classical founders, [[Haldane]], [[Fisher]], and [[Wright]], who assumed a constant environment, and argues that this was legitimate for their question (whether weak natural selection could drive evolution). Today, environmental heterogeneity is considered essential, so the legitimacy of a simplification depends on both the biology and the state of the science.

The essay describes three strategies for simplifying:

1. **Sacrifice generality to realism and precision.** Used by [[Holling]] and fishery biologists, and by [[Watt]]. Parameters are limited to the short-term behavior of a particular organism, and precise, testable predictions are produced for specific situations.
2. **Sacrifice realism to generality and precision.** Used by [[Kerner]] and [[Leigh]], and by most physicists entering the field. These general equations (such as Volterra predator-prey systems without time lags) are explicitly unrealistic. The hope is that unrealistic assumptions cancel and that deviations from nature indicate where complexity should be added.
3. **Sacrifice precision to realism and generality.** Favored by [[MacArthur]] and the author. Models are often graphical and assume only that functions increase or decrease, or are convex or concave. Predictions take the form of inequalities, for example between tropical and temperate species, insular and continental faunas, or patchy and uniform environments.

The author also addresses the risk of error in flexible models. Because every model has artificial assumptions, it is often unclear whether a result depends on the model's essentials or on its simplifying details. Using the analogy of a geographic map, the essay notes that in mathematical biology "it is not always obvious when we are using too high a magnification."

## Ecological & Environmental Context

The central ecological concept is environmental heterogeneity in two forms:

- **Fine-grained (spatial) heterogeneity:** each individual experiences many units of both environment types in proportion. The rate of increase is the average fitness, pW₁ + (1 − p)W₂.
- **Coarse-grained (temporal) heterogeneity:** each individual lives in one environment during its relevant life, or fitness varies across generations. The rate of increase is a product, W₁^p·W₂^(1−p).

The essay argues that the first type produces average effects and the second produces alternatives and therefore uncertainty.

Other ecological factors discussed include temporal variation, patchiness of the environment, habitat productivity, mode of hunting, habitat selection, niche breadth, and food-getting procedures. The author states that these all converge on the same theorem: environmental uncertainty favors broader niches, while certain but diverse environments favor specialization.

## Key Findings

**Robust theorem: uncertain environments favor broad niches and polymorphism.** This result was tested with three independent models:

- **Model I (fitness set, Levins 1962):** Each phenotype has a best environment, and fitness declines with deviation from it. With two environments, the fitness set is convex when the environments are similar relative to phenotype tolerance and concave when they diverge.
  - On a convex fitness set, populations are monomorphic and intermediately adapted.
  - On a concave fitness set, spatial diversity causes specialization on the more common habitat, while temporal diversity causes polymorphism.
- **Model II (calculus of variation):** The area under the fitness curve is fixed. Maximizing growth gives an optimum fitness equal to log(C) minus the uncertainty of the environment. More variable environments produce flatter curves and broader niches. Polymorphism becomes optimal when the environment distribution is broader than the maximum breadth achievable by any single phenotype.
- **Model III (one-locus, two-allele genetic model, Levins and MacArthur 1966):** Genotype fitness points are restricted by segregation to a curve bending toward the heterozygote. Selection in fine-grained environments maximizes average fitness and requires heterozygote superiority for polymorphism. In coarse-grained environments, sufficient heterogeneity broadens the niche. As the two environments become similar, the optimum tends to a single genotype.

The author notes that the models differ in assumptions (discrete vs. continuous environments; linked vs. independent fitness contributions), but their agreement on the main result is what makes it robust. The author also stresses that the models predict only that populations differ in the direction of their optima, not that evolution will reach the optimum.

**Non-robust theorem: high intrinsic growth rate yields smaller average population.** This result follows from the logistic equation dN/dt = rN(K − N)/K. Leigh (1965) showed that it also holds for a Volterra system without a saturation level. The essay argues that both results share one explanation: high r speeds the approach to K from below and also speeds the crash from above, an assumption not built into the definition of r. Adding a term for extraneous predation can reverse the result. The author concludes that the theorem is fragile and "cannot be asserted as a biological fact."

**Sufficient parameters.** Many lower-level variables can be reduced to a small set of higher-level parameters. Examples include additive genetic variance and total genetic variance, which summarize physiological gene interactions in population genetics. Kerner's conservation law for predator-prey systems and Goodwin's (1963) invariant in cellular metabolism, which he called a biological "temperature," are also cited. Niche breadth is a sufficient parameter for the spread of fitness across environments. Uncertainty emerges as a sufficient parameter as well, but it is a many-to-one mapping. From a given uncertainty value, one cannot tell whether the cause was temporal variation, patchiness, or low productivity, so information is lost.

**Niche breadth measures.** The author proposes two candidate measures, where p is the proportion of a species in each collection:

- Log B = −Σ p log p (method I)
- 1/B = Σ p² (method II)

The measures should give N for a species using N resources equally, lie between 1 and 2 for two resources used unequally, and never exceed the sum of breadths when populations merge. The author says neither is uniquely "true," and recommends reporting both.

**Puerto Rican Drosophila data (Table 1).** Seasonal niche breadth from 21 collections (maximum possible breadth 21) in 1962 is given for 10 entries. Selected values (method I / method II):

| Species | Method I | Method II |
|---|---|---|
| D. melanogaster | 14.4 | 10.5 |
| D. [garbled name in OCR, "Litifasciaeformis"] | 15.5 | 15.7 |
| D. dunni | 11.0 | 7.6 |
| D. tristriata | 6.9 | 5.7 |
| D. ananassae | 11.2 | 8.6 |
| D. repleta | 9.0 | 4.2 |
| D. nebulosa | 6.5 | 6.2 |
| D. paramediostriata | 11.2 | 7.9 |
| X4 (tripunctata group) | 7.2 | 6.0 |
| X6 (tripunctata group) | 13.9 | 12.0 |

**Three sources of imprecision in general models.** The author identifies:

1. Omitting factors with small effects, or large effects that occur rarely.
2. Vagueness about exact functional forms, used to emphasize qualitative properties.
3. The many-to-one property of sufficient parameters, which destroys information about lower-level events.

General models are therefore "necessary but not sufficient" for understanding nature. Understanding requires linking the general to the particular.

**Clusters of models.** A model is neither a hypothesis nor a theory and cannot be verified directly. Its value lies in generating good, testable hypotheses. Models are organized into clusters: alternative models for the same system can yield robust theorems, complementary models describe different aspects of one problem, and hierarchical nested models connect levels of organization. The essay ends with the view that conflicts between "realist" and "generalist" schools are mainly about method, not nature, and that methods should be judged by how well they help understand the real world.