---
name: tunnel-pressure-measurement-and-loads
description: Use when asked about, or when checking a tunnel report for, wind tunnel pressure measurement (pressure taps, tubing frequency response, sampling rate/duration), reference pressure and velocity, peak pressure estimation (Gumbel), area averaging/pressure integration, internal pressure, components and cladding (C&C) and MWFRS loads, combination with wind climate and directionality, measurement uncertainty, quality assurance and report content according to ASCE/SEI 49-21.
---

# Pressure measurement and loads in the wind tunnel — ASCE/SEI 49-21

Source: ASCE/SEI 49-21 (2021 edition). Standard text §1–§8, commentary §C1–§C8. Page numbers are PDF page order. Detailed table: `reference.md`.

## When to use

- When finding components and cladding (C&C) and MWFRS loads by pressure tap measurement on a rigid model.
- When asked how the Cp values in a tunnel report were nondimensionalized, how the peak value was estimated, and whether the measurement duration and frequency response are adequate.
- When assessing the combination of tunnel data with the wind climate and the directional effect.
- When tunnel Cp values are to be compared with a CFD result.

## Step by step

1. **Define the reference velocity (§3.3).** The reference velocity is measured at a location where the influence of the proximity model is minimal and is related to the target mean velocity profile in the test section. Its location, the measurement parameters and every conversion to another location/height are documented in the report.
2. **Choose the reference static pressure (§3.4.1).** If a static reference pressure is needed (e.g. external pressure coefficients are to be compared with the literature), it is measured so that the influence of local features is minimal; the location(s) are documented in the report. Commentary: the static port of a Pitot-static tube placed above the simulated flow can often be used (§C3.4.1).
3. **Place the pressure taps (§3.4.1).** The distribution must be sufficient to capture the desired load effects; measurements must be made at a number of locations and directions such that no significant load effect is missed. **The standard gives no numerical tap density.** Commentary: denser taps are recommended on small buildings and where the pressure gradient is high (roof corner/edge/ridge, wall edge); for pressure integration on simple rectangular tall buildings, about 20–30 taps per ring and at least 8–10 rings over the height have been found suitable by experience (§C3.4.1, §C4.2.2).
4. **Verify the frequency response of the measurement chain (§8.1).** In pressure measurement the amplitude ratio must not deviate by more than ±10% from a constant value at frequencies below the frequency Uh/B at model scale; the phase must also not deviate by more than ±10% from a linear variation in this range. A transfer function may be used for correction. Uh = mean velocity at mean roof height; B = the lesser of the smallest horizontal dimension and the mean roof height.
5. **Choose the sampling rate and duration (§3.4, §8.2).** Rate and duration are chosen so as to give a data set suitable for the intended analysis method. The duration must be longer than 500 times the longitudinal integral time scale at the height critical for the load under study. **The standard gives no numerical sampling rate (Hz)**; the rate is determined by the frequency response requirement and the nature of the target flow.
6. **Calibration and drift (§3.4).** Instruments are calibrated before the test and, if necessary, during and after the test; drift in mean values is corrected. It is checked that the taps are connected to the correct channel and that there are no leaks in the tubing (§3.4.1).
7. **Combine loads (§3.4.1.1).** Multi-point pressure integration is permitted for mean and time-varying load effects; for time-varying effects all pressures to be integrated must have been measured simultaneously.
8. **Address internal pressure (§3.4.1.2).** Internal pressure is found either analytically from the measured external pressures or by direct measurement with a suitable model; the effect of porosity, leakage and openings is assessed for different possible scenarios. Direct measurement of time-varying internal pressure requires internal volume scaling.
9. **Estimate the peak value (§3.4.1.3).** Peak pressures are determined with a statistical method in recognized literature; the probability of nonexceedance is reported; the raw time series cannot be filtered at aerodynamically relevant frequencies before the method is applied.
10. **Combine with climate (§6).** If load/response probability is required, the tunnel data are combined with the local wind climate or another specified velocity requirement by approved statistical procedures; all storm types that contribute to the hazard at the site are considered; assumptions and methods are documented in the report.
11. **Uncertainty and quality (§8.2, §8.3).** The total uncertainty in the aerodynamic coefficients from measurement hardware + sampling rate + test duration must not exceed 10%. The reliability of the data (uncertainty of the simulation, accuracy and repeatability of the measurement) is assessed.
12. **Report and retain (§1.2).** Load, pressure and reference velocity time series are retained; the report must be auditable.

