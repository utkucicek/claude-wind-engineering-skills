# Referans — Bölüm 7: Tasarım rüzgâr yüklerinin hesabı

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 7.
"PDF sayfası" = PDF sıra numarası (basılı sayfa = PDF − 18).
Tür: ZORUNLU = "shall", ÖNERİ = "should / recommended", YORUM = "Commentary" paragrafı ya da açıklayıcı metin.
Özetler kendi cümlelerimizle yazılmıştır; bağlayıcı olan belgenin kendi metnidir.

## 7.0–7.2 Genel şartlar ve rüzgâr iklimi

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §7 giriş | YORUM | Yapılar rijit, esnek ya da aeroelastik diye sınıflanır. Belge frekansa dayalı sınır tanımlamaz; ASCE/SEI 7-22 sınırı iyi bir göstergedir ama her yapı türünü kapsamaz. Nihai yük kabulü belgeleme ve hakem incelemesinin tamamlanmasına bağlıdır. | yok | 69 |
| PO 7-1 (§7.1.1) | ZORUNLU | Ele alınan yön ve/veya rüzgâr koşulu sayısı, yapıdaki yükleri tanımlamaya ve tasarım için kritik yönleri/etkileri yakalamaya yetmelidir. | yok | 69 |
| AC 7-1 | ZORUNLU | Benzetimler sınırlı azimut adımıyla yapılır; sonuçlar daha büyük tasarım yükü olasılığı gösteriyorsa ek yönler ele alınır. | adım ≤ 10° | 69 |
| §7.1.1 yorum | YORUM | Yön sayısı, yeterli gerekçe ve hakem ekibi ile AHJ onayı koşuluyla azaltılabilir. | yok | 69 |
| PO 7-2 (§7.1.2) | ZORUNLU | Uygun bir referans rüzgâr hızı belirlenir. | yok | 69 |
| AC 7-2 | ZORUNLU | Referans hız, yakın çevre modelinin örneklenen veriye etkisini en aza indiren bir yerde izlenir ve belgelenir. | yok | 69 |
| §7.1.2 yorum | YORUM / ÖNERİ | Tipik örnekleme: (1) çoğu yüksek bina için sınır tabakası dışında sayılan yükseklik, ya da (2) yapı yüksekliğinde, açıkça modellenen çevrenin rüzgâr üstü. Bazı yapılarda karakteristik yükseklik (çatı, saçak) kullanılır; başka yüksekliğe çevirme ayrıntılı belgelenmelidir. | yok | 70 |
| PO 7-3 (§7.1.3) | ZORUNLU | Tasarım yükü, çevrenin gelecekteki değişimine (ör. komşu binaların yıkılması) bağlı olmadan belirlenir. | yok | 70 |
| AC 7-3a | ZORUNLU | CWE ile bulunan MWFRS ve C&C yükleri, ASCE/SEI 7-22'nin (en güncel sürüm) yöntemlerine göre sınırlanır. Tablo 8-1 bu ölçütü "perdelenmemiş (unsheltered) durum için en küçük yük şartı" diye adlandırır. | Bölüm 7 metninde oran/yüzde yok (ASCE 7'ye gönderme) | 70; Tablo 8-1: 87 |
| AC 7-3b | ZORUNLU | İstatistiksel olarak durağan aerodinamik kuvvet/moment katsayıları, herhangi bir yük azalmasının bina türü ve biçimi için beklenen sonuçlarla uyumlu olduğunu doğrulamak üzere denetlenir. | yok | 70 |
| §7.1.3 yorum | YORUM | Projeyle ilgili olduğu ölçüde CWE yüklerinin ASCE/SEI 7-22 yükleriyle karşılaştırılması teşvik edilir. | yok | 70 |
| PO 7-4 (§7.2) | ZORUNLU | CWE verisi rüzgâr iklimi verisiyle birleştirilir. | yok | 70 |
| AC 7-4a | ZORUNLU | Şu istatistik yöntemlerden biri kullanılır: üst sınır (yönsüz), normalleştirilmiş sektör, çok sektörlü, yukarı geçiş, fırtına geçişi, doğrudan benzetim. | 6 yöntem | 70 |
| AC 7-4b | ZORUNLU | Sahaya özgü iklime katkı yapan bütün hava sistemleri hesaba katılır (Bölüm 3). İklim analizindeki varsayımlar ve birleştirme yöntemleri ayrıntılı belgelenir. | yok | 70 |
| §7.2 yorum — genel | YORUM / ÖNERİ | R yıllık hız ile R yıllık etki arasında açık ilişki yoktur; etki fırtına türü bazında bulunup sonra birleştirilmelidir. Üç fırtına türü (gök gürültülü, ekstratropikal, tropikal siklon) için dönüş periyotlarını birleştiren bağıntı verilir; yönlü hız veri kümeleri gerekir. | Denk. 7-1: denklem metinde okunamadı | 70–71 |
| §7.2 yorum — üst sınır | YORUM | En basit ve en güvenli yöntem; yönsellik yok sayılır. Tüm yönlerdeki en büyük tepki işlevine R dönüş periyotlu tasarım hızı konur. İklim analizi olmadan ASCE/SEI 7-22 hızlarıyla kullanılabilir; yönetmelik hızı kullanılırken fırtına türü ayrımı gerekmez. | yok | 71 |
| §7.2 yorum — normalleştirilmiş sektör | YORUM | Her sektöre, o sektörün R yıllık hızının tüm sektörlerdeki en büyük R yıllık hıza oranıyla ölçeklenmiş tasarım hızı atanır; tasarım tepkisi sektörler üzerindeki en büyüktür. Çoğunlukla güvenli taraf, nadiren güvensiz. Yönlü birleşik iklim modeli gerekir; kaba yön çözünürlüğü için yapılan varsayımlar rapora yazılmalıdır. | Denk. 7-2 ve 7-3: kısmen okunabiliyor, PDF'ten doğrulanmalı | 71 |
| §7.2 yorum — çok sektörlü | YORUM | Her yön sektörü için tepki–yıllık aşılma olasılığı hesaplanır; sektör dönüş periyotları bir çarpım bağıntısıyla birleştirilir. Sektörlerdeki uç rüzgârların bağımsızlığı varsayılır; gök gürültülü ve ekstratropikal fırtınalar için ayrı uygulanır. Sınırı: fırtına en büyüğünün yönü dışındaki yönlerden gelen daha zayıf rüzgârların katkısını yok sayar. | Denk. 7-4: denklem metinde okunamadı | 71–72 |
| §7.2 yorum — yukarı geçiş | YORUM | Gözlenen/benzetilen bütün rüzgârların ana dağılımına dayanır (genellikle iki parametreli Weibull; beş parametreli de kullanılmış). Parametreler yöne bağlıdır. Bugünkü uygulama gök gürültülü fırtınayı ayırmaz. Tropikal siklon benzetim sonuçlarıyla da kullanılabilir. | yok | 72 |
| §7.2 yorum — fırtına geçişi | YORUM | Her benzetilmiş tropikal siklonun hız–yön zaman serisinden en büyük tepki bulunur. Yön çözünürlüğü CWE verisininkiyle sınırlıdır. Yeterli sayıda benzetimle parametrik dağılım yerine görgül dağılım kullanılabilir. | CWE yön çözünürlüğü tipik olarak ≤ 10°; Denk. 7-5: denklem metinde okunamadı | 72 |
| §7.2 yorum — doğrudan benzetim | YORUM | Yönlü veriler her yön dilimi için uç değer dağılımına uydurulur; veri azsa komşu dilimler birleştirilebilir; Monte Carlo ile büyük veri kümesi üretilir; her olaydan yük/tepki hesaplanır. Dönüş periyodu Denk. 7-5 ile (λ: yılda ortalama fırtına sayısı). | yok | 72–73 |

