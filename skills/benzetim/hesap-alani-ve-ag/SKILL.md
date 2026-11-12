---
name: hesap-alani-ve-ag
description: Bina aerodinamiği benzetimi için geometri modelini (study building, proximity model, radius of proximity, topography, appurtenances, porous components), hesap alanı boyutunu (computational domain, blockage ratio) ve ağı (mesh regions, refinement, IRQ) kurarken ya da denetlerken kullan; ASCE CWE Prestandard Bölüm 6.2, 6.3 ve 6.4 şartlarını verir.
---

# Hesap alanı ve ağ (ASCE CWE Prestandard §6.2, §6.3, §6.4)

Kaynak: PDF sayfa 59–64. Madde tablosu ve denklemler `referans.md` içinde.

## Ne zaman kullanılır

- İncelenen binanın (study building) ve çevresinin hangi ayrıntıyla modelleneceğine karar verilirken.
- Çevre binaların ne kadarının açıkça modelleneceği (yakın çevre modeli, proximity model) sorulduğunda.
- Hesap alanı (computational domain, CD) boyutları ve tıkanma oranı (blockage ratio, BR) hesaplanırken.
- Ağ bölgeleri (yaklaşan akış, yakın akış, yerel akış, uzak akış) ve incelme düzeyleri seçilirken.
- Çatı ekipmanı gibi eklentiler (appurtenances) ya da geçirgen bileşenler (porous components) modellenecekken.

## Temel tanımlar

- **İnceleme bölgesi (study region):** İncelenen binayı, açıkça modellenen çevresini ve yakın topografyayı saran kutu; yaklaşan akış bölgesini içermez (§1.8, s. 25).
- **Yakınlık yarıçapı (radius of proximity):** İncelenen bina merkezli çember; dışındaki açık geometrinin inceleme bölgesi aerodinamiğine doğrudan girişim etkisi yoktur (§1.8, s. 25).
- **h_s:** İncelenen bina yüksekliği h ile çevre binaların ortalama yüksekliğinden büyük olanı (§1.9, s. 26).
- **h_av:** Açıkça modellenen bütün binaların ortalama çatı yüksekliklerinin ortalaması (§1.9, s. 26).
- **B_y:** Açıkça modellenen bina, yapı ve topografyanın akış yönündeki izdüşümünün en büyük enine genişliği (§1.9, s. 26).
- **l_CD,xu, l_CD,xd, l_CD,y, l_CD,z:** Alanın rüzgâr üstü ve rüzgâr altı akış yönü uzunlukları, genişliği ve yüksekliği (Şekil 6-1c).

## Adım adım

1. **Ölçeği sabitle (§6.2).** Geometri tam ya da küçültülmüş ölçekte olabilir; yaklaşan akış ve bina benzetimlerinde aynı ölçek katsayısı kullanılır.
2. **İncelenen binayı modelle (PO 6-2).**
   - Dış basınç için: bina biçimi, köşe ayrıntıları, balkonlar ve büyük cephe öğeleri açıkça modellenir (AC 6-2a).
   - İç basınç doğrudan benzetimden alınacaksa: iç hacim ve açıklıkların gerekli ayrıntısı modellenir, geçirgenlik ve açıklık etkisi doğru temsil edilir; küçültülmüş ölçekte iç hacim tutarlı ölçeklenir (AC 6-2b).
   - Ayrıntı düzeyi, ilgilenilen büyüklükleri yöneten akış olaylarını yakalamaya yetmeli, gereksiz karmaşıklık getirmemeli.
