---
name: sinir-kosullari-ve-kalite
description: Bina aerodinamiği LES benzetiminde sınır koşullarını (no-slip wall, wall model, y+, reference static pressure) kurarken ve kalite güvencesini (solver convergence, contour plots, monitoring probes, statistical convergence, sampling duration, mesh sensitivity, IRQ, time-step sensitivity, CFL) yaparken ya da raporlarken kullan; ASCE CWE Prestandard Bölüm 6.1, 6.5 ve 6.6 şartlarını verir.
---

# Sınır koşulları ve kalite güvencesi (ASCE CWE Prestandard §6.1, §6.5, §6.6)

Kaynak: PDF sayfa 59 ve 64–68. Madde tablosu ve denklemler `referans.md` içinde.

## Ne zaman kullanılır

- Boş alan doğrulaması bitmiş, bina hesap alanına konmuşken: kurulumun boş alanla tutarlılığını denetlemek için.
- Bina yüzeyinde duvar işlemi (çözülmüş duvar mı, duvar modeli mi) seçilirken.
- Referans statik basıncın nereden okunacağı sorulduğunda.
- Koşu süresi, başlangıç geçişi, ağ duyarlılığı, zaman adımı duyarlılığı planlanırken.
- Bina benzetimi raporunun kalite güvencesi bölümü yazılırken ya da denetlenirken.

## Adım adım

1. **Boş alanla aynı kurulumu koru (PO 6-1 / AC 6-1).** Geometri ve hız ölçeği, çözücü, sayısal yöntemler, türbülans modeli, zemin duvar modeli ve sınır koşulları yaklaşan akış benzetimindekiyle aynı olur. Amaç, bina benzetiminin aynı fiziksel bölgede boş alan sonucunu vermesidir.
2. **Bina yüzeyini kur (PO 6-10).**
   - Yüzey kaymaz (no-slip) duvardır; duvar yakını işlem, duvar yakını ağ çözünürlüğüyle tutarlı olur (AC 6-10a).
   - Duvar yakını akış yeterince çözülmüşse (y+ = y·u*/ν < 5) kaymazlık doğrudan uygulanır; daha az çözülmüşse duvar modeli kullanılır (AC 6-10a).
   - Geçirgen yüzey gibi özel sınırlar için ayrı doğrulama yapılır (AC 6-10a).
   - Bina yuvarlak biçimliyse (ayrılma yeri keskin kenarla belirlenmiyorsa) duvar modelinin etkisi incelenir (AC 6-10b).
   - Duvar yakını çözünürlüğü ya da duvar modeli değiştirilerek ek koşular yapılır ve duvar işleminin basınç dağılımına etkisi sayıya dökülür (AC 6-10c).
3. **Diğer sınırları kur (PO 6-11 / AC 6-11).** Giriş, çıkış, zemin, yanlar ve üst §5.1.2 ve §5.1.3'e uyar. Topografya modeli alandaysa topografyanın arazi pürüzlülüğü de uygun bir pürüzlülük modeliyle temsil edilir. Yorum: ormanlık alanda gölgelik (canopy) modeli, yalnız z0'a dayanan duvar fonksiyonundan daha güvenilirdir.
4. **Çözücü yakınsamasını yönet (AC 4-6c).** Her zaman adımında çözüm yeterince yakınsar; ölçüt koşu boyunca sağlanır; ölçüt ve denetimler raporlanır.
5. **Akış alanı çizimlerini üret (PO 6-12 / AC 6-12a).** Benzetilen her rüzgâr yönü için rüzgâr hızı ve basıncın ortalama, standart sapma (ya da türbülans şiddeti) ve anlık görüntü konturları; enterpolasyonsuz, hücre merkezi değerleriyle:
   - Yatay düzlemler: h/2, 2h/3, h ve h + 5 m (16 ft); en az ilk çevre bina sırasını kapsayan alan.
   - Bina(lar)ın ortasından geçen düşey düzlem(ler); aynı kapsam.
   - Çizimler ayrılma bölgelerini (çatı, yanlar) ve izi göstermeli.
