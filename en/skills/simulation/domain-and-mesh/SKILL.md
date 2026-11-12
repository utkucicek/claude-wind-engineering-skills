---
name: domain-and-mesh
description: Use when setting up or checking the geometry model (study building, proximity model, radius of proximity, topography, appurtenances, porous components), the computational domain size (blockage ratio) and the mesh (mesh regions, refinement, IRQ) for a building aerodynamics simulation; gives the requirements of Sections 6.2, 6.3 and 6.4 of the ASCE CWE Prestandard.
---

# Computational domain and mesh (ASCE CWE Prestandard §6.2, §6.3, §6.4)

Source: PDF pages 59–64. The clause table and equations are in `reference.md`.

## When to use

- When deciding in what detail the study building and its surroundings are to be modeled.
- When asked how much of the surrounding buildings is to be modeled explicitly (proximity model).
- When computing the dimensions of the computational domain (CD) and the blockage ratio (BR).
- When choosing the mesh regions (approach flow, near flow, local flow, far flow) and the refinement levels.
- When appurtenances such as rooftop equipment, or porous components, are to be modeled.

## Key definitions

- **Study region:** The box enclosing the study building, its explicitly modeled surroundings and nearby topography; does not include the approach flow region (§1.8, p. 25).
- **Radius of proximity:** Circle centered on the study building; explicit geometry outside it has no direct interference effect on the aerodynamics of the study region (§1.8, p. 25).
- **h_s:** The larger of the study building height h and the average height of the surrounding buildings (§1.9, p. 26).
- **h_av:** Average of the mean roof heights of all explicitly modeled buildings (§1.9, p. 26).
- **B_y:** Largest transverse width of the streamwise projection of the explicitly modeled buildings, structures and topography (§1.9, p. 26).
- **l_CD,xu, l_CD,xd, l_CD,y, l_CD,z:** Upwind and downwind streamwise lengths, width and height of the domain (Figure 6-1c).

## Step by step

1. **Fix the scale (§6.2).** The geometry can be at full or reduced scale; the same scale factor is used in the approach flow and building simulations.
2. **Model the study building (PO 6-2).**
   - For external pressure: the building shape, corner details, balconies and large facade features are modeled explicitly (AC 6-2a).
   - If internal pressure is to be taken directly from the simulation: the necessary detail of the internal volume and the openings is modeled, and the effect of porosity and openings is represented correctly; at reduced scale the internal volume is scaled consistently (AC 6-2b).
   - The level of detail shall be sufficient to capture the flow phenomena that govern the quantities of interest, without introducing unnecessary complexity.
3. **Choose and justify the proximity model (PO 6-3 / AC 6-3).** Nearby buildings and structures that can affect the load are modeled explicitly; the choice is justified in the report. The document gives no mandatory radius; the commentary mentions the common minimum radius of 240 m (787 ft) at full scale from the wind tunnel standard (ASCE 49-21) and says that a larger one may be needed for very tall buildings.
4. **Topography (PO 6-4).** If topography is placed in the proximity model (Method 2) it represents the local conditions; nearby features that can affect the load are modeled explicitly (AC 6-4a) and the choice is justified (AC 6-4b). Commentary: the topography is smoothed down to zero height at the outlet boundary.
5. **Appurtenances (PO 6-5).** Appurtenances whose loads are required are modeled directly on an appropriate model of the main structure. If at full scale the cell count allows adequate resolution, together with the building (AC 6-5a); if not, the flow at the appurtenance location can be determined and reproduced at a more suitable scale to obtain the load (AC 6-5b). At reduced scale a solution independent of Reynolds number is demonstrated (AC 6-5c); the scale and the detail are justified (AC 6-5d).
6. **Porous components (PO 6-6 / AC 6-6).** Either all the detail is modeled explicitly or the aerodynamic effect is represented mathematically. If coarsened geometry is used, it is shown by validation that the quantity of interest is represented correctly; the mesh resolution inside and around the porous region is shown.
7. **Place the building at the incident location (PO 6-7 / AC 6-7).** The most upwind building or topographic feature of the study region is placed at the incident location where the empty-domain simulation matched the target. The domain height is equal to that of the empty-domain simulation; the width and streamwise length are equal to it or larger.
8. **Check boundary and blockage effects (PO 6-8).**
   - Streamwise (AC 6-8a): the inlet far enough away for the upwind stagnation region to develop fully, independently of the inlet; the outlet far enough away that there is no artificial pressure build-up and no wake–outlet interaction. No numerical multiple is given.
   - Blockage (AC 6-8b): BR = (B_y · h_s) / (l_CD,y · l_CD,z) ≤ 3%; BR_y = B_y / l_CD,y ≤ 17%; BR_z = h_s / l_CD,z ≤ 17%.
   - In the case with surrounding buildings h_av is used instead of h_s; if there is topography it is included in the blockage calculation and h_s becomes the larger of the building height and the topography height (from the lowest foot to the highest peak).
   - These requirements are satisfied for every wind direction required (§6.3).
