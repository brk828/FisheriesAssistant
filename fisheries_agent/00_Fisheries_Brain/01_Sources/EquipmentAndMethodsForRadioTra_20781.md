---
species:
  - Micropterus salmoides
  - Salmo gairdneri
  - Perca flavescens
  - Oncorhynchus tshawytscha
  - Esox lucius
  - Cyprinus carpio
  - Salmo clarki
  - Acipenser transmontanus
  - Pylodictis olivaris
common_name: "Largemouth Bass, Steelhead, Yellow Perch, Chinook Salmon, Northern Pike, Common Carp, Cutthroat Trout, White Sturgeon, Flathead Catfish"
family: "Centrarchidae, Salmonidae, Percidae, Esocidae, Cyprinidae, Acipenseridae, Ictaluridae"
habitat: "Freshwater lakes, rivers, streams, thermal effluent plumes, and reservoirs near dams"
ocean_basin: "N/A"
location: "Minnesota (Cedar Creek, Lake Bemidji, Mary Lake, Lake Superior); Snake River, Washington; Yellowstone Lake (cited)"
tags:
  - ichthyology
  - telemetry
  - freshwater-fish
  - radio-tracking
  - methods
title: "Equipment and methods for radio tracking freshwater fish"
source_id: "20781"
minckley_id: "20781"
source_citation: "J. D. Winter, V. B. Kuechle, D. B. Siniff and J. R. Tester (1978). Equipment and methods for radio tracking freshwater fish. Miscellaneous Report:Agricultural Experiment Station, University of Minnesota. Minckley Library ID: 20781."
source_file: "20781.pdf"
text_extraction: "ocr"
---
# Equipment and Methods for Radio Tracking Freshwater Fish

#ichthyology #marine-biology #salmonidae

## Executive Summary

This University of Minnesota Agricultural Experiment Station Miscellaneous Report (152-1978), by J.D. Winter, V.B. Kuechle, D.B. Siniff and J.R. Tester, is a practical guide for fisheries biologists who want to start [[Radio Telemetry]] programs for freshwater fish. It covers the history of aquatic tracking, the design and cost of underwater radio transmitters, receivers and antennas, field tracking methods (shore, tower, boat and airplane), accuracy tests, and techniques for attaching transmitters to fish. The authors argue that radio tracking is cheaper, allows many individuals to be tracked at once, and is more practical for freshwater work than [[Ultrasonic Telemetry]], while acknowledging its limits in saline or deep water.

## Background & Description

Aquatic animal tracking began in the late 1950s with [[Ultrasonic Telemetry]] at 30–300 kHz, because low-frequency signals travel well through water. Terrestrial ecologists were developing radio transmitters at 27–300 MHz at the same time. The Cedar Creek Bioelectronics Laboratory at the University of Minnesota began radio tracking fish in 1969, first with carp and northern pike in a stream, then with [[Largemouth Bass]] in a northern Minnesota lake. Later projects included [[Steelhead]] in [[Lake Superior]], [[Yellow Perch]] in a power-plant thermal plume, and [[Chinook Salmon]] near hydroelectric dams on the Snake River.

The authors list the main advantages of underwater radio telemetry:

- **Cost:** A high-quality receiver costs under $1000 (U.S.), a yagi antenna about $50, transmitter parts about $20, and an assembled transmitter under $100.
- **Battery life:** Low current drain gives long operation.
- **No water contact:** Tagged fish can be located from shore, boat or aircraft.
- **Many individuals:** Each crystal-controlled transmitter has its own frequency. Simple decoding distinguishes over 100 radio tags, compared with about 10–20 ultrasonic tags.
- **Less interference:** Aquatic vegetation, thermoclines and hydrophone fouling by algae or bubbles affect radio signals less.
- **Versatility:** The same receivers and antennas serve aquatic and terrestrial animals.

