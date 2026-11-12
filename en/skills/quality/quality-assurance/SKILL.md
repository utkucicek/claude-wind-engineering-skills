---
name: quality-assurance
description: Use when auditing or planning the quality assurance of a CFD/LES wind load study; covers ASCE CWE Prestandard Chapter 8 and the Table 8-1 compliance matrix, verification/validation, the benchmark requirement, the mesh study (IRQ), time-step sensitivity and statistical convergence.
---

# Quality assurance (ASCE CWE Prestandard, Chapter 8)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 8 (Table 8-1),
plus §1.6, §6.6.3–6.6.5 and §9.5.4–9.5.6, on which Chapter 8 relies.
Page numbers are PDF sequence numbers (printed page = PDF − 18). Clause breakdown: `reference.md`.

Abbreviations: PO = Performance Objective, AC = Acceptance Criterion,
CWE = computational wind engineering, LES = large-eddy simulation,
RANS = Reynolds-averaged Navier–Stokes, IRQ = index of resolution quality,
SGS = subgrid scale.

## Structure of Chapter 8 — know this first

Chapter 8 is a short chapter: a single subsection (§8.1 Quality assurance workflow) and Table 8-1, which collects all the PO/AC clauses
of Chapters 3–7. It introduces no new PO/AC of its own. The opening sentence of the chapter mentions "a discussion on
simulation uncertainty", but in the text at hand there is no separate uncertainty subsection apart from §8.1 and the table
(not found in the text). There is no appendix either; after Chapter 10 come the References and the Index.

## When to use

- When, before a wind load CFD study starts, a list of "what evidence must I produce" is to be drawn up.
- When the compliance of a finished study with the Prestandard is to be audited clause by clause (compliance matrix).
- When the questions "can peak loads be obtained with RANS", "is benchmarking/validation mandatory", "how is mesh independence shown", "which studies are repeated on every project" come up.

## Step by step

1. **Confirm the method level (§8.1).** The document says that steady or unsteady RANS, whatever the turbulence closure, cannot give a reliable peak / fully transient solution for structural wind engineering; at a minimum, eddy-resolving transient approaches such as LES or wall-modeled LES are expected. Its counterpart in Table 8-1: PO/AC 4-2 (LES with a body-fitted mesh, including wall-modeled LES).
2. **Turn Table 8-1 into a compliance matrix.** Take the table rows in `reference.md`; for each AC add the columns "met / not met / not applicable", the location of the evidence in the report (figure, table, section) and, if there is a deviation, its justification. This table is mandatory in the report (§9.5.5).
3. **Assess the code verification and model validation documentation (§1.6).** The analyst assesses the scope and rigor of the verification/validation tests documented by the provider of the LES code used. If the client requests it, this information is provided together with the analyst's assessment of adequacy. If the scope is not sufficiently relevant to the application, additional testing should be done and documented (recommendation).
4. **Make solution verification project specific.** Studies repeated on every project (table below): mesh study, time-step sensitivity, statistical convergence, solver inner-iteration convergence, spectrum check.
5. **Prove the approach flow before the building run.** The Chapter 5 rows of Table 8-1: reproduction of the target profile and turbulence at the incident location in the empty domain, convergence of the velocity statistics, the spectrum cutoff frequency lying in the inertial subrange. Details and thresholds are in the Chapter 5 skill.
6. **Show the consistency of the building run (PO/AC 6-1).** Scale, solver, numerical method, turbulence model and boundary conditions must be consistent with the approach flow run.
7. **Add the design load quality check (PO/AC 7-16).** Mean/minimum/maximum force-moment plots versus direction, spectral response in the critical directions; the results of the other meshes in the mesh study on the same plot as well (recommendation).
8. **Write down the uncertainty and the known error sources (§9.5.4).** The uncertainty arising from the input parameters (wind data, terrain roughness model) is assessed; if a probabilistic method was used, its details are given; other known error sources are documented.
9. **Be honest about validation/benchmarking.** Because no reliable benchmark cases were available at the date of publication, the document does NOT MANDATE validation of the results against reference data; it RECOMMENDS reporting additional validation against representative experimental or high-fidelity simulation data (§9.5.4 commentary). If available, code verification and benchmark comparison documentation is added to the report (§9.5.6).
10. **Keep the digital records (§9.5.6).** A digital record of the models developed and the data produced is kept for quality control and future reference.

