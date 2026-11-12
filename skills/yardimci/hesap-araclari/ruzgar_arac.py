# -*- coding: utf-8 -*-
"""Rüzgâr benzetimi denetim hesapları (yalnız standart kitaplık + numpy).

  python ruzgar_arac.py profil   --z0 0.3 --zref 157.6 --uref 31.1 --z 20 40 80 157.6
  python ruzgar_arac.py tikanma  --by 54 --h 157.6 --ly 2000 --lz 940
  python ruzgar_arac.py kesme    --fc 1.72 --lb 27.5 --u 31.1
  python ruzgar_arac.py bosalan  olcum.csv --z0 0.3 --zref 157.6 --uref 31.1 --hmax 157.6
  python ruzgar_arac.py tepe     seri.csv --parca 10 --hedef 600

Ölçütlerin kaynağı: ASCE CWE ön standardı (madde numaraları çıktıda). Hedef profil burada logaritmik yasa ve
I_u = 1 / ln(z / z0) ile kurulur; proje başka bir hedef tanımlıyorsa (ASCE 7, EN 1991-1-4, ESDU) --hedef-csv ile verin."""
import argparse
import csv
import math
import sys

import numpy as np


def hedef_log(z, z0, zref, uref):
    """Logaritmik yasa: U(z) = uref ln(z/z0) / ln(zref/z0); I_u(z) = 1 / ln(z/z0)."""
    z = np.asarray(z, float)
    return uref * np.log(z / z0) / math.log(zref / z0), 1.0 / np.log(z / z0)


def profil(a):
    U, I = hedef_log(a.z, a.z0, a.zref, a.uref)
    print("z (m)    U (m/s)   I_u")
    for z, u, i in zip(a.z, U, I):
        print("%7.1f  %7.2f   %.3f" % (z, u, i))


def tikanma(a):
    """AC 6-8b: alan oranı <= %3, enine ve düşey oran <= %17."""
    br, en, du = a.by * a.h / (a.ly * a.lz), a.by / a.ly, a.h / a.lz
    for ad, v, sinir in (("alan oranı B_y h / (l_y l_z)", br, 0.03), ("enine oran B_y / l_y", en, 0.17), ("düşey oran h / l_z", du, 0.17)):
        print("%-30s %5.1f %%   sınır %4.0f %%   %s" % (ad, 100 * v, 100 * sinir, "geçti" if v <= sinir else "GEÇMEDİ"))
    print("Not: çevre binalar modellenmişse h = modellenen binaların ortalama çatı yüksekliği, B_y = izdüşüm genişliği.")


def kesme(a):
    """AC 5-2: indirgenmiş kesme frekansı n L_b / U >= 2 (kaplama), >= 1 (taşıyıcı sistem)."""
    r = a.fc * a.lb / a.u
    print("n_c L_b / U = %.2f" % r)
    print("  kaplama (C&C), gerekli >= 2:          %s" % ("geçti" if r >= 2 else "GEÇMEDİ"))
    print("  taşıyıcı sistem (MWFRS), gerekli >= 1: %s" % ("geçti" if r >= 1 else "GEÇMEDİ"))
    print("  gerekli kesme frekansı: kaplama %.2f Hz, taşıyıcı %.2f Hz" % (2 * a.u / a.lb, a.u / a.lb))


