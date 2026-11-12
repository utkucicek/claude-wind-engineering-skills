---
name: rapor-ve-hakem-incelemesi
description: Bir CFD/LES rüzgâr yükü raporu yazılırken, mevcut bir rapor eksik içerik açısından denetlenirken ya da bağımsız hakem incelemesi (independent peer review) planlanırken kullanılır; ASCE CWE Prestandard Bölüm 9 (report content, compliance matrix) ve Bölüm 10 (project peer review, basis of design, comment log, AHJ) şartlarını denetim listesi olarak uygular.
---

# Rapor içeriği ve hakem incelemesi (ASCE CWE Prestandard, Bölüm 9 ve 10)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 9 ve 10.
Sayfa numaraları PDF sıra numarasıdır (basılı sayfa = PDF − 18). Madde dökümü: `referans.md`.
Bu bölümlerde PO/AC numarası yoktur; şartlar alt bölüm numarasıyla (§9.x, §10.x) anılır.

Kısaltmalar: CWE = hesaplamalı rüzgâr mühendisliği (computational wind engineering), AHJ = yetkili idare
(Authority Having Jurisdiction), EOR = sorumlu yapı mühendisi (Engineer of Record), MWFRS = ana rüzgâr taşıyıcı sistem,
DAF = dinamik büyütme katsayısı (dynamic amplification factor), CFL = Courant–Friedrichs–Lewy sayısı,
PSD = güç spektral yoğunluğu (power spectral density).

## Ne zaman kullanılır

- Rüzgâr yükü CFD raporunun iskeleti kurulurken ya da taslak rapor teslimden önce denetlenirken.
- Başkasının hazırladığı bir CWE raporu "Prestandard'a göre eksik ne var" diye incelenirken.
- Hakem incelemesi kurulurken: kim hakem olabilir, kapsam ne, hangi belge ne zaman verilir, anlaşmazlık nasıl çözülür.
- Tasarım hakem incelemesinden sonra değiştiğinde ne yapılacağı sorulduğunda.

## Adım adım

### A. Raporu hazırlama (Bölüm 9)

1. **Amacı ve kapsamı yaz (§9.1).** Benzetimin birincil kapsamı, amaçları, projenin temel özellikleri. Raporun hedefi: üçüncü bir tarafın ve gerekiyorsa AHJ'nin ayrıntılı teknik inceleme yapabilmesi; çalışmanın Bölüm 2–7 performans hedefleriyle nasıl örtüştüğünü göstermek.
2. **Benzetim parametrelerini belgeleyip dört alt başlığa ayır (§9.2).** Yöntem (§9.2.1), alan ve ağ (§9.2.2), ölçekleme (§9.2.3), incelenen bina (§9.2.4).
3. **Akış özelliklerini iki durum için ver (§9.3).** Hem "boş hesap alanı" hem de bina ve yakın çevre eklenmiş alan için; uygulanabildiği yerde hedef ve benzetilen değer/profil yan yana.
4. **Sonuçları kapsamla uyumlu sun (§9.4).** Liste, ağırlıklı olarak yapısal rüzgâr yükü ve tepkisine odaklı bir çalışmanın beklenen sonuçlarıdır; kapsam farklıysa içerik değişebilir (yorum).
5. **Başvuru bilgilerini ekle (§9.5).** İstatistik yöntem, yapısal özellik varsayımları, sınırlamalar, benzetim kalitesinin nicelenmesi, Tablo 8-1 uyum matrisi, yöntemin kuramsal arka planı.
6. **Raporu aşamalı teslim et (§10.5).** Önce tasarım esasları (basis of design) ile benzetim parametre ve varsayımları, sonra tam rapor.

### B. Hakem incelemesini yürütme (Bölüm 10)

