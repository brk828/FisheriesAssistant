---
species: "Xyrauchen texanus"
common_name: "Razorback Sucker"
family: "Catostomidae"
habitat: "Riverine backwaters, floodplain wetlands, side channels, and reservoirs (laboratory troughs used as proxy)"
ocean_basin: "N/A (freshwater)"
location: "Green River, Utah; Colorado River basin; Lake Mohave, Arizona-Nevada (referenced)"
tags:
  - ichthyology
  - marine-biology
  - catostomidae
  - light-trap
  - larval-fish
  - razorback-sucker
title: "Factors Influencing Capture and Retention of Razorback Sucker in Light Traps"
source_id: "PML2796"
marsh_id: "PML2796"
library: "Marsh Library"
permission: "not public domain"
source_citation: "C. M. de Vlaming, K. R. Bestgen (2020). Factors Influencing Capture and Retention of Razorback Sucker in Light Traps. North American Journal of Fisheries Management. Marsh Library ID: PML2796."
source_file: "Vlaming and Bestgen. 2020. Razorback Sucker Capture and Retention..pdf"
text_extraction: "text"
---
# Factors Influencing Capture and Retention of Razorback Sucker in Light Traps

#ichthyology #marine-biology #catostomidae

## Executive Summary

This laboratory study tested how environmental and set-up variables affect the capture and retention of early life stages of the endangered [[Razorback Sucker]] in [[Light Trap]]s. The work supports management of [[Flaming Gorge Reservoir]] spring flow releases in the [[Green River]], which are triggered by the first detection of newly emerged larvae. Experiments in six troughs tested five life stages against [[Set Time]], [[Release Distance]], light presence, [[Turbidity]], larval density, cover, and environmental light. Light traps captured and retained larvae well under most conditions. Capture probability was lowest for the earliest protolarvae and for juveniles. The authors recommend overnight sets with a consistently bright light, and retrieval before sunrise.

## Background & Description

The Razorback Sucker is a long-lived, large-bodied catostomid endemic to the [[Colorado River Basin]]. It was federally listed as endangered in 1991. Its populations declined after water development, altered flow and temperature regimes, and competition or predation from more than 65 nonnative fish species. Most wild adults are believed extirpated. Hatchery stocking has re-established many riverine and reservoir populations, but recruitment remains insufficient. Spawning occurs in spring on the ascending limb or peak of the hydrograph. Correctly timed flows carry larvae into warm, food-rich floodplain wetlands that promote growth and survival.

Light traps in backwaters and floodplain wetlands are the main tool for detecting these larvae. Their efficiency, however, had been poorly understood. Attraction distance, the effects of turbidity, and light type and intensity were all unresolved. The study was designed to inform sampling protocols, flow-timing decisions, and an index of annual abundance. Its authors also note that comprehensive tests of light trap variables for fish larvae are rare.

**Study life stages** (per Methods):

| Life stage | Approximate TL |
|---|---|
| Early protolarvae (pre-swim bladder) | 8–10 mm |
| Late protolarvae (post-swim bladder) | 10–11 mm |
| Mesolarvae | 11–17 mm |
| Metalarvae | 18–26 mm |
| Juveniles | 27–50 mm |

Source fish came from [[Ouray National Fish Hatchery]] and were held at the [[Colorado State University]] Aquatic Research Laboratory. Mean starting TL was 10.0 mm (SD = 0.56) for 2017 fish and 8.7 mm (SD = 0.35) for 2018 fish. Fish were held in flow-through troughs at 6–10 mg/L dissolved oxygen and fed brine shrimp and flake food.

## Ecological & Environmental Context

**Experimental conditions**

- Six black steel troughs, each 4.9 m long by 0.45 m wide, filled to 0.29 m depth (about 640 L).
- Water temperature was 16.9–17.4 °C and dissolved oxygen 6–8 mg/L, similar to spring Green River backwaters.
- Traps were a quatrefoil design (modified from Killgore 1994) with 4-mm vertical apertures and 500-µm mesh capture basins. Green chemical light sticks served as the light source.
- Turbidity was set at about 75 NTU, roughly a 9–10 cm Secchi depth. This matches conditions common when larval emergence begins.
- Density treatments were low (25 fish, 0.04 larvae/L) and high (50 fish, 0.08 larvae/L).
- Cover was plastic vegetation or cement block, placed in front of or behind the trap.
- Environmental light was simulated as new-moon night (troughs dark) or sunrise (dark 0.5 h, then laboratory light for 1 h).

