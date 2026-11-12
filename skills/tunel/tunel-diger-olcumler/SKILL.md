---
name: tunel-diger-olcumler
description: Rüzgâr tünelinde basınç deliği dışındaki ölçümler ASCE/SEI 49-21'e göre sorulduğunda kullan; yüksek frekanslı kuvvet terazisi (high-frequency force balance, HFFB), doğrudan yük ölçümü ve rijit kesit modeli (section model), esnek yapılarda dinamik tepki çözümlemesi, aeroelastik model (aeroelastic model; vortex shedding, galloping, flutter), ürün deneyleri (products, solar arrays), kar yükü model çalışmaları (snow load), hortum/aşağı patlama (tornado, downburst) çerçevesi ve yaya düzeyi rüzgârın (pedestrian wind) kapsam durumu.
---

# Tünelde diğer ölçümler — ASCE/SEI 49-21

Kaynak: ASCE/SEI 49-21 (2021 baskısı). Standart metni §1–§8, yorum §C1–§C8. Sayfa numaraları PDF sayfa sırasıdır. Ayrıntılı tablo: `referans.md`.

## Ne zaman kullanılır

- Bir raporda kuvvet terazisi (HFFB), yük hücresi, kesit modeli veya aeroelastik model kullanılmışsa ve bunların şartları denetlenecekse.
- Yapının rijit / esnek / aeroelastik sınıflarından hangisine girdiği ve hangi deney türünün gerektiği sorulduğunda.
- Çatı güneş paneli gibi seri üretim ürünler için genel katsayı deneyi, kar yükü model çalışması veya hortum yükleri sorulduğunda.
- "Yaya düzeyi rüzgâr konforu bu standartta var mı?" sorusunda.

## Yapı sınıfları (§1.4, §C1.4)

- **Rijit yapı:** atalet yükü etkileri önemsiz → Bölüm 3.
- **Esnek yapı:** atalet yükü etkileri önemli, ama belirgin aeroelastik davranış beklenmiyor → Bölüm 4 (Bölüm 3 şartları da geçerli).
- **Aeroelastik yapı:** aerodinamik kuvvetler yapının kendi hareketinden etkileniyor → Bölüm 5.
- Standart bu sınıfların frekans sınırlarını tanımlamaz; yorum, yalnız frekansa bakılmamasını, deneyim ve tam ölçek başarımın da gözetilmesini önerir.

## Adım adım

1. **Sınıfı ve deney türünü seç.** Ampirik ön değerlendirme veya deneyim aerodinamik kararsızlık ya da yüklerin aeroelastik büyümesi olasılığını gösteriyorsa aeroelastik model deneyi zorunludur (§5.1). Aksi hâlde rijit model üzerinde HFFB veya yüksek frekanslı basınç integrasyonu yeterlidir (§4.2).
2. **HFFB (§4.2.1, §3.4.2).** Model + terazi birleşik sisteminin yanal ve burulma temel frekansları kalibrasyonda belirlenir; bu frekansların veriyi kirletmemesi sağlanır; sistem mekanik titreşimden arınmış olmalıdır. Mod biçimi ile ölçülen yük arasında yalınlaştırılmış bağıntı varsayılıyorsa gerçek mod biçimlerinin bundan sapmasının etkisi çözümlemede gözetilir.
3. **Doğrudan yük ölçümü ve kesit modeli (§3.4.2, §3.4.2.1).** Birleştirilecek bütün yük ölçümleri eşzamanlı alınır. Rijit kesit modeli boyunca sürekli geometride olmalı, tipik olmayan ayrıntılardan kaçınmalı ve §8.1 geometri şartlarını sağlamalıdır.
4. **Dinamik çözümleme (§4.1, §4.3).** Örnekleme hızı ve süresi rastgele titreşim kuramına dayalı yöntemler için uygun veri verecek biçimde seçilir. Frekans veya zaman tanım alanında çözümlemeye; sonuçların eşdeğer statik yük ya da doğrudan dinamik tepki olarak sunulmasına izin vardır.
5. **Aeroelastik model (§5.2).** Kütle, rijitlik ve sönüm (veya aralıkları) kabul görmüş dinamik benzerlik ilkeleriyle ölçeklenir; yapısal sönüm tam ölçeğe benzer olmalı. Reynolds alt eşiği bütün deney hız aralığında korunur. Yerçekimi kuvvetleri rijitliği etkiliyorsa Froude sayısı benzerliği gerekir ve raporlanır; Froude ölçeklemesinde hız ve frekans ölçekleri uzunluk ölçeğiyle sabitlenir. Tam aeroelastik modelde sönüm, frekans ve mod biçimleri tam ölçek hesaplarıyla karşılaştırılır.
6. **Aeroelastik deney koşulları (§5.3).** Hız aralığı ilgili sınır durumların ortalama yinelenme aralıklarına (MRI) göre belirlenir; nihai sınır durum (ULS) tasarım hızına kadar ve kararsızlığın başlangıcının ULS hızını aştığını gösterecek bir pay ile. Girdap uyarımında düşük hızda uyarım ve titreşimin başlamasının uzun sürebileceği gözetilir. Yön aralığı, yatay yapılarda sıfırdan farklı hücum açılarını da içerir. Düşük model hızlarının Reynolds etkileri raporda tartışılır; tünel titreşimi ve akustik dalgalardan kaynaklanan sahte uyarım önlenir.
7. **Raporla (§5.5).** Model türü seçiminin gerekçesi, ölçekleme ilkeleri, tam ölçeğe geçiş yöntemi ve varsayımları; tam ölçek ve model mekanik özellikleri (kütle, kutupsal atalet momenti, doğal frekanslar, sönüm) ve mesnet koşullarının modeldeki temsili.

