---
species: N/A
common_name: N/A
family: N/A
habitat: N/A
ocean_basin: N/A
location: Mexico
tags:
  - climatology
  - meteorology
  - data-documentation
  - precipitation
  - temperature
  - drought-indices
title: "Douglas Mexican temperature, precipitation and drought data base documentation"
source_id: "12378"
minckley_id: "12378"
source_citation: "D. Arthur (1992). Douglas Mexican temperature, precipitation and drought data base documentation. Minckley Library ID: 12378."
source_file: "12378.pdf"
text_extraction: "ocr"
---
# Douglas Mexican Temperature, Precipitation and Drought Data Base Documentation

#climatology #meteorology #data-management

## Executive Summary

This document describes a comprehensive climatological database for Mexico developed by Dr. Arthur Douglas (Creighton University). The dataset comprises monthly temperature and precipitation records from 280 precipitation stations and 92 temperature stations across 18 climatological divisions in Mexico, covering the period 1947–1988 (with some records extending earlier). The database includes raw station data, divisional means, standard deviations, and computed [[Palmer Drought Severity Index]] (PDSI) values. Data were double-keyed, quality-controlled using 3-sigma limits, and adjusted for varying station densities using effective station number calculations. This is a meteorological/hydrological dataset with no direct focus on fish or aquatic ecosystems.

## Background & Description

Dr. Douglas obtained paper copies of monthly temperature and precipitation data for Mexican meteorological stations. Station selection criteria included: (1) similarity in slope aspect and elevation, (2) minimum 95% data recovery for 1947–1988, and (3) annual rainfall totals within 20% of area-wide mean. The 18 climatological divisions (Figure 1, not reproduced here) were defined based on station density, targeting approximately 15 long-term stations per division—a methodology consistent with Englehart and Douglas's 60-division grid for the United States.

**Station Coverage:**
- **Precipitation stations:** 280 total, ranging from 10–20 per division (e.g., Division 1: 1–10 stations; Division 8: 1–20 stations)
- **Temperature stations:** 92 total, with sparser coverage (e.g., Division 1: 0–1 stations; Division 8: 0–10 stations)
- **Geographic extent:** All major Mexican states, including [[Baja California]], [[Sonora]], [[Chihuahua]], [[Durango]], [[Coahuila]], [[Nuevo León]], [[Tamaulipas]], [[Nayarit]], [[Jalisco]], [[Colima]], [[Guerrero]], [[Michoacán]], [[Guanajuato]], [[San Luis Potosí]], [[Hidalgo]], [[Distrito Federal]], [[Morelos]], [[Puebla]], [[Veracruz]], [[Oaxaca]], [[Chiapas]], [[Campeche]], and [[Yucatán]]

**Data Format:**
- Temperature: degrees Celsius to tenths
- Precipitation: millimeters to tenths
- Missing data: coded as -9999
- Trace amounts: coded as -8888

Station metadata include latitude, longitude, elevation, and unique station identifiers. Appendices A and B (partially reproduced) list station names, locations, and elevations (e.g., El Arco, Baja California Norte: 28°01'N, 113°25'W, 300 m elevation).

## Ecological & Environmental Context

While this dataset does not directly address aquatic ecosystems or fish populations, precipitation and temperature are fundamental drivers of hydrological regimes, which in turn govern freshwater and estuarine habitats. Key environmental parameters include:

- **Precipitation variability:** Critical for river discharge, lake levels, and wetland extent—all of which influence fish spawning, migration, and recruitment
- **Temperature regimes:** Affect water temperature, evaporation rates, and seasonal thermal stratification in aquatic systems
- **Drought indices:** [[Palmer Drought Severity Index]] (PDSI), [[Palmer Hydrologic Drought Index]] (PHDI), Palmer Z-Index, and [[Climate Analysis Center Modified Palmer Drought Index]] (PMDI) quantify moisture deficits that can lead to habitat contraction, reduced dissolved oxygen, and increased salinity in estuaries

**Base Periods and Normal Periods:**
- Base periods defined as longest interval with ≥50% of maximum stations reporting (Appendix D)
- Normal periods computed for 30-year intervals: 1901–1930, 1911–1940, 1921–1950, 1931–1960, 1941–1970, 1951–1980, 1961–1990, and full period of record (minimum 25 years required)

