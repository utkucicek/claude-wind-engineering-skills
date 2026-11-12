# Referans — Bölüm 8: Kalite güvencesi

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 8 ve Tablo 8-1.
"PDF sayfası" = PDF sıra numarası (basılı sayfa = PDF − 18).
Tür: ZORUNLU = "shall", ÖNERİ = "should / recommended", YORUM = "Commentary" ya da açıklayıcı metin.

Önemli: Bölüm 8 kendi PO/AC maddesini getirmez; Tablo 8-1, Bölüm 3–7'deki maddelerin başlık düzeyinde özetidir.
Aşağıdaki Tablo 8-1 dökümünde Bölüm 3–5 ve Bölüm 6'nın çoğu satırı YALNIZ tablo başlığından aktarılmıştır;
"Sayısal ölçüt" sütununda "tabloda yok" yazan yerlerde eşik ilgili bölümün metnindedir ve bu beceri kapsamında okunmamıştır.
Bu satırların asıl maddeleri kendi bölümlerinde ZORUNLU ("shall") diye yazılmış kabul ölçütleridir; tür sütunu "Tablo" olarak işaretlenmiştir.

## §8.1 Kalite güvencesi iş akışı

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §8 giriş | YORUM | Bölüm, önceki bölümlerdeki performans hedeflerini ve kabul ölçütlerini özetler; benzetim belirsizliği üzerine bir tartışmadan da söz eder (ayrı bir belirsizlik alt bölümü metinde bulunamadı). | yok | 81 |
| §8.1 (1. paragraf) | YORUM | CWE, parametreleri ve ilgilenilen büyüklükleri doğrusal olmayan biçimde etkileşen çok parametreli bir denklem sisteminin çözümüdür; ağ tasarımı, ayrıklaştırma ve çözüm yöntemi, türbülans modeli ve sınır koşulu seçimleri yük kestirimini karmaşıklaştırır. | yok | 81 |
| §8.1 (2. paragraf) | YORUM (beklenti: "expected") | Durağan ya da durağan olmayan RANS, türbülans kapaması ne olursa olsun, yapısal rüzgâr mühendisliği için güvenilir tepe / tam geçici çözüm veremez. En azından LES ve duvar modelli LES gibi geçici, girdap çözen yaklaşımların kullanılması beklenir. Bağlayıcı karşılığı PO/AC 4-2. | yok | 81 |
| §8.1 (3. paragraf) | YORUM | PO ve AC maddeleri CWE tasarımının kalitesini artırmak için geliştirilmiştir; Tablo 8-1 bunları özetler. | yok | 81 |
| §8.1 yorum | YORUM | LES ve DES'te ağ çözünürlüğü yalnız sayısal doğruluğu etkilemez, modellenen ile çözülen ölçekler arasındaki kesme frekansını da belirler; doğruluk ağ çözünürlüğü/kalitesi, sayısal şemalar ve ağ altı model arasındaki karmaşık etkileşimle belirlenir. | yok | 81 |

## Tablo 8-1 — Bölüm 3: Rüzgâr iklimi, hedef akış, arazi, topoğrafya (PDF s. 82)

| Madde | Tür | Özet (tablo başlığından) | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 3-1 | Tablo | Sahaya özgü yerel rüzgâr ikliminin değerlendirilmesi. | tabloda yok | 82 |
| AC 3-1a | Tablo | Sinoptik rüzgâr analizi için çok on yıllık rüzgâr kayıtları. | tabloda yok | 82 |
| AC 3-1b | Tablo | Kasırga rüzgârı analizi için Monte Carlo benzetimleri. | tabloda yok | 82 |
| AC 3-1c | Tablo | Yeniden analiz (reanalysis) veri kümeleri için çapraz geçerleme. | tabloda yok | 82 |
| PO 3-2 | Tablo | Sinoptik rüzgârların hedef akış koşulları. | tabloda yok | 82 |
| AC 3-2 | Tablo | Hedef akış parametrelerinin ve referans yüksekliklerinin belirlenmesi. | tabloda yok | 82 |
| PO 3-3 | Tablo | Rüzgâr üstü arazi maruziyetinin (exposure) nitelendirilmesi. | tabloda yok | 82 |
| AC 3-3 | Tablo | Yüzey pürüzlülüğü değerlendirmesi. | tabloda yok | 82 |
| PO 3-4 | Tablo | Topoğrafik özelliklerden etkilenen akışın benzetimi. | tabloda yok | 82 |
| AC 3-4 | Tablo | Kabul edilebilir topoğrafik akış benzetimleri (Topoğrafya Yöntemi 1 ve 2). | tabloda yok | 82 |

