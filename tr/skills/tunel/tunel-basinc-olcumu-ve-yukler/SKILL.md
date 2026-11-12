---
name: tunel-basinc-olcumu-ve-yukler
description: Rüzgâr tünelinde basınç ölçümü (pressure taps, tubing frequency response, sampling rate/duration), referans basınç ve hız (reference pressure/velocity), tepe değer kestirimi (peak pressure, Gumbel), alan ortalaması/basınç integrasyonu (pressure integration), iç basınç (internal pressure), kaplama (C&C) ve taşıyıcı sistem (MWFRS) yükleri, rüzgâr iklimiyle birleştirme ve yönsellik (wind climate, directionality), ölçüm belirsizliği, kalite güvencesi ve rapor içeriği ASCE/SEI 49-21'e göre sorulduğunda veya bir tünel raporu bu açılardan denetlenirken kullan.
---

# Tünelde basınç ölçümü ve yükler — ASCE/SEI 49-21

Kaynak: ASCE/SEI 49-21 (2021 baskısı). Standart metni §1–§8, yorum §C1–§C8. Sayfa numaraları PDF sayfa sırasıdır. Ayrıntılı tablo: `referans.md`.

## Ne zaman kullanılır

- Rijit model üzerinde basınç deliği (pressure tap) ölçümüyle kaplama ve taşıyıcı sistem yükleri bulunurken.
- Bir tünel raporundaki Cp değerlerinin nasıl boyutsuzlaştırıldığı, tepe değerin nasıl kestirildiği, ölçüm süresi ve frekans yanıtının yeterli olup olmadığı sorulduğunda.
- Tünel verisinin rüzgâr iklimiyle birleştirilmesi ve yön etkisi değerlendirilirken.
- Tünel Cp'leri CFD sonucuyla karşılaştırılacakken.

## Adım adım

1. **Referans hızı tanımla (§3.3).** Referans hız, yakın çevre modelinin etkisi en az olacak yerde ölçülür ve deney kesitindeki hedef ortalama hız profiliyle ilişkilendirilir. Yeri, ölçüm parametreleri ve başka bir konuma/yüksekliğe yapılan her dönüşüm raporda belgelenir.
2. **Referans statik basıncı seç (§3.4.1).** Statik referans basınç gerekiyorsa (ör. dış basınç katsayıları yayınlarla karşılaştırılacaksa) yerel öğelerin etkisi en az olacak biçimde ölçülür; konum(lar) raporda belgelenir. Yorum: benzetilen akışın üstüne yerleştirilmiş bir Pitot-statik tüpün statik deliği çoğu kez kullanılabilir (§C3.4.1).
3. **Basınç deliklerini yerleştir (§3.4.1).** Dağılım istenen yük etkilerini yakalamaya yetmeli; hiçbir önemli yük etkisi kaçmayacak sayıda konum ve yönde ölçülmeli. **Standart sayısal delik yoğunluğu vermez.** Yorum: küçük binalarda ve basınç gradyanının yüksek olduğu yerlerde (çatı köşesi/kenarı/mahyası, duvar kenarı) daha sık delik önerilir; basit dikdörtgen yüksek binalarda basınç integrasyonu için halka başına yaklaşık 20–30 delik ve yükseklik boyunca en az 8–10 halka deneyimle uygun bulunmuştur (§C3.4.1, §C4.2.2).
4. **Ölçüm zincirinin frekans yanıtını doğrula (§8.1).** Basınç ölçümünde genlik oranı, model ölçeğinde Uh/B frekansının altındaki frekanslarda sabit değerden ±%10'dan fazla sapmamalı; faz da bu aralıkta doğrusal değişimden ±%10'dan fazla sapmamalı. Düzeltme için aktarım işlevi (transfer function) kullanılabilir. Uh = ortalama çatı yüksekliğindeki ortalama hız; B = en küçük yatay boyut ile ortalama çatı yüksekliğinden küçük olanı.
5. **Örnekleme hızı ve süresini seç (§3.4, §8.2).** Hız ve süre, amaçlanan çözümleme yöntemine uygun veri kümesi verecek biçimde seçilir. Süre, incelenen yük için kritik yükseklikteki boyuna integral zaman ölçeğinin 500 katından uzun olmalıdır. **Standart sayısal örnekleme hızı (Hz) vermez**; hız, frekans yanıtı şartı ve hedef akışın niteliğiyle belirlenir.
6. **Kalibrasyon ve kayma (§3.4).** Ölçüm aletleri deneyden önce, gerekiyorsa deney sırasında ve sonrasında kalibre edilir; ortalama değerlerdeki kayma (drift) düzeltilir. Deliklerin doğru kanala bağlı olduğu ve hortumlarda kaçak olmadığı denetlenir (§3.4.1).
7. **Yük birleştir (§3.4.1.1).** Ortalama ve zamanla değişen yük etkileri için çok noktadan basınç integrasyonuna izin vardır; zamanla değişen etkilerde integre edilecek bütün basınçlar eşzamanlı ölçülmüş olmalıdır.
8. **İç basıncı ele al (§3.4.1.2).** İç basınç ya ölçülen dış basınçlardan analitik olarak ya da uygun modelle doğrudan ölçülerek bulunur; geçirgenlik, sızıntı ve açıklıkların etkisi farklı olası senaryolar için değerlendirilir. Zamanla değişen iç basıncın doğrudan ölçümünde iç hacim ölçeklemesi gerekir.
9. **Tepe değeri kestir (§3.4.1.3).** Tepe basınçlar tanınmış yayınlardaki istatistiksel bir yöntemle belirlenir; aşılmama olasılığı (probability of nonexceedance) raporlanır; yöntem uygulanmadan önce ham zaman serisi aerodinamikle ilgili frekanslarda süzülemez.
10. **İklimle birleştir (§6).** Yük/tepki olasılığı isteniyorsa tünel verisi yerel rüzgâr iklimi veya belirtilen başka bir hız şartıyla, onaylı istatistiksel süreçlerle birleştirilir; sahada tehlikeye katkısı olan bütün fırtına türleri dikkate alınır; varsayım ve yöntemler raporda belgelenir.
11. **Belirsizlik ve kalite (§8.2, §8.3).** Aerodinamik katsayılardaki, ölçüm donanımı + örnekleme hızı + deney süresinden gelen toplam belirsizlik %10'u geçmemeli. Verinin güvenilirliği (benzetimin belirsizliği, ölçümün doğruluğu ve tekrarlanabilirliği) değerlendirilir.
12. **Raporla ve sakla (§1.2).** Yük, basınç ve referans hız zaman serileri saklanır; rapor denetlenebilir olmalıdır.

