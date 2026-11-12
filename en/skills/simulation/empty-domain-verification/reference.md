# Reference: ASCE CWE Prestandard introduction to §5, §5.1 and §5.4

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Page numbers are PDF page order. The summaries are written in our own sentences; they are not quotations.

Type: MANDATORY = shall, RECOMMENDED = should, COMMENTARY = commentary (not binding).

## Clauses

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §5 introduction | MANDATORY | Approach flow simulations also satisfy all the PO/AC clauses of §4.2 (method, discretization, unresolved turbulence model, solver convergence, geometric and velocity scale). | none | 49 |
| §5 introduction | COMMENTARY | The content of the chapter is equally applicable to LES for pedestrian comfort/safety and air quality. | none | 49 |
| PO 5-1 | MANDATORY | The domain size is chosen so as to represent the target flow correctly and to avoid unwanted effects of the boundary conditions. | none | 49 |
| AC 5-1 | MANDATORY | The height contains the relevant part of the boundary layer and satisfies the vertical blockage requirement of the building simulation (§6.3). The streamwise length is larger than the inlet–first building distance in the building simulation and long enough to represent the streamwise length scales at the location of the first building. The width is sufficient to represent the lateral length scales. | No numerical multiple given; for vertical blockage §6.3 (BR_z ≤ 17%) | 49 |
| AC 5-1 commentary | COMMENTARY | A small domain distorts the turbulence and the length scales. With a lateral periodic condition, unwanted coupling of the two sides can produce artificial large structures. The three turbulence intensities, the spectrum and length scale of the streamwise component and flow visualization together show the adequacy of the domain. | none | 49–50 |
| PO 5-2 | MANDATORY | In the approach flow region the mesh is fine enough to capture the small-scale turbulence that matters for the subsequent building simulation; the measure is the highest reduced frequency in the incident flow power spectrum. | none | 50 |
| AC 5-2 | MANDATORY | The highest fully resolved reduced frequency is at least 2 for components and cladding (C&C) loads and at least 1 for overall loads. L_b is the characteristic dimension appropriate to the problem, n the highest fully resolved frequency, U the local reference velocity that produces the load. It is verified that this frequency lies in the inertial subrange. | n·L_b/U ≥ 2 (C&C); n·L_b/U ≥ 1 (overall load); n [Hz], dimensionless ratio | 50 |
| AC 5-2 commentary | COMMENTARY | The value 2 comes from the contribution of small-scale turbulence in the incident flow to the pressure fluctuations that lead to peak loads; for overall loads this contribution decreases, so the requirement is relaxed. n is taken as the highest frequency at which the streamwise velocity spectrum remains consistent with the −2/3 slope in the inertial subrange (Figure 5-2). | slope −2/3 (reduced spectrum) | 50–51 |
| PO 5-3 | MANDATORY | The turbulent inlet condition, together with the model choices and the mesh, supports producing the target turbulent wind at the incident location. The target comes from Chapter 3. The incident location coincides with the location of the most upwind building or structure in the computational domain of the building simulation. | none | 51 |
| AC 5-3 | MANDATORY | If the terrain exposure changes with wind direction, the quality of the turbulent flow at the incident location is demonstrated for each different exposure condition encountered over all directions. | none | 51 |
| §5.1.2 commentary (method families) | COMMENTARY | Inflow turbulence methods fall into three families: precursor simulation, recycling, synthetic generation. Keeping the profiles realistic along the domain is not easy. | none | 51 |
| §5.1.2 commentary (precursor/recycling) | COMMENTARY | Can be run in advance and the time- and position-dependent velocity field written to a database. If the ground roughness elements are shorter than the wall-adjacent cell, a rough-wall function written for wind can be used (it must give the effect of z0 correctly). If the elements extend beyond the first cell their effects must be resolved; their height and spacing must be defined so as to give the target profile. A recycling/periodic condition over an insufficient distance can lead to permanent locking of large structures; the periodic condition has to be shifted. | none | 51 |
| §5.1.2 commentary (synthetic, pressure) | COMMENTARY | Synthetic generators are efficient but can produce spurious pressure fluctuations; this spoils the estimation of fluctuating surface pressures. Removing them is regarded as essential for realistic surface pressure; there are methods in the literature that reduce them. | none | 51 |
| §5.1.2 commentary (synthetic, decay) | COMMENTARY / RECOMMENDED | Synthetic turbulence specified at the inlet develops downstream toward an equilibrium state. A ground wall treatment consistent with the log law preserves the mean profile; however, a decrease in turbulence intensity between the inlet and the location of interest is often seen, and this harms the estimation of pressure fluctuations on the building. The development should be monitored closely (should); if there is a marked change, the inlet statistics can be optimized so as to match the downstream target. | No numerical limit given (the binding limit is in AC 5-9) | 51 |
| §5.1.2 commentary (trial and error) | COMMENTARY | Finding the setup that gives a particular incident flow may require trial and error; it resembles searching for the arrangement of roughness elements, fence and spires in a wind tunnel. | none | 51–52 |
| PO 5-4 / AC 5-4 | MANDATORY | The ground boundary condition supports reproducing the target incident flow for the z0 determined from Chapter 3. | none | 52 |
| §5.1.3.1 commentary (two routes) | COMMENTARY | Roughness is represented either by resolving the effect of the elements or by a near-wall model that gives a friction velocity relation consistent with the target mean profile. | none | 52 |
| §5.1.3.1 commentary (explicit elements) | COMMENTARY / RECOMMENDED | If the elements are modeled explicitly, their distance from the buildings should be large enough that the local effect of individual elements does not reach the building. Representation options: body-fitted mesh, immersed boundary, body force. | none | 52 |
| §5.1.3.1 commentary (wall model) | COMMENTARY / RECOMMENDED | If the roughness height is smaller than or close to the first cell height in the building simulation, a near-wall model can be used. The model should give a friction velocity consistent with the neutral log law; the simplest equilibrium approach requires only z0. It has been reported that these models can fail, especially when the near-wall mesh is fine. | none | 52 |
| §5.1.3.1 commentary (sand grain) | COMMENTARY | The rough-wall function in many LES codes is based on sand-grain roughness and cannot be applied directly to wind over rough terrain; it should be verified that the function was written for wind and that the input is z0. | none | 52 |
| PO 5-5 / AC 5-5 | MANDATORY | Appropriate conditions are defined for the side, top and outlet boundaries that allow the target turbulent flow to be modeled correctly. | none | 52 |
| §5.1.3.2 commentary | COMMENTARY | Sides: a periodic condition is common (allows three-dimensional fluctuation, prevents an unwanted lateral gradient). Top: slip wall or far-field pressure. Alternative: sides and top as no-slip walls as in a wind tunnel; they should be far enough away not to interact with the wall boundary layers. Outlet: zero gradient or convective condition for velocity and turbulence; damping if necessary (instability, reflection). | none | 52–53 |
| §5.4 introduction | MANDATORY (framework) | The aim is a physically consistent approach flow and the target boundary layer at the incident location. The inlet conditions are defined so as to match the target at the incident location. Four headings: solver convergence, field inspection and comparison with the target, statistical convergence, mesh adequacy. | none | 55–56 |
| AC 4-6b (§5.4.1) | MANDATORY | The convergence criteria are applied throughout the run; the criteria and checks are reported. | none | 56 |
| §5.4.1 commentary | COMMENTARY / RECOMMENDED | With an iterative solver a drop in the residuals is expected at every time step; or the momentum and mass imbalances should be small and bounded. If the solver advances without reaching the criterion (at the maximum number of iterations), accuracy can be degraded. | 3–4 orders of magnitude residual drop | 56 |
| PO 5-7 | MANDATORY | The convergence of the mean and standard deviation estimates of the velocity profiles at the incident location is assessed. | none | 56 |
| AC 5-7 | MANDATORY | The initial transient T_init discarded before the analysis and the averaging time T_avg used for the statistics are reported. It is shown that the averaging time is sufficient to converge the mean velocity and turbulence intensities at building height. | No numerical duration given | 56 |
| §5.4.2 commentary | COMMENTARY / RECOMMENDED | The length of the initial transient depends on the domain size, the wind speed and the time scales resolved. A sufficiently long time series should be used. The simplest check: after the transient is discarded, compute the mean and standard deviation with a growing window and see whether they settle. | none | 56 |
| PO 5-8 | MANDATORY | It is shown that the setup represents the wind and pressure fields in a physically consistent way. | none | 56 |
| AC 5-8 | MANDATORY | For each different boundary layer condition: instantaneous velocity and pressure snapshots; contour plots of mean streamwise velocity, standard deviation of the three velocity fluctuations (or turbulence intensities), mean pressure and standard deviation of the pressure fluctuation. Planes: vertical plane at mid-width; horizontal plane at the height of the building studied. | 2 planes | 56 |
| PO 5-9 | MANDATORY | The flow at the incident location correctly represents the target flow determined from Chapter 3. | none | 56 |
| AC 5-9 (framework) | MANDATORY | The six items below are satisfied at the incident location, at distance x_i from the inlet, both at mid-width and at the 1/3-width positions measured from the centerline. | Lateral positions: center and 1/3 width | 56 |
| AC 5-9 (1a) | MANDATORY | For the shape of the mean velocity profile, the ratio of z0 to the characteristic dimension is equal in the model and at full scale (m: computational model, scaled if necessary; p: full-scale target). Because of the uncertainty in estimating the full-scale z0, it is sufficient that this holds within a factor of three. | (z0/L_b)_m = (z0/L_b)_p, within a factor of 3 | 57 |
| AC 5-9 (1b) | MANDATORY | The difference between the simulated and target mean velocity profiles is less than 10% over the upper 75% of h_max. If Topography Method 1 (§3.3.2) is applied, the range is extended to 100% of h_max. The measure is Equation 5-1. | < 10%; range: upper 75% of h_max (Method 1: 100%) | 57 |
| AC 5-9 (2) | MANDATORY | The same requirement for the turbulence intensity I_u profile; the measure is Equation 5-2. | < 10%; range: upper 75% of h_max (Method 1: 100%) | 57 |
| AC 5-9 (3) | MANDATORY | The integral length scale components needed to estimate the loading mechanisms correctly are within a factor of three of the target. | within a factor of 3 | 57 |
| AC 5-9 (4) | MANDATORY (plot) | The power spectral densities of the required velocity fluctuation components are plotted at the roof or top height of the building/structure being designed. No numerical acceptance limit given. | none | 57 |
| AC 5-9 (5) | MANDATORY (plot) | The profiles of the required Reynolds stress components are plotted; the relevant cross-spectral densities are plotted at roof/top height. No numerical acceptance limit given. | none | 57 |
| AC 5-9 (6) | MANDATORY | The profiles of the standard deviation of the pressure fluctuations are plotted and it is verified that they do not exceed 10% of the dynamic pressure computed with the reference velocity at roof/top height. | σ_p ≤ 0.10 · q_ref (q_ref: dynamic pressure with the roof/top reference velocity) | 57 |
| PO 5-10 | MANDATORY | The adequacy of the mesh resolution is demonstrated. | none | 57 |
| AC 5-10 | MANDATORY | The cutoff frequency is shown on the power spectrum of the streamwise velocity component and it is verified that it satisfies AC 5-2. | AC 5-2 limits | 57 |
| §5.4.4 commentary | COMMENTARY | The mesh determines the smallest turbulence scale that can be resolved; the mesh size upwind of the target building directly affects the cutoff frequency; what lies above it is left to the subgrid-scale (SGS) model. The cutoff frequency n_c can be found by iterative solution of Equation 5-3. | none | 57–58 |