## Tablo 8-1 — Bölüm 4: Benzetim yöntemi (PDF s. 82–83)

| Madde | Tür | Özet (tablo başlığından) | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 4-1 | Tablo | Hedef rüzgâr akışının doğru temsili. | tabloda yok | 82 |
| AC 4-1 | Tablo | Hedef geliş akışının doğrulanması. | tabloda yok | 82 |
| PO 4-2 | Tablo | Tepe basınç yükü için türbülansın zamansal ve uzamsal gelişimini yakalayan benzetimler. | tabloda yok | 82 |
| AC 4-2 | Tablo | Gövdeye oturan (body-fitted) ağla uygulanan LES yaklaşımları, duvar modelli LES dahil. | tabloda yok | 82 |
| PO 4-3 | Tablo | Ağdaki sayısal hataların ve çözülen türbülansın sönümünün en aza indirilmesi (uzamsal ayrıklaştırma, gradyan enterpolasyonu). | tabloda yok | 82 |
| AC 4-3 | Tablo | En az ikinci mertebe şemalar. | ≥ 2. mertebe | 82 |
| PO 4-4 | Tablo | Zaman bütünlemesindeki sayısal hataların en aza indirilmesi. | tabloda yok | 82 |
| AC 4-4 | Tablo | En az ikinci mertebe şema ve sayısal kararlılık ile girdap gelişimi için uygun zaman adımı. | ≥ 2. mertebe | 82 |
| PO 4-5 | Tablo | Süzgeç altı ölçek türbülansının çözülen akışa etkisinin fiziksel olarak tutarlı temsili. | tabloda yok | 82 |
| AC 4-5 | Tablo | Uygun SGS modellerinin kullanımı. | tabloda yok | 82 |
| PO 4-6 | Tablo | Ayrıklaştırılmış denklemler için kararlı ve doğru çözüm yöntemleri (zaman adımı içi çözücü yakınsaması). | tabloda yok | 83 |
| AC 4-6a | Tablo | Yakınsama denetimi. | tabloda yok | 83 |
| AC 4-6b | Tablo | Yaklaşım akışı benzetimlerinde kullanılan yakınsama ölçütlerinin raporu. | tabloda yok | 83 |
| AC 4-6c | Tablo | Bina aerodinamiği benzetimlerinde yakınsama ölçütlerinin raporu. | tabloda yok | 83 |
| PO 4-7 | Tablo | Tam ölçek ya da model ölçek benzetimler (geometrik ölçekleme). | tabloda yok | 83 |
| AC 4-7 | Tablo | Model ölçek benzetimler için şartlar. | tabloda yok | 83 |

## Tablo 8-1 — Bölüm 5: Yaklaşım akışı benzetimleri (PDF s. 83–84)

