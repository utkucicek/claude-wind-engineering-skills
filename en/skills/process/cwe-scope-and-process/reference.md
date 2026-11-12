# Reference: CWE prestandard Chapters 1, 2 and 4 — clause table

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". The summaries are written in our own sentences. "PDF page" is the PDF page order (printed page = PDF − 18).

Type: **MANDATORY** = "shall" in the text; **RECOMMENDED** = "should" / "recommended"; **COMMENTARY** = "Commentary" paragraph; **INFORMATIVE** = definition or explanatory main text (no mandatory mood).

Chapters 1 and 2 contain no numbered PO/AC. Chapter 4 contains 7 POs and 7 ACs (PO 4-1 … 4-7; AC 4-1, 4-2, 4-3, 4-4, 4-5, 4-6a, 4-7).

## Chapter 1 — General

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §1.1 | INFORMATIVE | Purpose of the document: to provide, through POs and ACs, the standardization needed for broad acceptance of determining building wind loads by the computational method; the focus is reliable quantification of the load. | — | 19 |
| §1.1 | INFORMATIVE | Load estimation requires turbulence-resolving large-eddy simulation (LES); the acceptance criteria were developed for LES with a body-fitted mesh; the wall-modeled approach can be hybrid RANS/LES or LES in the whole domain. | — | 19 |
| §1.1 commentary | COMMENTARY | For pedestrian wind conditions and air quality there are established approaches that do not resolve turbulence, and in most cases a steady solution is sufficient; if turbulence-resolved results are wanted, the approaches in this document are useful. Wind-driven rain, snow and hail are not addressed. | — | 19 |
| §1.2 | MANDATORY | The person using the computational wind tool shall know the theory of wind engineering applications and the fundamental importance of turbulence in load estimation. | — | 20 |
| §1.2 | RECOMMENDED | If this background is missing, it is recommended to obtain expert opinion from the wind engineering community before the document is used. | — | 20 |
| §1.2 | INFORMATIVE | Clause notation: "[Performance Objective x-x]" and "[Acceptance Criterion x-x]"; the first number is the chapter, the second the sequence number. Prescriptive requirements are also referred to as POs. A PO is good-practice guidance and allows flexibility of method as long as the outcome is achieved; an AC is a pass/fail criterion. Where several ACs belong to one PO a letter is added; not every PO has an AC. | — | 20 |
| §1.3 | INFORMATIVE | The document focuses on turbulence-resolving simulations (e.g. LES) applied with the finite volume method and a body-fitted mesh. Immersed boundary and lattice Boltzmann methods are not addressed in the document because they have been less studied and validated. | — | 20 |
| §1.4 | INFORMATIVE | The document gives the minimum requirements for conducting, interpreting and documenting CWE simulations for wind load estimation on buildings and other structures; the structure follows the Davenport loading chain; quality assurance, reporting and peer review requirements are also defined. | — | 20 |
| §1.4 | MANDATORY | The document shall not be used without competent wind engineering opinion and guidance on its suitability for a particular application. | — | 21 |
| §1.4 commentary | COMMENTARY | The loading chain has five links: wind climate, terrain effect, aerodynamic effect, dynamic effect, criteria. A CWE assessment must address every link. Uncertainty is measured by the coefficient of variation (CoV); the total CoV is found approximately as the square root of the sum of squares of the CoVs of the first four links, and the wind speed CoV is weighted by a factor of four. | Wind speed CoV weight: 4 | 21 |
| §1.5.1 | INFORMATIVE | The document covers the simulation conditions of both synoptic (boundary layer profile) and non-synoptic winds; full-scale measurements for non-synoptic winds are limited. | — | 21 |
| §1.5.1 commentary | COMMENTARY | Approaches for tornado and thunderstorm profiles appear in the commentaries of Chapters 4–6; from Chapter 7 onward there is no approach, because consensus on the step from event simulation to characteristic load is limited. | — | 21–22 |
| §1.5.2 | INFORMATIVE | The document contains no method for determining the future conditions caused by climate change. | — | 22 |
| §1.5.3 | INFORMATIVE | The document is for buildings and appurtenances; the approaches are also valid for products and other structures (transmission tower, silo, large solar panel array); the POs and ACs of Chapters 3–6 continue to apply. | — | 22 |
| §1.5.4 | INFORMATIVE | No PO is defined for the moving-mesh simulation required for true wind-structure interaction and aeroelastic instability. The document is for a rigid building model; limited aeroelastic behavior such as resonance is obtained by post-processing the aerodynamic data. | — | 22 |
| §1.5.4 commentary | COMMENTARY | Interaction is possible in slender and flexible buildings; this is generally tested in the wind tunnel with an aeroelastic model, at all the speeds the structure may experience in its lifetime. | — | 22 |
| §1.5.5 | MANDATORY | The assessment of the simulation against the PO/ACs is made with the tools addressed in Chapter 4; load/response estimation by artificial intelligence is outside the focus of the document. | — | 22 |
| §1.5.5 commentary | COMMENTARY | Artificial intelligence is seen mainly as a tool that complements simulation rather than replacing it: interpolation between wind directions, surrogate model for parametric studies, optimization of post-processing. | — | 22 |
| §1.5.6 | INFORMATIVE | DAD/DED is of limited applicability to buildings of unique architecture in a dense urban fabric, and may be useful for standard designs; it is outside the focus of the document. | — | 23 |
| §1.5.6 commentary | COMMENTARY | DAD estimates the loads of regularly shaped buildings from full-scale monitoring or model-scale wind tunnel data; DED uses real-time data and mostly surrogate modeling. | — | 23 |
| §1.6 | RECOMMENDED | Whichever LES code is used, the analyst should be familiar with the detailed documentation of the code's verification and validation tests. Commercial codes are generally the most reliable and best documented; open-source, academic and personal codes may be less reliable (the document's own assessment). | — | 23 |
| §1.6 | MANDATORY | The analyst assesses the range of conditions and the rigor of the code verification and model validation tests documented by the code provider. | — | 23 |
| §1.6 | MANDATORY | If the client asks, this test information is provided together with the analyst's assessment of adequacy. | — | 23 |
| §1.6 | RECOMMENDED | If the analyst or the client concludes that the tests are not sufficiently relevant to the application concerned, additional tests should be performed and documented. This verification and validation process is outside the scope of the document. | — | 23 |
| §1.6 commentary | COMMENTARY | The ASME definitions are adopted: code verification (correct implementation of the model in the code), solution verification (accuracy of the numerical solution relative to the estimate of the exact solution), validation (the degree to which the results represent experimental data in the context of use). Verification does not involve comparison with measurement. Code verification is done by the developer; solution verification and application-specific validation by the user. In CWE validation is mostly done against controlled wind tunnel experiments; the definition of a representative data set is out of scope. | — | 23 |
| §1.7 | MANDATORY | Determination of MWFRS, C&C and appurtenance wind loads by CWE requires peer review; the requirements are in Chapter 10. (The text says "requires", not "shall"; it is written as a binding requirement.) | — | 24 |

