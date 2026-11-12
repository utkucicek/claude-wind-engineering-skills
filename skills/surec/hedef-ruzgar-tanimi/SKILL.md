---
name: hedef-ruzgar-tanimi
description: "ASCE CWE ön standardı Bölüm 3'e göre rüzgâr iklimi modeli (wind climate model) ve gelen konumdaki (incident location) hedef rüzgâr akış koşulları (target wind flow conditions) tanımlanacaksa kullanılır: fırtına türleri, ortalama hız profili (mean wind speed profile), türbülans şiddeti (turbulence intensity), tümlev uzunluk ölçeği (integral length scale), güç spektrumu (power spectral density), Reynolds gerilmesi, pürüzlülük uzunluğu z0 (roughness length), maruziyet değişimi (exposure change) ve topoğrafya etkisi."
---

# Hedef rüzgâr tanımı (Bölüm 3)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 3 (Rüzgâr iklimi ve rüzgâr akış koşullarının nitelendirilmesi). Madde tablosu ve denklem dökümü: `referans.md`. Sayfa numaraları PDF sayfa sırasıdır (basılı sayfa = PDF − 18).

## Ne zaman kullanılır

- LES çalışmasından önce "boş alanda neyi tutturmam gerekiyor?" sorusu yanıtlanacaksa: hangi profiller, hangi bileşenler, hangi konumda.
- Saha için rüzgâr iklimi modeli kurulacak ya da var olan model denetlenecekse (veri kaynağı, fırtına ayrımı, yönsellik, dönüş periyodu aralığı).
- Hangi fırtına türünün (tropik dışı fırtına, kasırga, gök gürültülü fırtına, hortum, topoğrafya etkili rüzgâr) hesaba katılması gerektiği sorulduğunda.
- Yukarı akışta pürüzlülük değişimi ya da tepe/dağ etkisi varken hedefin nasıl tanımlanacağı sorulduğunda.

Kullanma: hedefin benzetimde ne ölçüde tutturulması gerektiğine ilişkin sayısal toleranslar Bölüm 3'te yoktur; bunlar yaklaşım akışı benzetimi becerisine (Bölüm 5) aittir.

## Temel fikir

Bölüm 3 iki ayrı ürünü ister:

1. **Rüzgâr iklimi modeli (wind climate model):** sahadaki rüzgâr hızı ve yönünün olasılıksal tanımı. Benzetimden gelen aerodinamik veriyle sonradan birleştirilir (PO 3-1).
2. **Hedef rüzgâr akış koşulları (target wind flow conditions):** her rüzgâr yönü için, hesaplama alanının gelen konumunda sağlanması gereken profil ve türbülans özellikleri (PO 3-2). Aynı konumda benzetimde tutturulur.

Gelen konum (incident location): alanda bina ya da topoğrafyanın eklendiği en yukarı akış noktası (§1.8, §4.1). Hedef, giriş sınırında değil burada tanımlanır.

## Adım adım

1. **Sahayı etkileyen hava sistemlerini belirle (§3.1).** Risk kategorisine göre sahada beklenen bütün hava sistemleri ele alınır: temel rüzgâr hızları ve ilgiliyse yön özellikleri.
   - Tropik dışı fırtınalar (extratropical storms): yer ve risk kategorisi ne olursa olsun (§3.1.1).
   - Kasırgalar (hurricanes): kasırga etkili bölgelerde her risk kategorisi (§3.1.2).
   - Gök gürültülü fırtınalar (thunderstorms): bunların belirleyici olduğu bölgelerde her risk kategorisi (§3.1.3).
   - Hortumlar (tornadoes): hortum eğilimli bölgede Risk Kategorisi III ve IV (§3.1.4).
   - Topoğrafya etkili diğer rüzgârlar (ör. yamaç aşağı rüzgârlar): her risk kategorisi (§3.1.5).
   Belgedeki bölge örnekleri ABD'ye özgüdür; başka ülkede karşılığını yerel yönetmelikten ve iklim verisinden bul, belgeye atfetme.