## 7.3 Ana rüzgâr taşıyıcı sistem (MWFRS)

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §7.3 giriş | ZORUNLU | Tam ölçek tasarım yükleri, sonsuz rijit model üzerinde toplanan CWE verisinin yapının yapısal özellikleriyle analitik olarak birleştirilmesiyle elde edilir. Bütün sistemler esnek kabul edilir. Yalnız rijit yapıya uygun yöntem, ancak sağlam teknik gerekçe ayrıntılı belgelenirse kullanılır. | yok | 73 |
| PO 7-5 (§7.3.1) | ZORUNLU | MWFRS aerodinamik tepkisi, her sınır elemanı yüzüne etkiyen yerel yüzey kuvvetlerinin bütünlenmesiyle bulunur. | yok | 73 |
| AC 7-5a | ZORUNLU | Bütünleme, koşu sırasında önceden tanımlı etki alanları üzerinde doğrudan yapılır (tüm bina, bina dilimi, tek kat). Basınç ve viskoz katkıyı içerir; viskoz kuvvetin eklenmesi kesin şart değildir (katkısı genelde küçük). | yok | 73 |
| AC 7-5b | ZORUNLU (izin + şart) | Birden çok ayrık noktadaki yüzey basıncı zaman serilerinin bütünlenmesiyle yük ve dinamik etki hesabına izin verilir. İzleme noktası dağılımı istenen yük etkilerini doğru yakalamaya yetmelidir. | yok | 73 |
| AC 7-5c | ZORUNLU | Gözenekli bina elemanları gözenekli ortam yaklaşımıyla modellendiğinde özel dikkat gösterilir; gözenekli ortama etkiyen kuvvetler toplam yüke katılır. | yok | 73 |
| §7.3.1 yorum — doğrudan bütünleme | YORUM | Kuvvet terazisi (HFFB) benzeri yaklaşımların varsayımları (basit mod biçimleri, doğrusallıktan sapma, serbestlik dereceleri arası bağlaşım) vardır. CWE'de kat kat yük ve moment doğrudan bulunabilir. Kuvvet terazisine benzer sayısal yöntem benimsenirse mod biçimi, bağlaşım ve burulma kestirimi konusunda özel dikkat gerekir (ASCE/SEI 49-21). | yok | 73 |
| §7.3.1 yorum — basınç bütünlemesi | YORUM / ÖNERİ | Yöntemin başarısı izleme noktalarının yeri ve yoğunluğuna bağlıdır; çevresel kapsama ("halkalar") ve halkaların düşey aralığı önemlidir. Komşu bina çatı yükseklikleri en alt halkanın yerini etkileyebilir. CWE'de nokta yoğunluğu en azından rüzgâr tüneli uygulamasıyla tutarlı olmalı, karmaşık geometride artmalı. Yerel yönetmelik en az yoğunluk veriyorsa o da sağlanır. | AWES-QAM-1 önerisi: tam ölçekte 120 m² (~1.300 ft²) yüzey başına ≥ 1 nokta | 74 |
| PO 7-6 (§7.3.2) | ZORUNLU (izin) | Yük ve yapısal etkilerin frekans ya da zaman tanım alanı yöntemiyle hesaplanmasına izin verilir. | yok | 74 |
| AC 7-6 | ZORUNLU | Her durumda dinamik büyütme katsayısı (DAF) sonuçlarla birlikte raporlanır. | yok | 74 |
| §7.3.2 yorum | YORUM / ÖNERİ | Frekans alanı: ortalama + arka plan (background) + rezonans bileşenleri birleştirilir. Zaman alanı: genelleştirilmiş hareket denklemi adım adım çözülür; örnek süresi kritik bir seçimdir, kayıtlar arası değişkenliği değerlendirebilmek için daha uzun süreli örnekler kullanılmalıdır. | yok (süre için sayı verilmemiş) | 74 |
| PO 7-7 (§7.3.3) | ZORUNLU | Tepe rüzgâr yükleri ve rüzgâr kaynaklı yapısal etkiler sunulur. | yok | 75 |
| AC 7-7 | ZORUNLU (izin) | Ya eşdeğer statik rüzgâr yükleri ya da yapısal modele doğrudan uygulanacak aerodinamik kuvvet/basınç zaman serileri kabul edilir. | yok | 75 |
| §7.3.3 yorum | YORUM | Eşdeğer statik yükler ortalama, arka plan ve rezonans etkilerini kapsar (ör. kat kat yükleme). Zaman serileriyle eleman iç kuvvetleri, talep/kapasite oranları, kat ötelemesi ve ivmeler doğrudan hesaplanabilir. | yok | 75 |

