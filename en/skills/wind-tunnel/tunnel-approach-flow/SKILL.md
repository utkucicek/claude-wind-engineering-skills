---
name: tunnel-approach-flow
description: Use when an atmospheric boundary layer (ABL) simulation in a wind tunnel has to be set up or checked against ASCE/SEI 49-21; covers the target mean velocity profile, turbulence intensity, integral length scale, power spectral density, roughness Reynolds number, reference velocity/height (Uref, zref), partial ABL and partial turbulence simulation (PTS), and the topographic model.
---

# Approach flow in the wind tunnel — ASCE/SEI 49-21

Source: ASCE/SEI 49-21 "Wind Tunnel Testing for Buildings and Other Structures" (2021 edition; supersedes 49-12). The standard text is Chapters 1–8, the commentary is Chapters C1–C8. In this skill "§2.3" points to the standard text and "§C2.3" to the commentary. Page numbers are PDF page order. Detailed table: `reference.md`.

## When to use

- When asked whether the boundary layer simulation in a tunnel report complies with the standard.
- When choosing the target profile, turbulence and scale compatibility while designing a tunnel test.
- When extracting inlet conditions from the report in order to rebuild the tunnel test in CFD.
- When a low-rise building, a large-scale product test (partial ABL, PTS) or complex terrain (topographic model) is involved.

Out of scope (other skill): model scale, blockage, proximity model → `tunnel-model-and-surroundings`; pressure measurement and loads → `tunnel-pressure-measurement-and-loads`.

## Step by step

1. **Identify the flow type (§2.1).** The standard sets requirements only for an ABL with neutral thermal stratification; in the tunnel this is isothermal flow. Non-neutral flow is permitted in stability tests of long-span bridge decks, provided the justification is discussed in the report. There is no mandatory requirement for non-synoptic winds such as tornadoes and downbursts; only a framework is given in the commentary (§2.3.2, §C2.3.2).
2. **Full ABL or partial ABL? (§2.3.1.1, §2.3.1.2)** For low-rise buildings and small structures, simulating only the lower part of the boundary layer (atmospheric surface layer, ASL) is permitted. For a full ABL zref = zg (gradient height); if only the ASL is modeled, zref = zs is taken (§C2.2, commentary).
3. **Choose the target profile (§2.3.1.1 item 1).** The mean velocity profile must be consistent with ABL or partial ABL models in recognized literature. The standard does not mandate a specific formula. The commentary gives the logarithmic law, the power law, the Harris–Deaves full ABL profile and the log–quadratic profile for hurricanes; Table C2-1 gives z0, 1/α, zg, zs, Iu and xLu values by ASCE 7 exposure category (§C2.3.1.1).
4. **Target the turbulence (§2.3.1.1 items 2–4).** The turbulence intensity profiles of the three velocity components must be consistent with the target mean velocity profile. The integral length scale and the power spectrum of the velocity fluctuations are measured between 60% and 100% of the mean roof height of the structure (or at other heights depending on the purpose of the test); they must be consistent with the target profile (and, for the length scale, with the model scale).
5. **Check scale compatibility (§2.2, Eq. 2-1…2-4).** Jensen number Lb/z0 (within a factor of 3), Lb/zref, xLu/Lb (within a factor of 3, or model value at least 3) and building Reynolds number (at least 11 000). Details are in the `tunnel-model-and-surroundings` skill.
6. **Check the roughness Reynolds number (§2.3.1.1 item 5, Eq. 2-5).** u*·z0/ν must be at least 2.5. For tunnel flow u* can be estimated with Eq. C2-1 in the commentary: u* = Uref·κ / ln(zref/z0), κ = 0.4.
7. **Locate the reference velocity and height (§2.3.1.1, §3.3).** Uref and zref must be at a location that minimizes the influence of the proximity model and of blockage; the relation of the chosen Uref–zref to the target boundary layer model must be explained in the report.
8. **PTS if the scaling requirements cannot be met (§2.3.1.3).** If the flow scaling requirements of §2.3.1.1 cannot be achieved, partial turbulence simulation is permitted: the nondimensional spectrum n·S(n)/U² is matched only at high frequencies (Eq. 2-6); the effect of the missing low-frequency turbulence must be accounted for with the methods and limits in the literature.
9. **Topographic model if there is complex terrain (§2.5).** In terrain that exceeds the extent of the proximity model or that generates flows not defined in §2.3, the wind characteristics at the site are determined in the tunnel with a topographic model: mean velocity and turbulence profiles at the site are measured for a number of directions sufficient to define the full range of directions.
10. **Report (§1.2).** For each wind direction considered, the simulated and target profiles are given together (see the checklist below).

