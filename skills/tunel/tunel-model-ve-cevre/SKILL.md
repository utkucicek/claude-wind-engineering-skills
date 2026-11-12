---
name: tunel-model-ve-cevre
description: Rüzgâr tüneli modelinin ASCE/SEI 49-21'e göre ölçeği (geometric scale), geometrik ayrıntısı ve doğruluğu, yakın çevre modeli (proximity model) kapsamı, tıkanma oranı (blockage ratio) sınırı ve düzeltmesi, Reynolds sayısı (Reynolds number) şartları ile yuvarlak hatlı yapılar ve rüzgâr yönü adımı (wind direction increment) sorulduğunda veya bir tünel raporunda bunlar denetlenirken kullan.
---

# Tünel modeli ve çevresi — ASCE/SEI 49-21

Kaynak: ASCE/SEI 49-21 (2021 baskısı). Standart metni §1–§8, yorum §C1–§C8. Sayfa numaraları PDF sayfa sırasıdır. Ayrıntılı tablo: `referans.md`.

## Ne zaman kullanılır

- Model ölçeği seçilirken ya da bir rapordaki ölçeğin akışla uyumu denetlenirken.
- "Çevre binalar hangi yarıçapa kadar modellenmeli?", "tıkanma %5'i geçti, ne olur?", "Reynolds sayısı yeterli mi?", "kaç derecede bir ölçülmeli?" sorularında.
- Tünel deneyini CFD'de yeniden kurarken geometri ve hesap alanı bilgisi rapordan çıkarılırken.

## Adım adım

1. **Ölçeği akışla uyumlu seç (§2.2).** Dört ölçüt birlikte sağlanır (m = model, p = prototip):
   - Denk. 2-1: (Lb/z0)m = (Lb/z0)p — 3 katı içinde (tam ölçekte z0 belirsizliği nedeniyle).
   - Denk. 2-2: (Lb/zref)m = (Lb/zref)p — model ve tam ölçekte aynı referans konumu seçilerek sağlanır.
   - Denk. 2-3: (xLu/Lb)m = (xLu/Lb)p — 3 katı içinde; ya da en az (xLu/Lb)m ≥ 3.
   - Denk. 2-4: (Lb·Ub/ν)m ≥ 11 000 — alt sınır.
   Biri tutmuyorsa belirsizlik ve gerekebilecek ek çalışmalar (yüksek Reynolds deneyi, daha büyük tesis) raporda tartışılır.
2. **Tıkanmayı hesapla (§1.4, §2.2).** Tıkanma oranı = (model + yakın çevre modellerinin kesit alanı) / (modelin bulunduğu yerde deney kesiti alanı). Düzeltme yapılmıyorsa %5'ten küçük olmalı; %5'i aşıyorsa gerekçe raporda verilir.
3. **Geometriyi doğru kur (§3.2, §8.1).** Model, rüzgârla etkileşen dış yüzeylerin doğru temsilidir; genel boyutlar ±%2 doğrulukta olmalı ve köşe eğrilik yarıçapına özellikle dikkat edilmelidir. Tam ölçeklenemeyen ayrıntılar (çok ince eleman) veya akışı bozan ölçüm donanımı (dıştan geçen basınç hortumu) varsa etkisi değerlendirilir, en aza indirilir ve raporda anlatılır.
4. **Rijitliği sağla (§3.2, §8.1).** Model, deney hız aralığında rijit davranmalı; rijit model çalışmalarında modelin doğal frekansı ilgilenilen en düşük doğal frekanstan en az %30 yüksek olmalıdır.
5. **Reynolds duyarlılığını değerlendir (§3.2).** Ölçek seçilirken Reynolds alt eşikleri gözetilir. Yalnız Reynolds etkisinin önemsiz olduğu durumlarda tek tünel hızında deney yapılabilir; aksi hâlde birden çok hız gerekir.
6. **Yakın çevre modelini kur (§2.4).** Deney binasının rüzgâr yükünü etkileyebilecek binalar, diğer yapılar ve topoğrafik öğeler modellenir. Standart sayısal yarıçap vermez; ölçüt "etkileyebilecek olan her şey"dir.
7. **Yönleri seç (§3.2).** Yön sayısı ve/veya rüzgâr koşulu sayısı, yükleri tanımlamaya ve tasarım için kritik yönleri yakalamaya yetmelidir. Sayısal adım yalnız yorumdadır: genel olarak 10°'den büyük olmamalı, gerekçeyle gevşetilebilir (§C3.2).
8. **Eklentiler (§2.6).** Eklenti (appurtenance) yükleri, ölçekleme şartları elveriyorsa ana yapı modeli üzerinde doğrudan ölçülür; elvermiyorsa eklentinin bulunduğu yerdeki akış alanı belirlenip daha büyük ölçekte yeniden üretilerek ölçülebilir.

