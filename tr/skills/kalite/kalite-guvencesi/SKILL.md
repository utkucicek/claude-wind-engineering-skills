---
name: kalite-guvencesi
description: Bir CFD/LES rüzgâr yükü çalışmasının kalite güvencesi (quality assurance) denetlenirken ya da planlanırken kullanılır; ASCE CWE Prestandard Bölüm 8 ve Tablo 8-1 uyum matrisi (compliance matrix), doğrulama/geçerleme (verification/validation), kıyas (benchmark) şartı, ağ çalışması (mesh study, IRQ), zaman adımı duyarlılığı ve istatistik yakınsama (statistical convergence) için.
---

# Kalite güvencesi (ASCE CWE Prestandard, Bölüm 8)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 8 (Tablo 8-1),
ayrıca Bölüm 8'in dayandığı §1.6, §6.6.3–6.6.5 ve §9.5.4–9.5.6.
Sayfa numaraları PDF sıra numarasıdır (basılı sayfa = PDF − 18). Madde dökümü: `referans.md`.

Kısaltmalar: PO = Performans Hedefi (Performance Objective), AC = Kabul Ölçütü (Acceptance Criterion),
CWE = hesaplamalı rüzgâr mühendisliği, LES = büyük girdap benzetimi (large-eddy simulation),
RANS = Reynolds ortalamalı Navier–Stokes, IRQ = çözünürlük kalitesi göstergesi (index of resolution quality),
SGS = ağ altı ölçek (subgrid scale).

## Bölüm 8'in yapısı — önce bunu bil

Bölüm 8 kısa bir bölümdür: tek alt başlık (§8.1 Kalite güvencesi iş akışı) ve Bölüm 3–7'deki bütün PO/AC maddelerini
toplayan Tablo 8-1. Kendi başına yeni bir PO/AC getirmez. Bölümün giriş cümlesi "benzetim belirsizliği üzerine bir
tartışma"dan söz eder, ancak eldeki metinde §8.1 ve tablo dışında ayrı bir belirsizlik alt bölümü yoktur
(metinde bulunamadı). Ek (appendix) de yoktur; Bölüm 10'dan sonra Kaynaklar ve Dizin gelir.

## Ne zaman kullanılır

- Bir rüzgâr yükü CFD çalışması başlamadan önce "hangi kanıtları üretmeliyim" listesi çıkarılacaksa.
- Bitmiş bir çalışmanın Prestandard'a uygunluğu madde madde denetlenecekse (uyum matrisi).
- "RANS ile tepe yük olur mu", "kıyas/geçerleme zorunlu mu", "ağ bağımsızlığı nasıl gösterilir", "hangi çalışmalar her projede tekrarlanır" soruları geldiğinde.

## Adım adım

