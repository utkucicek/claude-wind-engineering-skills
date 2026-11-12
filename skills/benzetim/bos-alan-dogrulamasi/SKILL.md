---
name: bos-alan-dogrulamasi
description: Bina eklenmeden önce boş hesap alanında (empty domain) yaklaşan akışın (approach flow) hedef atmosferik sınır tabakasını gelen konumda (incident location) tutturduğunu kanıtlamak gerektiğinde kullan; giriş türbülansı (precursor, recycling, synthetic inflow), zemin pürüzlülüğü z0, U ve I_u profil hatası, integral length scale, spectrum, cutoff frequency ve basınç oynaması ölçütlerini ASCE CWE Prestandard Bölüm 5.1 ve 5.4'e göre denetler.
---

# Boş alan doğrulaması (ASCE CWE Prestandard §5.1 ve §5.4)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 5.1 ve 5.4 (PDF sayfa 49–58). Madde ayrıntıları ve denklemler için `referans.md` dosyasına bak.

## Ne zaman kullanılır

- İki adımlı benzetim sürecinin ilk adımı kurulurken: bina olmayan hesap alanında (computational domain, CD) sinoptik rüzgâr için yaklaşan akış benzetimi.
- Giriş türbülansı yöntemi seçilirken ya da girişten gelen konuma kadar türbülansın değişimi sorgulanırken.
- "Boş alan profili hedefi tutuyor mu?" sorusuna sayısal ölçütle cevap verilecekken (AC 5-9).
- Yaklaşan akış bölgesindeki ağın yeterli frekansı çözüp çözmediği denetlenecekken (AC 5-2, AC 5-10).
- Boş alan koşusunun raporu yazılırken (hangi çizimler, hangi istatistikler).

Topografya ile değiştirilmiş hedef profil ya da sinoptik olmayan rüzgâr söz konusuysa `topografya-ve-sinoptik-olmayan-ruzgar` becerisine geç.

## Temel kavramlar

- **Gelen konum (incident location):** Hesap alanında bir binanın ya da topografyanın eklendiği en rüzgâr üstü konum (§1.8, s. 24; AC 4-1, s. 43). PO 5-3 bunu bina benzetimindeki en rüzgâr üstü bina ya da yapının konumuyla çakıştırır. Çevre binalar açıkça modelleniyorsa bu, hedef binanın yeri değil, modellenen çevrenin rüzgâr üstü kenarıdır (AC 6-7 ile tutarlı).
- **Yaklaşan akış bölgesi (approach flow region):** Giriş sınırından inceleme bölgesine (study region) kadar olan ve onu içeren ağ bölgesi (§1.8, s. 24).
- **h_max:** Binanın yüksekliği ile çevre binaların ortalama yüksekliğinden büyük olanı (§1.9, s. 26).
- **L_b:** İncelenen probleme uygun karakteristik boyut; **n:** tam çözülen en yüksek frekans (Hz); **U:** yükü üreten yerel referans hız (AC 5-2).

## Adım adım