| Madde | Tür | Özet (tablo başlığından) | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 5-1 | Tablo | Hedef rüzgâr alanını yakalayacak ve sınır koşulu etkilerinden kaçınacak hesap alanı boyutu. | tabloda yok | 83 |
| AC 5-1 | Tablo | Alan boyutu şartları. | tabloda yok | 83 |
| PO 5-2 | Tablo | Rüzgâr yükleri için küçük ölçekli türbülansı yakalayacak ağ çözünürlüğü. | tabloda yok | 83 |
| AC 5-2 | Tablo | Kaplama ve genel yükler için en büyük çözülen indirgenmiş frekans şartları. | tabloda yok | 83 |
| PO 5-3 | Tablo | Hedef türbülanslı rüzgâr koşullarının gelen konumnda yeniden üretilmesi. | tabloda yok | 83 |
| AC 5-3 | Tablo | Tüm farklı maruziyet koşulları ve tüm rüzgâr yönleri için gelen konumndaki türbülanslı akış kalitesinin gösterilmesi (kabul düzeyleri için tablo "A.C. 5-8" der; kabul şartı satırı 5-9'dur — PDF'ten doğrulanmalı). | tabloda yok | 83 |
| PO 5-4 | Tablo | Alan zemin yüzeyi için sınır koşulları. | tabloda yok | 83 |
| AC 5-4 | Tablo | Hedef zemin pürüzlülüğünün modellenmesi (tabloda "A.O. 3-3" göndermesi). | tabloda yok | 83 |
| PO 5-5 | Tablo | Alanın yan, üst ve çıkış sınır koşulları. | tabloda yok | 83 |
| AC 5-5 | Tablo | Uygun sınır koşullarının seçimi. | tabloda yok | 83 |
| PO 5-6 | Tablo | Boş alanda topoğrafyanın yaklaşım akışına etkisinin yeniden üretilmesi. | tabloda yok | 83 |
| AC 5-6 | Tablo | Topoğrafyadan etkilenen yaklaşım akışının doğru yeniden üretildiğinin gösterilmesi. | tabloda yok | 83 |
| PO 5-7 | Tablo | Hız istatistiklerinin yakınsaması. | tabloda yok | 84 |
| AC 5-7 | Tablo | Bina yüksekliğinde ortalama hız ve türbülans şiddetlerinin yakınsama raporu. | tabloda yok | 84 |
| PO 5-8 | Tablo | Yaklaşım akışı için rüzgâr ve basınç alanının fiziksel olarak tutarlı temsili. | tabloda yok | 84 |
| AC 5-8 | Tablo | Hız ve basınç alanlarının görselleştirilmesi. | tabloda yok | 84 |
| PO 5-9 | Tablo | Gelen konumnda hedef akış parametrelerinin doğru sunumu. | tabloda yok | 84 |
| AC 5-9 | Tablo | Gelen konumnda (tabloda "incipient") hem açıklık ortasında hem açıklığın 1/3 konumlarında akış özellikleri için kabul şartları (hedef değerler için 3-2 ve 3-3). | konum: orta ve 1/3 açıklık; eşikler tabloda yok | 84 |
| PO 5-10 | Tablo | Uygun ağ çözünürlüğü. | tabloda yok | 84 |
| AC 5-10 | Tablo | Rüzgâr spektrumu kesme frekansı eylemsizlik alt aralığında yer alır. | tabloda yok | 84 |

## Tablo 8-1 — Bölüm 6: Bina aerodinamiği benzetimleri (PDF s. 84–86)

