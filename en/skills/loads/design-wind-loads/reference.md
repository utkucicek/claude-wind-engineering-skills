# Reference — Chapter 7: Calculation of design wind loads

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Chapter 7.
"PDF page" = PDF sequence number (printed page = PDF − 18).
Type: MANDATORY = "shall", RECOMMENDED = "should / recommended", COMMENTARY = "Commentary" paragraph or explanatory text.
The summaries are written in our own words; what is binding is the document's own text.

## 7.0–7.2 General requirements and wind climate

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §7 introduction | COMMENTARY | Structures are classified as rigid, flexible or aeroelastic. The document defines no frequency-based limit; the ASCE/SEI 7-22 limit is a good indicator but does not cover every structure type. Final acceptance of the loads depends on completion of the documentation and the peer review. | none | 69 |
| PO 7-1 (§7.1.1) | MANDATORY | The number of directions and/or wind conditions considered must be sufficient to define the loads on the structure and to capture the directions/effects critical for design. | none | 69 |
| AC 7-1 | MANDATORY | Simulations are performed with a limited azimuth increment; if the results indicate the possibility of a larger design load, additional directions are considered. | increment ≤ 10° | 69 |
| §7.1.1 commentary | COMMENTARY | The number of directions may be reduced subject to sufficient justification and approval of the peer review team and the AHJ. | none | 69 |
| PO 7-2 (§7.1.2) | MANDATORY | A suitable reference wind speed is determined. | none | 69 |
| AC 7-2 | MANDATORY | The reference velocity is monitored and documented at a location that minimizes the influence of the proximity model on the sampled data. | none | 69 |
| §7.1.2 commentary | COMMENTARY / RECOMMENDED | Typical sampling: (1) for most tall buildings, a height considered to be outside the boundary layer, or (2) at structure height, upwind of the explicitly modeled surroundings. For some structures a characteristic height (roof, eave) is used; conversion to another height should be documented in detail. | none | 70 |
| PO 7-3 (§7.1.3) | MANDATORY | The design load is determined without relying on future changes of the surroundings (e.g. demolition of neighboring buildings). | none | 70 |
| AC 7-3a | MANDATORY | The MWFRS and C&C loads found by CWE are limited according to the methods of ASCE/SEI 7-22 (latest edition). Table 8-1 calls this criterion the "minimum load requirement for the unsheltered case". | no ratio/percentage in the Chapter 7 text (reference to ASCE 7) | 70; Table 8-1: 87 |
| AC 7-3b | MANDATORY | The statistically steady aerodynamic force/moment coefficients are checked to confirm that any load reduction is consistent with the results expected for the building type and shape. | none | 70 |
| §7.1.3 commentary | COMMENTARY | Comparison of the CWE loads with the ASCE/SEI 7-22 loads is encouraged to the extent relevant to the project. | none | 70 |
| PO 7-4 (§7.2) | MANDATORY | The CWE data are combined with wind climate data. | none | 70 |
| AC 7-4a | MANDATORY | One of the following statistical methods is used: upper bound (nondirectional), normalized sector, multisector, up-crossing, storm passage, direct simulation. | 6 methods | 70 |
| AC 7-4b | MANDATORY | All weather systems that contribute to the site-specific climate are taken into account (Chapter 3). The assumptions in the climate analysis and the combination methods are documented in detail. | none | 70 |
| §7.2 commentary — general | COMMENTARY / RECOMMENDED | There is no explicit relation between the R-year speed and the R-year effect; the effect should be found per storm type and then combined. A relation combining the return periods for three storm types (thunderstorm, extratropical, tropical cyclone) is given; directional speed data sets are required. | Eq. 7-1: equation could not be read in the text | 70–71 |
| §7.2 commentary — upper bound | COMMENTARY | The simplest and most conservative method; directionality is ignored. The design speed with return period R is inserted into the largest response function over all directions. It can be used with ASCE/SEI 7-22 speeds without a climate analysis; when the code speed is used, no distinction by storm type is needed. | none | 71 |
| §7.2 commentary — normalized sector | COMMENTARY | Each sector is assigned a design speed scaled by the ratio of that sector's R-year speed to the largest R-year speed over all sectors; the design response is the largest over the sectors. Mostly conservative, rarely unconservative. Requires a directional combined climate model; the assumptions made for coarse directional resolution should be written in the report. | Eqs. 7-2 and 7-3: partly readable, to be verified against the PDF | 71 |
| §7.2 commentary — multisector | COMMENTARY | The response–annual exceedance probability is computed for each direction sector; the sector return periods are combined with a product relation. Independence of the extreme winds in the sectors is assumed; applied separately for thunderstorms and extratropical storms. Its limitation: it ignores the contribution of weaker winds coming from directions other than the direction of the storm maximum. | Eq. 7-4: equation could not be read in the text | 71–72 |
| §7.2 commentary — up-crossing | COMMENTARY | Based on the parent distribution of all observed/simulated winds (usually two-parameter Weibull; five-parameter has also been used). The parameters depend on direction. Current practice does not separate thunderstorms. It can also be used with tropical cyclone simulation results. | none | 72 |
| §7.2 commentary — storm passage | COMMENTARY | The largest response is found from the speed–direction time series of each simulated tropical cyclone. The directional resolution is limited by that of the CWE data. With a sufficient number of simulations an empirical distribution can be used instead of a parametric distribution. | CWE directional resolution typically ≤ 10°; Eq. 7-5: equation could not be read in the text | 72 |
| §7.2 commentary — direct simulation | COMMENTARY | The directional data are fitted to an extreme value distribution for each direction segment; if data are scarce, neighboring segments may be merged; a large data set is generated by Monte Carlo; the load/response is computed from each event. Return period by Eq. 7-5 (λ: mean number of storms per year). | none | 72–73 |

