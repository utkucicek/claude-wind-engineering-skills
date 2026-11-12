---
name: calc-tools
description: Ready-made script for wind simulation checks; use when you need a target profile (log law, I_u), blockage ratios, cutoff frequency check, the empty domain 10 % check, or a peak value from a short record (Gumbel).
---

# Calculation tools

One file: `wind_tools.py` (Python 3, needs only `numpy`). It has five subcommands; all of them only read input and print a table.

## When to use

- When sizing or checking the computational domain (blockage).
- After an empty domain run, when comparing the measured profile with the target.
- When deciding from a spectrum whether the mesh is fine enough (cutoff frequency).
- When estimating the peak value for the design duration from a short pressure record.

## Commands

| Command | What it does | Source of the criterion |
|---|---|---|
| `profile --z0 --zref --uref --z ...` | Target U(z) and I_u(z) table from the log law | The target belongs to the project; see `target-wind-definition` |
| `blockage --by --h --ly --lz` | Area ratio ≤ 3 %, lateral and vertical ratios ≤ 17 % | CWE Prestandard AC 6-8b |
| `cutoff --fc --lb --u` | n·L_b/U ≥ 2 (C&C), ≥ 1 (MWFRS) | AC 5-2, AC 5-10 |
| `empty measured.csv --z0 --zref --uref --hmax` | Mean relative difference of U and I_u < 10 % over the upper 75 % of h_max | AC 5-9 |
| `peak series.csv --dt --segments --target` | Gumbel fit to segment extremes, extended to the target duration | For the choice of method see `design-wind-loads` |

Example:

```bash
python wind_tools.py blockage --by 54 --h 157.6 --ly 2000 --lz 940
```

## Input formats

- `empty`: CSV with a header row, columns `z,U,Iu` (m, m/s, ratio). Take the values from a vertical line at the incident location, or from a box average at that location.
- `peak`: single-column CSV (Cp or pressure), constant time step `--dt` (s).

## Limits

- The target profile is built only from the log law and I_u = 1 / ln(z / z0). If the project defines an ASCE 7, EN 1991-1-4 or ESDU profile, compute the target column from that source and compare by hand.
- `empty` computes the deviation as the mean of absolute relative differences at the measurement heights between 0.25·h_max and h_max. Equations 5-1 and 5-2 in the document are integrals over height; the lower limit and the absolute value sign could not be read from the PDF, so check them against the original. If the measurement heights are not evenly spaced, check the result by hand.
- The `empty` criterion is on the mean deviation; the script also prints the largest single-height deviation. Report it separately.
- For `peak`, uncertainty grows with the ratio of target duration to segment duration; the ratio is printed.

## Related skills

- `empty-domain-verification`, `domain-and-mesh`, `design-wind-loads`