def bosalan(a):
    """AC 5-9: U ve I_u'nun hedeften bağıl farkının, h_max'ın üst %75'lik kısmındaki ortalaması < %10.
    CSV sütunları: z,U,Iu (başlık satırı zorunlu). Her yükseklik ayrıca listelenir."""
    s = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
    z = np.array([float(r["z"]) for r in s])
    U = np.array([float(r["U"]) for r in s])
    I = np.array([float(r["Iu"]) for r in s])
    Ut, It = hedef_log(z, a.z0, a.zref, a.uref)
    b = (z >= 0.25 * a.hmax) & (z <= a.hmax)
    if b.sum() < 2:
        sys.exit("0,25 h_max - h_max aralığında en az iki ölçüm yüksekliği gerekli")
    print("z (m)    U/hedef   I_u/hedef   aralıkta")
    for i in range(len(z)):
        print("%7.1f   %.2f      %.2f        %s" % (z[i], U[i] / Ut[i], I[i] / It[i], "evet" if b[i] else "-"))
    eu, ei = float(np.mean(np.abs(U[b] / Ut[b] - 1))), float(np.mean(np.abs(I[b] / It[b] - 1)))
    print("Ortalama bağıl fark (z %.1f-%.1f m): U %.1f %% -> %s | I_u %.1f %% -> %s" % (
        0.25 * a.hmax, a.hmax, 100 * eu, "geçti" if eu < 0.10 else "GEÇMEDİ", 100 * ei, "geçti" if ei < 0.10 else "GEÇMEDİ"))
    print("Tek tek en büyük sapma: U %.1f %%, I_u %.1f %% (ölçüt ortalama üzerinedir; tek yükseklikteki büyük sapmayı raporda ayrıca yazın)." % (
        100 * np.abs(U[b] / Ut[b] - 1).max(), 100 * np.abs(I[b] / It[b] - 1).max()))


def tepe(a):
    """Kısa kayıttan beklenen tepe: kayıt eşit parçalara bölünür, parça uç değerlerine Gumbel uydurulur (momentler),
    hedef süreye uzatılır: mod_T = mod + (1/alfa) ln(T_hedef / T_parça); beklenen tepe = mod_T + 0,5772 / alfa.
    CSV: tek sütun (Cp ya da basınç), sabit zaman adımı; --dt saniye."""
    x = np.array([float(r[0]) for r in csv.reader(open(a.csv, encoding="utf-8-sig")) if r and r[0].replace(".", "").replace("-", "").replace("e", "").replace("+", "").isdigit()])
    n = len(x) // a.parca
    if n < 20:
        sys.exit("parça başına en az 20 örnek gerekli")
    Tp = n * a.dt
    for ad, uc in (("en büyük", x[:n * a.parca].reshape(a.parca, n).max(1)), ("en küçük", -x[:n * a.parca].reshape(a.parca, n).min(1))):
        s = uc.std(ddof=1)
        inv_alfa = s * math.sqrt(6) / math.pi
        mod = uc.mean() - 0.5772 * inv_alfa
        v = mod + inv_alfa * math.log(a.hedef / Tp) + 0.5772 * inv_alfa
        isaret = 1 if ad == "en büyük" else -1
        print("%-9s: parça uçları ort. %.3f, std %.3f | %.0f s için beklenen tepe %.3f (gözlenen uç %.3f)" % (ad, isaret * uc.mean(), s, a.hedef, isaret * v, isaret * uc.max()))
    print("Kayıt %.1f s = %d x %.1f s; hedef süre %.0f s. Uzatma oranı %.1f: oran büyüdükçe belirsizlik artar; raporda yazın." % (n * a.parca * a.dt, a.parca, Tp, a.hedef, a.hedef / Tp))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    k = p.add_subparsers(dest="komut", required=True)
    q = k.add_parser("profil"); q.add_argument("--z0", type=float, required=True); q.add_argument("--zref", type=float, required=True)
    q.add_argument("--uref", type=float, required=True); q.add_argument("--z", type=float, nargs="+", required=True); q.set_defaults(f=profil)
    q = k.add_parser("tikanma")
    for x in ("by", "h", "ly", "lz"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=tikanma)
    q = k.add_parser("kesme")
    for x in ("fc", "lb", "u"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=kesme)
    q = k.add_parser("bosalan"); q.add_argument("csv")
    for x in ("z0", "zref", "uref", "hmax"):
        q.add_argument("--" + x, type=float, required=True)
    q.set_defaults(f=bosalan)
    q = k.add_parser("tepe"); q.add_argument("csv"); q.add_argument("--parca", type=int, default=10)
    q.add_argument("--hedef", type=float, default=600.0); q.add_argument("--dt", type=float, required=True); q.set_defaults(f=tepe)
    a = p.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a.f(a)


if __name__ == "__main__":
    main()
