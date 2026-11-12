---
name: target-wind-definition
description: "Use when the wind climate model and the target wind flow conditions at the incident location are to be defined according to Chapter 3 of the ASCE CWE prestandard: storm types, mean wind speed profile, turbulence intensity, integral length scale, power spectral density, Reynolds stress, roughness length z0, exposure change and topography effect."
---

# Target wind definition (Chapter 3)

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 3 (Characterization of wind climate and wind flow conditions). Clause table and equation inventory: `reference.md`. Page numbers are PDF page order (printed page = PDF − 18).

## When to use

- Before an LES study, to answer "what do I have to match in the empty domain?": which profiles, which components, at which location.
- When a wind climate model is to be built for the site or an existing model is to be checked (data source, storm separation, directionality, range of return periods).
- When asked which storm type (extratropical storm, hurricane, thunderstorm, tornado, topographically influenced wind) has to be taken into account.
- When asked how the target is defined when there is a roughness change or a hill/mountain effect upstream.

Not for: numerical tolerances on how closely the target has to be matched in the simulation are not in Chapter 3; they belong to the approach flow simulation skill (Chapter 5).

## Basic idea

Chapter 3 requires two separate products:

1. **Wind climate model:** the probabilistic description of wind speed and direction at the site. It is combined afterwards with the aerodynamic data from the simulation (PO 3-1).
2. **Target wind flow conditions:** for every wind direction, the profile and turbulence properties to be achieved at the incident location of the computational domain (PO 3-2). They are matched in the simulation at the same location.

Incident location: the most upstream point in the domain where a building or topography is added (§1.8, §4.1). The target is defined here, not at the inlet boundary.

## Step by step

1. **Identify the weather systems affecting the site (§3.1).** All weather systems expected at the site are addressed according to the risk category: basic wind speeds and, where relevant, directional characteristics.
   - Extratropical storms: whatever the location and risk category (§3.1.1).
   - Hurricanes: every risk category in hurricane-prone regions (§3.1.2).
   - Thunderstorms: every risk category in the regions where they govern (§3.1.3).
   - Tornadoes: Risk Category III and IV in the tornado-prone region (§3.1.4).
   - Other topographically influenced winds (e.g. downslope winds): every risk category (§3.1.5).
   The regional examples in the document are specific to the USA; in another country find the equivalent from the local code and climate data, and do not attribute it to the document.
2. **Choose the data source of the wind climate model (§3.2, §3.2.1).** Options (those listed in the commentary): code basic speeds; long-term local/regional full-scale records; synthetic records from Monte Carlo simulation; reanalysis data; WRF modeling.
   - If measured records are used: a reliable station (e.g. conforming to World Meteorological Organization criteria) and a multidecadal record; a shorter period is justified and documented (AC 3-1a).
   - Storm types are separated; where necessary the records are corrected for exposure before the statistical analysis (§3.2.1).
   - In a hurricane-prone region local station speeds alone are not enough; Monte Carlo simulation is done with basin-scale hurricane tracks (AC 3-1b).
   - If reanalysis data are used, they are cross-validated against meteorological observations, especially for extreme events (AC 3-1c).
3. **Build the wind climate model (§3.2.2).** The model provides: the probabilistic combination of the relevant storm types; the whole range of return periods corresponding to the risk category of the building; the directionality of extreme events. It accounts for the site exposure before being combined with the simulation output.
4. **Characterize the upstream roughness (§3.3.1; PO 3-3 / AC 3-3).** The exposure(s) are established by determining the aerodynamic roughness length (z0) for each direction; the topography effect is considered where relevant. This assessment is used both in transferring the climate model to the site and in choosing the target parameters.
5. **Derive the target parameters direction by direction (§3.3.1; AC 3-2).** Five items:
   1. mean wind speed profile,
   2. turbulence intensity profile (the components needed for the loading mechanism),
   3. turbulence integral length scale profile (the components needed),
   4. power spectral densities of the velocity fluctuations (the components needed),
   5. the relevant cross-spectral densities and Reynolds stresses.