## 7.4 Bileşenler ve kaplama (C&C)

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 7-8 (§7.4.1) | ZORUNLU | C&C rüzgâr etkileri CWE'den örneklenen basınç verisiyle belirlenir; iç basınç için uygun pay bırakılır. | yok | 75 |
| AC 7-8 | ZORUNLU; yoğunluk kısmı ÖNERİ | İzleme noktası dağılımı yük etkilerini doğru yakalamaya yetmeli; yerler dış geometrinin karmaşıklığına ve yüzey basınç gradyanına göre özenle seçilir. Küçük binalarda ve yüksek gradyanlı bölgelerde (çatı köşeleri, kenarlar, mahyalar, duvar kenarları) daha yüksek yoğunluk önerilir. | yok | 75 |
| PO 7-9 (§7.4.2) | ZORUNLU (izin + şart) | C&C üzerindeki ortalama ve zamanla değişen etkiler için integral yöntemle doğrudan yük hesabına izin verilir. Uygun iç basınçların dikkate alınmasına özen gösterilir. | yok | 75 |
| AC 7-9 | ZORUNLU | Kuvvet bütünlemesinde kullanılan etki alanlarının boyutu ve dağılımı, izleme noktası yerleşim ilkeleriyle tutarlı olur; özellikle büyük basınç gradyanı beklenen bölgelerde yeterli uzamsal çözünürlük sağlanır. | yok (alan büyüklüğü verilmemiş) | 75–76 |
| PO 7-10 (§7.4.3) | ZORUNLU | Tepe tasarım yükleri, rüzgâr iklimi verisiyle birleştirmeye uygun süre ve olasılık düzeyleri için bir uç değer dağılımı kullanılarak belirlenir. | yok | 76 |
| AC 7-10a | ZORUNLU | Uç değer istatistik analizinden gelen aşılma olasılığı raporlanır. | yok (hedef olasılık verilmemiş) | 76 |
| AC 7-10b | ZORUNLU | Aerodinamik olaylarla ilgili olabilecek frekansları ortadan kaldıran hiçbir süzgeç benzetim verisine uygulanmaz. | yok | 76 |
| §7.4.3 yorum — tek tepe | YORUM (metinde "shall not" ifadesiyle) | Tek gözlenen tepe katsayıları kullanılmaz: tekrarlanabilirliği zayıftır ve deney süresine bağlıdır. Uygun istatistik yöntem tekrarlanabilirliği artırır ve aşılmama olasılığının hesabını sağlar. | yok | 76 |
| §7.4.3 yorum — yöntemler | YORUM | Yaygın iki yöntem: (1) topluluk ortalaması — eşit uzunluklu dilimlerin uç değerlerinin ortalaması, uygun tam ölçek gözlem süresini temsil edecek biçimde ölçeklenir; (2) Gumbel uydurma — dilim uç değerlerinden belirli bir kesir düzeyindeki tepe. Diğerleri: bağımsız fırtınalar yöntemi, BLUE, eşik üstü tepeler. Cook–Mayne en doğru sonucu verir ama uç rüzgâr iklimini gerektirir; farklı iklimlerde kurulacak ürünlerin genel katsayıları için uygun değildir. | gözlem süresi örneği: 10 dk – 1 sa; dilim sayısı ve kesir düzeyi: metinde bulunamadı | 76 |
| §7.4.3 yorum — cam | YORUM / ÖNERİ | Bazı durumlarda tek bir tepe değer uygun çıktı değildir; ör. cam hasarı birikimlidir (Brown integrali) ve integral hem CWE verisine hem deney sonucuna uygulanmalıdır. | yok | 76 |
| PO 7-11 / AC 7-11 (§7.4.4) | ZORUNLU | Bir ek elemanın net basınç katsayıları, net basınçların doğrudan türetilmesiyle belirlenir. | yok | 76 |
| §7.4.4 metin/yorum | YORUM | Yüzeye dik basınç baskın etkidir; pozitif basınç yüzeye doğru, negatif (emme) dışa doğru. Net basınç, bir cismin iki yüzündeki basınçların ya da dış + iç basıncın bileşimidir. | yok | 76 |
| PO 7-12 (§7.4.5) | ZORUNLU | İç basınçlar ya benzetilmiş dış basınçlardan analitik olarak kestirilir ya da CWE benzetiminde doğrudan belirlenir. | yok | 77 |
| AC 7-12a | ZORUNLU | Ortalama ve zamanla değişen iç basınç kestirilirken gözeneklilik, sızıntı ve açıklıkların etkisi olası senaryolar için dikkate alınır. Benzetilmiş iç basınca dayalı net basınçlar integral izleme yaklaşımıyla hesaplanır. | yok | 77 |
| AC 7-12b | ZORUNLU | Zamanla değişen iç basınç doğrudan çözülüyorsa ve benzetim tam ölçekte değilse iç hacim ölçeklemesi gerekir. Güvenli tarafta net basınç veren sapmalara izin vardır ama raporda belgelenir. | yok | 77 |
| AC 7-12c | ZORUNLU | Kısmen kapalı diğer hacimlerdeki (gevşek serili çatı kaplaması ve balast karoları altı, havalandırmalı cephe panellerinin arkası, alçak profilli çatı güneş paneli sistemlerinin altı) boşluk basınçları, gözenekli malzemenin arkasındaki yüzeylerin basıncını değiştirebilecekse dikkate alınır; bu hacimlere açılan açıklıkların boyutu, yeri ve/veya geçirgenliği özenle eşlenir. | yok | 77 |
| §7.4.5 yorum | YORUM / ÖNERİ | İç basıncı belirleyenler: dış basınç dağılımı, sızıntı yolları, açıklıklar, kapalı hava hacmi, kabuğun esnekliği. Büyük açıklıklar doğrudan türetilmeli ya da CWE'den hesaplanmalı. Analitik değerlendirmede bakılacak akış yolları: havalandırma giriş/çıkışı, iç bölmeler ve katlar arası bağlantılar, açık kalabilecek büyük açıklıklar, rüzgârın yol açabileceği kabuk hasarı. Hesap pratik değilse ASCE/SEI 7-22 ya da AS/NZS 1170.2 iç basınçlarının kullanılması önerilir. Kısmen kapalı hacimlerde iç hacim ölçeklemesi güvenli tarafta ihmal edilebilir; orifis akışında Reynolds benzerliği gerekmez; dar/belirsiz sızıntı yollu sistemlerde tam ölçek benzetim önerilir. | yok | 77–78 |
| PO 7-13 / AC 7-13 (§7.4.6) | ZORUNLU | Ortalama, standart sapma ve tepe (en küçük, en büyük) dış basınç katsayıları değerlendirilir. Dört katsayı da ilgili basıncın referans dinamik basınca bölünmesiyle tanımlanır; q_ref = ½·ρ·U_ref². Tepe basınç anlık ya da istatistiksel olabilir. | Denk. 7-6: metin çıkarımı bozuk, yapı okunabiliyor; PDF'ten doğrulanmalı | 78 |