## 7.3 Main wind force resisting system (MWFRS)

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §7.3 introduction | MANDATORY | Full-scale design loads are obtained by analytically combining the CWE data collected on an infinitely rigid model with the structural properties of the structure. All systems are assumed flexible. A method suitable only for a rigid structure is used only if sound technical justification is documented in detail. | none | 73 |
| PO 7-5 (§7.3.1) | MANDATORY | The MWFRS aerodynamic response is found by integrating the local surface forces acting on each boundary element face. | none | 73 |
| AC 7-5a | MANDATORY | The integration is performed directly during the run over predefined tributary areas (whole building, building segment, single story). It includes the pressure and viscous contributions; adding the viscous force is not a strict requirement (its contribution is generally small). | none | 73 |
| AC 7-5b | MANDATORY (permission + requirement) | Calculation of loads and dynamic effects by integrating surface pressure time series at multiple discrete points is permitted. The monitoring point distribution must be sufficient to capture the desired load effects correctly. | none | 73 |
| AC 7-5c | MANDATORY | Special care is taken when porous building elements are modeled with the porous media approach; the forces acting on the porous media are included in the total load. | none | 73 |
| §7.3.1 commentary — direct integration | COMMENTARY | Approaches similar to the high-frequency force balance (HFFB) have assumptions (simple mode shapes, deviation from linearity, coupling between degrees of freedom). In CWE, story-by-story loads and moments can be found directly. If a numerical method similar to the force balance is adopted, special care is needed regarding mode shape, coupling and torsion estimation (ASCE/SEI 49-21). | none | 73 |
| §7.3.1 commentary — pressure integration | COMMENTARY / RECOMMENDED | The success of the method depends on the location and density of the monitoring points; circumferential coverage ("rings") and the vertical spacing of the rings are important. The roof heights of neighboring buildings may affect the location of the lowest ring. In CWE the point density should be at least consistent with wind tunnel practice and should increase for complex geometry. If the local code gives a minimum density, that is also satisfied. | AWES-QAM-1 recommendation: ≥ 1 point per 120 m² (~1,300 ft²) of surface at full scale | 74 |
| PO 7-6 (§7.3.2) | MANDATORY (permission) | Calculation of loads and structural effects by a frequency or time domain method is permitted. | none | 74 |
| AC 7-6 | MANDATORY | In every case the dynamic amplification factor (DAF) is reported together with the results. | none | 74 |
| §7.3.2 commentary | COMMENTARY / RECOMMENDED | Frequency domain: the mean + background + resonant components are combined. Time domain: the generalized equation of motion is solved step by step; the sample duration is a critical choice, and longer-duration samples should be used to be able to assess record-to-record variability. | none (no number given for the duration) | 74 |
| PO 7-7 (§7.3.3) | MANDATORY | Peak wind loads and wind-induced structural effects are presented. | none | 75 |
| AC 7-7 | MANDATORY (permission) | Either equivalent static wind loads or aerodynamic force/pressure time series to be applied directly to the structural model are accepted. | none | 75 |
| §7.3.3 commentary | COMMENTARY | Equivalent static loads cover the mean, background and resonant effects (e.g. story-by-story loading). With time series, member internal forces, demand/capacity ratios, story drift and accelerations can be computed directly. | none | 75 |

