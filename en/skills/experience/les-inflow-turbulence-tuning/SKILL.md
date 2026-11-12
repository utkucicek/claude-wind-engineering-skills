---
name: les-inflow-turbulence-tuning
description: Use when synthetic inflow turbulence in LES misses the target in the empty domain, when turbulence decays before it reaches the building, or when the empty domain run has to be tuned repeatedly; mistakes made on one project and the sequence that worked.
---

# Tuning LES inflow turbulence in the empty domain (field experience)

This skill is not a summary of a standard. It records what happened on a single project (tall building with surroundings, LES, synthetic inflow turbulence, GPU solver). The numbers belong to that project; take the method and measure the numbers in your own run.

## When to use

- When turbulence intensity at the incident location in the empty domain run is clearly below or above the target.
- When the inflow turbulence is written as a sum of waves (sine modes).
- When the run duration has to be kept short.

## The sequence that worked

1. **Run the empty domain with the same box, mesh, solver and inlet as the building run.** Only the building and surroundings are removed from the geometry.
2. **Measure with a box average.** A single point record is noisy over a short duration; the cell average of a thin box at the incident location (example: ±15 m streamwise, ±100 m lateral, ±6 m vertical) is more stable.
3. **Measure the loss per frequency band.** If the inlet modes are locked to the record duration, each mode falls into a single FFT bin; the ratio of measured to prescribed variance per band can be read directly.
4. **Correct per band, not with a single factor.** Multiply the amplitude of each band by the inverse of the measured loss; limit the factor (example: 1–2.5).
5. **Verify the corrected inlet in the empty domain again.** An indirect estimate from the building run is misleading (see below).
6. **Write the rules before seeing the result:** at which ratio the result is valid, at which ratio it is reported with a warning, at which ratio it is void.

## Mistakes that were made

| Mistake | Symptom | Cause | Remedy |
|---|---|---|---|
| Locking mode frequencies to a short record | Turbulence at 0.37 of the target | The lowest frequency was below 1/T; the lock pushed the low-frequency modes one by one to 1/T, 2/T, 3/T…, energy piled up at periods of 1–5 s, and those waves decayed on the way | Set the lowest frequency to 1/T, reduce the number of modes |
| Planning a single overall correction factor | — | The loss differed strongly by band (ratios 0.94 / 0.42 / 0.84 / 0.95) | One factor per band |
| Estimating the building location from upstream stations of the building run | Estimate 1.2–1.3; direct measurement 0.95 | The amplification seen upstream does not carry through to the building location | Trust only the empty domain measurement |
| A waiting script matching an old "finished" line in the log | Two runs started at the same time | The search was not anchored to line start and time | Search only lines written after the run you started |
| Keeping the warm-up short | Face-average Cp differed by 0.06–0.08 between the first 20 s and the rest | Sampling started before the flow settled | Rule written in advance: if the difference exceeds the threshold, drop the first segment |

## Things to know

- **Turbulence changes along the flow.** In the same run, the ratio to target at building height was 2.06 at 60 m from the inlet, about 1.2 at 350–500 m, and 1.05 at the building location. No such change is expected across a wind tunnel turntable; report the streamwise change in the empty domain report as well.
- **Where you verify matters.** With explicitly modeled surroundings the CWE Prestandard puts the incident location at the most upwind building, not at the study building. In this project the criterion passed at the study building location and failed at the upwind edge of the surroundings.
- **Lower heights behave differently.** While the upper half was within 10 %, the ratio stayed at 0.82 at one quarter of the building height. Even if the mean criterion passes, state this in the report.
- **Reverse flow near the ground at the inlet.** With the amplified inlet the instantaneous velocity near the ground went negative (6 % of the time at 5 m). Check how the inlet boundary handles this.
- **Short record.** If the slowest wave fits into the record only once, low-frequency statistics are uncertain; for the duration requirement see `empty-domain-verification` and `boundary-conditions-and-quality`.

## Options for a lasting fix

- Precursor simulation: the turbulence is a real flow solution and does not decay on the way; it needs one long run and roughness tuning.
- A synthetic generator with more modes and mass conservation.
- First confirm with a small trial that the solver supports what a precursor needs (periodic boundaries, reading a recorded plane at the inlet).

## Related skills

- `empty-domain-verification`, `calc-tools`, `quality-assurance`
