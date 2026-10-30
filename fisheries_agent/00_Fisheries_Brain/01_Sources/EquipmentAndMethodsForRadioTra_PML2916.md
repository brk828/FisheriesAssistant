---
species: Cyprinus carpio, Esox lucius, Micropterus salmoides, Coregonus clupeaformis, Perca flavescens, Oncorhynchus mykiss, Oncorhynchus tshawytscha, Salmo salar
common_name: Common carp, Northern pike, Largemouth bass, Lake whitefish, Yellow perch, Steelhead, Chinook salmon, Atlantic salmon
family: Cyprinidae, Esocidae, Centrarchidae, Salmonidae, Percidae
habitat: Freshwater lakes, rivers, streams, reservoirs and thermal discharge plumes
ocean_basin: N/A
location: Minnesota (Cedar Creek, Lake Superior, Lake Bemidji, Mary Lake), Lower Columbia River, Eastern Minnesota lakes
tags: [telemetry, radio-tracking, freshwater-fish, equipment-methods, biotelemetry]
title: "Equipment and Methods for Radio Tracking Freshwater Fish"
source_id: "PML2916"
marsh_id: "PML2916"
library: "Marsh Library"
permission: "public domain"
source_citation: "J.D. Winter, V.B. Kuechle, D.B. Siniff, J.R. Tester (1978). Equipment and Methods for Radio Tracking Freshwater Fish. University of Minnesota Agricultural Experiment Station Miscellaneous Report 152-1978. Marsh Library ID: PML2916."
source_file: "Winter J.D. et. al. 1978. equipment and methods for radio tracking freshwater fish.pdf"
text_extraction: "mixed"
---
# Equipment and Methods for Radio Tracking Freshwater Fish

#ichthyology #marine-biology #telemetry #freshwater-fish

## Executive Summary

This University of Minnesota Agricultural Experiment Station Miscellaneous Report (1978) by J.D. Winter, V.B. Kuechle, D.B. Siniff and J.R. Tester describes the design, operation and limits of [[Radio Telemetry]] systems for tracking freshwater fish. The authors compare radio with [[Ultrasonic Telemetry]], detail the construction of low-power [[Underwater Radio Transmitter]]s, document receiver specifications, and summarize field tracking methods and antenna accuracy tests. The report is written to help fisheries biologists, who may be unfamiliar with wildlife telemetry literature, establish tracking programs with minimal literature searching.

## Background & Description

Aquatic animal tracking began in the late 1950s with ultrasonic systems (e.g., [[Johnson 1960 Sonic Tracking]] at Bonneville Dam). Low-frequency, long-wave radio transmitters in the 30–300 kHz range were initially pursued because they are minimally affected by water conductivity, but aquatic work soon shifted to the 53 MHz range, while terrestrial ecologists used 22–300 MHz transmitters.

The University of Minnesota's Cedar Creek Bioelectronics Laboratory first radio-tracked fish in 1969, using carp and northern pike in a stream and [[Largemouth Bass]] in a northern Minnesota lake. Later work included [[Lake Superior]] whitefish, yellow perch in the thermal plume of a power plant, and salmon and sturgeon near hydroelectric dams on the lower Columbia River.

Key advantages of radio over ultrasonic telemetry, as reported:
- Equipment is relatively inexpensive: a portable receiver for under $1,000 (the first unit cost about $125), a vagi antenna for about $50, transmitters about $20 each, and assembled units under $100.
- Low current drain gives long life; a 0.5 mA drain transmitter powered by a 42 mAh Mallory battery transmits about 3 months.
- Tracking is possible without contact with the water.
- Crystal-controlled frequencies allow individual identification: about 10–20 ultrasonic tags versus over 100 radio tags can be distinguished by simple decoding.
- The same receivers and antennas serve both aquatic and terrestrial animals.

Limitations include attenuation of radio signals with increasing conductivity and depth, which restricts underwater radio tracking to freshwater species or marine animals that surface periodically. Large metal objects, terrain, powerlines, ignition systems and citizen's band radio can cause interference.

## Ecological & Environmental Context

Signal attenuation depends on water conductivity. Tests in Lake Superior (about 80 µmho/cm) and Lake Bemidji (about 300 µmho/cm), representative of low- and moderate-conductivity waters of eastern and central Minnesota, showed greater attenuation in more conductive water. In Lake Superior the signal was lost at 8 m depth but received to 50 m; in Lake Bemidji 50% of the signal was lost at 4 m.

