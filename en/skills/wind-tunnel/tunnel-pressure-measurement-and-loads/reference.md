# Reference — pressure measurement and loads in the wind tunnel (ASCE/SEI 49-21)

Source: ASCE/SEI 49-21, §1.1–§1.2, §3.1, §3.3–§3.4, §6, §8 and the related commentary sections. Page = PDF page order.

Type column: **MANDATORY** = "shall" in the standard text; **MANDATORY (permitted)** = "shall be permitted"; **COMMENTARY** = commentary (not binding); **COMMENTARY (recommendation)** = "should / recommended" in the commentary.

## Standard text — scope and report

| Section (§) | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| 1.1 | scope | The standard gives the minimum requirements for tunnel testing for MWFRS and components and cladding (C&C) wind loads; it satisfies the tunnel testing requirements of ASCE 7-16. | — | 16 |
| 1.2 | MANDATORY | The report documents the test setup, the method and the results; it must be auditable, and the reviewing party must be able to understand all methods, assumptions and results. The content is included in the report or is documented and made available promptly on request. | — | 16 |
| 1.2 (1) | MANDATORY | Setup, purpose and method: scale similarity parameters (length, velocity, time); target terrain and proximity; measurement technique; other basic features of the setup. | — | 16 |
| 1.2 (2) | MANDATORY | For each direction, simulated and target velocity profile, turbulence intensity profile, spectrum and length scale. | — | 16 |
| 1.2 (3) | MANDATORY | Climate analysis: basic climate characteristics, data sets used, the statistical method that combines the climate data with the aerodynamic results. | — | 16 |
| 1.2 (4) | MANDATORY | The type and format of the results are determined by the agreement between the party commissioning the test and the laboratory. | — | 16 |
| 1.2 (5) | MANDATORY | Uncertainty is quantified: test process and techniques, structural property assumptions, climate data, instruments, approach flow and other sources. | — | 16 |
| 1.2 | MANDATORY | Load, pressure and reference velocity time series are retained for future reference and quality control. | — | 16 |
| 1.2 | MANDATORY | Justification in the report for test conditions that deviate from the standard. | — | 16 |

## Standard text — measurement

| Section (§) | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| 3.1 | scope | Chapter 3: mean, time-varying and peak aerodynamic load coefficients on a rigid structure. | — | 22 |
| 3.3 | MANDATORY | The reference velocity is measured at a location where the influence of the proximity model is minimal; it is related to the target mean velocity profile in the test section. | — | 22 |
| 3.3 | MANDATORY | The location of the reference velocity and the measurement parameters used in analysis/presentation are documented in the report; if the results are given relative to another location, the conversion information as well. | — | 22 |
| 3.4 | MANDATORY | Instruments are calibrated before the test and, if necessary, during and after it. | — | 22 |
| 3.4 | MANDATORY | The sampling rate and duration are chosen so as to give data suitable for the intended analysis method (see §8.1). | No number given (for duration see §8.2) | 22 |
| 3.4 | MANDATORY | Hardware with a frequency response sufficient to capture peak and time-varying quantities is used. | see §8.1 | 22 |
| 3.4 | MANDATORY | Drift observed in the mean measurements during the test is corrected. | — | 22 |
| 3.4.1 | MANDATORY (permitted) | Both local (C&C) and overall (MWFRS) load effects may be determined with a pressure-tapped rigid model. | — | 22 |
| 3.4.1 | MANDATORY | If a static reference pressure is needed, it is measured so that the influence of local features is minimal; location(s) in the report. | — | 22 |
| 3.4.1 | MANDATORY | Tap distribution sufficient to capture the desired load effects; measurement at a number of locations and directions such that no significant effect is missed. The density depends on the geometry and the purpose of the measurement; general guidance is in the commentary. | No number given | 22 |
| 3.4.1 | note | Quality assurance: it is checked that the taps are assigned to the correct connection and that there are no leaks in the tubing system. | — | 22 |
| 3.4.1.1 | MANDATORY (permitted) | Mean and time-varying load effects may be determined by multi-point surface pressure integration. | — | 22 |
| 3.4.1.1 | MANDATORY | For time-varying load effects all pressures to be integrated are measured simultaneously. | — | 22 |
| 3.4.1.2 | MANDATORY | Internal pressure is assessed analytically from the measured external pressures or by direct measurement with a suitable model; the effect of porosity, leakage and openings is considered for different scenarios. | — | 22 |
| 3.4.1.2 | MANDATORY | With measured internal pressure, the net pressure is computed by pressure integration. | — | 22 |
| 3.4.1.2 | MANDATORY | Direct measurement of time-varying internal pressure requires internal volume scaling; deviations that give net pressure on the safe side are permitted and are documented in the report. | see Eq. C3-3 (commentary) | 22 |
| 3.4.1.2 | MANDATORY | Cavity pressures in other partially enclosed volumes (under loose-laid roof membranes and ballast pavers, behind ventilated facade panels, under low-profile rooftop solar panels) are accounted for where they can change the surface pressure behind the porous surface; the size, location and/or porosity of the openings are matched carefully. | — | 22–23 |
| 3.4.1.3 | MANDATORY | Peak pressures are determined with a statistical method in recognized literature. | — | 23 |
| 3.4.1.3 | MANDATORY | The probability of nonexceedance in the statistical analysis is reported. | No value given | 23 |
| 3.4.1.3 | MANDATORY | Filtering of the raw time series at aerodynamically relevant frequencies before the method is applied is not permitted. | — | 23 |
| 4.2.2 | MANDATORY | In dynamic load calculation by pressure integration, the number and layout of the taps are sufficient to measure the total forces and moments to the accuracy the test requires. | No number given | 24 |