## Equations (plain text)

| Equation | Status | Content | PDF page |
|---|---|---|---|
| (5-1) | Corrupted in the text extraction; partly readable | Parts read: eps_ABL-U = (1/h_max) · integral[ (U_target − U_simulated) / U_target ] dz ≤ 0.1; upper limit h_max. The absolute value sign and the lower integration limit could not be read in the text (the sentence of the clause gives the range as "the upper 75% of h_max"; 100% with Topography Method 1). | 57 |
| (5-2) | Corrupted in the text extraction; partly readable | eps_ABL-Iu = (1/h_max) · integral[ (I_u,target − I_u,simulated) / I_u,target ] dz ≤ 0.1; upper limit h_max. Absolute value and lower limit could not be read (same note). | 57 |
| (5-3) | Equation unreadable in the text | Symbols seen: Delta, pi, n_c, F(n_c). A relation between the cutoff frequency n_c and the effective mesh size Delta that contains F(n_c) and is solved by iteration; the fraction structure could not be recovered. To be checked against the original PDF. | 57 |
| (5-4) | Readable | F(n_c) = sum (i = 1..3) S_ii(n_c); S_ii: turbulence auto power spectrum of the i-th component. | 58 |
| (5-5) | Readable (root sign inferred from the typesetting) | Delta = (Delta_x · Delta_y · Delta_z)^(1/3); Delta_x, Delta_y, Delta_z cell dimensions; Delta the effective mesh size at the place of interest. | 58 |

## Definitions (§1.8, §1.9, §4.1)

| Term | Summary | PDF page |
|---|---|---|
| Incident location | The most upwind location in the computational domain where a building or topography is added. §4.1 (AC 4-1) gives the same definition with the wording "to be added in the second step". | 24; 43 |
| Approach flow region | The mesh region from the inlet boundary up to the study region, and including it. | 24 |
| Study region | The box enclosing the building studied, its explicitly modeled surroundings and nearby topography; does not include the approach flow region. | 25 |
| h_max | The larger of the building height and the average height of the surrounding buildings. | 26 |
| Longitudinal integral time scale | The integral length scale divided by the mean velocity at the same height. | 25 |

## Not found in the text

- §5.1 gives no numerical multiple for the domain size (length, width in terms of building height).
- §5.4.2 gives no numerical lower limit for T_init and T_avg (the requirement of 500 integral time scales in the building simulation is in AC 6-14).
- For AC 5-9 (4) and (5) no numerical tolerance is given for agreement of the spectra/Reynolds stresses.
- There is no numerical permitted drop for the decrease of turbulence from the inlet to the incident location.