1. **Yöntem düzeyini doğrula (§8.1).** Belge, türbülans kapaması ne olursa olsun durağan ya da durağan olmayan RANS'ın yapısal rüzgâr mühendisliği için güvenilir tepe / tam geçici çözüm veremediğini söyler; en azından LES ya da duvar modelli LES gibi girdap çözen geçici yaklaşımlar beklenir. Tablo 8-1'deki karşılığı: PO/AC 4-2 (gövdeye oturan ağla LES, duvar modelli LES dahil).
2. **Tablo 8-1'i uyum matrisine çevir.** `referans.md` içindeki tablo satırlarını al; her AC için "sağlandı / sağlanmadı / uygulanmaz", kanıtın rapordaki yeri (şekil, tablo, bölüm) ve sapma varsa gerekçesi sütunlarını ekle. Bu tablo raporda zorunludur (§9.5.5).
3. **Kod doğrulama ve model geçerleme belgelerini değerlendir (§1.6).** Kullanılan LES kodunun sağlayıcısının belgelediği doğrulama/geçerleme sınamalarının kapsamını ve titizliğini analist değerlendirir. Müşteri isterse bu bilgi, analistin yeterlilik değerlendirmesiyle birlikte verilir. Kapsam uygulamayla yeterince ilgili değilse ek sınama yapılmalı ve belgelenmelidir (öneri).
4. **Çözüm doğrulamasını (solution verification) projeye özgü yap.** Her projede tekrarlanan çalışmalar (aşağıdaki tablo): ağ çalışması, zaman adımı duyarlılığı, istatistik yakınsama, çözücü iç yineleme yakınsaması, spektrum denetimi.
5. **Yaklaşım akışını bina koşusundan önce kanıtla.** Tablo 8-1'in Bölüm 5 satırları: boş alanda hedef profil ve türbülansın gelen konumnda (incident location) yeniden üretilmesi, hız istatistiklerinin yakınsaması, spektrum kesme frekansının eylemsizlik alt aralığında (inertial subrange) olması. Ayrıntı ve eşikler Bölüm 5 becerisinde.
6. **Bina koşusunun tutarlılığını göster (PO/AC 6-1).** Ölçek, çözücü, sayısal yöntem, türbülans modeli ve sınır koşulları yaklaşım akışı koşusuyla tutarlı olmalı.
7. **Tasarım yükü kalite denetimini ekle (PO/AC 7-16).** Yöne göre ortalama/en küçük/en büyük kuvvet-moment grafikleri, kritik yönlerde spektral tepki; ağ çalışmasındaki diğer ağların sonuçları da aynı grafikte (öneri).
8. **Belirsizliği ve bilinen hata kaynaklarını yaz (§9.5.4).** Girdi parametrelerinden (rüzgâr verisi, arazi pürüzlülüğü modeli) gelen belirsizlik değerlendirilir; olasılıksal yöntem kullanıldıysa ayrıntısı verilir; bilinen diğer hata kaynakları belgelenir.
9. **Geçerleme/kıyas konusunda dürüst ol.** Belge, yayım tarihinde güvenilir kıyas vakaları bulunmadığı için sonuçların referans veriye karşı geçerlenmesini ZORUNLU TUTMAZ; temsili deneysel ya da yüksek doğruluklu benzetim verisine karşı ek geçerlemenin raporlanmasını ÖNERİR (§9.5.4 yorumu). Varsa kod doğrulama ve kıyas karşılaştırma belgeleri rapora eklenir (§9.5.6).
10. **Sayısal kayıtları sakla (§9.5.6).** Geliştirilen modellerin ve üretilen verinin sayısal kaydı kalite denetimi ve ileride başvuru için tutulur.

## Her projede tekrarlanan çalışmalar

| Çalışma | Şart | Sayısal ölçüt | Madde, PDF s. |
|---|---|---|---|
| Ağ çalışması (mesh study) | Proje için en az iki rüzgâr yönünde yapılır. | ≥ 2 yön | PO 6-15, s. 67 |
| IRQ | Akış alanındaki ve basınç alanındaki anahtar izleme konumlarında alt sınırın altına düşmez; iki ağ çözünürlüğü arasındaki yük farkları raporlanır. | IRQ ≥ %75 | AC 6-15a, s. 67 |
| İzleme konumları | Bina yüksekliği boyunca ve binadan belirli uzaklığa kadar sanal sonda dizisi; yaklaşım akışını (özellikle rüzgâr üstü izleri) ve bina izini yakalar. | binadan 160 ft'e (~50 m) kadar | AC 6-15b, s. 67 |
| Ağ inceltme katsayısı | Yorumda: en çok üç ağ (kaba, orta, ince), ardışık r katsayısıyla inceltilir; ideal olarak 2. Alt sınır değeri metin çıkarımında bozuk. | r ideal = 2; alt sınır: metinde okunamadı | §6.6.4 yorumu, s. 67 |
| IRQ yorumu | <%75: daha fazla inceltme gerekir; %75–85: mühendislik çözümü için uygun; >%85: DNS'e yakın. | %75 / %85 | §6.6.4 yorumu, s. 68 |
| Zaman adımı duyarlılığı | Gözden geçirilir; hız spektrumları bina çevresindeki ve rüzgâr üstü binalarla hedef bina arasındaki anahtar konumlarda çizilir; ağ boyutu ve zaman adımından gelen kesme grafikte işaretlenir. | yok | PO/AC 6-16, s. 68 |
| Zaman adımı sınaması (yorum) | Zaman adımı yarıya indirilmiş ikinci bir koşunun spektrumu özdeş ya da çok benzerse adım yeterlidir; ya da ağ duyarlılık çalışmasında CFL sayısı korunur. | adım × ½ | §6.6.5 yorumu, s. 68 |
| İstatistik yakınsama | Hızın ortalama/standart sapması ile yük büyüklüklerinin ortalama, standart sapma ve tepe değerleri yakınsamış olmalı. | süre > 500 boyuna integral zaman ölçeği (hedef bina yüksekliğinde) | PO/AC 6-14, s. 66 |
| Yaklaşım akışı kanıtı | Tüm farklı arazi koşulları ve tüm yönler için gelen konumndaki türbülanslı akış kalitesi gösterilir. | eşikler Bölüm 5'te | AC 5-3, 5-9 (Tablo 8-1, s. 83–84) |

