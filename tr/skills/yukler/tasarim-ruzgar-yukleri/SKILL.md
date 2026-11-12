---
name: tasarim-ruzgar-yukleri
description: CFD/LES (CWE) sonuçlarından tasarım rüzgâr yükü çıkarılırken kullanılır; basınç katsayısı (pressure coefficient, Cp) tanımı ve referans hızı, tepe değer kestirimi (peak estimation, Gumbel, extreme value), kaplama (C&C) ile taşıyıcı sistem (MWFRS) ayrımı, rüzgâr iklimiyle birleştirme ve yönsellik (directionality), iç basınç (internal pressure), ASCE 7 sınırlaması ve DAF için ASCE CWE Prestandard Bölüm 7 şartlarını uygular.
---

# Tasarım rüzgâr yükleri (ASCE CWE Prestandard, Bölüm 7)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 7.
Sayfa numaraları PDF sıra numarasıdır (basılı sayfa = PDF sayfası − 18). Madde madde döküm: `referans.md`.

Kısaltmalar: PO = Performans Hedefi (Performance Objective), AC = Kabul Ölçütü (Acceptance Criterion),
CWE = hesaplamalı rüzgâr mühendisliği (computational wind engineering), MWFRS = ana rüzgâr taşıyıcı sistem
(main wind force resisting system), C&C = bileşenler ve kaplama (components and cladding),
AHJ = yetkili idare (Authority Having Jurisdiction), DAF = dinamik büyütme katsayısı (dynamic amplification factor).

## Ne zaman kullanılır

- Bir LES koşusunun basınç/kuvvet zaman serilerinden tasarım yükü (taban kesme, devrilme momenti, kat kat yük, kaplama basıncı) çıkarılacaksa.
- Tepe basınç katsayısının nasıl kestirileceği, tek gözlenen tepe değerin kullanılıp kullanılamayacağı sorulduğunda.
- CFD sonucu rüzgâr iklimi (dönüş periyodu, yön) ile birleştirilecekse.
- İç basınç, net basınç, ek yapı elemanı (appurtenance: güneş kırıcı, saçak, çatı ekipmanı, parapet) yükü hesaplanacaksa.
- CFD yükünün ASCE 7 ile ilişkisi / alt sınırı sorulduğunda.

Kapsam dışı: hortum ve diğer sinoptik olmayan olaylar (§7.7; belge açık bir yöntem vermez).

## Adım adım

