---
species: N/A
common_name: N/A
family: N/A
habitat: Natural streams and rivers (non-tidal freshwater)
ocean_basin: N/A
location: Theoretical model; example conditions from Austria (southern Alps); references to central and western European rivers, the Nile, and the Mississippi
tags: [limnology, hydrometeorology, stream-temperature, heat-balance, diurnal-cycle]
title: "On the diurnal heat balance and temperature cycle of natural streams"
source_id: "20944"
minckley_id: "20944"
source_citation: "J. Zimmerman (1974). On the diurnal heat balance and temperature cycle of natural streams. Meteorology and Atmospheric Physics 23(3): 349-370. Minckley Library ID: 20944."
source_file: "20944.pdf"
text_extraction: "ocr"
---
# Diurnal Heat Balance and Temperature Cycle of Natural Streams

#limnology #hydrometeorology #stream-temperature #heat-balance

## Executive Summary

This is a theoretical micrometeorological study by J. T. F. Zimmerman (Institute of Earth Sciences, Free University, Amsterdam), published in *Archiv für Meteorologie, Geophysik und Bioklimatologie*, Series A, 1974. It develops an analytical model of the daily temperature cycle of natural streams, driven by the [[Heat Balance Equation]]. The model defines an equilibrium state, reached far downstream from the source, characterised by a daily mean temperature, a daily amplitude and a time lag relative to the net heat flux. Upstream of that point, these properties vary with distance from the source. The analytical results agree well with the earlier numerical work of [[Eckel and Reuter]]. A Fourier expansion of the solar input reproduces the asymmetric shape of the observed temperature curve, which a first-order sinusoidal model cannot capture. A companion paper by [[Böhm]] (German, with English summary) presents a related numerical method for river water temperature that includes the effect of the natural horizon.

## Background & Description

The paper addresses a gap in stream thermal theory. Human activity increasingly alters natural water temperatures, which in turn affects physical, chemical and biological processes, so the heat balance of streams needs quantitative treatment, particularly under disturbed conditions.

**Literature context:**
- [[Guppy]] (1894) compiled observations showing that vertical temperature differences in rivers are usually very small because of intensive turbulent mixing. The daily minimum occurs at sunrise, and the summer maximum falls between 15h and 18h, later in deeper rivers.
- [[Forster]] (1894) documented annual thermal cycles of many rivers in central and western Europe.
- [[Eckel and Reuter]] (1950) provided the first quantitative treatment. They integrated the heat balance numerically for a hypothetical river with a given spring temperature (in their Fig. 1 example, 5°C at a 30 cm depth) under summer conditions in Austria.
- [[Kuhn]] (1972) attempted an analytical derivation, but did not distinguish local from individual (advected) temperature derivatives and omitted bottom heat flow. The present paper addresses both points.

**Governing equation:** For a well-mixed water column of depth h, the rate of temperature change is dT_w/dt = Q/(h ρ c), where Q is the net heat flux through the top and bottom surfaces, ρ is water density and c its specific heat.

**Heat flux components** (Q = Q_s + Q_l + Q_h + Q_e + Q_b + Q_m + Q_v):
- Absorbed [[Solar Radiation]] (Q_s), approximated as a half-sine between sunrise and sunset, with a Fourier-series form based on [[Milankovitch]] (1930).
- Net [[Long-Wave Radiation]] (Q_l), using the [[Brunt Relation]] for atmospheric emission and the Stefan–Boltzmann law for water emission (emissivity 0.97).
- Sensible heat conduction (Q_h) and latent heat flux (Q_e), using bulk transfer with a wind-speed-dependent coefficient and the [[Clausius-Clapeyron Relation]].
- [[Bottom Heat Flux]] (Q_b), modelled by conduction into the streambed, with the bed temperature set equal to the overlying water temperature at the interface.
- Lateral and longitudinal mixing (Q_m), restricted to localised inflows such as tributaries and groundwater.
- [[Viscous Dissipation]] (Q_v), which Vugts (cited) showed can be important in small streams. For a constant mean velocity, a 50 m fall corresponds to a 0.1°C gain if energy is conserved.

## Ecological & Environmental Context

The paper is a physical model and contains no biological data. Its environmental relevance lies in three areas:

