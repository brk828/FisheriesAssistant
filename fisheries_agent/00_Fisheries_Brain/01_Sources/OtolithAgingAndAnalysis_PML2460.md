---
species: N/A
common_name: Largemouth Bass (example in figures; OCR-garbled)
family: N/A
habitat: N/A
ocean_basin: N/A
location: Arizona, USA (Arizona State University)
tags: [ichthyology, marine-biology, otolith-aging, computational-biology, fish-age-estimation]
title: "Otolith Aging and Analysis"
source_id: "PML2460"
marsh_id: "PML2460"
library: "Marsh Library"
permission: "public domain"
source_citation: "B. Stewart (2005). Otolith Aging and Analysis. Arizona State University, Computational Biology Program. Marsh Library ID: PML2460."
source_file: "Stewart B. 2005. otolith aging and analysis .pdf"
text_extraction: "text"
---
# Otolith Aging and Analysis

#ichthyology #marine-biology #otolith-aging

## Executive Summary

This presentation, given by Bill Stewart of the [[Arizona State University]] Computational Biology Program, describes a project to build a program that estimates a fish's age by analyzing digital images of its [[Otolith]]s. The work covers otolith structure and growth, how biologists use otoliths, [[Image Enhancement]] in [[Matlab]], manual and semi-automatic methods for counting and measuring [[Annuli]], and back-calculation of past fish length using three models. The document has no numerical results for a specific fish population. Its example figures are labeled as [[Largemouth Bass]] (text is OCR-garbled), and its Weisberg example gives a small table of growth increments.

## Background & Description

**Otoliths.** An [[Otolith]] is a small calcified structure used for balance and hearing in fish. Each fish has three pairs: sagittae, lapilli, and asteriscii, which differ in shape and size. Otoliths grow continuously, so new material is added to the outer surface and older material is preserved. This creates a permanent record of the fish's life. Otoliths form daily rings; during periods of slow growth these rings pile up and form annular rings, or [[Annuli]].

**Other aging structures.** The presentation lists scales, bones, fin rays, and otoliths as structures used to age fish.

**Uses of otoliths.** Biologists use otoliths to study:
- Temperature history (Fanerson et al., 1995, as cited)
- Anadromy (Secor, 2002, as cited)
- Migration pathways (Thresher et al., 1994, as cited)
- Stock identification (Edmonds et al., 1995, as cited)
- Use as a natural tag (Campana, 1995, as cited)
- Age validation (many publications)

**Preparation.** Preparation is described as a very time-consuming process:
1. Mount the otolith on a slide.
2. Grind it until translucent.

**Project goal.** Create a program that calculates a fish's age by analyzing digital images of its otoliths.

**Software structure.** The [[Matlab]] program has three parts: image enhancement, methods for counting and measuring distances between annuli, and back-calculations.

## Ecological & Environmental Context

The presentation links otolith growth to environmental conditions and fish biology:

- **Growth and environment.** Slow-growing fish tend to have larger, heavier otoliths than fast-growing fish of the same size. The [[Biological Intercept Model]] accounts for this systematic variation in fish length.
- **Environmental effects on growth.** The [[Weisberg Model]] states that the year interaction term "describes how environmental conditions affect fish of different ages."
- **Stock and migration.** Otolith chemistry and structure are used to infer temperature history, anadromy, migration routes, and stock identity, as listed under Background.
- **Acknowledgements** credit [[Arizona Game and Fish]] staff (Kirk Young, Scott Bryan, Marianne Meding, Diana Rodgers) and ASU faculty (Rosemary Renaut, Paul Marsh), indicating a state-agency partnership.

## Key Findings

### 1. Image enhancement
- The [[Adapthisteq]] function applies contrast-limited adaptive histogram equalization ([[CLAHE]]).
- It divides the image into n × m blocks, computes a histogram for each block, and transforms pixel values so their distribution is approximately uniform.
- The "Numtiles" parameter sets the block grid. The example uses [2 2]. The figure comparing profiles with "No adjustment" and "Numtiles [20 20]" shows the effect of enhancement.
- The image-to-grayscale step is listed as "rgb2gray intensity image."

### 2. Measuring annuli
Two approaches are described.

**Manual:**
- The [[Impixel]] function lets the user click any point on the image.
- It outputs [x, y, intensity].
- The user counts the annuli and measures the distance from each point to the otolith focus.

**Semi-automatic:**
- The [[Improfile]] function reads intensity values along a line or multi-line path.
- The annuli profile is then analyzed to count rings.

### 3. Semi-automated counting
- The [[Polyfit]] function (p = polyfit(x, y, n)) finds the coefficients of a polynomial of degree n that fits the intensity data. Linear (n = 1) and quadratic (n = 2) fits are shown.
- Counting method: calculate the area under the polyfit line. For a better fit, disregard the first area plotted by the focus.
- Residual method: measure residuals below the polyfit curve, take their average, and multiply by a stringency factor between 0.1 and 0.5.
- The example values listed are: Median = 640, Stringency = 0.3. The OCR-garbled slide text also gives a calculation with the result "66.0" (uncertain due to OCR errors).
- Width at the edge of the selected area is used to calculate the number of rays (for fin-ray aging).

### 4. Back-calculation models
Back-calculation estimates fish length at earlier ages from otolith size. The presentation names three models.

**[[Frasier-Lee Model]] (regression):**
- L_i = a + (L_c − a)(S_i / S_c)
- L_i = body length (BCL) at annulus i
- L_c = length at capture
- S_i = otolith radius to annulus i
- S_c = total otolith radius
- a = correction factor, used only when aging with scales; otherwise a = 0

**[[Biological Intercept Model]]:**
- A modified Frasier-Lee model that accounts for systematic variation in fish length.
- L_i = L_c + (L_c − L_0)(S_i − S_c)/(S_c − S_0)
- L_0 = correction factor for body length
- S_0 = correction factor for otolith length
- The biological intercept can be estimated from simple measurements of fish and otolith size in newly hatched larvae in the laboratory.

**[[Weisberg Model]]:**
- Uses a linear model to separate age-specific and year-specific effects on otolith growth.
- Expected mean growth increment = age effect + year effect × year interaction.
- Analogous to a two-way analysis of variance, with fish age and growth year as factors for the average increment width.
- Example increment values listed in the text:
  - Age 1, 1993: 1.7
  - Age 2, 1994: 1.4
  - Age 3, 1995: 0.9
  - Age 1, 1994: 1.9
  - Age 2, 1995: 1.2
  - Age 3, 1996: 0.7
- A summary table gives 1993 (Age 1: 1.7), 1994 (Age 1: 1.9, Age 2: 1.4), 1995 (Age 1: 1.2, Age 2: 0.9), and 1996 (Age 1: 0.7).

### 5. Scope and limitations
- The document is a project presentation, not a research paper. It has no sample sizes, population data, or validation statistics.
- Reference lists and some slide text are unreadable because of OCR errors, so cited works and some values could not be confirmed.
- The "Graphical User Interface" slide is listed as a project component, but no details are given.