| Madde | Tür | Özet (tablo başlığından; 6-13…6-16 metinden) | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 6-1 | Tablo | Yaklaşım akışı benzetimlerinde üretilen rüzgâr ve basınç alanlarının tutarlı biçimde yeniden üretilmesi. | tabloda yok | 84 |
| AC 6-1 | Tablo | Geometrik/hız ölçekleri, çözücüler, sayısal yöntemler, türbülans modelleri ve sınır koşullarında yaklaşım akışı benzetimleriyle tutarlılık. | tabloda yok | 84 |
| PO 6-2 | Tablo | İncelenen binanın aerodinamiğini etkileyen ayrıntıların modellenmesi. | tabloda yok | 84 |
| AC 6-2a | Tablo | Binanın geometrik ayrıntılarının dahil edilmesi. | tabloda yok | 84 |
| AC 6-2b | Tablo | İç hacim ve açıklık modellerinin dahil edilmesi. | tabloda yok | 84 |
| PO 6-3 | Tablo | Aerodinamiği etkileyen yakın binaların ve diğer yapıların modellenmesi. | tabloda yok | 84 |
| AC 6-3 | Tablo | Seçilen yakın çevre modellerinin gerekçe raporu. | tabloda yok | 84 |
| PO 6-4 | Tablo | Topoğrafya modeli. | tabloda yok | 84 |
| AC 6-4a | Tablo | Bina çevresindeki topoğrafya modellerinin dahil edilmesi. | tabloda yok | 84 |
| AC 6-4b | Tablo | Topoğrafya modelinin gerekçe raporu. | tabloda yok | 84 |
| PO 6-5 | Tablo | Binaya ek elemanlar (appurtenances). | tabloda yok | 85 |
| AC 6-5a | Tablo | Tam ölçek, yüksek çözünürlüklü benzetimler için modelleme şartı. | tabloda yok | 85 |
| AC 6-5b | Tablo | 6-5a'ya seçenek. | tabloda yok | 85 |
| AC 6-5c | Tablo | Model ölçek benzetimler için modelleme şartı. | tabloda yok | 85 |
| AC 6-5d | Tablo | Geometrik ölçek ve ayrıntıların dahil edilmesine ilişkin gerekçe raporu. | tabloda yok | 85 |
| PO 6-6 | Tablo | Gözenekli bileşenler. | tabloda yok | 85 |
| AC 6-6 | Tablo | Açık modellerde gözeneklilik modelleme raporu; kabalaştırılmış modellerde geçerleme. | tabloda yok | 85 |
| PO 6-7 | Tablo | Alan boyutu, rüzgâr benzetimlerindekiyle karşılaştırmalı. | tabloda yok | 85 |
| AC 6-7 | Tablo | En rüzgâr üstü bina/topoğrafik özelliğin konumu; akış yönü, açıklık ve düşey doğrultuda alan uzunlukları. | tabloda yok | 85 |
| PO 6-8 | Tablo | Kabul edilebilir sınır ya da tıkanma (blockage) etkileri için alan boyutu. | tabloda yok | 85 |
| AC 6-8a | Tablo | Giriş ve çıkış sınırlarının en yakın bina ve topoğrafik özelliklere akış yönündeki uzaklıkları. | tabloda yok | 85 |
| AC 6-8b | Tablo | Kabul edilebilir en büyük tıkanma oranları. | tabloda yok | 85 |
| PO 6-9 | Tablo | Ağ çözünürlüğü şartları. | tabloda yok | 85 |
| AC 6-9a | Tablo | Yaklaşım akışı bölgesinde ağ çözünürlüğü. | tabloda yok | 85 |
| AC 6-9b | Tablo | Duvar yakını bölgede ağ çözünürlüğü. | tabloda yok | 85 |
| AC 6-9c | Tablo | Yerel akış bölgesinde ağ çözünürlüğü. | tabloda yok | 85 |
| AC 6-9d | Tablo | Uzak akış bölgesinde ağ çözünürlüğü. | tabloda yok | 85 |
| AC 6-9e | Tablo | Hız/basınç spektrumları ve IRQ ile ağ yeterliliğinin değerlendirilmesi. | tabloda yok | 85 |
| AC 6-9f | Tablo | Modellenen gözenekli elemanların yakınında ağ çözünürlüğü. | tabloda yok | 85 |
| PO 6-10 | Tablo | Bina yüzeyleri (sınır koşulu). | tabloda yok | 86 |
| AC 6-10a | Tablo | Duvar yakını akış işlemleri. | tabloda yok | 86 |
| AC 6-10b | Tablo | Yuvarlak bina yüzeyleri yakınındaki akış için duvar modellemesinin incelenmesi. | tabloda yok | 86 |
| AC 6-10c | Tablo | Duvar yakını işlemin basınç dağılımına etkisinin nicelenmesi. | tabloda yok | 86 |
| PO 6-11 | Tablo | Diğer sınırlar. | tabloda yok | 86 |
| AC 6-11 | Tablo | 5-4 ve 5-5'teki giriş, zemin, yan, üst sınırların kullanımı; topoğrafik akış benzetimlerinde arazi pürüzlülüğü modellemesi. | tabloda yok | 86 |
| PO 6-12 | Tablo | Hız ve basınç alanları. | tabloda yok | 86 |
| AC 6-12a | Tablo | Temsili konumlarda hız ve basınç özelliklerinin görselleştirilmesi. | tabloda yok | 86 |
| AC 6-12b | Tablo | İzleme noktalarında hız ve basınç davranışının görselleştirilmesi. | tabloda yok | 86 |
| PO 6-13 | ZORUNLU | Benzetimin genel kalitesi bina kabuğundaki basınç alanı incelenerek denetlenir. | yok | 66; tablo 86 |
| AC 6-13a | ZORUNLU | Basıncın ortalama ve standart sapma eş düzey haritaları bütün cephelerde, çatıda ve ilgiliyse ek elemanlarda çizilir; yüksek gradyanlı bölgelere (kenar, köşe) özel dikkat. | yok | 66 |
| AC 6-13b | ZORUNLU | Sonda konumları ASCE/SEI 49-21 kılavuzuna göre yerleştirilir (tablo: en büyük/en küçük basınç kestirimi konumları). | yok | 66 |
| AC 6-13c | ZORUNLU | Basınç izleme konumlarının çözünürlüğü, MWFRS ve C&C çalışmaları için yüzeydeki uzamsal değişimi yakalamaya yeter. | yok | 66 |
| AC 6-13d | ZORUNLU | Rapor, veri örnekleme çözünürlüğü seçimini gerekçelendirir. | yok (eşik verilmemiş) | 66 |
| AC 6-13e | ZORUNLU | Referans statik basınç izleme noktası model, yakın çevre ve sınır etkisinden uzak konur; çalışma bölgesinin doğrudan üstündeki bir statik basınç noktası referans için kullanılır. | yok | 66 |
| PO 6-14 | ZORUNLU | Anahtar noktalardaki hızın ortalama ve standart sapması ile ilgilenilen yük büyüklüklerinin ortalama, standart sapma ve tepe değer kestirimlerinin yakınsadığı belirlenir. | yok | 66 |
| AC 6-14 | ZORUNLU | Benzetim süresi, hedef bina yüksekliğindeki boyuna integral zaman ölçeğinin belirli katından uzundur. | > 500 boyuna integral zaman ölçeği | 66 |
| §6.6.3 yorum | YORUM | Gerekli süre ısınma + ortalama alma süresidir. Sinyalin ortalama ve standart sapması büyüyen pencere üzerinde (ilk geçici kısım atıldıktan sonra) izlenebilir; tepe değerler için blok en büyükleri ya da eşik üstü tepeler kullanılabilir. | yok | 66 |
| PO 6-15 | ZORUNLU ("must") | Proje için en az iki rüzgâr yönünde ağ çalışması yapılır. | ≥ 2 yön | 67 |
| AC 6-15a | ZORUNLU | IRQ, akış ve basınç alanındaki anahtar izleme konumlarında alt sınırın altında olmaz; iki ağ çözünürlüğü arasındaki yük büyüklüğü farkları raporlanır. | IRQ ≥ %75 | 67 |
| AC 6-15b | ZORUNLU | Anahtar izleme konumu, bina yüksekliği boyunca ve binadan belirli uzaklığa kadar bir dizi sanal sonda noktasıdır; özel durumlar için uyarlama yapılır; yaklaşım akışı (rüzgâr üstü izler) ve bina izi yakalanır. | binadan 160 ft'e (~50 m) kadar | 67 |
| §6.6.4 yorum | YORUM | Örtük süzgeçli LES/DES'te her ağ farklı ölçek çözünürlüğü verir; çözüm ancak DNS düzeyine yaklaşınca ağdan bağımsızdır. IRQ = çözülen türbülans kinetik enerjisi / toplam; toplam, iki ağ sonucundan SGS katkısı dışdeğerlenerek kestirilir. En çok üç ağ (kaba, orta, ince); inceltme katsayısı ideal olarak 2. Etkin mertebe p, şemanın sayısal mertebesiyle yaklaşık uyuşmalı; kestirilen mertebe kuramsaldan belirgin yüksekse kuramsal mertebeyi benimsemekten kaçınılmalı. | r ideal = 2; r alt sınırı: metinde okunamadı; Denk. 6-3…6-6: denklem metinde okunamadı | 67–68 |
| §6.6.4 yorum — IRQ aralıkları | YORUM | IRQ sınıfları: alt sınırın altı = daha fazla inceltme gerekir; orta aralık = mühendislik çözümü için uygun; üst aralık = DNS'e yakın. | < %75; %75–85; > %85 | 68 |
| PO 6-16 | ZORUNLU | Zaman adımı duyarlılığı gözden geçirilir. | yok | 68 |
| AC 6-16 | ZORUNLU | Hız spektrumları bina çevresindeki anahtar konumlarda ve hedef bina ile rüzgâr üstü binalar arasındaki bölgelerde çizilir; ağ boyutu ve zaman adımından kaynaklanan kesme grafikte gösterilir. | yok | 68 |
| §6.6.5 yorum | YORUM | Açık şemalarda en büyük zaman adımı yerel hücre boyutu ve hıza (CFL) bağlıdır; örtük şemalarda CFL 1'in üstüne çıkabilir ama gerekli zaman ölçekleri çözülmelidir. İyi bir sınama: yarı zaman adımlı ikinci koşu; spektrumlar özdeş/çok benzerse adım yeterlidir. Seçenek: ağ duyarlılık çalışmasında CFL'yi korumak. | adım × ½; CFL > 1 (örtük) olabilir | 68 |

