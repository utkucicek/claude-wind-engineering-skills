---
name: empty-domain-verification
description: Use when it has to be demonstrated, before the building is added, that the approach flow in the empty domain matches the target atmospheric boundary layer at the incident location; checks the inflow turbulence (precursor, recycling, synthetic inflow), ground roughness z0, U and I_u profile error, integral length scale, spectrum, cutoff frequency and pressure fluctuation criteria against Sections 5.1 and 5.4 of the ASCE CWE Prestandard.
---

# Empty-domain verification (ASCE CWE Prestandard §5.1 and §5.4)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Sections 5.1 and 5.4 (PDF pages 49–58). For clause details and equations see `reference.md`.

## When to use

- When setting up the first step of the two-step simulation process: the approach flow simulation for synoptic wind in the computational domain (CD) without the building.
- When choosing the inflow turbulence method, or when the change of turbulence from the inlet to the incident location is questioned.
- When the question "does the empty-domain profile match the target?" is to be answered with a numerical criterion (AC 5-9).
- When checking whether the mesh in the approach flow region resolves a sufficient frequency (AC 5-2, AC 5-10).
- When writing the report of the empty-domain run (which plots, which statistics).

If a target profile modified by topography or a non-synoptic wind is involved, switch to the `topography-and-non-synoptic-wind` skill.

## Key concepts

- **Incident location:** The most upwind location in the computational domain where a building or topography is added (§1.8, p. 24; AC 4-1, p. 43). PO 5-3 makes it coincide with the location of the most upwind building or structure in the building simulation. If surrounding buildings are modeled explicitly, this is not the position of the target building but the upwind edge of the modeled surroundings (consistent with AC 6-7).
- **Approach flow region:** The mesh region from the inlet boundary up to the study region, and including it (§1.8, p. 24).
- **h_max:** The larger of the building height and the average height of the surrounding buildings (§1.9, p. 26).
- **L_b:** Characteristic dimension appropriate to the problem studied; **n:** highest fully resolved frequency (Hz); **U:** local reference velocity that produces the load (AC 5-2).

## Step by step

1. **Fix the target.** The target profiles (U, turbulence intensities, length scales, z0) come from Chapter 3. If the terrain roughness changes with wind direction, each different exposure condition requires a separate empty-domain verification (AC 5-3).
2. **Size the computational domain (PO 5-1 / AC 5-1).**
   - Height: it should contain the relevant part of the boundary layer and satisfy the vertical blockage requirement of the building simulation (see §6.3; `domain-and-mesh`).
   - Streamwise length: larger than the distance between the inlet and the first building in the building simulation, and able to carry the streamwise length scales at the location of the first building.
   - Width: able to carry the lateral length scales.
   - The text gives no numerical multiple (for example "how many H") for these dimensions.
3. **Choose the approach flow region mesh (PO 5-2 / AC 5-2).** The highest fully resolved reduced frequency shall be n·L_b/U ≥ 2 for components and cladding (C&C) loads and n·L_b/U ≥ 1 for overall (global) loads; this frequency shall lie in the inertial subrange of the spectrum.
4. **Choose the inflow turbulence method (PO 5-3; commentary).** The text imposes no method; the commentary describes three families and their pitfalls:
   - Precursor simulation and recycling: can be run in advance and written to a database. A periodic/recycling setup of insufficient length can lead to locking of large structures; shifting the periodic condition may be necessary.
   - Synthetic turbulence generation: efficient, but (i) it can produce spurious pressure fluctuations, (ii) the turbulence intensity specified at the inlet usually decreases by the time it reaches the incident location. For this reason the development from the inlet to the incident location should be monitored closely; if there is a marked change, the inlet statistics can be adjusted so as to match the target downstream.
   - Finding the right setup may require trial and error (it is compared to adjusting roughness elements in a wind tunnel).
5. **Set up the ground condition (PO 5-4 / AC 5-4).** It shall reproduce the incident flow for the target z0. Two routes (commentary): resolving the roughness elements explicitly, or a near-wall model. If a wall function is used, verify that it was written for wind over rough terrain and that its input is z0; functions based on sand-grain roughness are not directly suitable.
6. **Set up the side, top and outlet boundaries (PO 5-5 / AC 5-5).** The text requires only that they are "appropriate"; the options in the commentary: periodic on the sides; slip wall or far-field pressure on the top; or no-slip walls as in a wind tunnel (if far enough away); zero gradient or convective condition at the outlet, with damping if necessary.
7. **Run and document solver convergence (AC 4-6b).** The convergence criterion is applied throughout the run and reported. Commentary: with an iterative solver a drop of three to four orders of magnitude in the residuals is expected at every time step.
8. **Discard the initial transient, show statistical convergence (PO 5-7 / AC 5-7).** T_init (the discarded initial transient) and T_avg (the averaging time) are reported; it is shown that the mean velocity and turbulence intensities at building height have converged. The text gives no numerical duration here; the simplest method in the commentary is to monitor the mean and standard deviation with a growing window.
9. **Produce the field plots (PO 5-8 / AC 5-8).** For each different boundary layer condition: instantaneous velocity and pressure snapshots; mean streamwise velocity, standard deviation of the three velocity components (or turbulence intensities), mean pressure and standard deviation of the pressure fluctuation. Planes: (1) vertical plane at mid-width, (2) horizontal plane at building height.
10. **Compare with the target at the incident location (PO 5-9 / AC 5-9).** At mid-width and at the 1/3-width positions measured from the centerline:
    - (1a) (z0/L_b) model = (z0/L_b) prototype, within a factor of three.
    - (1b) U profile error < 10% over the upper 75% of h_max; with Topography Method 1 the range is 100% of h_max. The measure is the relative error integrated over height in Equation 5-1 (≤ 0.1).
    - (2) The same requirement for the I_u profile, Equation 5-2.
    - (3) The required integral length scale components within a factor of three of the target.
    - (4) The power spectra of the required velocity components are plotted at roof/top height.
    - (5) The required Reynolds stress profiles are plotted; the cross-spectra are plotted at roof/top height.
    - (6) The profile of the standard deviation of the pressure fluctuation is plotted; it shall not exceed 10% of the dynamic pressure computed with the roof/top reference velocity.
