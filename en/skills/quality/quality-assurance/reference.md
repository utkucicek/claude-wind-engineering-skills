# Reference — Chapter 8: Quality assurance

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 8 and Table 8-1.
"PDF page" = PDF sequence number (printed page = PDF − 18).
Type: MANDATORY = "shall", RECOMMENDED = "should / recommended", COMMENTARY = "Commentary" or explanatory text.

Important: Chapter 8 introduces no PO/AC clause of its own; Table 8-1 is a heading-level summary of the clauses in Chapters 3–7.
In the Table 8-1 breakdown below, the rows of Chapters 3–5 and most of Chapter 6 are transcribed ONLY from the table heading;
where the "Numerical criterion" column says "not in table", the threshold is in the text of the relevant chapter and was not read within the scope of this skill.
The underlying clauses of these rows are acceptance criteria written as MANDATORY ("shall") in their own chapters; the type column is marked "Table".

## §8.1 Quality assurance workflow

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §8 introduction | COMMENTARY | The chapter summarizes the performance objectives and acceptance criteria of the preceding chapters; it also mentions a discussion on simulation uncertainty (a separate uncertainty subsection was not found in the text). | none | 81 |
| §8.1 (1st paragraph) | COMMENTARY | CWE is the solution of a multi-parameter system of equations whose parameters and quantities of interest interact nonlinearly; the choices of mesh design, discretization and solution method, turbulence model and boundary conditions complicate the load estimate. | none | 81 |
| §8.1 (2nd paragraph) | COMMENTARY (expectation: "expected") | Steady or unsteady RANS, whatever the turbulence closure, cannot give a reliable peak / fully transient solution for structural wind engineering. At a minimum, the use of transient, eddy-resolving approaches such as LES and wall-modeled LES is expected. Its binding counterpart is PO/AC 4-2. | none | 81 |
| §8.1 (3rd paragraph) | COMMENTARY | The PO and AC clauses were developed to raise the quality of CWE design; Table 8-1 summarizes them. | none | 81 |
| §8.1 commentary | COMMENTARY | In LES and DES the mesh resolution affects not only the numerical accuracy but also determines the cutoff frequency between the modeled and resolved scales; accuracy is determined by the complex interaction between mesh resolution/quality, numerical schemes and the subgrid model. | none | 81 |

## Table 8-1 — Chapter 3: Wind climate, target flow, terrain, topography (PDF p. 82)

| Clause | Type | Summary (from the table heading) | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 3-1 | Table | Assessment of the site-specific local wind climate. | not in table | 82 |
| AC 3-1a | Table | Multi-decadal wind records for synoptic wind analysis. | not in table | 82 |
| AC 3-1b | Table | Monte Carlo simulations for hurricane wind analysis. | not in table | 82 |
| AC 3-1c | Table | Cross-validation for reanalysis data sets. | not in table | 82 |
| PO 3-2 | Table | Target flow conditions of synoptic winds. | not in table | 82 |
| AC 3-2 | Table | Determination of the target flow parameters and reference heights. | not in table | 82 |
| PO 3-3 | Table | Characterization of the upwind terrain exposure. | not in table | 82 |
| AC 3-3 | Table | Surface roughness assessment. | not in table | 82 |
| PO 3-4 | Table | Simulation of flow affected by topographic features. | not in table | 82 |
| AC 3-4 | Table | Acceptable topographic flow simulations (Topography Methods 1 and 2). | not in table | 82 |

## Table 8-1 — Chapter 4: Simulation method (PDF pp. 82–83)

| Clause | Type | Summary (from the table heading) | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 4-1 | Table | Accurate representation of the target wind flow. | not in table | 82 |
| AC 4-1 | Table | Verification of the target inflow. | not in table | 82 |
| PO 4-2 | Table | Simulations that capture the temporal and spatial development of turbulence for peak pressure loads. | not in table | 82 |
| AC 4-2 | Table | LES approaches applied with a body-fitted mesh, including wall-modeled LES. | not in table | 82 |
| PO 4-3 | Table | Minimization of numerical errors on the mesh and of the damping of resolved turbulence (spatial discretization, gradient interpolation). | not in table | 82 |
| AC 4-3 | Table | At least second-order schemes. | ≥ 2nd order | 82 |
| PO 4-4 | Table | Minimization of numerical errors in time integration. | not in table | 82 |
| AC 4-4 | Table | At least a second-order scheme, and a time step suitable for numerical stability and eddy development. | ≥ 2nd order | 82 |
| PO 4-5 | Table | Physically consistent representation of the effect of subfilter-scale turbulence on the resolved flow. | not in table | 82 |
| AC 4-5 | Table | Use of suitable SGS models. | not in table | 82 |
| PO 4-6 | Table | Stable and accurate solution methods for the discretized equations (solver convergence within the time step). | not in table | 83 |
| AC 4-6a | Table | Convergence check. | not in table | 83 |
| AC 4-6b | Table | Report of the convergence criteria used in the approach flow simulations. | not in table | 83 |
| AC 4-6c | Table | Report of the convergence criteria in the building aerodynamics simulations. | not in table | 83 |
| PO 4-7 | Table | Full-scale or model-scale simulations (geometric scaling). | not in table | 83 |
| AC 4-7 | Table | Requirements for model-scale simulations. | not in table | 83 |