1. **Yapıyı sınıflandır (§7 giriş, §1.8).** Rijit (rigid), esnek (flexible) ya da aeroelastik. Belge frekansa dayalı bir sınır vermez; ASCE 7-22 sınırı iyi bir gösterge sayılır ama her yapı türünü kapsamaz (YORUM niteliğinde giriş metni).
2. **Rüzgâr yönlerini belirle (PO/AC 7-1).** Azimut adımı en çok 10°. Sonuçlar daha büyük tasarım yükü olasılığı gösteriyorsa ara yönler eklenir. Yön sayısının azaltılması yalnız gerekçe + hakem ekibi + AHJ onayıyla (yorum).
3. **Referans hızı izle (PO/AC 7-2).** Referans rüzgâr hızı, yakın çevre modelinin etkisinin en az olduğu bir noktada izlenir ve belgelenir. Yorum: tipik olarak ya sınır tabakasının dışında sayılan bir yükseklikte, ya da yapı yüksekliğinde ve açıkça modellenen çevrenin rüzgâr üstünde. Başka yüksekliğe çevirme yapılırsa ayrıntılı belgelenir.
4. **Basınç katsayılarını hesapla (PO/AC 7-13, Denk. 7-6).** Her izleme noktası için ortalama, standart sapma (rms), en küçük ve en büyük dış basınç katsayısı; hepsi referans dinamik basınca (q_ref = ½·ρ·U_ref²) bölünerek. Bu dört katsayı şeffaflık ve hakem incelemesi için istenir.
5. **MWFRS aerodinamik tepkisi (PO 7-5).** Yüzey kuvvetleri her sınır yüzü üzerinden bütünlenir. Tercih edilen yol: bütünlemeyi koşu sırasında önceden tanımlı etki alanları (tributary area) üzerinde yapmak — tüm bina (taban kesme/moment), bina dilimi (kesit kuvvetleri), tek kat (kat kat yük) (AC 7-5a). Ayrık noktalardaki basınç zaman serilerinin bütünlenmesi de kabul edilir; nokta dağılımı yük etkisini doğru yakalayacak yoğunlukta olmalı (AC 7-5b). Gözenekli ortam (porous media) ile modellenen elemanların kuvveti toplam yüke katılır (AC 7-5c).
6. **MWFRS tasarım yükü ve dinamik tepki (PO/AC 7-6, §7.3).** Bütün taşıyıcı sistemler esnek kabul edilir; yalnız rijit yapıya uygun yöntem, ancak teknik gerekçe ayrıntılı belgelenirse kullanılır. Frekans ya da zaman tanım alanı serbest; her durumda DAF raporlanır.
7. **MWFRS sonuç sunumu (PO/AC 7-7).** Tepe yükler ve yapısal etkiler ya eşdeğer statik rüzgâr yükü (equivalent static wind load) ya da yapısal modele doğrudan uygulanacak kuvvet/basınç zaman serisi olarak verilir.
8. **C&C yerel tepe basınçlar (PO/AC 7-8, 7-9).** İzleme noktaları dış geometrinin karmaşıklığına ve basınç gradyanına göre seçilir; küçük binalarda ve yüksek gradyanlı bölgelerde (çatı köşesi, kenar, mahya, duvar kenarı) daha sık nokta önerilir. Doğrudan bütünleme (integral) yöntemi de kullanılabilir; etki alanlarının boyutu ve dağılımı izleme noktası ilkeleriyle tutarlı seçilir. İç basınç payı hesaba katılır.
9. **Tepe tasarım yükünü kestir (PO 7-10).** Tepe değer bir uç değer dağılımı (extreme value distribution) ile, rüzgâr iklimiyle birleştirmeye uygun süre ve olasılık düzeyi için belirlenir. Aşılma olasılığı raporlanır (AC 7-10a). Aerodinamik olaylarla ilgili olabilecek frekansları silen hiçbir süzgeç uygulanmaz (AC 7-10b). Tek gözlenen tepe katsayısı kullanılmaz (yorum metninde, "shall not" ifadesiyle). Yöntem seçenekleri için aşağıdaki "Tepe değer yöntemleri" tablosuna bak.
10. **Net ve iç basınç (PO 7-11, 7-12).** Ek elemanların net basınç katsayısı net basıncın doğrudan türetilmesiyle bulunur. İç basınç ya benzetilmiş dış basınçlardan analitik olarak kestirilir ya da doğrudan benzetimde çözülür; gözeneklilik, sızıntı ve açıklıklar farklı senaryolar için dikkate alınır.
11. **Ek yapı elemanları (PO 7-14, 7-15).** Yükler ana yapı ile aynı hesap modelinden alınır; rijit ek elemanda §7.4.3 istatistik yaklaşımı, esnek ek elemanda §7.3.2 ile DAF.
12. **Rüzgâr iklimiyle birleştir (PO 7-4).** Kabul edilen altı yöntemden biri seçilir; sahadaki bütün hava sistemleri hesaba katılır; varsayımlar ve birleştirme yöntemi ayrıntılı belgelenir.
13. **Sınırlama ve tutarlılık denetimi (PO 7-3).** Yük, çevrenin gelecekte değişmesine (ör. komşu binanın yıkılması) bağlı olmadan belirlenir. MWFRS ve C&C yükleri ASCE/SEI 7-22'deki yöntemlere göre sınırlanır (AC 7-3a). İstatistiksel olarak durağan kuvvet/moment katsayıları, herhangi bir yük azalmasının bina türü ve biçimi için beklenenle uyumlu olduğunu doğrulamak üzere denetlenir (AC 7-3b).
14. **Tasarım yükü kalite denetimi (PO/AC 7-16).** Bütünlenmiş kuvvet ve momentler bir referans noktasına (genellikle taban ya da yapısal orijin) göre çizilir: her bileşen için yöne göre ortalama, en küçük, en büyük. Kritik yönlerde spektral tepki çizilir. Yorum: ağ çalışmasındaki diğer ağların sonuçları da aynı grafiklere eklenmeli.

