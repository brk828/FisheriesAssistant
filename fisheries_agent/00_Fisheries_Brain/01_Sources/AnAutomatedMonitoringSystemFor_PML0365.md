---
species: "Salmo gairdneri"
common_name: "Rainbow trout"
family: N/A
habitat: "Freshwater laboratory exposure systems (respirometer-metabolism chambers)"
ocean_basin: N/A
location: "U.S. EPA Environmental Research Laboratory, Duluth, MN"
tags: [ichthyology, marine-biology, salmo-gairdneri, toxicology, automated-monitoring, fish-acute-toxicity-syndromes]
title: "An Automated Monitoring System for Fish Physiology and Toxicology"
source_id: "PML0365"
marsh_id: "PML0365"
library: "Marsh Library"
permission: "public domain"
source_citation: "R. W. Carlson, G. J. Lien, B. A. Holman (1989). An Automated Monitoring System for Fish Physiology and Toxicology. U.S. EPA Environmental Research Laboratory, Duluth, MN, EPA/600/S3-89/011 (Project Summary). Marsh Library ID: PML0365."
source_file: "Carlson R.W 1989. An automated monitoring system for fish phsiology and toxicology.pdf"
text_extraction: "mixed"
---
# An Automated Monitoring System for Fish Physiology and Toxicology

#ichthyology #marine-biology #salmo-gairdneri

## Executive Summary

This EPA Project Summary (EPA/600/S3-89/01, August 1989) describes a [[Data Acquisition And Control System]] (DAC) built to automate physiological measurements and sample control in [[Rainbow Trout]] (*Salmo gairdneri*) exposed to lethal concentrations of toxicants. A microcomputer running menu-driven software, written in an extended BASIC, was linked to sensors and control devices through a custom interface module. The system measured water temperature, ventilation volume, dissolved oxygen (DO) and pH of inspired and expired water, and calculated [[Oxygen Uptake Efficiency]] and [[Oxygen Consumption]] for four fish at once. Manual measurements covered ventilation and cough frequency, the electrocardiogram, and arterial blood chemistry. The data were used to define [[Fish Acute Toxicity Syndromes]] (FATS) for specific modes of toxic action.

## Background & Description

**Fish Acute Toxicity Syndromes.** FATS are collections of direct and indirect clinical signs, based on respiratory-cardiovascular responses in rainbow trout, that are unique to a common mode of action. Syndromes had been defined for narcotics, oxidative phosphorylation [[Uncouplers]], [[Acetylcholinesterase Inhibitors]], respiratory membrane irritants, and the pyrethroid insecticide [[Fenvalerate]].

**Limitations of manual testing.** FATS testing required data on 11 respiratory-cardiovascular variables. Manual monitoring needed at least three full-time people, plus part-time help, during a seven-hour control period and up to 18 h of the acutely lethal exposure. Only two fish could be prepared and tested at a time, so two tests were needed to gather data on four fish.

**Project objectives.** The goal was an automated system that could:
- collect data on at least four fish at predetermined intervals, including unattended periods;
- allow sampling and measurement regimes to be changed during a test;
- be built from commercially available sensors, control valves, a personal computer, a custom interface, and menu-driven software.

**Test subjects.** Rainbow trout weighing 0.6 to 1.0 kg were exposed to a lethal concentration of an organic chemical. Fish were spinally transected and fitted with a latex rubber membrane separating expired from incoming water, a dorsal aortic cannula for blood sampling, copper wire electrodes for the electrocardiogram (EKG), and a urinary catheter.

**Subsystems.** The design had five parts:
1. Exposure apparatus for water and toxicant delivery, adapted from [[McKim And Goeden]] (1982) and enclosed in a vented enclosure to limit human exposure.
2. Automated sampling and measurement circuits.
3. Non-automated monitoring devices for functions that could not yet be automated.
4. A microcomputer that controlled automated monitoring.
5. An interface providing connections and switching between the computer and external devices.

