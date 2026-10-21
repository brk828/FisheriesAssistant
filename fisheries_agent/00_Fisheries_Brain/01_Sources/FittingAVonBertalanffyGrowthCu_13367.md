---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: N/A
tags: #fisheries-biology #growth-modeling #von-bertalanffy #statistical-methods #population-dynamics #age-length-data #least-squares #mathematical-modeling
title: "Fitting a Von Bertalanffy growth curve by least squares"
source_id: "13367"
minckley_id: "13367"
source_citation: "P. K. Tomlinson and N. J. Abramson (1961). Fitting a Von Bertalanffy growth curve by least squares. California Fish and Game Fish Bulletin 116: 3-69. Minckley Library ID: 13367."
source_file: "13367.pdf"
text_extraction: "ocr"
---
# Fitting a von Bertalanffy Growth Curve by Least Squares

#fisheries-biology #growth-modeling #von-bertalanffy #statistical-methods #population-dynamics

## Executive Summary

This technical bulletin presents a practical method for fitting the [[Von Bertalanffy Growth Curve]] to fish age-length data using [[Least Squares]] estimation. Authors Patrick K. Tomlinson and Norman J. Abramson provide comprehensive polynomial tables and computational procedures to enable fisheries biologists to estimate growth parameters (L∞, k, and t₀) when ages are equally spaced. The method addresses limitations of previous graphical and approximation techniques, offering an objective, repeatable approach with known statistical properties. The bulletin includes extensive polynomial tables (J_{p,j}(z)) for 4 to 18 age groups and a worked example using [[California Yellowtail]] (*Seriola dorsalis*) data. This work responds to growing interest in growth parameters' physiological significance and their relationships to environmental factors, mortality rates, and population characteristics.

## Background & Description

The [[Von Bertalanffy Growth Equation]] describes fish growth as an asymptotic function approaching maximum size. Beverton's (1954) modification takes the form:

l_t = L∞[1 - e^(-k(t-t₀))]

where:
- l_t = length at age t
- L∞ = maximum expected length (asymptotic size)
- k = growth coefficient (proportional to rate of body material destruction)
- t₀ = hypothetical age at zero length

The method builds on Pimentel-Gomes' (1953) approach for fitting [[Mitscherlich's Regression Law]], extending it to the von Bertalanffy curve. The general form y = α + βρ^x (where 0 < ρ < 1) encompasses multiple growth models including [[Gompertz's Law]], the [[Logistic Curve]], and von Bertalanffy functions.

Previous fitting methods relied on:
- Graphical "guessing-by-eye" approaches (von Bertalanffy, 1938)
- Approximation through transformation (Beverton and Holt, 1957; Ricker, 1958)
- The [[Gulland-Holt Plot]] for preliminary parameter estimation

These lacked objectivity and statistical rigor needed for comparative studies examining parameter relationships to temperature, food supply, population density, natural mortality, fecundity, and maturity characteristics.

## Ecological & Environmental Context

The foreword by Sidney J. Holt emphasizes the ecological importance of growth parameters in fisheries science:

**Environmental Relationships:**
- L∞ and k vary with food supply and population density
- k correlates with water temperature (Taylor 1958, 1959; Holt 1959, 1960)
- Parameters show taxonomic significance across species

**Population Dynamics Applications:**
- Growth parameters correlate with natural mortality and lifespan (inter- and intra-specifically)
- Mean size at maturity relates to growth parameters on interspecific basis
- Potential connections to metabolic parameters (Beverton and Holt, 1959)
- Essential for assessing exploited stock status and fisheries regulations effects

**Research Applications:**
- Analysis of [[Fish Tagging Experiments]] (discussed at North Atlantic Fish Marking Symposium, 1961)
- Fish-culture experiment analysis
- More discriminatory than simple growth increments or specific growth rates

The method enables systematic exploration of how biotic and abiotic environmental factors influence growth, supporting both theoretical population dynamics and practical fisheries management.

## Key Findings

**Methodological Contributions:**

1. **Parameter Estimation Procedure** (equal sample sizes):
   - Solve determinant equation for z = e^(-kq) using polynomial tables
   - Calculate k = -(1/q)log_e(z) where q is the constant age interval
   - Solve linear system for L∞ and t₀ using determinant methods
   - Under normality assumption, estimates equivalent to maximum likelihood

2. **Polynomial Tables Provided:**
   - J_{p,j}(z) tabulated for p = 4 to 18 age groups
   - z values from 0.01 to 0.99 in 0.01 increments
   - Computed in double-precision on IBM 7090
   - Accurate to eight significant digits
   - Enable rapid solution without electronic computer access

3. **Variance Estimation:**
   - Formulas provided for V(L∞), V(k), and V(t₀)
   - Based on Stevens (1951) method
   - Requires equal sample sizes per age group
   - Residual variance: s² = Σ(l_j - ŷ_j)²/(p-3)

4. **Weighted Least Squares Extension:**
   - Accommodates unequal sample sizes across age groups
   - Weights w_j = n_j/n (inversely proportional to variance)
   - Requires iterative solution (tables not practical)
   - Appropriate when variance constant across observations

5. **Worked Example** ([[California Yellowtail]]):
   - Random sample: n=11 per age group, 8 age groups (n=88 total)
   - Estimated parameters: L∞ = 1122.8 mm, k = 0.1776, t₀ = -2.45 years
   - Variances: V(L∞) = 4075.3, V(k) = 0.001060, V(t₀) = 0.1970
   - Demonstrates complete computational procedure with tables

**Advantages Over Previous Methods:**
- Objective and repeatable (eliminates subjective graphical fitting)
- Efficient (least squares under normality)
- Provides variance estimates for parameters
- Accessible to researchers without high-speed computers
- Well-documented statistical properties

**Limitations Noted:**
- Requires equally-spaced ages for tabled solution
- Equal sample sizes needed for variance formulas
- Distribution of parameter estimates generally unknown (caution in interpretation)
- Assumes constant variance across age groups

**Historical Context:**
The method addresses needs identified at multiple 1959-1961 symposia ([[Ciba Foundation Colloquium on Ageing]], [[British Ecological Society Symposium]], [[ICNAF Symposium]]) where growth parameter interpretation and estimation emerged as critical issues in fisheries biology and population dynamics research.