## Table 8-1 — Chapter 5: Approach flow simulations (PDF pp. 83–84)

| Clause | Type | Summary (from the table heading) | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 5-1 | Table | Computational domain size that captures the target wind field and avoids boundary condition effects. | not in table | 83 |
| AC 5-1 | Table | Domain size requirements. | not in table | 83 |
| PO 5-2 | Table | Mesh resolution that captures small-scale turbulence for wind loads. | not in table | 83 |
| AC 5-2 | Table | Requirements on the maximum resolved reduced frequency for cladding and overall loads. | not in table | 83 |
| PO 5-3 | Table | Reproduction of the target turbulent wind conditions at the incident location. | not in table | 83 |
| AC 5-3 | Table | Demonstration of the quality of the turbulent flow at the incident location for all different exposure conditions and all wind directions (for the acceptance levels the table says "A.C. 5-8"; the acceptance requirement row is 5-9 — to be verified against the PDF). | not in table | 83 |
| PO 5-4 | Table | Boundary conditions for the domain ground surface. | not in table | 83 |
| AC 5-4 | Table | Modeling of the target ground roughness (reference "A.O. 3-3" in the table). | not in table | 83 |
| PO 5-5 | Table | Side, top and outlet boundary conditions of the domain. | not in table | 83 |
| AC 5-5 | Table | Selection of suitable boundary conditions. | not in table | 83 |
| PO 5-6 | Table | Reproduction of the effect of topography on the approach flow in the empty domain. | not in table | 83 |
| AC 5-6 | Table | Demonstration that the approach flow affected by topography is reproduced correctly. | not in table | 83 |
| PO 5-7 | Table | Convergence of the velocity statistics. | not in table | 84 |
| AC 5-7 | Table | Convergence report of the mean velocity and turbulence intensities at building height. | not in table | 84 |
| PO 5-8 | Table | Physically consistent representation of the wind and pressure field for the approach flow. | not in table | 84 |
| AC 5-8 | Table | Visualization of the velocity and pressure fields. | not in table | 84 |
| PO 5-9 | Table | Accurate presentation of the target flow parameters at the incident location. | not in table | 84 |
| AC 5-9 | Table | Acceptance requirements for the flow properties at the incident location ("incipient" in the table), both at midspan and at the 1/3 span positions (3-2 and 3-3 for the target values). | location: mid and 1/3 span; thresholds not in table | 84 |
| PO 5-10 | Table | Suitable mesh resolution. | not in table | 84 |
| AC 5-10 | Table | The wind spectrum cutoff frequency lies in the inertial subrange. | not in table | 84 |

## Table 8-1 — Chapter 6: Building aerodynamics simulations (PDF pp. 84–86)