## Coefficient definition (commentary, §C3.4.1, Eq. C3-2)

Cp,max, Cp,min, Cp,mean and Cp,rms are defined, respectively, as the maximum, minimum, time-mean and root-mean-square (of the deviation from the mean) pressure over the sampling duration divided by qref = ½·ρ·Uref². All pressures are differential pressures relative to the static pressure in the undisturbed flow. The standard does not impose a single height for Uref; the report is required to give the definition (§3.3).

## Peak value methods (commentary, §C3.4.1.3)

- A single observed peak coefficient should not be used: its repeatability is poor and it depends on the test duration.
- Two common methods: (1) ensemble average — the mean of the maxima taken from segments of equal length that represent a suitable full-scale observation period (e.g. 10 min – 1 h); (2) Gumbel fit — finding the parameters from the segment maxima and estimating the peak that corresponds to a specified percentile level.
- Other recognized methods: method of independent storms, BLUE (best linear unbiased estimator), peaks over threshold (POT).
- The Cook–Mayne method is an extension of the Gumbel fit; it combines extreme value fits of load and wind speed, is the most accurate but requires knowledge of the extreme wind climate; it is not suitable for generic coefficients of products to be used in many climates.
- The Davenport peak factor is valid only for Gaussian processes; it is limited in complex flow.
- The effective duration of the largest local peak pressures on buildings is about 1–3 s at full scale (§C3.4).
- Large peak pressure coefficients can vary by 30% from one test realization to another, owing to the nature of the flow (§C8.2).

## Wind climate and directionality (summary)

Mandatory (§6.1–§6.8): a wind climate model is derived; record length, anemometer height and type, data quality, averaging time, terrain and storm type are considered; storm types are separated before detailed analysis; load reduction arising from the assessment of direction is permitted. In tropical cyclone regions a hazard model by an approved simulation method is required and the design loads are determined from the combined effect of tropical + non-tropical winds. If a tornado hazard model is required it is built by simulation; historical speed data of tornadoes cannot be used.

The commentary (§C6.8) lists the combination methods: non-directional upper-bound method (simplest and on the safe side; can also be used with ASCE 7 speeds without a climate analysis), normalized sector method (generally on the safe side, may occasionally be unconservative), multi-sector method, up-crossing method, storm passage method, direct simulation. Storm types are combined as statistically independent processes (Eq. C6-1, C6-2). The directional resolution of historical data is often coarser than that of the tunnel data (typically 10°); the assumptions made for this should be documented in the report. Airport data should be reduced to 10 m height and flat open terrain.

## Mandatory requirements (standard text, "shall")

| Section | Requirement |
|---|---|
| §1.2 | The report must be auditable; setup, method, flow, climate analysis, results and uncertainty quantification are included or are made available promptly on request. |
| §1.2 | Load, pressure and reference velocity time series are retained. |
| §3.3 | Reference velocity at a location where the influence of the proximity model is minimal; related to the target profile; location, parameters and conversions in the report. |
| §3.4 | Calibration before the test (during/after if necessary); sampling rate and duration suited to the method; frequency response sufficient to capture peak and time-varying quantities; mean drift is corrected. |
| §3.4.1 | Static reference pressure is measured so as to be least affected by local effects; its location in the report. |
| §3.4.1 | Tap distribution sufficient to capture the load effects; a number of locations and directions such that no significant effect is missed. |
| §3.4.1.1 | For time-varying effects the integrated pressures are measured simultaneously. |
| §3.4.1.2 | Internal pressure is assessed analytically or by direct measurement; porosity, leakage and opening scenarios are considered; cavity pressures are accounted for where they can change the load on the surface behind. |
| §3.4.1.3 | Peak pressure by a statistical method; probability of nonexceedance is reported; pre-filtering at aerodynamically relevant frequencies is prohibited. |
| §6.1–§6.8 | Combination with climate if a probabilistic result is required; storm types are separated; assumptions and methods in the report. |
| §8.1 | Pressure measurement chain: at frequencies below Uh/B, amplitude within ±10%, phase within ±10% of linear. Measurements free of acoustic effects, electrical noise, mechanical vibration and spurious fluctuations; temperature drift corrected. |
| §8.2 | Coefficient uncertainty (hardware, sampling rate, duration) ≤ 10%; duration > 500 longitudinal integral time scales. |
| §8.3 | Reliability is assessed; traceable calibration and repeatability checks are made; reliability comparisons with codes and with previous model and full-scale data (if available and meaningful) are included in the report. |