## 7.5–7.7 Ek elemanlar, kalite denetimi, sinoptik olmayan olaylar

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 7-14 (§7.5.1) | ZORUNLU | Ek elemanlardaki yükler, ana yapının tasarım yüklerinin elde edildiği aynı hesap modelinden türetilir. | yok | 78 |
| AC 7-14a | ZORUNLU | Yükler ya doğrudan yük hesabı (integral yöntem) ya da basınç bütünlemesi ile bulunur (§7.3.1). | yok | 78 |
| AC 7-14b | ZORUNLU (rijit) / izin (esnek) | Rijit ek elemanlarda tepe tasarım yükü §7.4.3 ile tutarlı istatistik yaklaşımla bulunur. Esnek ek elemanlarda DAF için §7.3.2 yöntemlerine izin verilir. | yok | 78 |
| §7.5.1 yorum | YORUM | AHJ bir ek elemanın ana yapıdan daha düşük hızda göçmesini (sigorta gibi) isteyebilir; çoğunlukla ana yapıyla aynı risk kategorisi beklenir. Örnekler: güneş kırıcılar, dekoratif kanatlar, balkonlar, saçaklar, çatı ekipmanı, parapetler. Belge genel ürün kurulumlarını açıkça ele almaz; yöntemler uyarlanarak uygulanabilir (ek kılavuz: ASCE/SEI 49-21). | yok | 78–79 |
| PO 7-15 / AC 7-15 (§7.5.2) | ZORUNLU | Ürün deney raporu ayrıca şunları içerir: (1) benzetilmiş yükler ve etkin rüzgâr alanı (effective wind area) ilişkisi — çatı güneş panellerinde normalleştirilmiş etkin rüzgâr alanına göre, diğer ürünlerde gerekliliği değerlendirilir; (2) verinin aerodinamik katsayılara çevrilmesi; (3) sonuçların uygulanabilirlik koşulları. | 3 madde | 79 |
| PO 7-16 / AC 7-16 (§7.6) | ZORUNLU | Binadaki bütünlenmiş kuvvet ve momentler bir referans noktasına (genellikle kule tabanı ya da yapısal orijin) göre çizilir; her bileşen için yöne göre ortalama, en küçük, en büyük. Kritik yönler için spektral tepki çizilir. | yok | 79 |
| §7.6 yorum | ÖNERİ | Ağ çalışmasında diğer ağlarla elde edilen sonuçların da bu grafiklere (doğrudan ya da değer bandı olarak) eklenmesi önerilir. | yok | 79 |
| §7.7 | YORUM (kapsam) | Belge, hortum gibi sinoptik olmayan olaylar için açık tasarım yükü yöntemi vermez. | yok | 79 |
| §7.7 yorum | YORUM | Tasarım standartlarıyla tutarlı, yayımlanmış bir yöntem henüz yoktur. ASCE/SEI 7-22 §32.18 sınır tabakası tünel katsayılarının kısıtlarla kullanılmasına izin verir (yalıtılmış bina, C sınıfı açık arazi); bu Prestandard'ın sinoptik yöntemleri temel katsayıları üretmek için kullanılabilir, sonra KvT düzeltmesi uygulanır (ASCE/SEI 7-22 §32.14). | yok | 79–80 |