2. **Rüzgâr iklimi modelinin veri kaynağını seç (§3.2, §3.2.1).** Seçenekler (yorumda sayılanlar): yönetmelik temel hızları; uzun süreli yerel/bölgesel tam ölçek kayıtlar; Monte Carlo benzetimli yapay kayıtlar; yeniden çözümleme (reanalysis) verisi; WRF modellemesi.
   - Ölçüm kaydı kullanılıyorsa güvenilir (ör. Dünya Meteoroloji Örgütü ölçütlerine uygun) istasyon ve onlarca yıllık kayıt; daha kısa süre gerekçelendirilip belgelenir (AC 3-1a).
   - Fırtına türleri ayrıştırılır; gerekiyorsa kayıtlar istatistik çözümlemeden önce maruziyete göre düzeltilir (§3.2.1).
   - Kasırga etkili bölgede yalnız yerel istasyon hızlarıyla yetinilmez; havza ölçeğinde kasırga izleriyle Monte Carlo benzetimi yapılır (AC 3-1b).
   - Yeniden çözümleme verisi kullanılıyorsa, özellikle uç olaylarda, meteorolojik gözlemlerle çapraz geçerlenir (AC 3-1c).
3. **Rüzgâr iklimi modelini kur (§3.2.2).** Model şunları sağlar: ilgili fırtına türlerinin olasılıksal birleşimi; binanın risk kategorisine karşılık gelen bütün dönüş periyodu aralığı; uç olayların yönselliği. Benzetim çıktısıyla birleştirilmeden önce saha maruziyetini hesaba katar.
4. **Yukarı akış pürüzlülüğünü nitelendir (§3.3.1; PO 3-3 / AC 3-3).** Her yön için aerodinamik pürüzlülük uzunluğu (z0) belirlenerek maruziyet(ler) saptanır; ilgiliyse topoğrafya etkisi gözetilir. Bu değerlendirme hem iklim modelinin sahaya taşınmasında hem hedef parametrelerin seçiminde kullanılır.
5. **Hedef parametreleri yön yön çıkar (§3.3.1; AC 3-2).** Beş kalem:
   1. ortalama rüzgâr hızı profili,
   2. türbülans şiddeti profili (yük mekanizması için gereken bileşenler),
   3. türbülans tümlev uzunluk ölçeği profili (gereken bileşenler),
   4. hız çalkantılarının güç spektral yoğunlukları (gereken bileşenler),
   5. ilgili çapraz spektral yoğunluklar ve Reynolds gerilmeleri.
6. **Uygun sınır tabaka modelini seç.** Tropik dışı fırtına için atmosferik sınır tabaka modeli (§3.3.1.1); kasırga için kasırga sınır tabakası modeli (§3.3.1.2). Belge belirli bir modeli zorunlu tutmaz; "uygun bir model" ister. Yorumda verilen seçenekler aşağıdaki tabloda.
7. **Maruziyet değişimini hesaba kat.** Yukarı akışta pürüzlülük değişiyorsa denge dışı etkiler için yorumda anılan yöntemler kullanılabilir (aşağıdaki tablo). Bu bir öneridir, zorunlu değil.
8. **Topoğrafyayı ele al (§3.3.2; PO 3-4 / AC 3-4).** Topoğrafya saha akışını etkileyebiliyorsa benzetimle nicelenir:
   - Topoğrafya, binaların açıkça modellendiği alanın **dışında** ise: ayrı benzetimlerle, ana benzetimin yeniden üretmesi gereken rüzgâr özellikleri çıkarılır ("Topoğrafya Yöntemi 1").
   - Karmaşık üç boyutlu topoğrafya sahanın **ayrılmaz parçası** ise (boğaz içi, dik yamaç): çalışma bölgesinin parçası olarak açıkça modellenir ve etkisi ana benzetimde belirlenir ("Topoğrafya Yöntemi 2").
9. **Sinoptik olmayan rüzgârlar gerekiyorsa (§3.3.3).** Belge burada zorunlu ölçüt koymaz; kapsamlı hedef parametre tanımının henüz çözülmediğini söyler. Yorumdaki modeller yalnız bilgi amaçlıdır.
10. **Belgele.** Hedef parametrelerin boş alan benzetiminde ne ölçüde tutturulduğu teknik raporda belgelenir ve tartışılır (§3.3.1).

## Hangi büyüklük hangi kaynaktan (tümü yorum niteliğinde seçenek)

