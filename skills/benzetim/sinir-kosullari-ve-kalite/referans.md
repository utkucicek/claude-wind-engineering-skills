# Referans: ASCE CWE Prestandard §6 girişi, §6.1, §6.5, §6.6

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Sayfa numaraları PDF sayfa sırasıdır. Özetler kendi cümlelerimizle yazılmıştır.

Tür: ZORUNLU = shall (ya da must), ÖNERİ = should, YORUM = commentary.

## Maddeler

| Madde | Tür | Özet | Sayısal ölçüt (birimiyle) | PDF sayfası |
|---|---|---|---|---|
| §6 giriş | ZORUNLU | Bina aerodinamiği benzetimleri §4.2'deki bütün PO/AC maddelerini (yöntem, ayrıklaştırma, çözülmeyen türbülans, çözücü yakınsaması, ölçekleme) sağlar; bu bölüm bunlara ek şartlar getirir. | yok | 59 |
| §6 giriş yorumu | YORUM | İçerik yaya konforu/güvenliği ve hava kalitesi için LES'e de uygulanabilir. | yok | 59 |
| PO 6-1 | ZORUNLU | Bina benzetimi, aynı fiziksel bölgede Bölüm 5 yaklaşan akış benzetiminin sonucuyla örtüşür. | yok | 59 |
| AC 6-1 | ZORUNLU | Bina benzetimi, §5.1 yaklaşan akış benzetimleriyle aynı geometri ve hız ölçeğini, çözücüyü, sayısal yöntemleri, türbülans modelini, zemin duvar modelini ve sınır koşullarını kullanır (PO 4-1'deki iki adımlı süreç). | yok | 59 |
| §6.1 yorumu | YORUM | Temel model seçimlerinin korunması, hedef akışın bina benzetiminde de doğru üretilmesini sağlar. | yok | 59 |
| PO 6-10 | ZORUNLU | Bina yüzeyindeki sınır koşulu, yüzey özelliklerine ve duvar yakını ağ çözünürlüğüne göre seçilir. | yok | 64 |
| AC 6-10a | ZORUNLU | Bina yüzeyi kaymaz duvar olarak modellenir; duvar yakını işlem ağ çözünürlüğüyle tutarlıdır. Duvar yakını akış yeterince çözülmüşse kaymazlık doğrudan uygulanır; daha az çözülmüşse duvar modeli kullanılır. Geçirgen yüzey gibi özel sınırlarda özel doğrulama ve geçerleme yapılır. | y+ = y·u*/ν < 5 (birimsiz) | 64 |
| AC 6-10b | ZORUNLU | Bina yuvarlak biçimliyse (ayrılma yeri keskin kenarla belirlenmiyorsa), duvar yakını akış yeterince çözülmeden duvar modeli kullanmanın etkisi incelenir. | yok | 64 |
| AC 6-10c | ZORUNLU | Duvar yakını ağ çözünürlüğü ya da duvar modeli değiştirilerek ek benzetimler yapılır ve duvar işleminin basınç dağılımına etkisi sayıya dökülür. | Koşu sayısı verilmemiş | 64 |
| PO 6-11 | ZORUNLU | Giriş, çıkış, zemin, yanlar ve üstte gerçekçi sınır koşulları, alan içindeki akışın doğru temsilini verecek biçimde ayarlanır. | yok | 64 |
| AC 6-11 | ZORUNLU | Bu sınırlar §5.1.2 ve §5.1.3 hükümlerine uyar. Topografyanın geometrik modeli alandaysa topografik özelliğe ait arazi pürüzlülüğü de uygun bir pürüzlülük modeliyle temsil edilir. | yok | 64 |
| §6.5.2 yorumu | YORUM | Arazi pürüzlülüğü topografya üzerindeki akışı etkiler; model seçimi kritiktir. Ormanlık bölgelerde gölgelik yüksekliğini ve yaprak yoğunluğunun düşey değişimini alan gölgelik modelleri, yalnız z0'a dayalı duvar fonksiyonlarından daha güvenilirdir. | yok | 64–65 |
| §6.6 giriş | Çerçeve | Dört başlık: zaman adımı çözücü yakınsaması; hız ve basınç alanlarının incelenmesi ve gelen konumdaki akışın hedefle karşılaştırılması; basınç istatistiklerinin yakınsaması; ağ bağımlılığı çözümlemesi. | yok | 65 |
| §6.6.1 | ZORUNLU | Benzetim, her zaman adımı çözümünün artık birikimini en aza indirecek ve fiziksel doğruluğu koruyacak kadar yakınsamasını sağlayacak biçimde yönetilir. | yok | 65 |
| AC 4-6c (§6.6.1) | ZORUNLU | Yakınsama ölçütleri koşu boyunca sağlanır; ölçütler ve denetimler raporlanır. | Burada sayı yok (§5.4.1 yorumu: 3–4 mertebe artık düşüşü) | 65 |
| PO 6-12 | ZORUNLU | Benzetimin genel kalitesi, bina(lar)ın rüzgâr üstündeki ve çevresindeki akış alanı çözümlenerek denetlenir. | yok | 65 |
| AC 6-12a | ZORUNLU | Benzetilen her rüzgâr yönü için rüzgâr hızı ve basıncın ortalama, standart sapma (ya da türbülans şiddeti) ve anlık görüntü konturları, enterpolasyonsuz hücre merkezi değerleriyle sunulur: (1) dört yatay düzlem, en az ilk çevre bina sırasını kapsayan alanda; (2) bina(lar)ın ortasından geçen düşey düzlem(ler), aynı kapsamda. Çizimler çatı ve yanlardaki ayrılma bölgelerini ve izi yakalar. | Yatay düzlemler: h/2, 2h/3, h, h + 5 m (16 ft) | 65 |
| AC 6-12b | ZORUNLU | Bina yüksekliği boyunca ve binadan belirli uzaklığa kadar temel izleme noktası sondaları tanımlanır; yerleri alandaki bina geometrilerine göre seçilir; rüzgâr üstü akışı (özellikle rüzgâr üstü binaların izleri) ve bina izini yakalar. Her nokta için sunulacaklar: (1) hız ve basınç zaman işaretinin temsil edici bölümü; (2) hızın ortalaması, standart sapması, türbülans şiddeti; (3) hız spektrumu. | Binadan ~50 m (160 ft) uzağa kadar | 65 |
| PO 6-13 | ZORUNLU | Benzetimin genel kalitesi basınç alanı çözümlenerek denetlenir. | yok | 66 |
| AC 6-13a | ZORUNLU | Bina cephesinin bütün yüzlerinde, çatıda ve ilgiliyse eklentilerde basıncın ortalama ve standart sapma konturları çizilir; kenar ve köşe yakınındaki yüksek basınç gradyanlı bölgelere özel dikkat gösterilir. | yok | 66 |
| AC 6-13b | ZORUNLU | Basınç noktaları bina üzerine ASCE/SEI 49-21 yönergelerine göre yerleştirilir. | yok | 66 |
| AC 6-13c | ZORUNLU | Basınç izleme noktalarının çözünürlüğü, MWFRS ve C&C çalışmaları için yüzeydeki uzamsal değişimi yakalamaya yeter. | Sayı verilmemiş | 66 |
| AC 6-13d | ZORUNLU | Rapor, veri örnekleme çözünürlüğü seçimini gerekçelendirir. | yok | 66 |
| §6.6.2.2 yorumu | YORUM / ÖNERİ | Ek basınç noktaları duvar kenarlarına, köşe ayrılması ve konik girdap bölgelerine konmalı; çatı çalışmalarında saçak ve mahya yakınında yoğunlaştırılmalı. Basit bir kontur çalışması nokta sayısı ve yerini belirlemeye yardım eder. | yok | 66 |
| AC 6-13e | ZORUNLU | Referans statik basınç izleme noktası, deney modelinden, yakın çevre modelinden ve sınırlardan etkilenmeyecek biçimde konumlanır. Referans için inceleme bölgesinin doğrudan üstüne yerleştirilen bir statik basınç noktası kullanılır. | Yükseklik verilmemiş | 66 |
| PO 6-14 | ZORUNLU | Şu büyüklüklerin istatistik tahminlerinin yakınsadığı belirlenir: (1) §6.6.2.1 izleme noktalarında rüzgâr hızının ortalaması ve standart sapması; (2) ilgilenilen yük büyüklüklerinin ortalama, standart sapma ve tepe değerleri. | yok | 66 |
| AC 6-14 | ZORUNLU | Benzetim süresi, hedef bina yüksekliğindeki akış yönü integral zaman ölçeğinin belirli bir katından büyük olur. | T > 500 · T_u (T_u: akış yönü integral zaman ölçeği = integral uzunluk ölçeği / aynı yükseklikteki ortalama hız, §1.8) | 66 |
| §6.6.3 yorumu | YORUM | Gereken süre, başlangıç (spin-up) süresi ile ortalama alma süresinden oluşur ve probleme bağlıdır. Hız için yeterlilik Bölüm 5'teki gibi denetlenir (yorum "§5.4.3" der; yöntem §5.4.2'de anlatılır). Toplam yük ve moment istatistikleri; kaplama için büyük emme ya da basınç beklenen cephe noktalarındaki basınç işaretleri kullanılır. Büyüyen pencereyle ortalama ve standart sapma izlenir; tepe değerler için blok en büyükleri ya da eşik üstü tepeler yöntemleri kullanılabilir. | yok | 66 |
| PO 6-15 | ZORUNLU (must) | Ağın incelenen durum için yeterince ince olduğundan emin olmak üzere proje için en az iki rüzgâr yönünde ağ çalışması yapılır. | ≥ 2 rüzgâr yönü | 67 |
| AC 6-15a | ZORUNLU | Çözümlenen benzetimlerde IRQ, akış alanındaki ve basınç alanındaki temel izleme konumlarında belirli değerden düşük olmaz. İki ağ çözünürlüğü arasında öngörülen yük büyüklüklerindeki farklar raporlanır. | IRQ ≥ %75 | 67 |
| AC 6-15b | ZORUNLU | Temel izleme konumu, bina yüksekliği boyunca ve binadan belirli uzaklığa kadar bir dizi sanal sonda noktasından oluşur; özel durumlara yer bırakılır. Sondalar yaklaşan akışı (özellikle rüzgâr üstü izler) ve bina izini yakalar. | Binadan ~50 m (160 ft) uzağa kadar | 67 |
| §6.6.4 yorumu (genel) | YORUM | Örtük süzgeçli LES/DES'te ağ boyutu süzgeç boyutunu belirlediği için her ağ farklı ölçek çözer; çözüm ancak DNS inceliğine yaklaşınca ağdan bağımsız olur. Modelleme ve ayrıklaştırma hataları birlikte değerlendirilmelidir. Pratik yol IRQ'dur; ayrıca farklı ağlarla elde edilen temel büyüklükleri karşılaştırmak yararlıdır. | yok | 67 |
| §6.6.4 yorumu (ağ sayısı ve r) | YORUM (içinde shall geçer) | IRQ için proje en çok üç ağla (kaba, orta, ince) benzetilir; ağlar ardışık olarak r katsayısıyla inceltilir. İdeal inceltme katsayısı 2'dir ama pahalıdır; en küçük r için metin çıkarımında "en az 2" yazıyor, bu ideal değerle aynı olduğundan bir simgenin (büyük olasılıkla kök işareti) düştüğü anlaşılıyor. | r ideal = 2; en küçük r: metinde güvenle okunamadı | 67 |
| §6.6.4 yorumu (p seçimi) | YORUM / ÖNERİ | p sayısal yöntemin mertebesidir; çoğu ticari çözücüde ikinci mertebe. Etkin mertebe Denklem 6-5 ile kestirilebilir ve şemanın mertebesine yaklaşık uymalıdır. Ardışık çözümlerin asimptotik bölgede olduğu güvencesi yoktur; alt ızgara katkısını az kestirmemek için p dikkatle seçilmeli; kestirilen mertebe kuramsaldan belirgin yüksekse kuramsal mertebe benimsenmemelidir. | p ≈ 2 (ikinci mertebe şemalar) | 67–68 |
| §6.6.4 yorumu (IRQ sınıfları) | YORUM | IRQ aralıklarının yorumu: düşükse daha fazla inceltme gerekir; orta aralık mühendislik çözümleri için uygun; yüksekse DNS'e yakın. | < %75: inceltme gerekli; %75–%85: mühendislik için eniyilenmiş; > %85: DNS'e yakın | 68 |
| PO 6-16 | ZORUNLU | Zaman adımı duyarlılığı incelenir. | yok | 68 |
| AC 6-16 | ZORUNLU | Rüzgâr hızı spektrumları, incelenen bina çevresindeki temel konumlarda ve hedef bina ile rüzgâr üstü binalar arasındaki bölgelerde çizilir; ağ boyutundan ve zaman adımından kaynaklanan kesme çizimlerde işaretlenir. | yok | 68 |
| §6.6.5 yorumu | YORUM | Duyarlılık çözücü türüne bağlıdır. Açık şemalar yerel hücre boyu ve hıza bağlı en büyük zaman adımı dayatır (CFL sayısı). Örtük şemalarda CFL 1'in üstüne çıkarılabilir, ama gereken zaman ölçekleri çözülmelidir; aşırı büyük adımda çözücü ıraksayabilir. İyi bir yöntem: zaman adımını yarıya indirip spektrumları karşılaştırmak; aynı ya da çok benzerse adım yeterlidir. Seçenek: ağ duyarlılığı çalışmasında CFL sayısını korumak. | CFL: örtük şemada > 1 olabilir; sayısal üst sınır verilmemiş; sınama için Δt/2 | 68 |