## Yakın çevre modeli — metnin söylediği

Zorunlu (§2.4, s. 21): yalnız tek cümlelik kapsam şartı — rüzgâr yükünü etkileyebilecek bina, yapı ve topoğrafik öğeler modellenir. **Yarıçap, içerik ayrıntısı veya sayısal ölçüt standart metninde yoktur.**

Yorum (§C2.4, s. 43–44; bağlayıcı değil):
- Amaç yerel rüzgâr ortamını benzetmektir; sahadaki rüzgâr koşullarına belirgin katkısı olan bütün nesneler dahil edilmelidir.
- Yakın çevre modeli, deney binasıyla birlikte döner tabla (turntable) üzerinde döner.
- Yüksek bina deneyleri (çoğunlukla 1:300–1:500) yaygın olarak yaklaşık 240 m (800 ft) veya daha büyük yarıçaplı bir çevre modeli içerir. Bu büyüklük kısmen tarihseldir: birçok tesisin döner tabla yarıçapı 1,2–1,5 m (4–5 ft) mertebesindedir.
- Döner tablanın dışında kalan ama çevresine göre belirgin biçimde büyük bir bina, deney binasının rüzgâr üstüne düştüğü yönlerde dahil edilebilir.
- Standart en küçük yarıçap vermez; çünkü güncel ABL deneylerinde ölçekler yaklaşık 1:20 ile 1:800 arasında değişir. Kapsamın yeterliliği rüzgâr mühendisinin sorumluluğundadır.
- Çevre binaları kesit, yükseklik ve belirgin özellikleri korunarak makul ölçüde sadeleştirilebilir; rüzgâr altında hareket etmemelidir. Gerçek kuzey model üzerinde gösterilmelidir.
- Çevre modeli topoğrafya içerdiği için zemini tünel tabanından belirgin yüksekse ön kenarda gerçek dışı ayrılma ve hızlanma olabilir; ön kenar eğimlendirilir (taper). Önerilen eğim %7'den azdır.
- Yapılması yüksek olasılıklı veya onaylanmış gelecek binalar dahil edilmesi düşünülmelidir.
- Birden çok çevre düzeni denenebilir; farklar fotoğraf, tablo veya şemayla belgelenmelidir. Tipik örnek: yararlı korunma sağlayan binaların çıkarıldığı "azaltılmış korunma" (reduced sheltering) düzeni.
- Tıkanma oranı deney modeli ile yakın çevre modelinin toplamından hesaplanır; yakın çevre modeli referans hız ölçüm yerindeki akışı etkilememelidir.

## Tıkanma — metnin söylediği

- Zorunlu: düzeltme yapılmadıkça %5'ten küçük; aşılırsa gerekçe raporda (§2.2, s. 20).
- Yorum: tıkanma %5'i aşmıyorsa boyuna basınç gradyanı ve diğer akış bozulmaları genellikle kabul edilebilir. Tıkanma hatalarını denetlemek veya sınırlamak için özel özen gösterilirse ya da analitik/ampirik düzeltmelerin geçerli olduğu gösterilebilirse daha büyük tıkanmaya çoğu kez izin verilebilir (§C2.3.1.1, s. 36). Sabit kesitli, pürüzlü tabanlı ve modelli bir deney kesitinde düzeltilmezse basınç akış yönünde belirgin düşer ve model üzerindeki ayrılma ile yeniden tutunmayı değiştirir; tavan yüksekliği ayarıyla denetlenir.
- **Belirli bir düzeltme formülü veya yöntemi standartta verilmemiştir** (metinde bulunamadı).

## Reynolds sayısı ve yuvarlak hatlı yapılar