## Where and how the profile is measured — what the text says and does not say

This is asked often; what the standard states explicitly must be kept separate from what it does not state.

What the text says:
- For the integral length scale and the spectrum, the measurement **height** is given: 60%–100% of the mean roof height (§2.3.1.1 items 3–4, pp. 20–21).
- The reference velocity and height must be at a location that minimizes the influence of the proximity model structures and of the associated blockage (§2.3.1.1, p. 20; §3.3, p. 22).
- Commentary: the reference velocity is typically measured either (1) at a height assumed to be outside the simulated boundary layer in tall-building applications, or (2) at the height of the structure, **upwind of the turntable**; if a Pitot-static tube is used upwind, a correction for the longitudinal pressure gradient is often needed (§C3.3, p. 46).
- Commentary: the proximity model rotates on the turntable together with the test building; the proximity model should not affect the flow at the location where the reference velocity is measured (§C2.4, p. 44).
- If a topographic model is used, the profiles are measured "at the test site" (§2.5, p. 21).
- The report gives the simulated and target profiles for each wind direction (§1.2 item 2, p. 16).

What the text does not say (not found in the text):
- At which location in the tunnel the approach flow **profile** (velocity, turbulence, spectrum) is to be measured — turntable center or upwind of the proximity model — is not stated explicitly.
- Whether the test model or the surrounding buildings are in place during the profile measurement is not stated explicitly.
- No numerical acceptance tolerance for the profile (e.g. ±% deviation from the target profile) is given; the criterion is of the form "consistent". Numerical tolerances exist only for the scale compatibility equations (2-1…2-5).

Therefore, when checking a report, this information must be read from the report and must not be attributed to the standard.

## Mandatory requirements (standard text, "shall")

| Section | Requirement |
|---|---|
| §2.1 | The simulation is for a neutrally stratified ABL; in bridge deck stability tests non-neutral flow is allowed if its justification is discussed in the report. |
| §2.2 | The model scale must be compatible with the lengths of the approach flow: Eq. 2-1 and the first relation of Eq. 2-3 within a factor of 3; (xLu/Lb)m ≥ 3 and (Lb·Ub/ν)m ≥ 11 000 are lower limits. If not met, the uncertainty and any additional studies that may be needed are discussed in the report. |
| §2.3.1.1 | Uref and zref at a location where the influence of the proximity model and of blockage is minimal; relation to the target boundary layer model in the report. |
| §2.3.1.1 | Tropical cyclone winds are simulated like the ABL, Uref is determined according to Chapter 6; for a hurricane approaching over water, Exposure Category C may be chosen. |
| §2.3.1.1 (1) | Mean velocity profile consistent with ABL / partial ABL models in recognized literature. |
| §2.3.1.1 (2) | Turbulence intensity profiles of the three components consistent with the target velocity profile. |
| §2.3.1.1 (3) | Integral length scale measured at 60%–100% of roof height; consistent with the target profile and the model scale. |
| §2.3.1.1 (4) | Power spectrum of the velocity fluctuations measured in the same height range; consistent with the target profile. |
| §2.3.1.1 (5) | u*·z0/ν ≥ 2.5 (Eq. 2-5). |
| §2.3.1.2 | Partial ABL simulation is allowed for low-rise structures. |
| §2.3.1.3 | If the scaling requirements cannot be met, PTS is allowed; the effect of the missing low frequencies is accounted for with methods in the literature. |
| §2.5 | In complex terrain a topographic model is built; mean velocity and turbulence profiles at the site are measured for a sufficient number of directions and the conditions of §2.3.1.1 are met. |
| §1.2 (2) | The report contains, for each direction, the simulated and target mean velocity profile, longitudinal turbulence intensity profile, turbulence spectrum and longitudinal length scale. |
| §1.2 | If the test conditions deviate from the standard, the justification is given in the report. |

## Highlights from the commentary (not binding)