## Tablo 8-1 — Bölüm 7: Tasarım rüzgâr yükleri (PDF s. 87–88)

Ayrıntı ve tür ayrımı: `skills/yukler/tasarim-ruzgar-yukleri/referans.md`. Burada tablo başlıkları verilmiştir.

| Madde | Tür | Özet (tablo başlığından) | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 7-1 / AC 7-1 | ZORUNLU | Yön ve/veya rüzgâr koşulu sayısı / en büyük azimut adımı. | ≤ 10° | 87 |
| PO 7-2 / AC 7-2 | ZORUNLU | Referans rüzgâr hızının izlenmesi / izleme konumu. | yok | 87 |
| PO 7-3 / AC 7-3a | ZORUNLU | Yük sınırlamaları / perdelenmemiş durum için en küçük yük şartı. | yok | 87 |
| AC 7-3b | ZORUNLU | Durağan aerodinamiğe dayalı yük azaltma tutarlılığı değerlendirmesi. | yok | 87 |
| PO 7-4 / AC 7-4a | ZORUNLU | Yerel iklimin benzetim kestirimleriyle birleştirilmesi / kabul edilen istatistik yöntemler. | 6 yöntem | 87 |
| AC 7-4b | ZORUNLU | Analiz ve yöntem ayrıntılarının belgelenmesi. | yok | 87 |
| PO 7-5 / AC 7-5a | ZORUNLU | Rüzgâr kuvvetleri / yüzey kuvvetlerinin bütünlenmesi şartı. | yok | 87 |
| AC 7-5b | ZORUNLU | Zamanla değişen yerel basınç verisini kullanan kabul edilir bütünleme yöntemi. | yok | 87 |
| AC 7-5c | ZORUNLU | Gözenekli elemanlı binalarda kuvvet hesabı şartı. | yok | 87 |
| PO 7-6 / AC 7-6 | ZORUNLU | Rüzgâra dinamik tepki / DAF raporu. | yok | 87 |
| PO 7-7 / AC 7-7 | ZORUNLU | Tepe yükler ve yapısal etkiler / kabul edilir yöntemler. | yok | 87 |
| PO 7-8 / AC 7-8 | ZORUNLU | Yerel tepe basınçlar / izleme konumları. | yok | 88 |
| PO 7-9 / AC 7-9 | ZORUNLU | Ortalama ve zamanla değişen basınçlar / doğrudan bütünleme şartları. | yok | 88 |
| PO 7-10 / AC 7-10a | ZORUNLU | Tepe tasarım yükleri / aşılma olasılığı raporu. | yok | 88 |
| AC 7-10b | ZORUNLU | Zamansal süzme yapılmaması şartı. | yok | 88 |
| PO 7-11 / AC 7-11 | ZORUNLU | Net basınç / doğrudan türetilmiş net basınçlardan katsayı. | yok | 88 |
| PO 7-12 / AC 7-12a | ZORUNLU | İç basınç / benzetilmiş dış basınçları kullanan analitik yöntem şartları. | yok | 88 |
| AC 7-12b | ZORUNLU | İç basıncın doğrudan belirlenmesi şartları. | yok | 88 |
| AC 7-12c | ZORUNLU | Kısmen kapalı hacimlerde iç basınç kestirimi şartları. | yok | 88 |
| PO 7-13 / AC 7-13 | ZORUNLU | Dış basınç / basınç katsayılarının kullanımı. | yok | 88 |
| PO 7-14 / AC 7-14a | ZORUNLU | Ek elemanlarda yükler / kabul edilir yöntemler. | yok | 88 |
| AC 7-14b | ZORUNLU | Rijit ve esnek ek elemanlar için yaklaşım şartları. | yok | 88 |
| PO 7-15 / AC 7-15 | ZORUNLU | Sonuç sunumu / raporlama şartları. | 3 madde | 88 |
| PO 7-16 / AC 7-16 | ZORUNLU | Bütünlenmiş kuvvet ve momentlerin sunumu / istatistik özelliklerinin görselleştirilmesi. | yok | 88 |

