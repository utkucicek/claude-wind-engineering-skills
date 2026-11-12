---
name: design-wind-loads
description: Use when deriving design wind loads from CFD/LES (CWE) results; applies the ASCE CWE Prestandard Chapter 7 requirements for pressure coefficient (Cp) definition and reference velocity, peak estimation (Gumbel, extreme value), the components and cladding (C&C) versus MWFRS split, combination with wind climate and directionality, internal pressure, the ASCE 7 limitation and DAF.
---

# Design wind loads (ASCE CWE Prestandard, Chapter 7)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 7.
Page numbers are PDF sequence numbers (printed page = PDF page − 18). Clause-by-clause breakdown: `reference.md`.

Abbreviations: PO = Performance Objective, AC = Acceptance Criterion,
CWE = computational wind engineering, MWFRS = main wind force resisting
system, C&C = components and cladding,
AHJ = Authority Having Jurisdiction, DAF = dynamic amplification factor.

## When to use

- When design loads (base shear, overturning moment, story-by-story loads, cladding pressures) are to be derived from the pressure/force time series of an LES run.
- When asked how the peak pressure coefficient is to be estimated, or whether the single observed peak value may be used.
- When the CFD result is to be combined with the wind climate (return period, direction).
- When internal pressure, net pressure, or appurtenance loads (sunshades, canopies, rooftop equipment, parapets) are to be calculated.
- When asked about the relation of the CFD load to ASCE 7 / its lower limit.

Out of scope: tornadoes and other non-synoptic events (§7.7; the document gives no explicit method).

## Step by step

1. **Classify the structure (§7 introduction, §1.8).** Rigid, flexible or aeroelastic. The document gives no frequency-based limit; the ASCE 7-22 limit is considered a good indicator but does not cover every structure type (introductory text of COMMENTARY nature).
2. **Set the wind directions (PO/AC 7-1).** Azimuth increment at most 10°. If the results indicate the possibility of a larger design load, intermediate directions are added. The number of directions may be reduced only with justification + approval of the peer review team + AHJ (commentary).
3. **Monitor the reference velocity (PO/AC 7-2).** The reference wind speed is monitored and documented at a point where the influence of the proximity model is minimal. Commentary: typically either at a height considered to be outside the boundary layer, or at structure height and upwind of the explicitly modeled surroundings. If a conversion to another height is made, it is documented in detail.
4. **Compute the pressure coefficients (PO/AC 7-13, Eq. 7-6).** For each monitoring point, the mean, standard deviation (rms), minimum and maximum external pressure coefficient; all divided by the reference dynamic pressure (q_ref = ½·ρ·U_ref²). These four coefficients are required for transparency and peer review.
5. **MWFRS aerodynamic response (PO 7-5).** Surface forces are integrated over each boundary face. Preferred route: perform the integration during the run over predefined tributary areas — whole building (base shear/moment), building segment (section forces), single story (story-by-story loads) (AC 7-5a). Integration of pressure time series at discrete points is also accepted; the point distribution must be dense enough to capture the load effect correctly (AC 7-5b). The force on elements modeled as porous media is included in the total load (AC 7-5c).
6. **MWFRS design load and dynamic response (PO/AC 7-6, §7.3).** All structural systems are assumed flexible; a method suitable only for a rigid structure is used only if the technical justification is documented in detail. Frequency or time domain is free; in every case the DAF is reported.
7. **Presentation of MWFRS results (PO/AC 7-7).** Peak loads and structural effects are given either as equivalent static wind loads or as force/pressure time series to be applied directly to the structural model.
8. **C&C local peak pressures (PO/AC 7-8, 7-9).** Monitoring points are selected according to the complexity of the external geometry and the pressure gradient; denser points are recommended for small buildings and in high-gradient regions (roof corners, edges, ridges, wall edges). The direct integration (integral) method may also be used; the size and distribution of the tributary areas are chosen consistently with the monitoring point principles. An allowance for internal pressure is included.
9. **Estimate the peak design load (PO 7-10).** The peak value is determined with an extreme value distribution, for a duration and probability level suitable for combination with the wind climate. The probability of exceedance is reported (AC 7-10a). No filter that removes frequencies that may be related to aerodynamic phenomena is applied (AC 7-10b). The single observed peak coefficient is not used (in the commentary text, with "shall not" wording). For the method options see the "Peak value methods" table below.
10. **Net and internal pressure (PO 7-11, 7-12).** The net pressure coefficient of appurtenances is found by direct derivation of the net pressure. Internal pressure is either estimated analytically from the simulated external pressures or resolved directly in the simulation; porosity, leakage and openings are considered for different scenarios.
11. **Appurtenances (PO 7-14, 7-15).** Loads are taken from the same computational model as the main structure; for a rigid appurtenance the statistical approach of §7.4.3, for a flexible appurtenance the DAF per §7.3.2.
12. **Combine with the wind climate (PO 7-4).** One of the six accepted methods is selected; all weather systems at the site are taken into account; the assumptions and the combination method are documented in detail.
13. **Limitation and consistency check (PO 7-3).** The load is determined without relying on future changes of the surroundings (e.g. demolition of a neighboring building). MWFRS and C&C loads are limited according to the methods in ASCE/SEI 7-22 (AC 7-3a). The statistically stationary force/moment coefficients are checked to confirm that any load reduction is consistent with what is expected for the building type and shape (AC 7-3b).
14. **Design load quality check (PO/AC 7-16).** The integrated forces and moments are plotted about a reference point (usually the base or the structural origin): for each component, mean, minimum, maximum versus direction. The spectral response is plotted for the critical directions. Commentary: the results of the other meshes in the mesh study should also be added to the same plots.