- Zorunlu alt sınırlar: bina Re ≥ 11 000 (Denk. 2-4); pürüzlülük Re u*·z0/ν ≥ 2,5 (Denk. 2-5).
- Yuvarlak kesitli yapılar için **standart metninde ayrı bir sayısal Reynolds eşiği yoktur.** Genel şart §3.2'dedir: Reynolds etkisi önemsiz değilse tek hızla yetinilemez.
- Yorum (§C3.2, s. 46): direnç krizi (drag crisis) söz konusu olan dairesel yapılarda Re dikkate alınmalıdır. Tünelde ulaşılabilen Re aralığı (genellikle bir mertebeden az) soruyu çözmeye yetmez; model ve tam ölçek çoğu kez direnç krizi minimumunun iki ayrı yanındadır. Amaç çoğunlukla türbülanslı yaklaşan akışın ve/veya (bazen abartılmış) model yüzey pürüzlülüğünün direnç krizinin etkisini azalttığını ya da giderdiğini göstermektir.
- Yorum (§C3.2): keskin köşeli yapılarda köşe keskinliği, eğri yüzeyli yapılarda yüzey pürüzlülüğü ayrılma ve yeniden tutunmayı belirgin etkiler; bu ayrıntılar belirleyicidir.
- Yorum (§C5.2.1.2, s. 55–56): keskin kenarlı yapıların çoğunda Re benzerliğinin sağlanamaması sorun değildir; dairesel ve eğri yüzeyli kesitlerde model–tam ölçek farkı belirgin olabilir; Re'ye duyarlı yapılarda sonuçlar tam ölçek ölçümlerine veya tam ölçek Re aralığındaki deney verisine dayanarak düzeltilmelidir. Korkuluk, ince kafes çubuğu gibi küçük elemanlarda eleman Re'si çok düşebilir (ör. 100 veya altı); eleman sayısını azaltıp genişliği artırarak (açık alanı koruyarak) Re yüksek tutulabilir.

## Zorunlu şartlar (standart metni, "shall")

| Bölüm | Şart |
|---|---|
| §2.2 | Denk. 2-1 ve 2-3 (ilk bağıntı) 3 katı içinde; (xLu/Lb)m ≥ 3 ve Re ≥ 11 000 alt sınır; sağlanamazsa belirsizlik raporda tartışılır. |
| §2.2 | Tıkanma oranı, düzeltme yapılmadıkça %5'ten küçük; aşılırsa gerekçe raporda. |
| §2.4 | Yükü etkileyebilecek bina, yapı ve topoğrafik öğeler modellenir. |
| §2.6 | Eklenti yükleri, ölçekleme elveriyorsa ana yapı modelinde doğrudan ölçülür; yerel akışı yeniden üreten büyük ölçekli deneye izin vardır. |
| §3.2 | Model dış geometrinin §8.1 toleransları içinde doğru temsilidir; kaçınılmaz çarpıklıklar değerlendirilir, en aza indirilir, raporda anlatılır. |
| §3.2 | Model deney hız aralığında rijit davranır. |
| §3.2 | Ölçeklemede Reynolds alt eşikleri gözetilir; tek tünel hızı yalnız Re etkisi önemsizse. |
| §3.2 | Yön/koşul sayısı yükleri tanımlar ve kritik yönleri yakalar. |
| §8.1 | Model genel boyutları ±%2 doğrulukta; köşe eğrilik yarıçapına özel dikkat. |
| §8.1 | Rijit model doğal frekansı, ilgilenilen en düşük doğal frekanstan en az %30 yüksek. |
| §1.2 (1) | Rapor uzunluk, hız ve zaman ölçeği benzerlik parametrelerini; hedef rüzgâr üstü arazi, çevre ve yakın çevre özelliklerini içerir. |

## Denetim listesi (tünel raporu okurken; evet/hayır)