## Checklist (when reading a tunnel report; yes/no)

1. Are the location and height at which the reference velocity was measured given clearly?
2. If the coefficients were converted to another height/location, is the conversion documented?
3. Is the location of the static reference pressure stated?
4. Is the Cp definition (qref, which velocity, which averaging time) written?
5. Are the number and layout of the pressure taps (drawing/table) given; are they densified at corners and edges?
6. Is the frequency response of the tubing system (or the correction by transfer function) documented, and is it within ±10% up to Uh/B?
7. Are the sampling rate and duration given with their model and full-scale equivalents?
8. Is the duration longer than 500 integral time scales at the critical height?
9. Were the pressures used in area averaging/integration measured simultaneously?
10. Are the peak value method (e.g. Gumbel, ensemble average) and the probability of nonexceedance stated?
11. Is it clear that no filtering that removes aerodynamic frequencies was applied before the peak estimation?
12. Was a statistical estimate used instead of a single observed peak?
13. How was internal pressure handled (measurement, analytical, ASCE 7 value) and for which opening scenarios?
14. Are the wind climate data source, the separation of storm types and the combination method described?
15. If directional reduction was used, are the method and the directional resolution assumptions documented?
16. Is the uncertainty quantification (including the ≤ 10% coefficient uncertainty) given?
17. Are the traceability of the calibration and the repeatability check stated?
18. Is there a reliability comparison with a code or with previous data?
19. Is it stated that the time series are retained?
20. Are deviations from the standard justified?

## When comparing with CFD

What must be taken from the report:
- **Nondimensionalization:** location and height of Uref (outside the boundary layer, or roof height), air density, location of the static reference pressure. The comparison is meaningless unless the CFD Cp is computed with the same qref and the same static reference.
- **Tap locations:** the coordinates of each tap. In CFD the comparison must be made with the point/cell value at the tap location, not with a surface average.
- **Frequency content:** the upper frequency up to which the measurement chain gives a flat response (at least Uh/B) and the sampling rate. Rms and peak values depend on bandwidth; the CFD time series must be brought to the same effective bandwidth before the comparison.
- **Duration:** tunnel duration in terms of integral time scales (≥ 500). If the CFD (especially LES) duration is much shorter than this, the uncertainty of the peak and rms estimates is large; the commentary says that large peak coefficients can vary by 30% from realization to realization even in the tunnel.
- **Peak definition:** method, segment length (full-scale equivalent), number of segments and probability of nonexceedance. CFD peak values must be computed with the same method and the same percentile; they must not be compared using the raw maximum/minimum value.
- **Area averaging:** which taps were combined, with which weights, and simultaneously.
- **Internal pressure and net pressure:** whether the value in the report is external Cp or net pressure; by which route the internal pressure was added.
- **Climate combination:** the design pressures in the report are often values combined with the directional climate and corresponding to a return period; they cannot be compared directly with the coefficient CFD gives for a single direction. The comparison must be made on the raw, direction-by-direction coefficients.
- **Blockage and other corrections:** whether a correction was applied to the reported coefficients.

## Related skills

- `tunnel-approach-flow` — target profile, turbulence, choice of reference velocity/height.
- `tunnel-model-and-surroundings` — scale, blockage, proximity model, Reynolds, direction increment.
- `tunnel-other-measurements` — high-frequency force balance, dynamic response by pressure integration, aeroelastic model, products.
