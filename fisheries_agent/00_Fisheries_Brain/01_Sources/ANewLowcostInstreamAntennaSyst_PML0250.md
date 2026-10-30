---
species: Oncorhynchus mykiss
common_name: Steelhead (anadromous Rainbow Trout)
family: Salmonidae (salmonids, as referenced in text)
habitat: Small coastal streams and the freshwater-estuary interface
ocean_basin: Pacific Ocean
location: Scott Creek estuary, central California coast, USA
tags: [ichthyology, marine-biology, salmonidae, pit-tag, fish-telemetry, instream-antenna, steelhead, estuary]
title: "A New Low-Cost Instream Antenna System for Tracking Passive Integrated Transponder (PIT)-Tagged Fish in Small Streams"
source_id: "PML0250"
marsh_id: "PML0250"
library: "Marsh Library"
permission: "not public domain"
source_citation: "M. H. Bond, C. V. Hanson, R. Bernstein, S. A. Hayes, R. B. MacFarlane (2007). A New Low-Cost Instream Antenna System for Tracking Passive Integrated Transponder (PIT)-Tagged Fish in Small Streams. Transactions of the American Fisheries Society 136:562-569. Marsh Library ID: PML0250."
source_file: "Bond M.H. et al. 2007. A new low cost instream antenna systen for tracking passive integrated transponder PIT tagged fish in small streams.pdf"
text_extraction: "text"
---
# A New Low-Cost Instream Antenna System for Tracking PIT-Tagged Fish in Small Streams

#ichthyology #marine-biology #salmonidae

## Executive Summary

This methods paper describes a low-cost, low-power [[Instream Antenna]] system for detecting [[Passive Integrated Transponder Tag|PIT-tagged]] fish movement in small streams. The system uses [[Allflex-USA]] technology and reads both [[Half-Duplex Tag|half-duplex (HDX)]] and [[Full-Duplex Tag|full-duplex (FDX)]] tags. The complete reading system cost approximately US$1,000, compared with US$5,000–20,000 for commercial FDX systems. The antenna was tested at the head of the [[Scott Creek]] estuary in central California, where it recorded the [[Diel Movement]] of juvenile and adult [[Steelhead]] between the estuary and upstream freshwater habitat during spring and fall 2004.

## Background & Description

PIT tags are small, inert, battery-free, and can last the life of a tagged animal. They have been used to measure growth, survival, and movement of individual fish. Detection methods include handheld [[Wand-Type Reader]] units for active searching and automated instream readers for larger-scale movement studies. Automated systems are often expensive, and commercial readers for FDX tags are costlier than those for HDX tags.

Tag types differ in size and suitability:

- **HDX tags:** 23.1 mm long, 3.9 mm diameter, 0.6 g. Suitable for larger fish (salmonids >80 mm fork length).
- **FDX tags:** 11.5 mm long, 2.1 mm diameter, 0.09 g. Suitable for smaller fish (~65 mm FL). Similar-sized tags have shown no observable effects on survival, growth, or swimming performance in salmonids (Prentice et al. 1990).

Historically, researchers had to choose one tag type and build a reader around it. Changing tag types mid-study meant running two reader systems at once. The authors' goal was a single, inexpensive reader that handles both tag types.

The Allflex circuitry conforms to ISO 11784/11785 animal-tagging standards. This technology is common in pet and livestock industries but was almost unknown in fisheries.

## Ecological & Environmental Context

The study site was the head of the estuary of Scott Creek, a small stream on the coast of central California (37°02′22″N, 122°13′W). Steelhead were tagged at the tail of the estuary, about 1,000 m downstream of the reader-antenna. The reader was positioned to detect fish moving between estuarine and upstream freshwater habitats.

Key deployment conditions:

- A blocking net ensured that all fish moving through the section passed through the antenna window.
- The frame was beveled on the upstream face and protected by a 6-mm aluminum debris plate.
- The antenna was bolted to the streambed with stainless steel hardware. Small amounts of metal did not measurably affect reading.
- Sites must be checked for electromagnetic interference before installation.

Environmental factors that could explain movement timing, such as food resources, flow, temperature, and dissolved oxygen, were suggested for future analysis but were not measured in this study.

## Key Findings

### Antenna and System Design

- **Antenna:** Six turns of 10 AWG solid copper wire in a 2.5 cm PVC housing, with an inductance of about 250,000 nH. The antenna measures 279.4 cm × 60.9 cm.
- **Reader:** A bare Allflex ISO panel reader board (25 × 3.5 × 3 cm) sealed in PVC. The reader-to-antenna connection must not exceed 60 cm.
- **Power:** Two 225 Ah, 6 V lead-acid batteries in parallel, housed in a waterproof case on the bank. Power and communications run through 23 m of flexible conduit.
- **Data logger:** A custom device built on a PIC microcontroller. It stores 2,000 tag events with date and time stamps and costs under US$60. Any device that reads an RS232 or RS422 serial port can log the reader output.
- **Total cost:** The complete system cost approximately US$1,000. The body text states the total as "approximately $1,0?5" because the figure is partly garbled in the scan. Costs rise with debris loads, poor substrate, long cable runs, or freezing temperatures.

### Reading Performance

- The 279.4 × 60.9 cm antenna was the largest size that reliably read both tag types throughout the reading window.
- Tags passed perpendicular to the antenna at speeds up to 1 m/s were all read.
- Tags passed within 8 cm outside the reading window on any side were also read.
- Detection probability decreased at angles away from perpendicular.
- Maximum reading frame: 40 cm for FDX tags and 152 cm for HDX tags.
- When laid flat on the streambed, the antenna reads tags within 20 cm of its plane.
- Small deformations of the antenna shape reduce reading range.
- Alternating HDX and FDX tags can be read in rapid succession as long as both do not occupy their reading frames simultaneously.

### Power Performance

- Reader and antenna draw approximately 400–900 mA at 6 V DC. The text reports this range, though the scan is partly illegible.
- The two batteries sustained continuous reading for roughly 12–24 days between changes (figure partly garbled in the scan).
- The compact, low-power design may suit handheld wand-type use in stream surveys.

### Steelhead Movement Results

- **Tagged:** 231 wild steelhead (>63 mm FL) were tagged with Allflex FDX tags in the estuary.
- **Detected:** 146 steelhead were recorded moving through the reader at least once during summer and fall.
- **Reads:** The exact count of independent reads is partly garbled in the scan. The text gives "4.65g," which is likely about 4,650 reads.
- **Deployment:** The prototype ran continuously from April to December 2004, with only brief interruptions for battery changes.
- **Diel pattern:** Movement was mostly diel, concentrated just before dawn and just after sunset. This is consistent with prior salmonid studies (Greenberg and Giller 2003; Bradford and Higgins 2001).
- **Seasonal shift:** Fall peaks occurred later in the morning and earlier in the evening than spring peaks. The authors attribute this to seasonal changes in sunrise and sunset times.
- **Direction:** With one reader, direction of movement could not be determined for each event. Trapping data showed that most upstream movement occurred after dusk, and fish returned to the estuary in the morning.

### Conclusions and Recommendations

- The system is a feasible, low-cost option for high-resolution fish tracking in small streams where commercial systems are prohibitive.
- Placing two readers, one upstream of the other, would allow unambiguous determination of movement direction.
- The authors recommend linking movement data to environmental variables to identify the drivers of estuary-to-freshwater movement.