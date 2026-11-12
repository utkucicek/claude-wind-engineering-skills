---
name: tunnel-model-and-surroundings
description: Use when asked about, or when checking in a tunnel report, the wind tunnel model's geometric scale, geometric detail and accuracy, the extent of the proximity model, the blockage ratio limit and correction, Reynolds number requirements, rounded structures and the wind direction increment according to ASCE/SEI 49-21.
---

# Tunnel model and its surroundings — ASCE/SEI 49-21

Source: ASCE/SEI 49-21 (2021 edition). Standard text §1–§8, commentary §C1–§C8. Page numbers are PDF page order. Detailed table: `reference.md`.

## When to use

- When choosing the model scale or checking whether the scale in a report is compatible with the flow.
- For the questions "up to what radius must the surrounding buildings be modeled?", "blockage exceeded 5%, what happens?", "is the Reynolds number sufficient?", "at what angular increment must measurements be taken?".
- When extracting geometry and domain information from the report while rebuilding the tunnel test in CFD.

## Step by step

1. **Choose a scale compatible with the flow (§2.2).** Four criteria are met together (m = model, p = prototype):
   - Eq. 2-1: (Lb/z0)m = (Lb/z0)p — within a factor of 3 (because of the uncertainty of z0 at full scale).
   - Eq. 2-2: (Lb/zref)m = (Lb/zref)p — achieved by choosing the same reference location at model and full scale.
   - Eq. 2-3: (xLu/Lb)m = (xLu/Lb)p — within a factor of 3; or at least (xLu/Lb)m ≥ 3.
   - Eq. 2-4: (Lb·Ub/ν)m ≥ 11 000 — lower limit.
   If one is not met, the uncertainty and any additional studies that may be needed (high-Reynolds test, larger facility) are discussed in the report.
2. **Compute the blockage (§1.4, §2.2).** Blockage ratio = (cross-sectional area of the model + proximity models) / (test section area at the location of the model). If no correction is made it must be less than 5%; if it exceeds 5% the justification is given in the report.
3. **Build the geometry correctly (§3.2, §8.1).** The model is an accurate representation of the external surfaces that interact with the wind; the overall dimensions must be accurate to ±2% and particular attention must be paid to the corner radius of curvature. If there are details that cannot be scaled exactly (very thin members) or measurement hardware that disturbs the flow (externally routed pressure tubing), their effect is assessed, minimized and described in the report.
4. **Ensure rigidity (§3.2, §8.1).** The model must behave rigidly over the test velocity range; in rigid model studies the natural frequency of the model must be at least 30% higher than the lowest natural frequency of interest.
5. **Assess Reynolds sensitivity (§3.2).** The Reynolds lower thresholds are observed when choosing the scale. Testing at a single tunnel velocity is allowed only where the Reynolds effect is insignificant; otherwise more than one velocity is required.
6. **Build the proximity model (§2.4).** Buildings, other structures and topographic features that could affect the wind load on the test building are modeled. The standard gives no numerical radius; the criterion is "everything that could affect it".
7. **Choose the directions (§3.2).** The number of directions and/or wind conditions must be sufficient to define the loads and to capture the directions critical for design. A numerical increment exists only in the commentary: in general it should not be greater than 10°, and may be relaxed with justification (§C3.2).
8. **Appurtenances (§2.6).** Loads on appurtenances are measured directly on the model of the main structure if the scaling requirements allow; if not, the flow field at the location of the appurtenance may be determined and reproduced at a larger scale for the measurement.

## Proximity model — what the text says

Mandatory (§2.4, p. 21): only a one-sentence scope requirement — buildings, structures and topographic features that could affect the wind load are modeled. **There is no radius, level of content detail or numerical criterion in the standard text.**