3. **Yakın çevre modelini seç ve gerekçelendir (PO 6-3 / AC 6-3).** Yükü etkileyebilecek yakın binalar ve yapılar açıkça modellenir; seçim raporda gerekçelendirilir. Belge zorunlu bir yarıçap vermez; yorum, rüzgâr tüneli standardının (ASCE 49-21) tam ölçekte 240 m (787 ft) yaygın en küçük yarıçapını anar ve çok yüksek binalarda daha büyüğünün gerekebileceğini söyler.
4. **Topografya (PO 6-4).** Topografya yakın çevre modeline konuyorsa (Yöntem 2) yerel koşulları temsil eder; yükü etkileyebilecek yakın özellikler açıkça modellenir (AC 6-4a) ve seçim gerekçelendirilir (AC 6-4b). Yorum: topografya çıkış sınırında sıfır yüksekliğe yumuşatılarak indirilir.
5. **Eklentiler (PO 6-5).** Yükü istenen eklentiler ana yapının uygun modeli üzerinde doğrudan modellenir. Tam ölçekte hücre sayısı yeterli çözünürlüğe izin veriyorsa binayla birlikte (AC 6-5a); olmuyorsa eklenti konumundaki akış belirlenip daha uygun ölçekte yeniden üretilerek yük alınabilir (AC 6-5b). Küçültülmüş ölçekte Reynolds sayısından bağımsız çözüm gösterilir (AC 6-5c); ölçek ve ayrıntı gerekçelendirilir (AC 6-5d).
6. **Geçirgen bileşenler (PO 6-6 / AC 6-6).** Ya bütün ayrıntı açıkça modellenir ya da aerodinamik etki matematiksel olarak temsil edilir. Kabalaştırılmış geometri kullanılırsa ilgilenilen büyüklüğün doğru temsil edildiği doğrulamayla (validation) gösterilir; geçirgen bölge içindeki ve çevresindeki ağ çözünürlüğü gösterilir.
7. **Binayı gelen konuma yerleştir (PO 6-7 / AC 6-7).** İnceleme bölgesinin en rüzgâr üstü binası ya da topografik özelliği, boş alan benzetiminin hedefi tutturduğu gelen konuma (incident location) konur. Alan yüksekliği boş alan benzetimindekine eşit; genişlik ve akış yönü uzunluk ona eşit ya da daha büyük olur.
8. **Sınır ve tıkanma etkisini denetle (PO 6-8).**
   - Akış yönü (AC 6-8a): giriş, rüzgâr üstü durma bölgesinin girişten bağımsız tam gelişmesine yetecek kadar uzakta; çıkış, yapay basınç birikimi ve iz–çıkış etkileşimi olmayacak kadar uzakta. Sayısal kat verilmemiştir.
   - Tıkanma (AC 6-8b): BR = (B_y · h_s) / (l_CD,y · l_CD,z) ≤ %3; BR_y = B_y / l_CD,y ≤ %17; BR_z = h_s / l_CD,z ≤ %17.
   - Çevre binalı durumda h_s yerine h_av kullanılır; topografya varsa tıkanma hesabına katılır ve h_s, bina yüksekliği ile topografya yüksekliğinden (en alçak etekten en yüksek tepeye) büyüğü olur.
   - Bu şartlar gereken her rüzgâr yönü için sağlanır (§6.3).
9. **Ağ bölgelerini kur (PO 6-9).**
   - Yaklaşan akış bölgesi: boş alan benzetimindekiyle aynı çözünürlük (AC 6-9a).
   - Yakın akış bölgesi: yaklaşan akış bölgesiyle aynı ya da daha ince (AC 6-9b).
   - Yerel akış bölgesi: gövde kaynaklı akış yapılarını çözecek biçimde daha ince; binaya yakınlığa göre kademeli; en ince ağ bina duvarı yakınında; düzeyler arası geçiş kademeli (AC 6-9c).
   - Uzak akış bölgesi: ilgilenilen bölgelerdeki akışı etkilemeyecek ölçüde kabalaştırılabilir (AC 6-9d).
   - Açık geometrili geçirgen bileşende iç hacimler anlamlı ölçüde ayrıklaştırılır (AC 6-9f).
10. **Ağı belgele ve yeterliliğini göster (AC 6-9e).** Topoloji, bölge çözünürlükleri, geçişler ve kalite ölçütleri raporlanır. Yeterlilik basınç ve hız spektrumlarıyla ve ağ bağımlılığı çözümlemesiyle gösterilir; izleme noktalarında çözünürlük kalite göstergesi (index of resolution quality, IRQ) %75 olmalıdır. IRQ hesabı için `sinir-kosullari-ve-kalite` (§6.6.4).

## Zorunlu şartlar