## Tepe değer yöntemleri (§7.4.3 yorumu, PDF s. 76)

| Yöntem | Metnin söylediği |
|---|---|
| Topluluk ortalaması (ensemble average) | Eşit uzunlukta dilimlerden alınan birkaç en büyük/en küçük değerin ortalaması; dilim, uygun bir gerçek ölçek gözlem süresini (örnek olarak 10 dk – 1 sa) temsil edecek biçimde ölçeklenir. Yaygın iki yöntemden biri. |
| Gumbel uydurma (Gumbel fitting) | Eşit uzunlukta dilimlerin uç değerleriyle belirli bir kesir (fractile) düzeyine karşılık gelen tepe kestirilir. Yaygın iki yöntemden diğeri. |
| Bağımsız fırtınalar yöntemi, BLUE (best linear unbiased estimator), eşik üstü tepeler (peak-over-threshold) | Tanınan diğer uç değer yöntemleri olarak anılır. |
| Cook–Mayne | Gumbel uydurmanın, yük ve rüzgâr hızı uç değer dağılımlarını birleştiren uzantısı; en doğru sonucu verir ama uç rüzgâr iklimini bilmeyi gerektirir, bu yüzden farklı iklimlerde kullanılacak ürünlerin genel katsayıları için uygun değildir. |

Metinde BULUNMAYANLAR: dilim sayısı, kesir düzeyi (ör. %78 gibi bir değer), Gumbel için en az kayıt süresi. Bunları belge adına yazma.
Kayıt süresi şartı Bölüm 6'dadır: benzetim süresi hedef bina yüksekliğindeki boyuna integral zaman ölçeğinin (longitudinal integral time scale) 500 katından uzun olmalı (AC 6-14, PDF s. 66). Örnekleme çözünürlüğü için sayısal eşik yok; seçimin raporda gerekçelendirilmesi istenir (AC 6-13d, PDF s. 66).

## Rüzgâr iklimiyle birleştirme yöntemleri (AC 7-4a; yorum PDF s. 70–73)

| Yöntem | Özet (yorum metni) |
|---|---|
| Üst sınır / yönsüz (upper bound, nondirectional) | En basit ve en güvenli taraf. Yönsellik yok sayılır; tüm yönlerin en büyük tepkisi tasarım hızıyla eşlenir. İklim analizi yapmadan ASCE 7-22 hızlarıyla da kullanılabilir; o durumda fırtına türüne göre ayrım gerekmez. |
| Normalleştirilmiş sektör (normalized sector) | Basit; çoğunlukla güvenli tarafta, nadiren güvensiz çıkabilir. Yönlü birleşik iklim modeli gerekir. |
| Çok sektörlü (multisector) | Her sektör için tepki–aşılma olasılığı hesaplanır; sektörlerdeki uç rüzgârların istatistiksel bağımsızlığı varsayılır. Gök gürültülü fırtına ve ekstratropikal fırtına için ayrı uygulanır. |
| Yukarı geçiş (up-crossing) | Ana olasılık dağılımına (genellikle iki parametreli Weibull) dayanır; bugünkü uygulama gök gürültülü fırtınayı ayırmaz. |
| Fırtına geçişi (storm passage) | Benzetilmiş her tropikal siklonun hız–yön zaman serisinden en büyük tepki bulunur. |
| Doğrudan benzetim (direct simulation) | Yönlü uç değer dağılımlarından Monte Carlo ile büyük veri kümesi üretilir. |

Yorum: R yıllık rüzgâr hızı ile R yıllık rüzgâr etkisi arasında açık bir ilişki yoktur; etki fırtına türü bazında bulunup sonra birleştirilmelidir (Denk. 7-1; denklem metinde okunamadı).
İklim modelinin yön çözünürlüğü çoğu kez CWE verisinden kabadır; iki veri kümesini birleştirirken yapılan varsayımlar rapora yazılır.