Commentary (§C2.4, pp. 43–44; not binding):
- The aim is to simulate the local wind environment; all objects that contribute significantly to the wind conditions at the site should be included.
- The proximity model rotates on the turntable together with the test building.
- Tall building tests (mostly 1:300–1:500) commonly include a surrounding model with a radius of about 240 m (800 ft) or larger. This size is partly historical: the turntable radius of many facilities is of the order of 1.2–1.5 m (4–5 ft).
- A building that lies outside the turntable but is markedly large relative to its surroundings may be included for the directions in which it falls upwind of the test building.
- The standard gives no minimum radius, because scales in current ABL tests range from about 1:20 to 1:800. The adequacy of the extent is the responsibility of the wind engineer.
- Surrounding buildings may be simplified to a reasonable degree while preserving their cross section, height and prominent features; they should not move under the wind. True north should be marked on the model.
- Because the surrounding model contains topography, if its ground is markedly higher than the tunnel floor, unrealistic separation and acceleration can occur at the leading edge; the leading edge is tapered. The recommended slope is less than 7%.
- Inclusion of future buildings that are highly likely to be built or have been approved should be considered.
- More than one surrounding configuration may be tested; the differences should be documented with photographs, tables or sketches. Typical example: the "reduced sheltering" configuration in which buildings that provide beneficial shelter are removed.
- The blockage ratio is computed from the sum of the test model and the proximity model; the proximity model should not affect the flow at the reference velocity measurement location.

## Blockage — what the text says

- Mandatory: less than 5% unless a correction is made; if exceeded, justification in the report (§2.2, p. 20).
- Commentary: if blockage does not exceed 5%, the longitudinal pressure gradient and other flow distortions are generally acceptable. Larger blockage can often be allowed if special care is taken to control or limit blockage errors, or if analytical/empirical corrections can be shown to be valid (§C2.3.1.1, p. 36). In a test section of constant cross section with a rough floor and a model, if not corrected, the pressure drops markedly in the flow direction and alters separation and reattachment on the model; it is controlled by adjusting the ceiling height.
- **No specific correction formula or method is given in the standard** (not found in the text).

## Reynolds number and rounded structures

- Mandatory lower limits: building Re ≥ 11 000 (Eq. 2-4); roughness Re u*·z0/ν ≥ 2.5 (Eq. 2-5).
- For structures of circular cross section **there is no separate numerical Reynolds threshold in the standard text.** The general requirement is in §3.2: if the Reynolds effect is not insignificant, a single velocity is not enough.
- Commentary (§C3.2, p. 46): for circular structures where the drag crisis is an issue, Re should be considered. The Re range achievable in the tunnel (generally less than one order of magnitude) is not enough to settle the question; model and full scale are often on opposite sides of the drag crisis minimum. The aim is mostly to show that the turbulent approach flow and/or (sometimes exaggerated) model surface roughness reduces or removes the effect of the drag crisis.
- Commentary (§C3.2): on sharp-cornered structures the corner sharpness, and on curved-surface structures the surface roughness, markedly affect separation and reattachment; these details are decisive.
- Commentary (§C5.2.1.2, pp. 55–56): for most sharp-edged structures the failure to achieve Re similarity is not a problem; for circular and curved-surface sections the model–full-scale difference can be marked; for Re-sensitive structures the results should be corrected on the basis of full-scale measurements or test data in the full-scale Re range. For small members such as railings and thin lattice bars the member Re can become very low (e.g. 100 or below); Re can be kept high by reducing the number of members and increasing their width (preserving the open area).

## Mandatory requirements (standard text, "shall")

| Section | Requirement |
|---|---|
| §2.2 | Eq. 2-1 and 2-3 (first relation) within a factor of 3; (xLu/Lb)m ≥ 3 and Re ≥ 11 000 lower limits; if not met, the uncertainty is discussed in the report. |
| §2.2 | Blockage ratio less than 5% unless a correction is made; if exceeded, justification in the report. |
| §2.4 | Buildings, structures and topographic features that could affect the load are modeled. |
| §2.6 | Appurtenance loads are measured directly on the model of the main structure if scaling allows; a larger-scale test that reproduces the local flow is permitted. |
| §3.2 | The model is an accurate representation of the external geometry within the tolerances of §8.1; unavoidable distortions are assessed, minimized and described in the report. |
| §3.2 | The model behaves rigidly over the test velocity range. |
| §3.2 | Reynolds lower thresholds are observed in scaling; a single tunnel velocity only if the Re effect is insignificant. |
| §3.2 | The number of directions/conditions defines the loads and captures the critical directions. |
| §8.1 | Overall model dimensions accurate to ±2%; particular attention to corner radius of curvature. |
| §8.1 | Rigid model natural frequency at least 30% higher than the lowest natural frequency of interest. |
| §1.2 (1) | The report contains the length, velocity and time scale similarity parameters, and the target upwind terrain, surroundings and proximity characteristics. |

