---
name: boundary-conditions-and-quality
description: Use when setting up the boundary conditions (no-slip wall, wall model, y+, reference static pressure) of a building aerodynamics LES simulation and when performing or reporting its quality assurance (solver convergence, contour plots, monitoring probes, statistical convergence, sampling duration, mesh sensitivity, IRQ, time-step sensitivity, CFL); gives the requirements of Sections 6.1, 6.5 and 6.6 of the ASCE CWE Prestandard.
---

# Boundary conditions and quality assurance (ASCE CWE Prestandard §6.1, §6.5, §6.6)

Source: PDF pages 59 and 64–68. The clause table and equations are in `reference.md`.

## When to use

- When the empty-domain verification is finished and the building has been placed in the computational domain: to check the consistency of the setup with the empty domain.
- When choosing the wall treatment on the building surface (resolved wall or wall model).
- When asked where the reference static pressure is to be read.
- When planning the run duration, initial transient, mesh sensitivity and time-step sensitivity.
- When writing or checking the quality assurance section of the building simulation report.

## Step by step

1. **Keep the same setup as the empty domain (PO 6-1 / AC 6-1).** The geometric and velocity scale, solver, numerical methods, turbulence model, ground wall model and boundary conditions are the same as in the approach flow simulation. The aim is that the building simulation gives the empty-domain result in the same physical region.
2. **Set up the building surface (PO 6-10).**
   - The surface is a no-slip wall; the near-wall treatment is consistent with the near-wall mesh resolution (AC 6-10a).
   - If the near-wall flow is sufficiently resolved (y+ = y·u*/ν < 5) the no-slip condition is applied directly; if it is less resolved a wall model is used (AC 6-10a).
   - For special boundaries such as a porous surface, dedicated verification and validation is carried out (AC 6-10a).
   - If the building has a rounded shape (the separation location is not fixed by a sharp edge), the effect of the wall model is examined (AC 6-10b).
   - Additional runs are made with the near-wall resolution or the wall model changed, and the effect of the wall treatment on the pressure distribution is quantified (AC 6-10c).
3. **Set up the other boundaries (PO 6-11 / AC 6-11).** The inlet, outlet, ground, sides and top comply with §5.1.2 and §5.1.3. If a topography model is in the domain, the terrain roughness of the topography is also represented by an appropriate roughness model. Commentary: in a forested area a canopy model is more reliable than a wall function based on z0 alone.
4. **Manage solver convergence (AC 4-6c).** The solution converges sufficiently at every time step; the criterion is met throughout the run; the criterion and the checks are reported.
5. **Produce the flow field plots (PO 6-12 / AC 6-12a).** For every wind direction simulated, contours of the mean, standard deviation (or turbulence intensity) and instantaneous snapshot of wind speed and pressure; without interpolation, with cell-center values:
   - Horizontal planes: h/2, 2h/3, h and h + 5 m (16 ft); an area covering at least the first row of surrounding buildings.
   - Vertical plane(s) through the middle of the building(s); same extent.
   - The plots shall show the separation regions (roof, sides) and the wake.
6. **Define the monitoring points (AC 6-12b).** Point probes along the building height and out to about 50 m (160 ft) from the building; their positions are chosen according to the geometry; they capture the upwind flow (especially the wakes of upwind buildings) and the building wake. For each point: a representative portion of the velocity and pressure time signal; the mean, standard deviation and turbulence intensity of the velocity; the velocity spectrum.
7. **Surface pressure plots and pressure taps (PO 6-13).**
   - Mean and standard deviation pressure contours on all facades, on the roof and, if necessary, on the appurtenances; special attention to the high-gradient regions at edges and corners (AC 6-13a).
   - Pressure taps are placed according to the guidance of ASCE/SEI 49-21 (AC 6-13b).
   - The tap density is sufficient to capture the variation over the surface for MWFRS and components and cladding (C&C) studies (AC 6-13c); the choice of sampling resolution is justified (AC 6-13d).
8. **Take the reference static pressure (AC 6-13e).** The reference pressure point is positioned so that it is not affected by the model, the proximity model or the boundaries; a static pressure monitoring point placed directly above the study region is used.
9. **Show statistical convergence (PO 6-14 / AC 6-14).** At the monitoring points the mean and standard deviation of the velocity, and the mean, standard deviation and peak values of the load quantities of interest, shall have converged. The simulation duration is larger than 500 times the streamwise integral time scale at the height of the target building. Commentary: the simplest check is a growing window; for peak values, block maxima or peaks-over-threshold.
10. **Do a mesh study (PO 6-15 / AC 6-15a, 6-15b).** In at least two wind directions for the project. IRQ at least 75% in the flow and pressure field at the monitoring points; the differences in the load quantities between two meshes are reported. IRQ calculation (commentary): at most three meshes (coarse, medium, fine), successive refinement factor r; IRQ = k_resolved / k_total, k_total = k_resolved + a_k·Δ^p (Equations 6-3 – 6-6, `reference.md`).
11. **Examine time-step sensitivity (PO 6-16 / AC 6-16).** Velocity spectra are plotted at key locations around the building and between the target building and the upwind buildings; the cutoff arising from the mesh size and from the time step is marked on the plot. Commentary: halving the time step and comparing the spectra is a good method; or it is enough to keep the CFL number constant in the mesh sensitivity study.

