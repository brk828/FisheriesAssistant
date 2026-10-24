---
species: N/A
common_name: N/A
family: N/A
habitat: Terrestrial climate stations (precipitation and temperature records); no aquatic habitat described
ocean_basin: N/A
location: Mexico (Baja California, Sonora, Chihuahua, Coahuila, Nuevo León, Tamaulipas, Veracruz, Oaxaca, Chiapas, Yucatán Peninsula and other states)
tags: [climate-data, precipitation, Mexico, Global-Historical-Climatology-Network, station-metadata, hydrology, tree-ring-laboratory]
title: "Temperature and precipitation data for the reporting stations from Mexico that are on the Global Historical Climate Network data set."
source_id: "12376"
minckley_id: "12376"
source_citation: "B. Lofgren (1994). Temperature and precipitation data for the reporting stations from Mexico that are on the Global Historical Climate Network data set. Minckley Library ID: 12376."
source_file: "12376.pdf"
text_extraction: "ocr"
---
# Mexican Precipitation and Temperature Station Data from the Global Historical Climatology Network

#ichthyology #marine-biology #climatology

## Executive Summary
This is a data package, not a research paper. A cover letter dated 2 November 1984 from the University of Arizona Laboratory of Tree-Ring Research was sent to Mr. Dave E. Brown of the Zoology Department at Arizona State University. It encloses temperature and precipitation data for Mexican reporting stations in the [[Global Historical Climatology Network]]. The package contains a station listing with coordinates, elevation and period of record. It also has monthly and annual precipitation averages for each station, raw monthly precipitation time series for a few stations, a data-format key, and a README for the search tools. The document contains no fish or other biological observations. It is useful as a climatic and hydrological baseline for aquatic habitats in Mexico.

## Background & Description
- **Sender and recipient:** the [[Laboratory of Tree-Ring Research]] at the [[University of Arizona]] (Tucson) provided the data to a zoologist at [[Arizona State University]]. The letter offers further data on request.
- **Data source:** the README says the records are long-term monthly temperature, precipitation, sea level pressure and station pressure data. They come from the Carbon Dioxide Information Analysis Center, Oak Ridge National Laboratory, data set NDP-041, Publication No. 3912. They are the [[Global Historical Climatology Network]] data.
- **Software:** a diskette includes FIND, a case-sensitive station-name search routine, and UPDATE, a routine that extracts single or multiple station records. Station files are mexppt.sta for precipitation and mextmp.sta for temperature. Output files can be named by the user, for example a TEXCOCO precipitation file.
- **Record format:**
  - Each record holds the year, 12 monthly values, a total or average, a station ID and a data-type code.
  - The data-type codes are DA = minimum temperature, DB = maximum temperature, DC = mean temperature and DD = precipitation.
  - Temperature is in tenths of a degree F and precipitation is in hundredths of an inch.
  - Missing-data flags of -9999 and -8888 appear in the raw series.
- **Station listing:** roughly 300 stations with 10-digit IDs beginning 4057. Each entry gives name, state, latitude, longitude, elevation (m), first and last year of record, and the first-column value. Coverage runs from the Baja California peninsula and Sonora to Chihuahua, Coahuila, Nuevo León, Tamaulipas, Jalisco, Nayarit, Michoacán, Mexico City, Veracruz, Oaxaca, Chiapas and the Yucatán Peninsula (Campeche, Quintana Roo). Records begin as early as 1878 for some stations (e.g., Mexico City area). Several run to 1990, and the last is Tapachula, Chiapas.

## Ecological & Environmental Context
The data describe regional climate gradients that structure freshwater and coastal habitats, though no habitats are discussed.
- **Arid northwest:** [[Baja California]] and [[Sonora]] stations are very dry. Examples are San Luis 11.34 in/yr, El Socorro 14.79 in/yr, Bahía de los Ángeles 5.91 in/yr and Delta 5.55 in/yr.
- **Summer-monsoon pattern:** [[Sierra Madre Occidental]] stations in Sonora, Chihuahua, Sinaloa and Durango peak in July–August, e.g., Moctezuma 15.41 in in July. Stations in the Cape Region of Baja California Sur peak in August–September, e.g., Santiago 12.42 in in September.
- **Gulf of Mexico slope:** Veracruz and Oaxaca stations are very wet, reflecting the [[Gulf of Mexico]] climate. Annual totals reach 492.24 in at Cataluña, Oaxaca.
- **Yucatán Peninsula:** stations such as Mérida (92.05 in/yr) have a wet summer and autumn season. A raw series is given for [[Yucatán Peninsula]] stations.
- **Northeast:** [[Nuevo León]], [[Coahuila]] and Tamaulipas show a September maximum. Monterrey peaks at 15.08 in in September.
- **Pacific coast:** Nayarit and Jalisco have a strong June–September peak. Paso de Arocha, Nayarit, had 46.41 in in August.

## Key Findings
- The package covers roughly 300 Mexican stations from the Global Historical Climatology Network, with monthly and annual precipitation averages for each.
- Each station's averages list the number of years of missing data per month and the number of years used in the calculation, so data completeness is documented.
- **Driest annual averages:** Bahía de los Ángeles (5.91 in), Delta (5.55 in), Bataques (5.00 in) and Colonia Juárez (6.70 in).
- **Wettest annual averages:**
  - Cataluña, Oaxaca: 492.24 in
  - Usila, Oaxaca: 376.77 in
  - Valle Nacional, Oaxaca: 372.46 in
  - Canton, Oaxaca: 350.30 in
  - Ojitlán, Oaxaca: 320.13 in
  - Ayautla, Oaxaca: 354.31 in
  - Requetemú, San Luis Potosí: 215.07 in
- Spatial climatic contrasts follow the Pacific monsoon and Gulf of Mexico rainfall regimes. The documented stations span arid desert to humid tropical settings.
- The raw monthly series (1895–1987 depending on station) are provided for Mérida, Tekax, Sotuta, Izamal, Valladolid, Telchaquillo, Campeche-region stations, Cuatro Ciénegas and others. They have many gaps flagged -9999/-8888.
- The Cuatro Ciénegas, Coahuila record (4057634205) is notable because that basin is a well-known aquatic endemism site. Its mean annual precipitation is about 22.67 in, with a September peak of 3.87 in.
- No fish, invertebrate, plankton, or water chemistry data are in the document. It supports hydroclimatic analysis only, such as drought and flow variation in [[Zoogeography]] studies.