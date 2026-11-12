---
name: topography-and-non-synoptic-wind
description: Use when the target wind profile comes from a separate topography simulation (topography Method 1, reproduction in the empty domain without the topography) or when asked about simulating non-synoptic wind such as a downburst or tornado; states what Sections 5.2 and 5.3 of the ASCE CWE Prestandard require and what they leave out of scope.
---

# Flow modified by topography and non-synoptic wind (ASCE CWE Prestandard §5.2, §5.3)

Source: PDF pages 53–55. For details see `reference.md`.

## When to use

- When the topography effect is to be represented without placing the topography in the building simulation (Method 1 in Figure 3-2): the target profile is taken from a separate topography simulation and reproduced in the empty domain without the topography.
- When the user wants to compute downburst, thunderstorm or tornado loads by CWE: to convey the position of the document correctly.

If the topography is placed in the proximity model (Method 2), `domain-and-mesh` (PO 6-4) applies, not this skill.

## Step by step — Topography Method 1 (§5.2)

1. Take the target profiles from the separate topography simulation. The document does not describe how this topography simulation is to be done.
2. Set up an empty-domain simulation that does not contain the topography geometry and reproduce the target profiles at the incident location (PO 5-6).
3. Document the computational domain size, the mesh resolution and all boundary conditions (AC 5-6).
4. Report the full turbulence statistics (mean, rms, length scales, spectra) of the three velocity components and the pressure at different heights at the incident location (AC 5-6).
5. Plot the mean and standard deviation velocity and pressure contours in horizontal planes and in streamwise/wall-normal planes; verify with these plots that the profiles do not change unrealistically within the domain (AC 5-6).
6. Show that the target field predicted by the topography simulation is produced correctly at the incident location in terms of the basic velocity statistics relevant to the application (AC 5-6).
7. Repeat this for all relevant wind directions; the topography effect depends on direction (AC 5-6).
8. Apply the AC 5-9 check of the `empty-domain-verification` skill; with Method 1 the error range for U and I_u is 100% of h_max (not the upper 75%).

## Non-synoptic wind (§5.3)

- The document says that a mature approach, ready for use in industry, does not yet exist for non-synoptic wind loads; for this reason explicit simulation of these winds is not expected when this Prestandard is applied (it also refers to §1.5.1).
- This section contains no PO or AC clause; the content is commentary.
- Summary of the methods in the commentary:
  - Downburst: (1) setups that mimic the experimental rig — stationary, moving or pulsed impinging jet (the size and momentum of the jet determine the flow), or a louver array upwind; (2) cooling source term (its intensity, size and travel speed are decisive); (3) weather forecast models.
  - Tornado: (1) tornado-like vortex mimicking the experimental rig; the inflow radius r0, the inflow depth h0 and the tangential/radial inflow velocity conditions determine the vortex; the corner flow region is particularly important because of the high speed and pressure deficit; alternatively a vertical louver array; (2) simulations that include the dominant forcing mechanisms that create the tornado.
  - Alternative approach: instead of modeling the full field, representing particular features of these flows (acceleration, angle of attack, streamline curvature); an active research area.
  - Ground roughness can be included with explicit elements or with a wall function; most existing studies have used a smooth ground.

## Mandatory requirements

- **PO 5-6** — The target profiles from the topography simulation are reproduced at the incident location in an empty-domain simulation that does not contain the explicit geometry of the topography.
- **AC 5-6** — Domain size, mesh and boundary conditions are documented; the full turbulence statistics of the three velocity components and the pressure are reported at different heights; mean and standard deviation contours are plotted in two kinds of plane and it is verified that there is no unrealistic change; the target field is produced correctly at the incident location; this is done for all relevant directions.
- **§5.3** — No mandatory clause; explicit simulation of non-synoptic wind is not expected within this Prestandard.

## Checklist

- [ ] Is the topography really kept outside the building simulation (Method 1)?
- [ ] Does the empty-domain simulation exclude the topography geometry?
- [ ] Were the domain size, the mesh and all boundary conditions documented?
- [ ] Were the mean, rms, length scale and spectrum of the three velocity components reported at more than one height at the incident location?
- [ ] Was the pressure also reported at different heights?
- [ ] Are there mean and standard deviation contours in horizontal and streamwise/vertical planes?
- [ ] Was it shown with plots that the profiles do not degrade within a short distance after the inlet?
- [ ] Was the AC 5-9 error range taken as 100% of h_max?
- [ ] Were all relevant wind directions covered?
- [ ] If non-synoptic wind is requested, was the user told clearly that the document keeps it out of scope?

## Common mistakes

- Imposing the profile from the topography simulation at the inlet only: without the topography the flow returns to the flat-terrain equilibrium boundary layer (commentary).
- Ignoring the difference in equations and numerical methods between the topography simulation and the building simulation; especially with mesoscale weather forecast models (energy and moisture equations, coarse mesh) the profiles can change unrealistically near the inlet (commentary).
- Verifying in one direction and generalizing to the other directions.
- Leaving the error range limited to the upper 75% with Method 1.
- Presenting the commentary in §5.3 as if it were a design method; the document gives no acceptance criterion for downbursts and tornadoes.
- Assuming that the document gives a method for the topography simulation itself; it does not.

## Related skills

- `empty-domain-verification` — §5.1, §5.4; AC 5-9 criteria.
- `domain-and-mesh` — placing the topography in the proximity model (PO 6-4), including it in the blockage calculation (AC 6-8b).
- `boundary-conditions-and-quality` — roughness model on the topography (AC 6-11).
