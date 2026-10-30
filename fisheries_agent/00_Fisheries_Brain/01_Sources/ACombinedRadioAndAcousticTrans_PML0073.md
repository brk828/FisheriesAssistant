---
species: "Esox lucius"
common_name: "Northern Pike"
family: "Esocidae"
habitat: "Freshwater (shallow loch)"
ocean_basin: "N/A"
location: "Loch Kinord, Scotland, UK"
tags: [ichthyology, marine-biology, esocidae, biotelemetry, fish-tracking, acoustic-telemetry, radio-telemetry]
title: "A combined radio and acoustic transmitter for fixing direction and range of freshwater fish (RAFIX)"
source_id: "PML0073"
marsh_id: "PML0073"
library: "Marsh Library"
permission: "not public domain"
source_citation: "J. D. Armstrong, M. Lucas, J. Fryer, L. Vila, L. G. Pierce (1988). A combined radio and acoustic transmitter for fixing direction and range of freshwater fish (RAFIX). Journal of Fish Biology 33, 879-884. Marsh Library ID: PML0073."
source_file: "Armstrong et al. 1988. Combined Radio and Acoustic Trans. for Fixing Direction and Range of Freshwater Fish.pdf"
text_extraction: "text"
---
# RAFIX: A Combined Radio-Acoustic Tag for Tracking Freshwater Fish

#ichthyology #marine-biology #esocidae

## Executive Summary

The paper describes **RAFIX**, a combined [[Radio Telemetry]] and [[Acoustic Telemetry]] tag and receiving system for locating freshwater fish. The tag transmits acoustic and radio pulses at the same time. The difference in arrival times at a single receiving station gives the fish's range, and a [[Directional Hydrophone]] gives its bearing. The system was tested on a single [[Northern Pike]] in [[Loch Kinord]]. The authors report that the position estimates matched an independent two-point triangulation. They also report that RAFIX can locate fish from one station with a range error of about 0.1 m once calibrated, and they argue it is more precise than two-directional hydrophone fixes.

## Background & Description

**Tracking context.** Radio tags work only in shallow, low-conductivity fresh water, where signal attenuation between fish and surface is modest. Acoustic tags work in sea or fresh water and at great depth (at least 6500 m is cited), but perform poorly in shallow, fast-flowing water with high background noise and entrained air. The paper reviews the main location methods:

- **[[Triangulation]]** with directional hydrophones or antennae.
- **Time-of-arrival methods** using three receiving stations, best suited to static fish with a home range.
- **[[Transponder Tags]]**, which reply to an interrogating sonar pulse and give range and bearing, but which may be impractical in shallow fresh water because of the bulk of the sonar transducer.
- **[[Synchronous Pingers]]**, which emit pulses from a crystal-controlled oscillator and whose range can be calculated from the time of flight, but whose clocks drift apart after a few hours.
- **Continuous-wave transmitters**, which have limited use because they are not pulsed and battery life is short.

**Tag design.** The transmitter contains a pulse-shaper and timer that trigger both output stages at once. Each pulse is 5 ms long and repeats every 1 s. The acoustic channel runs at 75 kHz. The radio channel operates in the 49.82–49.98 MHz band (the text cites a UK performance specification for this range). The tag is powered by a single 6 V lithium cell and sealed in a polypropylene tube. Reported dimensions are 5.5 × 1.6 cm, with a mass of 26 g in water. A 20 cm nylon-insulated whip antenna projects from the end, and the antenna is matched to the environment when submerged. The stated tag life on one battery is about 30 days. (Parts of the scanned text, including the output power figures, are garbled and are not reproduced here.)

**Receiving system.** Radio pulses were picked up by a loop antenna (48.5 × 48.5 cm), decoded, amplified, and displayed on an oscilloscope. Acoustic pulses were picked up by a directional hydrophone with a 15° beam angle, which allowed bearing to be found by locating the signal maximum. Range was read from the time delay between the radio and acoustic arrivals. Signals could also be recorded on a stereo cassette recorder and displayed later on a digital oscilloscope.

## Ecological & Environmental Context

**Sound speed and its uncertainty.** Radio waves travel at about 3 × 10⁸ m/s, so their travel time is effectively negligible. Sound in water travels at about 1500 m/s, which makes the acoustic delay the basis of the range measurement. Sound speed depends on temperature, salinity, and depth. Temperature is the main factor in shallow fresh water. For the loch, the authors used a value of 1414 m/s from the [[Medwin Sound Speed Equation]], calculated for the loch's temperature. For temperate fresh water, a standard value (about 1481 m/s, for 10 °C at 1 m depth) is said to be adequate, with a maximum error of 2.4% over a 1–20 °C range. For precise work, plankton and trapped air bubbles can alter sound speed, so the authors recommend calibrating the system against a test tag over a known range at each site.

**Environmental limits of acoustic signals.** Acoustic signals are weakened by extensive [[Macrophyte]] growth and by [[Plankton Blooms]], which can attenuate sound rapidly. Radio signals are unaffected by these conditions and can also be used under [[Ice Cover]]. The authors therefore see radio as an advantage over acoustic pingers.

**Frequency choice.** Most fish radio tracking uses frequencies of 100–200 MHz. The authors used 50 MHz, a band in which signal attenuation is lower. They note that the lower frequency needs loop antennae, which are smaller, instead of bulky Yagi antennae. They suggest that long-term fixed-station studies currently using about 173 MHz could benefit from moving to this lower band.

**Regulatory note.** The trials ran under a Test and Development Licence from the UK Department of Trade and Industry. The 49 MHz band is shared with consumer devices such as baby alarms and garage door controllers. The authors anticipate that equipment will need type approval, and they warn that interference from consumer use could affect biotelemetry, though they found no serious problems in rural locations.

## Key Findings

- **Method.** RAFIX gives range and bearing from one receiving station by timing the gap between simultaneous radio and acoustic pulses. It does not need a multi-station array or a clock synchronised to the tag.
- **Field trial.** A single pike (about 55 cm total length) was tagged after anaesthesia with [[Benzocaine]] (0.1 mg/l) and released. The fish was held in a tank overnight first. A stationary 3 m rowing boat served as the tracking station.
- **Behaviour.** The tag did not affect the fish's posture. In the 4 h after release, the pike made several distinct movements and stayed still between them. Positions from RAFIX matched an independent two-point directional triangulation.
- **Escape response.** After being startled, the fish moved away from the receiver. Its maximum swimming speed, averaged over 1 s, was about 2 body lengths per second, or 1.1 m/s.
- **Accuracy.** At 50 m, bearings could be read to within 1°, which corresponds to an uncertainty of about 1.7 m in fish position. Once calibrated, the range error is about 0.1 m. The authors conclude that the area in which a fish is known to lie is smaller than with two-directional hydrophone fixes.
- **Best practice.** For the most accurate positions, the authors recommend taking two or three simultaneous range measurements at roughly 90° to the fish.
- **Advantages over other systems.** RAFIX needs no external clock and no time-consuming recalibration, and it can carry variable telemetry data such as temperature or heart rate, because the radio output signals the exact time of each pulse.
- **Tag options.** An internal ferrite rod aerial could replace the external whip where it is unacceptable, but this increases tag size. Extra batteries extend tag life where size is not critical.
- **Conclusion.** The authors describe RAFIX as a new method for accurately locating fish in fresh water, with clear advantages over the systems then in use for many applications.