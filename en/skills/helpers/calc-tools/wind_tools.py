# -*- coding: utf-8 -*-
"""Check calculations for wind simulations (standard library + numpy only).

  python wind_tools.py profile  --z0 0.3 --zref 157.6 --uref 31.1 --z 20 40 80 157.6
  python wind_tools.py blockage --by 54 --h 157.6 --ly 2000 --lz 940
  python wind_tools.py cutoff   --fc 1.72 --lb 27.5 --u 31.1
  python wind_tools.py empty    measured.csv --z0 0.3 --zref 157.6 --uref 31.1 --hmax 157.6
  python wind_tools.py peak     series.csv --dt 0.05 --segments 10 --target 600

Criteria come from the ASCE CWE Prestandard (clause numbers are printed). The target profile here is the log law
with I_u = 1 / ln(z / z0); if the project defines another target (ASCE 7, EN 1991-1-4, ESDU), compute it separately."""
import argparse
import csv
import math
import sys

import numpy as np


def target_log(z, z0, zref, uref):
    """Log law: U(z) = uref ln(z/z0) / ln(zref/z0); I_u(z) = 1 / ln(z/z0)."""
    z = np.asarray(z, float)
    return uref * np.log(z / z0) / math.log(zref / z0), 1.0 / np.log(z / z0)


def profile(a):
    U, I = target_log(a.z, a.z0, a.zref, a.uref)
    print("z (m)    U (m/s)   I_u")
    for z, u, i in zip(a.z, U, I):
        print("%7.1f  %7.2f   %.3f" % (z, u, i))


def blockage(a):
    """AC 6-8b: area ratio <= 3 %, lateral and vertical ratios <= 17 %."""
    br, lat, ver = a.by * a.h / (a.ly * a.lz), a.by / a.ly, a.h / a.lz
    for name, v, lim in (("area ratio B_y h / (l_y l_z)", br, 0.03), ("lateral ratio B_y / l_y", lat, 0.17), ("vertical ratio h / l_z", ver, 0.17)):
        print("%-30s %5.1f %%   limit %4.0f %%   %s" % (name, 100 * v, 100 * lim, "pass" if v <= lim else "FAIL"))
    print("Note: with explicitly modeled surroundings, h = mean roof height of all modeled buildings, B_y = projected width.")


def cutoff(a):
    """AC 5-2: reduced cutoff frequency n L_b / U >= 2 (C&C), >= 1 (MWFRS)."""
    r = a.fc * a.lb / a.u
    print("n_c L_b / U = %.2f" % r)
    print("  components and cladding, required >= 2: %s" % ("pass" if r >= 2 else "FAIL"))
    print("  MWFRS, required >= 1:                   %s" % ("pass" if r >= 1 else "FAIL"))
    print("  required cutoff frequency: C&C %.2f Hz, MWFRS %.2f Hz" % (2 * a.u / a.lb, a.u / a.lb))


def empty(a):
    """AC 5-9: mean relative difference of U and I_u from target over the upper 75 % of h_max < 10 %.
    CSV columns: z,U,Iu (header row required). Each height is also listed."""
    s = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
    z = np.array([float(r["z"]) for r in s])
    U = np.array([float(r["U"]) for r in s])
    I = np.array([float(r["Iu"]) for r in s])
    Ut, It = target_log(z, a.z0, a.zref, a.uref)
    b = (z >= 0.25 * a.hmax) & (z <= a.hmax)
    if b.sum() < 2:
        sys.exit("at least two measurement heights are needed between 0.25 h_max and h_max")
    print("z (m)    U/target  I_u/target  in range")
    for i in range(len(z)):
        print("%7.1f   %.2f      %.2f        %s" % (z[i], U[i] / Ut[i], I[i] / It[i], "yes" if b[i] else "-"))
    eu, ei = float(np.mean(np.abs(U[b] / Ut[b] - 1))), float(np.mean(np.abs(I[b] / It[b] - 1)))
    print("Mean relative difference (z %.1f-%.1f m): U %.1f %% -> %s | I_u %.1f %% -> %s" % (
        0.25 * a.hmax, a.hmax, 100 * eu, "pass" if eu < 0.10 else "FAIL", 100 * ei, "pass" if ei < 0.10 else "FAIL"))
    print("Largest single deviation: U %.1f %%, I_u %.1f %% (the criterion is on the mean; report large single-height deviations separately)." % (
        100 * np.abs(U[b] / Ut[b] - 1).max(), 100 * np.abs(I[b] / It[b] - 1).max()))


def peak(a):
    """Expected peak from a short record: split into equal segments, fit a Gumbel distribution to the segment
    extremes (method of moments), extend to the target duration: mode_T = mode + (1/alpha) ln(T_target / T_segment);
    expected peak = mode_T + 0.5772 / alpha. CSV: one column (Cp or pressure), constant time step --dt in seconds."""
    x = []
    for r in csv.reader(open(a.csv, encoding="utf-8-sig")):
        try:
            x.append(float(r[0]))
        except (ValueError, IndexError):
            pass
    x = np.array(x)
    n = len(x) // a.segments
    if n < 20:
        sys.exit("at least 20 samples per segment are needed")
    Ts = n * a.dt
    for name, ext, sign in (("maximum", x[:n * a.segments].reshape(a.segments, n).max(1), 1), ("minimum", -x[:n * a.segments].reshape(a.segments, n).min(1), -1)):
        s = ext.std(ddof=1)
        inv_alpha = s * math.sqrt(6) / math.pi
        mode = ext.mean() - 0.5772 * inv_alpha
        v = mode + inv_alpha * math.log(a.target / Ts) + 0.5772 * inv_alpha
        print("%-8s: segment extremes mean %.3f, std %.3f | expected peak for %.0f s %.3f (observed extreme %.3f)" % (name, sign * ext.mean(), s, a.target, sign * v, sign * ext.max()))
    print("Record %.1f s = %d x %.1f s; target duration %.0f s. Extension ratio %.1f: uncertainty grows with this ratio; state it in the report." % (
        n * a.segments * a.dt, a.segments, Ts, a.target, a.target / Ts))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    k = p.add_subparsers(dest="command", required=True)
    q = k.add_parser("profile"); q.add_argument("--z0", type=float, required=True); q.add_argument("--zref", type=float, required=True)
    q.add_argument("--uref", type=float, required=True); q.add_argument("--z", type=float, nargs="+", required=True); q.set_defaults(f=profile)
    q = k.add_parser("blockage")
    for x in ("by", "h", "ly", "lz"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=blockage)
    q = k.add_parser("cutoff")
    for x in ("fc", "lb", "u"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=cutoff)
    q = k.add_parser("empty"); q.add_argument("csv")
    for x in ("z0", "zref", "uref", "hmax"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=empty)
    q = k.add_parser("peak"); q.add_argument("csv"); q.add_argument("--segments", type=int, default=10)
    q.add_argument("--target", type=float, default=600.0); q.add_argument("--dt", type=float, required=True); q.set_defaults(f=peak)
    a = p.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a.f(a)


if __name__ == "__main__":
    main()