**Analysis.** Each trial was an experimental unit analysed by [[Logistic Regression]] (logit link, R 3.x series; type III likelihood ratio tests). Non-overlapping 95% confidence intervals were used as a de facto significance test.

**Context for field use.** Field light traps are typically set overnight, about 8 h, though sets can reach 24 h. Larval [[Cyprinidae]] and [[Catostomidae]] are often collected together and show similar [[Phototaxis]]. The results may therefore inform sampling of related larval taxa, such as [[Northern Pike]] in comparable trap studies.

## Key Findings

**1. Capture probability by life stage (abstract means, with ranges)**

- Early protolarvae: mean 0.40 (range 0.28–0.55) across treatments.
- Late protolarvae: mean 0.76 after swim bladder development.
- Mesolarvae, the most common stage in field samples: mean 0.86 (range 0.80–0.90).
- Metalarvae: mean 0.42 (range 0.21–0.66).
- Juveniles: lower than other stages.
- Capture was relatively high (>0.75) for most commonly sampled stages under standard conditions. The bell-shaped pattern, peaking at late protolarvae and mesolarvae, is attributed to changes in swimming ability and phototactic response.

**2. Set time**

- Capture probability increased with longer sets. At 4 h, mesolarvae and later stages were usually 0.80–0.90, while early protolarvae were about 0.60 and juveniles about 0.50.
- Preliminary tests gave capture rates of 11.2 fish/h at 2 h, 5.7 fish/h at 4 h, and 2.6 fish/h at 8 h. Total captures were similar across set times.
- Differences between 4 h and 8 h were negligible except for juveniles.
- Shorter sets (0.5–2 h) produced lower captures, with the largest deficit for juveniles.

**3. Release distance**

- Distances of 1, 3, and 5 m (trough length was 400–500 times body length) had little effect on capture. At 4 h, differences across distances were only about 0.04–0.15.
- Distance mattered more at short set times and for early protolarvae, metalarvae, and juveniles.
- No upper limit to attraction distance was found. An opportunistic test captured larvae released 3 m away after only 5 min.

**4. Light presence (the largest single effect)**

- Without light, captures were 0.10 or less for all stages except juveniles.
- Light presence and life stage interacted significantly. The light/no-light difference was greatest for mesolarvae.

**5. Retention probability**

- With light present, mean retention was 0.92 (range 0.77–0.98) across life stages and turbidity conditions. Juveniles reached 0.97.
- Without light, mean retention fell to 0.28 (range 0.01–0.14). Early protolarvae retention dropped from 0.39 in clear water to 0.05 in turbid water without light.
- Retention was never 1.0, so larvae appear to move out of and back into traps. Terminal counts may therefore underestimate the total entering a trap.

**6. Turbidity**

- Turbidity effects on capture were stage-specific. Early protolarvae captures fell in turbid water at 5 m, but rose at 1 m.
- Mesolarvae were minimally affected. Metalarvae and juveniles captured more in turbid water, possibly because cover reduces predation risk and increases activity.
- Turbidity did not noticeably affect retention when light was present.

**7. Density and cover**

- Larval density had no detectable effect on capture, supporting the use of trap catches as an abundance index.
- Vegetation or rock placed in front of traps reduced capture for mesolarvae and metalarvae. Cover behind the trap had little effect.
- Juvenile captures were highest with cover behind the trap, but overall cover trials were functionally similar.

**8. Environmental light**

- Retention was lower under simulated sunrise than under night conditions for all stages except juveniles, by 0.03–0.25. This was of concern for the earliest stages.

**9. Recommendations**

- Use 8-h or longer sets, matching typical overnight field practice, with a consistently bright light source.
- End sampling before or at sunrise, and collect trap contents before sun exposure.
- Place traps in open areas away from vegetation or rock. Increase trap density or sampling frequency in turbid water, or where heavy cover exists.
- Juveniles are poorly sampled by light traps. If they are targeted, increase set duration or trap density, or add other gear such as seines.
- Maintain consistent set duration across nights and years for long-term comparisons.
- Light traps are reliable for detecting early life stages of Razorback Sucker, and support earlier findings of [[Snyder and Meismer 1997]] (mesolarvae capture 0.13–0.36 in their study, versus higher capture here).

**10. Management implications**

- Light trap detection supports the [[Larval Trigger Study]] and the timing of spring releases from [[Flaming Gorge Reservoir]].
- Light traps may underestimate later stages and their abundance in the wild. Low juvenile captures are attributed to reduced phototaxis rather than swimming constraints.
- Further studies in larger, natural arenas and with brighter or LED light sources are needed. Limitations include the linear trough shape, which may have biased capture upward.