1. **Hedefi sabitle.** Hedef profiller (U, türbülans şiddetleri, uzunluk ölçekleri, z0) Bölüm 3'ten gelir. Arazi pürüzlülüğü rüzgâr yönüne göre değişiyorsa her farklı açıklık (exposure) koşulu ayrı bir boş alan doğrulaması ister (AC 5-3).
2. **Hesap alanını boyutlandır (PO 5-1 / AC 5-1).**
   - Yükseklik: sınır tabakasının ilgili kısmını alsın ve bina benzetiminin düşey tıkanma şartını sağlasın (§6.3'e bak; `hesap-alani-ve-ag`).
   - Akış yönü uzunluk: giriş ile bina benzetimindeki ilk bina arası uzaklıktan büyük olsun ve ilk bina konumunda akış yönü uzunluk ölçeklerini taşıyabilsin.
   - Genişlik: yanal uzunluk ölçeklerini taşıyabilsin.
   - Metin bu boyutlar için sayısal kat (örneğin "kaç H") vermez.
3. **Yaklaşan akış bölgesi ağını seç (PO 5-2 / AC 5-2).** Tam çözülen en yüksek indirgenmiş frekans (reduced frequency) kaplama (cladding) yükleri için n·L_b/U ≥ 2, toplam (global) yükler için n·L_b/U ≥ 1 olmalı; bu frekans spektrumun atalet alt aralığında (inertial subrange) kalmalı.
4. **Giriş türbülansı yöntemini seç (PO 5-3; yorum).** Metin yöntem dayatmaz; üç aileyi ve tuzaklarını yorumda anlatır:
   - Öncül benzetim (precursor) ve geri besleme (recycling): önceden koşulup veri tabanına yazılabilir. Yetersiz uzunlukta periyodik/geri beslemeli kurulum büyük yapıların kilitlenmesine yol açabilir; periyodik koşulu kaydırmak gerekebilir.
   - Yapay türbülans üretimi (synthetic): verimli, ama (i) sahte basınç oynamaları üretebilir, (ii) girişte verilen türbülans şiddeti gelen konuma kadar çoğu zaman azalır. Bu yüzden girişten gelen konuma gelişim yakından izlenmeli; belirgin değişim varsa giriş istatistikleri, hedef aşağıda tutacak biçimde ayarlanabilir.
   - Doğru kurulumu bulmak deneme-yanılma isteyebilir (rüzgâr tünelinde pürüzlülük elemanı ayarına benzetilir).
5. **Zemin koşulunu kur (PO 5-4 / AC 5-4).** Hedef z0 için gelen akışı yeniden üretmeli. İki yol (yorum): pürüzlülük elemanlarını açıkça çözmek ya da duvar yakını modeli. Duvar fonksiyonu kullanılıyorsa pürüzlü arazi üzerindeki rüzgâr için yazılmış olduğunu ve girdisinin z0 olduğunu doğrula; kum tanesi (sand-grain) pürüzlülüğüne dayalı fonksiyonlar doğrudan uygun değildir.
6. **Yan, üst ve çıkış sınırlarını kur (PO 5-5 / AC 5-5).** Metin yalnızca "uygun" olmasını ister; yorumdaki seçenekler: yanlarda periyodik; üstte kaygan duvar ya da uzak alan basıncı; ya da tüneldeki gibi kaymaz duvarlar (yeterince uzaksa); çıkışta sıfır gradyan ya da taşınımlı (convective) koşul, gerekirse sönümleme.
7. **Koş ve çözücü yakınsamasını belgele (AC 4-6b).** Yakınsama ölçütü koşu boyunca uygulanır ve raporlanır. Yorum: yinelemeli çözücüde her zaman adımında artıklarda üç-dört mertebe düşüş beklenir.
8. **Başlangıç geçişini at, istatistik yakınsamasını göster (PO 5-7 / AC 5-7).** T_init (atılan başlangıç geçişi) ve T_avg (ortalama alma süresi) raporlanır; bina yüksekliğinde ortalama hız ve türbülans şiddetlerinin yakınsadığı gösterilir. Metin burada sayısal bir süre vermez; yorumdaki en basit yöntem büyüyen pencereyle ortalama ve standart sapmayı izlemektir.
9. **Alan çizimlerini üret (PO 5-8 / AC 5-8).** Her farklı sınır tabakası koşulu için: anlık hız ve basınç görüntüleri; ortalama akış yönü hızı, üç hız bileşeninin standart sapması (ya da türbülans şiddetleri), ortalama basınç ve basınç oynamasının standart sapması. Düzlemler: (1) genişlik ortasında düşey düzlem, (2) bina yüksekliğinde yatay düzlem.
10. **Gelen konumda hedefle karşılaştır (PO 5-9 / AC 5-9).** Genişlik ortasında ve merkez hattından ölçülen 1/3 genişlik konumlarında:
    - (1a) (z0/L_b) model = (z0/L_b) prototip, üç kat içinde.
    - (1b) U profili hatası < %10, h_max'ın üst %75'i boyunca; Topografya Yöntem 1'de aralık h_max'ın %100'ü. Ölçü, Denklem 5-1'deki yükseklik boyunca integral alınmış bağıl hatadır (≤ 0,1).
    - (2) I_u profili için aynı şart, Denklem 5-2.
    - (3) Gerekli integral uzunluk ölçeği bileşenleri hedefin üç katı içinde.
    - (4) Gerekli hız bileşenlerinin güç spektrumları çatı/tepe yüksekliğinde çizilir.
    - (5) Gerekli Reynolds gerilmesi profilleri çizilir; çapraz spektrumlar çatı/tepe yüksekliğinde çizilir.
    - (6) Basınç oynamasının standart sapma profili çizilir; çatı/tepe referans hızıyla hesaplanan dinamik basıncın %10'unu aşmamalı.
11. **Ağ yeterliliğini spektrumda göster (PO 5-10 / AC 5-10).** Kesme frekansı (cutoff frequency) akış yönü hız spektrumunda işaretlenir ve AC 5-2'yi sağladığı doğrulanır. Kesme frekansı için yorumdaki yol Denklem 5-3 – 5-5'tir (5-3 metinde bozuk; `referans.md`).
12. **Şart sağlanmıyorsa** girişi/zemini/ağı değiştirip 7–11'i yinele; bina benzetimine ancak ondan sonra geç (bkz. `sinir-kosullari-ve-kalite`, PO 6-1).

## Zorunlu şartlar

- **PO 5-1 / AC 5-1** — Alan boyutu hedef akışı doğru temsil etmeli, sınır etkisi olmamalı; yükseklik, akış yönü uzunluk ve genişlik için yukarıdaki nitel şartlar.
- **PO 5-2 / AC 5-2** — n·L_b/U en az 2 (kaplama), en az 1 (toplam yük); bu frekans atalet alt aralığında.
- **PO 5-3** — Giriş koşulu, model ve ağla birlikte, gelen konumda hedef türbülanslı akışı üretmeli; gelen konum en rüzgâr üstü bina/yapının konumu.
- **AC 5-3** — Açıklık yöne göre değişiyorsa her farklı açıklık koşulu için kalite gösterilir.
- **PO 5-4 / AC 5-4** — Zemin koşulu hedef z0 için gelen akışı yeniden üretmeli.
- **PO 5-5 / AC 5-5** — Yan, üst, çıkış koşulları hedef akışın doğru modellenmesine izin vermeli.
- **AC 4-6b (§5.4.1)** — Yakınsama ölçütü koşu boyunca uygulanır ve raporlanır.
- **PO 5-7 / AC 5-7** — T_init ve T_avg raporlanır; bina yüksekliğinde U ve türbülans şiddetlerinin yakınsadığı gösterilir.
- **PO 5-8 / AC 5-8** — Anlık ve istatistik alan çizimleri, iki düzlemde, her farklı sınır tabakası koşulu için.
- **PO 5-9 / AC 5-9** — Gelen konumda altı maddelik karşılaştırma (yukarıda adım 10).
- **PO 5-10 / AC 5-10** — Kesme frekansı spektrumda gösterilir, AC 5-2 ile doğrulanır.

## Denetim listesi

- [ ] Gelen konum, bina benzetiminde en rüzgâr üstü binanın/topografyanın geleceği yer olarak mı tanımlandı (hedef binanın yeri değil)?
- [ ] Alan yüksekliği bina benzetimindeki düşey tıkanma şartını da sağlıyor mu?
- [ ] Giriş–gelen konum uzaklığı, bina benzetimindeki giriş–ilk bina uzaklığından büyük mü?
- [ ] Kaplama yükü isteniyorsa n·L_b/U ≥ 2, yalnız toplam yük isteniyorsa ≥ 1 sağlanıyor mu?
- [ ] Bu en yüksek frekans spektrumda atalet alt aralığının içinde mi?
- [ ] Duvar fonksiyonu pürüzlü arazi rüzgârı için mi yazılmış ve girdisi z0 mı?
- [ ] (z0/L_b) model ile prototip üç kat içinde mi?
- [ ] U için Denklem 5-1 hatası ≤ 0,1 mi (h_max'ın üst %75'i; Topografya Yöntem 1'de %100)?
- [ ] I_u için Denklem 5-2 hatası ≤ 0,1 mi (aynı aralık)?
- [ ] Karşılaştırma hem genişlik ortasında hem 1/3 genişlik konumlarında yapıldı mı?
- [ ] Gerekli integral uzunluk ölçekleri hedefin üç katı içinde mi?
- [ ] Spektrumlar ve çapraz spektrumlar çatı/tepe yüksekliğinde çizildi mi; Reynolds gerilmesi profilleri çizildi mi?
- [ ] Basınç oynaması standart sapması, çatı yüksekliği dinamik basıncının %10'unun altında mı?
- [ ] T_init ve T_avg raporlandı mı; bina yüksekliğinde yakınsama gösterildi mi?
- [ ] İki düzlemde anlık ve istatistik alan çizimleri var mı?
- [ ] Kesme frekansı spektrum çiziminde işaretli mi?
- [ ] Yöne bağlı her farklı açıklık koşulu için bunların hepsi yinelendi mi?
- [ ] Çözücü yakınsama ölçütü ve denetimi raporda mı?

## Sık yapılan hatalar

- Doğrulamayı hedef binanın konumunda yapmak; çevre binalar modelleniyorsa gelen konum çevrenin rüzgâr üstü kenarıdır.
- Giriş profilinin hedefi tutmasını yeterli saymak; şart girişte değil gelen konumdadır ve yapay türbülansta şiddet yol boyunca düşebilir.
- Yalnızca ortalama hız profilini denetlemek; I_u, uzunluk ölçeği, spektrum ve basınç oynaması da şarttır.
- Yapay girişin ürettiği sahte basınç oynamasını denetlememek (AC 5-9 madde 6).
- Makine mühendisliği tipi kum tanesi pürüzlülüklü duvar fonksiyonuna z0 girmek.
- Yalnızca merkez hattında karşılaştırma yapmak; 1/3 genişlik konumları da istenir.
- Kesme frekansını ağdan tahmin edip spektrumda göstermemek.
- Bina benzetiminde boş alandan farklı ağ, çözücü, alt ızgara modeli ya da sınır koşulu kullanmak (AC 6-1, AC 6-9a).
- Metinde olmayan sayıları (alan boyu için "5H", süre için sabit bir değer) bu bölüme atfetmek; §5.1 ve §5.4 bunları vermez.

## İlgili beceriler

- `topografya-ve-sinoptik-olmayan-ruzgar` — §5.2, §5.3.
- `hesap-alani-ve-ag` — §6.2–6.4: tıkanma oranları, ağ bölgeleri.
- `sinir-kosullari-ve-kalite` — §6.1, §6.5, §6.6: bina benzetiminde aynı kurulumun korunması, IRQ, örnekleme süresi.
