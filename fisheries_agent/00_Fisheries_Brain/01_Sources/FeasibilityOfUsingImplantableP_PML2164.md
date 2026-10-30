---
species:
  - Oncorhynchus tshawytscha
  - Oncorhynchus nerka
  - Oncorhynchus mykiss
  - Salmo salar
common_name:
  - Chinook salmon
  - Sockeye salmon
  - Steelhead
  - Atlantic salmon
family: Salmonidae
habitat: Freshwater (streams, hatcheries, rivers, fish ladders) and seawater (holding cages); juvenile and adult life stages, including maturing adults
ocean_basin: Pacific (Atlantic salmon used as a test species)
location: Northwest Fisheries Center, Seattle, Washington, USA; Columbia River dams (Lower Granite, McNary); laboratory and hatchery tests
tags:
  - electronic-tagging
  - passive-integrated-transponder
  - fish-tagging
  - salmonid-biology
  - fisheries-research
title: "Feasibility of using Implantable Passive Integrated Transponder (PIT) Tags in Salmonids"
source_id: "PML2164"
marsh_id: "PML2164"
library: "Marsh Library"
permission: "not public domain"
source_citation: "E. F. Prentice, T. A. Flagg, C. S. McCutcheon (1990). Feasibility of using Implantable Passive Integrated Transponder (PIT) Tags in Salmonids. American Fisheries Society Symposium 7:317-332. Marsh Library ID: PML2164."
source_file: "Prentice E.F. et al. 1990. Feasibility of using implantable passive intergrated transponder tags in salmonids.pdf"
text_extraction: "mixed"
---
# Feasibility of Using Implantable Passive Integrated Transponder (PIT) Tags in Salmonids

#ichthyology #marine-biology #salmonidae

## Executive Summary

This paper, by Prentice, Flagg, and McCutcheon of the [[National Marine Fisheries Service]] (NMFS) Northwest Fisheries Center, evaluates the technical and biological feasibility of implanting [[Passive Integrated Transponder Tag]] (PIT) tags in [[Chinook Salmon]], [[Sockeye Salmon]], [[Steelhead]], and [[Atlantic Salmon]]. The tags are small, glass-encapsulated, and energized by an external magnetic field, which lets biologists read individual codes without anesthetizing or handling fish. Across laboratory and field trials, PIT tags did not measurably harm growth, survival, swimming performance, or reproduction, and tag retention was near 100%. The authors conclude that PIT tags are suitable for individual identification of salmonids and propose wider uses, including behavioral and movement studies.

## Background & Description

Marking fish for recognition has a long history, and many tag and mark types have been used. None was fully satisfactory on technical and biological grounds, which motivated NMFS to begin testing [[Passive Integrated Transponder Tag]] technology in 1983.

The tag is 12.0 mm long and 2.1 mm in diameter. It consists of an antenna coil of coated copper wire wound around an [[Integrated Circuit Chip]], sealed in a glass tube. Each tag carries one of about 34 × 10⁹ factory-programmed codes (rendered "34 x loe" in the scan). The identification code has a preamble and a 40-bit code arranged as five 8-bit bytes, each with a parity bit. One reading error per byte can be detected and corrected.

Operating principle:
- The interrogation system transmits alternating current at 400 kHz through a tuned loop, creating a magnetic field.
- A tag entering the field for as little as 25 ms receives induced current that powers its circuit.
- The circuit divides the fundamental frequency by 8 and 10, returning a signal at 40 to 50 kHz (mark-space coding).
- The interrogator filters out the excitation signal, decodes the tag signal, and converts it to ASCII hexadecimal characters for transfer to a computer via an RS232 port or storage in internal memory.
- Data transfer rate is 4,000 bits/s.

Two interrogation configurations are described: a [[Portable Tag Interrogation System]] and a [[Fixed Tag Monitor System]].

## Ecological & Environmental Context

**Reading performance.** Detection range depends on equipment: up to 7.6 cm for hand-held interrogators and about 18 cm for fixed full-loop interrogators. Tags read easily through soft and hard tissue, seawater, fresh water, glass, and plastic, and with difficulty through metal. Extreme temperatures from −90 to 60 °C did not appreciably affect detection. Tags remained readable at movement speeds up to 3.6 m/s. The expected operational life is 10 years or more because the tag is passive and needs no battery.

**Regulatory context.** Operators need no special permits beyond the [[Federal Communications Commission]] requirements for low-power transmitting devices in the USA, or their equivalents elsewhere. Permanent monitoring installations, such as those at hydroelectric dams, fall under stricter requirements. The hand-held interrogator is already FCC-certified.

**Biological suitability criteria.** The authors state that a fish tag should not alter growth, survival, behavior, or reproduction, should be retained, and should have a long functional life. Test fish ranged in fork length from about 55 mm to over 800 mm. Tags were injected into the body cavity with a modified hypodermic syringe and 12-gauge needle.

