---
species: N/A
common_name: N/A
family: N/A
habitat: Spatially variable (heterogeneous) environments, modeled as two discrete niches
ocean_basin: N/A
location: N/A
tags: [evolutionary-biology, quantitative-genetics, phenotypic-plasticity, theoretical-model]
title: "Genotype-environment interaction and the evolution of phenotypic plasticity"
source_id: "12095"
minckley_id: "12095"
source_citation: "S. Via and R. Lande (1985). Genotype-environment interaction and the evolution of phenotypic plasticity. Evolution 39(3): 505-522. Minckley Library ID: 12095."
source_file: "12095.pdf"
text_extraction: "ocr"
---
# Genotype-Environment Interaction and the Evolution of Phenotypic Plasticity

#evolutionary-biology #quantitative-genetics #population-genetics

## Executive Summary

This theoretical paper by [[Sara Via]] and [[Russell Lande]] (*Evolution* 39(3): 505–522, 1985; University of Chicago) uses [[Quantitative Genetics]] models to ask how the level of [[Phenotypic Plasticity]] of a polygenic trait evolves in spatially variable environments. The authors treat a trait expressed in two discrete environments as two genetically correlated "character states." Their central result is that the cross-environment [[Genetic Correlation]] controls both the trajectory and the speed of evolution toward the joint optimum. Unless the correlation is exactly +1, the polygenic variation is exhausted, or plasticity is costly, populations at equilibrium reach the optimum in each environment, though strongly positive or negative correlations can cause temporary maladaptation. The paper also shows that migration restriction can speed local adaptation, but that geographic variation in the norm of reaction is maintained at equilibrium only under special conditions.

## Background & Description

**Scope and framing.** The paper addresses the [[Norm of Reaction]], the profile of phenotypes a genotype produces across environments (Schmalhausen, 1949). Phenotypic plasticity is the extent to which the environment modifies the phenotype (Gause, 1947; Bradshaw, 1965). The authors note that most classical theory, beginning with [[Levene Multiple-Niche Model]] (1953), concerns when a single locus stays polymorphic in a multi-niche environment. Those one-locus models are poorly suited to quantitative traits for four stated reasons:

1. In two-allele one-locus models, the mean and genetic variance are statistically dependent, whereas in polygenic traits they can evolve independently (Slatkin, 1978).
2. Multiple-niche criteria rely on allele fitnesses, which cannot be measured for polygenic traits.
3. Dynamics of the mean phenotype and norm of reaction are not described by existing models.
4. In two-allele, two-niche models, the additive genetic correlation across environments is always −1.

**Genotype-environment interaction as genetic correlation.** Following [[Falconer 1952]], the authors treat a trait in each environment as a separate character state. Genotype-environment interaction then corresponds to a genetic correlation below +1. A correlation of +1 means identical genetic bases; values between +1 and −1 allow some independent evolution. Earlier polygenic models of spatial variation (e.g., Bulmer, 1971; Slatkin, 1978) assumed the cross-environment correlation was +1.

**Selection regimes.** The models follow [[Christiansen 1975]] in distinguishing:
- **Soft selection:** each niche contributes a constant fraction of the total population (populations regulated locally, e.g., by resource limitation).
- **Hard selection:** each niche's contribution is weighted by its mean fitness (global regulation, e.g., when populations are limited by evolving traits).

**Model structure.** Each individual experiences only one environment. Cross-environment genetic correlations must therefore be estimated from replicated genotypes or family members, using family-mean correlations or the re-expression of genotype-environment interaction as genetic covariance. Stabilizing selection depletes additive variance, so observed variance at equilibrium is presumed to be maintained by mutation-selection balance (Lande, 1976, 1980a; Turelli, 1984). Assumptions include weak selection, large populations, Gaussian phenotypic and fitness distributions, and an intermediate optimum. The authors note that major fitness components such as fecundity or survival are not well described by these Gaussian fitness assumptions.

## Ecological & Environmental Context

The models concern coarse-grained environments and discrete habitats. The authors state that they do not treat continuous variation such as temperature or photoperiod, but suggest the models may help interpret experiments run at discrete points along an environmental gradient.

Ecological examples motivate the work:
- **Herbivores on new host plants:** an herbivore invading an area with a new set of host plants may be poorly adapted to all of them.
- **Host-associated trade-offs:** genetically based trade-offs in growth or feeding behavior across host plants (estimable as cross-host genetic correlations) have been proposed as drivers of herbivore specialization (e.g., [[Rausher 1984]]; Futuyma, 1985).
- **Man-made disturbance:** recently created environments may contain populations that have not yet reached equilibrium (e.g., Snaydon, 1970; Antonovics, 1971).

Population subdivision and migration are central to the spatial analysis. Restricted migration can reduce the constraining effect of high cross-environment correlations and facilitate local adaptation (Maynard Smith, 1966; Felsenstein, 1981).

## Key Findings

**Panmictic populations (soft selection)**