## Katsayı tanımı (yorum, §C3.4.1, Denk. C3-2)

Cp,max, Cp,min, Cp,mean ve Cp,rms; sırasıyla örnekleme süresindeki en büyük, en küçük, zaman ortalaması ve karekök-ortalama (ortalamadan sapmanın) basıncın qref = ½·ρ·Uref² değerine bölünmesiyle tanımlanır. Bütün basınçlar bozulmamış akıştaki statik basınca göre fark basıncıdır. Standart Uref için tek bir yükseklik dayatmaz; rapor tanımı vermek zorundadır (§3.3).

## Tepe değer yöntemleri (yorum, §C3.4.1.3)

- Tek bir gözlenen tepe katsayısı kullanılmamalıdır: tekrarlanabilirliği zayıftır ve deney süresine bağlıdır.
- Yaygın iki yöntem: (1) topluluk ortalaması (ensemble average) — eşit uzunlukta, uygun bir tam ölçek gözlem süresini (ör. 10 dk – 1 sa) temsil eden dilimlerden alınan en büyüklerin ortalaması; (2) Gumbel uydurma — dilim en büyüklerinden parametreleri bulup belirli bir yüzdelik düzeye karşılık gelen tepeyi kestirmek.
- Diğer tanınan yöntemler: bağımsız fırtınalar yöntemi, BLUE (en iyi doğrusal yansız kestirici), eşik üstü tepe (POT).
- Cook–Mayne yöntemi Gumbel uydurmanın uzantısıdır; yük ve rüzgâr hızı uç değer uydurmalarını birleştirir, en doğrusudur ama uç rüzgâr iklimi bilgisini gerektirir; birçok iklimde kullanılacak ürünlerin genel katsayıları için uygun değildir.
- Davenport tepe çarpanı yalnız Gauss süreçleri için geçerlidir; karmaşık akışta sınırlıdır.
- Binalarda en büyük yerel tepe basınçların etkin süresi tam ölçekte yaklaşık 1–3 s'dir (§C3.4).
- Büyük tepe basınç katsayıları, akışın doğası gereği bir deney gerçeklemesinden ötekine %30 değişebilir (§C8.2).

## Rüzgâr iklimi ve yönsellik (özet)