- Strong wind: velocity greater than 10 m/s at 10 m height; in this case mechanical turbulence breaks down the thermal stratification (§C2.1).
- The boundary layer depth simulated in the tunnel, (zg)m, is mostly 0.75–1.50 m; in low-rise building studies (zs)m can be increased up to 0.5–0.75 m (§C2.2).
- Common approach in practice: adjust the upwind floor roughness until the desired power law exponent is obtained (§C2.2). z0 may vary with direction; the most appropriate boundary layer should be used for each direction (§C2.3.1.1).
- The choice of zref changes the profile: for the same Uref = 20 m/s, if zref = 600 m is taken instead of 10 m, the velocity at 600 m differs by a factor of about 1.7 (§C2.3.1.1).
- Lateral and vertical turbulence: Iv ≈ 0.8·Iu, Iw ≈ 0.5·Iu (lower part of the ABL). Length scales: yLu ≈ 0.3·xLu, zLu ≈ 0.5·xLu.
- The xLu estimate is sensitive to the method: a difference of up to about 30% between temporal correlation and spectrum fitting; the relation z/(2π·fm) may give values 2–3 times lower (§C2.3.1.1).
- The lower limit of xLu,m/Lb,m for PTS is a research topic; values in the range 0.7–1.5 have been suggested (§C2.3.1.3).
- Topographic models agree well with field measurements at scales of 1:500–1:5 000; the step (terrace) size must be chosen carefully: a completely smooth surface gives low turbulence, a very large step gives distorted turbulence (§C2.5).

## Checklist (when reading a tunnel report; yes/no)

1. Does the report say which edition (49-21) it complies with?
2. Is it stated that the flow is a neutrally stratified ABL (or is the justification for the deviation given)?
3. Is it written whether a full ABL or a partial ABL was simulated?
4. Are the target mean velocity profile and the publication/model it is based on stated?
5. Are the simulated and target mean velocity profiles given together for each wind direction?
6. Are the simulated and target longitudinal turbulence intensity profiles given for each direction?
7. Are the simulated and target turbulence spectrum and longitudinal integral length scale given?
8. Were the length scale and spectrum measured between 60% and 100% of roof height (or at another, justified height)?
9. Is the model–prototype ratio of Lb/z0 within a factor of 3?
10. Is the model–prototype ratio of xLu/Lb within a factor of 3, or is the model value at least 3?
11. Is u*·z0/ν ≥ 2.5 shown?
12. Are the location of Uref and zref and their relation to the target boundary layer model explained?
13. Was the reference velocity measurement location chosen so that it is not affected by the proximity model?
14. Does the report state where in the tunnel and in which configuration (model/surroundings present or not) the profile was measured? (The standard does not require this; it is needed for CFD.)
15. If PTS was used, are the way the missing low-frequency turbulence was compensated and the publication it is based on stated?
16. If a topographic model was used, are its scale, the profiles at the site and the measurement directions given?
17. If there is a deviation from the requirements, is there a justification and a discussion of uncertainty?

## When comparing with CFD

What must be taken from the report in order to rebuild the tunnel test in CFD:
- **Inlet profiles:** U(z), Iu(z) (Iv, Iw if available), xLu and spectrum; at which height, for which direction. The standard asks only for "simulated and target profile for each direction"; if there is no numerical table it must be requested from the laboratory.
- **Location and configuration of the profile measurement:** The standard does not define this. Whether in CFD the profile is to be matched at the inlet boundary or at the building location (empty tunnel) depends on it; it must be learned from the report or from the laboratory.
- **Reference definition:** The location and height at which Uref was measured (outside the boundary layer, or at roof height upwind of the turntable) and, if a conversion to another height was made, the conversion (§3.3, §C3.3). The coefficients are nondimensionalized with this velocity; if the same definition is not used in CFD, Cp cannot be compared directly.
- **z0 and u*:** If the report gives z0, the roughness Reynolds requirement and the fit to the logarithmic profile can be checked.
- **Partial ABL / PTS:** If the low-frequency turbulence left out in the tunnel was added afterwards by analysis, the CFD result must be compared with the corrected data (or with the same correction applied), not with the raw tunnel data.
- **Longitudinal pressure gradient:** The commentary says that in the ABL the longitudinal pressure variation is approximately zero and that in the tunnel it is controlled by adjusting the ceiling (§C2.3.1.1). In the CFD domain it must also be checked separately whether the profile is maintained up to the building location.
- **Length scale method:** It should be asked whether xLu was found by correlation or by spectrum fitting; the difference between methods can reach 30%.

## Related skills

- `tunnel-model-and-surroundings` — scale, blockage, proximity model, Reynolds number, direction increment.
- `tunnel-pressure-measurement-and-loads` — pressure measurement, reference pressure, peak value, combination with climate, report.
- `tunnel-other-measurements` — high-frequency force balance, aeroelastic model, products, snow, non-synoptic winds.