## Standard text — wind climate

| Section (§) | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| 6.1 | MANDATORY | If load/response probability is required in the report, the tunnel data are combined with the local wind climate or another specified velocity requirement. | — | 28 |
| 6.1 | note | In regions not affected by tropical cyclones, measurements at a nearby airport are an acceptable data source. | — | 28 |
| 6.1, 6.3 | MANDATORY | In regions affected by tropical cyclones a hazard model by an approved simulation method is required; the design loads are determined from the combined effect of tropical and non-tropical winds. | — | 28 |
| 6.2 | MANDATORY | A wind climate model is derived; record length (sampling error), anemometer height and type, data quality, averaging time, terrain and storm type are considered; method and data sources in the report. | — | 28 |
| 6.2 | MANDATORY | Storm types are separated from the database before detailed analysis. | — | 28 |
| 6.2 | MANDATORY (permitted) | Load reduction arising from the assessment of wind direction is permitted. | No limit given | 28 |
| 6.4 | MANDATORY | Extratropical storms are considered; the model uses historical data; data of other storm types are removed from the record. Numerical weather prediction models are permitted. | — | 28 |
| 6.5 | MANDATORY | Thunderstorms are considered; historical data are used; other types are removed. | — | 28 |
| 6.6 | MANDATORY | If a tornado hazard model is required it is built by an approved simulation method; historical speed data of tornadoes cannot be used. | — | 28 |
| 6.7 | MANDATORY | Orographic winds are considered; if there are no measurements, estimation from local knowledge or a numerical model is permitted. | — | 28 |
| 6.8 | MANDATORY | The tunnel data are combined with the climate data by approved statistical procedures; all storm types that contribute to the hazard at the site are considered; all assumptions and methods in the report. | — | 28 |

## Standard text — measurement requirements and quality

