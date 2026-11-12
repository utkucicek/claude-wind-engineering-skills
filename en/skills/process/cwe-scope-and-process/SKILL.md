---
name: cwe-scope-and-process
description: "Use when asked about the scope of the ASCE computational wind engineering prestandard (Prestandard for Use of Computational Wind Engineering in Building Design, CWE), what it excludes, the permitted tools (LES, wall-modeled LES, hybrid RANS/LES; status of RANS, LBM, immersed boundary), verification and validation, the two-step process (approach flow + building aerodynamics), the incident location and the basic definitions, or when a CFD wind load study has to be checked from the start for conformance with this document."
---

# CWE prestandard: scope and process (Chapters 1, 2 and 4)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 1 (General), Chapter 2 (Process), Chapter 4 (General simulation requirements). Detailed clause table: `reference.md`. Page numbers are PDF page order (printed page = PDF page − 18).

## When to use

- Before starting a wind load CFD study, to answer "is this job within the scope of the document, and which solver/method is accepted?".
- When asked whether an existing study (e.g. RANS, LBM, immersed boundary method, AI surrogate model) conforms to the prestandard for design wind loads.
- When the meaning of terms such as "incident location", "approach flow region", "study region" or "radius of proximity" is needed.
- When asked how the two-step process (empty domain + domain with building) is set up and what may change between the two steps.
- When the requirements on discretization order, time step/CFL, subgrid-scale model, convergence within a time step and scaling/Reynolds number are to be checked.

Not for: the target wind profile and climate model, see `target-wind-definition`; the detailed criteria for the approach flow simulation (Chapter 5) and the building aerodynamics simulation (Chapter 6) are outside this skill.

## Purpose and structure of the document

- Purpose: to bring to the computational method a counterpart of the standardization that exists for wind tunnel testing; to define, through performance objectives and acceptance criteria, the path to load estimates usable in design for the main wind force resisting system (MWFRS), components and cladding (C&C) and appurtenances (§1.1).
- The document is not a "how-to" guide; the user must have a background in wind engineering and turbulence (§1.2).
- There are two kinds of clause: performance objective (Performance Objective, PO x-y) and acceptance criterion (Acceptance Criterion, AC x-y). A PO describes good practice and allows freedom of method as long as the outcome is achieved; an AC is a pass/fail criterion. Not every PO has an AC; where several ACs belong to one PO they are distinguished by a letter (a, b, c) (§1.2).
- The structure follows the Davenport wind loading chain: wind climate → terrain effect → aerodynamic effect → dynamic effect → criteria. A CWE study must address every link of the chain (§1.4, commentary).
- Chapters 1 and 2 contain no numbered PO/AC; the obligations are plain "shall" sentences. Chapter 4 contains PO 4-1 … 4-7 and the ACs attached to them.

## Step by step

1. **Scope check (§2.1, §1.5).** Is the job a building/appurtenance wind load (MWFRS, C&C, appurtenance)? Does it fall under one of the exclusions below?
   - Aeroelastic simulation with a moving mesh: out of scope. The document is for a rigid building model; limited aeroelastic behavior such as resonance is obtained by post-processing the aerodynamic data (§1.5.4).
   - Future conditions due to climate change: no method is given (§1.5.2).
   - Load estimation by artificial intelligence: outside the focus of the document; the assessment is made with the tools of Chapter 4 (§1.5.5).
   - Database-assisted design (DAD) / data-enabled design (DED): outside the focus (§1.5.6).
   - Wind-driven rain, snow, hail: not addressed (§1.1 commentary).
   - Non-synoptic winds (tornado, thunderstorm): approaches appear in the commentaries of Chapters 4–6; from Chapter 7 onward (the step from event to characteristic load) there is no method (§1.5.1 commentary).
   - Other structures and products (transmission tower, silo, solar panel array): the same approach is considered valid; the PO/ACs of Chapters 3–6 continue to apply (§1.5.3).