| Büyüklük | Belgede anılan kaynak / model | Geçerlilik notu (belgeye göre) | Denklem |
|---|---|---|---|
| Ortalama hız profili U(z), tropik dışı | Harris ve Deaves (1979) | Nötr atmosfer, ekvatordan 30°'den uzak, kuvvetli rüzgâr (10 m'de ortalama hız > ~10 m/s), düz ve düzgün pürüzlü arazi. ~300 m altında ikinci ve üst mertebe terimler, ~30 m altında birinci mertebe terim de ihmal edilebilir. | 3-1 |
| Gradyan yüksekliği zg | Sürtünme hızı ve Coriolis parametresine bağlı bağıntı | f = 2ω sinφ; ω = 7,27 × 10⁻⁵ rad/s | 3-2, 3-3 |
| von Kármán sabiti κ | — | 0,4 alınır | 3-1 açıklaması |
| z0 değeri seçimi | ASCE/SEI 49-21 | Uygun değer seçimi için kılavuz | — |
| Pürüzlülük değişiminin ortalama hıza etkisi | Deaves (1981a) | Denge dışı etkiler | — |
| Boyuna türbülans standart sapması σu(z) | ESDU Item 83045 | Kuvvetli tropik dışı rüzgâr, düz ve düzgün pürüzlü arazi | 3-4 – 3-6 |
| Boyuna türbülans şiddeti Iu(z) | σu(z) / U(z) | — | 3-7 |
| Pürüzlülük değişiminin σu'ya etkisi | Deaves (1981b) | Denge dışı etkiler | — |
| Yanal ve düşey σv, σw (dolayısıyla Iv, Iw) | ESDU Item 85020 | — | — |
| Boyuna tümlev uzunluk ölçeği Lu^x(z) | ESDU Item 85020 | Kuvvetli tropik dışı rüzgâr, düz ve düzgün pürüzlü arazi | 3-8 – 3-12 |
| Diğer sekiz tümlev uzunluk ölçeği | ESDU Item 86010 | Yüksek frekans aralığı | — |
| Boyuna spektrum Suu(n, z) | ESDU Item 85020 | Yüksek frekans aralığı | 3-13 |
| Yanal spektrum Svv | Kaimal vd. (1972); seçenek: Solari ve Piccardo (2001) | — | — |
| Düşey spektrum Sww | Lumley ve Panofsky (1964); seçenek: Solari ve Piccardo (2001) | — | — |
| Pürüzlülük değişiminin uzunluk ölçeği ve spektruma etkisi | ESDU Item 85020 | Denge dışı etkiler | — |
| Reynolds gerilmesi u′w′ | Eş-spektrumun (co-spectrum) frekans üzerinden tümlevi | Gerilme tensörünün en baskın bileşeni | 3-14, 3-15 |
| Kasırga ortalama hız profili | Alt ~300–400 m'de logaritmik yasa; üstü için Vickery vd. (2009) logaritmik-kareli model | Okyanus üstü gradyan yüksekliği atalet kararlılığı parametresine bağlı | 3-16 – 3-18 |
| Topoğrafya etkisi | Ayrı benzetim (Yöntem 1) ya da açık modelleme (Yöntem 2); isteğe bağlı LiDAR karşılaştırması, WRF bağlaşımı | — | — |
| İklim modeli: temel hızlar | ASCE/SEI 7-22 (yönsüz temel hızlar; ayrı hortum hızları) ya da §26.5.3'e uyularak yerel kayıt / Monte Carlo / yeniden çözümleme / WRF | Risk Kategorisi I–IV için dönüş periyotları 300, 700, 1 700, 3 000 yıl | — |
| Uç değer çözümlemesi | Bağımsız fırtınalar yöntemi (Cook 1982; Harris 1999); karma iklimde fırtına türleri ayrı değerlendirilip birleştirilir (Gomes ve Vickery 1978) | — | — |
| Hız-yön ortak dağılımı | İki ya da beş parametreli Weibull; yukarı geçiş yöntemiyle birleştirme | Dağılım kuyruğunun uyumu kritik | — |

Denklemlerin açık biçimi kaynak düz metinde bozuk çıkmıştır; katsayıları buradan ya da bellekten yazma, asıl PDF'ten (s. 36–38) al. Ayrıntı: `referans.md`.

## Yüksek binalarda özel dikkat (§3.3.1.1 yorum)

Yüksek binalarda boş alan benzetiminde şunların hepsinin doğru nitelendirilmesi özellikle önerilir: ortalama hız profili; türbülans şiddeti (özellikle boyuna ve yanal); tümlev uzunluk ölçekleri (özellikle Lu^z, Lv^z, Lu^y, Lv^y, Lv^x); spektrumlar (özellikle boyuna ve yanal); u′w′ Reynolds gerilmesi.