## Denklemler (düz metin)

| Denklem | Durum | İçerik | PDF sayfası |
|---|---|---|---|
| y+ (AC 6-10a içinde, numarasız) | Dizgi bozuk; yapı okunuyor | y+ = y · u* / ν < 5 (y: duvara dik uzaklık, u*: sürtünme hızı, ν: kinematik viskozite) | 64 |
| (6-3) | Okunuyor | IRQ = k_çözülen / k_toplam | 67 |
| (6-4) | Okunuyor (üs konumu dizgiden çıkarıldı) | k_toplam = k_çözülen + a_k · Δ^p; ikinci terim alt ızgara katkısının kestirimi; Δ süzgeç genişliği (örtük süzgeçte etkin ağ boyutu) | 67 |
| (6-5) | Metin çıkarımında bozuk; yapı kısmen okunuyor | p = ln[ (k_çözülen,kaba − k_çözülen,orta) / (k_çözülen,orta − k_çözülen,ince) ] / ln(r). Pay ve paydanın bu sırası bozuk metinden çıkarılmıştır; özgün PDF'ten denetlenmeli. | 67 |
| (6-6) | Metin çıkarımında bozuk; yapı kısmen okunuyor | Görülen parçalar: a_k, (1 / Δ_ince^p), (k_çözülen,ince − k_çözülen,orta), (r^p − 1). Olası biçim: a_k = (1/Δ_ince^p) · (k_çözülen,ince − k_çözülen,orta) / (r^p − 1). Kesin biçim metinde okunamadı; özgün PDF'ten denetlenmeli. | 68 |

Etkin ağ boyutu Δ için Denklem 5-5'e bakılır: Δ = (Δ_x · Δ_y · Δ_z)^(1/3) (s. 58).

## Metinde bulunamayanlar (§6.1, §6.5, §6.6 içinde)

- Toplam kaç rüzgâr yönünün benzetileceği (yalnız ağ çalışması için "en az iki yön" verilir).
- Bina benzetimi için referans hızın tanımı ve okunacağı yer (referans statik basınç AC 6-13e'de var; referans hız bu bölümlerde yok; AC 5-9 (6) çatı/tepe yüksekliğindeki referans hızdan söz eder).
- Referans statik basınç noktasının yüksekliği ya da uzaklığı için sayı.
- Zaman adımı ya da CFL için sayısal sınır.
- Başlangıç geçişi (spin-up) için sayısal süre; 500 katlık şartın yalnız ortalama alma süresini mi toplam süreyi mi kastettiği açıkça ayrılmamış, metin "benzetim süresi" der.
- Basınç noktası sayısı ya da aralığı için sayı (ASCE/SEI 49-21'e gönderilir).
- İki ağ arasındaki yük farkı için kabul edilebilir yüzde.