## Mandatory requirements

- **PO 6-1 / AC 6-1** — The same scale, solver, numerical method, turbulence model, ground wall model and boundary conditions as the empty domain.
- **PO 6-10 / AC 6-10a–c** — No-slip wall; directly if y+ < 5, otherwise a wall model; effect of the wall model for a rounded shape; quantification of the effect by additional runs.
- **PO 6-11 / AC 6-11** — Other boundaries according to §5.1.2 and §5.1.3; topography roughness is modeled.
- **AC 4-6c (§6.6.1)** — Convergence at every time step; report of the criterion and the check.
- **PO 6-12 / AC 6-12a, 6-12b** — Contours in four horizontal planes and the vertical plane; monitoring points within ~50 m and their time signal, statistics and spectrum.
- **PO 6-13 / AC 6-13a–e** — Surface pressure contours; pressure taps according to ASCE/SEI 49-21; adequate tap density and its justification; reference static pressure above the study region.
- **PO 6-14 / AC 6-14** — Statistical convergence; duration > 500 streamwise integral time scales (at the height of the target building).
- **PO 6-15 / AC 6-15a, 6-15b** — Mesh study in at least two directions; IRQ ≥ 75%; report of the differences; definition of the monitoring points.
- **PO 6-16 / AC 6-16** — Time-step sensitivity; mesh and time-step cutoff marked on the spectra.

## Checklist

- [ ] Are the solver, numerical schemes, subgrid-scale model, ground wall model and boundary conditions exactly the same as in the empty-domain run?
- [ ] Is the building surface a no-slip wall?
- [ ] If y+ < 5 does not hold, is a wall model used?
- [ ] For a rounded building, was the effect of the wall model examined?
- [ ] Was the effect of the wall treatment on the pressure distribution quantified by additional runs?
- [ ] If topography is in the domain, was its roughness modeled?
- [ ] Was the convergence criterion met at every time step and reported?
- [ ] Are there contours in the horizontal planes h/2, 2h/3, h and h + 5 m for every direction?
- [ ] Were the contours plotted with cell-center values without interpolation?
- [ ] Do the planes cover at least the first row of surrounding buildings?
- [ ] Are the monitoring points along the building height and within ~50 m, so as to cover the upwind wakes and the building wake?
- [ ] Were the time signal, mean, standard deviation, turbulence intensity and spectrum presented for every monitoring point?
- [ ] Are there mean and standard deviation pressure contours on all facades and on the roof?
- [ ] Does the pressure tap layout comply with ASCE/SEI 49-21, and is its density justified?
- [ ] Is the reference static pressure taken from directly above the study region, at an unaffected point?
- [ ] Is the simulation duration longer than 500 integral time scales?
- [ ] Was it shown that the mean, standard deviation and peak values of the load quantities have converged?
- [ ] Was the mesh study done in at least two wind directions, and is IRQ ≥ 75%?
- [ ] Were the load differences between the two meshes reported?
- [ ] Are the mesh and time-step cutoffs marked on the spectra?

## Common mistakes

- Using a scheme, subgrid-scale model or ground model in the building run that differs from the empty domain; the empty-domain verification loses its validity.
- Applying the no-slip wall directly without looking at the y+ value or, conversely, leaving the wall model unquestioned on a fine mesh.
- Skipping the wall model sensitivity for a building that is not sharp-edged.
- Taking the reference pressure from the inlet, the outlet or a point under the influence of the building.
- Plotting the contours smoothed by interpolation to the nodes; the document requires the cell-center value.
- Confusing the 500 integral time scales with a different time scale (for example the flow-through time) instead of the total duration; the integral time scale is the integral length scale divided by the mean velocity at the same height (§1.8).
- Doing the mesh study in a single direction; at least two directions are required.
- Blindly taking the theoretical order for p in the IRQ calculation; if the estimated order is markedly higher than the theoretical one, this can understate the subgrid-scale contribution (commentary).
- Expecting full mesh independence in implicit LES; the commentary says this would only happen at direct numerical simulation (DNS) fineness.
- Attributing things that are not in these sections: the total number of wind directions, a numerical CFL limit and the definition of the reference velocity for the building simulation were not found in §6.1, §6.5, §6.6.

## Related skills

- `empty-domain-verification` — §5.1.2, §5.1.3 boundary conditions; AC 5-9 incident flow criteria.
- `domain-and-mesh` — §6.2–6.4: geometry, blockage, mesh regions, AC 6-9e.
- `topography-and-non-synoptic-wind` — §5.2, §5.3.