## 7.4 Components and cladding (C&C)

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 7-8 (§7.4.1) | MANDATORY | C&C wind effects are determined from pressure data sampled from the CWE; a suitable allowance is made for internal pressure. | none | 75 |
| AC 7-8 | MANDATORY; density part RECOMMENDED | The monitoring point distribution must be sufficient to capture the load effects correctly; locations are selected carefully according to the complexity of the external geometry and the surface pressure gradient. Higher density is recommended for small buildings and in high-gradient regions (roof corners, edges, ridges, wall edges). | none | 75 |
| PO 7-9 (§7.4.2) | MANDATORY (permission + requirement) | Direct load calculation by the integral method is permitted for the mean and time-varying effects on C&C. Care is taken to consider the appropriate internal pressures. | none | 75 |
| AC 7-9 | MANDATORY | The size and distribution of the tributary areas used in the force integration are consistent with the monitoring point placement principles; sufficient spatial resolution is provided, especially in regions where large pressure gradients are expected. | none (no area size given) | 75–76 |
| PO 7-10 (§7.4.3) | MANDATORY | Peak design loads are determined using an extreme value distribution for durations and probability levels suitable for combination with the wind climate data. | none | 76 |
| AC 7-10a | MANDATORY | The probability of exceedance from the extreme value statistical analysis is reported. | none (no target probability given) | 76 |
| AC 7-10b | MANDATORY | No filter that eliminates frequencies that may be related to aerodynamic phenomena is applied to the simulation data. | none | 76 |
| §7.4.3 commentary — single peak | COMMENTARY (with "shall not" wording in the text) | Single observed peak coefficients are not used: their repeatability is poor and they depend on the test duration. A suitable statistical method increases repeatability and allows the probability of non-exceedance to be calculated. | none | 76 |
| §7.4.3 commentary — methods | COMMENTARY | Two common methods: (1) ensemble average — the average of the extreme values of equal-length segments, scaled to represent a suitable full-scale observation duration; (2) Gumbel fitting — the peak at a specified fractile level from the segment extreme values. Others: method of independent storms, BLUE, peak-over-threshold. Cook–Mayne gives the most accurate result but requires the extreme wind climate; it is not suitable for generic coefficients of products to be installed in different climates. | observation duration example: 10 min – 1 h; number of segments and fractile level: not found in the text | 76 |
| §7.4.3 commentary — glass | COMMENTARY / RECOMMENDED | In some cases a single peak value is not the appropriate output; e.g. glass damage is cumulative (Brown integral) and the integral should be applied both to the CWE data and to the test result. | none | 76 |
| PO 7-11 / AC 7-11 (§7.4.4) | MANDATORY | The net pressure coefficients of an appurtenance are determined by direct derivation of the net pressures. | none | 76 |
| §7.4.4 text/commentary | COMMENTARY | Pressure normal to the surface is the dominant effect; positive pressure acts toward the surface, negative (suction) outward. Net pressure is the combination of the pressures on the two faces of a body, or of the external + internal pressure. | none | 76 |
| PO 7-12 (§7.4.5) | MANDATORY | Internal pressures are either estimated analytically from the simulated external pressures or determined directly in the CWE simulation. | none | 77 |
| AC 7-12a | MANDATORY | When estimating the mean and time-varying internal pressure, the effect of porosity, leakage and openings is considered for possible scenarios. Net pressures based on simulated internal pressure are computed with the integral monitoring approach. | none | 77 |
| AC 7-12b | MANDATORY | If the time-varying internal pressure is resolved directly and the simulation is not at full scale, internal volume scaling is required. Deviations that give conservative net pressures are permitted but are documented in the report. | none | 77 |
| AC 7-12c | MANDATORY | Cavity pressures in other partially enclosed volumes (beneath loose-laid roofing and ballast pavers, behind ventilated facade panels, beneath low-profile rooftop solar panel systems) are considered if they could change the pressure on the surfaces behind the porous material; the size, location and/or permeability of the openings to these volumes are mapped carefully. | none | 77 |
| §7.4.5 commentary | COMMENTARY / RECOMMENDED | What determines the internal pressure: external pressure distribution, leakage paths, openings, enclosed air volume, flexibility of the envelope. Large openings should be derived directly or computed from the CWE. Flow paths to be considered in an analytical assessment: ventilation inlets/outlets, internal partitions and connections between stories, large openings that may be left open, envelope damage that the wind may cause. If the calculation is not practical, use of the ASCE/SEI 7-22 or AS/NZS 1170.2 internal pressures is recommended. In partially enclosed volumes internal volume scaling may conservatively be neglected; Reynolds similarity is not required for orifice flow; full-scale simulation is recommended for systems with narrow/uncertain leakage paths. | none | 77–78 |
| PO 7-13 / AC 7-13 (§7.4.6) | MANDATORY | The mean, standard deviation and peak (minimum, maximum) external pressure coefficients are evaluated. All four coefficients are defined by dividing the relevant pressure by the reference dynamic pressure; q_ref = ½·ρ·U_ref². The peak pressure may be instantaneous or statistical. | Eq. 7-6: text extraction corrupted, structure readable; to be verified against the PDF | 78 |