| Section (§) | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| 8.1 | MANDATORY | The hardware must be able to give a repeatable measure of the mean and, where required, the dynamic/time-varying load or response. | — | 32 |
| 8.1 | MANDATORY | In measurements of time-varying local pressure, total load and aeroelastic response, the frequency response is high enough to measure at all relevant frequencies without significant amplitude and phase distortion. | — | 32 |
| 8.1 | MANDATORY | In pressure measurement the ratio of the measured amplitude to the applied pressure amplitude does not deviate from a constant value below the stated frequency. | ±10%; frequency < Uh/B (model scale) | 32 |
| 8.1 | MANDATORY | The phase of the response does not deviate from a linear variation in the same frequency range. | ±10% | 32 |
| 8.1 | MANDATORY (permitted) | Transfer functions may be used to correct the response. | — | 32 |
| 8.1 | MANDATORY | Measurements are free of significant acoustic effects, electrical noise and mechanical vibration; processed measurements contain no spurious fluctuations (ambient pressure variations caused by the fan, door opening, external wind); temperature drift is corrected if necessary. | — | 32 |
| 8.1 | MANDATORY | The overall model dimensions are within the stated accuracy. | ±2% | 32 |
| 8.1 | MANDATORY | The rigid model natural frequency is higher than the lowest natural frequency of interest. | At least 30% | 32 |
| 8.2 | MANDATORY | The total uncertainty in the reported results (aerodynamic coefficients) from hardware, sampling rate and test duration does not exceed the limit. | ≤ 10% | 32 |
| 8.2 | MANDATORY | The test duration and sampling rate take account of the nature of the target flow. | — | 32 |
| 8.2 | MANDATORY | The test duration is longer than the stated multiple of the longitudinal integral time scale at the height critical for the load under study. | > 500 integral time scales | 32 |
| 8.3 | MANDATORY | The reliability of all tunnel data is assessed: uncertainty of the simulation, accuracy and repeatability of the measurements. | — | 32 |
| 8.3 | MANDATORY | Procedures that ensure reliability are established: basic checks of the hardware, traceable calibration, measurement repeatability. | — | 32 |
| 8.3 | MANDATORY | Reliability comparisons with codes, previous model and full-scale data and past experience are included in the report, if available and meaningful. | — | 32 |

## Commentary