**Divisional Adjustment Procedures:**
To account for temporal variation in station density, divisional means were adjusted using effective number of stations (E):

$$E_{ij} = \frac{N_{ij}}{1 + \bar{r}(N_{ij} - 1)}$$

where $N_{ij}$ = actual number of stations for year $i$ and month $j$, and $\bar{r}$ = mean divisional correlation for month $j$ (Appendices E and F). Adjusted divisional values ($V_{ij}$) were computed as:

$$V_{ij} = D_{bj} + (A_{ij} \times F_{ij})$$

where $D_{bj}$ = divisional mean for base period $b$ and month $j$, $A_{ij}$ = mean divisional anomaly, and $F_{ij} = E_{ij}/E_{rj}$ (adjustment factor relative to reference year $r$).

## Key Findings

**Data Quality and Completeness:**
- All data were double-keyed and compared record-by-record; discrepancies were flagged and corrected against paper copies
- Quality control flagged values exceeding 3-sigma limits; Dr. Douglas verified flagged values against original Mexican records and climatological comparisons with surrounding stations
- For precipitation, ratios of monthly station values to divisional means were also used for QC

**Computed Datasets:**
- Monthly means, standard deviations, and N-counts for each station and division
- Normal values for each 30-year period (requires ≥25 years of data)
- Palmer drought statistics (PDSI, PHDI, Z-Index, PMDI) computed for each division and month, requiring serially complete data; missing precipitation replaced with divisional period-of-record means, missing temperature replaced with divisional POR means (minimal error for drought calculations, as precipitation is the critical element in Mexico)

**Archived Files:**
34 packed files (.EXE format) totaling ~1.5 MB unpacked, including:
- Station and divisional precipitation/temperature data (MEXPCP.DAT, MEXTMP.DAT)
- Station name lists with coordinates (MEXPCP.NAM, MEXTMP.NAM)
- Means, standard deviations, and counts for normal periods and full record (MXPCMNDV.DAT, MXTPMNDV.DAT, etc.)
- Annual divisional statistics (MXPCPMNY.DAT, MXTMPMNY.DAT)
- Palmer drought indices (MEX-PDSI.RPM, MEX-PHDI.RPM, MEX-Z.RPM, MEX-CAC.RPM)
- Adjusted divisional data (DVADJPCP.DAT, DVADJTMP.DAT)

**Methodological References:**
- Yevjevich (1972): effective number of stations
- Parker, Legg, and Folland (1992): adjustment methods for representative divisional values
- Englehart and Douglas (1985): precipitation frequency analysis for conterminous United States
- Karl and Knight (1985): Palmer Drought Severity Index atlas
- Heddinghaus and Sabol (1991): review of Palmer Drought Severity Index

**Limitations:**
- Temperature station density is considerably lower than precipitation (e.g., Division 1 has 0–1 temperature stations vs. 1–10 precipitation stations)
- Some divisions have months with no reporting stations during the base period (noted with asterisks in station count table)
- Data replacement for missing values (POR means) may smooth extreme events, though impact on drought indices is stated to be minimal

**Applications:**
This dataset provides a foundation for:
- Long-term climate trend analysis in Mexico
- Drought monitoring and water resource management
- Hydrological modeling (input for streamflow, lake level, and groundwater recharge models)
- Indirect assessment of climate impacts on aquatic ecosystems (e.g., correlating drought indices with fish population dynamics, wetland extent, or water quality parameters)

**Selected Bibliography:**
- Alexanderson (1986): homogeneity test for precipitation data
- Douglas and Englehart (1989): summertime ridge position and continental rainfall regimes
- Hansen and Lebedeff (1987): global surface air temperature trends
- Karl (1986): soil moisture parameterizations and subsequent temperatures
- Mitchell (1957): drought onset analysis
- Mooley, Parthasarathy, and Pant (1985): Indian monsoon rainfall and 500 mb ridge location
- Shukla and Misrah (1977): sea surface temperature, wind speed, and monsoon rainfall
- Wallen (1955): precipitation characteristics in Mexico

---

**Note:** This document describes a climatological database with no direct ichthyological or marine biological content. Tags reflect the meteorological focus. Cross-links to drought indices and geographic locations are provided for potential integration with aquatic ecosystem studies.