1. **Hakemi seç ve AHJ'ye bildir (§10.2).** Tasarım ekibi seçer, genel mutabakat için AHJ'ye iletir. Hakem çıkar çatışması taşımaz, tasarım ekibinin parçası değildir, tasarım ekibinden ve benzetimin sponsorundan tümüyle bağımsızdır.
2. **Yetkinliği doğrula (§10.1).** Yedi alan: sınır tabakası dahil hesaplamalı akış benzetimi; rüzgâr mühendisliği ve küt cisim akışı; (ilgiliyse) esnek yapıların dinamik tepkisi; rüzgâr tehlikesi tanımı; maruziyet belirleme; rüzgâr tüneli modellemesiyle yük belirleme; bu Prestandard'ın şartları.
3. **Başlangıç toplantısı yap (§10.4).** EOR, benzetim ekibi, (uygunsa) AHJ ve hakemler: iş kapsamı, iletişim yöntemi, inceleme aşamalarının sıklığı ve zamanı, her aşamada tasarımın ne kadar gelişmiş olacağı.
4. **Yazılı iş kapsamı hazırla (§10.3).** Yedi kalem — aşağıdaki denetim listesinde.
5. **Önce tasarım esaslarını incelet (§10.3-1).** Tam benzetimden ÖNCE; böylece yorumlar son koşudan önce ele alınır.
6. **Yorumları yazılı yürüt (§10.5).** Hakemler zamanında yazılı yorum verir; tasarım ekibi bütün yorumları hakemleri tatmin edecek biçimde çözer. Yorum kütüğü (comment log) tarihleriyle tutulur (iyi uygulama, yorum).
7. **Kapanış raporu (§10.6).** İnceleme kapsamı, yorum kütüğü ve hakemlerin Prestandard'ın PO/AC şartlarına genel uygunluk konusundaki mesleki görüşü.
8. **Sorumluluğu karıştırma (§10.7).** Yük ve tepkiyi belirleme sorumluluğu yalnız benzetimi yapan rüzgâr mühendisindedir.
9. **Anlaşmazlık ve sonradan değişiklik (§10.8, §10.9).** Çözülemeyen anlaşmazlıkta aynı yetkinlik şartlarını sağlayan başka uzmanlar tutulur. İnceleme bittikten sonra esaslı tasarım değişikliği olursa EOR, AHJ'yi bilgilendirir; AHJ ek inceleme isteyebilir.

## Zorunlu şartlar

- §9 giriş: rapor, Bölüm 2–7 performans hedefleriyle uyumu gösterir; aşağıdaki başlıkları kapsamla ilgili olduğu ölçüde doğrudan ele alır.
- §9.1–§9.5.6: rapor içeriği (ayrıntı denetim listesinde).
- §9.5.5: Tablo 8-1 ile hizalı uyum özeti tablosu.
- §10.1: Prestandard kullanıldığında bağımsız hakem incelemesi yapılır (ayrıca §1.7).
- §10.2: hakem bağımsızlığı; çok kişili ekipte bir başkan.
- §10.3: yazılı iş kapsamı, yedi kalem; tasarım esasları incelemesi ilk adım.
- §10.4: başlangıç toplantısı.
- §10.5: Bölüm 9'a dayalı Hesaplamalı Rüzgâr Benzetimi Raporu aşamalı olarak verilir; yazılı yorumlar; tasarım ekibi yorumları çözer.
- §10.6: yazılı hakem raporu.
- §10.7: yük belirleme sorumluluğu rüzgâr mühendisinde.
- §10.8: anlaşmazlıkta ek uzmanlar, aynı şartlarla.
- §10.9: esaslı değişiklikte EOR, AHJ'yi bilgilendirir.

## Denetim listesi — rapor içeriği (evet/hayır)

**Amaç ve yöntem (§9.1, §9.2.1)**
- [ ] Benzetimin kapsamı, amaçları ve projenin temel özellikleri yazıldı mı?
- [ ] Yazılımın adı, geliştiricisi ve sürümü var mı?
- [ ] Akış modellemesinin temel özellikleri ve türbülans üretim yaklaşımı (yapay ve/veya doğal), çözülmeyen türbülansın ele alınışı anlatıldı mı?
- [ ] Uzamsal ayrıklaştırma, gradyan enterpolasyonu ve zamansal ayrıklaştırma yöntemleri yazıldı mı?
- [ ] Çözüm yöntemi, zaman adımı, en büyük CFL sayısı ve çözücü yakınsama ölçütleri verildi mi?
- [ ] Toplam benzetim süresi, istatistik için kullanılan süre ve istatistik yakınsamasını denetleme yöntemi yazıldı mı?

**Alan, ağ, ölçek, bina (§9.2.2–§9.2.4)**
- [ ] Hesap alanının geometrisi ve giriş, zemin, yan, üst, çıkış sınır koşulları belgelendi mi?
- [ ] Arazi elemanları ve topoğrafik özelliklerin alanda nasıl temsil edildiği yazıldı mı?
- [ ] Ağ ve çözünürlüğün bölgelere göre (yaklaşım akışı, yakın/yerel akış, uzak alan) değişimi anlatıldı mı?
- [ ] Bina çevresindeki, yüzler ve köşelerdeki yerel çözünürlük raporlandı mı?
- [ ] Geometrik uzunluk ölçeği, zaman ölçeği ve zaman adımı verildi mi?
- [ ] Akışkan yoğunluğunun nasıl ele alındığı ve Reynolds sayısı yazıldı mı?
- [ ] Bina ve çevre eklenmiş alanda hedeflenen ve ulaşılan tıkanma oranı (blockage ratio) nicelendi mi?
- [ ] CFL sayısı verildi mi?
- [ ] Binanın tam geometrisi, yüzey parametreleri, modellenen ve atlanan ek elemanlar ve bina görselleri var mı?