## Checklist (when reading a tunnel report; yes/no)

1. Are the geometric scale, velocity scale and time scale given in the report?
2. Is Lb/z0 compatibility (within a factor of 3) shown?
3. Is xLu/Lb compatibility (within a factor of 3, or model value ≥ 3) shown?
4. Is the model Reynolds number (Lb·Ub/ν) ≥ 11 000?
5. Is the blockage ratio given, and was it computed for the model + proximity model together?
6. Is blockage less than 5%; if not, are there a correction and a justification?
7. Are the model dimensional accuracy (±2%) and the corner radius addressed?
8. Are architectural details that project from the facade by 2% or more of the smallest horizontal dimension included in the model? (commentary recommendation, §C8.1)
9. If there are details that cannot be scaled or hardware that disturbs the flow, is their effect described?
10. Is the rigidity / natural frequency of the model (at least 30% margin) documented?
11. Is the extent of the proximity model (radius, buildings included) defined and photographed?
12. Are markedly large buildings outside the turntable addressed?
13. Are future/approved buildings and multiple surrounding configurations (e.g. reduced sheltering) documented?
14. Are true north and the direction definition (coordinate system) given?
15. Is the wind direction increment 10° or finer; if not, is there a justification? (commentary)
16. If there are rounded surfaces, is Reynolds sensitivity (multiple velocities, surface roughness, correction) discussed?
17. If the test was run at a single velocity, is the insignificance of the Reynolds effect justified?
18. If there is complex terrain, was a topographic model or a leading-edge taper (less than 7%) used?

## When comparing with CFD

What must be taken from the report:
- **Scale and model dimensions:** geometric scale, Lb, model height; whether the CFD will be run at model scale or full scale, and hence the Re difference, must be known.
- **Test section dimensions and blockage:** tunnel width/height and blockage ratio. If the tunnel walls will not be modeled in CFD, the blockage effect (and any correction applied) can be a source of difference; if the report says a correction was made, it must be found out to which data it was applied.
- **Extent of the proximity model:** radius, which buildings are included, level of simplification, which surrounding configuration (existing / future / reduced sheltering) belongs to which result. Because the standard gives no numerical radius, this information comes only from the report.
- **Beyond the surrounding model:** in the tunnel there is a boundary layer generated with roughness elements upwind of the surrounding model; the roughness used in CFD from where the surrounding buildings end up to the inlet must be consistent with this.
- **Corner radius and architectural detail:** which details are present on the model (balcony, parapet, sunshade); the CFD geometry must match the level of detail of the tunnel model. Corner sharpness governs separation.
- **Direction definition and increment:** which direction is 0°, sense of rotation, increment (typically 10°). Because the surrounding model rotates with the building, in CFD too the building + surroundings must be rotated together and the inlet profile must stay fixed (if the roughness varies with direction, the direction–profile mapping in the report is used).
- **Reynolds number:** tunnel Re and the roughness/correction applied on rounded surfaces. Between full-scale CFD and the model-scale tunnel the separation point on curved surfaces can differ.
- **Topography:** the leading-edge taper and terrain stepping are artifacts specific to the tunnel; a deliberate decision must be made on whether to copy them exactly in CFD.

## Related skills

- `tunnel-approach-flow` — target profile, turbulence, integral length scale, PTS, topographic model.
- `tunnel-pressure-measurement-and-loads` — pressure measurement, peak value, combination with climate, report.
- `tunnel-other-measurements` — high-frequency force balance, aeroelastic model (Re, Froude), products.