6. **İzleme noktalarını tanımla (AC 6-12b).** Bina yüksekliği boyunca ve binadan yaklaşık 50 m (160 ft) uzağa kadar nokta sondaları; yerleri geometriye göre seçilir; rüzgâr üstü akışı (özellikle rüzgâr üstü binaların izlerini) ve bina izini yakalar. Her nokta için: hız ve basınç zaman işaretinin temsil edici bir bölümü; hızın ortalaması, standart sapması ve türbülans şiddeti; hız spektrumu.
7. **Yüzey basıncı çizimleri ve basınç noktaları (PO 6-13).**
   - Bütün cephelerde, çatıda ve gerekiyorsa eklentilerde ortalama ve standart sapma basınç konturları; kenar ve köşelerdeki yüksek gradyan bölgelerine özel dikkat (AC 6-13a).
   - Basınç noktaları ASCE/SEI 49-21 yönergelerine göre yerleştirilir (AC 6-13b).
   - Nokta yoğunluğu ana taşıyıcı sistem (MWFRS) ve kaplama (C&C) çalışmaları için yüzeydeki değişimi yakalamaya yeter (AC 6-13c); örnekleme çözünürlüğü seçimi gerekçelendirilir (AC 6-13d).
8. **Referans statik basıncı al (AC 6-13e).** Referans basınç noktası modelden, yakın çevre modelinden ve sınırlardan etkilenmeyecek biçimde konumlanır; inceleme bölgesinin doğrudan üstüne konan bir statik basınç izleme noktası kullanılır.
9. **İstatistik yakınsamayı göster (PO 6-14 / AC 6-14).** İzleme noktalarında hızın ortalaması ve standart sapması ile ilgilenilen yük büyüklüklerinin ortalama, standart sapma ve tepe değerleri yakınsamış olmalı. Benzetim süresi, hedef bina yüksekliğindeki akış yönü integral zaman ölçeğinin 500 katından büyük olur. Yorum: en basit denetim büyüyen pencere; tepe değerler için blok en büyükleri (block maxima) ya da eşik üstü tepeler (peaks-over-threshold).
10. **Ağ çalışması yap (PO 6-15 / AC 6-15a, 6-15b).** Proje için en az iki rüzgâr yönünde. İzleme noktalarında akış ve basınç alanında IRQ en az %75; iki ağ arasındaki yük büyüklüğü farkları raporlanır. IRQ hesabı (yorum): en çok üç ağ (kaba, orta, ince), ardışık inceltme katsayısı r; IRQ = k_çözülen / k_toplam, k_toplam = k_çözülen + a_k·Δ^p (Denklem 6-3 – 6-6, `referans.md`).
11. **Zaman adımı duyarlılığını incele (PO 6-16 / AC 6-16).** Bina çevresindeki ve hedef bina ile rüzgâr üstü binalar arasındaki temel konumlarda hız spektrumları çizilir; ağ boyutundan ve zaman adımından gelen kesme çizimde işaretlenir. Yorum: zaman adımını yarıya indirip spektrumları karşılaştırmak iyi bir yöntemdir; ya da ağ duyarlılığı çalışmasında CFL sayısını sabit tutmak yeter.

## Zorunlu şartlar

- **PO 6-1 / AC 6-1** — Boş alanla aynı ölçek, çözücü, sayısal yöntem, türbülans modeli, zemin duvar modeli, sınır koşulları.
- **PO 6-10 / AC 6-10a–c** — Kaymaz duvar; y+ < 5 ise doğrudan, değilse duvar modeli; yuvarlak biçimde duvar modeli etkisi; ek koşularla etkinin sayıya dökülmesi.
- **PO 6-11 / AC 6-11** — Diğer sınırlar §5.1.2 ve §5.1.3'e göre; topografya pürüzlülüğü modellenir.
- **AC 4-6c (§6.6.1)** — Her zaman adımında yakınsama; ölçüt ve denetim raporu.
- **PO 6-12 / AC 6-12a, 6-12b** — Dört yatay düzlem ve düşey düzlemde konturlar; ~50 m içinde izleme noktaları ve bunların zaman işareti, istatistiği, spektrumu.
- **PO 6-13 / AC 6-13a–e** — Yüzey basıncı konturları; ASCE/SEI 49-21'e göre basınç noktaları; yeterli nokta yoğunluğu ve gerekçesi; referans statik basınç inceleme bölgesinin üstünde.
- **PO 6-14 / AC 6-14** — İstatistik yakınsama; süre > 500 akış yönü integral zaman ölçeği (hedef bina yüksekliğinde).
- **PO 6-15 / AC 6-15a, 6-15b** — En az iki yönde ağ çalışması; IRQ ≥ %75; farkların raporu; izleme noktalarının tanımı.
- **PO 6-16 / AC 6-16** — Zaman adımı duyarlılığı; spektrumlarda ağ ve zaman adımı kesmesi işaretli.

