---
name: report-and-peer-review
description: Use when writing a CFD/LES wind load report, auditing an existing report for missing content, or planning an independent peer review; applies the ASCE CWE Prestandard Chapter 9 (report content, compliance matrix) and Chapter 10 (project peer review, basis of design, comment log, AHJ) requirements as a checklist.
---

# Report content and peer review (ASCE CWE Prestandard, Chapters 9 and 10)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapters 9 and 10.
Page numbers are PDF sequence numbers (printed page = PDF − 18). Clause breakdown: `reference.md`.
These chapters have no PO/AC numbers; the requirements are cited by subsection number (§9.x, §10.x).

Abbreviations: CWE = computational wind engineering, AHJ = Authority
Having Jurisdiction, EOR = Engineer of Record, MWFRS = main wind force resisting system,
DAF = dynamic amplification factor, CFL = Courant–Friedrichs–Lewy number,
PSD = power spectral density.

## When to use

- When setting up the skeleton of a wind load CFD report or auditing a draft report before delivery.
- When reviewing a CWE report prepared by someone else for "what is missing according to the Prestandard".
- When setting up the peer review: who can be a peer reviewer, what the scope is, which document is provided when, how disputes are resolved.
- When asked what to do when the design changes after the peer review.

## Step by step

### A. Preparing the report (Chapter 9)

1. **Write the purpose and scope (§9.1).** The primary scope of the simulation, its objectives, the main features of the project. The aim of the report: to allow a third party and, if necessary, the AHJ to carry out a detailed technical review; to show how the study aligns with the performance objectives of Chapters 2–7.
2. **Document the simulation parameters and split them into four subheadings (§9.2).** Method (§9.2.1), domain and mesh (§9.2.2), scaling (§9.2.3), study building (§9.2.4).
3. **Give the flow properties for two cases (§9.3).** Both for the "empty computational domain" and for the domain with the building and the proximity model added; where applicable, target and simulated values/profiles side by side.
4. **Present the results consistently with the scope (§9.4).** The list is the expected results of a study focused mainly on structural wind loads and response; if the scope is different the content may change (commentary).
5. **Add the reference information (§9.5).** Statistical method, structural property assumptions, limitations, quantification of the simulation quality, Table 8-1 compliance matrix, theoretical background of the method.
6. **Deliver the report in stages (§10.5).** First the basis of design together with the simulation parameters and assumptions, then the full report.

### B. Conducting the peer review (Chapter 10)

1. **Select the peer reviewer and notify the AHJ (§10.2).** The design team selects and forwards the selection to the AHJ for general concurrence. The peer reviewer has no conflict of interest, is not part of the design team, and is fully independent of the design team and of the sponsor of the simulation.
2. **Confirm competence (§10.1).** Seven areas: computational flow simulation including the boundary layer; wind engineering and bluff body flow; (if relevant) dynamic response of flexible structures; wind hazard definition; exposure determination; load determination by wind tunnel modeling; the requirements of this Prestandard.
3. **Hold a kickoff meeting (§10.4).** EOR, simulation team, (if appropriate) AHJ and the peer reviewers: scope of work, method of communication, frequency and timing of the review stages, how far the design will have progressed at each stage.
4. **Prepare a written scope of work (§10.3).** Seven items — in the checklist below.
5. **Have the basis of design reviewed first (§10.3-1).** BEFORE the full simulation; so that the comments are addressed before the final run.
6. **Handle the comments in writing (§10.5).** The peer reviewers give written comments in a timely manner; the design team resolves all comments to the satisfaction of the peer reviewers. A comment log is kept with dates (good practice, commentary).
7. **Closing report (§10.6).** The scope of the review, the comment log and the professional opinion of the peer reviewers on general compliance with the PO/AC requirements of the Prestandard.
8. **Do not blur responsibility (§10.7).** The responsibility for determining the loads and the response rests solely with the wind engineer who performs the simulation.
9. **Disputes and subsequent changes (§10.8, §10.9).** In an unresolved dispute, other experts meeting the same competence requirements are retained. If a substantial design change occurs after the review is finished, the EOR informs the AHJ; the AHJ may require additional review.

## Mandatory requirements

