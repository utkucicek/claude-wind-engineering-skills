# Beceri dizini

Toplam 15 beceri.

## Süreç (CWE Bölüm 1–4)

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [cwe-kapsam-ve-surec](skills/surec/cwe-kapsam-ve-surec/SKILL.md) | ASCE hesaplamalı rüzgâr mühendisliği ön standardının (Prestandard for Use of Computational Wind Engineering in Building Design, CWE) kapsamı, dışladıkları, izin verilen araçlar (LES, wall-modeled LES, hybrid RANS/LES; RANS, LBM, immersed boundary durumu), doğrulama-geçerleme (verification and validation), iki adımlı süreç (approach flow + building aerodynamics), gelen konum (incident location) ve temel tanımlar sorulduğunda ya da bir CFD rüzgâr yükü çalışmasının bu belgeye uyup uymadığı baştan denetlenecekse kullanılır. | SKILL.md, referans.md |
| [hedef-ruzgar-tanimi](skills/surec/hedef-ruzgar-tanimi/SKILL.md) | ASCE CWE ön standardı Bölüm 3'e göre rüzgâr iklimi modeli (wind climate model) ve gelen konumdaki (incident location) hedef rüzgâr akış koşulları (target wind flow conditions) tanımlanacaksa kullanılır: fırtına türleri, ortalama hız profili (mean wind speed profile), türbülans şiddeti (turbulence intensity), tümlev uzunluk ölçeği (integral length scale), güç spektrumu (power spectral density), Reynolds gerilmesi, pürüzlülük uzunluğu z0 (roughness length), maruziyet değişimi (exposure change) ve topoğrafya etkisi. | SKILL.md, referans.md |