| Clause | Type | Summary (from the table heading; 6-13…6-16 from the text) | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 6-1 | Table | Consistent reproduction of the wind and pressure fields generated in the approach flow simulations. | not in table | 84 |
| AC 6-1 | Table | Consistency with the approach flow simulations in geometric/velocity scales, solvers, numerical methods, turbulence models and boundary conditions. | not in table | 84 |
| PO 6-2 | Table | Modeling of the details that affect the aerodynamics of the study building. | not in table | 84 |
| AC 6-2a | Table | Inclusion of the geometric details of the building. | not in table | 84 |
| AC 6-2b | Table | Inclusion of internal volume and opening models. | not in table | 84 |
| PO 6-3 | Table | Modeling of nearby buildings and other structures that affect the aerodynamics. | not in table | 84 |
| AC 6-3 | Table | Justification report for the selected proximity models. | not in table | 84 |
| PO 6-4 | Table | Topography model. | not in table | 84 |
| AC 6-4a | Table | Inclusion of topography models around the building. | not in table | 84 |
| AC 6-4b | Table | Justification report for the topography model. | not in table | 84 |
| PO 6-5 | Table | Building appurtenances. | not in table | 85 |
| AC 6-5a | Table | Modeling requirement for full-scale, high-resolution simulations. | not in table | 85 |
| AC 6-5b | Table | Alternative to 6-5a. | not in table | 85 |
| AC 6-5c | Table | Modeling requirement for model-scale simulations. | not in table | 85 |
| AC 6-5d | Table | Justification report on the geometric scale and the inclusion of details. | not in table | 85 |
| PO 6-6 | Table | Porous components. | not in table | 85 |
| AC 6-6 | Table | Porosity modeling report for explicit models; validation for coarsened models. | not in table | 85 |
| PO 6-7 | Table | Domain size, in comparison with that in the wind simulations. | not in table | 85 |
| AC 6-7 | Table | Location of the most upwind building/topographic feature; domain lengths in the streamwise, spanwise and vertical directions. | not in table | 85 |
| PO 6-8 | Table | Domain size for acceptable boundary or blockage effects. | not in table | 85 |
| AC 6-8a | Table | Streamwise distances of the inlet and outlet boundaries from the nearest buildings and topographic features. | not in table | 85 |
| AC 6-8b | Table | Maximum acceptable blockage ratios. | not in table | 85 |
| PO 6-9 | Table | Mesh resolution requirements. | not in table | 85 |
| AC 6-9a | Table | Mesh resolution in the approach flow region. | not in table | 85 |
| AC 6-9b | Table | Mesh resolution in the near-wall region. | not in table | 85 |
| AC 6-9c | Table | Mesh resolution in the local flow region. | not in table | 85 |
| AC 6-9d | Table | Mesh resolution in the far flow region. | not in table | 85 |
| AC 6-9e | Table | Assessment of mesh adequacy with velocity/pressure spectra and the IRQ. | not in table | 85 |
| AC 6-9f | Table | Mesh resolution near modeled porous elements. | not in table | 85 |
| PO 6-10 | Table | Building surfaces (boundary condition). | not in table | 86 |
| AC 6-10a | Table | Near-wall flow treatments. | not in table | 86 |
| AC 6-10b | Table | Examination of the wall modeling for flow near rounded building surfaces. | not in table | 86 |
| AC 6-10c | Table | Quantification of the effect of the near-wall treatment on the pressure distribution. | not in table | 86 |
| PO 6-11 | Table | Other boundaries. | not in table | 86 |
| AC 6-11 | Table | Use of the inlet, ground, side, top boundaries in 5-4 and 5-5; terrain roughness modeling in topographic flow simulations. | not in table | 86 |
| PO 6-12 | Table | Velocity and pressure fields. | not in table | 86 |
| AC 6-12a | Table | Visualization of the velocity and pressure properties at representative locations. | not in table | 86 |
| AC 6-12b | Table | Visualization of the velocity and pressure behavior at the monitoring points. | not in table | 86 |
| PO 6-13 | MANDATORY | The overall quality of the simulation is checked by examining the pressure field on the building envelope. | none | 66; table 86 |
| AC 6-13a | MANDATORY | Contour maps of the mean and standard deviation of the pressure are plotted on all facades, on the roof and, where relevant, on the appurtenances; special attention to high-gradient regions (edges, corners). | none | 66 |
| AC 6-13b | MANDATORY | Probe locations are placed according to the ASCE/SEI 49-21 guidance (table: locations for maximum/minimum pressure estimation). | none | 66 |
| AC 6-13c | MANDATORY | The resolution of the pressure monitoring locations is sufficient to capture the spatial variation on the surface for the MWFRS and C&C studies. | none | 66 |
| AC 6-13d | MANDATORY | The report justifies the choice of data sampling resolution. | none (no threshold given) | 66 |
| AC 6-13e | MANDATORY | The reference static pressure monitoring point is placed away from the influence of the model, the proximity model and the boundaries; a static pressure point directly above the study region is used for reference. | none | 66 |
| PO 6-14 | MANDATORY | It is established that the mean and standard deviation of the velocity at key points, and the estimates of the mean, standard deviation and peak value of the load quantities of interest, have converged. | none | 66 |
| AC 6-14 | MANDATORY | The simulation duration is longer than a specified multiple of the longitudinal integral time scale at the target building height. | > 500 longitudinal integral time scales | 66 |
| §6.6.3 commentary | COMMENTARY | The required duration is the spin-up + averaging duration. The mean and standard deviation of the signal can be monitored over a growing window (after the initial transient part is discarded); for peak values, block maxima or peak-over-threshold can be used. | none | 66 |
| PO 6-15 | MANDATORY ("must") | A mesh study is performed for the project in at least two wind directions. | ≥ 2 directions | 67 |
| AC 6-15a | MANDATORY | The IRQ is not below the lower limit at the key monitoring locations in the flow and pressure field; the differences in load quantities between the two mesh resolutions are reported. | IRQ ≥ 75% | 67 |
| AC 6-15b | MANDATORY | The key monitoring location is an array of virtual probe points along the building height and out to a specified distance from the building; adaptation is made for special cases; the approach flow (upwind wakes) and the building wake are captured. | up to 160 ft (~50 m) from the building | 67 |
| §6.6.4 commentary | COMMENTARY | In implicitly filtered LES/DES each mesh gives a different scale resolution; the solution is mesh independent only as it approaches DNS level. IRQ = resolved turbulent kinetic energy / total; the total is estimated by extrapolating the SGS contribution from the results of two meshes. At most three meshes (coarse, medium, fine); refinement factor ideally 2. The effective order p should approximately agree with the numerical order of the scheme; if the estimated order is markedly higher than the theoretical one, adopting the theoretical order should be avoided. | r ideal = 2; lower limit of r: could not be read in the text; Eqs. 6-3…6-6: equations could not be read in the text | 67–68 |
| §6.6.4 commentary — IRQ ranges | COMMENTARY | IRQ classes: below the lower limit = further refinement needed; middle range = suitable for an engineering solution; upper range = close to DNS. | < 75%; 75–85%; > 85% | 68 |
| PO 6-16 | MANDATORY | The time-step sensitivity is reviewed. | none | 68 |
| AC 6-16 | MANDATORY | Velocity spectra are plotted at key locations around the building and in the regions between the target building and the upwind buildings; the cutoff arising from the mesh size and the time step is shown on the plot. | none | 68 |
| §6.6.5 commentary | COMMENTARY | In explicit schemes the maximum time step depends on the local cell size and velocity (CFL); in implicit schemes the CFL may exceed 1 but the required time scales must be resolved. A good test: a second run with half the time step; if the spectra are identical/very similar, the step is adequate. Alternative: keeping the CFL constant in the mesh sensitivity study. | step × ½; CFL > 1 possible (implicit) | 68 |