## Zorunlu şartlar

- §3.1: Risk kategorisine göre sahada beklenen bütün hava sistemleri ele alınır.
- §3.1.1–§3.1.5: fırtına türüne göre kapsam (yukarıdaki 1. adım).
- PO 3-1 (§3.2): Aerodinamik veri, sahaya özgü rüzgâr iklimi modeliyle birleştirilir.
- AC 3-1a (§3.2.1): Güvenilir istasyon; onlarca yıllık kayıt ya da gerekçeli ve belgeli kısa süre.
- §3.2.1: Fırtına ayrımı; gerekiyorsa maruziyet düzeltmesi, istatistikten önce.
- AC 3-1b (§3.2.1): Kasırga bölgesinde yalnız yerel istasyon verisi yasak; havza ölçekli Monte Carlo.
- AC 3-1c (§3.2.1): Yeniden çözümleme verisi gözlemle çapraz geçerlenir.
- §3.2.2: İklim modeli üç koşulu sağlar (olasılıksal birleşim, tüm dönüş periyodu aralığı, yönsellik) ve saha maruziyetini içerir.
- PO 3-2 (§3.3): Hedef koşullar gelen konumda yön yön türetilir ve benzetimde aynı konumda tutturulur.
- PO 3-3 / AC 3-3 (§3.3.1): Yukarı akış z0 nitelendirilir, maruziyet belirlenir.
- AC 3-2 (§3.3.1): Beş hedef parametre belirlenir; tutturma derecesi raporda belgelenir.
- §3.3.1.1 / §3.3.1.2: Uygun atmosferik / kasırga sınır tabakası modeli kullanılır.
- PO 3-4 / AC 3-4 (§3.3.2): Topoğrafya etkisi benzetimle nicelenir; konumuna göre Yöntem 1 ya da Yöntem 2.

## Sık yapılan hatalar

- Hedefi giriş sınırında tanımlamak. Hedef gelen konumdadır; girişten oraya kadar profil bozulur.
- Yalnız ortalama hız ve Iu ile yetinmek. AC 3-2 uzunluk ölçeği, spektrum, çapraz spektrum ve Reynolds gerilmesini de ister (gereken bileşenler için).
- Tek bir profil kullanıp bütün yönlere uygulamak. Türetme yön yön yapılır.
- Yorumdaki Harris-Deaves / ESDU bağıntılarını "zorunlu" diye sunmak. Zorunlu olan "uygun bir model" kullanmaktır; bağıntılar örnek seçenektir.
- Bağıntıları geçerlilik koşulları dışında kullanmak (zayıf rüzgâr, ekvatora yakın enlem, düzgün olmayan arazi).
- Bölüm 3'e sayısal tolerans atfetmek (ör. "profil %x içinde olmalı"). Bölüm 3'te böyle bir eşik yoktur.
- Kasırga bölgesinde yalnız havaalanı istasyon verisiyle uç değer çözümlemesi yapmak.
- Fırtına türlerini ayırmadan tek dağılım uydurmak; karma iklimde türler ayrı değerlendirilip birleştirilmelidir (yorum).
- İstasyon çevresindeki pürüzlülüğün zamanla değişimini ve yakın engelleri gözden kaçırmak (yorum).
- Sahanın içindeki karmaşık topoğrafyayı düz arazi + ayrı benzetimle geçiştirmek; bu durumda açık modelleme (Yöntem 2) gerekir.
- Yöntem 1'de ters akış ya da belirli yüksekliklerde hızlanma/eksiklik içeren profillerin düz arazi üzerinde yeniden üretilmesinin zor olduğunu hesaba katmamak (yorum).
- Hortum ya da ani iniş akımı için belgede kabul ölçütü varmış gibi davranmak. §3.3.3 yalnız değerlendirme ve yorum içerir.

## İlgili beceriler

- `cwe-kapsam-ve-surec` — kapsam, araç seçimi, iki adımlı süreç, gelen konum tanımı.
- Yaklaşım akışı benzetimi (Bölüm 5) becerisi — hedefin boş alanda tutturulması ve kabul ölçütleri.
- Bina aerodinamiği benzetimi (Bölüm 6) ve yük/tepki birleştirme (Bölüm 7 ve sonrası) becerileri — iklim modelinin aerodinamik veriyle birleştirilmesi.