## Benzetim (CWE Bölüm 5–6)

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [bos-alan-dogrulamasi](skills/benzetim/bos-alan-dogrulamasi/SKILL.md) | Bina eklenmeden önce boş hesap alanında (empty domain) yaklaşan akışın (approach flow) hedef atmosferik sınır tabakasını gelen konumda (incident location) tutturduğunu kanıtlamak gerektiğinde kullan; giriş türbülansı (precursor, recycling, synthetic inflow), zemin pürüzlülüğü z0, U ve I_u profil hatası, integral length scale, spectrum, cutoff frequency ve basınç oynaması ölçütlerini ASCE CWE Prestandard Bölüm 5.1 ve 5.4'e göre denetler. | SKILL.md, referans.md |
| [hesap-alani-ve-ag](skills/benzetim/hesap-alani-ve-ag/SKILL.md) | Bina aerodinamiği benzetimi için geometri modelini (study building, proximity model, radius of proximity, topography, appurtenances, porous components), hesap alanı boyutunu (computational domain, blockage ratio) ve ağı (mesh regions, refinement, IRQ) kurarken ya da denetlerken kullan; ASCE CWE Prestandard Bölüm 6.2, 6.3 ve 6.4 şartlarını verir. | SKILL.md, referans.md |
| [sinir-kosullari-ve-kalite](skills/benzetim/sinir-kosullari-ve-kalite/SKILL.md) | Bina aerodinamiği LES benzetiminde sınır koşullarını (no-slip wall, wall model, y+, reference static pressure) kurarken ve kalite güvencesini (solver convergence, contour plots, monitoring probes, statistical convergence, sampling duration, mesh sensitivity, IRQ, time-step sensitivity, CFL) yaparken ya da raporlarken kullan; ASCE CWE Prestandard Bölüm 6.1, 6.5 ve 6.6 şartlarını verir. | SKILL.md, referans.md |
| [topografya-ve-sinoptik-olmayan-ruzgar](skills/benzetim/topografya-ve-sinoptik-olmayan-ruzgar/SKILL.md) | Hedef rüzgâr profili ayrı bir topografya benzetiminden geliyorsa (topography Method 1, empty domain'de topografyasız yeniden üretim) ya da fırtına inişi, hortum gibi sinoptik olmayan rüzgâr (non-synoptic wind, downburst, tornado) benzetimi sorulduğunda kullan; ASCE CWE Prestandard Bölüm 5.2 ve 5.3'ün ne istediğini ve neyi kapsam dışı bıraktığını söyler. | SKILL.md, referans.md |

## Yükler (CWE Bölüm 7)

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [tasarim-ruzgar-yukleri](skills/yukler/tasarim-ruzgar-yukleri/SKILL.md) | CFD/LES (CWE) sonuçlarından tasarım rüzgâr yükü çıkarılırken kullanılır; basınç katsayısı (pressure coefficient, Cp) tanımı ve referans hızı, tepe değer kestirimi (peak estimation, Gumbel, extreme value), kaplama (C&C) ile taşıyıcı sistem (MWFRS) ayrımı, rüzgâr iklimiyle birleştirme ve yönsellik (directionality), iç basınç (internal pressure), ASCE 7 sınırlaması ve DAF için ASCE CWE Prestandard Bölüm 7 şartlarını uygular. | SKILL.md, referans.md |

## Kalite ve rapor (CWE Bölüm 8–10)

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [kalite-guvencesi](skills/kalite/kalite-guvencesi/SKILL.md) | Bir CFD/LES rüzgâr yükü çalışmasının kalite güvencesi (quality assurance) denetlenirken ya da planlanırken kullanılır; ASCE CWE Prestandard Bölüm 8 ve Tablo 8-1 uyum matrisi (compliance matrix), doğrulama/geçerleme (verification/validation), kıyas (benchmark) şartı, ağ çalışması (mesh study, IRQ), zaman adımı duyarlılığı ve istatistik yakınsama (statistical convergence) için. | SKILL.md, referans.md |
| [rapor-ve-hakem-incelemesi](skills/kalite/rapor-ve-hakem-incelemesi/SKILL.md) | Bir CFD/LES rüzgâr yükü raporu yazılırken, mevcut bir rapor eksik içerik açısından denetlenirken ya da bağımsız hakem incelemesi (independent peer review) planlanırken kullanılır; ASCE CWE Prestandard Bölüm 9 (report content, compliance matrix) ve Bölüm 10 (project peer review, basis of design, comment log, AHJ) şartlarını denetim listesi olarak uygular. | SKILL.md, referans.md |

## Rüzgâr tüneli (ASCE/SEI 49-21)

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [tunel-basinc-olcumu-ve-yukler](skills/tunel/tunel-basinc-olcumu-ve-yukler/SKILL.md) | Rüzgâr tünelinde basınç ölçümü (pressure taps, tubing frequency response, sampling rate/duration), referans basınç ve hız (reference pressure/velocity), tepe değer kestirimi (peak pressure, Gumbel), alan ortalaması/basınç integrasyonu (pressure integration), iç basınç (internal pressure), kaplama (C&C) ve taşıyıcı sistem (MWFRS) yükleri, rüzgâr iklimiyle birleştirme ve yönsellik (wind climate, directionality), ölçüm belirsizliği, kalite güvencesi ve rapor içeriği ASCE/SEI 49-21'e göre sorulduğunda veya bir tünel raporu bu açılardan denetlenirken kullan. | SKILL.md, referans.md |
| [tunel-diger-olcumler](skills/tunel/tunel-diger-olcumler/SKILL.md) | Rüzgâr tünelinde basınç deliği dışındaki ölçümler ASCE/SEI 49-21'e göre sorulduğunda kullan; yüksek frekanslı kuvvet terazisi (high-frequency force balance, HFFB), doğrudan yük ölçümü ve rijit kesit modeli (section model), esnek yapılarda dinamik tepki çözümlemesi, aeroelastik model (aeroelastic model; vortex shedding, galloping, flutter), ürün deneyleri (products, solar arrays), kar yükü model çalışmaları (snow load), hortum/aşağı patlama (tornado, downburst) çerçevesi ve yaya düzeyi rüzgârın (pedestrian wind) kapsam durumu. | SKILL.md, referans.md |
| [tunel-model-ve-cevre](skills/tunel/tunel-model-ve-cevre/SKILL.md) | Rüzgâr tüneli modelinin ASCE/SEI 49-21'e göre ölçeği (geometric scale), geometrik ayrıntısı ve doğruluğu, yakın çevre modeli (proximity model) kapsamı, tıkanma oranı (blockage ratio) sınırı ve düzeltmesi, Reynolds sayısı (Reynolds number) şartları ile yuvarlak hatlı yapılar ve rüzgâr yönü adımı (wind direction increment) sorulduğunda veya bir tünel raporunda bunlar denetlenirken kullan. | SKILL.md, referans.md |
| [tunel-yaklasan-akis](skills/tunel/tunel-yaklasan-akis/SKILL.md) | Rüzgâr tünelinde atmosferik sınır tabaka (atmospheric boundary layer, ABL) benzetiminin ASCE/SEI 49-21'e göre kurulması veya denetlenmesi gerektiğinde kullan; hedef ortalama hız profili (mean velocity profile), türbülans şiddeti (turbulence intensity), integral uzunluk ölçeği (integral length scale), güç spektrumu (power spectral density), pürüzlülük Reynolds sayısı, referans hız/yükseklik (Uref, zref), kısmi ABL ve kısmi türbülans benzetimi (partial turbulence simulation, PTS), topoğrafya modeli (topographic model) konularını kapsar. | SKILL.md, referans.md |

## Yardımcı

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [hesap-araclari](skills/yardimci/hesap-araclari/SKILL.md) | Rüzgâr benzetimi denetim hesapları için hazır betik; hedef profil (log law, I_u), tıkanma oranı (blockage), kesme frekansı (cutoff frequency), boş alan (empty domain) ±%10 denetimi ve kısa kayıttan tepe değer (Gumbel peak) hesabı gerektiğinde kullanılır. | SKILL.md, ruzgar_arac.py |

## Deneyim

| Beceri | Ne zaman kullanılır | Dosyalar |
|---|---|---|
| [les-giris-turbulansi-ayari](skills/deneyim/les-giris-turbulansi-ayari/SKILL.md) | LES'te yapay giriş türbülansı (synthetic inflow turbulence) boş alanda (empty domain) hedefi tutturmadığında, türbülans binaya gelmeden söndüğünde ya da boş alan koşusu tekrar tekrar ayarlanırken kullanılır; bir projede yaşanmış hatalar ve işe yarayan sıra. | SKILL.md |
