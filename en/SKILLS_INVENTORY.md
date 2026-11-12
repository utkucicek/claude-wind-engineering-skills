# Skill inventory

15 skills in total.

## Process (CWE Chapters 1–4)

| Skill | When to use | Files |
|---|---|---|
| [cwe-scope-and-process](skills/process/cwe-scope-and-process/SKILL.md) | Use when asked about the scope of the ASCE computational wind engineering prestandard (Prestandard for Use of Computational Wind Engineering in Building Design, CWE), what it excludes, the permitted tools (LES, wall-modeled LES, hybrid RANS/LES; status of RANS, LBM, immersed boundary), verification and validation, the two-step process (approach flow + building aerodynamics), the incident location and the basic definitions, or when a CFD wind load study has to be checked from the start for conformance with this document. | SKILL.md, reference.md |
| [target-wind-definition](skills/process/target-wind-definition/SKILL.md) | Use when the wind climate model and the target wind flow conditions at the incident location are to be defined according to Chapter 3 of the ASCE CWE prestandard: storm types, mean wind speed profile, turbulence intensity, integral length scale, power spectral density, Reynolds stress, roughness length z0, exposure change and topography effect. | SKILL.md, reference.md |

## Simulation (CWE Chapters 5–6)

| Skill | When to use | Files |
|---|---|---|
| [boundary-conditions-and-quality](skills/simulation/boundary-conditions-and-quality/SKILL.md) | Use when setting up the boundary conditions (no-slip wall, wall model, y+, reference static pressure) of a building aerodynamics LES simulation and when performing or reporting its quality assurance (solver convergence, contour plots, monitoring probes, statistical convergence, sampling duration, mesh sensitivity, IRQ, time-step sensitivity, CFL); gives the requirements of Sections 6.1, 6.5 and 6.6 of the ASCE CWE Prestandard. | SKILL.md, reference.md |
| [domain-and-mesh](skills/simulation/domain-and-mesh/SKILL.md) | Use when setting up or checking the geometry model (study building, proximity model, radius of proximity, topography, appurtenances, porous components), the computational domain size (blockage ratio) and the mesh (mesh regions, refinement, IRQ) for a building aerodynamics simulation; gives the requirements of Sections 6.2, 6.3 and 6.4 of the ASCE CWE Prestandard. | SKILL.md, reference.md |
| [empty-domain-verification](skills/simulation/empty-domain-verification/SKILL.md) | Use when it has to be demonstrated, before the building is added, that the approach flow in the empty domain matches the target atmospheric boundary layer at the incident location; checks the inflow turbulence (precursor, recycling, synthetic inflow), ground roughness z0, U and I_u profile error, integral length scale, spectrum, cutoff frequency and pressure fluctuation criteria against Sections 5.1 and 5.4 of the ASCE CWE Prestandard. | SKILL.md, reference.md |
| [topography-and-non-synoptic-wind](skills/simulation/topography-and-non-synoptic-wind/SKILL.md) | Use when the target wind profile comes from a separate topography simulation (topography Method 1, reproduction in the empty domain without the topography) or when asked about simulating non-synoptic wind such as a downburst or tornado; states what Sections 5.2 and 5.3 of the ASCE CWE Prestandard require and what they leave out of scope. | SKILL.md, reference.md |

## Loads (CWE Chapter 7)

| Skill | When to use | Files |
|---|---|---|
| [design-wind-loads](skills/loads/design-wind-loads/SKILL.md) | Use when deriving design wind loads from CFD/LES (CWE) results; applies the ASCE CWE Prestandard Chapter 7 requirements for pressure coefficient (Cp) definition and reference velocity, peak estimation (Gumbel, extreme value), the components and cladding (C&C) versus MWFRS split, combination with wind climate and directionality, internal pressure, the ASCE 7 limitation and DAF. | SKILL.md, reference.md |

## Quality and reporting (CWE Chapters 8–10)

| Skill | When to use | Files |
|---|---|---|
| [quality-assurance](skills/quality/quality-assurance/SKILL.md) | Use when auditing or planning the quality assurance of a CFD/LES wind load study; covers ASCE CWE Prestandard Chapter 8 and the Table 8-1 compliance matrix, verification/validation, the benchmark requirement, the mesh study (IRQ), time-step sensitivity and statistical convergence. | SKILL.md, reference.md |
| [report-and-peer-review](skills/quality/report-and-peer-review/SKILL.md) | Use when writing a CFD/LES wind load report, auditing an existing report for missing content, or planning an independent peer review; applies the ASCE CWE Prestandard Chapter 9 (report content, compliance matrix) and Chapter 10 (project peer review, basis of design, comment log, AHJ) requirements as a checklist. | SKILL.md, reference.md |

## Wind tunnel (ASCE/SEI 49-21)

| Skill | When to use | Files |
|---|---|---|
| [tunnel-approach-flow](skills/wind-tunnel/tunnel-approach-flow/SKILL.md) | Use when an atmospheric boundary layer (ABL) simulation in a wind tunnel has to be set up or checked against ASCE/SEI 49-21; covers the target mean velocity profile, turbulence intensity, integral length scale, power spectral density, roughness Reynolds number, reference velocity/height (Uref, zref), partial ABL and partial turbulence simulation (PTS), and the topographic model. | SKILL.md, reference.md |
| [tunnel-model-and-surroundings](skills/wind-tunnel/tunnel-model-and-surroundings/SKILL.md) | Use when asked about, or when checking in a tunnel report, the wind tunnel model's geometric scale, geometric detail and accuracy, the extent of the proximity model, the blockage ratio limit and correction, Reynolds number requirements, rounded structures and the wind direction increment according to ASCE/SEI 49-21. | SKILL.md, reference.md |
| [tunnel-other-measurements](skills/wind-tunnel/tunnel-other-measurements/SKILL.md) | Use when asked about wind tunnel measurements other than pressure taps according to ASCE/SEI 49-21; high-frequency force balance (HFFB), direct load measurement and rigid section model, dynamic response analysis of flexible structures, aeroelastic model (vortex shedding, galloping, flutter), product tests (products, solar arrays), snow load model studies, the tornado/downburst framework and the scope status of pedestrian wind. | SKILL.md, reference.md |
| [tunnel-pressure-measurement-and-loads](skills/wind-tunnel/tunnel-pressure-measurement-and-loads/SKILL.md) | Use when asked about, or when checking a tunnel report for, wind tunnel pressure measurement (pressure taps, tubing frequency response, sampling rate/duration), reference pressure and velocity, peak pressure estimation (Gumbel), area averaging/pressure integration, internal pressure, components and cladding (C&C) and MWFRS loads, combination with wind climate and directionality, measurement uncertainty, quality assurance and report content according to ASCE/SEI 49-21. | SKILL.md, reference.md |

## Helpers

| Skill | When to use | Files |
|---|---|---|
| [calc-tools](skills/helpers/calc-tools/SKILL.md) | Ready-made script for wind simulation checks; use when you need a target profile (log law, I_u), blockage ratios, cutoff frequency check, the empty domain 10 % check, or a peak value from a short record (Gumbel). | SKILL.md, wind_tools.py |

## Experience

| Skill | When to use | Files |
|---|---|---|
| [les-inflow-turbulence-tuning](skills/experience/les-inflow-turbulence-tuning/SKILL.md) | Use when synthetic inflow turbulence in LES misses the target in the empty domain, when turbulence decays before it reaches the building, or when the empty domain run has to be tuned repeatedly; mistakes made on one project and the sequence that worked. | SKILL.md |