2. **Competence and expert opinion (§1.2, §1.4).** Does the user have the theoretical background? The document shall not be used without competent wind engineering advice.
3. **Choice of tool (§1.3, §4.2.1; PO 4-2, AC 4-2).** For design loads: large-eddy simulation (LES) with a body-fitted mesh. Wall-modeled LES is permitted; this can be a hybrid RANS/LES that solves RANS near the wall, or a form that solves the LES equations in the whole domain.
4. **Code verification and validation documentation (§1.6).** Assess the range and rigor of the code provider's verification and validation tests; if the client asks, provide this information together with your own assessment of adequacy.
5. **Target wind conditions (Chapter 3).** Derive the targets direction by direction with the `target-wind-definition` skill.
6. **Scale decision (§4.2.4; PO 4-7, AC 4-7).** Full scale or reduced scale; if reduced, the same scale factors in both steps and model Reynolds number ≥ 11,000.
7. **Numerical settings (§4.2.2–4.2.3; PO 4-3 … 4-6).** At least second-order spatial and temporal discretization; report the CFL number; physically consistent subgrid-scale model; convergence criterion within the time step.
8. **Step 1 – approach flow simulation (§4.1; PO 4-1, AC 4-1).** In the domain without structures (empty), show that the target wind conditions are achieved at the incident location. Details: Chapter 5.
9. **Step 2 – building aerodynamics simulation (§4.1).** Add the site-specific building model. Relative to Step 1 only the following may change: addition of the structures; extension of the domain in the lateral and/or streamwise direction if needed to avoid boundary condition effects; local mesh refinement around the structures. Details: Chapter 6.
10. **Peer review (§1.7).** Use of CWE for MWFRS, C&C and appurtenance loads requires peer review; the requirements are in Chapter 10.

## Flowchart (§2.3, Figure 2-1)

The document gives a flowchart (Figure 2-1, PDF p. 30) to guide the reader between chapters. The content of the figure is not in the plain-text source (only its caption); do not invent its boxes. The sequence that can be verified from the text is the structure of the document itself: wind climate and target flow conditions (Chapter 3) → general simulation requirements and the two-step process (Chapter 4) → approach flow simulation (Chapter 5) → building aerodynamics simulation (Chapter 6) → determination of overall wind effects, quality assurance, reporting, peer review (Chapter 10) (§1.4, §4.1, §1.7).

## Which tool for which purpose

| Tool / method | Status for design wind loads | Basis |
|---|---|---|
| Finite volume LES with body-fitted mesh | Required method | AC 4-2, §1.3 |
| Wall-modeled LES (including hybrid RANS/LES) | Permitted | §4.2.1, §1.1 |
| Approaches that do not resolve turbulence (steady) | Not accepted for loads (load estimation requires turbulence-resolving LES); established in other guidelines for pedestrian comfort and air quality, and mostly sufficient there | §1.1 and its commentary |
| Immersed boundary method | Not addressed in the document; not validated for peak loads across different geometries and solvers | §1.3, §4.2.1 commentary |
| Lattice Boltzmann method (LBM) | Not addressed in the document; same reason | §1.3, §4.2.1 commentary |
| Artificial intelligence / surrogate model | Outside the focus; in the commentary it is seen as a complement to simulation, not a replacement (interpolation between directions, parametric surrogate model, post-processing) | §1.5.5 |
| DAD / DED | Outside the focus; may be useful for standard designs | §1.5.6 |

Note: where individual gust conditions have to be seen explicitly for pedestrian safety or air quality, the PO/ACs here remain valid as recommendations (§4.2.1 commentary).

## Verification and validation (§1.6)

- **Code verification:** showing that the mathematical model has been implemented correctly in the code; the code developer's job.
- **Solution verification:** the accuracy of a particular numerical solution relative to the estimate of the exact solution of the computational model; the user's job (errors from space-time discretization, iteration, machine precision).
- **Validation:** the degree to which the model results represent experimental data for the context of use; usually done by the user for the specific application; in CWE mostly against controlled wind tunnel data.
- Verification does not involve comparison with measured data; validation does.
- The document leaves this process itself, and the definition of an experimental data set for validation, out of scope.

## Key definitions (§1.8, in our own words)

- **Incident location:** the most upstream place, relative to the flow, where a building or topography is added in the computational domain. §4.1 repeats this as "the most upstream location where a building or topography will be added in the second step". If surrounding buildings are modeled explicitly, this is the location of the first body added, not of the study building.
- **Approach flow region:** the mesh region that starts at the inlet boundary and also includes the study region.
- **Study region:** the bounding box enclosing the study building, its explicitly modeled surroundings and the relevant nearby topography. The definition also says that the study region does not include the approach flow region (for this tension between the two definitions see the note in `reference.md`).
- **Study building:** the main structure whose wind effects are studied; surrounding buildings and terrain are not included.
- **Radius of proximity:** the radius of the circle centered on the study building outside which geometric details have no direct interference effect on the aerodynamics of the study region. (The document gives no separate definition of "proximity model" in 1.8; only "proximate model(s)" appears in the blockage ratio definition.)
- **Local flow region:** the mesh region that encloses the study building and its immediate surroundings, where the load-governing phenomena such as impingement, separated shear layers, separation bubbles and the wake are captured.
- **Near-wall mesh:** the region adjacent to solid boundaries where wall-affected turbulence is resolved or modeled.
- **Background region:** the part of the domain not covered by the other three regions.
- **Meshing region:** there are four types: approach flow, local flow, near-wall, background.
- **Computational domain (CD):** the virtual volume in which the air flow around the structure is simulated.
- **Inlet boundary:** the upstream edge where the wind enters the domain.
- **Blockage ratio:** the ratio of the projected area of the model and proximate models, normal to the flow axis, to the cross-sectional area (the definition text appears corrupted in the source; `reference.md`).
- **Aerodynamic roughness length (z0):** a measure of surface roughness related to the typical obstacle height, which determines the distribution of velocity with height.
- **Atmospheric boundary layer (ABL):** the turbulent lower atmosphere, typically 1000–4000 m deep in strong winds, in which speed increases with height. **Atmospheric surface layer:** the lower part in which the profile is logarithmic over flat, uniformly rough terrain.
- **Integral length scale:** a length representing the typical size of the turbulent eddies in the boundary layer.
- **Rigid structure / flexible structure:** a structure for which the inertial effect in the wind response is negligible / significant.
- **MWFRS, C&C, product, return period (MRI), sand-grain roughness height** and others: `reference.md`.
- Terms not listed in 1.8 are used with their meaning in the wind provisions of ASCE/SEI 7-22.

