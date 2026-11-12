---
name: tunnel-other-measurements
description: Use when asked about wind tunnel measurements other than pressure taps according to ASCE/SEI 49-21; high-frequency force balance (HFFB), direct load measurement and rigid section model, dynamic response analysis of flexible structures, aeroelastic model (vortex shedding, galloping, flutter), product tests (products, solar arrays), snow load model studies, the tornado/downburst framework and the scope status of pedestrian wind.
---

# Other measurements in the wind tunnel — ASCE/SEI 49-21

Source: ASCE/SEI 49-21 (2021 edition). Standard text §1–§8, commentary §C1–§C8. Page numbers are PDF page order. Detailed table: `reference.md`.

## When to use

- When a high-frequency force balance (HFFB), load cell, section model or aeroelastic model was used in a report and its requirements are to be checked.
- When asked which of the rigid / flexible / aeroelastic classes the structure falls into and which type of test is required.
- When asked about generic coefficient tests for mass-produced products such as rooftop solar panels, a snow load model study or tornado loads.
- For the question "is pedestrian-level wind comfort covered by this standard?".

## Structure classes (§1.4, §C1.4)

- **Rigid structure:** inertial load effects insignificant → Chapter 3.
- **Flexible structure:** inertial load effects significant, but no marked aeroelastic behavior expected → Chapter 4 (the Chapter 3 requirements also apply).
- **Aeroelastic structure:** the aerodynamic forces are affected by the structure's own motion → Chapter 5.
- The standard does not define frequency limits for these classes; the commentary recommends not looking at frequency alone, but also considering experience and full-scale performance.

## Step by step

1. **Choose the class and the test type.** If an empirical preliminary assessment or experience indicates the possibility of aerodynamic instability or aeroelastic amplification of the loads, an aeroelastic model test is mandatory (§5.1). Otherwise an HFFB or high-frequency pressure integration on a rigid model is sufficient (§4.2).
2. **HFFB (§4.2.1, §3.4.2).** The lateral and torsional fundamental frequencies of the combined model + balance system are determined in the calibration; it is ensured that these frequencies do not contaminate the data; the system must be free of mechanical vibration. If a simplified relation between mode shape and measured load is assumed, the effect of the deviation of the actual mode shapes from it is considered in the analysis.
3. **Direct load measurement and section model (§3.4.2, §3.4.2.1).** All load measurements to be combined are taken simultaneously. A rigid section model must have continuous geometry along its length, must avoid atypical details and must meet the geometry requirements of §8.1.
4. **Dynamic analysis (§4.1, §4.3).** The sampling rate and duration are chosen so as to give data suitable for methods based on random vibration theory. Analysis in the frequency or time domain is permitted, as is presentation of the results as equivalent static loads or as direct dynamic response.
5. **Aeroelastic model (§5.2).** Mass, stiffness and damping (or their ranges) are scaled by accepted principles of dynamic similarity; the structural damping must be similar to full scale. The Reynolds lower threshold is maintained over the whole test velocity range. If gravity forces affect the stiffness, Froude number similarity is required and is reported; with Froude scaling the velocity and frequency scales are fixed by the length scale. For a full aeroelastic model the damping, frequency and mode shapes are compared with the full-scale calculations.
6. **Aeroelastic test conditions (§5.3).** The velocity range is set according to the mean recurrence intervals (MRI) of the relevant limit states; up to the ultimate limit state (ULS) design speed and with a margin that shows that the onset of instability exceeds the ULS speed. For vortex excitation, the excitation at low speed and the fact that the onset of vibration may take a long time are considered. The range of directions also includes nonzero angles of attack for horizontal structures. The Reynolds effects of low model speeds are discussed in the report; spurious excitation from tunnel vibration and acoustic waves is prevented.
7. **Report (§5.5).** The justification for the choice of model type, the scaling principles, the method of conversion to full scale and its assumptions; the full-scale and model mechanical properties (mass, polar moment of inertia, natural frequencies, damping) and the representation of the support conditions in the model.