| Section (§) | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| C1.2 | COMMENTARY | What a tall building MWFRS report may contain: raw aerodynamic coefficients by direction (Strouhal number, drag and lift coefficients), power spectra of the total forces, overturning moment and shear, design loads and directional combinations, acceleration estimates for serviceability. | — | 34 |
| C3.3 | COMMENTARY | The measured load is nondimensionalized with the air density and the reference velocity; the reference velocity should be measured, retained and used in the analysis with the appropriate air density. Measurement at additional reference heights can be useful for quality control. | — | 46 |
| C3.3 | COMMENTARY | The reference velocity is typically measured (1) at a height assumed to be outside the boundary layer (most tall buildings) or (2) at the height of the structure, upwind of the turntable. | — | 46 |
| C3.3 | COMMENTARY (recommendation) | The reference velocity hardware should be placed where it is least affected by the test structure, the proximity model and the upwind modeling conditions; with an upwind Pitot-static tube a correction for the longitudinal pressure gradient is often needed. | — | 46 |
| C3.3 | COMMENTARY (recommendation) | Some structures need other reference heights tied to a characteristic height (roof, eave); re-referencing conversions should be fully described in the report. | — | 46 |
| C3.4, Eq. C3-1 | COMMENTARY | Model–full-scale frequency ratio: nm/np = (Lp/Lm)·(Um/Up). | Example: Lp/Lm = 400, Um/Up = 0.25 → model frequencies about 100 times faster | 46 |
| C3.4 | COMMENTARY | Effective duration of the largest local peak pressures on buildings; a cladding element with a natural frequency above a few hertz responds fully (quasi-statically) to this load. | About 1–3 s at full scale | 46 |
| C3.4 | COMMENTARY (recommendation) | For large-span cladding the possibility of resonance and (especially in hurricane regions) fatigue should be examined. | — | 46 |
| C3.4.1 | COMMENTARY (recommendation) | Tap locations should be chosen carefully according to the complexity of the external geometry and the surface pressure gradient; a higher density is recommended on small buildings and in high-gradient regions (roof corner/edge/ridge, wall edge). | No number given | 46 |
| C3.4.1, Eq. C3-2 | COMMENTARY | Cp,max, Cp,min, Cp,mean, Cp,rms = the respective pressure / qref; qref = ½·ρ·Uref². The pressures are differential pressures relative to the static pressure in the undisturbed flow. | — | 47 |
| C3.4.1 | COMMENTARY (recommendation) | The static reference pressure measurement should be placed where it is not affected by the test model and the proximity model; the static port of a Pitot-static tube above the flow simulation can often be used. | — | 47 |
| C3.4.1.1 | COMMENTARY | Pressure integration is used for the whole structure, large areas/MWFRS, or the net loads on elements exposed to wind on both faces (eave, parapet, sign, solar panel, freestanding wall). The averaging may be equally weighted or weighted (e.g. weights that give the midspan moment directly). | — | 47 |
| C3.4.1.1 | COMMENTARY | For two-faced elements the differential pressure is found from the algebraic difference of the simultaneous measurement (single tap or area average) of the two faces. | — | 47 |
| C3.4.1.2 | COMMENTARY | What governs internal pressure: external pressure distribution; size/distribution of cracks and leakage paths; size/distribution of openings; enclosed air volume; flexibility of the envelope. Large openings can markedly affect the net cladding pressure and the frame loads. | — | 47 |
| C3.4.1.2, Eq. C3-3 | COMMENTARY | Internal volume scaling (for Helmholtz resonance): Vm/Vp = (Lm/Lp)³ / (UH,m/UH,p)². | — | 47 |
| C3.4.1.2 | COMMENTARY | Direct measurement is often not practicable; internal pressure is more commonly computed from a weighted average of the openings, a flow balance or the direct effect of each opening. If calculation/measurement cannot be applied, the internal pressures in codes such as ASCE 7 are commonly used. | — | 47 |
| C3.4.1.2 | COMMENTARY (recommendation) | Flow paths to be considered in the analytical assessment: external pressure at ventilation inlets/outlets; partitions/connections within a floor and between floors; large openings that may be left open; the possibility of the envelope or partitions being breached by wind. | — | 47 |
| C3.4.1.2 | COMMENTARY (recommendation) | In cavities such as under ballast pavers, under solar panels and in ventilated facades, the internal pressure should be measured; internal volume scaling may be neglected, staying on the safe side; Re similarity is not required for the flow through the holes. | — | 47 |
| C3.4.1.3 | COMMENTARY (recommendation) | Single observed peak coefficients should not be used (poor repeatability, dependence on duration). | — | 48 |
| C3.4.1.3 | COMMENTARY | Two common methods: ensemble average and Gumbel fit; both use the extreme values of segments of equal length that represent a suitable full-scale observation period. | Segment example: 10 min – 1 h at full scale | 48 |
| C3.4.1.3 | COMMENTARY | Other methods: independent storms, BLUE, POT. Cook–Mayne is the most accurate but requires the extreme wind climate. The Davenport peak factor is for Gaussian processes only. | — | 48 |
| C3.4.1.3 | COMMENTARY | If the capacity is not defined by a single peak load (e.g. glass: damage accumulation integral), the tunnel output should be processed in a way compatible with the capacity definition. | — | 48 |
| C3.4.1.3 | COMMENTARY (recommendation) | No filtering that removes any frequency that may be relevant to the aerodynamic phenomenon should be applied. | — | 48 |
| C4.2.2 | COMMENTARY | Tap layout found suitable by experience for simple rectangular shapes (pressure integration); complex shapes require more taps. | About 20–30 taps per ring; at least 8–10 rings over the height | 52 |
| C4.2.2 | COMMENTARY (recommendation) | The roof heights of adjacent buildings may be considered when choosing the height of the nearest ring; where documents that give a minimum tap density apply, that density should be used. | — | 52 |
| C4.2.2 | COMMENTARY | In multi-tower structures connected by a common podium, all towers and the podium should be instrumented and the data taken simultaneously. | — | 52 |
| C6.2 | COMMENTARY | Primary data: 2-min speeds recorded hourly or daily peak gust speeds. The data should be reduced to 10 m height and flat open terrain. | 2 min; 10 m | 60 |
| C6.3 | COMMENTARY | Tropical cyclones are generally significant, at the stated return periods, only near the coast; the tropical cyclone boundary layer is modeled well in the tunnel, particularly in the lower part. | About 100 km from the coast for ≤ 100 years; lowest 300 m | 60 |
| C6.6 | COMMENTARY | It is unlikely that a single structure will experience damaging tornado-induced wind at the stated return periods. | About 3 000 years or less | 61 |
| C6.8, Eq. C6-1/2 | COMMENTARY | Storm types are combined as independent processes: 1/R = 1 − Π(1 − 1/Ri). The wind effect should be found by storm type and then combined. | — | 61–62 |
| C6.8 | COMMENTARY | The extreme wind hazard model (return periods longer than about 10 years) is built by fitting independent storm maxima to an extreme value distribution. | > ~10 years | 61 |
| C6.8 | COMMENTARY | Non-directional upper-bound method: simplest, on the safe side; the R-year speed is applied to the largest response function over all directions; can also be used with ASCE 7 speeds without a climate analysis. | — | 62 |
| C6.8, Eq. C6-3/4 | COMMENTARY | Normalized sector method: each sector is assigned v_design(R,θ) = [v(R,θ)/max v(R,θ)]·vR; generally on the safe side, occasionally unconservative. | — | 62 |
| C6.8, Eq. C6-5 | COMMENTARY | Multi-sector method: extreme winds in the sectors are assumed independent; applied separately for thunderstorms and extratropical storms. | — | 63 |
| C6.8 | COMMENTARY | Up-crossing method: joint speed–direction distribution from hourly 1–2 min means (generally two-parameter Weibull). It does not distinguish thunderstorms. | 1 or 2 min | 63 |
| C6.8, Eq. C6-6 | COMMENTARY | Storm passage method (simulated tropical cyclones): the directional resolution is limited by the tunnel data. | Tunnel data typically 10° | 63 |
| C6.8 | COMMENTARY | Where the directional resolution of the historical data is coarser than that of the tunnel data, the assumptions made should be documented in the report. | — | 63 |
| C8.1, Eq. C8-1/2 | COMMENTARY | Basic kinematic relation: nm·Lm/Um = np·Lp/Up; nm/np = tp/tm = (Lp/Lm)·(Um/Up). | — | 68 |
| C8.1 | COMMENTARY | The frequency response of the tubing system depends on the tube length and diameter, changes in diameter and the transducer volume; a restrictor/equalizer or an analytical correction is used. | No number given | 68 |
| C8.2 | COMMENTARY | Large peak pressure coefficients can vary from one realization to another owing to the nature of the flow. | Up to 30% | 69 |
| C8.2 | COMMENTARY (recommendation) | All laboratory measurements should be made with instruments with traceable calibration; the calibration history should be retained. | — | 69 |
| C8.2 | COMMENTARY | Mean values require the shortest sampling duration, rms/variance somewhat longer, and extreme values and higher-order correlations (including the spectrum) a long one. | — | 69 |
| C8.2 | COMMENTARY | Independent uncertainties combine as the square root of the sum of their squares. | Example: if peak Cp 10%→7% and climate 15%, total 18%→17% | 69 |
| C8.2 | COMMENTARY | Basis of the duration requirement: about 500 integral time scales is sufficient for stable statistics if the peak analysis is done properly; the duration of commonly used databases is about 700 integral time scales. | ~500; ~700 | 70 |
| C8.3 | COMMENTARY | Aims of quality control: that the flow and model scaling match full scale (and that it is stated if they do not), that instruments and software work correctly, that the limits of the interpretations are stated, that human error is reduced, that the report is complete and verifiable. | — | 70 |

## Not found in the text

- A **mandatory** numerical criterion for pressure tap density (taps/m², minimum number of taps): none. Only the ring example in the commentary.
- A numerical sampling rate (Hz) or a limit on tube length/diameter: none.
- A mandatory method for the peak value or a specific value of the probability of nonexceedance: none; only "statistical method + reporting of the probability".
- A numerical rule for area averaging (e.g. relation between effective area and number of taps): none.
- A numerical lower limit for directional reduction (e.g. a certain percentage of the non-directional value): not in this standard.
- A mandatory test duration as a full-scale equivalent (e.g. 1 hour): none; the requirement is in terms of the integral time scale.