**Respirometer-metabolism chambers.** Four [[Respirometer-Metabolism Chamber]] units were modified so that overflow from the A (exposure water) and B (expired water) compartments reached flow-measuring devices. Water was drawn to the sensing electrodes without aeration. Ventilation was monitored with non-contact stainless steel wire electrodes in the B and C compartments.

**Interface and power.** The interface read analog signals from DO, pH, temperature and flow-pressure transducers, and controlled solenoids, motors, toxicant pumps and the urine fraction collector. The internal supply gave +12, +15 and -15 V DC. External supplies provided +5, -5 and +24 V DC.

**Computer and software.** The system ran on an IBM PC AT specially manufactured for Analog Devices, under the Concurrent CPM-86 multitasking operating system. The in-house program "TEST" contained 1083 lines of source code, required 55 KB of memory for the source or 48 KB for compiled object code, and consisted of a main program, a timing task and an interrupt task running concurrently, and 25 subroutines.

## Ecological & Environmental Context

The study is laboratory-based. Its ecological relevance lies in how toxicants disturb the respiratory and cardiovascular function of fish, and in how those disturbances indicate the mode of toxic action. Every test used freshwater, and the system tracked pH, DO, temperature and flow of both inspired and expired water. Oxygen uptake efficiency, which depends on the difference in DO between the two waters, was a key indicator of gill function. Sampling was timed so that inspired and expired water were taken as close together in time as possible.

The [[Environmental Research Laboratory]] in Duluth, Minnesota, developed the system. The project fits into EPA's wider effort to link chemical exposure with specific physiological effects. Specialized FATS testing reduces the need for animal use, since more data come from each fish.

## Key Findings

**Test history.** By the report date, 17 tests involving 68 fish had been completed. These comprised three freshwater control runs, two control tests on a carrier solvent used to dissolve some test chemicals, and 13 tests with organic chemicals used to describe FATS.

**Performance and validation.** The system performed as designed, despite sporadic electronic malfunctions and sensor calibration problems in some tests. The first chemical tested automatically, [[2,4-Dinitrophenol]] (an uncoupler), gave results consistent with manual testing. This confirmed that the system was suitable for FATS testing and that the responses used to define FATS were reproducible.

**Main advantages.**
- Four fish could be monitored at once for cardiorespiratory responses.
- Ventilation volume and DO measurements became effortless, so more than two fish could be tested per run.
- The number of FATS tests possible in the same time frame at least doubled.
- Round-the-clock monitoring increased the number of measurements of ventilation volume, oxygen uptake efficiency and oxygen consumption, and made data gaps during critical periods less likely.

**Real-time decision-making.** Real-time data allowed experimenters to judge how a test was progressing. Narcotic chemicals produce reversible effects, even near apparent death (respiratory arrest), whereas chemicals with specific modes of action cause irreversible effects. By following ventilation volume, oxygen consumption, locomotor activity and the EKG on the printout, fish could be revived with toxicant-free water at various stages of intoxication, and recovery monitored to test whether a chemical was [[Narcosis|narcotic]].

**Conclusions from the report.**
1. Automated monitoring of respiratory-cardiovascular variables saved considerable time and effort compared with manual data gathering.
2. Continuous data collection during unattended operation ensured that data were captured during critical changes.
3. Real-time sampling and calculation of vital signs allowed judgments about the course of an experiment.
4. Automation allowed faster data collection at shorter intervals than manual methods. More samples gave greater statistical reliability.
5. Data were stored immediately in computer files, making them easy to manipulate and transfer between computers.
6. Less manual sampling reduced human exposure to potentially hazardous chemicals.

**Project documentation.** The full report, "An Automated Monitoring System for Fish Physiology and Toxicology" (NTIS order no. PB 89-155 212/AS, $15.95 subject to change), is available from the National Technical Information Service in Springfield, Virginia. The authors were Richard W. Carlson, Gregory J. Lien and Bruce A. Holman of the Environmental Research Laboratory. The report was distributed by the Center for Environmental Research Information in Cincinnati, Ohio.