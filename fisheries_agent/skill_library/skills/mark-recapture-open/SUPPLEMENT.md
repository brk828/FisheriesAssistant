---
name: mark-recapture-open-supplement
status: draft
generated: 2026-10-20
---

# mark-recapture-open: supplement from developer-supplied sources


## PIT Tag Detection Systems

### Passive Instream Antennas

[[src:webber-2014]] deployed stationary flat-plate antennas (33 × 68 cm) to detect razorback suckers in the Green River, Utah, at a known spawning location. These antennas operated for 29 days in 2012 and continuously for 90 days in 2013, detecting 569 razorback suckers, 19 Colorado pikeminnow, and 16 flannelmouth suckers [[src:webber-2014]]. The readers recorded time and date of each detection and excluded the same fish from being detected more than once within a 10-second period [[src:webber-2014]]. In 2013, a platform was constructed to hold the battery and reader above high water, and solar panels continuously powered the batteries [[src:webber-2014]]. Longer cords allow readers to remain above high water, but decrease the read range of antennas (general).

[[src:franssen-2021]] used riverwide active sampling and remote PIT tag antennas to resample razorback suckers over three years, with PIT antennas deployed at multiple locations along the San Juan River. These remote detections accounted for 63% of all reencounters [[src:franssen-2021]].

### Detection Probability and Encounter Histories

(General) Detection probability refers to the probability that a tagged fish present in the study area is detected during a sampling occasion. [[src:franssen-2021]] included both active captures (raft-mounted electrofishing and trammel nets) and passive PIT antenna detections in their encounter histories, treating them identically in the analysis. Sampling effort varied by year: 2018 had significantly lower effort than 2017 and 2019 because annual monitoring was not conducted due to funding lapse, and low flows left one antenna out of water for much of the year [[src:franssen-2021]].

[[src:webber-2014]] noted that 93% of the 569 razorback suckers detected by antennas had not been detected by researchers since being stocked (up to 13 years prior), demonstrating that passive detection greatly increases detection rates over active sampling alone. They suggest that survival estimates may have been underestimated when only active capture data were used; studies in the lower Colorado River showed survival rates increased from 9% or less (active sampling only) to 39% when PIT antenna data were added [[src:webber-2014]].

## Tag Size and Retention

### Tag Size Selection

[[src:buxton-2025]] tested 8-mm and 12-mm PIT tags on Santa Ana Suckers ranging from 60–130 mm fork length. The study randomly assigned 61 fish to three treatments: control (n=20), 8-mm PIT tag (n=21), and 12-mm PIT tag (n=20) [[src:buxton-2025]]. (General) The rule of thumb is to avoid implanting tags exceeding 2% of body weight, though recent studies have revised this guideline.

### Tag Retention

[[src:buxton-2025]] reported tag loss rates of 5.3% for the 8-mm tag treatment and 5.9% for the 12-mm tag treatment over 36 days. Fisher's exact test indicated no statistically significant difference in tag loss across treatments (P=0.536) [[src:buxton-2025]]. One 12-mm tag loss occurred after the implanter malfunctioned and required a second injection [[src:buxton-2025]].

[[src:franssen-2021]] assessed apparent survival of razorback suckers over three years post-stocking; the study implanted all fish with identifiably unique PIT tags [[src:franssen-2021]]. (General) Long-term tag retention studies are essential for multi-year mark-recapture analyses.

[[src:avery-2011]] used PIT tags that were retained in river otter scat after predation, enabling distributional analysis of released razorback suckers [[src:avery-2011]].

### Survival Outcomes Related to Tagging

[[src:buxton-2025]] reported overall 87.8% survival. Five mortalities occurred within 48 hours of tagging: two in the 8-mm treatment (both within 1 hour) and three in the 12-mm treatment (within 48 hours, showing signs of internal bleeding) [[src:buxton-2025]]. The smallest fish in the study (60 mm fork length) tagged with a 12-mm tag died [[src:buxton-2025]]. Fisher's exact test showed no statistically significant difference in survival across treatments (P=0.354) [[src:buxton-2025]]. The study suggested mortality was likely due to tag puncturing vital organs or damage to organs in the peritoneal cavity [[src:buxton-2025]].

## Apparent Versus True Survival

### Definition and Interpretation

[[src:franssen-2021]] used Cormack–Jolly–Seber (CJS) live-recapture models in Program MARK version 9.0 to estimate apparent survival and detection probabilities. These models estimate apparent survival rather than true survival because permanent emigration out of the sampled study area is confounded with true mortality [[src:franssen-2021]]. The study explicitly used the term "survival" while noting it only estimated apparent survival [[src:franssen-2021]].

### Movement and Emigration Effects

[[src:franssen-2021]] found that downstream movement after stocking was negatively associated with fish size, indicating that emigration likely contributed to higher apparent mortality of smaller fish. The study assessed correlations between individual fish characteristics and downstream movement using Kendall's rank correlation test (nonparametric, due to nonnormal distribution and heterogeneity of variances) [[src:franssen-2021]].