## Studies repeated on every project

| Study | Requirement | Numerical criterion | Clause, PDF p. |
|---|---|---|---|
| Mesh study | Performed for the project in at least two wind directions. | ≥ 2 directions | PO 6-15, p. 67 |
| IRQ | Does not fall below the lower limit at the key monitoring locations in the flow field and in the pressure field; the load differences between the two mesh resolutions are reported. | IRQ ≥ 75% | AC 6-15a, p. 67 |
| Monitoring locations | An array of virtual probes along the building height and out to a specified distance from the building; it captures the approach flow (especially upwind wakes) and the building wake. | up to 160 ft (~50 m) from the building | AC 6-15b, p. 67 |
| Mesh refinement factor | In the commentary: at most three meshes (coarse, medium, fine), refined by a successive factor r; ideally 2. The lower-limit value is corrupted in the text extraction. | r ideal = 2; lower limit: could not be read in the text | §6.6.4 commentary, p. 67 |
| IRQ interpretation | <75%: further refinement needed; 75–85%: suitable for an engineering solution; >85%: close to DNS. | 75% / 85% | §6.6.4 commentary, p. 68 |
| Time-step sensitivity | Is reviewed; velocity spectra are plotted at key locations around the building and between the upwind buildings and the target building; the cutoff arising from the mesh size and the time step is marked on the plot. | none | PO/AC 6-16, p. 68 |
| Time-step test (commentary) | If the spectrum of a second run with the time step halved is identical or very similar, the step is adequate; or the CFL number is kept constant in the mesh sensitivity study. | step × ½ | §6.6.5 commentary, p. 68 |
| Statistical convergence | The mean/standard deviation of the velocity and the mean, standard deviation and peak values of the load quantities must have converged. | duration > 500 longitudinal integral time scales (at the target building height) | PO/AC 6-14, p. 66 |
| Approach flow evidence | The quality of the turbulent flow at the incident location is shown for all different terrain conditions and all directions. | thresholds in Chapter 5 | AC 5-3, 5-9 (Table 8-1, pp. 83–84) |

Note: The Chapter 6 clauses in this table are the part read for this skill (§6.6.2.2–6.6.5). The thresholds of the other clauses of Chapters 3–6
appear in Table 8-1 only as headings; for numerical values see the skill for the relevant chapter / the PDF, do not produce numbers from here.

## Mandatory requirements

- §8.1: RANS (steady or not) is not considered reliable for peak and transient solutions; at least LES / wall-modeled LES is expected (the chapter text says "expected"; its binding counterpart is PO/AC 4-2).
- Table 8-1: the 53 PO and 84 AC clauses of Chapters 3–7; compliance with all of them is shown (§9.5.5 compliance matrix).
- §1.6: the analyst assesses the scope and rigor of the verification/validation tests documented by the code provider; provides it if the client requests.
- PO 6-14 / AC 6-14: statistical convergence; duration > 500 longitudinal integral time scales.
- PO 6-15 / AC 6-15a, 6-15b: mesh study in at least two directions; IRQ ≥ 75%; differences between the two meshes are reported.
- PO 6-16 / AC 6-16: time-step sensitivity; spectra and cutoff frequencies.
- PO 7-16 / AC 7-16: plots of integrated force/moment and spectral response.
- §9.5.4: the simulation quality is assessed in terms of mesh refinement, time-step sensitivity, inner-iteration solver convergence, statistical convergence and spectral properties; input uncertainty and known error sources are written down.
- §9.5.5: compliance summary table aligned with Table 8-1.
- §9.5.6: conditions that deviate from the Prestandard are justified; the digital record is kept; code verification / benchmark documentation is added if available.

