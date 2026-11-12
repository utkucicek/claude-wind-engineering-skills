# Reference: ASCE CWE Prestandard introduction to §6, §6.1, §6.5, §6.6

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Page numbers are PDF page order. The summaries are written in our own sentences.

Type: MANDATORY = shall (or must), RECOMMENDED = should, COMMENTARY = commentary.

## Clauses

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §6 introduction | MANDATORY | Building aerodynamics simulations satisfy all the PO/AC clauses of §4.2 (method, discretization, unresolved turbulence, solver convergence, scaling); this chapter adds requirements to them. | none | 59 |
| §6 introduction commentary | COMMENTARY | The content is also applicable to LES for pedestrian comfort/safety and air quality. | none | 59 |
| PO 6-1 | MANDATORY | The building simulation agrees, in the same physical region, with the result of the Chapter 5 approach flow simulation. | none | 59 |
| AC 6-1 | MANDATORY | The building simulation uses the same geometric and velocity scale, solver, numerical methods, turbulence model, ground wall model and boundary conditions as the §5.1 approach flow simulations (the two-step process of PO 4-1). | none | 59 |
| §6.1 commentary | COMMENTARY | Keeping the basic model choices ensures that the target flow is also produced correctly in the building simulation. | none | 59 |
| PO 6-10 | MANDATORY | The boundary condition on the building surface is chosen according to the surface properties and the near-wall mesh resolution. | none | 64 |
| AC 6-10a | MANDATORY | The building surface is modeled as a no-slip wall; the near-wall treatment is consistent with the mesh resolution. If the near-wall flow is sufficiently resolved the no-slip condition is applied directly; if it is less resolved a wall model is used. For special boundaries such as a porous surface, dedicated verification and validation is carried out. | y+ = y·u*/ν < 5 (dimensionless) | 64 |
| AC 6-10b | MANDATORY | If the building has a rounded shape (the separation location is not fixed by a sharp edge), the effect of using a wall model without the near-wall flow being sufficiently resolved is examined. | none | 64 |
| AC 6-10c | MANDATORY | Additional simulations are made with the near-wall mesh resolution or the wall model changed, and the effect of the wall treatment on the pressure distribution is quantified. | Number of runs not given | 64 |
| PO 6-11 | MANDATORY | Realistic boundary conditions at the inlet, outlet, ground, sides and top are set so as to give a correct representation of the flow within the domain. | none | 64 |
| AC 6-11 | MANDATORY | These boundaries comply with the provisions of §5.1.2 and §5.1.3. If the geometric model of the topography is in the domain, the terrain roughness belonging to the topographic feature is also represented by an appropriate roughness model. | none | 64 |
| §6.5.2 commentary | COMMENTARY | Terrain roughness affects the flow over topography; the choice of model is critical. In forested regions, canopy models that take the canopy height and the vertical variation of leaf density into account are more reliable than wall functions based on z0 alone. | none | 64–65 |
| §6.6 introduction | Framework | Four headings: time-step solver convergence; inspection of the velocity and pressure fields and comparison of the flow at the incident location with the target; convergence of the pressure statistics; mesh dependency analysis. | none | 65 |
| §6.6.1 | MANDATORY | The simulation is managed so that the solution of every time step converges enough to minimize the accumulation of residuals and to preserve physical accuracy. | none | 65 |
| AC 4-6c (§6.6.1) | MANDATORY | The convergence criteria are met throughout the run; the criteria and checks are reported. | No number here (§5.4.1 commentary: 3–4 orders of magnitude residual drop) | 65 |
| PO 6-12 | MANDATORY | The overall quality of the simulation is checked by analyzing the flow field upwind of and around the building(s). | none | 65 |
| AC 6-12a | MANDATORY | For every wind direction simulated, contours of the mean, standard deviation (or turbulence intensity) and instantaneous snapshot of wind speed and pressure are presented with cell-center values without interpolation: (1) four horizontal planes, over an area covering at least the first row of surrounding buildings; (2) vertical plane(s) through the middle of the building(s), with the same extent. The plots capture the separation regions on the roof and sides and the wake. | Horizontal planes: h/2, 2h/3, h, h + 5 m (16 ft) | 65 |
| AC 6-12b | MANDATORY | Key monitoring point probes are defined along the building height and out to a certain distance from the building; their positions are chosen according to the building geometries in the domain; they capture the upwind flow (especially the wakes of upwind buildings) and the building wake. To be presented for each point: (1) a representative portion of the velocity and pressure time signal; (2) the mean, standard deviation and turbulence intensity of the velocity; (3) the velocity spectrum. | Out to ~50 m (160 ft) from the building | 65 |
| PO 6-13 | MANDATORY | The overall quality of the simulation is checked by analyzing the pressure field. | none | 66 |
| AC 6-13a | MANDATORY | Mean and standard deviation contours of pressure are plotted on all faces of the building facade, on the roof and, where relevant, on the appurtenances; special attention is given to the regions of high pressure gradient near edges and corners. | none | 66 |
| AC 6-13b | MANDATORY | Pressure taps are placed on the building according to the guidance of ASCE/SEI 49-21. | none | 66 |
| AC 6-13c | MANDATORY | The resolution of the pressure monitoring points is sufficient to capture the spatial variation over the surface for MWFRS and C&C studies. | No number given | 66 |
| AC 6-13d | MANDATORY | The report justifies the choice of data sampling resolution. | none | 66 |
| §6.6.2.2 commentary | COMMENTARY / RECOMMENDED | Additional pressure taps should be placed at wall edges and in the regions of corner separation and conical vortices; in roof studies they should be concentrated near the eaves and the ridge. A simple contour study helps to determine the number and position of the taps. | none | 66 |
| AC 6-13e | MANDATORY | The reference static pressure monitoring point is positioned so that it is not affected by the test model, the proximity model or the boundaries. A static pressure point placed directly above the study region is used for the reference. | Height not given | 66 |
| PO 6-14 | MANDATORY | It is established that the statistical estimates of these quantities have converged: (1) the mean and standard deviation of the wind speed at the §6.6.2.1 monitoring points; (2) the mean, standard deviation and peak values of the load quantities of interest. | none | 66 |
| AC 6-14 | MANDATORY | The simulation duration is larger than a certain multiple of the streamwise integral time scale at the height of the target building. | T > 500 · T_u (T_u: streamwise integral time scale = integral length scale / mean velocity at the same height, §1.8) | 66 |
| §6.6.3 commentary | COMMENTARY | The duration required consists of the initial (spin-up) time and the averaging time and depends on the problem. For velocity, adequacy is checked as in Chapter 5 (the commentary says "§5.4.3"; the method is described in §5.4.2). Overall load and moment statistics are used; for C&C, the pressure signals at facade points where large suction or pressure is expected. The mean and standard deviation are monitored with a growing window; for peak values the block maxima or peaks-over-threshold methods can be used. | none | 66 |
| PO 6-15 | MANDATORY (must) | To be sure that the mesh is fine enough for the case studied, a mesh study is done in at least two wind directions for the project. | ≥ 2 wind directions | 67 |
| AC 6-15a | MANDATORY | In the simulations analyzed the IRQ is not lower than a certain value at the key monitoring locations in the flow field and in the pressure field. The differences in the predicted load quantities between two mesh resolutions are reported. | IRQ ≥ 75% | 67 |
| AC 6-15b | MANDATORY | The key monitoring location consists of a series of virtual probe points along the building height and out to a certain distance from the building; room is left for special cases. The probes capture the approach flow (especially upwind wakes) and the building wake. | Out to ~50 m (160 ft) from the building | 67 |
| §6.6.4 commentary (general) | COMMENTARY | In implicitly filtered LES/DES the mesh size determines the filter size, so each mesh resolves different scales; the solution becomes mesh-independent only as it approaches DNS fineness. Modeling and discretization errors should be assessed together. The practical route is the IRQ; it is also useful to compare the key quantities obtained with different meshes. | none | 67 |
| §6.6.4 commentary (number of meshes and r) | COMMENTARY (contains a shall) | For the IRQ the project is simulated with at most three meshes (coarse, medium, fine); the meshes are refined successively by the factor r. The ideal refinement factor is 2 but it is expensive; for the smallest r the text extraction reads "at least 2", and since this is the same as the ideal value it appears that a symbol (most probably the root sign) has been dropped. | r ideal = 2; smallest r: could not be read reliably in the text | 67 |
| §6.6.4 commentary (choice of p) | COMMENTARY / RECOMMENDED | p is the order of the numerical method; second order in most commercial solvers. The effective order can be estimated with Equation 6-5 and should agree approximately with the order of the scheme. There is no guarantee that the successive solutions are in the asymptotic range; p should be chosen carefully so as not to underestimate the subgrid-scale contribution; if the estimated order is markedly higher than the theoretical one, the theoretical order should not be adopted. | p ≈ 2 (second-order schemes) | 67–68 |
| §6.6.4 commentary (IRQ classes) | COMMENTARY | Interpretation of the IRQ ranges: if low, more refinement is needed; the middle range is suitable for engineering solutions; if high, close to DNS. | < 75%: refinement needed; 75%–85%: optimized for engineering; > 85%: close to DNS | 68 |
| PO 6-16 | MANDATORY | Time-step sensitivity is examined. | none | 68 |
| AC 6-16 | MANDATORY | Wind speed spectra are plotted at key locations around the study building and in the regions between the target building and the upwind buildings; the cutoff arising from the mesh size and from the time step is marked on the plots. | none | 68 |
| §6.6.5 commentary | COMMENTARY | Sensitivity depends on the type of solver. Explicit schemes impose a maximum time step that depends on the local cell size and velocity (CFL number). With implicit schemes the CFL can be raised above 1, but the required time scales must be resolved; with an excessively large step the solver can diverge. A good method: halve the time step and compare the spectra; if they are the same or very similar the step is adequate. Alternative: keep the CFL number in the mesh sensitivity study. | CFL: can be > 1 with an implicit scheme; no numerical upper limit given; Δt/2 for the test | 68 |