6. **Choose the appropriate boundary layer model.** For extratropical storms an atmospheric boundary layer model (§3.3.1.1); for hurricanes a hurricane boundary layer model (§3.3.1.2). The document does not make a particular model mandatory; it requires "an appropriate model". The options given in the commentary are in the table below.
7. **Account for exposure change.** If the roughness changes upstream, the methods mentioned in the commentary can be used for the non-equilibrium effects (table below). This is a recommendation, not mandatory.
8. **Address topography (§3.3.2; PO 3-4 / AC 3-4).** If topography can affect the site flow it is quantified by simulation:
   - If the topography is **outside** the domain in which the buildings are modeled explicitly: separate simulations are used to derive the wind characteristics that the main simulation has to reproduce ("Topography Method 1").
   - If complex three-dimensional topography is an **integral part** of the site (inside a gorge, steep slope): it is modeled explicitly as part of the study region and its effect is determined in the main simulation ("Topography Method 2").
9. **If non-synoptic winds are required (§3.3.3).** The document sets no mandatory criterion here; it says that a comprehensive definition of target parameters has not yet been resolved. The models in the commentary are for information only.
10. **Document.** The degree to which the target parameters are matched in the empty-domain simulation is documented and discussed in the technical report (§3.3.1).

## Which quantity from which source (all are options with commentary status)

| Quantity | Source / model mentioned in the document | Validity note (according to the document) | Equation |
|---|---|---|---|
| Mean velocity profile U(z), extratropical | Harris and Deaves (1979) | Neutral atmosphere, more than 30° from the equator, strong wind (mean speed at 10 m > ~10 m/s), flat and uniformly rough terrain. Below ~300 m the second- and higher-order terms, and below ~30 m also the first-order term, can be neglected. | 3-1 |
| Gradient height zg | Relation depending on friction velocity and Coriolis parameter | f = 2ω sinφ; ω = 7.27 × 10⁻⁵ rad/s | 3-2, 3-3 |
| von Kármán constant κ | — | Taken as 0.4 | explanation of 3-1 |
| Choice of z0 value | ASCE/SEI 49-21 | Guidance for choosing an appropriate value | — |
| Effect of roughness change on mean velocity | Deaves (1981a) | Non-equilibrium effects | — |
| Longitudinal turbulence standard deviation σu(z) | ESDU Item 83045 | Strong extratropical wind, flat and uniformly rough terrain | 3-4 – 3-6 |
| Longitudinal turbulence intensity Iu(z) | σu(z) / U(z) | — | 3-7 |
| Effect of roughness change on σu | Deaves (1981b) | Non-equilibrium effects | — |
| Lateral and vertical σv, σw (hence Iv, Iw) | ESDU Item 85020 | — | — |
| Longitudinal integral length scale Lu^x(z) | ESDU Item 85020 | Strong extratropical wind, flat and uniformly rough terrain | 3-8 – 3-12 |
| The other eight integral length scales | ESDU Item 86010 | High-frequency range | — |
| Longitudinal spectrum Suu(n, z) | ESDU Item 85020 | High-frequency range | 3-13 |
| Lateral spectrum Svv | Kaimal et al. (1972); alternative: Solari and Piccardo (2001) | — | — |
| Vertical spectrum Sww | Lumley and Panofsky (1964); alternative: Solari and Piccardo (2001) | — | — |
| Effect of roughness change on length scale and spectrum | ESDU Item 85020 | Non-equilibrium effects | — |
| Reynolds stress u′w′ | Integral of the co-spectrum over frequency | The most dominant component of the stress tensor | 3-14, 3-15 |
| Hurricane mean velocity profile | Logarithmic law in the lowest ~300–400 m; above that the Vickery et al. (2009) logarithmic-quadratic model | Over-ocean gradient height depends on the inertial stability parameter | 3-16 – 3-18 |
| Topography effect | Separate simulation (Method 1) or explicit modeling (Method 2); optional LiDAR comparison, WRF coupling | — | — |
| Climate model: basic speeds | ASCE/SEI 7-22 (non-directional basic speeds; separate tornado speeds) or, in compliance with §26.5.3, local records / Monte Carlo / reanalysis / WRF | Return periods for Risk Category I–IV are 300, 700, 1,700, 3,000 years | — |
| Extreme value analysis | Method of independent storms (Cook 1982; Harris 1999); in a mixed climate the storm types are assessed separately and combined (Gomes and Vickery 1978) | — | — |
| Joint speed-direction distribution | Two- or five-parameter Weibull; combination by the up-crossing method | The fit of the tail of the distribution is critical | — |