## Mandatory requirements (standard text, "shall")

| Section | Requirement |
|---|---|
| §1.1 | Pedestrian-level wind, pollutant dispersion, dust and wind energy studies are out of scope; however, including them in the wind load report is permitted. |
| §3.4.2 | The model + load cell/balance system free of mechanical vibration; fundamental frequencies determined in the initial calibration and prevented from contaminating the data; load measurements to be combined are simultaneous. |
| §3.4.2.1 | Rigid section model with continuous geometry along its length; meets the geometry requirements of §8.1. |
| §3.5 | Product tests: the range of building geometry and product location, the range of product geometry and repeated/interfering arrangements are considered; the product geometry is modeled exactly; the results are not extrapolated to geometries not modeled unless a basis is given; interpolation is allowed if verified by test; the conditions of validity in the report. |
| §3.5 | For rooftop solar panel arrays the results are presented as a function of the normalized effective wind area. |
| §4.1 | All test requirements of Chapter 3 also apply to dynamic load data. |
| §4.2.1 | The HFFB calibration determines the lateral and torsional fundamental frequencies; the effect of mode shape deviation is considered in the analysis. |
| §4.2.2 | In pressure integration the number and layout of the taps are at a level that gives the total forces and moments to the required accuracy. |
| §4.4 | A generic dynamic amplification factor (DAF) may be determined for products; the limits of validity in the report. |
| §5.1 | If there is a possibility of instability or aeroelastic amplification, an aeroelastic model test is mandatory. |
| §5.2.1 | Mass, stiffness and damping are scaled by dynamic similarity; damping similar to full scale; Re lower threshold over the whole velocity range; Froude similarity if required. |
| §5.2.2.1 | The length/width ratio of the section model sufficient to model the spanwise correlation correctly; the model rigid enough for local bending to remain insignificant. |
| §5.2.2.2 | A partial aeroelastic model is permitted if it has been shown by static model tests that the critical response is governed by the fundamental sway modes. |
| §5.2.2.3 | For a full aeroelastic model the damping, frequency and mode shapes are compared with the full-scale calculation; if an exact match cannot be achieved, the reasons and possible effects are discussed in the report. |
| §5.3 | Velocity range ULS speed + margin; range of directions covers the significant directions; low-speed Re effects in the report; spurious excitation is prevented. |
| §5.4 | A full aeroelastic model is instrumented so as to measure the total (mean + dynamic) response directly; for section and partial models the conversion to the full structure is made by approved methods. |
| §7.1 | Tunnel or water flume model studies for snow load are permitted as an aid to the interpretation of the ASCE 7 snow provisions; the report contains the scaling principles, calculation methods, assumptions and the limitations arising from similarity mismatch. |
| §8.1 | Rigid model natural frequency at least 30% higher than the lowest natural frequency of interest. |

## Highlights from the commentary (not binding)