**Field settings.** Studies drew on fish passing [[Lower Granite Dam]] and [[McNary Dam]] on the [[Columbia River]], and on hatchery stocks. Tagged fish were held in freshwater, transferred to seawater cages, or held in tanks supplied with well water or stream water.

## Key Findings

**1. Tag retention and longevity (fall chinook, 1986–1987).**
- Two groups of 300 juvenile fall chinook salmon, one tagged and one control, were held in fresh water until smoltification and then in seawater cages.
- After 570 days, tag operation was 100%, and tag retention was reported as high (the value is garbled in the scan).
- Growth of tagged fish was slightly depressed relative to controls.
- Through day 409, survival was 89.7% (control) and 86.7% (tagged), respectively.
- After day 409, comparisons were confounded by many precocious males in the control group, which suffered high mortality.
- At 570 days, survival was 36.4% for controls and 76.5% for tagged fish.

**2. Minimum tagging size (juvenile fall chinook, 1986).**
- About 200 fish in each of four size groups, ranging from 56 to 120 mm fork length, were tagged and held separately.
- Two water sources were tested: well water and stream water, the latter containing fish pathogens.
- Tag retention was 99–100% for all groups, and most tag-related wound healing occurred within 14 days, regardless of water source.
- Survival was 97.0–100% in well water and up to 98.0% in stream water groups. No association between survival and water source or tag presence was found.

**3. Juvenile sockeye and chinook growth and survival.**
- Two fingerling sizes and one smolt group were tested. Lengths at tagging ranged from 55 to 107 mm.
- Each group had untagged controls and tagged fish.
- Survival was at least 96.5% in control and tagged groups, and no difference was found at 14 days.
- The authors state that the PIT tag does not compromise growth or survival of juvenile salmonids.

**4. Survival at 14 days (Columbia River trials).**
- Survival was compared among five treatments (control, PIT-tagged, coded-wire-tagged, coded-wire plus PIT, and freeze-branded) for yearling chinook, steelhead, and age-0 chinook at Lower Granite (1986) and McNary (1985–1986) dams.
- Fish were combined in holding cages after tagging and checked daily.
- Survival in tagged groups did not differ meaningfully from controls. Table values are partly garbled in the scan.

**5. Wound healing and tissue response (fall chinook, 3.7 g average, 10 °C well water).**
- Ten fish were sampled histologically from a population of 161 on days 22, 30, and 45.
- By day 22, granulation tissue had replaced damaged dermis and muscle. By days 30 and 45, the injection site was hard to locate and healing was complete.
- Visual checks showed wounds closed by day 14, and complete healing within 2 weeks.
- No host reaction, melanomacrophage accumulation, or adhesions were observed, indicating the glass-encapsulated tag is biologically inert.
- Tags were found mostly near the abdominal musculature posterior to the pyloric caeca and close to the spleen. Some were embedded in nearby tissue, and in a few cases the authors saw preliminary signs of encapsulation.
- Tag retention was 100% in this study.

**6. Swimming performance (726 juvenile chinook, plus steelhead and age-0 chinook).**
- Tests used a modified [[Blazka Respirometer]] stamina chamber, with videotaped analysis of stamina, tail-beat rate, and respiratory rate.
- Neither the surgery nor the tag affected swimming stamina, stride efficiency, or respiratory rate.
- Post-test survival (14 days) was unaffected, and tag retention was 100%.
- No adverse tissue reactions or tag migration were found.
- The authors conclude that the tag should not compromise swimming during downstream migration.

**7. Maturing Atlantic salmon.**
- Trials used 21 male and 60 female maturing Atlantic salmon, weighing 2,500 to 10,000 g and measuring 61 to 80 cm.
- All tag wounds were closed and healing by day 3, with no infection.
- All 21 males matured, and tag retention was 100%.
- Forty-eight females were spawned. Tag retention was 83% in spawned females and 100% in nonspawners (value partly garbled in scan).
- Four tags passed during the first egg stripping, and four more during strippings two through four. Passed tags were easily seen among the eggs.
- Tags did not appear to affect egg quality or survival.

**8. Future applications.**
- The authors describe the PIT tag as the first generation of computer-age identification systems. Prawns and crabs have also been tagged, and the tag could suit any animal that can accept and retain it.
- Proposed uses include individual identification of broodstock, serial growth measurements on the same animals (reducing replicate numbers), combining treatments, behavioral studies, and automated or [[Capture-Recapture]] movement monitoring.
- Pelagic animals might be monitored with trawl nets carrying PIT detectors in an open cod-end or a purse seine. Benthic animals might be followed with a grid system or underwater sled.

**9. Funding.** The project was supported by electrical ratepayers through the [[Bonneville Power Administration]].