**Akış özellikleri (§9.3)**
- [ ] Değerler hem boş alan hem bina eklenmiş alan için, hedef ve benzetilen yan yana mı?
- [ ] Yerel rüzgâr iklimi, meteoroloji veri kaynağı ve veri kalitesi anlatıldı mı?
- [ ] Hedef referans hızlar ve dönüş periyotları yöne göre tanımlandı mı?
- [ ] Yaklaşım arazisi, yöne göre hedef maruziyet sınıfları ve dikkate alınan fırtına türleri yazıldı mı?
- [ ] Yönselliğin benzetimde ve sonuçlarda nasıl ele alınacağı belirtildi mi?
- [ ] Sahayı etkileyebilecek bütün hava sistemi türleri ve benzetime nasıl katıldıkları anlatıldı mı?
- [ ] Sahaya özgü olasılıksal iklim modeli ve referans akış koşulları belgelendi mi?
- [ ] Ortalama hız profili alan boyunca belgelendi mi?
- [ ] Boyuna, yanal ve düşey türbülans şiddeti profilleri alan boyunca belgelendi mi?
- [ ] Türbülans integral uzunluk ölçeği profili ve tam ölçek atmosfer hedefiyle karşılaştırması var mı?
- [ ] Hız çalkantılarının PSD'si üç doğrultuda verildi ve tam ölçek atmosfer spektrumuyla karşılaştırıldı mı?
- [ ] Kısmi türbülans modeli kullanıldıysa eksik düşük frekanslı türbülansın nasıl hesaba katıldığı yazıldı mı?
- [ ] Dahil edilen topoğrafik özellikler anlatıldı mı?
- [ ] İlgiliyse ekstratropikal ve sinoptik olmayan fırtına sistemlerinin etkisinin nasıl ele alındığı yazıldı mı?

**Sonuçlar (§9.4)**
- [ ] Kuvvetlerin benzetimde hangi yolla ölçüldüğü anlatıldı mı?
- [ ] x, y, z eksen takımı ve proje eksenleriyle ilişkisi tanımlandı mı?
- [ ] Ele alınan yön sayısı ve yönlerin sonuçlara nasıl temel olduğu yazıldı mı?
- [ ] Kuvvet ve moment katsayılarının ortalaması ve standart sapması, tüm yönler için, yönsellik etkisi öncesi ve sonrası verildi mi?
- [ ] Taban devrilme momenti ve taban kesmesi için, kritik yönlerde, rüzgâr doğrultusu ve rüzgâra dik tepki PSD grafikleri var mı?
- [ ] Taban kesme ve devrilme momentleri referans kot(lar)ında, iki dik doğrultuda, ele alınan dönüş periyotları ve yönler için verildi mi?
- [ ] Taban kesme, devrilme momenti ve burulmanın yöne göre ortalama/en küçük/en büyük grafikleri var mı?
- [ ] Bina yüksekliği boyunca kuvvet ölçme ve taban kuvvetlerini belirleme yöntemi anlatıldı mı?
- [ ] Genel bina yüklerinin DAF değeri nicelendi mi?
- [ ] (Kapsamda ya da AHJ/hakem istediyse) kesme ve momentlerin sönüm, kütle ve frekansa duyarlılığı var mı?
- [ ] Kat kat eşdeğer statik (ya da etkin) rüzgâr yükleri verildi mi?
- [ ] Burulma dahil, tüm ilgili yönlerin etkisini yakalayan yön birleşimli yük durumları var mı?
- [ ] Yönetmelik/standart yöntemiyle bulunan genel tasarım yükleri verildi ve CWE yükleriyle karşılaştırıldı mı?
- [ ] Bina hareketi kestirimleri (yanal ve burulma ivmeleri, istenen konumlarda, belirtilen dönüş periyotları için tepe ivme) var mı?
- [ ] (İstendiyse) ivmelerin sönüm, kütle ve frekansa duyarlılığı var mı?
- [ ] Yerel ve alan ortalamalı kaplama basınçları, belirtilen dönüş periyotları için, tüm kabukta pozitif ve negatif, ortalama ve tepe olarak verildi mi?
- [ ] İlişkili iç basıncın ele alınışı ile yerel basınç ölçüm konumları ve yöntemi anlatıldı mı?
- [ ] Uzun açıklıklı esnek elemanlar için dinamik etkileri içeren eşdeğer statik yük, etki alanı gözetilerek verildi mi?
- [ ] Ek elemanlarda (çatı ekipmanı, saçak, tabela, direk) tepe kuvvet ve moment talepleri ile aeroelastik etkilere (çırpınma, dörtnal) ilişkin yorum var mı?
- [ ] İç basınçların nasıl ele alındığı ve tasarım yüklerine nasıl girdiği yazıldı mı?

