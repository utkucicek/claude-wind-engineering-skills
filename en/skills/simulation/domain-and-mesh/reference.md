# Reference: ASCE CWE Prestandard §6.2, §6.3, §6.4

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Page numbers are PDF page order. The summaries are written in our own sentences.

Type: MANDATORY = shall (or must), RECOMMENDED = should, COMMENTARY = commentary.

## Clauses

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §6.2 introduction | MANDATORY | The geometry can be modeled at full or reduced scale; the same scale factor is used in the approach flow and building simulations. | none | 59 |
| PO 6-2 | MANDATORY | The study building is modeled in enough detail to include all features that affect the aerodynamics with respect to wind loading. | none | 60 |
| AC 6-2a | MANDATORY | The geometric details important for external pressure coefficients (building shape, corner details, balconies, large facade features) are modeled explicitly. | none | 60 |
| AC 6-2b | MANDATORY | If internal pressure is determined directly from the simulation, the necessary detail of the internal volume and the openings is modeled; porosity (§6.2.5) and opening effects are represented correctly; at reduced scale the internal volume is scaled consistently, as in wind tunnel studies. | none | 60 |
| §6.2.1 commentary | COMMENTARY (contains a shall) | Internal pressures, including Helmholtz resonance where necessary, shall be taken into account when the load is determined; they can be obtained analytically from the simulated external pressures or directly from the simulation. The level of detail is sufficient to capture the flow phenomena that govern the quantities of interest and does not introduce unnecessary complexity. | none | 60 |
| PO 6-3 | MANDATORY | Nearby buildings and other structures that can affect the load on the study building are modeled explicitly. | none | 60 |
| AC 6-3 | MANDATORY | The report justifies the choice of the proximity model. | none | 60 |
| §6.2.2 commentary | COMMENTARY | The wind tunnel testing standard ASCE 49-21 suggests a common minimum value at full scale for the radius of the proximity model; a larger radius may be needed for very tall buildings. A similar approach can be followed in simulation. | 240 m (787 ft), full scale | 60 |
| PO 6-4 | MANDATORY | If the topography model is included in the proximity model (Figure 3-2, Method 2) it represents the local conditions at the site. | none | 60 |
| AC 6-4a | MANDATORY | Nearby topographic features that can affect the load are modeled explicitly (Figure 6-1f). | none | 60 |
| AC 6-4b | MANDATORY | The report justifies the choice of the topography model. | none | 60 |
| §6.2.3 commentary | COMMENTARY | The topography is smoothed down to zero height at the outlet boundary to prevent unwanted interaction with the boundary conditions. | none | 60 |
| PO 6-5 | MANDATORY | If the loads on appurtenances are to be determined, and if the scale requirements of this document allow it, the appurtenances are modeled directly on an appropriate model of the main structure. | none | 60 |
| AC 6-5a | MANDATORY | In a full-scale study the appurtenances are modeled together with the study building if the cell count allows adequate resolution for the appurtenances. | none | 60 |
| AC 6-5b | MANDATORY (permission) | If 6-5a cannot be met, the flow at the appurtenance location can be determined and the load obtained by reproducing this flow at a scale at which the load effects can be resolved adequately. | none | 60–61 |
| AC 6-5c | MANDATORY (must) | The reduced-scale simulation contains enough geometric detail for the flow separation and wake characteristics to represent full scale; the model shows a solution independent of Reynolds number. | none | 61 |
| AC 6-5d | MANDATORY | The report justifies the geometric scale and the details included in the simulation. | none | 61 |
| §6.2.4 commentary | COMMENTARY | Rooftop equipment, mechanical units, signs, chimneys, tanks and shading elements require care; if they are very small relative to the building, scaling becomes difficult, but modeling the building and the appurtenance together can give valid results. For Reynolds independence in the scaled model the geometry should contain particular surface details or roughness. | none | 61 |
| §6.2.5 introduction | MANDATORY | Porous components (perforated panel, screen, wire mesh, permeable double-skin facade) are represented either by the explicit geometry of all the detail or by a mathematical representation of the aerodynamic effect. This subsection gives requirements for the explicit representation. | none | 61 |
| PO 6-6 | MANDATORY | The explicit geometric details and numerical representations capture all relevant velocity and pressure fields near the component. | none | 61 |
| AC 6-6 | MANDATORY | If explicit modeling is chosen, all details related to porosity are included. If coarsened geometry is used, appropriate validation shows that the quantity of interest is represented correctly. The mesh resolution used inside and around the porous regions is shown. | none | 61 |
| §6.3 introduction | MANDATORY | The simulation of every wind direction required satisfies the domain requirements of this section. Dimensions: upwind and downwind streamwise lengths, width, height (Figure 6-1c). Two basic concerns: the model must be exposed to the correct target flow; it must not experience unwanted effects from the boundaries. | none | 61 |
| PO 6-7 | MANDATORY | The domain is defined such that the geometric model is exposed to the target flow having the target mean velocity, turbulence intensity and integral length scales defined in Chapter 3. | none | 61 |
| AC 6-7 | MANDATORY | The most upwind building or topographic feature of the study region is placed at the incident location where the §5.1 approach flow simulations showed that the target is represented correctly. The domain height is equal to that in the Chapter 5 simulations; the width and streamwise length are equal to those or larger. | Height = empty-domain height; width and length ≥ empty domain | 61 |
| PO 6-8 | MANDATORY | The domain dimensions are large enough that the flow around the model experiences no boundary or blockage effect. | none | 62 |
| AC 6-8a | MANDATORY | The distance between the inlet and the study region is sufficient for the upwind stagnation region to develop fully, independently of the inlet. The outlet is far enough from the most downwind building or topography that there is no artificial pressure build-up at the outlet and no interaction of the wake structures with the outlet. | No numerical distance given | 62 |
| AC 6-8b | MANDATORY | The frontal blockage ratio of the study region and other obstacles is limited by area and, separately, in the lateral and vertical directions. In the case with surrounding buildings (Figure 6-1e) the average height h_av is used instead of h_s; h_av and B_y are the average of the mean roof heights and the largest projected width of all explicitly modeled buildings. If there is topography it is included in the blockage calculation and h_s becomes the larger of the building height and the topography height (from the lowest foot to the highest peak). | BR < 3% (area); lateral and vertical < 17% (Equations 6-1, 6-2 are written with "≤") | 62 |
| §6.3 commentary | COMMENTARY / RECOMMENDED | The upwind length should be sufficient for flow development and for the inlet effect not to reach the region; the downwind length should prevent wake–outlet interference (pressure wave reflection, backflow); the width should contain the body-induced structures and prevent artificial confinement; the height should represent the relevant part of the boundary layer. The blockage limits are there to prevent artificial flow acceleration and confinement. For domain examples reference is made to low-rise, high-rise and urban-scale studies. | ≤ 3% frontal, ≤ 17% lateral/vertical | 63 |
| PO 6-9 | MANDATORY | The mesh is of acceptable quality and has the resolution to model the smallest scales of interest in the different regions of the domain (Figure 6-1c). | none | 63 |
| AC 6-9a | MANDATORY | In the approach flow region the resolution is the same as in the approach flow region of the §5.1.1.2 empty-domain simulations. | Same resolution | 63 |
| AC 6-9b | MANDATORY | In the near flow region the resolution is the same as in the approach flow region or finer. | ≤ approach flow region cell size | 63 |
| AC 6-9c | MANDATORY | In the local flow region the mesh is refined further to resolve the body-induced flow structures; different levels can be used according to proximity to the building. The finest resolution is near the building wall; the transition between levels is gradual. | No numerical growth ratio given | 63 |
| AC 6-9d | MANDATORY (permission) | In the far flow region the mesh may be coarsened to a reasonable extent that does not affect the flow in the regions of interest. | none | 63 |
| AC 6-9e | MANDATORY | The mesh topology, region resolutions, transition between resolutions and other basic quality metrics are reported. The adequacy of the mesh is determined by analysis of the pressure and velocity spectra and by a mesh dependency analysis; the IRQ is shown at the key monitoring points in the flow. The calculation method is in §6.6.4. | IRQ = 75% (AC 6-15a says "at least 75%") | 63 |
| §6.4 commentary (flow structures) | COMMENTARY / RECOMMENDED | Structures relevant to the load: separated shear layers, reattaching separation bubbles, wake vortices, conical vortices. For C&C loads the small eddies near the surface should be resolved. The ideal topology is close to isotropic; cells with a high aspect ratio should be avoided; transitions should be gradual, especially near the surface; skewness and nonorthogonality should be checked. | No numerical limit given | 63–64 |
| AC 6-9f | MANDATORY | For porous components modeled with explicit geometry, the mesh in the porous region is fine enough to discretize the internal volumes meaningfully. | none | 64 |
| AC 6-9f commentary | COMMENTARY / RECOMMENDED | Sufficient refinement to resolve holes, openings, wires and edges; near a solid surface either the viscous boundary layer should be resolved or an appropriate wall function used; the change of resolution away from the wall should be smooth; refinement should be maintained in the near and intermediate wake regions. | none | 64 |

