# Referans: ASCE CWE Prestandard §5 girişi, §5.1 ve §5.4

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Sayfa numaraları PDF sayfa sırasıdır. Özetler kendi cümlelerimizle yazılmıştır; alıntı değildir.

Tür: ZORUNLU = shall, ÖNERİ = should, YORUM = commentary (bağlayıcı değil).

## Maddeler

| Madde | Tür | Özet | Sayısal ölçüt (birimiyle) | PDF sayfası |
|---|---|---|---|---|
| §5 giriş | ZORUNLU | Yaklaşan akış benzetimleri §4.2'deki bütün PO/AC maddelerini (yöntem, ayrıklaştırma, çözülmeyen türbülans modeli, çözücü yakınsaması, geometri ve hız ölçeği) de sağlar. | yok | 49 |
| §5 giriş | YORUM | Bölümün içeriği yaya konforu/güvenliği ve hava kalitesi için LES'e de aynı ölçüde uygulanabilir. | yok | 49 |
| PO 5-1 | ZORUNLU | Alan boyutu hedef akışı doğru temsil edecek ve sınır koşullarının istenmeyen etkisinden kaçınacak biçimde seçilir. | yok | 49 |
| AC 5-1 | ZORUNLU | Yükseklik sınır tabakasının ilgili kısmını alır ve bina benzetiminin düşey tıkanma şartını sağlar (§6.3). Akış yönü uzunluk, bina benzetimindeki giriş–ilk bina uzaklığından büyüktür ve ilk bina konumunda akış yönü uzunluk ölçeklerini temsil edecek kadar uzundur. Genişlik yanal uzunluk ölçeklerini temsil etmeye yeter. | Sayısal kat verilmemiş; düşey tıkanma için §6.3 (BR_z ≤ %17) | 49 |
| AC 5-1 yorumu | YORUM | Küçük alan türbülansı ve uzunluk ölçeklerini bozar. Yanal periyodik koşulda iki yanın istenmeyen bağlaşması yapay büyük yapılar üretebilir. Üç türbülans şiddeti, akış yönü bileşeninin spektrumu ve uzunluk ölçeği ile akış görselleştirmesi birlikte alanın yeterliliğini gösterir. | yok | 49–50 |
| PO 5-2 | ZORUNLU | Yaklaşan akış bölgesinde ağ, sonraki bina benzetimi için önemli küçük ölçekli türbülansı yakalayacak incelikte olur; ölçü, gelen akış güç spektrumundaki en yüksek indirgenmiş frekanstır. | yok | 50 |
| AC 5-2 | ZORUNLU | En yüksek tam çözülen indirgenmiş frekans kaplama yükleri için en az 2, toplam yükler için en az 1 olur. L_b probleme uygun karakteristik boyut, n tam çözülen en yüksek frekans, U yükü üreten yerel referans hız. Bu frekansın atalet alt aralığında olduğu doğrulanır. | n·L_b/U ≥ 2 (kaplama); n·L_b/U ≥ 1 (toplam yük); n [Hz], birimsiz oran | 50 |
| AC 5-2 yorumu | YORUM | 2 değeri, gelen akıştaki küçük ölçekli türbülansın tepe yüklere yol açan basınç oynamalarına katkısından gelir; toplam yüklerde bu katkı azaldığı için şart gevşetilmiştir. n, akış yönü hız spektrumunun atalet alt aralığında −2/3 eğimiyle uyumlu kaldığı en yüksek frekans olarak alınır (Şekil 5-2). | eğim −2/3 (indirgenmiş spektrum) | 50–51 |
| PO 5-3 | ZORUNLU | Türbülanslı giriş koşulu, model seçimleri ve ağla birlikte, gelen konumda hedef türbülanslı rüzgârı üretmeyi destekler. Hedef Bölüm 3'ten gelir. Gelen konum, bina benzetiminde hesap alanındaki en rüzgâr üstü bina ya da yapının konumuyla çakışır. | yok | 51 |
| AC 5-3 | ZORUNLU | Arazi açıklığı rüzgâr yönüyle değişiyorsa, gelen konumdaki türbülanslı akışın kalitesi bütün yönlerde karşılaşılan her farklı açıklık koşulu için gösterilir. | yok | 51 |
| §5.1.2 yorumu (yöntem aileleri) | YORUM | Giriş türbülansı yöntemleri üç ailedir: öncül benzetim (precursor), geri besleme (recycling), yapay üretim (synthetic). Profilleri alan boyunca gerçekçi tutmak kolay değildir. | yok | 51 |
| §5.1.2 yorumu (precursor/recycling) | YORUM | Önceden koşulup zaman ve konuma bağlı hız alanı veri tabanına yazılabilir. Zemin pürüzlülük elemanları duvara komşu hücreden kısaysa rüzgâr için yazılmış pürüzlü duvar fonksiyonu kullanılabilir (z0 etkisini doğru vermeli). Elemanlar ilk hücreyi aşıyorsa etkileri çözülmeli; yükseklik ve aralıkları hedef profili verecek biçimde tanımlanmalı. Yetersiz uzaklıkta geri besleme/periyodik koşul büyük yapıların kalıcı kilitlenmesine yol açabilir; periyodik koşulu kaydırmak gerekir. | yok | 51 |
| §5.1.2 yorumu (synthetic, basınç) | YORUM | Yapay üreteçler verimlidir ama sahte basınç oynamaları üretebilir; bu, oynak yüzey basınçlarının tahminini bozar. Giderilmesi gerçekçi yüzey basıncı için zorunlu sayılır; yazında bunu azaltan yöntemler vardır. | yok | 51 |
| §5.1.2 yorumu (synthetic, sönme) | YORUM / ÖNERİ | Girişte verilen yapay türbülans aşağı akışta bir denge durumuna doğru gelişir. Log yasasıyla uyumlu zemin duvar işlemi ortalama profili korur; ancak giriş ile ilgilenilen konum arasında türbülans şiddetinde azalma sık görülür ve bu, bina üzerindeki basınç oynamalarının tahminine zarar verir. Gelişim yakından izlenmeli (should); belirgin değişim varsa giriş istatistikleri aşağı akış hedefini tutturacak biçimde eniyilenebilir. | Sayısal sınır verilmemiş (bağlayıcı sınır AC 5-9'dadır) | 51 |
| §5.1.2 yorumu (deneme-yanılma) | YORUM | Belirli bir gelen akışı veren kurulumu bulmak deneme-yanılma gerektirebilir; rüzgâr tünelinde pürüzlülük elemanı, çit, kule düzeni aramaya benzer. | yok | 51–52 |
| PO 5-4 / AC 5-4 | ZORUNLU | Zemin sınır koşulu, Bölüm 3'ten belirlenen z0 için hedef gelen akışı yeniden üretmeyi destekler. | yok | 52 |
| §5.1.3.1 yorumu (iki yol) | YORUM | Pürüzlülük, elemanların etkisi çözülerek ya da hedef ortalama profille uyumlu sürtünme hızı bağıntısı veren duvar yakını modeliyle temsil edilir. | yok | 52 |
| §5.1.3.1 yorumu (açık elemanlar) | YORUM / ÖNERİ | Elemanlar açıkça modelleniyorsa binalara uzaklıkları, tek tek elemanların yerel etkisi binaya ulaşmayacak kadar büyük olmalı. Temsil seçenekleri: gövdeye uyan ağ, gömülü sınır (immersed boundary), hacim kuvveti. | yok | 52 |
| §5.1.3.1 yorumu (duvar modeli) | YORUM / ÖNERİ | Pürüzlülük yüksekliği bina benzetimindeki ilk hücre yüksekliğinden küçük ya da ona yakınsa duvar yakını modeli kullanılabilir. Model sürtünme hızını nötr log yasasıyla uyumlu vermeli; en basit denge yaklaşımı yalnız z0 ister. Bu modellerin, özellikle duvar yakını ağ ince olduğunda, başarısız olabildiği bildirilmiştir. | yok | 52 |
| §5.1.3.1 yorumu (kum tanesi) | YORUM | Birçok LES kodundaki pürüzlü duvar fonksiyonu kum tanesi pürüzlülüğüne göredir ve pürüzlü arazi rüzgârına doğrudan uygulanamaz; fonksiyonun rüzgâr için yazıldığı ve girdinin z0 olduğu doğrulanmalı. | yok | 52 |
| PO 5-5 / AC 5-5 | ZORUNLU | Yan, üst ve çıkış sınırları için hedef türbülanslı akışın doğru modellenmesine izin veren uygun koşullar tanımlanır. | yok | 52 |
| §5.1.3.2 yorumu | YORUM | Yanlar: periyodik koşul yaygın (üç boyutlu oynamaya izin verir, istenmeyen yanal gradyanı önler). Üst: kaygan duvar ya da uzak alan basıncı. Seçenek: yan ve üst, tüneldeki gibi kaymaz duvar; duvar sınır tabakalarıyla etkileşmeyecek kadar uzak olmalı. Çıkış: hız ve türbülans için sıfır gradyan ya da taşınımlı koşul; gerekirse sönümleme (kararsızlık, yansıma). | yok | 52–53 |
| §5.4 giriş | ZORUNLU (çerçeve) | Amaç, fiziksel olarak tutarlı yaklaşan akış ve gelen konumda hedef sınır tabakası. Giriş koşulları, gelen konumda hedefi tutacak biçimde tanımlanır. Dört başlık: çözücü yakınsaması, alan incelemesi ve hedefle karşılaştırma, istatistik yakınsama, ağ yeterliliği. | yok | 55–56 |
| AC 4-6b (§5.4.1) | ZORUNLU | Yakınsama ölçütleri koşu boyunca uygulanır; ölçütler ve denetimler raporlanır. | yok | 56 |
| §5.4.1 yorumu | YORUM / ÖNERİ | Yinelemeli çözücüde her zaman adımında artıklarda düşüş beklenir; ya da momentum ve kütle dengesizlikleri küçük ve sınırlı olmalı. Çözücü ölçüte ulaşmadan (en çok yineleme sayısıyla) ilerlerse doğruluk bozulabilir. | 3–4 mertebe artık düşüşü | 56 |
| PO 5-7 | ZORUNLU | Gelen konumdaki hız profillerinin ortalama ve standart sapma tahminlerinin yakınsaması değerlendirilir. | yok | 56 |
| AC 5-7 | ZORUNLU | Çözümlemeden önce atılan başlangıç geçişi T_init ve istatistik için kullanılan ortalama süresi T_avg raporlanır. Ortalama süresinin, bina yüksekliğinde ortalama hız ve türbülans şiddetlerini yakınsatmaya yettiği gösterilir. | Sayısal süre verilmemiş | 56 |
| §5.4.2 yorumu | YORUM / ÖNERİ | Başlangıç geçişinin uzunluğu alan boyutuna, rüzgâr hızına ve çözülen zaman ölçeklerine bağlıdır. Yeterince uzun zaman serisi kullanılmalı. En basit denetim: geçiş atıldıktan sonra büyüyen pencereyle ortalama ve standart sapmayı hesaplayıp oturup oturmadığına bakmak. | yok | 56 |
| PO 5-8 | ZORUNLU | Kurulumun rüzgâr ve basınç alanlarını fiziksel olarak tutarlı temsil ettiği gösterilir. | yok | 56 |
| AC 5-8 | ZORUNLU | Her farklı sınır tabakası koşulu için: anlık hız ve basınç görüntüleri; ortalama akış yönü hızı, üç hız oynamasının standart sapması (ya da türbülans şiddetleri), ortalama basınç ve basınç oynaması standart sapması kontur çizimleri. Düzlemler: genişlik ortasında düşey düzlem; incelenen bina yüksekliğinde yatay düzlem. | 2 düzlem | 56 |
| PO 5-9 | ZORUNLU | Gelen konumdaki akış, Bölüm 3'ten belirlenen hedef akışı doğru temsil eder. | yok | 56 |
| AC 5-9 (çerçeve) | ZORUNLU | Aşağıdaki altı madde, girişten x_i uzaklıktaki gelen konumda, hem genişlik ortasında hem merkez hattından ölçülen 1/3 genişlik konumlarında sağlanır. | Yanal konumlar: merkez ve 1/3 genişlik | 56 |
| AC 5-9 (1a) | ZORUNLU | Ortalama hız profil biçimi için z0'ın karakteristik boyuta oranı modelde ve tam ölçekte eşit olur (m: gerekirse ölçekli hesap modeli, p: tam ölçek hedef). Tam ölçek z0 tahminindeki belirsizlik nedeniyle üç kat içinde sağlanması yeter. | (z0/L_b)_m = (z0/L_b)_p, 3 kat içinde | 57 |
| AC 5-9 (1b) | ZORUNLU | Benzetilen ve hedef ortalama hız profilleri arasındaki fark, h_max'ın üst %75'i boyunca %10'dan küçük olur. Topografya Yöntem 1 (§3.3.2) uygulanıyorsa aralık h_max'ın %100'üne genişler. Ölçü Denklem 5-1'dir. | < %10; aralık: h_max'ın üst %75'i (Yöntem 1: %100) | 57 |
| AC 5-9 (2) | ZORUNLU | Türbülans şiddeti I_u profili için aynı şart; ölçü Denklem 5-2. | < %10; aralık: h_max'ın üst %75'i (Yöntem 1: %100) | 57 |
| AC 5-9 (3) | ZORUNLU | Yükleme mekanizmalarını doğru tahmin için gereken integral uzunluk ölçeği bileşenleri hedefin üç katı içinde olur. | 3 kat içinde | 57 |
| AC 5-9 (4) | ZORUNLU (çizim) | Gereken hız oynaması bileşenlerinin güç spektral yoğunlukları, tasarlanan bina/yapının çatı ya da tepe yüksekliğinde çizilir. Sayısal kabul sınırı verilmemiş. | yok | 57 |
| AC 5-9 (5) | ZORUNLU (çizim) | Gereken Reynolds gerilmesi bileşenlerinin profilleri çizilir; ilgili çapraz spektral yoğunluklar çatı/tepe yüksekliğinde çizilir. Sayısal kabul sınırı verilmemiş. | yok | 57 |
| AC 5-9 (6) | ZORUNLU | Basınç oynamalarının standart sapma profilleri çizilir ve çatı/tepe yüksekliğindeki referans hızla hesaplanan dinamik basıncın %10'unu aşmadığı doğrulanır. | σ_p ≤ 0,10 · q_ref (q_ref: çatı/tepe referans hızıyla dinamik basınç) | 57 |
| PO 5-10 | ZORUNLU | Ağ çözünürlüğünün yeterliliği gösterilir. | yok | 57 |
| AC 5-10 | ZORUNLU | Kesme frekansı, akış yönü hız bileşeninin güç spektrumunda gösterilir ve AC 5-2'yi sağladığı doğrulanır. | AC 5-2 sınırları | 57 |
| §5.4.4 yorumu | YORUM | Ağ, çözülebilen en küçük türbülans ölçeğini belirler; hedef binanın rüzgâr üstündeki ağ boyutu kesme frekansını doğrudan etkiler; bunun üstü alt ızgara (SGS) modeline kalır. Kesme frekansı n_c, Denklem 5-3'ün yinelemeli çözümüyle bulunabilir. | yok | 57–58 |

## Denklemler (düz metin)

| Denklem | Durum | İçerik | PDF sayfası |
|---|---|---|---|
| (5-1) | Metin çıkarımında bozuk; kısmen okunuyor | Okunan parçalar: eps_ABL-U = (1/h_max) · integral[ (U_hedef − U_benzetim) / U_hedef ] dz ≤ 0,1; üst sınır h_max. Mutlak değer işareti ve alt integral sınırı metinde okunamadı (maddenin cümlesi aralığı "h_max'ın üst %75'i" olarak verir; Topografya Yöntem 1'de %100). | 57 |
| (5-2) | Metin çıkarımında bozuk; kısmen okunuyor | eps_ABL-Iu = (1/h_max) · integral[ (I_u,hedef − I_u,benzetim) / I_u,hedef ] dz ≤ 0,1; üst sınır h_max. Mutlak değer ve alt sınır okunamadı (aynı not). | 57 |
| (5-3) | Denklem metinde okunamadı | Görülen simgeler: Delta, pi, n_c, F(n_c). Kesme frekansı n_c ile etkin ağ boyutu Delta arasında, F(n_c) içeren ve yinelemeyle çözülen bir bağıntı; kesir yapısı çıkarılamadı. Özgün PDF'ten denetlenmeli. | 57 |
| (5-4) | Okunuyor | F(n_c) = toplam (i = 1..3) S_ii(n_c); S_ii: i. bileşenin türbülans öz güç spektrumu. | 58 |
| (5-5) | Okunuyor (kök işareti dizgiden çıkarıldı) | Delta = (Delta_x · Delta_y · Delta_z)^(1/3); Delta_x, Delta_y, Delta_z hücre boyutları; Delta ilgilenilen yerdeki etkin ağ boyutu. | 58 |

## Tanımlar (§1.8, §1.9, §4.1)

| Terim | Özet | PDF sayfası |
|---|---|---|
| Incident location (gelen konum) | Hesap alanında bir binanın ya da topografyanın eklendiği en rüzgâr üstü konum. §4.1 (AC 4-1) aynı tanımı "ikinci adımda eklenecek" ifadesiyle verir. | 24; 43 |
| Approach flow region | Giriş sınırından inceleme bölgesine kadar olan ve onu içeren ağ bölgesi. | 24 |
| Study region (inceleme bölgesi) | İncelenen binayı, açıkça modellenen çevresini ve yakın topografyayı saran kutu; yaklaşan akış bölgesini içermez. | 25 |
| h_max | Binanın yüksekliği ile çevre binaların ortalama yüksekliğinden büyük olanı. | 26 |
| Longitudinal integral time scale | İntegral uzunluk ölçeğinin aynı yükseklikteki ortalama hıza bölümü. | 25 |

## Metinde bulunamayanlar

- §5.1 alan boyutu için sayısal kat (bina yüksekliği cinsinden uzunluk, genişlik) vermez.
- §5.4.2 T_init ve T_avg için sayısal alt sınır vermez (bina benzetimindeki 500 integral zaman ölçeği şartı AC 6-14'tedir).
- AC 5-9 (4) ve (5) için spektrum/Reynolds gerilmesi uyumuna sayısal tolerans verilmemiştir.
- Girişten gelen konuma türbülans azalması için sayısal bir izin verilen düşüş yoktur.
