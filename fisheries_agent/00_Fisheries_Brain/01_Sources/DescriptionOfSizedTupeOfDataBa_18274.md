---
species:
  - "Ptychocheilus lucius"
  - "Xyrauchen texanus"
  - "Gila cypha"
  - "Gila elegans"
common_name: "Colorado Squawfish, Razorback Sucker, Humpback Chub, Bonytail Chub (with other co-occurring fishes)"
family: "Cyprinidae, Catostomidae"
habitat: "Freshwater rivers, backwaters, eddies, shoreline and side channels, flooded gravel pits, and reservoir margins"
ocean_basin: "N/A"
location: "Colorado River Basin (Green, Colorado, Gunnison, Dolores, Yampa, White, Duchesne, Little Snake rivers; Lake Powell; Grand Valley)"
tags:
  - ichthyology
  - marine-biology
  - cyprinidae
  - catostomidae
  - freshwater-fish-survey
  - data-documentation
title: "Description of sized tupe of data base for Colorado River fishes"
source_id: "18274"
minckley_id: "18274"
source_citation: "Unknown (1986). Description of sized tupe of data base for Colorado River fishes. Minckley Library ID: 18274."
source_file: "18274.pdf"
text_extraction: "ocr"
---
# Colorado River Basin Fish Survey Database: Structure, Sampling Designs and Data Availability

#ichthyology #marine-biology #cyprinidae #catostomidae

## Executive Summary

This document is a set of technical attachments (3a, 3b and 4) describing the [[Fish And Wildlife Service]] (FWS) [[Colorado River Basin]] database for endangered and rare fishes. It covers three data types: Catch, Rare, and [[Radiotelemetry]]. It also explains how each sampling design can be used to build habitat-utilization curves, lists the mainframe computing environment used to manage the data, and gives record counts. The fishes of primary interest are [[Colorado Squawfish]], [[Razorback Sucker]], [[Humpback Chub]] and [[Bonytail Chub]]. The document is a data-documentation and handling guide rather than a research report, so it contains no population estimates or ecological conclusions of its own.

## Background & Description

The database has three components:

- **Catch data:** total counts of all fish species captured in a collection or group of collections, together with physical site parameters. Each record is one species at one sample.
- **Rare data:** individual records for each rare fish (for example, total length), with physical parameters measured at the exact capture point.
- **Radiotelemetry data:** locations of radio-equipped adult fish and the physical parameters at those locations. Each record is one observation.

The physical parameters recorded in all types are water depth, water velocity at six-tenths of the water column, and dominant substrate size. Water temperature was measured in some collections. Catch measurements are averages over the area of a seine haul, whereas Rare measurements are point values at the capture location.

The Catch dataset holds about 60,000 records, reflecting roughly 25,000 individual sampling efforts with a variety of gears. Fewer than 20% of these efforts captured a rare fish. The Rare dataset holds about 8,000 records. The Radio dataset is much smaller, with 859 records in total.

### Sampling Designs

Each record carries a "Type" code identifying its sampling design. The main designs are:

- **Annual young-of-the-year (YOY) river-wide surveys** (September–October). Surveys began on the Green River in 1979 and on the Colorado River in 1982. Velocity was not measured in 1979 and 1980, so those data are excluded from analysis. Gunnison, Dolores, Yampa and White rivers were surveyed in some years, but no Colorado squawfish were collected there, so those data are not used. Sampling used 1/8-in (3 mm, Colorado River) or 3/16-in (4 mm, Green River) seines, with two backwater and two shoreline hauls every 5 river miles.
- **[[Standardized Sampling Program]]** (Green and Colorado rivers, 1979–1981; Gunnison, Dolores, White and Yampa rivers, 1981). Rivers were divided into homogeneous strata. Stations consisted of two 0.5-mile reaches separated by a 4.5-mile intervening reach. Each stratum was sampled once in pre-runoff and runoff periods and twice in post-runoff periods. Electrofishing, trap, gill, trammel nets and seines were used.
- **Diel YOY sampling** at sites with previously high squawfish numbers. Each site was sampled for 4 days, with three 8-hour periods per day divided into 4-hour halves, using a 1/4-in seine.
- **Adult capture for radio implantation** (mostly spring, mainly electrofishing, with trammel and gill nets). This design evolved into an annual spring monitoring program.
- **Spring monitoring program**, in which selected reaches are electrofished each year to track trends in juvenile and adult Colorado squawfish.
- **Grand Valley flooded gravel pit study** (1982), in which six pits connected to the river were sampled with trammel nets, gill nets and electrofishing.
- **Lake Powell radiotelemetry capture** of adult squawfish. Physical parameters were not measured, so these data are unsuitable for habitat curves.
- **Special rare-fish surveys**, which were highly variable, though some data suit curve generation for humpback chub, Colorado squawfish and razorback sucker.