## Equations (plain text)

| Equation | Status | Content | PDF page |
|---|---|---|---|
| y+ (within AC 6-10a, unnumbered) | Typesetting corrupted; structure readable | y+ = y · u* / ν < 5 (y: wall-normal distance, u*: friction velocity, ν: kinematic viscosity) | 64 |
| (6-3) | Readable | IRQ = k_resolved / k_total | 67 |
| (6-4) | Readable (position of the exponent inferred from the typesetting) | k_total = k_resolved + a_k · Δ^p; the second term is the estimate of the subgrid-scale contribution; Δ the filter width (with an implicit filter, the effective mesh size) | 67 |
| (6-5) | Corrupted in the text extraction; structure partly readable | p = ln[ (k_resolved,coarse − k_resolved,medium) / (k_resolved,medium − k_resolved,fine) ] / ln(r). This order of numerator and denominator has been inferred from the corrupted text; to be checked against the original PDF. | 67 |
| (6-6) | Corrupted in the text extraction; structure partly readable | Parts seen: a_k, (1 / Δ_fine^p), (k_resolved,fine − k_resolved,medium), (r^p − 1). Possible form: a_k = (1/Δ_fine^p) · (k_resolved,fine − k_resolved,medium) / (r^p − 1). The exact form could not be read in the text; to be checked against the original PDF. | 68 |

For the effective mesh size Δ see Equation 5-5: Δ = (Δ_x · Δ_y · Δ_z)^(1/3) (p. 58).

## Not found in the text (within §6.1, §6.5, §6.6)

- How many wind directions are to be simulated in total (only "at least two directions" is given, for the mesh study).
- The definition of the reference velocity for the building simulation and where it is to be read (the reference static pressure is in AC 6-13e; the reference velocity is not in these sections; AC 5-9 (6) speaks of the reference velocity at roof/top height).
- A number for the height or distance of the reference static pressure point.
- A numerical limit for the time step or CFL.
- A numerical duration for the initial transient (spin-up); whether the 500-times requirement means only the averaging time or the total duration is not clearly distinguished, the text says "simulation duration".
- A number for the count or spacing of pressure taps (reference is made to ASCE/SEI 49-21).
- An acceptable percentage for the load difference between two meshes.