- §9 introduction: the report shows compliance with the performance objectives of Chapters 2–7; it directly addresses the headings below to the extent relevant to the scope.
- §9.1–§9.5.6: report content (details in the checklist).
- §9.5.5: compliance summary table aligned with Table 8-1.
- §10.1: when the Prestandard is used, an independent peer review is performed (also §1.7).
- §10.2: independence of the peer reviewer; a chair in a multi-person team.
- §10.3: written scope of work, seven items; the basis of design review is the first step.
- §10.4: kickoff meeting.
- §10.5: the Computational Wind Simulation Report based on Chapter 9 is provided in stages; written comments; the design team resolves the comments.
- §10.6: written peer review report.
- §10.7: the responsibility for determining the loads lies with the wind engineer.
- §10.8: in a dispute, additional experts, under the same requirements.
- §10.9: on a substantial change the EOR informs the AHJ.

## Checklist — report content (yes/no)

**Purpose and method (§9.1, §9.2.1)**
- [ ] Were the scope and objectives of the simulation and the main features of the project stated?
- [ ] Are the name, developer and version of the software given?
- [ ] Were the main features of the flow modeling and the turbulence generation approach (synthetic and/or natural), and the treatment of unresolved turbulence, described?
- [ ] Were the spatial discretization, gradient interpolation and temporal discretization methods stated?
- [ ] Were the solution method, time step, maximum CFL number and solver convergence criteria given?
- [ ] Were the total simulation duration, the duration used for statistics and the method of checking statistical convergence stated?

**Domain, mesh, scale, building (§9.2.2–§9.2.4)**
- [ ] Were the geometry of the computational domain and the inlet, ground, side, top, outlet boundary conditions documented?
- [ ] Was it stated how terrain elements and topographic features are represented in the domain?
- [ ] Was the variation of the mesh and resolution by region (approach flow, near/local flow, far field) described?
- [ ] Was the local resolution around the building, on the faces and at the corners reported?
- [ ] Were the geometric length scale, time scale and time step given?
- [ ] Were the treatment of the fluid density and the Reynolds number stated?
- [ ] Were the target and achieved blockage ratio in the domain with the building and surroundings added quantified?
- [ ] Was the CFL number given?
- [ ] Are the full geometry of the building, the surface parameters, the modeled and omitted appurtenances and images of the building included?

**Flow properties (§9.3)**
- [ ] Are the values given for both the empty domain and the domain with the building added, with target and simulated side by side?
- [ ] Were the local wind climate, the meteorological data source and the data quality described?
- [ ] Were the target reference speeds and return periods defined by direction?
- [ ] Were the approach terrain, the target exposure categories by direction and the storm types considered stated?
- [ ] Was it stated how directionality is to be handled in the simulation and in the results?
- [ ] Were all types of weather system that may affect the site, and how they are included in the simulation, described?
- [ ] Were the site-specific probabilistic climate model and the reference flow conditions documented?
- [ ] Was the mean velocity profile documented along the domain?
- [ ] Were the longitudinal, lateral and vertical turbulence intensity profiles documented along the domain?
- [ ] Are the turbulence integral length scale profile and its comparison with the full-scale atmospheric target included?
- [ ] Was the PSD of the velocity fluctuations given in three directions and compared with the full-scale atmospheric spectrum?
- [ ] If a partial turbulence model was used, was it stated how the missing low-frequency turbulence is accounted for?
- [ ] Were the topographic features included described?
- [ ] If relevant, was it stated how the effect of extratropical and non-synoptic storm systems is handled?

**Results (§9.4)**
- [ ] Was it described by what means the forces are measured in the simulation?
- [ ] Were the x, y, z axis system and its relation to the project axes defined?
- [ ] Were the number of directions considered and how the directions form the basis of the results stated?
- [ ] Were the mean and standard deviation of the force and moment coefficients given for all directions, before and after the directionality effect?
- [ ] Are there PSD plots of the along-wind and across-wind response for the base overturning moment and base shear, in the critical directions?
- [ ] Were the base shears and overturning moments given at the reference elevation(s), in two orthogonal directions, for the return periods and directions considered?
- [ ] Are there mean/minimum/maximum plots versus direction of the base shear, overturning moment and torsion?
- [ ] Was the method of measuring the forces along the building height and determining the base forces described?
- [ ] Was the DAF of the overall building loads quantified?
- [ ] (If in the scope or requested by the AHJ/peer reviewer) is the sensitivity of the shears and moments to damping, mass and frequency included?
- [ ] Were the story-by-story equivalent static (or effective) wind loads given?
- [ ] Are there direction-combined load cases, including torsion, that capture the effect of all relevant directions?
- [ ] Were the overall design loads found by the code/standard method given and compared with the CWE loads?
- [ ] Are building motion estimates (lateral and torsional accelerations, at the requested locations, peak acceleration for the specified return periods) included?
- [ ] (If requested) is the sensitivity of the accelerations to damping, mass and frequency included?
- [ ] Were the local and area-averaged cladding pressures given for the specified return periods, over the whole envelope, positive and negative, as mean and peak?
- [ ] Were the treatment of the associated internal pressure and the local pressure measurement locations and method described?
- [ ] For long-span flexible elements, was the equivalent static load including dynamic effects given, with the tributary area taken into account?
- [ ] For appurtenances (rooftop equipment, canopies, signs, masts), are the peak force and moment demands and a comment on aeroelastic effects (flutter, galloping) included?
- [ ] Was it stated how internal pressures are handled and how they enter the design loads?