### §1.8 Definitions (PDF pp. 24–26) — all INFORMATIVE

Terms not defined here are used in the document with their meaning in the wind provisions of ASCE/SEI 7-22.

| Term | Definition in our own words | PDF page |
|---|---|---|
| Aerodynamic roughness length (z0) | A measure of surface roughness related to the typical obstacle size; sets the distribution of velocity with height. | 24 |
| Aeroelastic feedback | The motion of a body in the wind changing the wind load acting on it. | 24 |
| Aeroelastic model | A model that simulates the stiffness, mass and damping of the full-scale structure. | 24 |
| Aeroelastic structure | A flexible structure whose own motion affects the aerodynamic forces. | 24 |
| Approach flow region | The mesh region extending from the inlet boundary up to the study region and also including the study region. | 24 |
| Approved | Found acceptable by the authority having jurisdiction. | 24 |
| Atmospheric boundary layer (ABL) | The lower part of the atmosphere; typically 3,000–13,000 ft (1,000–4,000 m) deep in strong winds; speed increases with height and the flow is turbulent. | 24 |
| Atmospheric surface layer | The lower part of the ABL in which the profile is logarithmic over flat and uniformly rough terrain. | 24 |
| Authority Having Jurisdiction (AHJ) | The organization or person responsible for administering and enforcing the provisions of the document. | 24 |
| Background region | The part of the domain not covered by the approach flow, local flow and near-wall regions. | 24 |
| Blockage ratio | The ratio of the projected area of the model and the proximate model(s), in the plane normal to the flow axis, to the cross-sectional area. Note: the source text says "the cross section of the model" in the denominator; this looks like a drafting inconsistency and has been carried over as is. | 24 |
| Code verification | Establishing that the code implements the mathematical model correctly. | 24 |
| Components and cladding (C&C) | Elements of the building envelope or of appurtenances/rooftop equipment that are not regarded as MWFRS. | 24 |
| Computational domain (CD) | The virtual volume in which the air flow around the structure is simulated. | 24 |
| Cell | A control volume into which the domain is divided. | 24 |
| Dynamic amplification factor (DAF) | A multiplier applied to the static load coefficient to account for the inertial load arising from modal excitation; depends on wind speed, structural frequency and structural + aerodynamic damping. | 24 |
| Edge / Face | The boundary of a face / the boundary of a cell. | 24 |
| Flexible structure | A structure for which the inertial load effect in the wind response is significant. | 24 |
| Incident location | The most upstream place in the computational domain where a building or topography is added. (Repeated in §4.1: the most upstream location where a building or topography will be added in the second step; Figure 4-1.) | 24 (and 43) |
| Inlet boundary | The upstream edge where the wind enters the domain. | 24 |
| Integral (macro) length scale | A length representing the typical size of the eddies/gusts in the boundary layer. | 25 |
| Lateral / Longitudinal / Vertical turbulence | Fluctuations of velocity in the horizontal direction normal to the mean wind / in the mean wind direction / in the vertical direction. | 25, 26 |
| Local flow region | The mesh region that encloses the study building and its immediate surroundings and captures load-affecting phenomena such as impingement, separated shear layer, separation bubble and wake. | 25 |
| Longitudinal integral time scale | The average duration of the eddies in the wind direction; the integral length scale divided by the mean speed at the same height. | 25 |
| Main wind force resisting system (MWFRS) | The assemblage of elements providing support and stability for the structure as a whole; generally receives load from more than one surface. | 25 |
| Mesh | The whole set of cells in the domain. | 25 |
| Meshing region | A subdomain whose resolution and structure are adjusted to capture particular flow features; four types: approach flow, local flow, near-wall, background. | 25 |
| Monte Carlo simulation | Generation of sequences of events (e.g. hurricane speeds) by drawing from the statistical properties of the phenomenon. | 25 |
| Near-wall mesh | The region adjacent to solid boundaries (building, terrain, ground) where wall-affected turbulence is resolved or modeled; the zone where wall treatments (refinement, wall function, low-Reynolds modeling) are required. | 25 |
| Non-boundary layer flows | Winds that do not conform to atmospheric boundary layer characteristics. | 25 |
| Partial turbulence simulation | An approach that simulates particular aspects of the turbulence spectrum rather than all of it. | 25 |
| Product | Components that can be added to buildings (e.g. rooftop solar panels) or stand-alone structures used at many sites; mostly mass-produced. | 25 |
| Radius of proximity | The radius of the circle centered on the study building outside which explicit geometric details have no direct interference effect on the aerodynamics of the study region. | 25 |
| Recognized literature | Published research and technical papers that have passed peer review. | 25 |
| Return period (MRI) | The average number of years between two events of the same kind; mean recurrence interval. | 25 |
| Reynolds number | The ratio of inertial forces to viscous forces: Ub·Lb/ν. | 25 |
| Rigid structure | A building for which the inertial load effect in the wind response is negligible. | 25 |
| Sand-grain roughness height | In the computational model, the height of a single layer of closely packed elements giving the same flow resistance as the representative full-scale surface. | 25 |
| Solution verification | Establishing the accuracy of a particular numerical solution relative to the estimate of the exact solution of the model. | 25 |
| Study building | The main structure whose wind effects are studied; excluding surrounding buildings and terrain features. | 25 |
| Study region | The bounding box enclosing the study building, its explicitly modeled surroundings and the relevant nearby topography; does not include the approach flow region. | 25 |
| Synthetic wind records | Time series generated so as to be statistically similar to real measurements. | 26 |
| Tornado | A rotating column of air in contact with the ground, generally attached to the base of a storm cloud. | 26 |
| Tropical cyclone | Circulation around a low pressure originating over tropical oceans; hurricane in the Americas (sustained wind above 74 mi/h), typhoon in Asia-Pacific. | 26 |
| Turbulence | Random fluctuations, gusts, in velocity/pressure. | 26 |
| Up-crossing method | A statistical method that computes the mean recurrence rate of events of a given magnitude. | 26 |
| Validation | Confirmation that the simulation results correctly represent the real physical phenomenon being modeled. | 26 |
| Vortex shedding | Alternate shedding of vortices from the two sides of a slender structure. | 26 |
| Wind climate model | The output of a probabilistic climate study containing speed and direction statistics. | 26 |

