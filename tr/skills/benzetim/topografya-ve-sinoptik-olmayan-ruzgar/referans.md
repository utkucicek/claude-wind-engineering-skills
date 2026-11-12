# Referans: ASCE CWE Prestandard §5.2 ve §5.3

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Sayfa numaraları PDF sayfa sırasıdır. Özetler kendi cümlelerimizle yazılmıştır.

Tür: ZORUNLU = shall, ÖNERİ = should, YORUM = commentary.

## Maddeler

| Madde | Tür | Özet | Sayısal ölçüt (birimiyle) | PDF sayfası |
|---|---|---|---|---|
| §5.2 giriş | Çerçeve | Topografya, bina benzetimine konmadan temsil ediliyorsa (Şekil 3-2, Yöntem 1) hedef akış ayrı bir topografya benzetiminden alınır. Belge o topografya benzetiminin yöntemini tarif etmez. | yok | 53 |
| PO 5-6 | ZORUNLU | Topografya benzetiminden alınan hedef profiller, topografyanın açık geometrik modelini içermeyen boş alan benzetiminde gelen konumda yeniden üretilir. | yok | 53 |
| AC 5-6 (belgeleme) | ZORUNLU | Hesap alanı boyutu, ağ çözünürlüğü ve kullanılan bütün sınır koşulları belgelenir. | yok | 53 |
| AC 5-6 (istatistik) | ZORUNLU | Gelen konumda farklı yüksekliklerde üç hız bileşeninin tam türbülans istatistikleri (ortalama, rms, uzunluk ölçekleri, spektrumlar) ve basınç raporlanır. | 3 hız bileşeni; yükseklik sayısı verilmemiş | 53 |
| AC 5-6 (kontur) | ZORUNLU | Ortalama ve standart sapma hız ve basınç alanları, yatay düzlemlerde ve akış yönü/duvara dik düzlemlerde çizilir; akışın alan içindeki gelişimi görülür ve profillerde gerçek dışı değişim olmadığı doğrulanır. | yok | 53 |
| AC 5-6 (hedef) | ZORUNLU | Topografya benzetiminin öngördüğü hedef alan, uygulamaya ilişkin temel hız istatistikleri bakımından gelen konumda doğru üretilir. | Burada sayı yok; sayısal sınırlar AC 5-9'da (Yöntem 1 için aralık h_max'ın %100'ü) | 53; 57 |
| AC 5-6 (yönler) | ZORUNLU | Topografya etkisi yöne bağlı olduğundan çözümleme ilgili bütün rüzgâr yönleri için yapılır. | Yön sayısı verilmemiş | 53 |
| §5.2 yorumu | YORUM | Hedef alan topografyasız alanın girişine doğrudan dayatılırsa akış düz arazi denge sınır tabakasına geri evrilir. Topografya benzetimi ile sonraki benzetimler arasındaki denklem ve sayısal yöntem farkı, girişe yakın kısa mesafede gerçek dışı profil değişimine yol açabilir; orta ölçek hava tahmin modellerinde (enerji ve nem korunumu, kaba ağ) sık görülür. Çok dikkat gerekir. | yok | 53 |
| §5.3 ana metin | Bilgi (zorunlu madde yok) | Geçici (transient) rüzgârlar için yöntemler geliştirilmiştir, ama kapsamlı hedef akış parametrelerinin tanımı ve akıştaki değişkenlik ile binanın akış içindeki konumundan doğan geniş parametre kümesi gibi sorunlar çözülmemiştir. Olgun, sektöre hazır bir yaklaşım yoktur; bu nedenle sinoptik olmayan rüzgârın açık benzetimi bu Prestandard uygulanırken beklenmez (§1.5.1). Yine de fırtına ve hortum profilleri yorumda ele alınır. | yok | 53–54 |
| §5.3 yorumu (genel) | YORUM | Zemin pürüzlülüğü açık elemanlarla ya da duvar fonksiyonlarıyla alınabilir; çalışmaların çoğu düz zemin kullanmıştır. Tam alanı modellemek yerine belirli akış özelliklerini (ivmelenme, hücum açısı, akım çizgisi eğriliği) temsil etmek önerilen bir seçenektir; etkin araştırma konusudur. | yok | 54 |
| §5.3 yorumu (fırtına inişi) | YORUM | İki sınıf: (1) deney düzeneklerini taklit eden modeller; (2) fırtınayı oluşturan soğutma kaynak terimlerini içeren modeller. Taklit kurulumda duran, hareketli ya da darbeli çarpan jet kullanılır; jetin boyutu ve momentumu çıkış akışını belirler (Şekil 5-3). Seçenek: rüzgâr üstünde panjur dizisi; panjur biçimi, eğim açısı, açılma süresi ve üst akıştaki aşırı basınç belirleyicidir. Soğutma kaynak teriminde şiddet, boyut ve ilerleme hızı zemine yakın akışı belirler. Hava tahmin modelleri de kullanılabilir; başlangıç ve sınır koşulları akışın evrimini yönetir. | yok | 54 |
| §5.3 yorumu (hortum) | YORUM | İki yol: (1) deney düzeneklerini taklit eden hortum benzeri girdap; (2) baskın zorlama mekanizmalarını içeren benzetim. Taklit kurulum (Şekil 5-4) teğetsel, radyal ve eksenel üç hız bileşenini ve üç bölgeyi (sınır tabakası girişi, köşe akışı, üst akış) üretir; köşe akışı yüksek hız ve basınç açığı nedeniyle özellikle önemlidir. Girdap özelliklerini giriş yarıçapı r0, derinliği h0 ve teğetsel/radyal giriş hızı koşulları belirler. Seçenek: çalıştırılabilir düşey panjur dizisi (açısal hız, konum, aşırı basınç belirleyici). | yok | 55 |

## Denklemler

Bu iki alt bölümde numaralı denklem yoktur.

## Metinde bulunamayanlar

- Topografya benzetiminin kendisi için yöntem, ağ ya da kabul ölçütü.
- AC 5-6 için ayrı bir sayısal tolerans (sayılar AC 5-9'dan gelir).
- Sinoptik olmayan rüzgâr için herhangi bir PO/AC, hedef profil ya da kabul sınırı.