**Reference information (§9.5)**
- [ ] Was the statistical method that combines the climate with the structural response documented?
- [ ] Were the assumed mass, damping, stiffness and mode shapes and their source (sponsor data, code estimate, measurement) stated?
- [ ] Were the main limitations of the approach and the assumptions affecting accuracy/applicability stated?
- [ ] Was the quality assessed in terms of mesh refinement, time-step sensitivity, inner-iteration convergence, statistical convergence and spectral properties?
- [ ] Were the uncertainty arising from the input parameters and other known error sources assessed?
- [ ] Is there a compliance summary table aligned with Table 8-1?
- [ ] Were the equations, turbulence models and discretization techniques summarized; were deviations from the Prestandard justified?
- [ ] Was code verification / benchmark comparison documentation added if available; is the digital record of the model and data being kept?

## Checklist — peer review (yes/no)

- [ ] Is (are) the peer reviewer(s) fully independent of the design team and the sponsor, with no conflict of interest?
- [ ] Was the selection notified to the AHJ?
- [ ] Are the seven competence areas in §10.1 covered?
- [ ] If there is more than one person, was a chair designated?
- [ ] Was the kickoff meeting held (scope, communication, stage schedule)?
- [ ] Does the written scope of work contain these seven items: (1) basis of design review, (2) wind hazard and simulation technique, (3) setup, inputs, domain generation, run, results and compliance with the acceptance criteria, (4) evaluation of the results against the PO/AC, (5) design loads and other outputs, (6) other matters important for the performance objectives, (7) peer reviewer comments?
- [ ] Was the basis of design reviewed before the full simulation?
- [ ] Was the report provided in stages?
- [ ] Are the comments in writing and were all of them resolved to the satisfaction of the peer reviewers?
- [ ] At closure, is there a written peer review report containing the scope + comment log + compliance opinion?
- [ ] Are the peer review documents kept without being mixed into the construction (contract) documents?
- [ ] If a substantial design change occurred after the review, was the AHJ informed?

## Common mistakes

- Giving only the flow profiles of the domain with the building added; the empty domain results and the target–simulation comparison are also required (§9.3).
- Not putting the code loads in the report; §9.4.5.5 requires both that they be given and that they be compared with the CWE.
- Omitting the DAF, the blockage ratio, the CFL number or the software version.
- Arranging the compliance matrix in a form independent of Table 8-1.
- Writing "the Prestandard requires validation"; the §9.5.4 commentary does not mandate validation, it recommends it.
- Treating the peer reviewer as jointly responsible for the wind load (§10.7) or attaching the peer review correspondence to the project drawings (commentary).
- Skipping the basis of design review and confronting the peer reviewer with a finished run (§10.3-1).
- Selecting the peer reviewer from within the design team or the sponsor.
- Not notifying the AHJ after the shape, mass distribution, stiffness or damping has changed (§10.9 and its commentary).
- Attributing requirements to the document that it does not contain: the number of peer reviewers, a licensing requirement (commentary: some jurisdictions may require it, it is not a general requirement of the Prestandard), the review duration are not in the text.

## Related skills

- `skills/quality/quality-assurance` — Table 8-1 compliance matrix and quality evidence.
- `skills/loads/design-wind-loads` — how the load results to be presented in the report are produced (Chapter 7).
- `skills/process/cwe-scope-and-process`, `skills/process/target-wind-definition`, `skills/simulation/*` — acceptance criteria for the flow properties and simulation parameters (Chapters 3–6).