1. Geometrik ölçek, hız ölçeği ve zaman ölçeği raporda verilmiş mi?
2. Lb/z0 uyumu (3 katı içinde) gösterilmiş mi?
3. xLu/Lb uyumu (3 katı içinde ya da model değeri ≥ 3) gösterilmiş mi?
4. Model Reynolds sayısı (Lb·Ub/ν) ≥ 11 000 mi?
5. Tıkanma oranı verilmiş mi ve model + yakın çevre birlikte mi hesaplanmış?
6. Tıkanma %5'ten küçük mü; değilse düzeltme ve gerekçe var mı?
7. Model boyut doğruluğu (±%2) ve köşe yarıçapı ele alınmış mı?
8. Cepheden, en küçük yatay boyutun %2'si veya daha fazla taşan mimari ayrıntılar modele katılmış mı? (yorum önerisi, §C8.1)
9. Ölçeklenemeyen ayrıntılar veya akışı bozan donanım varsa etkisi anlatılmış mı?
10. Modelin rijitliği / doğal frekansı (en az %30 pay) belgelenmiş mi?
11. Yakın çevre modelinin kapsamı (yarıçap, dahil edilen binalar) tanımlanmış ve fotoğraflanmış mı?
12. Döner tabla dışındaki belirgin büyük binalar ele alınmış mı?
13. Gelecekte yapılacak/onaylı binalar ve birden çok çevre düzeni (ör. azaltılmış korunma) belgelenmiş mi?
14. Gerçek kuzey ve yön tanımı (koordinat sistemi) verilmiş mi?
15. Rüzgâr yönü adımı 10° veya daha sık mı; değilse gerekçe var mı? (yorum)
16. Yuvarlak hatlı yüzeyler varsa Reynolds duyarlılığı (birden çok hız, yüzey pürüzlülüğü, düzeltme) tartışılmış mı?
17. Tek hızda deney yapıldıysa Reynolds etkisinin önemsizliği gerekçelendirilmiş mi?
18. Karmaşık arazi varsa topoğrafya modeli ya da ön kenar eğimi (%7'den az) kullanılmış mı?

## CFD ile karşılaştırırken dikkat

Rapordan alınması gerekenler:
- **Ölçek ve model boyutları:** geometrik ölçek, Lb, model yüksekliği; CFD model ölçeğinde mi tam ölçekte mi koşulacak, buna göre Re farkı bilinmeli.
- **Deney kesiti boyutları ve tıkanma:** tünel genişliği/yüksekliği ve tıkanma oranı. Tünel duvarları CFD'de modellenmeyecekse tıkanma etkisi (ve uygulanmış düzeltme) farkın kaynağı olabilir; rapor düzeltme yapıldığını söylüyorsa hangi veriye uygulandığı öğrenilmeli.
- **Yakın çevre modelinin kapsamı:** yarıçap, hangi binaların dahil olduğu, sadeleştirme düzeyi, hangi çevre düzeninin (mevcut / gelecek / azaltılmış korunma) hangi sonuca ait olduğu. Standart sayısal yarıçap vermediği için bu bilgi yalnız rapordan gelir.
- **Çevre modelinin ötesi:** tünelde çevre modelinin rüzgâr üstünde pürüzlülük elemanlarıyla üretilen sınır tabaka vardır; CFD'de çevre binalarının bittiği yerden girişe kadar hangi pürüzlülüğün kullanılacağı bununla tutarlı olmalı.
- **Köşe yarıçapı ve mimari ayrıntı:** modelde hangi ayrıntıların bulunduğu (balkon, parapet, güneş kırıcı); CFD geometrisi tünel modelindeki ayrıntı düzeyiyle eşleşmeli. Köşe keskinliği ayrılmayı belirler.
- **Yön tanımı ve adımı:** 0° hangi yön, dönüş yönü, adım (tipik 10°). Çevre modeli binayla birlikte döndüğü için CFD'de de bina + çevre birlikte döndürülmeli, giriş profili sabit kalmalıdır (pürüzlülük yöne göre değişiyorsa rapordaki yön–profil eşlemesi kullanılır).
- **Reynolds sayısı:** tünel Re'si ve yuvarlak yüzeylerde uygulanan pürüzlülük/düzeltme. Tam ölçek CFD ile model ölçek tünel arasında eğri yüzeylerde ayrılma noktası farklı çıkabilir.
- **Topoğrafya:** ön kenar eğimi ve arazi basamaklaması tünele özgü yapaylıklardır; CFD'de aynen kopyalanıp kopyalanmayacağına bilinçli karar verilmeli.

## İlgili beceriler

- `tunel-yaklasan-akis` — hedef profil, türbülans, uzunluk ölçeği, PTS, topoğrafya modeli.
- `tunel-basinc-olcumu-ve-yukler` — basınç ölçümü, tepe değer, iklimle birleştirme, rapor.
- `tunel-diger-olcumler` — kuvvet terazisi, aeroelastik model (Re, Froude), ürünler.