## Doğrulama, geçerleme ve kıyas (Bölüm 8'in dayandığı diğer maddeler)

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §1.6 (1) | YORUM | LES kodlarının olgunluğu ve güvenilirliği geniş aralıktadır; genelde en güvenilir ve en iyi belgelenmiş olanlar ticari kodlardır, açık kaynak/akademik/bireysel kodlar daha az güvenilir olabilir. | yok | 23 |
| §1.6 (2) | ÖNERİ | Analist, kullanılan kodun doğrulama ve geçerleme sınama belgelerini ayrıntılı tanımalıdır. | yok | 23 |
| §1.6 (3) | ZORUNLU | Analist, kod sağlayıcının belgelediği kod doğrulama ve model geçerleme sınamalarının koşul aralığını ve titizliğini değerlendirir. | yok | 23 |
| §1.6 (4) | ZORUNLU | Müşteri isterse bu bilgi, analistin yeterlilik değerlendirmesiyle birlikte sağlanır. | yok | 23 |
| §1.6 (5) | ÖNERİ | Analist ya da müşteri kapsamı/titizliği uygulama için yetersiz bulursa ek sınama yapılmalı ve belgelenmelidir. Bu doğrulama/geçerleme süreci belgenin kapsamı dışındadır. | yok | 23 |
| §1.6 yorum | YORUM | Tanımlar (ASME): kod doğrulama = matematik modelin kodda doğru uygulandığının belirlenmesi; çözüm doğrulama = belirli bir sayısal çözümün doğruluğunun belirlenmesi; geçerleme = model sonuçlarının kullanım bağlamında görgül veriyi ne ölçüde temsil ettiğinin belirlenmesi. Kod doğrulamayı geliştirici, çözüm doğrulamayı (ayrıklaştırma, yineleme, hassasiyet hataları) CWE kullanıcısı yapmalıdır. CWE'de geçerleme çoğunlukla denetimli koşullu rüzgâr tüneli verisine dayanmıştır; temsili deney veri kümesi tanımlamak kapsam dışıdır. | yok | 23 |
| §1.8 tanımlar | YORUM | Kod doğrulama, çözüm doğrulama ve geçerleme tanımları terimler listesinde de yer alır. | yok | 24–26 |
| §9.5.4 | ZORUNLU | Rapor, ağ inceltme, zaman adımı duyarlılığı, iç yineleme çözücü yakınsaması, istatistik yakınsama ve spektral özellikler bakımından benzetim kalitesini değerlendirir; girdi parametrelerinden (rüzgâr verisi, arazi pürüzlülüğü modeli) gelen belirsizliği değerlendirir; olasılıksal yöntem (Monte Carlo, güven aralığı) kullanıldıysa ayrıntısını verir; bilinen diğer hata kaynaklarını belgeler. | yok | 93–94 |
| §9.5.4 yorum | YORUM / ÖNERİ | Yayım tarihinde CWE için güvenilir kıyas vakaları bulunmadığından belge sonuçların referans veriye karşı geçerlenmesini zorunlu tutmaz; temsili görgül ya da yüksek doğruluklu benzetim verisine karşı ek geçerlemenin raporlanması önerilir. | yok | 94 |
| §9.5.5 | ZORUNLU | Rapor, Tablo 8-1 ile hizalı bir uyum özeti tablosu içerir. | yok | 94 |
| §9.5.6 | ZORUNLU | Yöntem bilgisi (denklemler, türbülans modelleri, ayrıklaştırma) verilir; Prestandard'dan sapan koşullar gerekçelendirilir; tescilli tasarım uzmanı model ve verinin sayısal kaydını saklar; varsa kod doğrulama ve/veya kıyas karşılaştırma belgeleri eklenir. | yok | 94 |
| §10.7 yorum | YORUM | Hakem incelemesi, benzetimi yapan ekibin olağan kalite güvence önlemlerinin yerini tutmaz. | yok | 98 |

## Okunamayan / eksik yerler

- Denk. 6-3 … 6-6 (IRQ, toplam kinetik enerji, etkin mertebe, a_k): denklem metinde okunamadı.
- Ağ inceltme katsayısı r için alt sınır: metin çıkarımında değer bozuk ("at least 2" biçiminde çıkmış, ideal değerle aynı görünüyor; kök işareti düşmüş olabilir) — PDF'ten doğrulanmalı.
- Bölüm 8'de ayrı bir belirsizlik alt bölümü ve herhangi bir ek (appendix): metinde bulunamadı.
- Tablo 8-1'deki Bölüm 3–5 ve Bölüm 6'nın (6-13…6-16 dışındaki) eşik değerleri: tabloda yok; ilgili bölüm metni bu beceri kapsamında okunmadı.

## Sayım

Tablo 8-1: 53 PO (Bölüm 3: 4, Bölüm 4: 7, Bölüm 5: 10, Bölüm 6: 16, Bölüm 7: 16) ve 84 AC
(Bölüm 3: 6, Bölüm 4: 9, Bölüm 5: 10, Bölüm 6: 35, Bölüm 7: 24). Bölüm 8'in kendine ait PO/AC maddesi yoktur.