The explicit form of the equations came out corrupted in the plain-text source; do not write the coefficients from here or from memory, take them from the original PDF (pp. 36–38). Details: `reference.md`.

## Special care for tall buildings (§3.3.1.1 commentary)

For tall buildings it is particularly recommended that all of the following are characterized correctly in the empty-domain simulation: the mean velocity profile; turbulence intensity (especially longitudinal and lateral); integral length scales (especially Lu^z, Lv^z, Lu^y, Lv^y, Lv^x); spectra (especially longitudinal and lateral); the u′w′ Reynolds stress.

## Mandatory requirements

- §3.1: All weather systems expected at the site are addressed according to the risk category.
- §3.1.1–§3.1.5: scope by storm type (step 1 above).
- PO 3-1 (§3.2): The aerodynamic data are combined with a site-specific wind climate model.
- AC 3-1a (§3.2.1): Reliable station; multidecadal record, or a shorter period that is justified and documented.
- §3.2.1: Storm separation; exposure correction where necessary, before the statistics.
- AC 3-1b (§3.2.1): In a hurricane region local station data alone are prohibited; basin-scale Monte Carlo.
- AC 3-1c (§3.2.1): Reanalysis data are cross-validated against observation.
- §3.2.2: The climate model meets three conditions (probabilistic combination, whole range of return periods, directionality) and includes the site exposure.
- PO 3-2 (§3.3): The target conditions are derived direction by direction at the incident location and matched in the simulation at the same location.
- PO 3-3 / AC 3-3 (§3.3.1): The upstream z0 is characterized and the exposure is determined.
- AC 3-2 (§3.3.1): Five target parameters are determined; the degree of matching is documented in the report.
- §3.3.1.1 / §3.3.1.2: An appropriate atmospheric / hurricane boundary layer model is used.
- PO 3-4 / AC 3-4 (§3.3.2): The topography effect is quantified by simulation; Method 1 or Method 2 depending on its location.

## Common mistakes

- Defining the target at the inlet boundary. The target is at the incident location; the profile degrades from the inlet to that point.
- Settling for mean velocity and Iu only. AC 3-2 also requires the length scale, spectrum, cross-spectrum and Reynolds stress (for the components needed).
- Using a single profile and applying it to all directions. The derivation is done direction by direction.
- Presenting the Harris-Deaves / ESDU relations in the commentary as "mandatory". What is mandatory is to use "an appropriate model"; the relations are example options.
- Using the relations outside their conditions of validity (weak wind, latitude near the equator, non-uniform terrain).
- Attributing a numerical tolerance to Chapter 3 (e.g. "the profile must be within x%"). Chapter 3 has no such threshold.
- Doing an extreme value analysis in a hurricane region with airport station data alone.
- Fitting a single distribution without separating storm types; in a mixed climate the types should be assessed separately and combined (commentary).
- Overlooking the change over time of the roughness around the station and nearby obstructions (commentary).
- Glossing over complex topography inside the site with flat terrain + a separate simulation; in that case explicit modeling (Method 2) is required.
- In Method 1, not allowing for the fact that profiles containing reverse flow or speed-up/deficit at particular heights are hard to reproduce over flat terrain (commentary).
- Acting as if the document had an acceptance criterion for tornadoes or downbursts. §3.3.3 contains only discussion and commentary.

## Related skills

- `cwe-scope-and-process` — scope, choice of tool, two-step process, definition of the incident location.
- Approach flow simulation (Chapter 5) skill — matching the target in the empty domain and the acceptance criteria.
- Building aerodynamics simulation (Chapter 6) and load/response combination (Chapter 7 onward) skills — combining the climate model with the aerodynamic data.