**Başvuru bilgileri (§9.5)**
- [ ] İklimi yapısal tepkiyle birleştiren istatistik yöntem belgelendi mi?
- [ ] Varsayılan kütle, sönüm, rijitlik ve mod biçimleri ile kaynağı (sponsor verisi, yönetmelik kestirimi, ölçüm) yazıldı mı?
- [ ] Yaklaşımın başlıca sınırlamaları ve doğruluğu/uygulanabilirliği etkileyen varsayımlar belirtildi mi?
- [ ] Ağ inceltme, zaman adımı duyarlılığı, iç yineleme yakınsaması, istatistik yakınsama ve spektral özellikler bakımından kalite değerlendirildi mi?
- [ ] Girdi parametrelerinden gelen belirsizlik ve bilinen diğer hata kaynakları değerlendirildi mi?
- [ ] Tablo 8-1 ile hizalı uyum özeti tablosu var mı?
- [ ] Denklemler, türbülans modelleri ve ayrıklaştırma teknikleri özetlendi mi; Prestandard'dan sapmalar gerekçelendirildi mi?
- [ ] Varsa kod doğrulama / kıyas karşılaştırma belgeleri eklendi mi; model ve verinin sayısal kaydı saklanıyor mu?

## Denetim listesi — hakem incelemesi (evet/hayır)

- [ ] Hakem(ler) tasarım ekibinden ve sponsordan tümüyle bağımsız mı, çıkar çatışması yok mu?
- [ ] Seçim AHJ'ye bildirildi mi?
- [ ] §10.1'deki yedi yetkinlik alanı karşılanıyor mu?
- [ ] Birden çok kişi varsa başkan belirlendi mi?
- [ ] Başlangıç toplantısı yapıldı mı (kapsam, iletişim, aşama takvimi)?
- [ ] Yazılı iş kapsamı şu yedi kalemi içeriyor mu: (1) tasarım esasları incelemesi, (2) rüzgâr tehlikesi ve benzetim tekniği, (3) kurulum, girdiler, alan üretimi, koşu, sonuçlar ve kabul ölçütlerine uygunluk, (4) sonuçların PO/AC'ye göre değerlendirilmesi, (5) tasarım yükleri ve diğer çıktılar, (6) performans hedefleri için önemli diğer konular, (7) hakem yorumları?
- [ ] Tasarım esasları, tam benzetimden önce incelendi mi?
- [ ] Rapor aşamalı verildi mi?
- [ ] Yorumlar yazılı mı ve hepsi hakemleri tatmin edecek biçimde çözüldü mü?
- [ ] Kapanışta kapsam + yorum kütüğü + uygunluk görüşünü içeren yazılı hakem raporu var mı?
- [ ] Hakem belgeleri yapım (sözleşme) belgelerine karıştırılmadan mı saklanıyor?
- [ ] İnceleme sonrası esaslı tasarım değişikliği olduysa AHJ bilgilendirildi mi?

## Sık yapılan hatalar

- Yalnız bina eklenmiş alanın akış profillerini vermek; boş alan sonuçları ve hedef–benzetim karşılaştırması da istenir (§9.3).
- Yönetmelik yüklerini rapora koymamak; §9.4.5.5 hem verilmesini hem CWE ile karşılaştırılmasını ister.
- DAF'ı, tıkanma oranını, CFL sayısını ya da yazılım sürümünü atlamak.
- Uyum matrisini Tablo 8-1'den bağımsız bir biçimde düzenlemek.
- "Prestandard geçerleme istiyor" diye yazmak; §9.5.4 yorumu geçerlemeyi zorunlu tutmaz, önerir.
- Hakemi rüzgâr yükünün ortak sorumlusu saymak (§10.7) ya da hakem yazılarını proje çizimlerine eklemek (yorum).
- Tasarım esasları incelemesini atlayıp hakemi bitmiş koşuyla karşılaştırmak (§10.3-1).
- Hakemi tasarım ekibinin ya da sponsorun içinden seçmek.
- Biçim, kütle dağılımı, rijitlik ya da sönüm değiştikten sonra AHJ'ye haber vermemek (§10.9 ve yorumu).
- Belgeye olmayan şart yakıştırmak: hakem sayısı, lisans zorunluluğu (yorum: bazı idareler isteyebilir, Prestandard'ın genel şartı değil), inceleme süresi metinde yoktur.

## İlgili beceriler

- `skills/kalite/kalite-guvencesi` — Tablo 8-1 uyum matrisi ve kalite kanıtları.
- `skills/yukler/tasarim-ruzgar-yukleri` — raporda sunulacak yük sonuçlarının nasıl üretileceği (Bölüm 7).
- `skills/surec/cwe-kapsam-ve-surec`, `skills/surec/hedef-ruzgar-tanimi`, `skills/benzetim/*` — akış özellikleri ve benzetim parametrelerinin kabul ölçütleri (Bölüm 3–6).