Not: Bu tablodaki Bölüm 6 maddeleri bu beceri için okunan kısımdır (§6.6.2.2–6.6.5). Bölüm 3–6'nın diğer maddelerinin
eşikleri Tablo 8-1'de yalnız başlık olarak geçer; sayısal değer için ilgili bölümün becerisine/PDF'e bak, buradan sayı üretme.

## Zorunlu şartlar

- §8.1: RANS (durağan ya da değil) tepe ve geçici çözüm için güvenilir sayılmaz; en az LES / duvar modelli LES beklenir (bölüm metni "expected" der; bağlayıcı karşılığı PO/AC 4-2).
- Tablo 8-1: Bölüm 3–7'nin 53 PO ve 84 AC maddesi; hepsine uygunluk gösterilir (§9.5.5 uyum matrisi).
- §1.6: analist, kod sağlayıcının belgelediği doğrulama/geçerleme sınamalarının kapsam ve titizliğini değerlendirir; müşteri isterse verir.
- PO 6-14 / AC 6-14: istatistik yakınsama; süre > 500 boyuna integral zaman ölçeği.
- PO 6-15 / AC 6-15a, 6-15b: en az iki yönde ağ çalışması; IRQ ≥ %75; iki ağ arası farklar raporlanır.
- PO 6-16 / AC 6-16: zaman adımı duyarlılığı; spektrumlar ve kesme frekansları.
- PO 7-16 / AC 7-16: bütünlenmiş kuvvet/moment ve spektral tepki grafikleri.
- §9.5.4: ağ inceltme, zaman adımı duyarlılığı, iç yineleme çözücü yakınsaması, istatistik yakınsama ve spektral özellikler açısından benzetim kalitesi değerlendirilir; girdi belirsizliği ve bilinen hata kaynakları yazılır.
- §9.5.5: Tablo 8-1 ile hizalı uyum özeti tablosu.
- §9.5.6: Prestandard'dan sapan koşullar gerekçelendirilir; sayısal kayıt saklanır; varsa kod doğrulama / kıyas belgeleri eklenir.

## Denetim listesi (evet/hayır)