Notes on the definitions:
- §1.8 contains **no** definition of "proximity model"; only "radius of proximity" is defined, and the words "proximate model(s)" appear in the blockage ratio.
- The definition of "approach flow region" counts the study region as "included", while the definition of "study region" says it "does not include" the approach flow region. Reading the two definitions together: the approach flow region contains the study region, and the converse does not hold. The text does not explain this further.

### §1.9 Notation (PDF pp. 26–27) — INFORMATIVE

| Symbol | Meaning |
|---|---|
| B | Characteristic building dimension: the smaller of the least horizontal dimension and the mean roof height |
| By | Largest transverse width of the streamwise projection of the explicitly modeled study and surrounding structures (and topography) |
| f | Coriolis parameter |
| h | Mean roof height (from the average ground level around the structure) |
| hav | Average of the mean roof heights of all explicitly modeled structures |
| hmax | The larger of the building height and the average height of the surrounding buildings |
| hs | The larger of the study building height (h) and the average height of the surrounding buildings (Figure 6-1) |
| Lb | Characteristic cross-sectional length scale of the structure |
| lCD,x,u / lCD,x,d | Length of the computational domain in the upstream / downstream direction |
| lCD,y / lCD,z | Width / height of the computational domain |
| Lu^x, Lu^y, Lu^z | Integral length scale of the longitudinal turbulence component in the x, y, z directions |
| Iu, Iv, Iw | Longitudinal, lateral, vertical turbulence intensity |
| k | Turbulence kinetic energy |
| n, nc | Frequency, cutoff frequency |
| P | Pressure |
| S | Power spectral density |
| u* | Friction velocity |
| u′ | Instantaneous turbulent fluctuation |
| U | Mean velocity |
| Ub | Characteristic velocity appropriate for the building or appurtenance |
| Uref, Us | Mean velocity at height zref and zs |
| u | Instantaneous velocity (U + u′) |
| vR | All-direction design wind speed for return period R |
| z, z0 | Height above ground, aerodynamic roughness length |
| zg | Gradient height (top of the boundary layer) |
| zref | Height at which the mean velocity is measured/referenced |
| zs | Surface layer height; about 10% of the boundary layer height |
| α | Power law exponent for the variation of mean velocity with height |
| κ | von Kármán constant |
| ν | Kinematic viscosity of air |
| Subscripts | m: model; b: building; g: gradient; 0: ground; p: prototype (full scale); ref: reference; s: surface layer |