Zorunlu (§6.1–§6.8): rüzgâr iklim modeli türetilir; kayıt uzunluğu, anemometre yüksekliği ve türü, veri kalitesi, ortalama alma süresi, arazi ve fırtına türü gözetilir; fırtına türleri ayrıntılı çözümlemeden önce ayrıştırılır; yön değerlendirmesinden kaynaklanan yük azaltmasına izin vardır. Tropikal siklon bölgelerinde onaylı bir benzetim yöntemiyle tehlike modeli gerekir ve tasarım yükleri tropikal + tropikal olmayan rüzgârların birleşik etkisiyle belirlenir. Hortum tehlike modeli gerekiyorsa benzetimle kurulur; hortumların tarihsel hız verisi kullanılamaz.

Yorum (§C6.8) birleştirme yöntemlerini sıralar: yönsüz üst sınır yöntemi (en basit ve güvenli yanda; ASCE 7 hızlarıyla iklim çözümlemesi yapmadan da kullanılabilir), normalleştirilmiş sektör yöntemi (genellikle güvenli yanda, seyrek olarak güvensiz çıkabilir), çok sektörlü yöntem, yukarı geçiş (up-crossing) yöntemi, fırtına geçişi yöntemi, doğrudan benzetim. Fırtına türleri istatistiksel bağımsız süreçler olarak birleştirilir (Denk. C6-1, C6-2). Tarihsel verinin yön çözünürlüğü çoğu kez tünel verisinden (tipik 10°) kabadır; bunun için yapılan varsayımlar raporda belgelenmelidir. Havalimanı verisi 10 m yükseklik ve düz açık araziye indirgenmelidir.

## Zorunlu şartlar (standart metni, "shall")

| Bölüm | Şart |
|---|---|
| §1.2 | Rapor denetlenebilir olmalı; düzen, yöntem, akış, iklim çözümlemesi, sonuçlar ve belirsizlik niceliği yer alır ya da istendiğinde hemen sunulur. |
| §1.2 | Yük, basınç ve referans hız zaman serileri saklanır. |
| §3.3 | Referans hız yakın çevre modelinin etkisi en az olan yerde; hedef profille ilişkili; yer, parametreler ve dönüşümler raporda. |
| §3.4 | Kalibrasyon deney öncesi (gerekirse sırasında/sonrasında); örnekleme hızı ve süresi yönteme uygun; frekans yanıtı tepe ve zamanla değişen büyüklükleri yakalamaya yeterli; ortalama kayması düzeltilir. |
| §3.4.1 | Statik referans basınç yerel etkilerden en az etkilenecek biçimde ölçülür; yeri raporda. |
| §3.4.1 | Delik dağılımı yük etkilerini yakalamaya yeterli; önemli hiçbir etki kaçmayacak sayıda konum ve yön. |
| §3.4.1.1 | Zamanla değişen etkiler için integre edilen basınçlar eşzamanlı ölçülür. |
| §3.4.1.2 | İç basınç analitik veya doğrudan ölçümle değerlendirilir; geçirgenlik, sızıntı, açıklık senaryoları gözetilir; boşluk (cavity) basınçları, arkadaki yüzeyin yükünü değiştirebildiği durumlarda hesaba katılır. |
| §3.4.1.3 | Tepe basınç istatistiksel yöntemle; aşılmama olasılığı raporlanır; aerodinamikle ilgili frekanslarda ön süzme yasak. |
| §6.1–§6.8 | Olasılıklı sonuç isteniyorsa iklimle birleştirme; fırtına türleri ayrıştırılır; varsayım ve yöntemler raporda. |
| §8.1 | Basınç ölçüm zinciri: Uh/B altındaki frekanslarda genlik ±%10, faz doğrusaldan ±%10 içinde. Ölçümler akustik etki, elektriksel gürültü, mekanik titreşim ve sahte çalkantılardan arınmış; sıcaklık kayması düzeltilmiş. |
| §8.2 | Katsayı belirsizliği (donanım, örnekleme hızı, süre) ≤ %10; süre > 500 boyuna integral zaman ölçeği. |
| §8.3 | Güvenilirlik değerlendirilir; izlenebilir kalibrasyon ve tekrarlanabilirlik denetimleri yapılır; yönetmelik, önceki model ve tam ölçek verisiyle güvenilirlik karşılaştırmaları (varsa ve anlamlıysa) rapora konur. |

## Denetim listesi (tünel raporu okurken; evet/hayır)