## Bölüm 6'dan bu beceride kullanılan çapraz göndermeler

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| AC 6-13d (§6.6.2.2) | ZORUNLU | Rapor, veri örnekleme çözünürlüğü seçimini gerekçelendirir. | yok | 66 |
| PO 6-14 (§6.6.3) | ZORUNLU | Anahtar izleme noktalarındaki hızın ortalaması ve standart sapması ile ilgilenilen yük büyüklüklerinin ortalama, standart sapma ve tepe değerlerine ait kestirimlerin yakınsadığı gösterilir. | yok | 66 |
| AC 6-14 | ZORUNLU | Benzetim süresi, hedef bina yüksekliğindeki boyuna integral zaman ölçeğinin belirli bir katından uzun olur. | > 500 boyuna integral zaman ölçeği | 66 |
| §6.6.3 yorum | YORUM | Gerekli süre = ısınma (spin-up) + ortalama alma süresi; probleme bağlıdır. Tepe değerlerin doğru yakalanıp yakalanmadığı blok en büyükleri ya da eşik üstü tepeler yaklaşımıyla değerlendirilebilir. | yok | 66 |

## Okunamayan / eksik yerler

- Denk. 7-1 (fırtına türlerinin birleştirilmesi), 7-4 (çok sektörlü), 7-5 (fırtına geçişi): denklem metinde okunamadı.
- Denk. 7-2, 7-3 (normalleştirilmiş sektör) ve 7-6 (basınç katsayıları): kısmen okunabiliyor; yapı yukarıda sözle verildi, simgeler PDF'ten doğrulanmalı.
- Kaplama alan ortalaması için sayısal alan, Gumbel kesir düzeyi, dilim sayısı, ASCE 7 alt sınır yüzdesi, Bölüm 7'ye özgü belirsizlik maddesi: metinde bulunamadı.

## Sayım

Bölüm 7: 16 PO (7-1 … 7-16) ve 24 AC (7-1, 7-2, 7-3a/b, 7-4a/b, 7-5a/b/c, 7-6, 7-7, 7-8, 7-9, 7-10a/b, 7-11, 7-12a/b/c, 7-13, 7-14a/b, 7-15, 7-16) — toplam 40 madde, hepsi yukarıda.