## Zorunlu şartlar

- PO 7-1 / AC 7-1 (§7.1.1): yön adımı ≤ 10°; daha büyük yük olasılığı varsa ek yön.
- PO 7-2 / AC 7-2 (§7.1.2): referans hız, yakın çevre modelinden en az etkilenen yerde izlenir ve belgelenir.
- PO 7-3 / AC 7-3a, 7-3b (§7.1.3): çevrenin gelecekteki değişimine güvenilmez; yükler ASCE/SEI 7-22 yöntemlerine göre sınırlanır; yük azalması durağan kuvvet/moment katsayılarıyla tutarlılık açısından denetlenir.
- PO 7-4 / AC 7-4a, 7-4b (§7.2): altı istatistik yöntemden biri; tüm hava sistemleri; varsayımlar belgelenir.
- §7.3 giriş: bütün sistemler esnek kabul edilir; rijit yöntem yalnız belgelenmiş gerekçeyle.
- PO 7-5 / AC 7-5a–c (§7.3.1): yüzey kuvvetlerinin bütünlenmesi; gözenekli ortam kuvvetleri dahil.
- PO 7-6 / AC 7-6 (§7.3.2): DAF her durumda raporlanır.
- PO 7-7 / AC 7-7 (§7.3.3): tepe yük ve etkiler sunulur (eşdeğer statik yük ya da zaman serisi).
- PO 7-8 / AC 7-8 (§7.4.1): C&C için basınç verisi + iç basınç payı; yeterli sayıda ve doğru yerde izleme noktası.
- PO 7-9 / AC 7-9 (§7.4.2): bütünleme yönteminde etki alanları yeterli uzamsal çözünürlükte.
- PO 7-10 / AC 7-10a, 7-10b (§7.4.3): uç değer dağılımı; aşılma olasılığı raporu; aerodinamik frekansları silen süzgeç yok.
- PO/AC 7-11 (§7.4.4): net basınç doğrudan türetilir.
- PO 7-12 / AC 7-12a–c (§7.4.5): iç basınç; tam ölçekte değilse iç hacim ölçeklemesi; kısmen kapalı boşluklar.
- PO/AC 7-13 (§7.4.6): ortalama, rms, en küçük, en büyük dış basınç katsayıları.
- PO 7-14 / AC 7-14a, 7-14b (§7.5.1): ek elemanlar aynı modelden; rijit/esnek ayrımı.
- PO/AC 7-15 (§7.5.2): ürün deney raporu içeriği (etkin rüzgâr alanı ilişkisi, katsayıya çevirme, uygulanabilirlik koşulları).
- PO/AC 7-16 (§7.6): kuvvet/moment grafikleri ve kritik yön spektrumları.

## Denetim listesi (evet/hayır)

- [ ] Yön adımı 10° ya da daha küçük mü? Büyükse gerekçe + hakem + AHJ onayı var mı?
- [ ] Sonuçlar ara yönde daha büyük yük olasılığı gösteriyor mu; gösteriyorsa ek yön koşuldu mu?
- [ ] Referans hızın izlendiği nokta ve yükseklik belgelendi mi; yakın çevre etkisinden uzak mı?
- [ ] Katsayılar başka bir yüksekliğe çevrildiyse dönüşüm ayrıntılı yazıldı mı?
- [ ] Her nokta için Cp ortalama, rms, en küçük, en büyük verildi mi?
- [ ] Tepe değer bir uç değer istatistiğiyle mi bulundu (tek gözlenen tepe DEĞİL)?
- [ ] Aşılma olasılığı raporlandı mı?
- [ ] Zaman serisine aerodinamik frekansları silebilecek süzgeç uygulanmadığı doğrulandı mı?
- [ ] Benzetim süresi 500 boyuna integral zaman ölçeğinden uzun mu (AC 6-14)?
- [ ] MWFRS kuvvetleri tanımlı etki alanları üzerinde bütünlendi mi; gözenekli eleman kuvvetleri dahil mi?
- [ ] Yapı esnek kabul edildi mi; edilmediyse gerekçe belgelendi mi?
- [ ] DAF raporlandı mı?
- [ ] İç basınç nasıl ele alındı (analitik / doğrudan / yönetmelik değeri) yazıldı mı; açıklık ve sızıntı senaryoları düşünüldü mü?
- [ ] Rüzgâr iklimi birleştirme yöntemi altı yöntemden biri mi ve varsayımları yazıldı mı?
- [ ] Yük, komşu yapıların gelecekte değişmesine bağlı olmadan mı belirlendi?
- [ ] ASCE/SEI 7-22'ye göre sınırlama uygulandı mı; yük azalması katsayılarla tutarlı mı?
- [ ] Yöne göre ortalama/en küçük/en büyük kuvvet-moment grafikleri ve kritik yön spektrumları var mı?

