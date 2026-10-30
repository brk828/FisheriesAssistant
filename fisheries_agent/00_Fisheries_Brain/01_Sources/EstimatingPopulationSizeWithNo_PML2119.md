---
species: "Nyctalus noctula (allele source only; simulated population is generic)"
common_name: "Noctule bat (allele data source); simulated populations"
family: "N/A"
habitat: "N/A"
ocean_basin: "N/A"
location: "N/A (allele frequencies drawn from 13 studied noctule bat populations)"
tags: [chiroptera, population-ecology, noninvasive-sampling, capture-mark-recapture, simulation]
title: "Estimating Population Size with Noninvasive Capture-Mark-Recapture Data"
source_id: "PML2119"
marsh_id: "PML2119"
library: "Marsh Library"
permission: "not public domain"
source_citation: "E. Petit, N. Valiere (2006). Estimating Population Size with Noninvasive Capture-Mark-Recapture Data. Conservation Biology 20(4). Marsh Library ID: PML2119."
source_file: "Petit E. et al. 2005. Estimating population size with noninvasive capture mark reacpture data.pdf"
text_extraction: "text"
---
# Estimating Population Size with Noninvasive Capture-Mark-Recapture Data

#chiroptera #population-ecology #conservation-biology

## Executive Summary

This simulation study asks whether population size can be estimated reliably from noninvasively collected genetic samples (hair, feces) taken in a **single sampling session**, instead of the multiple sessions required by [[Capture-Mark-Recapture]] (CMR). Using the [[GEMINI Software]] to simulate a full [[Noninvasive Genetic Sampling]] survey with multilocus genotypes, the authors compared six estimation methods across four sampling-effort levels. The main conclusion is that single-session estimates can be as reliable as multisession estimates, and that a [[Bayesian Estimator]] performs best. The study also finds that residual [[Genotyping Error]] introduces only a marginal bias. The work is framed as a tool for monitoring elusive and rare species.

## Background & Description

**Classical CMR** estimates abundance (N) by marking animals in a first capture session and recording the proportion of marked animals in later sessions. This approach is difficult for species that are hard to catch or handle. Molecular tags from noninvasively collected samples avoid handling, so they are widely used to estimate population size. However, genetic tags differ from physical marks in two ways:

- **[[Shadow Effect]]:** two different individuals can share the same multilocus genotype, which underestimates N.
- **[[Genotyping Error]]:** DNA from noninvasive samples is prone to errors, which typically overestimate N.

Previous genetic studies relied on [[Multisession Sampling]], or on the asymptote of [[Accumulation-Curve Method]]s that plot unique genotypes against the number of samples analyzed. Accumulation-curve methods do not explicitly model the capture-recapture process and cannot easily account for capture heterogeneity.

**Simulation design (GEMINI):**

- **Population:** allele frequencies from one noctule bat (*Nyctalus noctula*) population, chosen for its lowest probability of identity among 13 studied populations.
- **Loci:** eight loci. Reported probability of identity was 4.38 × 10⁻¹³ (unbiased), so the shadow effect should be minor.
- **Population size:** N = 100 (additional runs with N = 1,000 gave similar results).
- **Sample sizes (n):** 50, 100, 150, and 300 samples. For single-session designs, all samples came from one session. For multisession designs, samples were split across five sessions (e.g., 50 samples = 10 per session × 5).
- **Assumptions:** stationary, closed population; equal capture probability for all individuals; no loss of marks.
- **Replication:** each condition was replicated 200 times.
- **Genotyping:** eight PCR amplifications per sample and locus, with a threshold rule that retained alleles appearing at least three times. Error rates were set to allelic dropout (ADO) = 0.3 and false alleles (FA) = 0.1 per locus.

## Ecological & Environmental Context

The authors stress that sampling design depends on study purpose and field logistics:

- **Single-session sampling** is simpler in the field but estimates only N. It cannot be used for survival or recruitment, which require multisession CMR.
- **Feces persistence** affects independence between sessions. Feces can persist for long periods, such as about 100 days for forest elephants and years for European bats, so samples from one session may have been deposited during another.
- **Latrine species**, such as [[European Badger]] and bats, accumulate feces at shared sites. Sampling over one period gives a representative sample of the population if all individuals have an equal chance of defecating at the site.
- **Population closure** is harder to meet over long sampling periods, which favors single-session designs.

## Key Findings

**Estimation methods compared**

- **[[Maximum-Likelihood Model]] (MLM-M0):** Otis et al. (1978) model for closed populations, fitted with CAPTURE.
- **[[Accumulation-Curve Method]] (ACM):** three equations, from Kohn et al. (1999), Eggert et al. (2003), and D. Chessel (occupancy formulation). Data were permuted 50 times per replicate.
- **[[Bayesian Estimator]] (BM):** Gazey and Staley (1986) sequential method. Two versions were tested: BM-multiple and BM-single.

**Results with sample identities**

- The [[Kohn Equation]] ACM was the most biased. Mean bias ranged from about 1.36% to 26%. Its [[Mean Squared Error]] (MSE) was at least 8 times, and up to about 200 times, higher than the others, so it was dropped from further analysis.
- MSE, bias, and variance all decreased as sampling effort increased. All methods overestimated N at n ≤ 150. Bias became negligible at n = 150, and variance became negligible at n = 300.
- At n = 50, the [[Eggert Equation]] ACM gave the worst results. The Chessel ACM and BM-single gave the best results, with BM-multiple and MLM-M0 close behind.
- Coverage of the 95% confidence interval (CI) was low for ACM-Eggert and ACM-Chessel (9.5–42% at n = 50). For MLM-M0, BM-multiple, and BM-single, coverage was at least 82%.
- The Chessel ACM had a narrower CI than the others, but its CI included the true N in only about 60–80% of simulations.

**Results with consensus genotypes**

- Correct identification rose from 2.9% for uncorrected genotypes to 99.3% for consensus genotypes.
- Residual multilocus error after correction averaged 0.7%.
- Residual errors changed N estimates by 1.5–3.5%, depending on method and sample size.
- Differences between sample-identity and consensus-genotype estimates were significant only at the highest effort (n = 150 and n = 300). Bias was always positive.
- At n = 300, coverage for the MLM dropped to about 25%. Other methods showed only slight reductions.

**Main conclusions**

1. Single-session sampling gives estimates as reliable as multisession sampling. Two of three ACM equations and BM-single achieved MSE comparable to MLM-M0 and BM-multiple.
2. [[Bayesian Estimator]]s performed best overall. BM-single showed less bias and variance than BM-multiple in single-session designs. The authors attribute this to explicit modeling of the capture-recapture process and use of all recapture information.
3. The Kohn ACM equation was strongly biased and is not recommended under these conditions.
4. Residual genotyping error marginally biased estimates, but its effect was small. The bias from using molecular tags was negligible, even with error rates (ADO 0.3, FA 0.1) at the upper end of published values.
5. Noninvasive sampling avoids animal disturbance and can estimate N for species that are difficult to catch. This makes it useful for managing elusive and rare species.

**Caveats**

- Simulations assumed closure, equal capture probability, no time variation in capture, no mark loss, and no behavioral effects.
- Real populations with heterogeneity (different sexes, ages, or related individuals) could affect results. Such effects were not tested in this study.
- A pilot study is recommended to estimate genotyping error rates and set the minimum number of PCR amplifications needed.