- **Thermal regime of rivers:** Water temperature governs many physical, chemical and biological processes. The model links stream temperature to meteorology (air temperature, humidity, wind, cloud-influenced radiation) and to streambed properties.
- **Equilibrium versus non-equilibrium reaches:** Downstream of the source, the daily mean temperature approaches an equilibrium value. In some systems this may never be reached. Zimmerman notes that rivers flowing roughly north–south, perpendicular to climatic gradients, may have an equilibrium temperature that keeps changing. [[Guppy]] (1894) suggested this may apply to the [[Nile River]] and [[Mississippi River]].
- **Climate contrast:** Guppy (1894) found that daily mean temperatures of lowland European rivers lie above air temperature, whereas arid-region rivers such as the Nile generally fall below it. Zimmerman attributes this to differences in the surface energy partitioning between land and water, particularly evaporation, in arid areas.
- **Small mountain streams:** Bottom heat flux and viscous dissipation are important in small streams over conductive beds, as shown by [[Vugts]] and [[Brown]] (1969).

## Key Findings

**1. Equilibrium state.** For given external parameters, the model defines an equilibrium daily mean temperature, amplitude and time lag. Far downstream, the daily mean temperature is T_eq = Q_mean/k, where k is the exchange coefficient (k = 33.3 W m⁻² K⁻¹ in the numerical example).

**2. Numerical example.** The example uses conditions similar to those of [[Eckel and Reuter]] and [[Vugts]] for a clear summer day in the southern Alps. The equilibrium daily mean (Q/k = 22.7°C) lies above the assumed mean air temperature at observation level (21.5°C). Zimmerman states that the value depends on the chosen parameters, but that positive water–air differences in humid areas are typical.

**3. Relaxation distance.** Downstream of the source, the difference between the daily mean water temperature and its equilibrium value decays exponentially with dimensionless distance. The relaxation time is τ_r = h ρ c / k. Table 1 gives relaxation distances of about 122 km to 1952 km across the tabulated depths. The shape of the decay makes deep rivers adjust slowly, and this effect is most important for north–south or south–north flow.

**4. Equilibrium amplitude (Table 2).** The amplitude of the daily cycle decreases with depth. Bottom heat flux damps the cycle, with the effect largest in shallow streams.

| Depth (cm) | 30 | 60 | 120 | 240 | 480 |
|---|---|---|---|---|---|
| Amplitude, no bottom flux (°C) | 2.9 | 1.5 | 0.8 | 0.4 | 0.2 |
| Amplitude, bottom b = 23.8 W m⁻² K⁻¹ (°C) | 2.2 | 1.3 | 0.7 | 0.4 | 0.2 |

**5. Time lag (Table 3).** The equilibrium time lag of water temperature behind the periodic heat flux is about 4 h 42 min at 30 cm without bottom flux, rising to about 5 h 56 min at 480 cm. A conductive bed shortens the lag slightly, most noticeably in shallow streams (about 4 h 15 min at 30 cm). Zimmerman notes that the lag approaches the limit arctan(1/m) for deep water.

**6. Damped oscillation with distance.** The amplitude function f(x′) and phase function η(x′) both oscillate with decreasing amplitude as distance increases. Their first extrema correspond to water parcels that have travelled about half a day and about a full day. The bottom heat flux increases damping by reducing the relaxation time.

**7. Local versus individual temperature.** Local and advected (Lagrangian) temperature histories coincide only in the equilibrium state. Upstream, advection causes them to diverge.

**8. Non-sinusoidal daily cycle.** A first-order sinusoidal model cannot reproduce the observed asymmetry. Using a Fourier series for solar input (truncated at the eighth harmonic), the model shows:
- The daily maximum occurs later in the afternoon and the minimum occurs later in the morning than in first-order theory.
- The temperature rises quickly in the morning and falls slowly through the afternoon and night, producing a marked tail.
- The daily maximum is underestimated by first-order theory because of reduced peak solar input, even though daily mean solar input is the same.

Predictions for the 1.5 h and 3 h travel-time points agree well with [[Vugts]].

**9. Heat budget.** Daily mean terms (Table 4) show that absorbed solar radiation is mainly balanced by net outgoing long-wave radiation and evaporation in the equilibrium state. Near a cool source, conduction becomes dominant and evaporation and long-wave exchange are reduced.

**10. Companion study.** [[Böhm]] (1974) simplifies the formulas for direct and scattered radiation, long-wave exchange and convective heat exchange, and makes the equations numerically integrable. The paper includes the effect of the natural horizon on river temperatures and the sky-view term, and applies the method to a clear summer day in Austria.