The stated limitations are that radio signals attenuate with conductivity and depth, so the method suits freshwater or animals that surface regularly. Radio signals can also be deflected by large metal objects, terrain and vegetation. Both systems are subject to interference from powerlines, unshielded ignition systems and citizen's band radio.

## Ecological & Environmental Context

Signal behaviour depends on water chemistry and depth. Tests were run in two lakes: [[Lake Superior]] (about 80 µmho/cm conductivity) and [[Lake Bemidji]] (about 300 µmho/cm). Signal range fell by 50 percent at 8 m depth in Lake Superior, though the signal was still received at 50 m. In Lake Bemidji, half the signal was lost at 4 m. Attenuation was exponential with depth and greater in higher-conductivity water. A [[Thermocline]] or ice cover had little effect on the signal in the authors' tracking observations.

The authors chose 53 MHz because it appeared to penetrate water better than higher VHF frequencies. A winter lake comparison supported this: 53 MHz signals attenuated less than 164 MHz signals (Figure 3, 70 µmho/cm water).

Fish behaviour also shaped the methods. Long-term tracking of [[Largemouth Bass]] used grid systems around home ranges, with markers 6 m apart on shore and 15 m offshore. Salmon and steelhead tracking involved fish that moved long distances, which favoured mobile and airborne receivers.

## Key Findings

### Transmitter design and performance
- Transmitters used a squegging circuit that produces a pulsing signal. Pulse width was 0.02–0.025 s, pulse rate 60–120 pulses per minute, and duty cycle 3% ± 1%. Pulse spacing can encode temperature or depth, which allowed physiological and environmental telemetry in free-ranging fish (Tester and Siniff 1976).
- Power came from certified [[Mercury Cell Battery]] cells (1.4 V) or [[Lithium Battery]] cells (2.8 V). Lithium cells weigh about half as much in water and perform better in cold water, but the smallest available cell (14 × 23 mm, 4.3 g in air) was too bulky for small fish.
- Life estimates: a 0.5 mA transmitter on a 42 mAh RM-1 cell lasts about 3 months. Larger RM-1 cells (1000 mAh) at 0.5–0.7 mA gave expected and observed lives of 60–83 days. The smallest perch transmitters (160 mAh RM-675, 0.2 mA) lasted 30 ± 5 days. Higher current drain gave a non-linear gain in range but a nearly linear loss of battery life.
- Weight guideline: transmitter weight in water should not exceed 1–1.25% of the fish's weight out of water, so the fish regains equilibrium within minutes.

**Example packages**
- Yellow perch (up to 300 g fish): 30 × 10 × 5 mm, 3.3 g in water (6.5 g dry).
- Steelhead: 17 mm diameter × 40 mm, 15.6 g in water (26.0 g dry).

Transmitters were encapsulated in Scotchcast #5 two-part epoxy, which was durable and compatible with the components.

### Receivers
- The first receiver was a modified automobile radio costing about $125, which could distinguish up to 30 individuals spaced 33 kHz apart.
- The later frequency-synthesizer receiver has a sensitivity of −143 dBm, an IF bandwidth of 1.2 kHz, a noise figure of about 4 dB, and weighs 1.8 kg. It distinguishes over 100 frequencies spaced 5–10 kHz apart, with 1 kHz channel selection.
- A memory option stores up to 64 channels, which can be scanned automatically. It is useful for airplane searches and for unattended logging of temperature or pressure tags.

### Signal range and antennas
- Maximum ranges in 80–300 µmho/cm water were: loop antenna 0.8–1.2 km; yagi antenna 2.4–3.6 km; loop antenna on airplane 4.5 km.
- A yagi gave up to three times the range of a loop. A mobile unit with a yagi gave 2–3 times the range of a loop.
- Signals were 35–45% weaker when the transmitter antenna was broadside to the receiver, so the transmitter antenna was kept horizontal and pointed at the receiver.

