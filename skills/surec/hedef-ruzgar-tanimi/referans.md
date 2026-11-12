# Referans: CWE ön standardı Bölüm 3 — madde tablosu

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 3. Özetler kendi cümlelerimizle yazılmıştır. "PDF sayfası" PDF sayfa sırasıdır (basılı sayfa = PDF − 18).

Tür: **ZORUNLU** = metinde "shall"; **ÖNERİ** = "should"; **YORUM** = "Commentary" paragrafı; **BİLGİ** = açıklayıcı ana metin.

Bölüm 3'te 4 PO ve 6 AC vardır: PO 3-1, 3-2, 3-3, 3-4; AC 3-1a, 3-1b, 3-1c, 3-2, 3-3, 3-4.

## §3.1 Hava sistemleri ve fırtına türleri

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §3.1 | ZORUNLU | Belirli bir risk kategorisindeki bina ve eklentilerin tasarımını destekleyen CWE çalışmaları, sahada beklenen bütün hava sistemlerinin etkisini ele alır: temel rüzgâr hızları ve ilgiliyse yön özellikleri. Yaklaşım ASCE/SEI 7-22 rüzgâr tehlike haritalarının türetilmesiyle uyumludur. | — | 31 |
| §3.1 yorum | YORUM | Gözlenen/benzetilen rüzgârların tamamının istatistiği yorulma, yaya konforu ve hava kalitesi için kullanılır; sinoptik kayıtlara genelde Weibull dağılımı uydurulur. Uç olayların istatistiği ise dayanım ve kullanılabilirlik tasarımıyla ilgilidir. | — | 31–32 |
| §3.1.1 | ZORUNLU | Saha nerede olursa olsun, her risk kategorisinde tropik dışı fırtınaların olası etkisi ele alınır. | — | 31 |
| §3.1.1 yorum | YORUM | Tropik dışı fırtınalar ekvatordan 30°'den uzak bölgelerde yıl boyu gelişebilen, sinoptik ölçekli, dönen alçak basınç sistemleridir; yüzlerce mil çapında alan kaplar, tipik olarak iki ile beş gün sürer. | Enlem > 30°; süre 2–5 gün | 31–32 |
| §3.1.2 | ZORUNLU | Kasırgaların uç koşulları belirlediği bölgelerde (belge ABD'den örnekler sayar) her risk kategorisinde kasırga etkisi ele alınır. | — | 32 |
| §3.1.2 yorum | YORUM | Kasırgalar tropik/alt tropik sularda doğan sinoptik ölçekli sistemlerdir (kuzey yarıkürede tipik Mayıs–Kasım); birkaç günden bir haftadan fazlaya sürer; başka havzalarda tayfun ya da tropikal siklon denir. | — | 32 |
| §3.1.3 | ZORUNLU | Gök gürültülü fırtına ani iniş akımlarının uç koşulları belirlediği bölgelerde (belge örnek olarak Kayalık Dağlar'ın doğusunu verir) her risk kategorisinde bu etki ele alınır. | — | 32 |
| §3.1.3 yorum | YORUM | Ani iniş akımları orta ölçekli, güçlü üç boyutlu ve zamana bağlı sistemlerdir; yayılımı birkaç mil, süresi tipik 10–30 dakikadır; özellikle zeminden ilk birkaç yüz fitte yüksek şiddetli dışa akış üretir. | Süre 10–30 dk | 32 |
| §3.1.4 | ZORUNLU | ABD'nin hortum eğilimli bölgesinde (Şekil 3-1) yer alan Risk Kategorisi III ve IV bina ve eklentilerin tasarımında hortum etkisi ele alınır (ASCE/SEI 7-22 §32.1.1). | Risk Kategorisi III, IV | 32 |
| §3.1.4 yorum | YORUM | Hortumlar daha büyük sistemler içinde gelişen, çok karmaşık üç boyutlu ve zamana bağlı olaylardır; zemin yakınında tipik birkaç yüz fit genişliktedir ve ortalama 10–30 dakika sürer. | Süre 10–30 dk | 33 |
| §3.1.5 | ZORUNLU | Topoğrafyanın etkilediği rüzgârlar gibi diğer rüzgâr türlerinin etkisi, risk kategorisinden bağımsız olarak ele alınır. ASCE/SEI 7-22 bu tür alanları Özel Rüzgâr Bölgeleri olarak tanımlar (§26.5.2). | — | 33 |
| §3.1.5 yorum | YORUM | Topoğrafya etkili rüzgârlar genelde mevsimseldir ve belirgin yönsellik gösterir; belge dünyadan yamaç aşağı rüzgâr örnekleri sayar. | — | 33 |

## §3.2 Yerel rüzgâr ikliminin değerlendirilmesi

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 3-1 (§3.2) | ZORUNLU | CWE ile rüzgâr kaynaklı yük etkileri ve tepkiler değerlendirilirken, benzetimden gelen aerodinamik veri sahaya özgü bir rüzgâr iklimi modeliyle birleştirilir. | — | 33 |
| §3.2 yorum | YORUM | Risk Kategorisi I, II, III, IV için temel hız dönüş periyotları sırasıyla 300, 700, 1 700 ve 3 000 yıldır. ASCE/SEI 7-22 tropik dışı fırtına, kasırga ve gök gürültülü fırtınayı içeren yönsüz temel hızlar ile etkili plan alanına bağlı ayrı hortum hızları verir. Seçenek olarak, ASCE/SEI 7-22 §26.5.3'e uyularak, temel hızlar uzun süreli yerel/bölgesel tam ölçek kayıtlardan, Monte Carlo yapay kayıtlarından, yeniden çözümlemeden ya da WRF modellemesinden kestirilebilir. | MRI: 300 / 700 / 1 700 / 3 000 yıl | 33 |
| §3.2.1 | ZORUNLU | Olasılıksal iklim modeli için uzun süreli tam ölçek kayıt kullanılıyorsa kayıtlar güvenilir (ör. Dünya Meteoroloji Örgütü ölçütlerine uygun) istasyonlardan alınır. | — | 33 |
| AC 3-1a (§3.2.1) | ZORUNLU | Onlarca yılı kapsayan (multidecadal) kayıtlar kullanılır; daha kısa dönem ancak gerekçelendirilip belgelenirse kabul edilir. | "Onlarca yıl" (kesin yıl sayısı verilmez) | 33 |
| §3.2.1 | ZORUNLU | Uzun süreli kayıtlardaki farklı fırtına türleri ayrıştırılır; ilgiliyse kayıtlar, istatistik çözümlemeden önce maruziyete göre düzeltilir. | — | 33 |
| AC 3-1b (§3.2.1) | ZORUNLU | Kasırga etkili bölgelerde yalnız yerel istasyon kayıtlı hızların kullanılmasına izin verilmez; havza ölçeğinde kasırga izi kayıtlarıyla Monte Carlo benzetimi yapılır. | — | 33–34 |
| AC 3-1c (§3.2.1) | ZORUNLU | Yeniden çözümleme veri kümeleri (yalnız küresel modelden ya da bölgesel modelle ölçek küçültülmüş) saha koşullarını nitelendirmek için kullanılıyorsa, başarımı meteorolojik gözlemlerle, özellikle uç olaylara dikkat edilerek çapraz geçerlenir. | — | 34 |
| §3.2.1 yorum | YORUM/ÖNERİ | Birden çok istasyonun incelenmesi önerilir. Çözümlemeden önce veri kalitesi, ölçüm donanımı ve zaman içindeki yer/tip değişiklikleri gözden geçirilmelidir; anemometre yakınındaki engeller (ör. hangar) kayıtları bozabilir. İstasyonun yukarı akışındaki z0 nitelendirilerek tropik dışı fırtına kayıtları düzgün açık araziye (ör. ASCE/SEI 7-22 Maruziyet C) taşınmalı; pürüzlülüğün zamanla değişimi (ör. kentleşme) gözetilmelidir. Topoğrafyadan etkilenen istasyon kayıtları düzeltilmelidir (§3.3.2). Kasırgada yer istasyonu tek bir gerçekleşmeyi temsil eder ve hasar/arıza ile veri kaybedebilir; uydu, dropsonde, Doppler radarı, şamandıra ağı ve uçak keşfi çok daha kapsamlı örnekleme sağlar ve benzetim teknikleri bunlara karşı geçerlenmelidir. | — | 34 |
| §3.2.2 (1) | ZORUNLU | İklim modeli, çalışma alanı için ilgili fırtına türlerinin olasılıksal birleşimidir. | — | 34 |
| §3.2.2 (2) | ZORUNLU | İklim modeli, incelenen bina(lar)ın risk kategorisiyle ilgili bütün dönüş periyodu aralığını kapsar. | — | 34 |
| §3.2.2 (3) | ZORUNLU | İklim modeli, uç rüzgâr olaylarının yönselliğinin etkisini hesaba katar. | — | 34 |
| §3.2.2 | ZORUNLU | İklim modeli, tasarım yüklerini ve yapısal tepkiyi değerlendirmek üzere benzetim çıktısıyla birleştirilmeden önce proje sahasının maruziyet(ler)ini hesaba katar (§3.3). | — | 34 |
| §3.2.2 yorum | YORUM/ÖNERİ | Ölçülen ya da yapay uzun süreli kayıtlarla hız-yön ortak olasılık dağılımı kurulabilir; iki ya da beş parametreli Weibull ile yaklaşık temsil yaygındır; yönlü Weibull parametreleri aerodinamik veriyle ör. yukarı geçiş yöntemiyle birleştirilir. Dağılım kuyruğunun uyumuna büyük özen gösterilmelidir. Uç hız dağılımı gerekiyorsa uygun uç değer çözümlemesi kullanılmalıdır; bağımsız fırtınalar yöntemi en sağlam yaklaşımlardan sayılır. Karma iklimde her fırtına türünün uç dağılımı ayrı değerlendirilip sonra birleştirilmelidir. Topoğrafyanın yerel rejimi etkilediği yerlerde özel değerlendirme yapılmalıdır. | — | 34–35 |

## §3.3 Hedef rüzgâr akış koşullarının tanımı

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 3-2 (§3.3) | ZORUNLU | Hesaplama alanının gelen konumundaki sahaya özgü hedef rüzgâr akış koşulları yön yön türetilir; sonra benzetimlerde aynı konumda tutturulur. | — | 35 |
| PO 3-3 / AC 3-3 (§3.3.1) | ZORUNLU | Proje sahasının yukarı akışındaki aerodinamik pürüzlülük uzunluğu nitelendirilerek maruziyet(ler) belirlenir. (Metin PO ve AC'yi tek cümlede birlikte verir.) | Sayısal z0 değeri verilmez | 35 |
| §3.3.1 | ZORUNLU | İlgili olduğu yerde bu süreç topoğrafya etkilerini gereğince gözetir. | — | 35 |
| AC 3-2 (§3.3.1) | ZORUNLU | Pürüzlülük değerlendirmesinin sonucu, iklim modelini sahaya taşımak ve şu hedef parametreleri belirlemek için kullanılır: (1) ortalama rüzgâr hızı profili; (2) türbülans şiddeti profili; (3) türbülans tümlev uzunluk ölçeği profili; (4) hız çalkantılarının güç spektral yoğunlukları; (5) ilgili çapraz spektral yoğunluklar ve Reynolds gerilmeleri. (2)–(4), ilgili yük mekanizmalarını doğru kestirmek için gereken bileşenler içindir. | Sayısal tolerans verilmez | 35 |
| §3.3.1 | ZORUNLU | Bu hedef parametrelerin boş alan benzetimlerinde ne ölçüde tutturulduğu teknik raporda belgelenir ve tartışılır. | — | 35 |
| §3.3.1.1 | ZORUNLU | Tropik dışı fırtınalar için, boş alan benzetiminde gelen konumda tutturulacak hedef koşulları tanımlamak üzere uygun bir atmosferik sınır tabaka modeli kullanılır. | — | 35 |
| §3.3.1.1 yorum – ortalama hız | YORUM | Ortalama hızın yükseklikle değişimi için çeşitli bağıntılar vardır (kuvvet yasası, logaritmik, logaritmik-doğrusal, parabolik düzeltmeli logaritmik); bazıları tüm sınır tabakada, bazıları yalnız yüzey tabakasında geçerlidir. Nötr koşullar, ekvatordan 30°'den uzak bölgeler, kuvvetli ve kayma baskın tropik dışı rüzgâr, düz ve düzgün pürüzlü arazi için Harris ve Deaves (1979) bağıntısı (Denklem 3-1) kullanılabilir. | "Kuvvetli" = 33 ft (~10 m) yükseklikte ortalama hız > 33 ft/s (~10 m/s); enlem > 30° | 35–36 |
| §3.3.1.1 yorum – Denklem 3-1 terimleri | YORUM | Sürtünme hızı u*, von Kármán sabiti κ, pürüzlülük uzunluğu z0 (değer seçimi için ASCE/SEI 49-21) ve gradyan yüksekliği zg cinsindendir. Belirli yüksekliklerin altında üst mertebe terimler ihmal edilebilir. | κ = 0,4; z < 1 000 ft (~300 m): ikinci ve üst mertebe terimler ihmal; z < 100 ft (~30 m): birinci mertebe terim de ihmal | 36 |
| §3.3.1.1 yorum – Denklem 3-2, 3-3 | YORUM | Gradyan yüksekliği sürtünme hızının Coriolis parametresine oranından kestirilir (kaynakta zg = u*/(6f) olarak okunuyor); f = 2ω sinφ, ω yerin açısal hızı, φ enlem. | ω = 7,27 × 10⁻⁵ rad/s | 36 |
| §3.3.1.1 yorum – pürüzlülük değişimi (hız) | YORUM | Yukarı akıştaki z0 değişiminin ortalama hız üzerindeki denge dışı etkisi için Deaves (1981a) yaklaşımı kullanılabilir. | — | 36 |
| §3.3.1.1 yorum – σu, Iu | YORUM | Boyuna türbülans standart sapması profili için ESDU Item 83045 bağıntısı (Denklem 3-4) verilir; η(z) = 1 − z/zg (3-5) ve yüzey Rossby sayısı Ro = u*/(f·z0) (3-6) kullanılır. Boyuna türbülans şiddeti Iu(z) = σu(z)/U(z) (3-7). | Denklem 3-4 katsayıları kaynak metinde okunamıyor | 36 |
| §3.3.1.1 yorum – pürüzlülük değişimi (σu) | YORUM | σu üzerindeki denge dışı etki için Deaves (1981b) kullanılabilir. | — | 37 |
| §3.3.1.1 yorum – yanal/düşey | YORUM | Yanal ve düşey türbülans standart sapması profilleri (ve bunlardan türbülans şiddetleri) için ESDU Item 85020 bağıntıları kullanılabilir. | — | 37 |
| §3.3.1.1 yorum – Lu^x | YORUM | Boyuna tümlev uzunluk ölçeğinin x doğrultusundaki profili için ESDU Item 85020 bağıntısı (Denklem 3-8) verilir; A(z) (3-9), Kolmogorov parametresi K(z) (3-10), enerji yitim hızı ε(z) (3-11) ve dU/dz (3-12) ile birlikte. | Katsayılar kaynak metinde okunamıyor | 37 |
| §3.3.1.1 yorum – diğer uzunluk ölçekleri | YORUM | Diğer sekiz tümlev uzunluk ölçeğinin profilleri, yüksek frekans aralığı için ESDU Item 86010'da verilir. | Yüksek frekans aralığı: n·z/U(z) > 0,1 (kaynakta bozuk yazım; bu biçimde okunuyor) | 37 |
| §3.3.1.1 yorum – spektrumlar | YORUM | Boyuna spektrum Suu için ESDU Item 85020 (Denklem 3-13, yüksek frekans aralığı); yanal Svv için Kaimal vd. (1972); düşey Sww için Lumley ve Panofsky (1964); yanal ve düşey için seçenek Solari ve Piccardo (2001). | Denklem 3-13 üssü/katsayısı kaynak metinde güvenle okunamıyor | 37–38 |
| §3.3.1.1 yorum – pürüzlülük değişimi (ölçek, spektrum) | YORUM | Uzunluk ölçekleri ve spektral yoğunluklar üzerindeki denge dışı etki için ESDU Item 85020'de özetlenen yaklaşım kullanılabilir. | — | 38 |
| §3.3.1.1 yorum – Reynolds gerilmesi | YORUM | Reynolds gerilme tensörünün en baskın bileşeni, akış doğrultusu-düşey düzlemdeki kayma gerilmesini temsil eden u′w′'dir; eş-spektrumun (çapraz spektrumun gerçek kısmı) frekans üzerinden tümleviyle tanımlanır (Denklem 3-14, 3-15). | — | 38 |
| §3.3.1.1 yorum – yüksek binalar | ÖNERİ (yorum içinde "should") | Yüksek binalarda boş alan benzetiminde şunların doğru nitelendirilmesine özel özen gösterilmelidir: ortalama hız profili; türbülans şiddeti (özellikle boyuna, yanal); tümlev uzunluk ölçekleri (özellikle Lu^z, Lv^z, Lu^y, Lv^y, Lv^x); spektrumlar (özellikle boyuna, yanal); u′w′ bileşeni. | — | 38 |
| §3.3.1.2 | ZORUNLU | Kasırgalar için, boş alan benzetiminde gelen konumda tutturulacak hedef koşulları tanımlamak üzere uygun bir kasırga sınır tabakası modeli kullanılır. | — | 38 |
| §3.3.1.2 yorum | YORUM | Gradyan kasırga rüzgâr alanının erken temsilleri Batts vd. (1980) ve Holland (1980) modellerindedir. Kasırga sınır tabakasının alt kısmında ortalama profil logaritmik yasadan ihmal edilebilir ölçüde sapar; okyanus üstü tam ölçek ölçümler bunu doğrular. Bu yüksekliğin üstünde daha iyi doğruluk için Vickery vd. (2009) logaritmik-kareli modeli (Denklem 3-16) kullanılabilir. Okyanus üstünde gradyan yüksekliği, atalet kararlılığı parametresi I'ye bağlı bir bağıntıyla (3-17) kestirilir; I, Coriolis parametresi, gradyan yüksekliğindeki hız ve fırtına merkezine radyal uzaklık r cinsinden yaklaşık verilir (3-18). | Logaritmik yasa geçerliliği: alt 1 000–1 300 ft (~300–400 m). Denklem 3-16…3-18 katsayıları kaynak metinde güvenle okunamıyor | 38 |
| PO 3-4 (§3.3.2) | ZORUNLU | Dağ, tepe gibi topoğrafik özellikler saha akış koşullarını etkileyebiliyorsa, çalışma alanına yaklaşan akışın uzay ve zamandaki değişimini nicelemek için benzetim yapılır. | — | 39 |
| AC 3-4 (§3.3.2) – Yöntem 1 | ZORUNLU | Topoğrafya, binaların açıkça modellendiği alan kısmının ötesinde ise, ana benzetimlerin sonradan yeniden üretmesi gereken rüzgâr özelliklerini türetmek için ayrı benzetimler yapılır ("Topoğrafya Yöntemi 1", Şekil 3-2). | — | 39 |
| AC 3-4 (§3.3.2) – Yöntem 2 | ZORUNLU | Karmaşık üç boyutlu topoğrafya sahanın ayrılmaz parçası ise (ör. boğaz içinde ya da dik dağ yamacında), bu özellikler çalışma bölgesinin parçası olarak açıkça modellenir ve etkileri ana benzetimlerde belirlenir ("Topoğrafya Yöntemi 2", Şekil 3-2). | — | 39 |
| §3.3.2 yorum | YORUM/ÖNERİ | Yöntem 1, "Adım 0"da gelen konumda ters akışlı ya da belirli yüksekliklerde hızlanma/eksiklik içeren profiller üretebilir; bunları "Adım 1"de düz arazi üzerinde yeniden üretmek zor olabilir. Topoğrafya çalışmasında yüzey için uygun aerodinamik pürüzlülük seçimine özen gösterilmeli; mümkünse sonuçlar güvenilir uzun süreli LiDAR ölçümleriyle karşılaştırılmalıdır. Bölgesel/yerel topoğrafya çalışmaları WRF ile bağlaşabilir; iki modelin arayüzü özel dikkat ister. | — | 39 |
| §3.3.3 | BİLGİ | Sinoptik olmayan rüzgârlar için birçok analitik model geliştirilmiştir; CWE'nin bu alanda potansiyeli büyüktür ancak yayım tarihinde kapsamlı hedef akış parametrelerinin tanımı gibi önemli güçlükler çözülmemiştir. Bu maddede numaralı PO/AC ve "shall" yoktur. | — | 40 |
| §3.3.3 yorum – ani iniş akımı | YORUM | Ani iniş akımı dışa akış bölgesinde hız yalnız zeminden birkaç yüz fite kadar artar, üstünde azalır (Şekil 3-3). Anılan modeller: Oseguera ve Bowles (1988), Vicroy (1991) ile Oseguera-Bowles-Vicroy modeli; Wood vd. (2001) uzayda durağan ani iniş akımının ortalama radyal hız profili için görgül model (Denklem 3-19; Umax profildeki en büyük yatay ortalama hız, δ hızın Umax'ın yarısına düştüğü yükseklik). Xhelaj vd. (2020): Wood modeli en büyük radyal hız zemine yakınken, Oseguera-Bowles-Vicroy daha yüksekteyken daha uygundur. Holmes ve Oliver (2000): durağan radyal hız ile fırtına hücresinin öteleme hareketinin vektör toplamı. Ötelenen hücre ile içinde bulunduğu sınır tabaka rüzgârı arasındaki ilişki ve bu olayların türbülans özellikleri henüz tam bilinmemektedir. | Denklem 3-19 katsayıları kaynak metinde güvenle okunamıyor | 40–41 |
| §3.3.3 yorum – hortum | YORUM | Hortumlar tek hücreli (orta dönme oranları) ya da iki hücreli (çok daha büyük dönme oranları) girdap yapısında olabilir. Hedef olarak çeşitli radyal uzaklıklarda üç hız bileşeninin düşey profilleri gerekir; en büyük ortalama teğetsel hız, bunun radyal konumu ve zeminden yüksekliği temel hedef parametrelerdir. Nitelikli tam ölçek ölçüm azdır; radar ölçümlerinde zemine en yakın kısım genelde eksiktir. Anılan modeller: Fujita (1978), Xu ve Hangan (2009) (görgül); Baker ve Sterling (2017) (denklem tabanlı). En yalın model Rankine girdabıdır (Denklem 3-20): içte katı cisim dönmesi (hız yarıçapla orantılı), dışta kuvvet yasasıyla azalan bölge. | Radar verisinde eksik kalan kısım: zeminden ilk ~100 ft (~30 m); azalma üssü α tipik −0,5 ile −0,7 arası | 41 |

## Denklem dökümü (PDF s. 36–41)

Kaynak düz metinde denklemler PDF çıkarımı nedeniyle bozuktur. Aşağıda yalnız **ne için** oldukları ve güvenle okunabilen parçalar verilmiştir. Katsayıları asıl PDF'ten al; buradan ya da bellekten tamamlama.

| Denklem | Konu | Kaynakta güvenle okunan | Durum |
|---|---|---|---|
| 3-1 | Ortalama hız profili (Harris ve Deaves) | u*/κ çarpanı, ln(z/z0) ana terimi ve z/zg'nin artan kuvvetlerinde düzeltme terimleri | Düzeltme katsayıları okunamıyor |
| 3-2 | Gradyan yüksekliği | zg = u*/(6f) | Okunuyor (bozuk dizilim) |
| 3-3 | Coriolis parametresi | f = 2ω sinφ; ω = 7,27 × 10⁻⁵ rad/s | Okunuyor |
| 3-4 | σu(z) (ESDU 83045) | u*, η(z), ln(z/z0), ln(Ro) içerir | Katsayılar okunamıyor |
| 3-5 | η(z) | η = 1 − z/zg | Okunuyor |
| 3-6 | Yüzey Rossby sayısı | Ro = u*/(f·z0) | Okunuyor |
| 3-7 | Boyuna türbülans şiddeti | Iu(z) = σu(z)/U(z) | Okunuyor |
| 3-8 | Lu^x(z) (ESDU 85020) | A(z), σu(z), K(z), ε(z) cinsinden | Üsler güvenle okunamıyor |
| 3-9 | A(z) | η(z)'ye bağlı | Katsayılar okunamıyor |
| 3-10 | Kolmogorov parametresi K(z) | Ro ve z/zg'ye bağlı | Okunamıyor |
| 3-11 | Enerji yitim hızı ε(z) | u*², η(z)² ve dU/dz'ye bağlı (yaklaşık) | Kısmen okunuyor |
| 3-12 | dU/dz | 3-1'in türevi | Katsayılar okunamıyor |
| 3-13 | Boyuna spektrum (yüksek frekans) | n·Suu/σu², A(z) ve n·Lu^x/U cinsinden | Üs güvenle okunamıyor |
| 3-14, 3-15 | u′w′ ve eş-spektrum | u′w′ = eş-spektrumun 0'dan sonsuza frekans tümlevi; eş-spektrum = çapraz spektrumun gerçek kısmı | Okunuyor |
| 3-16 | Kasırga ortalama hız profili (Vickery vd.) | u*/κ çarpanı, ln(z/z0) ve (z/zg)² düzeltmesi | Katsayı güvenle okunamıyor |
| 3-17 | Okyanus üstü kasırga gradyan yüksekliği | I'ye bağlı | Okunamıyor |
| 3-18 | Atalet kararlılığı parametresi I | f, U(zg) ve r cinsinden | Tam biçim okunamıyor |
| 3-19 | Ani iniş akımı ortalama radyal hız profili (Wood vd.) | Umax, z/δ ve hata fonksiyonu (erf) içerir | Katsayılar okunamıyor |
| 3-20 | Rankine girdabı teğetsel hızı | r ≤ R: Uθ,max·(r/R); r > R: Uθ,max·(r/R)^α | Okunuyor; α tipik −0,5 … −0,7 |

## Belirsiz / kaynakta eksik noktalar

- Şekil 3-1 (hortum eğilimli bölge), Şekil 3-2 (topoğrafya yöntemleri) ve Şekil 3-3 (ani iniş akımı yapısı) kaynak düz metinde yalnız başlık olarak vardır.
- §3.3.2 yorumundaki "Adım 0" terimi Bölüm 3–4 ana metninde tanımlanmaz; Şekil 3-2'de tanımlı olduğu anlaşılıyor (topoğrafya ön benzetimi), ancak şekil içeriği doğrulanamadı.
- AC 3-2 ile AC 3-3'ün metindeki sırası tersine görünür (önce PO 3-3 / AC 3-3, sonra AC 3-2); AC 3-2 köşeli ayracı beş parametrelik listenin başındadır ve PO 3-2'ye bağlıdır.
- Bölüm 3, hedeflerin tutturulmasına ilişkin sayısal tolerans vermez.