## Sık yapılan hatalar

- Kayıttaki tek en büyük/en küçük Cp değerini tasarım değeri diye almak. Belge bunun tekrarlanabilirliğinin zayıf olduğunu ve deney süresine bağlı olduğunu söyler.
- Gürültüyü azaltmak için zaman serisini süzmek ve bu sırada aerodinamik kaynaklı frekansları silmek (AC 7-10b).
- Belgeye olmayan sayı yakıştırmak: Gumbel kesir düzeyi, dilim sayısı, ASCE 7'nin yüzde kaçı gibi alt sınır oranları Bölüm 7 metninde yoktur; "ASCE/SEI 7-22 yöntemlerine göre sınırlanır" denir.
- CFD yükünü yalnız komşu binanın perdelemesi sayesinde düşük bulup bunu tasarıma taşımak (PO 7-3).
- Rijit yapı varsayımıyla dinamik bileşeni atlamak; belge varsayılan olarak esnek kabul ister.
- DAF'ı raporlamamak.
- İç basıncı unutup yalnız dış Cp ile kaplama tasarlamak.
- Referans hızı yapının ya da çevre modelinin etkilediği bir noktadan almak.
- Gözenekli ortamla modellenen elemanların kuvvetini toplam yüke eklememek.
- Bu bölümü hortum yükü için kullanmak (§7.7 kapsam dışı; yorum yalnız ASCE/SEI 7-22 Bölüm 32 ile temel katsayı kullanımına değinir).

## Metinde bulunmayanlar (uydurma)

- Kaplama için alan ortalamasında sayısal alan büyüklüğü: metinde bulunamadı. Yalnız etki alanı seçim ilkesi (AC 7-9) ve raporda yerel + alan ortalamalı kaplama basıncı istenmesi (§9.4.5.8) var.
- Bölüm 7'de ayrı bir "belirsizlik" (uncertainty) maddesi: metinde bulunamadı. Belirsizlik değerlendirmesi rapor şartı olarak §9.5.4'tedir.
- Basınç noktası yoğunluğu için tek sayı yorumdadır: AWES-QAM-1 önerisi olarak tam ölçekte 120 m² (yaklaşık 1.300 ft²) yüzey başına en az 1 nokta; CWE'de en azından rüzgâr tüneli uygulamasıyla tutarlı olmalı (YORUM, PDF s. 74).

## İlgili beceriler

- `skills/kalite/kalite-guvencesi` — Tablo 8-1 uyum matrisi, ağ ve zaman adımı çalışmaları, istatistik yakınsama.
- `skills/kalite/rapor-ve-hakem-incelemesi` — bu bölümde üretilen sonuçların raporda nasıl sunulacağı ve hakem incelemesi.
- `skills/surec/hedef-ruzgar-tanimi` — rüzgâr iklimi ve hedef akış (Bölüm 3).
- `skills/benzetim/bos-alan-dogrulamasi`, `skills/benzetim/hesap-alani-ve-ag`, `skills/benzetim/sinir-kosullari-ve-kalite` — yaklaşım akışı ve bina aerodinamiği benzetimi (Bölüm 5–6); kayıt süresi ve izleme noktası şartları.
- `skills/tunel/tunel-basinc-olcumu-ve-yukler` — rüzgâr tüneli tarafındaki karşılık.
