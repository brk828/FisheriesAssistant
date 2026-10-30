---
species: Sander vitreus
common_name: Walleye
family: Percidae
habitat: Experimental stream channels with alternating pools and riffles
ocean_basin: N/A
location: EPA field station, Monticello, Minnesota, USA
tags: [ichthyology, marine-biology, percidae, radio-telemetry, fish-tracking, experimental-channels]
title: "Automatic Radio Tracking of Fish in Experimental Channels"
source_id: "PML1302"
marsh_id: "PML1302"
library: "Marsh Library"
permission: "public domain"
source_citation: "V. B. Kuechle, K. C. Zinnel, M. J. Ross, R. A. Reichle, D. B. Siniff, C. F. Kleiner (1986). Automatic Radio Tracking of Fish in Experimental Channels. U.S. Environmental Protection Agency, Center for Environmental Research Information, Cincinnati OH, EPA/600/S3-85/075. Marsh Library ID: PML1302."
source_file: "Kuechle V.B et al. 1986. Automatic radio tracking of fish in experimental channels.pdf"
text_extraction: "text"
---
# Automatic Radio Tracking of Fish in Experimental Channels

#ichthyology #marine-biology #percidae

## Executive Summary

This EPA project summary describes the development and field testing of an automated radio-telemetry system, the [[Monticello Remote Sensing System]] (MRSS), for tracking fish in outdoor [[Experimental Channels]] at the [[EPA Monticello Field Station]] in Minnesota. The system uses a microprocessor-controlled receiver and 12 buried antennas to locate radio-tagged [[Walleye]]. A 28-day system verification found that 98.7% of 5,297 known-position fixes were correct. A subsequent 28-day study recorded 21,039 location observations on 10 walleyes. The authors conclude that the system performed to specification and can measure movement, activity, mortality and social behavior, and that behavioral changes could serve as sensitive indicators of [[Aquatic Toxicants]] effects.

## Background & Description

The project was motivated by the need to monitor fish behavior in controlled channels without manual observation. Behavioral measurements were considered a sensitive way to detect the effects of contaminants, and automated tracking was expected to reduce labor while providing continuous data.

The authors emphasize software over hardware. Most automated animal monitoring systems of the period relied on fixed hardware, whereas this design used programmable logic to allow changes during development and in future studies. The software consisted of twelve distinct modules. A key Monticello-specific feature was a signal-to-noise ratio (SNR) measure that indicated how reliable each fish location was.

Key hardware and software components:

- **Microprocessor:** [[RCA 1802 Microprocessor]], programmed in RCA COSMAC assembly language. Development used the COSMAC Development System on the University of Minnesota Cyber 74 NOS time-sharing facility, with the code converted to hexadecimal machine code.
- **Memory:** Three pages of CDP 1822 static RAM (256 x 4 configuration, six chips), with standby power backup. ROM chips could replace program storage.
- **Signal measurement:** National Semiconductor ADC0808 eight-bit A/D converter.
- **Control interface:** RCA microterminal notepad and utility ROM UT5.
- **Output:** Results were printed on thermal paper, with receiver, channel, day, time of day and antenna number recorded.

Each tracking cycle initialized operating registers and scanned all 12 antennas for one fish frequency out of 32 possible channels. Scanning began at antenna 13, the farthest from the receiver, and ended at the antenna at station 2. The antenna with the strongest reading was recorded. The processor then compared that signal with the average background noise from the other antennas. This comparison acted as an index of reliability, so that weak signals, interference from power lines, unshielded ignition systems and thunderstorms could be rejected. The system then either moved to the next fish frequency or paused for a preset installation-dependent interval before repeating.

## Ecological & Environmental Context

The test channels were built at the EPA Monticello field station. Each channel was a riffle-and-pool stream section fed at a flow rate of 270 gal/min, with pools and riffles serving as the locations where fish were detected. The antennas were buried in the channel bed. The source describes testing of antenna designs and cable installation, including low-loss coaxial cable and direct burial, to reduce signal attenuation and stay within acceptable operating limits. Water chemistry, habitat and invertebrate or plankton data are not reported.

The fish studied were radio-tagged [[Walleye]]. The source does not report their size range, release density or transmitter specifications.

## Key Findings

**System verification (May 1979):**
- 11 walleyes were released and monitored over 28 days.
- Four transmitters at known pool and riffle locations served as reference transmitters.
- The system made 5,297 location determinations on those reference transmitters.
- 5,229 fixes (98.7%) were correct.
- Of the 68 errors, 42 (62%) occurred at low SNR, and most would likely have been rejected in actual tracking.

**Walleye tracking:**
- Over a 28-day period, 21,039 location observations were made on 10 walleyes.
- Movement patterns showed a pronounced crepuscular (dawn/dusk) activity pattern.
- Each walleye favored one pool on a given day or series of consecutive days.
- Larger fish moved away from the release pool sooner than smaller fish.
- The two largest fish used mutually exclusive primary pools in each time period.
- Walleyes tended to form groups of mixed size.

**Conclusions:**
- The Monticello Automatic Fish Tracking system performed to specification.
- It can measure movement patterns, mortality, activity patterns and social interactions.
- Changes in these behavioral parameters could provide timely and sensitive measures of the effects of aquatic toxicants.
- The document is an EPA project summary (EPA/600/S3-85/075) from the Center for Environmental Research Information in Cincinnati, Ohio.