## Peak value methods (§7.4.3 commentary, PDF p. 76)

| Method | What the text says |
|---|---|
| Ensemble average | The average of several maximum/minimum values taken from segments of equal length; the segment is scaled to represent a suitable full-scale observation duration (as an example, 10 min – 1 h). One of the two common methods. |
| Gumbel fitting | The peak corresponding to a specified fractile level is estimated from the extreme values of segments of equal length. The other of the two common methods. |
| Method of independent storms, BLUE (best linear unbiased estimator), peak-over-threshold | Mentioned as other recognized extreme value methods. |
| Cook–Mayne | An extension of Gumbel fitting that combines the extreme value distributions of the load and the wind speed; gives the most accurate result but requires knowledge of the extreme wind climate, so it is not suitable for generic coefficients of products to be used in different climates. |

NOT in the text: number of segments, fractile level (e.g. a value such as 78%), minimum record duration for Gumbel. Do not state these on behalf of the document.
The record duration requirement is in Chapter 6: the simulation duration must be longer than 500 times the longitudinal integral time scale at the target building height (AC 6-14, PDF p. 66). There is no numerical threshold for the sampling resolution; the choice is required to be justified in the report (AC 6-13d, PDF p. 66).

## Methods of combination with the wind climate (AC 7-4a; commentary PDF pp. 70–73)

| Method | Summary (commentary text) |
|---|---|
| Upper bound / nondirectional | The simplest and most conservative. Directionality is ignored; the largest response over all directions is paired with the design speed. It can also be used with ASCE 7-22 speeds without a climate analysis; in that case no distinction by storm type is needed. |
| Normalized sector | Simple; mostly conservative, can rarely turn out unconservative. Requires a directional combined climate model. |
| Multisector | The response–exceedance probability is computed for each sector; statistical independence of the extreme winds in the sectors is assumed. Applied separately for thunderstorms and extratropical storms. |
| Up-crossing | Based on the parent probability distribution (usually two-parameter Weibull); current practice does not separate thunderstorms. |
| Storm passage | The largest response is found from the speed–direction time series of each simulated tropical cyclone. |
| Direct simulation | A large data set is generated by Monte Carlo from directional extreme value distributions. |

Commentary: there is no explicit relation between the R-year wind speed and the R-year wind effect; the effect should be found per storm type and then combined (Eq. 7-1; the equation could not be read in the text).
The directional resolution of the climate model is often coarser than the CWE data; the assumptions made when combining the two data sets are written in the report.

## Mandatory requirements

- PO 7-1 / AC 7-1 (§7.1.1): direction increment ≤ 10°; additional directions if a larger load is possible.
- PO 7-2 / AC 7-2 (§7.1.2): the reference velocity is monitored and documented at the location least affected by the proximity model.
- PO 7-3 / AC 7-3a, 7-3b (§7.1.3): future changes of the surroundings are not relied upon; loads are limited according to the ASCE/SEI 7-22 methods; load reduction is checked for consistency with the stationary force/moment coefficients.
- PO 7-4 / AC 7-4a, 7-4b (§7.2): one of the six statistical methods; all weather systems; assumptions are documented.
- §7.3 introduction: all systems are assumed flexible; rigid method only with documented justification.
- PO 7-5 / AC 7-5a–c (§7.3.1): integration of surface forces; porous media forces included.
- PO 7-6 / AC 7-6 (§7.3.2): the DAF is reported in every case.
- PO 7-7 / AC 7-7 (§7.3.3): peak loads and effects are presented (equivalent static load or time series).
- PO 7-8 / AC 7-8 (§7.4.1): pressure data for C&C + allowance for internal pressure; monitoring points in sufficient number and in the right places.
- PO 7-9 / AC 7-9 (§7.4.2): in the integration method, tributary areas with sufficient spatial resolution.
- PO 7-10 / AC 7-10a, 7-10b (§7.4.3): extreme value distribution; exceedance probability reported; no filter that removes aerodynamic frequencies.
- PO/AC 7-11 (§7.4.4): net pressure is derived directly.
- PO 7-12 / AC 7-12a–c (§7.4.5): internal pressure; internal volume scaling if not at full scale; partially enclosed cavities.
- PO/AC 7-13 (§7.4.6): mean, rms, minimum, maximum external pressure coefficients.
- PO 7-14 / AC 7-14a, 7-14b (§7.5.1): appurtenances from the same model; rigid/flexible distinction.
- PO/AC 7-15 (§7.5.2): product test report content (effective wind area relation, conversion to coefficients, conditions of applicability).
- PO/AC 7-16 (§7.6): force/moment plots and critical-direction spectra.