## Table 8-1 — Chapter 7: Design wind loads (PDF pp. 87–88)

Details and type distinction: `skills/loads/design-wind-loads/reference.md`. The table headings are given here.

| Clause | Type | Summary (from the table heading) | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 7-1 / AC 7-1 | MANDATORY | Number of directions and/or wind conditions / maximum azimuth increment. | ≤ 10° | 87 |
| PO 7-2 / AC 7-2 | MANDATORY | Monitoring of the reference wind speed / monitoring location. | none | 87 |
| PO 7-3 / AC 7-3a | MANDATORY | Load limitations / minimum load requirement for the unsheltered case. | none | 87 |
| AC 7-3b | MANDATORY | Assessment of the consistency of load reduction based on statistically steady aerodynamics. | none | 87 |
| PO 7-4 / AC 7-4a | MANDATORY | Combination of the local climate with the simulation estimates / accepted statistical methods. | 6 methods | 87 |
| AC 7-4b | MANDATORY | Documentation of the analysis and method details. | none | 87 |
| PO 7-5 / AC 7-5a | MANDATORY | Wind forces / requirement for integration of surface forces. | none | 87 |
| AC 7-5b | MANDATORY | Acceptable integration method using time-varying local pressure data. | none | 87 |
| AC 7-5c | MANDATORY | Force calculation requirement for buildings with porous elements. | none | 87 |
| PO 7-6 / AC 7-6 | MANDATORY | Dynamic response to wind / DAF report. | none | 87 |
| PO 7-7 / AC 7-7 | MANDATORY | Peak loads and structural effects / acceptable methods. | none | 87 |
| PO 7-8 / AC 7-8 | MANDATORY | Local peak pressures / monitoring locations. | none | 88 |
| PO 7-9 / AC 7-9 | MANDATORY | Mean and time-varying pressures / direct integration requirements. | none | 88 |
| PO 7-10 / AC 7-10a | MANDATORY | Peak design loads / exceedance probability report. | none | 88 |
| AC 7-10b | MANDATORY | Requirement that no temporal filtering is performed. | none | 88 |
| PO 7-11 / AC 7-11 | MANDATORY | Net pressure / coefficient from directly derived net pressures. | none | 88 |
| PO 7-12 / AC 7-12a | MANDATORY | Internal pressure / requirements for the analytical method using simulated external pressures. | none | 88 |
| AC 7-12b | MANDATORY | Requirements for direct determination of internal pressure. | none | 88 |
| AC 7-12c | MANDATORY | Requirements for internal pressure estimation in partially enclosed volumes. | none | 88 |
| PO 7-13 / AC 7-13 | MANDATORY | External pressure / use of pressure coefficients. | none | 88 |
| PO 7-14 / AC 7-14a | MANDATORY | Loads on appurtenances / acceptable methods. | none | 88 |
| AC 7-14b | MANDATORY | Approach requirements for rigid and flexible appurtenances. | none | 88 |
| PO 7-15 / AC 7-15 | MANDATORY | Presentation of results / reporting requirements. | 3 items | 88 |
| PO 7-16 / AC 7-16 | MANDATORY | Presentation of the integrated forces and moments / visualization of their statistical properties. | none | 88 |