- The cross-environment genetic correlation determines both the trajectory and the rate of evolution. Negative correlations slow evolution along the eigenvector of parallel change, while positive correlations slow movement along the eigenvector of divergent change.
- For a symmetric case (q = 0.5), eigenvalues are λ₁ = −G(1 + γ)/(ω² + P) for parallel change and λ₂ = −G(1 − γ)/(ω² + P) for opposing change, where γ is the genetic correlation. High or low γ produces a large discrepancy in time scales.
- When one environment is rare (q → 0), the smallest eigenvalue approaches λ ≈ −qG(1 − γ²)/(ω² + P), so approach to the joint optimum becomes extremely slow.
- Under soft selection with an initial asymmetry (Fig. 2A, C), correlations have little effect on the trajectory itself but do affect speed. Slowest approach occurs at extreme negative correlations for stabilizing selection and at high positive correlations under disruptive selection.
- When one environment is common (Fig. 3A, with 70% of individuals in environment 1), negative cross-environment covariance produces temporary maladaptation in the rare environment, because adaptation there waits until the common-environment optimum is approached.
- When the population is well adapted to one environment only (Fig. 3C), uncorrelated traits evolve most directly. High positive correlations cause overshoot in the initially well-adapted environment, while negative correlations cause maladaptive evolution in the opposite direction. High correlations of either sign slow approach to the joint optimum.

**Hard selection**

- Evolution under hard selection differs from soft selection. Here the joint fitness function is the arithmetic average of environment-specific fitnesses (W̄ = qW̄₁ + (1 − q)W̄₂), so the adaptive topography is no longer bivariate normal (Fig. 1B).
- Even a slight asymmetry in initial position, variances, selection parameters, or niche frequencies makes the niche with the highest initial mean fitness contribute increasing numbers of individuals until its own optimum is nearly reached. Evolution in the less-fit environment is then dominated by correlated response.
- Adaptation occurs first in the most abundant environment and later in rare ones (Fig. 3B). Mean fitness in one environment can temporarily decrease, most often in the rare environment or where fitness is initially lowest.
- Linearized eigenvalues apply only near the optimum. Numerical iterations show rates close to those under soft selection.

**Joint optimum and equilibrium**

- Unless the cross-environment correlation is +1, polygenic variation is exhausted, or plasticity is costly, populations eventually reach the optimum phenotype in each environment at equilibrium. Mean fitness increases monotonically in the joint sense, with temporary local declines possible.
- Genetic variation in quantitative characters is not maintained by environmental heterogeneity once the joint optimum is reached. Remaining variance around the equilibrium norm of reaction is produced by mutation.

**Subdivided populations**

- Migration restriction can facilitate local adaptation by weakening the constraining effects of high genetic correlations. If migration is much stronger than selection (m ≫ G/(ω² + P)), geographic variation in breeding values is removed on a time scale of about 1/m generations. If selection is stronger, geographic variation decreases over about 2/[(1 + γ)m] generations, and phenotypes approach their optima on a time scale of (ω² + P)/G generations.
- At equilibrium, populations in different environments converge to the same vector of mean breeding values (z̄₁₂ = z̄₂₁ and z̄₁₁ = z̄₂₂), even though the expressed phenotypes differ. A reciprocal transplant would therefore reveal no geographic variation in breeding values.
- Three conditions prevent this convergence: no migration (m = 0), exhausted genetic variance in one character state, or a cross-environment correlation of +1. A cost to plasticity may also leave the equilibrium away from the optimum.

**Circumstances that prevent reaching the joint optimum**

The authors list five:
1. A correlation of +1 makes **G** singular, so no genetic variation exists in one principal direction, and small perturbations cause permanent displacement.
2. Negative correlations among many traits can halt response. An average correlation of −1/(n − 1) among n simultaneously selected characters can stop evolution (Dickerson, 1955), which may limit the number of environments a population can adapt to at once.
3. Exhausted genetic variation in one character state prevents evolution in that direction, a "developmental constraint."
4. With no gene flow, populations in different environments never converge, because unexpressed states are not subject to selection in a given environment. Limited migration may also lead to reproductive isolation before the joint optimum is reached.
5. A cost to plasticity makes expressed states more similar, producing an equilibrium between the joint optimum and the point where the expressed means coincide (Via, unpubl.).

**Implications for empirical work**

- Observed differences among populations in different environments may reflect an unfinished evolutionary trajectory rather than different optima. The frequency of these cases relative to equilibrium remains an empirical question.
- Estimating directional selection and the joint optimum, together with genetic variance, a cross-environment correlation between −1 and +1, and non-zero migration, can show whether a population has reached equilibrium. If it has not, evolution of the norm of reaction is still in progress.
- Because breeding-value vectors are expected to be equal at equilibrium, differences in those vectors among populations are not a criterion for adaptation. Significantly different mean vectors in reciprocal tests would instead indicate that further evolution is expected, unless gene flow is absent or the genetic covariance matrix is singular.
- Estimates of stabilizing selection (Lande and Arnold, 1983) can test whether the phenotypic mean sits at the optimum in each environment.

**Scan note.** The final page of the scan includes the truncated opening of an unrelated abstract from the same journal issue, on [[Darwin's Finches]] (Geospizinae) and natural selection on body size and beak morphology. It is not summarized here because the text is incomplete.