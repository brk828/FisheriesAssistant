---
species: "Carpiodes carpio (River Carpsucker)"
family: "Catostomidae"
habitat: "Freshwater river; Des Moines River"
ocean_basin: "N/A (freshwater system, Mississippi River drainage)"
common_name: "River Carpsucker"
study_location: "Des Moines River, Boone County, Iowa, USA"
study_years: "1964-1965"
sample_size: "144 individuals (fecundity estimates); 29 (equation calibration); 12 (egg diameter/weight relationship)"
source_id: "15698"
---

# A Method of Estimating Fecundity; with Data on River Carpsuckers, Carpiodes carpio

#ichthyology #marine-biology #Catostomidae #freshwater-biology #fecundity-estimation

## Executive Summary
This 1969 study (Behmer, published in *Transactions of the American Fisheries Society*) presents a refined statistical method for estimating fish fecundity, adapting a technique originally developed by [[Larimore 1957 Warmouth Fecundity Method]] for the [[Warmouth]] (*Chaenobryttus gulosus*). The method leverages tight allometric relationships between **egg diameter**, **dry egg weight**, and **wet ovary weight** to estimate the total number of maturing eggs without requiring exhaustive manual counting. The technique was applied to 144 [[River Carpsucker]] (*Carpiodes carpio*) collected from the Des Moines River, Iowa, during 1964–1965. The study establishes a strong linear relationship between female body weight and estimated egg number, and raises important caveats regarding multiple spawning events and oocyte atresia that could affect fecundity interpretation.

## Background & Description
- **Species**: River Carpsucker, *Carpiodes carpio* (family [[Catostomidae]])
- **Egg characteristics**:
  - Egg diameter measured in hundredths of millimeters via horizontal-axis projection on a scale microprojector (minimizes measurement bias)
  - Egg weight measured in micrograms (dry weight, after formalin preservation for several months)
  - Strong allometric (power-law) relationship between egg diameter and dry egg weight (log-log correlation coefficient r = 0.98)
- **Ovary characteristics**:
  - Wet ovary weight strongly correlated with dry weight of maturing eggs (r = 0.99)
  - Maximum recorded ovary weight: 151 g, representing 20.5% of total body weight in the most fecund female
- **Body size range**:
  - Females examined ranged from 183 g (lowest egg count: 4,430 eggs) to 737 g (highest egg count: 154,000 eggs)

## Ecological & Environmental Context
- **Habitat**: Riverine freshwater system — Des Moines River, Boone County, Iowa
- **Reproductive ecology**:
  - Evidence (per [[Behmer 1967 Spawning Periodicity Study]]) suggests River Carpsuckers may be **iteroparous within a season**, potentially spawning multiple times per year, meaning single fecundity estimates may underrepresent total annual egg production
  - **Oocyte atresia** (degeneration of eggs prior to spawning) occurs in ovaries during the spawning season, a phenomenon paralleled in [[Brook Trout]] (*Salvelinus fontinalis*) as documented by [[Vladykov 1956 Brook Trout Fecundity]] and [[Henderson 1963 Brook Trout Atresia Study]]
  - This atresia complicates fecundity estimates, since methods here quantify only **maturing eggs present at time of capture**, not total lifetime or annual reproductive output
- **Comparative context**: Method builds directly on techniques for the [[Warmouth]] (Centrarchidae), suggesting broad applicability of the egg diameter/weight regression approach across teleost taxa with determinate or indeterminate spawning strategies

## Key Findings

### Statistical Relationships Established
1. **Egg diameter vs. dry egg weight** (n = 12 fish, ~75 eggs/fish):
   - `log(mean dry egg weight, µg) = -4.256 + 3.264 × log(mean egg diameter, 0.01mm)`
   - Correlation coefficient: r = 0.98

2. **Wet ovary weight vs. dry weight of maturing eggs** (n = 29 fish):
   - `dry weight of maturing eggs (g) = -1.372 + 0.348 × (wet ovary weight, g)`
   - Correlation coefficient: r = 0.99

3. **Composite egg number estimation equation**:
   - `Y = 3,930.6 + 15.5X`
   - where `X = [-1.372 + 0.348(wet ovary weight)] × 10^6 / (mean egg diameter)^3.264`
   - Correlation with conventional egg-counting method: r = 0.96 (high validation accuracy)

4. **Body weight vs. egg number** (n = 144 fish, 1964–1965 combined):
   - `Egg number (thousands) = -6.72 + 0.158 × (weight of fish, g)`
   - Relationship is **linear** across the sampled weight range (100–700+ g)
   - [[Analysis of Covariance]] revealed **no significant differences** in slope or intercept between 1964 and 1965 sampling years, supporting temporal consistency of the relationship

### Methodological Significance
- Provides a **less labor-intensive alternative** to traditional gravimetric egg-counting methods
- Requires only: (a) mean egg diameter measurement, and (b) wet ovary weight — both faster to obtain than exhaustive counts
- Method's high correlation (0.96) with conventional counting validates its reliability for [[Catostomidae]] and potentially other oviparous fish with similar reproductive morphology

### Biological Caveats
- Fecundity estimates reflect **standing maturing egg stock**, not necessarily total annual reproductive output, due to:
  - Possible multiple spawning events per season ([[Behmer 1967 Spawning Periodicity Study]])
  - Ongoing atresia removing eggs from the maturing pool before spawning
- These caveats are broadly relevant to fecundity studies across fish taxa, as parallel atresia dynamics were noted in [[Brook Trout]] populations