## Verification, validation and benchmarking (other clauses on which Chapter 8 relies)

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §1.6 (1) | COMMENTARY | The maturity and reliability of LES codes span a wide range; in general the most reliable and best documented are commercial codes, while open-source/academic/individual codes may be less reliable. | none | 23 |
| §1.6 (2) | RECOMMENDED | The analyst should be thoroughly familiar with the verification and validation test documentation of the code used. | none | 23 |
| §1.6 (3) | MANDATORY | The analyst assesses the range of conditions and the rigor of the code verification and model validation tests documented by the code provider. | none | 23 |
| §1.6 (4) | MANDATORY | If the client requests it, this information is provided together with the analyst's assessment of adequacy. | none | 23 |
| §1.6 (5) | RECOMMENDED | If the analyst or the client finds the scope/rigor insufficient for the application, additional testing should be done and documented. This verification/validation process is outside the scope of the document. | none | 23 |
| §1.6 commentary | COMMENTARY | Definitions (ASME): code verification = establishing that the mathematical model is implemented correctly in the code; solution verification = establishing the accuracy of a specific numerical solution; validation = establishing the degree to which the model results represent empirical data in the context of use. Code verification should be done by the developer, solution verification (discretization, iteration, precision errors) by the CWE user. In CWE, validation has mostly relied on wind tunnel data under controlled conditions; defining a representative experimental data set is out of scope. | none | 23 |
| §1.8 definitions | COMMENTARY | The definitions of code verification, solution verification and validation also appear in the list of terms. | none | 24–26 |
| §9.5.4 | MANDATORY | The report assesses the simulation quality in terms of mesh refinement, time-step sensitivity, inner-iteration solver convergence, statistical convergence and spectral properties; assesses the uncertainty arising from the input parameters (wind data, terrain roughness model); gives the details if a probabilistic method (Monte Carlo, confidence interval) was used; documents other known error sources. | none | 93–94 |
| §9.5.4 commentary | COMMENTARY / RECOMMENDED | Because no reliable benchmark cases for CWE were available at the date of publication, the document does not mandate validation of the results against reference data; reporting of additional validation against representative empirical or high-fidelity simulation data is recommended. | none | 94 |
| §9.5.5 | MANDATORY | The report contains a compliance summary table aligned with Table 8-1. | none | 94 |
| §9.5.6 | MANDATORY | Information on the method (equations, turbulence models, discretization) is given; conditions that deviate from the Prestandard are justified; the registered design professional keeps a digital record of the model and data; code verification and/or benchmark comparison documentation is added if available. | none | 94 |
| §10.7 commentary | COMMENTARY | Peer review does not replace the normal quality assurance measures of the team performing the simulation. | none | 98 |

## Unreadable / missing items

- Eqs. 6-3 … 6-6 (IRQ, total kinetic energy, effective order, a_k): equations could not be read in the text.
- Lower limit for the mesh refinement factor r: the value is corrupted in the text extraction (it came out in the form "at least 2", looks the same as the ideal value; the square-root sign may have been dropped) — to be verified against the PDF.
- A separate uncertainty subsection in Chapter 8 and any appendix: not found in the text.
- The threshold values of Chapters 3–5 and of Chapter 6 (other than 6-13…6-16) in Table 8-1: not in the table; the text of the relevant chapter was not read within the scope of this skill.

## Count

Table 8-1: 53 PO (Chapter 3: 4, Chapter 4: 7, Chapter 5: 10, Chapter 6: 16, Chapter 7: 16) and 84 AC
(Chapter 3: 6, Chapter 4: 9, Chapter 5: 10, Chapter 6: 35, Chapter 7: 24). Chapter 8 has no PO/AC clause of its own.