11. **Show mesh adequacy in the spectrum (PO 5-10 / AC 5-10).** The cutoff frequency is marked on the streamwise velocity spectrum and it is verified that it satisfies AC 5-2. The route in the commentary for the cutoff frequency is Equations 5-3 – 5-5 (5-3 is corrupted in the text; `reference.md`).
12. **If a requirement is not met**, change the inlet/ground/mesh and repeat steps 7–11; move on to the building simulation only after that (see `boundary-conditions-and-quality`, PO 6-1).

## Mandatory requirements

- **PO 5-1 / AC 5-1** — The domain size shall represent the target flow correctly, with no boundary effect; the qualitative requirements above for height, streamwise length and width.
- **PO 5-2 / AC 5-2** — n·L_b/U at least 2 (C&C), at least 1 (overall load); this frequency in the inertial subrange.
- **PO 5-3** — The inlet condition, together with the model and the mesh, shall produce the target turbulent flow at the incident location; the incident location is the location of the most upwind building/structure.
- **AC 5-3** — If the exposure changes with direction, the quality is demonstrated for each different exposure condition.
- **PO 5-4 / AC 5-4** — The ground condition shall reproduce the incident flow for the target z0.
- **PO 5-5 / AC 5-5** — The side, top and outlet conditions shall allow the target flow to be modeled correctly.
- **AC 4-6b (§5.4.1)** — The convergence criterion is applied throughout the run and reported.
- **PO 5-7 / AC 5-7** — T_init and T_avg are reported; convergence of U and the turbulence intensities at building height is shown.
- **PO 5-8 / AC 5-8** — Instantaneous and statistical field plots, in two planes, for each different boundary layer condition.
- **PO 5-9 / AC 5-9** — Six-item comparison at the incident location (step 10 above).
- **PO 5-10 / AC 5-10** — The cutoff frequency is shown on the spectrum and verified against AC 5-2.

## Checklist

- [ ] Has the incident location been defined as the place where the most upwind building/topography will go in the building simulation (not the position of the target building)?
- [ ] Does the domain height also satisfy the vertical blockage requirement of the building simulation?
- [ ] Is the inlet–incident location distance larger than the inlet–first building distance in the building simulation?
- [ ] Is n·L_b/U ≥ 2 satisfied if C&C loads are required, ≥ 1 if only overall loads are required?
- [ ] Is this highest frequency inside the inertial subrange of the spectrum?
- [ ] Was the wall function written for wind over rough terrain, and is its input z0?
- [ ] Are (z0/L_b) of the model and of the prototype within a factor of three?
- [ ] Is the Equation 5-1 error for U ≤ 0.1 (upper 75% of h_max; 100% with Topography Method 1)?
- [ ] Is the Equation 5-2 error for I_u ≤ 0.1 (same range)?
- [ ] Was the comparison made both at mid-width and at the 1/3-width positions?
- [ ] Are the required integral length scales within a factor of three of the target?
- [ ] Were the spectra and cross-spectra plotted at roof/top height; were the Reynolds stress profiles plotted?
- [ ] Is the standard deviation of the pressure fluctuation below 10% of the roof-height dynamic pressure?
- [ ] Were T_init and T_avg reported; was convergence at building height shown?
- [ ] Are there instantaneous and statistical field plots in two planes?
- [ ] Is the cutoff frequency marked on the spectrum plot?
- [ ] Were all of these repeated for each different direction-dependent exposure condition?
- [ ] Are the solver convergence criterion and its check in the report?

## Common mistakes

- Doing the verification at the position of the target building; if surrounding buildings are modeled, the incident location is the upwind edge of the surroundings.
- Regarding it as sufficient that the inlet profile matches the target; the requirement is at the incident location, not at the inlet, and with synthetic turbulence the intensity can drop along the way.
- Checking only the mean velocity profile; I_u, the length scale, the spectrum and the pressure fluctuation are also required.
- Not checking the spurious pressure fluctuation produced by a synthetic inlet (AC 5-9 item 6).
- Entering z0 into a mechanical-engineering type wall function with sand-grain roughness.
- Comparing only on the centerline; the 1/3-width positions are also required.
- Estimating the cutoff frequency from the mesh and not showing it on the spectrum.
- Using a mesh, solver, subgrid-scale model or boundary condition in the building simulation that differs from the empty domain (AC 6-1, AC 6-9a).
- Attributing to this section numbers that are not in the text ("5H" for the domain length, a fixed value for the duration); §5.1 and §5.4 do not give them.

## Related skills

- `topography-and-non-synoptic-wind` — §5.2, §5.3.
- `domain-and-mesh` — §6.2–6.4: blockage ratios, mesh regions.
- `boundary-conditions-and-quality` — §6.1, §6.5, §6.6: keeping the same setup in the building simulation, IRQ, sampling duration.