## Zorunlu şartlar (standart metni, "shall")

| Bölüm | Şart |
|---|---|
| §1.1 | Yaya düzeyi rüzgâr, kirletici yayılımı, toz ve rüzgâr enerjisi çalışmaları kapsam dışıdır; ancak rüzgâr yükü raporuna eklenmelerine izin vardır. |
| §3.4.2 | Model + yük hücresi/terazi sistemi mekanik titreşimden arınmış; temel frekanslar ilk kalibrasyonda belirlenir ve veriyi kirletmesi önlenir; birleştirilecek yük ölçümleri eşzamanlıdır. |
| §3.4.2.1 | Rijit kesit modeli boyunca sürekli geometride; §8.1 geometri şartlarını sağlar. |
| §3.5 | Ürün deneyleri: bina geometrisi ve ürün konumu aralığı, ürün geometrisi aralığı ve yinelenen/girişimli dizilimler gözetilir; ürün geometrisi tam modellenir; sonuçlar, dayanak verilmedikçe modellenmeyen geometrilere dışdeğerlenmez; içdeğerleme deneyle doğrulanırsa serbesttir; geçerlilik koşulları raporda. |
| §3.5 | Çatı güneş paneli dizilerinde sonuçlar normalleştirilmiş etkili rüzgâr alanına (normalized effective wind area) göre sunulur. |
| §4.1 | Bölüm 3'ün bütün deney şartları dinamik yük verisi için de geçerlidir. |
| §4.2.1 | HFFB kalibrasyonu yanal ve burulma temel frekanslarını belirler; mod biçimi sapmasının etkisi çözümlemede gözetilir. |
| §4.2.2 | Basınç integrasyonunda delik sayısı ve yerleşimi toplam kuvvet ve momentleri gereken doğrulukta verecek düzeyde olur. |
| §4.4 | Ürünler için genel dinamik büyütme çarpanı (DAF) belirlenebilir; geçerlilik sınırları raporda. |
| §5.1 | Kararsızlık veya aeroelastik büyüme olasılığı varsa aeroelastik model deneyi zorunlu. |
| §5.2.1 | Kütle, rijitlik, sönüm dinamik benzerlikle ölçeklenir; sönüm tam ölçeğe benzer; Re alt eşiği tüm hız aralığında; gerekirse Froude benzerliği. |
| §5.2.2.1 | Kesit modelinin boy/genişlik oranı açıklık boyunca korelasyonu doğru modellemeye yeterli; model yerel eğilme önemsiz kalacak kadar rijit. |
| §5.2.2.2 | Kısmi aeroelastik modele, kritik tepkinin temel salınım modlarınca belirlendiği statik model deneyleriyle gösterilmişse izin vardır. |
| §5.2.2.3 | Tam aeroelastik modelde sönüm, frekans ve mod biçimleri tam ölçek hesabıyla karşılaştırılır; tam eşleşme sağlanamazsa nedenleri ve olası etkileri raporda tartışılır. |
| §5.3 | Hız aralığı ULS hızı + pay; yön aralığı önemli yönleri kapsar; düşük hız Re etkileri raporda; sahte uyarım önlenir. |
| §5.4 | Tam aeroelastik model toplam (ortalama + dinamik) tepkiyi doğrudan ölçecek biçimde donatılır; kesit ve kısmi modellerde tam yapıya geçiş onaylı yöntemlerle yapılır. |
| §7.1 | Kar yükü için tünel veya su kanalı model çalışmalarına ASCE 7 kar hükümlerinin yorumuna yardımcı olarak izin vardır; rapor ölçekleme ilkelerini, hesap yöntemlerini, varsayımları ve benzerlik uyumsuzluğundan gelen sınırlamaları içerir. |
| §8.1 | Rijit model doğal frekansı, ilgilenilen en düşük doğal frekanstan en az %30 yüksek. |