Note: the definitions of hmax and hs are almost identical in the text; the difference cannot be determined from the text.

## Chapter 2 — Computational wind engineering process

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §2.1 | INFORMATIVE | Scope: minimum requirements for estimating by CWE the wind loads on the MWFRS and on individual structural appurtenances / C&C of buildings and appurtenances. | — | 29 |
| §2.1 | MANDATORY | Loads produced by simulation shall satisfy the performance requirements of the document in order to be usable as design loads in jurisdictions that permit the computational approach. | — | 29 |
| §2.1 commentary | COMMENTARY | CWE can also do things beyond this document (multiphase / multispecies flow, simulations for which the mean flow alone is enough). The approach in the document can also be used for more reliable quantification of turbulent flow for pedestrian comfort and safety. | — | 29 |
| §2.2 | INFORMATIVE | Coordinate system: right-hand rule; x streamwise, y lateral, z vertical. U, V, W mean velocities; u′, v′, w′ fluctuating components. | — | 29 |
| §2.3 | INFORMATIVE | Figure 2-1 is a flowchart showing the layout of the document and the process expected in a CWE study. The content of the figure is not in the plain-text source (caption only). | not found in text | 29–30 |

## Chapter 4 — General simulation requirements

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 4-1 (§4.1) | MANDATORY | The simulation process shall verify that the approach wind field is represented correctly within the computational domain. Once the correct field has been obtained, the building aerodynamics simulation may proceed. | — | 43 |
| §4.1 | MANDATORY | The computation is done with a two-step process (Figure 4-1): Step 1 approach flow simulation, Step 2 building aerodynamics simulation. | 2 steps | 43 |
| AC 4-1 (§4.1, Step 1) | MANDATORY | A simulation without the structure(s) is run to verify that the model correctly represents the target wind flow conditions at the incident location within the computational domain. Incident location: the most upstream location where a building or topography will be added in the second step. | — | 43 |
| §4.1 (Step 2) | MANDATORY | The site-specific building model is added to the domain. Relative to Step 1 the changes in model choices are limited to: (i) addition of the structures, (ii) extension of the domain in the lateral and/or streamwise direction if needed to avoid unwanted effects of the boundary conditions, (iii) local mesh refinement around the structures. | — | 43 |
| §4.1 | INFORMATIVE | Additional requirements: §4.2 applies to both steps; Chapter 5 gives the requirements for Step 1, Chapter 6 for Step 2. | — | 43 |
| §4.2.1 | INFORMATIVE | In determining peak wind loads it is important to resolve the turbulence structures and the associated velocity/pressure fluctuations. | — | 43 |
| PO 4-2 (§4.2.1) | MANDATORY | The simulation method shall resolve the evolution in time and space of the important turbulence scales in the flow. | — | 44 |
| AC 4-2 (§4.2.1) | MANDATORY | An LES method with a body-fitted mesh approach is used. | — | 44 |
| §4.2.1 | INFORMATIVE (permission) | Wall-modeled LES may be used; it can be a hybrid form that solves RANS near the wall and connects to LES a little further away, or a form in which the LES equations are solved in the whole domain. | — | 44 |
| §4.2.1 commentary | COMMENTARY | The most common and proven route is finite volume LES with a body-fitted mesh; wall-modeled LES results have been validated against wind tunnel and field experiments for various building geometries and with different codes. In cases where individual gust conditions are explicitly required (sometimes pedestrian safety, air quality) the PO/ACs here remain valid as recommendations. Immersed boundary and lattice Boltzmann methods had not, at the date of publication, been validated for peak loads across different geometries and solvers; the sensitivity to model choices is not sufficiently known; with an immersed boundary, reconstruction of the surface pressure can be difficult where the boundary is not aligned with the mesh. | — | 44 |
| §4.2.2 | INFORMATIVE | The PO/ACs on mesh resolution are given separately: Chapter 5 for the approach flow, Chapter 6 for the building aerodynamics. | — | 44 |
| PO 4-3 (§4.2.2) | MANDATORY | The spatial discretization and gradient interpolation methods are chosen so as to reduce numerical error and the damping of resolved turbulence. | — | 45 |
| AC 4-3 (§4.2.2) | MANDATORY | The spatial discretization schemes are at least second order. | ≥ 2nd order | 45 |
| PO 4-4 (§4.2.2) | MANDATORY | The temporal discretization is chosen so as to reduce numerical error. | — | 45 |
| AC 4-4 (§4.2.2) | MANDATORY | The temporal discretization is at least second-order accurate; the time step is chosen so as to maintain stability and to resolve the time evolution of all eddies resolved in space; the Courant-Friedrichs-Lewy (CFL) number is reported. | ≥ 2nd order; CFL reported (no mandatory numerical threshold) | 45 |
| PO 4-5 / AC 4-5 (§4.2.2) | MANDATORY | The subgrid-scale (SGS) model represents the effect of unresolved turbulence on the resolved flow in a physically consistent way. (The text gives the PO and the AC together in a single sentence.) | — | 45 |
| §4.2.2 commentary – space | COMMENTARY | To prevent excessive damping of turbulence structures the schemes should be at least second order; this is necessary but not sufficient. Second-order accuracy is generally obtained on structured Cartesian or well-aligned unstructured meshes; irregular meshes and high skewness degrade accuracy. Many solvers blend first and second order for convergence; this is why the mesh dependency analysis of Chapter 6 is needed. | — | 45 |
| §4.2.2 commentary – time | COMMENTARY | For the time evolution of the resolved eddies the CFL number should be of order 1. Implicit methods can be stable at higher CFL. A CFL that is too high over a large part of the domain reduces accuracy; exceeding 1 locally, on the other hand, can give accurate results while reducing cost. As long as the acceptance criteria of Chapters 5 and 6 are met, a time step giving CFL > 1 in some places may be used. Note: in the source text the CFL definition is written in the form "U Δx/Δt"; this is most probably a typesetting error (the form seen in the source has been carried over, no correction made). | CFL ≈ 1 (recommendation, commentary) | 45 |
| §4.2.2 commentary – SGS | COMMENTARY | In finite volume the most common route is a subgrid-scale model with the linear eddy viscosity assumption. As the mesh is refined the effect of the model choice decreases; since peak loads require a fine mesh the effect is limited, and accurate results have been obtained with various models. For this reason no requirement for a particular subgrid-scale model is set; the mesh dependency analysis of Chapter 6 must demonstrate the required accuracy. | — | 45 |
| PO 4-6 (§4.2.3) | MANDATORY | The discretized system of equations is solved with a stable and accurate solution method. | — | 46 |
| AC 4-6a (§4.2.3) | MANDATORY | If an iterative procedure is used within the time step, convergence criteria are applied to converge the solution before moving to the next step. For non-iterative, directly computed time integration methods no check of iteration convergence is required; however, numerical stability and consistency checks are made at every step: enforcement of the relevant CFL condition, verification of physical boundedness, monitoring of the temporal variation of the solution. (Only "4-6a" is seen in the source; "4-6b" was not found in the text.) | No numerical residual threshold given | 46 |
| §4.2.3 commentary | COMMENTARY | Pressure-velocity coupling is essential for mass conservation; PISO-type corrector steps reduce the divergence error, and highly unsteady flows may need additional correctors. The coupling must not produce artificial damping or spurious oscillation; these can give a solution that is formally converged but physically wrong. It is important that the continuity residuals remain small at every step. | — | 46 |
| §4.2.4 | INFORMATIVE | The simulation may be done at full scale or at reduced geometric and/or velocity scale. For possible scaling requirements (geometric, kinematic, dynamic similarity) reference is made to ASCE/SEI 49-21 §2.2. | — | 46 |
| PO 4-7 (§4.2.4) | MANDATORY | If scaling is used, the same scale factors are used in the approach flow and building aerodynamics simulations; in this way the similarity criteria that ensure consistency of the lengths in the two simulations are met. | — | 46 |
| AC 4-7 (§4.2.4) | MANDATORY | The geometric and velocity scales are chosen so as to satisfy the model Reynolds number criterion (Equation 4-1). Lb is the relevant dimension of the building, Ub is the wind speed at roof height; the values are those in the computational model (subscript m). | (Lb·Ub/ν)m ≥ 11,000 (dimensionless) | 46 |
| §4.2.4 | MANDATORY | If the criterion cannot be met, or if the building has a rounded/streamlined shape that may give rise to Reynolds dependence, additional simulations (e.g. at a higher Reynolds number) are made for both the wind simulations and the building aerodynamics simulations. | — | 46 |
| §4.2.4 | MANDATORY | If reduced scale is used for appurtenances, a sensitivity study is made showing that the results represent the expected loading conditions and are independent of Reynolds number; the Reynolds number is defined with a characteristic length relating to the appurtenance (e.g. a representative dimension of the appurtenance). | — | 46 |
| §4.2.4 commentary | COMMENTARY | At the high Reynolds numbers of interest to CWE the flow around sharp-edged buildings is independent of Reynolds number. For appurtenances the relevant Reynolds number is based on the local speed near the appurtenance, and the effects are not well known. Full-scale simulation is best; at reduced scale independence must be verified. Wind tunnel methods solve this with a large model scale and partial turbulence simulation; the same methods can be used in LES. | — | 47 |

## Unclear points / gaps in the source

- Figure 1-1 (loading chain), Figure 2-1 (flowchart) and Figure 4-1 (two-step process and incident location) are present in the plain-text source only as captions; the drawing content could not be verified.
- Equation 4-1 is corrupted in the text extraction; it reads as "Lb Ub / ν, subscript m, ≥ 11,000" and is consistent with the surrounding text.
- The "U Δx/Δt" form in the CFL definition (PDF p. 45) is like this in the source; a typesetting error is highly probable.
- The denominator of the "blockage ratio" definition (PDF p. 24) is written inconsistently in the source.
