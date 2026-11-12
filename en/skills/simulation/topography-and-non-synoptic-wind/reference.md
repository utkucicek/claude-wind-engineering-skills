# Reference: ASCE CWE Prestandard §5.2 and §5.3

Source: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Page numbers are PDF page order. The summaries are written in our own sentences.

Type: MANDATORY = shall, RECOMMENDED = should, COMMENTARY = commentary.

## Clauses

| Clause | Type | Summary | Numerical criterion | PDF page |
|---|---|---|---|---|
| §5.2 introduction | Framework | If the topography is represented without being placed in the building simulation (Figure 3-2, Method 1), the target flow is taken from a separate topography simulation. The document does not describe the method of that topography simulation. | none | 53 |
| PO 5-6 | MANDATORY | The target profiles taken from the topography simulation are reproduced at the incident location in an empty-domain simulation that does not contain the explicit geometric model of the topography. | none | 53 |
| AC 5-6 (documentation) | MANDATORY | The computational domain size, the mesh resolution and all boundary conditions used are documented. | none | 53 |
| AC 5-6 (statistics) | MANDATORY | The full turbulence statistics (mean, rms, length scales, spectra) of the three velocity components and the pressure are reported at different heights at the incident location. | 3 velocity components; number of heights not given | 53 |
| AC 5-6 (contours) | MANDATORY | The mean and standard deviation velocity and pressure fields are plotted in horizontal planes and in streamwise/wall-normal planes; the development of the flow within the domain is seen and it is verified that there is no unrealistic change in the profiles. | none | 53 |
| AC 5-6 (target) | MANDATORY | The target field predicted by the topography simulation is produced correctly at the incident location in terms of the basic velocity statistics relevant to the application. | No number here; the numerical limits are in AC 5-9 (for Method 1 the range is 100% of h_max) | 53; 57 |
| AC 5-6 (directions) | MANDATORY | Since the topography effect depends on direction, the analysis is done for all relevant wind directions. | Number of directions not given | 53 |
| §5.2 commentary | COMMENTARY | If the target field is imposed directly at the inlet of the domain without topography, the flow evolves back to the flat-terrain equilibrium boundary layer. The difference in equations and numerical methods between the topography simulation and the subsequent simulations can lead to unrealistic profile change within a short distance near the inlet; this is often seen with mesoscale weather forecast models (energy and moisture conservation, coarse mesh). Great care is needed. | none | 53 |
| §5.3 main text | Informative (no mandatory clause) | Methods have been developed for transient winds, but problems such as the definition of comprehensive target flow parameters, and the large parameter set arising from the variability of the flow and the position of the building within the flow, have not been resolved. There is no mature, industry-ready approach; for this reason explicit simulation of non-synoptic wind is not expected when this Prestandard is applied (§1.5.1). Thunderstorm and tornado profiles are nevertheless discussed in the commentary. | none | 53–54 |
| §5.3 commentary (general) | COMMENTARY | Ground roughness can be included with explicit elements or with wall functions; most studies have used a smooth ground. Representing particular flow features (acceleration, angle of attack, streamline curvature) instead of modeling the full field is a suggested alternative; it is an active research topic. | none | 54 |
| §5.3 commentary (downburst) | COMMENTARY | Two classes: (1) models that mimic experimental rigs; (2) models that include the cooling source terms that create the storm. In the mimicking setup a stationary, moving or pulsed impinging jet is used; the size and momentum of the jet determine the outflow (Figure 5-3). Alternative: a louver array upwind; the louver shape, tilt angle, opening time and the overpressure upstream are decisive. With the cooling source term the intensity, size and travel speed determine the flow near the ground. Weather forecast models can also be used; the initial and boundary conditions govern the evolution of the flow. | none | 54 |
| §5.3 commentary (tornado) | COMMENTARY | Two routes: (1) tornado-like vortex mimicking experimental rigs; (2) simulation that includes the dominant forcing mechanisms. The mimicking setup (Figure 5-4) produces the three velocity components, tangential, radial and axial, and three regions (boundary layer inflow, corner flow, upper flow); the corner flow is particularly important because of the high speed and pressure deficit. The vortex properties are determined by the inflow radius r0, the inflow depth h0 and the tangential/radial inflow velocity conditions. Alternative: an actuated vertical louver array (angular velocity, position, overpressure decisive). | none | 55 |

## Equations

There are no numbered equations in these two subsections.

## Not found in the text

- A method, mesh or acceptance criterion for the topography simulation itself.
- A separate numerical tolerance for AC 5-6 (the numbers come from AC 5-9).
- Any PO/AC, target profile or acceptance limit for non-synoptic wind.