### Tracking methods
- **Hand-held loop (shore):** Used the null for bearings. Usable in storms and at night, and does not disturb fish.
- **Temporary tower:** Useful on small lakes and near thermal effluents or dams. Pairs of towers allowed simultaneous fixes. Towers could log signal presence, activity and temperature.
- **Mobile vehicle:** A van with a yagi on a rotatable mast was built for [[Lake Superior]] work, where frequent stops made tip-up mounts too slow.
- **Boat:** A yagi on a 4 m telescopic mast in a 5.5 m boat was effective for searching small areas. A loop antenna was used for final localisation, and the fish was within about 20 m when the signal became omnidirectional.
- **Airplane:** Useful for large lakes (>125–250 km²) and nomadic species. Loops were mounted under each wing. Average range as a percentage of maximum was 60% at 150 m altitude, 75% at 300 m, 75% at 450 m, 93% at 600 m and 100% at 750 m. Accuracy was about 100 m radius with landmarks 1–3 km away. Aircraft speed (>96 km/h) left little time per frequency, and rental cost limited use.

### Accuracy
- **Yagi (tower tests):** Bearings were close together (S.E. < 0.45°), with systematic tower errors corrected to within ±3°. Distance errors were under 5 m at 100 m and 43 m at 800 m after correction. Van-mounted yagi mean errors were about 14 m at 200 m and 28 m at 400 m.
- **Loop (football-field tests):** Mean bearing error ranged from 0.3 m (5–15 m class) to 4.81 m (76–92 m class). Calculated maximum triangulation error ranged from 2.1 m to 10.7 m, and mean triangulation error from 0.79 m to 6.49 m.
- **Antenna reversal:** Detected at 4.6 m, complete at 2.7 m at 53 MHz. The smallest distance class in the accuracy study was therefore set at 5–15 m.
- Triangulation is most accurate when bearing lines intersect at 90°, so trackers should move to positions that give near-perpendicular bearings.
- Sextant bearings (Mark II) were accurate to ±0.5° and less affected by rough water or metal than compass bearings.

### Attachment methods
No single method suits all species. Choice depends on morphology, behaviour, habitat and project goals.
- **External:** Faster and easier, and suited to spawning and feeding fish. Risks include skin erosion, possible fungal infection, snagging and drag.
- **Sub-dorsal fin mount:** Used for fish with long dorsal fins (e.g. Centrarchidae, Percidae). Two teflon-coated ground-plane wires pass under the fin, with a soft plastic washer on the other side.
- **Mid-dorsal saddle:** Used for most salmonids (1.5–5.0 kg). A 16 × 45 mm plastic saddle is potted to the transmitter and threaded under the skin of the back.
- **Surgical implantation:** Internal tags are less subject to drag or snagging and suit long-term and physiological work. Surgery takes longer, carries more infection risk, and recovery is slower. Tests showed about 10% signal absorption by the fish's body.
- **Stomach insertion:** Quick, with the shortest habituation time, but transmitters may be regurgitated and insertion can rupture the oesophagus. Haynes (1978) found greater mortality for stomach-tagged salmon tagged far upstream and suggested the posterior oesophagus for spawning fish.
- A whip antenna should not extend beyond the caudal fin.

### Cost and budget notes
- Transmitter parts cost about $20 (U.S.).
- The receiver parts cost about $125 for the early model.
- Custom mercury cells outside the common RM-1 and RM-640 sizes were costly unless ordered in quantities above 1000.

### Funding and sources
The research was supported by the U.S. Energy Research and Development Administration, the Minnesota Department of Natural Resources (with U.S. Fish and Wildlife Service funds under the Anadromous Fish Act), and the U.S. Environmental Protection Agency. The reference list contains about 40 works, including [[Cochran and Lord 1963]] on radio-tracking systems and Marshall (1960–1963) on short-wave transmitters. The appendix gives receiver specifications and a front-panel control guide for the memory receiver.