Aquatic vegetation, ice and thermoclines had little effect on radio signals, whereas they can absorb or deflect ultrasonic signals. Air bubbles from turbulent water and algal growth on hydrophones can disrupt ultrasonic reception. Radio signals in a lake were stronger at 53 MHz than at 164 MHz in one comparison, contrary to earlier expectations.

Transmitter weight should not exceed 1–1.25% of the fish's weight out of water. Surgical attachment methods have welfare implications: stomach insertion was associated with higher mortality of upstream-migrating salmon in the Lower Columbia River (Haynes 1978) and gut-lining atrophy, while internal implantation requires longer habituation.

## Key Findings

**Transmitter design**
- A basic circuit based on Cochran and Lord (1963) was modified with a squegging circuit (added capacitor and resistor) to produce a pulsed signal, which saves power and extends life.
- Pulse width was 0.02–0.025 s, with 60–120 pulses per minute, and a 3% (or 1%) duty cycle.
- Pulse period can vary with temperature or pressure, allowing physiological and environmental telemetry (Tester and Siniff 1976).
- Batteries were certified [[Mercury Cell]]s (1.4 V) or [[Lithium Battery]]s (2.8 V). Lithium cells offer about 2.5 times the volume and twice the weight of an equivalent mercury cell and better low-temperature performance, but the smallest available (14 mm diameter, 4.3 g) was too bulky for small fish.
- Yellow perch transmitters used Mallory RM-675 batteries (30 × 10 × 5 mm, 3.3 g in water, 6.5 g dry). Perch transmitters lasted 3–5 days; the smallest had 0.2 mA current drain.
- Steelhead transmitters used Mallory RM-1 batteries (17 mm diameter × 40 mm, 15.6 g in water, 26.0 g dry). Steelhead transmitters lasted several months.
- Components were encapsulated in Scotchcast #5 epoxy resin; a silicone rubber (RTV-30) mold was used for potting.

**Signal and range**
- Transmitters operate at 53 MHz (52.5–53.5 MHz), chosen for presumed better water penetration.
- Maximum ranges in water of 80–300 µmho/cm: loop antenna 0.8–1.2 km; yagi antenna 2.4–3.6 km; loop on airplane 4.5 km.
- Transmitter antennas were kept broadside-aligned to be pointed at the receiver; broadside orientation reduced signal range by 35–45%.

**Receivers**
- The first receiver was a modified automobile radio (about $125), a portable hand-held unit distinguishing up to 30 individuals spaced 33 kHz apart.
- The later [[Phase-Locked Receiver]] (double conversion, frequency synthesizer) uses three detent switches with 1 kHz channel spacing, covers any 1 MHz range, distinguishes over 100 frequencies spaced 5–10 kHz apart, has sensitivity of −143 dBm, an IF bandwidth of 1.2 kHz, a noise figure of about 4 dB, and weighs 1.8 kg.
- A memory option stores up to 64 channels (16 or 32 in later versions) and can scan automatically; this supports airplane tracking and unattended monitoring.

**Tracking methods**
- Locations were plotted from compass bearings, visual bearings or both, often on gridded maps.
- Temporary towers (up to about 15 m) with yagi antennas and rotors gave good shore-based coverage; mobile tracking used vehicle-mounted yagi antennas.
- Airplane tracking used loop antennas mounted on aircraft struts; average ranges were 60% of maximum at 150 m altitude, 75% at 450 m and 100% at 750 m.

**Antenna accuracy**
- Yagi bearings at distances of 100–300 m were accurate to about ±3.0° (about ±5 m at 100 m and ±43 m at 800 m).
- Mean bearing error for a loop antenna was ±1.3 m from 5–15 m and ±4.9 m from 76–92 m.

**Attachment methods**
- External attachment: a sub-dorsal fin mount (best for fish with long dorsal fins, e.g., Centrarchidae and Percidae) and a mid-dorsal saddle mount (used for salmonids, e.g., 0.5–5.0 kg steelhead).
- Internal attachment: intraperitoneal implantation (fastest recovery time than external, but surgical habituation required) and stomach insertion (shortest habituation time).

**Key references and resources**
- Key sources include Cochran and Lord (1963), Marshall and Kupa (1963), Johnson (1960), Tester and Siniff (1976) and the *Underwater Telemetry Newsletter* (1971–1976).

**Funding acknowledgments**
- Supported by the U.S. Energy Research and Development Administration, the Minnesota Department of Natural Resources with U.S. Fish and Wildlife Service funds, and the U.S. Environmental Protection Agency.