## Yorumdan öne çıkanlar (bağlayıcı değil)

- **HFFB varsayımları (§C4.2.1):** ilk üç mod ayrışık ve birbirine dik; salınım mod biçimleri yükseklikle doğrusal; burulma mod biçimi yükseklik boyunca sabit; harekete bağlı kuvvet yok; model + terazi sistemi yeterince rijit. Doğrusal olmayan mod biçimi için tipik düzeltmeler: eğilme taban momentinde ±%10, burulmada %30–%40 azaltma; tepe ivmelerinde %20'ye varan düzeltme.
- **Aeroelastik duyarlılık göstergeleri (§C5.1):** narinlik oranı binalarda 10:1'i, köprülerde 30:1'i aşıyorsa; kaldırma veya burulma kuvveti eğrisinin hücum açısına göre eğimi negatifse; titreşim periyotları olağandışı uzunsa.
- **Kesit modeli (§C5.2.2.1):** ölçek tipik 1:10–1:100; model boyu tabliye genişliğinin yaklaşık 4–5 katı. Girdap uyarımında hız ince adımlarla taranmalı ve her hızda yeterince beklenmelidir. Kesit modelinde kısmi türbülans benzetimi, n·d/U ≥ 1,0 için boyuna ve düşey spektrumları eşlemelidir.
- **Aeroelastik bina modelleri (§C5.2.2.2–3):** ölçek tipik 1:200–1:600; en az en düşük üç mod (iki salınım + burulma); karmaşık modlarda 3–7 düzeyde toplanmış kütleli tam model.
- **Hız aralığı (§C5.3):** binalarda en az risk kategorisine uygun nihai dayanım MRI hızına kadar; uzun açıklıklı köprülerde Kuzey Amerika uygulamasında kararsızlık başlangıcı için 10 000 yıllık MRI yaygındır. Türbülans girdap uyarımını bastırma ve çırpınma (flutter) başlangıcını yükseltme eğilimindedir; düşük türbülans olasılığı da denenmelidir.
- **Sönüm (§C5.2.1.1):** tam ölçek sönüm çoğu kez iyi bilinmez; bir dizi sönüm değeri için deney önerilir.
- **Ürünler (§C3.5):** deneyler çoğunlukla 1:50 veya daha büyük ölçekte yapılır ve PTS gerektirir; çatı güneş panelinde uygunsa en az sekiz sıra, temsili genel binaların çatısında denenmelidir.
- **Kar (§C7.1):** parçacık yöntemi ile zaman adımlı benzetim (A ve B) yöntemleri anlatılır; parçacık yöntemleri tam dinamik benzetim değil yaklaşık benzeşimdir. Kar için CFD umut verici ama henüz geniş geometri aralığında doğrulanmamıştır; ölçekli model çalışmasıyla birlikte tamamlayıcı araç olarak önerilir.
- **Hortum ve aşağı patlama (§C2.3.2):** yerleşik ölçekleme kuralları yoktur; yorum, aerodinamik + statik basınç bileşenlerini, hortum boyutunun binaya göre üç durumunu ve koşullu ortalama (conditional averaging) yaklaşımını içeren bir çerçeve önerir. Parametre aralıkları `referans.md` içindedir.