1. Referans hızın ölçüldüğü konum ve yükseklik açıkça verilmiş mi?
2. Katsayılar başka bir yüksekliğe/konuma çevrildiyse dönüşüm belgelenmiş mi?
3. Statik referans basıncın yeri belirtilmiş mi?
4. Cp tanımı (qref, hangi hız, hangi ortalama süresi) yazılmış mı?
5. Basınç deliklerinin sayısı ve yerleşimi (çizim/tablo) verilmiş mi; köşe ve kenarlarda sıklaştırılmış mı?
6. Hortum sisteminin frekans yanıtı (veya aktarım işleviyle düzeltme) belgelenmiş ve Uh/B'ye kadar ±%10 içinde mi?
7. Örnekleme hızı ve süresi model ve tam ölçek karşılığıyla verilmiş mi?
8. Süre, kritik yükseklikte 500 integral zaman ölçeğinden uzun mu?
9. Alan ortalaması/integrasyonda kullanılan basınçlar eşzamanlı mı ölçülmüş?
10. Tepe değer yöntemi (ör. Gumbel, topluluk ortalaması) ve aşılmama olasılığı belirtilmiş mi?
11. Tepe kestiriminden önce aerodinamik frekansları gideren bir süzme yapılmadığı açık mı?
12. Tek bir gözlenen tepe yerine istatistiksel kestirim mi kullanılmış?
13. İç basınç nasıl ele alınmış (ölçüm, analitik, ASCE 7 değeri) ve hangi açıklık senaryoları için?
14. Rüzgâr iklimi veri kaynağı, fırtına türü ayrımı ve birleştirme yöntemi anlatılmış mı?
15. Yönsel azaltma kullanıldıysa yöntem ve yön çözünürlüğü varsayımları belgelenmiş mi?
16. Belirsizlik niceliği (≤ %10 katsayı belirsizliği dahil) verilmiş mi?
17. Kalibrasyonun izlenebilirliği ve tekrarlanabilirlik denetimi belirtilmiş mi?
18. Yönetmelik veya önceki verilerle güvenilirlik karşılaştırması var mı?
19. Zaman serilerinin saklandığı belirtilmiş mi?
20. Standarttan sapmalar gerekçelendirilmiş mi?

## CFD ile karşılaştırırken dikkat

Rapordan alınması gerekenler:
- **Boyutsuzlaştırma:** Uref'in yeri ve yüksekliği (sınır tabaka dışı mı, çatı yüksekliği mi), hava yoğunluğu, statik referans basıncın yeri. CFD Cp'si aynı qref ve aynı statik referansla hesaplanmadıkça karşılaştırma anlamsızdır.
- **Delik konumları:** her deliğin koordinatı. CFD'de karşılaştırma delik konumundaki noktasal/hücre değeriyle yapılmalı; yüzey ortalamasıyla değil.
- **Frekans içeriği:** ölçüm zincirinin düz yanıt verdiği üst frekans (en az Uh/B) ve örnekleme hızı. Rms ve tepe değerler bant genişliğine bağlıdır; CFD zaman serisi karşılaştırmadan önce aynı etkin bant genişliğine getirilmelidir.
- **Süre:** tünel süresi integral zaman ölçeği cinsinden (≥ 500). CFD (özellikle LES) süresi bundan çok kısaysa tepe ve rms kestirimlerinin belirsizliği büyüktür; yorum, büyük tepe katsayılarının tünelde bile gerçeklemeden gerçeklemeye %30 oynayabildiğini söyler.
- **Tepe tanımı:** yöntem, dilim uzunluğu (tam ölçek karşılığı), dilim sayısı ve aşılmama olasılığı. CFD tepe değerleri aynı yöntem ve aynı yüzdelikle hesaplanmalıdır; ham en büyük/en küçük değerle karşılaştırılmamalıdır.
- **Alan ortalaması:** hangi deliklerin, hangi ağırlıklarla ve eşzamanlı olarak birleştirildiği.
- **İç basınç ve net basınç:** rapordaki değer dış Cp mi, net basınç mı; iç basınç hangi yolla eklendi.
- **İklim birleştirmesi:** rapordaki tasarım basınçları çoğu kez yönsel iklimle birleştirilmiş ve bir dönüş periyoduna karşılık gelen değerlerdir; CFD'nin tek yön için verdiği katsayıyla doğrudan karşılaştırılamaz. Karşılaştırma ham, yön bazlı katsayılar üzerinden yapılmalıdır.
- **Tıkanma ve diğer düzeltmeler:** raporlanan katsayılara düzeltme uygulanıp uygulanmadığı.

## İlgili beceriler

- `tunel-yaklasan-akis` — hedef profil, türbülans, referans hız/yükseklik seçimi.
- `tunel-model-ve-cevre` — ölçek, tıkanma, yakın çevre, Reynolds, yön adımı.
- `tunel-diger-olcumler` — kuvvet terazisi, basınç integrasyonuyla dinamik tepki, aeroelastik model, ürünler.