- [ ] Yöntem LES ya da duvar modelli LES mi (RANS'tan tepe yük alınmıyor mu)?
- [ ] Tablo 8-1'in her AC satırı için "sağlandı/sağlanmadı/uygulanmaz" + kanıt yeri yazıldı mı?
- [ ] Sağlanmayan ya da sapılan her madde için gerekçe var mı?
- [ ] Kullanılan kodun doğrulama/geçerleme belgeleri incelendi ve yeterliliği değerlendirildi mi?
- [ ] Ağ çalışması en az iki rüzgâr yönünde yapıldı mı?
- [ ] IRQ anahtar konumlarda (akış ve basınç alanı) %75'in altına düşmüyor mu?
- [ ] İki ağ arasındaki yük büyüklüğü farkları raporlandı mı?
- [ ] Zaman adımı duyarlılığı incelendi mi; spektrumlarda ağ ve zaman adımı kesmeleri işaretli mi?
- [ ] Benzetim süresi 500 boyuna integral zaman ölçeğinden uzun mu ve ortalama/rms/tepe yakınsaması gösterildi mi?
- [ ] Çözücünün iç yineleme yakınsaması raporlandı mı?
- [ ] Boş alanda yaklaşım akışı, tüm farklı arazi koşulları ve yönler için hedefle karşılaştırıldı mı?
- [ ] Bina koşusu, yaklaşım akışı koşusuyla aynı ölçek/çözücü/şema/model/sınır koşullarını kullanıyor mu?
- [ ] Girdi belirsizliği (rüzgâr verisi, pürüzlülük) ve bilinen hata kaynakları yazıldı mı?
- [ ] Geçerleme/kıyas yapıldıysa rapora eklendi mi; yapılmadıysa bunun zorunlu olmadığı ama önerildiği açıkça belirtildi mi?
- [ ] Model ve veri dosyalarının sayısal kaydı saklanıyor mu?

## Sık yapılan hatalar

- "Prestandard kıyas/rüzgâr tüneli geçerlemesi şart koşuyor" demek. Koşmuyor; öneriyor (§9.5.4 yorumu). Tersini, yani "geçerleme gereksiz" demek de yanlış: kod doğrulama/geçerleme belgelerinin değerlendirilmesi zorunlu (§1.6).
- Klasik ağ bağımsızlığı beklemek. Yorum: örtük süzgeçli LES'te ağ boyutu süzgeç genişliğidir; çözüm ancak DNS düzeyine yaklaşınca ağdan bağımsız olur. Bu yüzden IRQ + iki ağ arası fark raporu istenir.
- Ağ çalışmasını tek rüzgâr yönünde yapmak (en az iki).
- IRQ hesabında yöntemin kuramsal mertebesini körü körüne almak; yorum, kestirilen mertebe kuramsal olandan belirgin yüksekse kuramsal değeri benimsemekten kaçınmayı, SGS katkısını küçümsememeyi söyler.
- Yakınsamayı yalnız ortalama için gösterip tepe değerleri unutmak (PO 6-14 tepe değerleri de sayar).
- Uyum matrisini Tablo 8-1 sırasından farklı, eksik ya da kanıt göstermeden vermek.
- Tablo 8-1 başlıklarından sayısal eşik "tahmin etmek". Tablo yalnız konu başlığı verir.
- Hakem incelemesini kalite güvencesinin yerine saymak; §10.7 yorumu bunun olağan kalite güvencesinin yerini tutmadığını söyler.

## Metin çıkarımındaki tutarsızlıklar (olduğu gibi aktarıldı)

- Tablo 8-1'de bazı çapraz göndermeler "A.O." kısaltmasıyla yazılmış (ör. 5-4 satırında "A.O. 3-3", 6-5b satırında "A.O. 6-5a"); bunların AC kastettiği anlaşılıyor ama metin böyle.
- AC 5-3 satırı kabul düzeyleri için "A.C. 5-8"e gönderme yapıyor; tabloda kabul şartlarını anlatan satır AC 5-9. PDF'ten doğrulanmalı.
- AC 5-9 satırında "incipient location" yazıyor; başka yerlerde "incident location".

## İlgili beceriler

- `skills/yukler/tasarim-ruzgar-yukleri` — Bölüm 7 maddelerinin ayrıntısı (PO/AC 7-1 … 7-16).
- `skills/kalite/rapor-ve-hakem-incelemesi` — uyum matrisinin ve kalite kanıtlarının raporda sunumu, hakem incelemesi.
- `skills/surec/cwe-kapsam-ve-surec`, `skills/surec/hedef-ruzgar-tanimi`, `skills/benzetim/bos-alan-dogrulamasi`, `skills/benzetim/hesap-alani-ve-ag`, `skills/benzetim/sinir-kosullari-ve-kalite`, `skills/benzetim/topografya-ve-sinoptik-olmayan-ruzgar` — Tablo 8-1'in Bölüm 3–6 satırlarının sayısal eşikleri bu becerilerdedir.