## Checklist (yes/no)

- [ ] Is the method LES or wall-modeled LES (peak loads are not being taken from RANS)?
- [ ] For each AC row of Table 8-1, was "met/not met/not applicable" + the location of the evidence written?
- [ ] Is there a justification for every clause not met or deviated from?
- [ ] Was the verification/validation documentation of the code used reviewed and its adequacy assessed?
- [ ] Was the mesh study performed in at least two wind directions?
- [ ] Does the IRQ stay at or above 75% at the key locations (flow and pressure field)?
- [ ] Were the differences in load quantities between the two meshes reported?
- [ ] Was the time-step sensitivity examined; are the mesh and time-step cutoffs marked on the spectra?
- [ ] Is the simulation duration longer than 500 longitudinal integral time scales, and was mean/rms/peak convergence shown?
- [ ] Was the inner-iteration convergence of the solver reported?
- [ ] Was the approach flow in the empty domain compared with the target for all different terrain conditions and directions?
- [ ] Does the building run use the same scale/solver/scheme/model/boundary conditions as the approach flow run?
- [ ] Were the input uncertainty (wind data, roughness) and the known error sources written down?
- [ ] If validation/benchmarking was done, was it added to the report; if not, was it clearly stated that it is not mandatory but recommended?
- [ ] Is the digital record of the model and data files being kept?

## Common mistakes

- Saying "the Prestandard requires benchmark/wind tunnel validation". It does not; it recommends it (§9.5.4 commentary). Saying the opposite, i.e. "validation is unnecessary", is also wrong: assessment of the code verification/validation documentation is mandatory (§1.6).
- Expecting classical mesh independence. Commentary: in implicitly filtered LES the mesh size is the filter width; the solution becomes mesh independent only as it approaches DNS level. This is why the IRQ + a report of the difference between two meshes is required.
- Performing the mesh study in a single wind direction (at least two).
- Blindly taking the theoretical order of the method in the IRQ calculation; the commentary says to avoid adopting the theoretical value if the estimated order is markedly higher than the theoretical one, and not to underestimate the SGS contribution.
- Showing convergence only for the mean and forgetting the peak values (PO 6-14 also counts peak values).
- Giving the compliance matrix in an order different from Table 8-1, incomplete, or without showing evidence.
- "Guessing" numerical thresholds from the Table 8-1 headings. The table gives only topic headings.
- Treating peer review as a substitute for quality assurance; the §10.7 commentary says it does not replace normal quality assurance.

## Inconsistencies in the text extraction (reproduced as is)

- In Table 8-1 some cross-references are written with the abbreviation "A.O." (e.g. "A.O. 3-3" in the 5-4 row, "A.O. 6-5a" in the 6-5b row); it is understood that these mean AC, but this is how the text reads.
- The AC 5-3 row refers to "A.C. 5-8" for the acceptance levels; the row in the table that describes the acceptance requirements is AC 5-9. To be verified against the PDF.
- The AC 5-9 row reads "incipient location"; elsewhere it is "incident location".

## Related skills

- `skills/loads/design-wind-loads` — details of the Chapter 7 clauses (PO/AC 7-1 … 7-16).
- `skills/quality/report-and-peer-review` — presentation of the compliance matrix and the quality evidence in the report, and peer review.
- `skills/process/cwe-scope-and-process`, `skills/process/target-wind-definition`, `skills/simulation/empty-domain-verification`, `skills/simulation/domain-and-mesh`, `skills/simulation/boundary-conditions-and-quality`, `skills/simulation/topography-and-non-synoptic-wind` — the numerical thresholds of the Chapter 3–6 rows of Table 8-1 are in these skills.