[[src:avery-2011]] and other researchers noted that pond-reared razorback suckers commonly move large distances downstream after stocking, sometimes 1–92.1 km, which complicates survival assessment [[src:avery-2011]]. [[src:webber-2014]] documented one razorback sucker moving upstream 311 km from the stocking location to the detection site.

## Release-Group and Rearing Covariates

### Flow Conditioning Treatment

[[src:franssen-2021]] compared flow-conditioned (n=533) versus control (n=530) age-2 razorback suckers reared for 10 weeks in adjacent outdoor raceways. The flow treatment raceway included a center wall, cinderblocks as baffles perpendicular to flow, and pumps creating circular flow with median velocity of 0.125 m/s [[src:franssen-2021]]. 

Flow conditioning doubled mean apparent survival during the first overwinter period: control fish = 0.14 (95% CI = 0.09–0.21), flow-conditioned fish = 0.28 (95% CI = 0.19–0.38), both calculated at mean size of 325 mm total length [[src:franssen-2021]]. Both groups had similar mean overwinter apparent survival thereafter (both >0.75) [[src:franssen-2021]].

[[src:avery-2011]] exercise-conditioned razorback suckers using propeller pumps generating approximately 30 cm/s flow for 30 days prior to stocking. Exercised fish maintained position in a laboratory flow chamber two times longer and at velocities 25 cm/s higher than nonexercised fish [[src:avery-2011]].

### Size at Stocking

[[src:franssen-2021]] found size at stocking and Fulton's condition factor (K) were positively associated with first-overwinter apparent survival regardless of treatment. Mean survival was <0.20 for fish <275 mm total length but >0.65 for fish >450 mm total length [[src:franssen-2021]]. Individual covariates (total length and K) were only assessed for survival during the first overwinter period because these values likely changed in subsequent years [[src:franssen-2021]].

[[src:buxton-2025]] tested for effects of initial fork length and weight on growth using ordinary least squares regression. Both initial fork length and weight significantly affected growth (P < 0.001 for length; P = 0.0153 for weight), with no significant treatment or interaction effects detected (P > 0.05) [[src:buxton-2025]].

## Model Selection and Reporting for CJS Analyses

### Model Structure

[[src:franssen-2021]] assessed effects of treatment (Flow), time (t), stocking size (TL), Fulton's K, and their interactions on survival (Φ). Because 63% of reencounters were remote PIT detections rather than in-hand captures, they did not assess effects of individual covariates on detection probability (ρ) [[src:franssen-2021]].

Time effects on survival were assessed two ways: full time-dependent model (Φ_t1,2,3_) and a structure grouping the first and third time periods due to considerably fewer 2018 captures (Φ_t2,1=3_) [[src:franssen-2021]]. Within- and between-year sampling periods were classified by calendar year, though most active sampling occurred March–November [[src:franssen-2021]].

### Handling Dead Encounters

Two experimentally stocked razorback suckers found dead were coded in the input file to be removed after their last encounter, following standard Program MARK procedures [[src:franssen-2021]].

### Model Selection

All possible combinations of effects and interactions on Φ and ρ were modeled and ranked using Akaike's information criterion corrected for small sample size (AICc) [[src:franssen-2021]]. (General) The RMark package provides an R interface to Program MARK, while the marked package offers alternative CJS implementation entirely in R.

### Reporting Standards

[[src:franssen-2021]] reported survival estimates with 95% confidence intervals for each treatment group and time period. Statistical tests used general linear models (with log₁₀-transformed total length) to compare size and condition between treatments, implemented using the "lm" function in R [[src:franssen-2021]].

---

**Suggested R workflow** (unexecuted):

```r
library(RMark)
library(FSA)

# Prepare encounter history data
# Columns: individual ID, occasion 1, occasion 2, ..., 
#          treatment, size, condition
ch_data <- process.data(encounter_df, model="CJS")

# Build covariate models for survival
phi_flow <- list(formula = ~Flow)
phi_time <- list(formula = ~time)
phi_size <- list(formula = ~TL + K)
phi_interact <- list(formula = ~Flow * TL)

# Detection probability structure
p_constant <- list(formula = ~1)
p_time <- list(formula = ~time)

# Run candidate model set
model_list <- create.model.list("CJS")
results <- mark.wrapper(model_list, data=ch_data, 
                        adjust=TRUE)  # AICc adjustment

# Extract top model and survival estimates
top_model <- results
survival_ests <- get.real(top_model, "Phi", vcv=TRUE)
```

This supplement synthesizes practices from regional fisheries studies applying CJS models to PIT-tagged endangered suckers, emphasizing detection infrastructure, tag retention assessment, treatment covariates, and transparent reporting of apparent survival. (unsourced)
