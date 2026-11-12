---
name: topografya-ve-sinoptik-olmayan-ruzgar
description: Hedef rüzgâr profili ayrı bir topografya benzetiminden geliyorsa (topography Method 1, empty domain'de topografyasız yeniden üretim) ya da fırtına inişi, hortum gibi sinoptik olmayan rüzgâr (non-synoptic wind, downburst, tornado) benzetimi sorulduğunda kullan; ASCE CWE Prestandard Bölüm 5.2 ve 5.3'ün ne istediğini ve neyi kapsam dışı bıraktığını söyler.
---

# Topografya ile değişmiş akış ve sinoptik olmayan rüzgâr (ASCE CWE Prestandard §5.2, §5.3)

Kaynak: PDF sayfa 53–55. Ayrıntı için `referans.md`.

## Ne zaman kullanılır

- Topografya etkisi, topografya bina benzetimine konmadan temsil edilecekse (Şekil 3-2'deki Yöntem 1): hedef profil ayrı bir topografya benzetiminden alınır ve topografyasız boş alanda yeniden üretilir.
- Kullanıcı fırtına inişi (downburst), gök gürültülü fırtına ya da hortum (tornado) yükünü CWE ile hesaplamak istediğinde: belgenin tutumunu doğru aktarmak için.

Topografya yakın çevre modeline konuyorsa (Yöntem 2) bu beceri değil `hesap-alani-ve-ag` (PO 6-4) geçerlidir.

## Adım adım — Topografya Yöntem 1 (§5.2)

1. Hedef profilleri ayrı topografya benzetiminden al. Belge bu topografya benzetiminin nasıl yapılacağını tarif etmez.
2. Topografya geometrisini içermeyen boş alan benzetimi kur ve hedef profilleri gelen konumda (incident location) yeniden üret (PO 5-6).
3. Hesap alanı boyutunu, ağ çözünürlüğünü ve bütün sınır koşullarını belgele (AC 5-6).
4. Gelen konumda farklı yüksekliklerde üç hız bileşeninin tam türbülans istatistiklerini (ortalama, rms, uzunluk ölçekleri, spektrumlar) ve basıncı raporla (AC 5-6).
5. Yatay düzlemlerde ve akış yönü/duvara dik düzlemlerde ortalama ve standart sapma hız ve basınç konturlarını çiz; profillerin alan içinde gerçek dışı değişmediğini bu çizimlerle doğrula (AC 5-6).
6. Topografya benzetiminin öngördüğü hedef alanın, uygulamaya ilişkin temel hız istatistikleri bakımından gelen konumda doğru üretildiğini göster (AC 5-6).
7. Bunu ilgili bütün rüzgâr yönleri için yinele; topografya etkisi yöne bağlıdır (AC 5-6).
8. `bos-alan-dogrulamasi` becerisindeki AC 5-9 denetimini uygula; Yöntem 1'de U ve I_u hata aralığı h_max'ın %100'üdür (üst %75 değil).

## Sinoptik olmayan rüzgâr (§5.3)

- Belge, sinoptik olmayan rüzgâr yükleri için olgun ve sektörde kullanıma hazır bir yaklaşımın henüz bulunmadığını söyler; bu yüzden bu Prestandard uygulanırken bu rüzgârların açık benzetiminin yapılması beklenmez (§1.5.1'e de gönderme yapar).
- Bu bölümde PO ya da AC maddesi yoktur; içerik yorumdur.
- Yorumdaki yöntem özeti:
  - Fırtına inişi: (1) deney düzeneğini taklit eden kurulumlar — duran, hareketli ya da darbeli çarpan jet (jetin boyutu ve momentumu akışı belirler) ya da rüzgâr üstünde panjur (louver) dizisi; (2) soğutma kaynak terimi (şiddeti, boyutu, ilerleme hızı belirleyici); (3) hava tahmin modelleri.
  - Hortum: (1) deney düzeneğini taklit eden hortum benzeri girdap; giriş yarıçapı r0, derinliği h0 ve teğetsel/radyal giriş hızı koşulları girdabı belirler; köşe akışı bölgesi yüksek hız ve basınç açığı nedeniyle özellikle önemlidir; seçenek olarak düşey panjur dizisi; (2) hortumu oluşturan baskın zorlama mekanizmalarını içeren benzetimler.
  - Seçenek yaklaşım: tam alanı modellemek yerine bu akışların belirli özelliklerini (ivmelenme, hücum açısı, akım çizgisi eğriliği) temsil etmek; etkin araştırma alanı.
  - Zemin pürüzlülüğü açık elemanlarla ya da duvar fonksiyonuyla alınabilir; mevcut çalışmaların çoğu düz zemin kullanmıştır.

## Zorunlu şartlar

- **PO 5-6** — Topografya benzetiminden gelen hedef profiller, topografyanın açık geometrisini içermeyen boş alan benzetiminde gelen konumda yeniden üretilir.
- **AC 5-6** — Alan boyutu, ağ, sınır koşulları belgelenir; üç hız bileşeninin tam türbülans istatistikleri ve basınç farklı yüksekliklerde raporlanır; iki tür düzlemde ortalama ve standart sapma konturları çizilir ve gerçek dışı değişim olmadığı doğrulanır; hedef alan gelen konumda doğru üretilir; bütün ilgili yönler için yapılır.
- **§5.3** — Zorunlu madde yok; sinoptik olmayan rüzgârın açık benzetimi bu Prestandard kapsamında beklenmez.

## Denetim listesi

- [ ] Topografya gerçekten bina benzetiminin dışında mı tutuluyor (Yöntem 1)?
- [ ] Boş alan benzetimi topografya geometrisini içermiyor mu?
- [ ] Alan boyutu, ağ ve bütün sınır koşulları belgelendi mi?
- [ ] Gelen konumda üç hız bileşeni için ortalama, rms, uzunluk ölçeği ve spektrum, birden çok yükseklikte raporlandı mı?
- [ ] Basınç da farklı yüksekliklerde raporlandı mı?
- [ ] Yatay ve akış yönü/düşey düzlemlerde ortalama ve standart sapma konturları var mı?
- [ ] Profillerin girişten sonra kısa mesafede bozulmadığı çizimlerle gösterildi mi?
- [ ] AC 5-9 hata aralığı h_max'ın %100'ü olarak mı alındı?
- [ ] İlgili bütün rüzgâr yönleri kapsandı mı?
- [ ] Sinoptik olmayan rüzgâr isteniyorsa, belgenin bunu kapsam dışı tuttuğu kullanıcıya açıkça söylendi mi?

## Sık yapılan hatalar

- Topografya benzetiminden gelen profili yalnızca girişe dayatmak: topografya yokken akış düz arazi denge sınır tabakasına geri döner (yorum).
- Topografya benzetimi ile bina benzetimi arasındaki denklem ve sayısal yöntem farkını göz ardı etmek; özellikle orta ölçek hava tahmin modellerinde (enerji ve nem denklemleri, kaba ağ) profiller giriş yakınında gerçek dışı değişebilir (yorum).
- Tek yönde doğrulayıp diğer yönlere genellemek.
- Yöntem 1'de hata aralığını üst %75 ile sınırlı bırakmak.
- §5.3'teki yorumu bir tasarım yöntemi gibi sunmak; belge fırtına inişi ve hortum için kabul ölçütü vermez.
- Belgenin topografya benzetiminin kendisi için yöntem verdiğini sanmak; vermez.

## İlgili beceriler

- `bos-alan-dogrulamasi` — §5.1, §5.4; AC 5-9 ölçütleri.
- `hesap-alani-ve-ag` — topografyanın yakın çevre modeline konması (PO 6-4), tıkanma hesabına katılması (AC 6-8b).
- `sinir-kosullari-ve-kalite` — topografya üzerinde pürüzlülük modeli (AC 6-11).