## 7.5–7.7 Appurtenances, quality check, non-synoptic events

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| PO 7-14 (§7.5.1) | MANDATORY | The loads on appurtenances are derived from the same computational model from which the design loads of the main structure are obtained. | none | 78 |
| AC 7-14a | MANDATORY | The loads are found either by direct load calculation (integral method) or by pressure integration (§7.3.1). | none | 78 |
| AC 7-14b | MANDATORY (rigid) / permission (flexible) | For rigid appurtenances the peak design load is found with a statistical approach consistent with §7.4.3. For flexible appurtenances the methods of §7.3.2 are permitted for the DAF. | none | 78 |
| §7.5.1 commentary | COMMENTARY | The AHJ may want an appurtenance to fail at a lower speed than the main structure (like a fuse); mostly the same risk category as the main structure is expected. Examples: sunshades, decorative fins, balconies, canopies, rooftop equipment, parapets. The document does not explicitly address generic product installations; the methods can be applied with adaptation (additional guidance: ASCE/SEI 49-21). | none | 78–79 |
| PO 7-15 / AC 7-15 (§7.5.2) | MANDATORY | The product test report additionally contains: (1) the simulated loads and the effective wind area relation — for rooftop solar panels versus normalized effective wind area, for other products its necessity is assessed; (2) conversion of the data to aerodynamic coefficients; (3) the conditions of applicability of the results. | 3 items | 79 |
| PO 7-16 / AC 7-16 (§7.6) | MANDATORY | The integrated forces and moments on the building are plotted about a reference point (usually the tower base or the structural origin); for each component, mean, minimum, maximum versus direction. The spectral response is plotted for the critical directions. | none | 79 |
| §7.6 commentary | RECOMMENDED | It is recommended that the results obtained with the other meshes in the mesh study also be added to these plots (directly or as a band of values). | none | 79 |
| §7.7 | COMMENTARY (scope) | The document gives no explicit design load method for non-synoptic events such as tornadoes. | none | 79 |
| §7.7 commentary | COMMENTARY | There is as yet no published method consistent with the design standards. ASCE/SEI 7-22 §32.18 permits the use of boundary layer tunnel coefficients with restrictions (isolated building, Exposure C open terrain); the synoptic methods of this Prestandard can be used to produce the base coefficients, after which the KvT correction is applied (ASCE/SEI 7-22 §32.14). | none | 79–80 |

## Cross-references from Chapter 6 used in this skill

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| AC 6-13d (§6.6.2.2) | MANDATORY | The report justifies the choice of data sampling resolution. | none | 66 |
| PO 6-14 (§6.6.3) | MANDATORY | It is shown that the mean and standard deviation of the velocity at key monitoring points, and the estimates of the mean, standard deviation and peak values of the load quantities of interest, have converged. | none | 66 |
| AC 6-14 | MANDATORY | The simulation duration is longer than a specified multiple of the longitudinal integral time scale at the target building height. | > 500 longitudinal integral time scales | 66 |
| §6.6.3 commentary | COMMENTARY | Required duration = spin-up + averaging duration; it is problem dependent. Whether the peak values are captured correctly can be assessed with the block maxima or the peak-over-threshold approach. | none | 66 |

## Unreadable / missing items

- Eq. 7-1 (combination of storm types), 7-4 (multisector), 7-5 (storm passage): equation could not be read in the text.
- Eqs. 7-2, 7-3 (normalized sector) and 7-6 (pressure coefficients): partly readable; the structure is given in words above, the symbols are to be verified against the PDF.
- Numerical area for cladding area averaging, Gumbel fractile level, number of segments, ASCE 7 lower-limit percentage, an uncertainty clause specific to Chapter 7: not found in the text.

## Count

Chapter 7: 16 PO (7-1 … 7-16) and 24 AC (7-1, 7-2, 7-3a/b, 7-4a/b, 7-5a/b/c, 7-6, 7-7, 7-8, 7-9, 7-10a/b, 7-11, 7-12a/b/c, 7-13, 7-14a/b, 7-15, 7-16) — 40 clauses in total, all of them above.