- **HFFB assumptions (§C4.2.1):** the first three modes uncoupled and orthogonal to each other; sway mode shapes linear with height; torsional mode shape constant over the height; no motion-dependent forces; the model + balance system sufficiently rigid. Typical corrections for a nonlinear mode shape: ±10% on the bending base moment, 30%–40% reduction in torsion; correction of up to 20% on peak accelerations.
- **Indicators of aeroelastic sensitivity (§C5.1):** if the slenderness ratio exceeds 10:1 for buildings, 30:1 for bridges; if the slope of the lift or torsional force curve with respect to the angle of attack is negative; if the periods of vibration are unusually long.
- **Section model (§C5.2.2.1):** scale typically 1:10–1:100; model length about 4–5 times the deck width. For vortex excitation the velocity should be swept in fine steps and held long enough at each velocity. Partial turbulence simulation on a section model should match the longitudinal and vertical spectra for n·d/U ≥ 1.0.
- **Aeroelastic building models (§C5.2.2.2–3):** scale typically 1:200–1:600; at least the lowest three modes (two sway + torsion); for complex modes a full model with masses lumped at 3–7 levels.
- **Velocity range (§C5.3):** for buildings at least up to the ultimate strength MRI speed appropriate to the risk category; for long-span bridges an MRI of 10 000 years for the onset of instability is common in North American practice. Turbulence tends to suppress vortex excitation and to raise the onset of flutter; the possibility of low turbulence should also be tested.
- **Damping (§C5.2.1.1):** full-scale damping is often not well known; testing for a range of damping values is recommended.
- **Products (§C3.5):** tests are mostly run at a scale of 1:50 or larger and require PTS; rooftop solar panels should be tested, where appropriate, with at least eight rows on the roof of representative generic buildings.
- **Snow (§C7.1):** the particle method and the time-stepping simulation methods (A and B) are described; particle methods are not a full dynamic simulation but an approximate analogy. CFD for snow is promising but has not yet been validated over a wide range of geometries; it is recommended as a complementary tool together with a scaled model study.
- **Tornado and downburst (§C2.3.2):** there are no established scaling rules; the commentary proposes a framework that includes the aerodynamic + static pressure components, three cases of tornado size relative to the building, and the conditional averaging approach. The parameter ranges are in `reference.md`.

## Checklist (when reading a tunnel report; yes/no)

1. Are the rigid / flexible / aeroelastic class of the structure and the justification for the chosen test type given?
2. If an HFFB was used, are the fundamental frequencies (sway and torsion) of the model + balance system reported?
3. Is it shown that these frequencies do not contaminate the measurement band (or that a mechanical admittance correction was made)?
4. Are the assumed mode shapes and the corrections applied for the actual mode shapes described?
5. Are the structural properties (frequency, mass, damping) and their sources in the report?
6. Are the analysis domain (frequency/time) and the form of the results (equivalent static load / direct response) stated?
7. If there is an aeroelastic model, are the scaling of mass, stiffness and damping and the velocity/frequency scales given?
8. Is it discussed whether Froude similarity is required?
9. Is the Reynolds lower threshold also met at the lowest test velocity?
10. Does the velocity range exceed the ULS speed by a margin; is the instability onset speed determined?
11. Are the model damping, frequencies and mode shapes compared with the full-scale targets?
12. In a product test, are the range of geometries tested and the conditions of validity written clearly; was any extrapolation made?
13. In a snow study, are the limitations arising from similarity mismatches stated?
14. If there are pedestrian-level wind results, is it clear that they are not covered by the ASCE 49 requirements?

## When comparing with CFD

- **HFFB results** are the total base moments and their spectra; the CFD counterpart is the time series of the surface pressure integrated about the base. From the report: the location of the moment axis (balance center), the nondimensionalization (reference velocity, area, length) and the direction definition must be taken.
- **The resonant response is not measured in the tunnel**; it is added analytically with the structural properties. The comparison with CFD must be made on the raw aerodynamic loads (mean, background, spectrum); the design loads in the report (equivalent static load) include damping, frequency and climate assumptions.
- **Mode shape corrections** may have been applied to the report results; it must be found out whether they are raw or corrected.
- **Aeroelastic effects** (aerodynamic damping, lock-in) do not appear in CFD with rigid geometry; aeroelastic model results cannot be compared directly with rigid CFD.
- **Product tests** are mostly run with PTS; the reported coefficients include the low-frequency compensation (see `tunnel-approach-flow`).
- **Pedestrian-level wind:** this standard gives no criterion for it; the comparison criterion must come from another source.

## Related skills

- `tunnel-approach-flow` — approach flow, PTS, scope of non-synoptic winds.
- `tunnel-model-and-surroundings` — scale, blockage, Reynolds, appurtenances.
- `tunnel-pressure-measurement-and-loads` — pressure integration, peak value, combination with climate, uncertainty, report.