9. **Set up the mesh regions (PO 6-9).**
   - Approach flow region: the same resolution as in the empty-domain simulation (AC 6-9a).
   - Near flow region: the same as the approach flow region or finer (AC 6-9b).
   - Local flow region: finer, so as to resolve the body-induced flow structures; graded according to proximity to the building; the finest mesh near the building wall; gradual transition between levels (AC 6-9c).
   - Far flow region: may be coarsened to an extent that does not affect the flow in the regions of interest (AC 6-9d).
   - For a porous component with explicit geometry the internal volumes are discretized meaningfully (AC 6-9f).
10. **Document the mesh and show its adequacy (AC 6-9e).** The topology, region resolutions, transitions and quality metrics are reported. Adequacy is shown by pressure and velocity spectra and by a mesh dependency analysis; at the monitoring points the index of resolution quality (IRQ) shall be 75%. For the IRQ calculation see `boundary-conditions-and-quality` (§6.6.4).

## Mandatory requirements

- **§6.2** — The same scale factor in the approach flow and building simulations.
- **PO 6-2 / AC 6-2a, 6-2b** — Building detail; for external pressure the shape, corners, balconies, large facade features; for internal pressure the internal volume and openings.
- **PO 6-3 / AC 6-3** — Nearby buildings that can have an effect are modeled explicitly; the choice is justified.
- **PO 6-4 / AC 6-4a, 6-4b** — Topography in the proximity model represents the local conditions; the choice is justified.
- **PO 6-5 / AC 6-5a–d** — Appurtenances; Reynolds independence; justification of scale and detail.
- **PO 6-6 / AC 6-6** — Porous components; validation for coarsening; demonstration of the mesh.
- **PO 6-7 / AC 6-7** — The most upwind building/topography at the incident location; domain height equal to the empty domain; width and length equal or larger.
- **PO 6-8 / AC 6-8a, 6-8b** — No boundary and blockage effect; BR ≤ 3%, BR_y ≤ 17%, BR_z ≤ 17% (Equations 6-1, 6-2).
- **PO 6-9 / AC 6-9a–f** — Mesh quality and region resolutions; IRQ 75%.

## Checklist

- [ ] Are the empty-domain and building simulations at the same geometric scale?
- [ ] Are the building shape, corner details, balconies and large facade features in the model?
- [ ] If internal pressure is taken from the simulation, were the internal volume and the openings modeled?
- [ ] Was the extent of the proximity model justified in the report?
- [ ] If topography was placed in the model, was the choice justified?
- [ ] Does the most upwind building or topographic feature stand at the incident location verified in the empty domain?
- [ ] Is the domain height the same as in the empty-domain simulation?
- [ ] Are the domain width and length not smaller than in the empty domain?
- [ ] Is BR ≤ 3%?
- [ ] Are BR_y ≤ 17% and BR_z ≤ 17%?
- [ ] Was h_av taken into account in the case with surrounding buildings, and the topography height in the case with topography?
- [ ] Are the blockage and domain requirements satisfied separately for every wind direction?
- [ ] Is the approach flow region mesh the same as in the empty domain?
- [ ] Is the near flow region not coarser than the approach flow region?
- [ ] Is the finest mesh near the building wall and are the level transitions gradual?
- [ ] Are the mesh topology, region resolutions, transitions and quality metrics in the report?
- [ ] Is IRQ at least 75% at the monitoring points?
- [ ] At reduced scale, was independence of Reynolds number demonstrated?

## Common mistakes

- Rebuilding the domain after adding the surrounding buildings in a way that shifts the incident location; the most upwind building must sit at the location verified in the empty domain.
- Checking only the area blockage (3%) and skipping the lateral and vertical 17% limits.
- Computing the blockage for a single direction; the projected width B_y changes with direction.
- Overlooking that h_av must be used as the height in the case with surrounding buildings.
- Changing the approach flow region mesh in the building simulation (this invalidates the empty-domain verification).
- Presenting the 240 m radius as a mandatory requirement; it is commentary and a reference to ASCE 49-21, what is mandatory is the justification.
- Attributing to this section domain length multiples that are not in the document (for example "how many H" upwind/downwind); §6.3 gives only qualitative requirements and blockage limits.
- Leaving abrupt jumps in cell size between levels; using cells with a high aspect ratio (the commentary recommends avoiding them).

## Related skills

- `empty-domain-verification` — verification of the incident location, AC 5-1 domain size, AC 5-2 resolution.
- `boundary-conditions-and-quality` — wall condition, y+, IRQ calculation, time step, sampling duration.
- `topography-and-non-synoptic-wind` — Method 1, in which the topography is kept outside the domain.