## Denetim listesi

- [ ] Çözücü, sayısal şemalar, alt ızgara modeli, zemin duvar modeli ve sınır koşulları boş alan koşusuyla birebir aynı mı?
- [ ] Bina yüzeyi kaymaz duvar mı?
- [ ] y+ < 5 değilse duvar modeli kullanılıyor mu?
- [ ] Yuvarlak biçimli binada duvar modelinin etkisi incelendi mi?
- [ ] Duvar işleminin basınç dağılımına etkisi ek koşularla sayıya döküldü mü?
- [ ] Topografya alandaysa pürüzlülüğü modellendi mi?
- [ ] Her zaman adımında yakınsama ölçütü sağlandı ve raporlandı mı?
- [ ] h/2, 2h/3, h ve h + 5 m yatay düzlemlerinde konturlar her yön için var mı?
- [ ] Konturlar enterpolasyonsuz hücre merkezi değerleriyle mi çizildi?
- [ ] Düzlemler en az ilk çevre bina sırasını kapsıyor mu?
- [ ] İzleme noktaları bina yüksekliği boyunca ve ~50 m içinde, rüzgâr üstü izleri ve bina izini kapsayacak biçimde mi?
- [ ] Her izleme noktası için zaman işareti, ortalama, standart sapma, türbülans şiddeti ve spektrum sunuldu mu?
- [ ] Bütün cephelerde ve çatıda ortalama ve standart sapma basınç konturları var mı?
- [ ] Basınç noktası düzeni ASCE/SEI 49-21'e uygun ve yoğunluğu gerekçelendirilmiş mi?
- [ ] Referans statik basınç inceleme bölgesinin doğrudan üstünden, etkilenmeyen bir noktadan mı alınıyor?
- [ ] Benzetim süresi 500 integral zaman ölçeğinden uzun mu?
- [ ] Yük büyüklüklerinin ortalama, standart sapma ve tepe değerlerinin yakınsadığı gösterildi mi?
- [ ] Ağ çalışması en az iki rüzgâr yönünde yapıldı mı ve IRQ ≥ %75 mi?
- [ ] İki ağ arasındaki yük farkları raporlandı mı?
- [ ] Spektrumlarda ağ ve zaman adımı kesmeleri işaretli mi?

## Sık yapılan hatalar

- Bina koşusunda boş alandan farklı şema, alt ızgara modeli ya da zemin modeli kullanmak; boş alan doğrulaması geçerliliğini yitirir.
- y+ değerine bakmadan kaymaz duvarı doğrudan uygulamak ya da tersine, ince ağda duvar modelini sorgulamadan bırakmak.
- Keskin kenarlı olmayan binada duvar modeli duyarlılığını atlamak.
- Referans basıncı girişten, çıkıştan ya da bina etkisindeki bir noktadan almak.
- Konturları düğümlere enterpolasyonla yumuşatarak çizmek; belge hücre merkezi değerini ister.
- 500 integral zaman ölçeğini toplam süre yerine farklı bir zaman ölçeğiyle (örneğin akış geçiş süresiyle) karıştırmak; integral zaman ölçeği, integral uzunluk ölçeğinin aynı yükseklikteki ortalama hıza bölümüdür (§1.8).
- Ağ çalışmasını tek yönde yapmak; en az iki yön istenir.
- IRQ hesabında p için kuramsal mertebeyi körü körüne almak; kestirilen mertebe kuramsaldan belirgin yüksekse bu, alt ızgara katkısını az gösterebilir (yorum).
- Örtük LES'te ağdan tam bağımsızlık beklemek; yorum, bunun ancak doğrudan sayısal benzetim (DNS) inceliğinde olacağını söyler.
- Bu bölümlerde olmayan şeyleri atfetmek: toplam rüzgâr yönü sayısı, sayısal CFL sınırı ve bina benzetimi için referans hız tanımı §6.1, §6.5, §6.6'da bulunamadı.

## İlgili beceriler

- `bos-alan-dogrulamasi` — §5.1.2, §5.1.3 sınır koşulları; AC 5-9 gelen akış ölçütleri.
- `hesap-alani-ve-ag` — §6.2–6.4: geometri, tıkanma, ağ bölgeleri, AC 6-9e.
- `topografya-ve-sinoptik-olmayan-ruzgar` — §5.2, §5.3.