- **§6.2** — Yaklaşan akış ve bina benzetimlerinde aynı ölçek katsayısı.
- **PO 6-2 / AC 6-2a, 6-2b** — Bina ayrıntısı; dış basınç için biçim, köşe, balkon, büyük cephe öğeleri; iç basınç için iç hacim ve açıklıklar.
- **PO 6-3 / AC 6-3** — Etkileyebilecek yakın binalar açıkça modellenir; seçim gerekçelendirilir.
- **PO 6-4 / AC 6-4a, 6-4b** — Yakın çevre modelindeki topografya yerel koşulları temsil eder; seçim gerekçelendirilir.
- **PO 6-5 / AC 6-5a–d** — Eklentiler; Reynolds bağımsızlığı; ölçek ve ayrıntı gerekçesi.
- **PO 6-6 / AC 6-6** — Geçirgen bileşenler; kabalaştırma için doğrulama; ağ gösterimi.
- **PO 6-7 / AC 6-7** — En rüzgâr üstü bina/topografya gelen konumda; alan yüksekliği boş alanla eşit; genişlik ve uzunluk eşit ya da büyük.
- **PO 6-8 / AC 6-8a, 6-8b** — Sınır ve tıkanma etkisi yok; BR ≤ %3, BR_y ≤ %17, BR_z ≤ %17 (Denklem 6-1, 6-2).
- **PO 6-9 / AC 6-9a–f** — Ağ kalitesi ve bölge çözünürlükleri; IRQ %75.

## Denetim listesi

- [ ] Boş alan ve bina benzetimi aynı geometri ölçeğinde mi?
- [ ] Bina biçimi, köşe ayrıntıları, balkonlar ve büyük cephe öğeleri modelde var mı?
- [ ] İç basınç benzetimden alınıyorsa iç hacim ve açıklıklar modellendi mi?
- [ ] Yakın çevre modelinin kapsamı raporda gerekçelendirildi mi?
- [ ] Topografya modele konduysa seçimi gerekçelendirildi mi?
- [ ] En rüzgâr üstü bina ya da topografik özellik, boş alanda doğrulanan gelen konumda mı duruyor?
- [ ] Alan yüksekliği boş alan benzetimiyle aynı mı?
- [ ] Alan genişliği ve uzunluğu boş alandakinden küçük değil mi?
- [ ] BR ≤ %3 mü?
- [ ] BR_y ≤ %17 ve BR_z ≤ %17 mi?
- [ ] Çevre binalı durumda h_av, topografyalı durumda topografya yüksekliği hesaba katıldı mı?
- [ ] Tıkanma ve alan şartları her rüzgâr yönü için ayrı ayrı sağlanıyor mu?
- [ ] Yaklaşan akış bölgesi ağı boş alandakiyle aynı mı?
- [ ] Yakın akış bölgesi yaklaşan akış bölgesinden kaba değil mi?
- [ ] En ince ağ bina duvarı yakınında mı ve düzey geçişleri kademeli mi?
- [ ] Ağ topolojisi, bölge çözünürlükleri, geçişler ve kalite ölçütleri raporda mı?
- [ ] İzleme noktalarında IRQ en az %75 mi?
- [ ] Küçültülmüş ölçekte Reynolds sayısından bağımsızlık gösterildi mi?

## Sık yapılan hatalar

- Çevre binaları ekleyince alanı gelen konumu kaydıracak biçimde yeniden kurmak; en rüzgâr üstü bina boş alanda doğrulanan konuma oturmalı.
- Yalnızca alan tıkanmasını (%3) denetleyip yanal ve düşey %17 sınırlarını atlamak.
- Tıkanmayı tek yön için hesaplamak; izdüşüm genişliği B_y yöne göre değişir.
- Çevre binalı durumda yükseklik olarak h_av kullanılması gerektiğini gözden kaçırmak.
- Bina benzetiminde yaklaşan akış bölgesi ağını değiştirmek (boş alan doğrulamasını geçersiz kılar).
- 240 m yarıçapı zorunlu şart gibi sunmak; yorumdur ve ASCE 49-21'e atıftır, zorunlu olan gerekçelendirmedir.
- Belgede olmayan alan boyu katlarını (örneğin rüzgâr üstü/altı için "kaç H") bu bölüme atfetmek; §6.3 yalnız nitel şart ve tıkanma sınırı verir.
- Düzeyler arasında ani hücre boyu sıçraması bırakmak; yüksek en-boy oranlı hücreler kullanmak (yorumda kaçınılması önerilir).

## İlgili beceriler

- `bos-alan-dogrulamasi` — gelen konumun doğrulanması, AC 5-1 alan boyutu, AC 5-2 çözünürlük.
- `sinir-kosullari-ve-kalite` — duvar koşulu, y+, IRQ hesabı, zaman adımı, örnekleme süresi.
- `topografya-ve-sinoptik-olmayan-ruzgar` — topografyanın alan dışında tutulduğu Yöntem 1.