## Equations (plain text)

| Equation | Status | Content | PDF page |
|---|---|---|---|
| (6-1) | Typesetting corrupted; structure readable | BR = (B_y · h_s) / (l_CD,y · l_CD,z) ≤ 3% | 62 |
| (6-2) | Typesetting corrupted; structure readable | BR_y = B_y / l_CD,y ≤ 17% and BR_z = h_s / l_CD,z ≤ 17% | 62 |

Note: In the case with surrounding buildings h_av replaces h_s in these equations (AC 6-8b).

## Definitions (§1.8, §1.9)

| Term | Summary | PDF page |
|---|---|---|
| Blockage ratio | The ratio of the projected area of the test model and the proximity models, in the plane normal to the flow axis, to the cross-sectional area. | 24 |
| Radius of proximity | The radius of the circle centered on the study building; explicit geometric features outside it have no direct interference effect on the aerodynamics of the study region. | 25 |
| Study building | The building or structure of primary interest in the wind effect analysis; surrounding buildings and terrain excluded. | 25 |
| Study region | The box enclosing the study building, its explicitly modeled surroundings and nearby topography; does not include the approach flow region. | 25 |
| Local flow region | The mesh region that encloses the study building and its vicinity and captures structures such as impingement, separated shear layers, separation bubbles and the wake. | 25 |
| Meshing region | §1.8 lists four types: approach flow, local flow, near-wall, background. (The text of §6.4 also speaks of "near flow" and "far flow" regions; their definition was not found in §1.8, see Figure 6-1c.) | 25 |
| h_av, h_s, B_y | See the §1.9 list of symbols. | 26 |

## Not found in the text

- Numerical multiples, in terms of building height, for the upwind, downwind, lateral and vertical domain dimensions.
- A mandatory radius for the proximity model (240 m is in the commentary only).
- Numerical limits for cell growth ratio, aspect ratio, skewness.
- A numerical recommendation for the cell size on the building surface (for example "H/how many").