## Checklist (yes/no)

- [ ] Is the direction increment 10° or smaller? If larger, is there justification + peer review + AHJ approval?
- [ ] Do the results indicate the possibility of a larger load at an intermediate direction; if so, were additional directions run?
- [ ] Were the point and height at which the reference velocity is monitored documented; is it away from the influence of the proximity model?
- [ ] If the coefficients were converted to another height, was the conversion written out in detail?
- [ ] Were Cp mean, rms, minimum, maximum given for each point?
- [ ] Was the peak value found with an extreme value statistic (NOT the single observed peak)?
- [ ] Was the probability of exceedance reported?
- [ ] Was it confirmed that no filter that could remove aerodynamic frequencies was applied to the time series?
- [ ] Is the simulation duration longer than 500 longitudinal integral time scales (AC 6-14)?
- [ ] Were the MWFRS forces integrated over defined tributary areas; are the forces on porous elements included?
- [ ] Was the structure assumed flexible; if not, was the justification documented?
- [ ] Was the DAF reported?
- [ ] Was it stated how internal pressure was handled (analytical / direct / code value); were opening and leakage scenarios considered?
- [ ] Is the wind climate combination method one of the six methods, and were its assumptions written down?
- [ ] Was the load determined without relying on future changes of neighboring structures?
- [ ] Was the limitation per ASCE/SEI 7-22 applied; is the load reduction consistent with the coefficients?
- [ ] Are there mean/minimum/maximum force-moment plots versus direction and critical-direction spectra?

## Common mistakes

- Taking the single largest/smallest Cp value in the record as the design value. The document says its repeatability is poor and that it depends on the test duration.
- Filtering the time series to reduce noise and in doing so removing frequencies of aerodynamic origin (AC 7-10b).
- Attributing numbers to the document that it does not contain: the Gumbel fractile level, the number of segments, lower-limit ratios such as a percentage of ASCE 7 are not in the Chapter 7 text; it says "limited according to the ASCE/SEI 7-22 methods".
- Finding the CFD load low only thanks to the sheltering of a neighboring building and carrying this into the design (PO 7-3).
- Skipping the dynamic component under a rigid-structure assumption; the document requires the flexible assumption by default.
- Not reporting the DAF.
- Forgetting internal pressure and designing the cladding with external Cp only.
- Taking the reference velocity from a point affected by the structure or the surroundings model.
- Not adding the force on elements modeled as porous media to the total load.
- Using this chapter for tornado loads (§7.7 out of scope; the commentary only touches on the use of base coefficients with ASCE/SEI 7-22 Chapter 32).

## Not in the text (do not invent)

- Numerical area size for area averaging of cladding: not found in the text. There is only the tributary area selection principle (AC 7-9) and the requirement for local + area-averaged cladding pressures in the report (§9.4.5.8).
- A separate "uncertainty" clause in Chapter 7: not found in the text. Uncertainty assessment is a reporting requirement in §9.5.4.
- The only number for pressure point density is in the commentary: as the AWES-QAM-1 recommendation, at least 1 point per 120 m² (about 1,300 ft²) of surface at full scale; in CWE it should be at least consistent with wind tunnel practice (COMMENTARY, PDF p. 74).

## Related skills

- `skills/quality/quality-assurance` — Table 8-1 compliance matrix, mesh and time-step studies, statistical convergence.
- `skills/quality/report-and-peer-review` — how the results produced in this chapter are presented in the report, and peer review.
- `skills/process/target-wind-definition` — wind climate and target flow (Chapter 3).
- `skills/simulation/empty-domain-verification`, `skills/simulation/domain-and-mesh`, `skills/simulation/boundary-conditions-and-quality` — approach flow and building aerodynamics simulation (Chapters 5–6); record duration and monitoring point requirements.
- `skills/wind-tunnel/tunnel-pressure-measurement-and-loads` — the counterpart on the wind tunnel side.