## Denetim listesi (tünel raporu okurken; evet/hayır)

1. Yapının rijit / esnek / aeroelastik sınıfı ve seçilen deney türünün gerekçesi verilmiş mi?
2. HFFB kullanıldıysa model + terazi sisteminin temel frekansları (salınım ve burulma) raporlanmış mı?
3. Bu frekansların ölçüm bandını kirletmediği (veya mekanik admitans düzeltmesi yapıldığı) gösterilmiş mi?
4. Varsayılan mod biçimleri ve gerçek mod biçimleri için uygulanan düzeltmeler anlatılmış mı?
5. Yapısal özellikler (frekans, kütle, sönüm) ve kaynakları raporda mı?
6. Çözümleme tanım alanı (frekans/zaman) ve sonuç biçimi (eşdeğer statik yük / doğrudan tepki) belirtilmiş mi?
7. Aeroelastik model varsa kütle, rijitlik, sönüm ölçeklemesi ve hız/frekans ölçekleri verilmiş mi?
8. Froude benzerliği gerekip gerekmediği tartışılmış mı?
9. Reynolds alt eşiği en düşük deney hızında da sağlanmış mı?
10. Hız aralığı ULS hızını bir payla aşıyor mu; kararsızlık başlangıç hızı belirlenmiş mi?
11. Model sönümü, frekansları ve mod biçimleri tam ölçek hedefleriyle karşılaştırılmış mı?
12. Ürün deneyinde denenen geometri aralığı ve geçerlilik koşulları açıkça yazılmış mı; dışdeğerleme yapılmış mı?
13. Kar çalışmasında benzerlik uyumsuzluklarından doğan sınırlamalar belirtilmiş mi?
14. Yaya düzeyi rüzgâr sonuçları varsa bunların ASCE 49 şartlarıyla kapsanmadığı anlaşılır mı?

## CFD ile karşılaştırırken dikkat

- **HFFB sonuçları** toplam taban momentleri ve bunların spektrumlarıdır; CFD'de karşılığı yüzey basıncının taban etrafında integre edilmiş zaman serisidir. Rapordan: moment ekseninin (terazi merkezinin) konumu, boyutsuzlaştırma (referans hız, alan, uzunluk), yön tanımı alınmalıdır.
- **Rezonans tepkisi tünelde ölçülmez**, yapısal özelliklerle analitik olarak eklenir. CFD ile karşılaştırma ham aerodinamik yükler (ortalama, arka plan, spektrum) üzerinden yapılmalı; rapordaki tasarım yükleri (eşdeğer statik yük) sönüm, frekans ve iklim varsayımlarını içerir.
- **Mod biçimi düzeltmeleri** rapor sonuçlarına uygulanmış olabilir; ham mı düzeltilmiş mi olduğu öğrenilmelidir.
- **Aeroelastik etkiler** (aerodinamik sönüm, kilitlenme) rijit geometrili CFD'de ortaya çıkmaz; aeroelastik model sonuçları rijit CFD ile doğrudan karşılaştırılamaz.
- **Ürün deneyleri** çoğunlukla PTS ile yapılır; raporlanan katsayılar düşük frekans telafisini içerir (bkz. `tunel-yaklasan-akis`).
- **Yaya düzeyi rüzgâr** için bu standart ölçüt vermez; karşılaştırma ölçütü başka kaynaktan gelmelidir.

## İlgili beceriler

- `tunel-yaklasan-akis` — yaklaşan akış, PTS, sinoptik olmayan rüzgârların kapsamı.
- `tunel-model-ve-cevre` — ölçek, tıkanma, Reynolds, eklentiler.
- `tunel-basinc-olcumu-ve-yukler` — basınç integrasyonu, tepe değer, iklimle birleştirme, belirsizlik, rapor.