Only seining data from the YOY surveys and diel sampling are suitable for YOY habitat-utilization curves. Other designs are suitable for juvenile and adult squawfish and for adult razorback sucker and humpback chub.

## Ecological & Environmental Context

The database emphasizes [[Habitat Utilization Curves]]: relationships between fish occurrence and depth, velocity, substrate and temperature. Habitat types recorded include backwater, eddy, isolated pool, main channel, pool, riffle, run, shoreline, side channel, lake and gravel pit. Substrate categories are silt, sand, gravel, rubble/cobble, boulder and bedrock.

The Catch dataset records roughly 50 taxa or code categories. These include the target endangered fishes, numerous suckers (bluehead, flannelmouth, longnose, mountain, white), sunfishes, black bullhead and channel catfish, trout, minnows and dace, and several hybrid combinations. Gear types include electrofishing, seines of several mesh sizes, trammel and gill nets, trap and wire traps, minnow traps, trawl and angling.

Radiotelemetry used two methods. In the first, depth, velocity and substrate were recorded each time a fish was located during routine tracking. In the second, a randomly selected fish was observed for one randomly chosen eight-hour period. If the fish stayed stationary for 30 minutes, habitat was measured and weighted by time in 15-minute intervals. In 1985, velocity was also measured at two-, six- and eight-tenths of the water column, 1 m on either side of the fish.

## Key Findings

**Data volume and coverage**

- Catch: about 60,000 records from about 25,000 sampling efforts. Fewer than 20% captured a rare fish.
- Rare: about 8,000 records. Rare-fish records have no matching data for sites where no rare fish were found.
- Radio: 859 records total (Table 5 lists yearly counts for Colorado, Green, Duchesne, White and Yampa rivers, 1980–1985; for example, 143 records on the Green River in 1980 and 108 on the Green River in 1984).
- Table 2 lists Colorado squawfish rare-data records by river and year, with the largest counts on the Green River in 1981–1982 and Colorado River in 1980–1981. Table 3 lists razorback sucker records and Table 4 lists humpback chub records, with the greatest totals on the Green River and Colorado River. Exact figures are in the source tables.
- Table 1 gives YOY Colorado squawfish totals by year and habitat for both rivers. Examples include 513 YOY from 41 backwater records on the Colorado River in 1985, and 329 total YOY across Green River collections in 1980.

**Data quality and limitations**

- Velocity was not measured for the 1979 and 1980 YOY surveys, so those data are excluded.
- Missing values are coded 9999 in the Catch dataset and 99 in the Larva dataset. The Catch documentation says the missing-value description is incomplete.
- The Radio database includes only stationary fish. Duration and count fields are not meaningful for moving fish.
- The Larva dataset (544 records) includes 1981 and 1982 records from all sites, and 1983 records only from sites with squawfish. Records for 1979, 1980, 1984 and 1985 had not yet been added at the time of writing.
- The SPSS listing shows 29,879 cases in the Catch file, which differs from the approximately 60,000 records stated in the text. The two figures may reflect different versions or aggregation levels, so the source should be checked before reuse.

**Computing environment and handling**

- The mainframe database resides on a CDC Cyber 865 at the Denver Federal Center, running NOS 2.4. Access is available at 300, 1200 or 2400 baud.
- Analysis and data management use [[SPSS Statistical Software]] version 9.0, which can handle up to 500 variables per record.
- Users need familiarity with NOS, the XEDIT text editor and SPSS. ASCII file transfer to a microcomputer is useful.
- The Radio and Larva datasets were exported for use in other systems. The Radio file is an ASCII file of about 50 kb, and the Larva file is in dBase 3 format with 128 fields, including size-class counts for each species (less than 10 mm up to over 60 mm).

**Significance**

The database supports habitat-use analysis for federally listed Colorado Basin fishes and for population monitoring. Its usefulness depends on choosing the correct sampling design for each analysis, and on accounting for missing values and differing protocols across years and rivers.