## Mandatory requirements

- §1.2: The user shall have the necessary theoretical knowledge of wind engineering and turbulence.
- §1.4: The document shall not be used without competent wind engineering opinion.
- §1.5.5: The assessment is made with the tools of Chapter 4 (not artificial intelligence).
- §1.6: The analyst assesses the range and rigor of the verification/validation tests documented by the code provider; if the client asks, this information and the analyst's assessment of adequacy are provided.
- §1.7: Peer review is required for MWFRS, C&C and appurtenance loads (Chapter 10).
- §2.1: To count as design loads, the simulated loads shall satisfy the performance requirements of the document.
- PO 4-1 / AC 4-1 (§4.1): It is verified that the approach wind field is represented correctly; the two-step process is mandatory; Step 1 verifies the target conditions at the incident location with a simulation without structures; in Step 2 the changes are limited to three items.
- PO 4-2 / AC 4-2 (§4.2.1): The evolution in time and space of the important turbulence scales is resolved; LES with a body-fitted mesh is used.
- PO 4-3 / AC 4-3 (§4.2.2): Spatial discretization at least second order.
- PO 4-4 / AC 4-4 (§4.2.2): Temporal discretization at least second order; the time step ensures stability and the time evolution of the resolved eddies; the CFL number is reported.
- PO 4-5 / AC 4-5 (§4.2.2): The subgrid-scale (SGS) model shall be physically consistent (no particular model is imposed).
- PO 4-6 / AC 4-6a (§4.2.3): Stable and accurate solution method; for an iterative method, a convergence criterion within the time step; for a non-iterative method, stability and consistency checks at every step.
- PO 4-7 / AC 4-7 (§4.2.4): The same scale factors in both steps; model Reynolds number (Lb·Ub/ν) ≥ 11,000; additional simulations if this cannot be met or if the building has a rounded/streamlined shape; for appurtenances at reduced scale, a Reynolds sensitivity study.

## Common mistakes

- Presenting a RANS result as a design peak load. The document requires turbulence-resolving LES for load estimation.
- Describing work done with an LBM or immersed boundary solver as "compliant with the prestandard". The document does not address these methods; no claim of compliance can be made, only the statement that the method is out of scope.
- Skipping the empty-domain step or checking the target profile at the inlet boundary. The place of the check is the incident location.
- Taking the incident location at the position of the study building when surrounding buildings are present. The definition is based on the most upstream building/topography added.
- Changing the mesh resolution, numerical scheme, inflow generator or scale between Step 1 and Step 2. The permitted changes are three items.
- Treating the commentary statement "CFL should be of order 1" as a mandatory threshold. What is mandatory is that the CFL number is reported; exceeding 1 locally is accepted as long as the acceptance criteria of Chapters 5–6 are met (commentary).
- Writing that a particular subgrid-scale model is "mandatory". The document specifies no model; it refers to the mesh dependency analysis (Chapter 6).
- Confusing verification with validation; a wind tunnel comparison is validation, mesh/time-step sensitivity is solution verification.
- Computing the Reynolds criterion with full-scale values. The criterion is evaluated with Lb and Ub of the computational model.
- Drawing conclusions about aeroelastic instability from a rigid model result. Out of scope.

## Related skills

- `target-wind-definition` — Chapter 3: wind climate and target wind flow conditions.
- Chapter 5 (approach flow simulation) and Chapter 6 (building aerodynamics simulation) skills — the corresponding folders in this repository.
- Chapter 10 (peer review) and reporting skills.
