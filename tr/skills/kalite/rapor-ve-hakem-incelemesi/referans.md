# Referans — Bölüm 9: Rapor içeriği ve Bölüm 10: Proje hakem incelemesi

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 9 ve 10.
"PDF sayfası" = PDF sıra numarası (basılı sayfa = PDF − 18).
Tür: ZORUNLU = "shall", ÖNERİ = "should / recommended", YORUM = "Commentary" ya da açıklayıcı metin.
Bu iki bölümde PO/AC numaralı madde yoktur; şartlar alt bölüm numarasıyla verilir. Sayısal eşik neredeyse hiç yoktur.

## Bölüm 9 — Rapor içeriği

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §9 giriş | ZORUNLU | Bölüm, benzetimin niteliğini (varsayımlar, sınırlamalar, teknik parametreler, sonuçlar) belgelemek için en az şartları verir. Rapor, üçüncü tarafın ve gerekiyorsa AHJ'nin ayrıntılı teknik incelemesine yetecek bilgiyi içerir ve çalışmanın Bölüm 2–7 performans hedefleriyle uyumunu gösterir. Aşağıdaki başlıklar kapsamla ilgili olduğu ölçüde doğrudan ele alınır; hakem ya da sponsor ek içerik isteyebilir. | yok | 89 |
| §9 giriş yorumu | YORUM | Raporun birincil amacı sponsor ile rüzgâr mühendisinin anlaştığı girdileri, varsayımları ve sonuçları kaydetmektir; ikincil olarak, ASCE/SEI 7-22'ye göre rüzgâr tüneli deneyine seçenek bir yöntem olarak uygunluğun hakem ekibi ve AHJ tarafından incelenebilmesini sağlar. | yok | 89 |
| §9.1 | ZORUNLU | Benzetimin birincil kapsam ve amaçları ile projenin temel özellikleri belirtilir. | yok | 89 |
| §9.2 | ZORUNLU | Hesap alanı, ilgili geometrik koşullar ve önemli özellikler (giriş geometrisi, pürüzlülük elemanları, zaman adımı) ile sınır koşulları anlatılır. | yok | 89 |
| §9.2.1 (a) | ZORUNLU | Yazılımın adı, geliştiricisi ve sürümü; akış modellemesinin temel özellikleri; türbülans üretim yaklaşımı (yapay ve/veya doğal) ve çözülmeyen türbülansın ele alınışı. | yok | 89 |
| §9.2.1 (b) | ZORUNLU | Uzamsal ayrıklaştırma ve gradyan enterpolasyon yöntemleri, zamansal ayrıklaştırma yöntemleri; çözüm yöntemi, zaman adımı, en büyük CFL sayısı, çözücü yakınsama ölçütleri. | yok | 89–90 |
| §9.2.1 (c) | ZORUNLU | Toplam benzetim süresi, istatistik hesaplamak için kullanılan süre ve istatistik kestirimlerinin yakınsamasını denetleme yöntemi; ilgili diğer yöntem konuları. | yok | 90 |
| §9.2.2 (a) | ZORUNLU | Hesap alanının tüm özellikleri (geometri vb.); giriş, zemin, yan, üst ve çıkış sınır koşulları; arazi elemanları ve topoğrafik özellikler ile bunların alandaki temsili. | yok | 90 |
| §9.2.2 (b) | ZORUNLU | Ağ ve çözünürlüğün yaklaşım akışı, yakın akış, yerel akış ve uzak alan bölgelerindeki değişimi; bina çevresindeki, yüzler ve köşelerdeki yerel çözünürlük. | yok | 90 |
| §9.2.3 | ZORUNLU | Tüm ölçekleme parametreleri: geometrik uzunluk ölçeği, zaman ölçeği, zaman adımı; akışkan yoğunluğunun ele alınışı; Reynolds sayısı; bina eklenmiş alanda hedef ve ulaşılan tıkanma oranı; zamansal ayrıklaştırmanın CFL sayısı (Bölüm 4'e göre). | yok | 90 |
| §9.2.4 | ZORUNLU | İncelenen binanın benzetim özellikleri: tam geometri, yüzey parametreleri, modellenen ya da atlanan ek elemanlar; ilgili tüm yüzey ve özellikleri gösteren görseller. | yok | 90 |
| §9.3 | ZORUNLU | Akış özellikleri hem boş hesap alanı hem de bina ve yakın çevre eklenmiş alan için belgelenir; uygulanabildiği yerde hedef ve benzetilen değer/profil birlikte verilir. | 2 durum | 90 |
| §9.3.1 | ZORUNLU | Yerel rüzgâr iklimi, meteoroloji veri kaynağı ve kalitesi; yöne göre hedef referans hızlar ve dönüş periyotları; yaklaşım arazisi ve yöne göre hedef maruziyet sınıfları; dikkate alınan fırtına türleri; yönselliğin benzetimde ve sonuçlarda ele alınış biçimi. | yok | 90 |
| §9.3.2 | ZORUNLU | Sahayı ve binayı etkilediği düşünülen tüm hava sistemi türleri ve benzetime nasıl katıldıkları (bkz. §3.1). | yok | 90 |
| §9.3.3 | ZORUNLU | Sahaya özgü olasılıksal rüzgâr iklimi modelinin ilgili tüm ayrıntıları ve referans akış koşulları (bkz. §3.2, §3.3). | yok | 91 |
| §9.3.3.1 | ZORUNLU | Ortalama hız profili hesap alanı boyunca uzamsal olarak belgelenir (ölçütler Bölüm 5'te). | yok | 91 |
| §9.3.3.2 | ZORUNLU | Boyuna, yanal ve düşey türbülans şiddeti profilleri alan boyunca belgelenir (ölçütler Bölüm 5'te). | 3 bileşen | 91 |
| §9.3.3.3 | ZORUNLU | Türbülans integral uzunluk ölçeği profili alan boyunca belgelenir; benzetilen değerlerin tam ölçekte beklenen atmosfer hedefiyle karşılaştırması anlatılır. | yok | 91 |
| §9.3.3.4 | ZORUNLU | Hız çalkantılarının güç spektral yoğunluğu benzetim hacmi boyunca boyuna, enine ve düşey olarak belgelenir; tam ölçek atmosfer spektrumuyla karşılaştırılır. Kısmi türbülans modellerinde eksik düşük frekanslı türbülansın nasıl hesaba katıldığı anlatılır. (Metin, ölçütler için Bölüm 8'e gönderme yapar.) | 3 doğrultu | 91 |
| §9.3.4 | ZORUNLU (emir kipi) | Benzetime dahil edilen başlıca topoğrafik özellikler anlatılır (şartlar Bölüm 3'te). | yok | 91 |
| §9.3.5 | ZORUNLU (ilgiliyse) | Benzetimin ekstratropikal ve sinoptik olmayan fırtına sistemlerinin etkisini nasıl ele aldığı anlatılır. | yok | 91 |
| §9.4 | ZORUNLU | Kapsama dayalı tüm ilgili sonuçlar verilir; kuvvetlerin benzetimde hangi yolla ölçüldüğü anlatılır. Aşağıdaki liste, ağırlıklı olarak yapısal rüzgâr yükü ve tepkisine odaklı bir kapsam için beklenen sonuçlardır. | yok | 91 |
| §9.4 yorum | YORUM | Çıktının içeriği, tescilli tasarım uzmanıyla anlaşılan kapsama göre değişir; farklı kapsamlı benzetimler farklı sonuç türleri gerektirebilir. | yok | 91 |
| §9.4.1 | ZORUNLU | Kullanılan x, y, z eksen takımı ve proje eksenleriyle ilişkisi tanımlanır. | yok | 92 |
| §9.4.2 | ZORUNLU | Ele alınan rüzgâr yönü sayısı ve bu yönlerin sonuçlara nasıl temel oluşturduğu anlatılır. | yok | 92 |
| §9.4.3 | ZORUNLU | Aerodinamik kuvvet ve moment katsayılarının ortalaması ve standart sapması verilir; tüm benzetilen yönler için, yönsellik etkisi dikkate alınmadan önce ve sonra. | yok | 92 |
| §9.4.4 | ZORUNLU | Taban devrilme momenti ve taban kesmesi için, seçilen kritik rüzgâr yönleri ve/veya kritik tepki doğrultularında, hem rüzgâr doğrultusundaki hem rüzgâra dik tepki için güç spektral yoğunluğu grafikleri verilir. | yok | 92 |
| §9.4.5.1 | ZORUNLU | Genel taban kesmeleri ve devrilme momentleri, tanımlı referans kot(lar)ında, iki dik doğrultuda, ele alınan dönüş periyotları ve yönler için verilir. Taban kesme, devrilme momenti ve burulmanın yöne göre ortalama, en küçük, en büyük grafikleri verilir. Bina yüksekliği boyunca kuvvet ölçme ve taban kuvvetlerini belirleme yöntemi anlatılır. Genel bina yüklerinin DAF değeri nicelenir. | 2 dik doğrultu | 92 |
| §9.4.5.2 | ZORUNLU (koşullu) | Kapsamda istenmişse ya da AHJ / hakem heyeti isterse, taban kesme ve momentlerinin sönüm, kütle ve frekans değişimlerine duyarlılığı verilir. | yok | 92 |
| §9.4.5.3 | ZORUNLU | Tanımlı yapısal dinamik özellikler için, yapı yüksekliği boyunca her katta dikkate alınacak eşdeğer statik (ya da etkin) rüzgâr yükleri verilir. | yok | 92 |
| §9.4.5.4 | ZORUNLU | Kat kat eşdeğer statik yükler için, burulma etkisi dahil, tüm ilgili yön ve etkilerden gelen yükleme ve tepkiyi yakalayan yön birleşimleri verilir. | yok | 92 |
| §9.4.5.5 | ZORUNLU | Yönetmelik ya da standarda dayalı yöntemle elde edilen genel tasarım rüzgâr yükleri verilir ve CWE benzetiminden elde edilen tasarım yükleriyle karşılaştırılır. | yok | 92 |
| §9.4.5.6 | ZORUNLU | Bina hareketi kestirimleri (yanal ve burulma ivmeleri) istenen konumlarda (ör. kulenin üst katları, kullanıcıya duyarlı alanlar) verilir; belirtilen dönüş periyotları için tepe ivme sonuçları yer alır. | yok | 92 |
| §9.4.5.7 | ZORUNLU (koşullu) | Kapsamda istenmişse ya da AHJ / hakem heyeti isterse, tepe ivme kestirimlerinin sönüm, kütle ve frekansa duyarlılığı verilir. | yok | 93 |
| §9.4.5.8 | ZORUNLU | Belirtilen dönüş periyotları için yerel ve alan ortalamalı kaplama basınçları verilir; tüm bina kabuğunda pozitif (içe) ve negatif (dışa) etkiler için ortalama ve tepe basınçlar yer alır. İlişkili iç basınçların ele alınış yaklaşımı ile yerel basınç ölçüm konumları ve yöntemi anlatılır. | yok (alan büyüklüğü verilmemiş) | 93 |
| §9.4.5.9 | ZORUNLU | MWFRS'nin parçası olan ya da olmayan uzun açıklıklı esnek elemanlara (uzun açıklıklı çatılar, büyük kapama duvarları vb.) etkiyen, dinamik rüzgâr etkilerini içeren eşdeğer statik yük verilir. Tepe yük etkileri belirlenirken elemanların etki alanı, alan yükleme etki katsayıları (ör. büyük konsollar) dahil, dikkate alınır. | yok | 93 |
| §9.4.5.10 | ZORUNLU | Çatı üstü ya da kabuğa bağlı ek elemanlar, saçaklar ve çıkmalar, tabelalar ve direkler için tepe kuvvet ve moment talepleri verilir. Tescilli tasarım uzmanı, esnek bileşenlerde çırpınma (flutter) ve dörtnal (galloping) olasılığı dahil aeroelastik etkiler hakkında da görüş bildirir. | yok | 93 |
| §9.4.5.11 | ZORUNLU | İç basınçların nasıl dikkate alındığı ve verilen genel tasarım yüklerine nasıl girdiği anlatılır. | yok | 93 |
| §9.5.1 | ZORUNLU | İklimin yapısal tepkiyle birleştirilmesinde kullanılan istatistik yöntem (sektör, yukarı geçiş, fırtına geçişi vb.) belgelenir. | yok | 93 |
| §9.5.2 | ZORUNLU | Analizde varsayılan kütle, sönüm, rijitlik ve mod biçimleri ile bunların kaynağı (sponsor verisi, yönetmelik kestirimi, yerinde ölçüm) belirtilir. Sponsor isterse duyarlılık değerlendirmeleri eklenir. | yok | 93 |
| §9.5.3 | ZORUNLU | Kullanılan hesaplama yaklaşımının başlıca sınırlamaları verilir; sonuçların doğruluğunu ya da uygulanabilirliğini etkileyen varsayımlar vurgulanır. | yok | 93 |
| §9.5.4 | ZORUNLU | İlgilenilen çıktı büyüklükleri için benzetim kalitesi; ağ inceltme, zaman adımı duyarlılığı, iç yineleme çözücü yakınsaması, istatistik yakınsama ve spektral özellikler bakımından değerlendirilir. Girdi parametrelerinden (rüzgâr verisi, arazi pürüzlülüğü modellemesi dahil) kaynaklanan belirsizlik değerlendirilir. Olasılıksal yöntem (Monte Carlo, güven aralığı) kullanıldıysa ayrıntısı verilir. Bilinen diğer hata kaynakları belgelenir. | yok | 93–94 |
| §9.5.4 yorum | YORUM / ÖNERİ | Yayım tarihinde CWE uygulamaları için güvenilir kıyas vakaları bulunmadığından Prestandard, benzetim sonuçlarının referans veriye karşı geçerlenmesini zorunlu tutmaz. Yine de kestirim güvenilirliğini göstermek için temsili görgül ya da yüksek doğruluklu benzetim verisine karşı ek geçerlemenin raporlanması önerilir. | yok | 94 |
| §9.5.5 | ZORUNLU | Benzetimin başlıca performans hedefleri ve kabul ölçütleriyle uyumunu göstermek üzere Tablo 8-1 ile hizalı bir özet tablo eklenir. | yok | 94 |
| §9.5.6 | ZORUNLU | CWE yaklaşımı hakkında bilgi verilir (temel denklemler, türbülans modelleri, ayrıklaştırma teknikleri). Benzetim koşulları Prestandard'da belirtilenlerden farklıysa gerekçe sunulur. Tescilli tasarım uzmanı, kalite denetimi ve ileride başvuru için geliştirilen modellerin ve üretilen verinin sayısal kaydını saklar. Varsa CWE kod doğrulama ve/veya kıyas vakalarıyla karşılaştırma belgeleri rapora eklenir. | yok | 94 |

## Bölüm 10 — Proje hakem incelemesi

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §1.7 | ZORUNLU | MWFRS, C&C ve ek eleman yüklerini belirlemek için CWE kullanılması hakem incelemesi gerektirir; şartlar Bölüm 10'da. | yok | 24 |
| §10.1 (a) | ZORUNLU | Bu Prestandard'ın hükümleri kullanıldığında bağımsız hakem incelemesi yapılır. | yok | 95 |
| §10.1 (b) | ZORUNLU | İnceleme, şu konularda deneyim ve bilgi sahibi uzman bir firma ya da kişi heyetince yapılır: (1) atmosferik sınır tabakası akışı dahil hesaplamalı akış benzetimi; (2) rüzgâr mühendisliği ve küt cisimler çevresinde akış; (3) ilgiliyse esnek yapıların rüzgârda dinamik tepkisi; (4) rüzgâr tehlikesi tanımı (aşılma olasılığına bağlı tasarım hızı ve yönleri); (5) maruziyet belirleme; (6) rüzgâr tüneli modellemesiyle rüzgâr yükü belirleme; (7) benzetim alanının geliştirilmesi ve yürütülmesine ilişkin Prestandard şartları. | 7 yetkinlik alanı | 95 |
| §10.1 yorum | YORUM | Hakem süreci, CWE ile tasarım yükü kestiriminde kalite denetiminin vazgeçilmez bir bileşenidir. | yok | 95 |
| §10.2 (a) | ZORUNLU | Tasarım ekibi hakemi/heyeti seçer ve seçimini genel mutabakat için AHJ'ye bildirir. | yok | 95 |
| §10.2 (b) | ZORUNLU | Hakem projeyle ilgili çıkar çatışması oluşturmaz, proje tasarım ekibinin parçası olmaz; tasarım ekibinden ve benzetimin sponsorundan tümüyle bağımsızdır. | yok | 95 |
| §10.2 (c) | ZORUNLU | Hakem birimi birden çok kişiden oluşuyorsa biri başkanlık eder. Başkan, hakemler arası anlaşmazlıklarda arabuluculuktan, inceleme kaydının tutulmasından ve ekibin resmî görüşlerinin bildirilmesinden sorumludur. | yok | 95 |
| §10.2 yorum | YORUM / ÖNERİ | Hakem ya da heyet bileşimi genellikle mal sahibi ve tasarım ekibince (EOR + benzetim ekibi), AHJ adına yapılıyorsa yapı idaresiyle birlikte belirlenmelidir. Heyet bileşimi için belirli bir öneri yoktur; §10.1 alanlarında uzmanlık bulunmalıdır. Bazı idareler başkanın o yargı bölgesinde lisanslı olmasını isteyebilir; bu Prestandard'ın genel şartı değildir. | yok | 95–96 |
| §10.3 (a) | ZORUNLU | İnceleme kapsamı mal sahibi, tasarım ekibi, hakem ekibi ve uygun olduğu ölçüde AHJ arasında görüşülür. Hakem(ler), sözleşmede yazılı bir iş kapsamı hazırlar. | yok | 96 |
| §10.3-1 | ZORUNLU | Tasarım esasları (basis of design) belgesinin incelenmesi: tam benzetimden önce, ilk adım olarak yapılır; böylece yorumlar son benzetimden önce ele alınır. Belge, en azından, Prestandard'daki unsurların nasıl ele alınacağını özetler. | yok | 96 |
| §10.3-2 | ZORUNLU | Rüzgâr tehlikesi belirlemesinin ve yük ile tepkiyi bulmak için kullanılacak benzetim tekniğinin incelenmesi. | yok | 96 |
| §10.3-3 | ZORUNLU | Benzetim kurulumunun, girdilerin ve alan üretiminin; benzetim başarımının; sonuçların incelenmesi; hesaplanan yük ve tepkilerin onaylı kabul ölçütlerini karşılayıp karşılamadığının belirlenmesi. | yok | 96 |
| §10.3-4 | ZORUNLU | Benzetim sonuçlarının incelenmesi ve belirtilen performans hedefleri ile kabul ölçütleri açısından değerlendirilmesi. | yok | 96 |
| §10.3-5 | ZORUNLU | Yapısal tasarımda kullanılacak kestirilmiş tasarım rüzgâr yüklerinin ve kapsamla ilgili diğer çıktıların değerlendirmesinin incelenmesi. | yok | 96 |
| §10.3-6 | ZORUNLU | Belirlenen performans hedeflerini karşılamak için önemli görülen diğer konular. | yok | 96 |
| §10.3-7 | ZORUNLU | Hakem yorumları: hakem(ler) teknik yorumlarını, olası çözüm yollarını ve ek görüşme gerektiren konuları da belirterek tasarım ekibine iletir. | yok | 96 |
| §10.3 (son) | YORUM (izin) | AHJ ve geliştirme ekibinin diğer üyelerinin takdiriyle kapsam, kritik yapısal olmayan elemanların rüzgâr tasarımı gibi başka konuları içerecek biçimde genişletilebilir. | yok | 96 |
| §10.4 | ZORUNLU | EOR, benzetimi yapan ekip, (uygunsa) AHJ ve hakemler arasında toplantı yapılır: iş kapsamı, iletişim yöntem ve hatları, inceleme aşamalarının sıklığı ve zamanlaması, her aşamada tasarımın beklenen gelişmişlik düzeyi belirlenir. | yok | 96–97 |
| §10.4 yorum | ÖNERİ | Hakem süreci tasarımın olabildiğince erken aşamasında başlatılmalıdır; erken mutabakat yeniden işi önler. Başlangıç toplantısında kapsam, takvim ve özel iletişim/teslim şartları görüşülmelidir. İnceleme ve yanıt süreleri proje tasarım takvimine konmalıdır. | yok (süre verilmemiş) | 97 |
| §10.5 | ZORUNLU | Hakeme, incelemeyi kolaylaştıracak biçimde düzenlenmiş belgeler verilir. Bunlardan biri, içeriği Bölüm 9 şartlarına dayanan Hesaplamalı Rüzgâr Benzetimi Raporu'dur; tasarım esasları ile benzetim parametre ve varsayımlarının erken incelenmesi için aşamalı sunulur. Hakemler, gerektiğinde eylem istekleriyle birlikte, EOR'a, benzetim ekibine ve gerekiyorsa AHJ'ye zamanında yazılı yorum verir. Tasarım ekibi bütün yorumları hakemleri tatmin edecek biçimde çözmekle sorumludur. | yok | 97 |
| §10.5 yorum | ÖNERİ | Her teslimden sonra benzetim ekibinin hakemlerle toplantı yapıp belgeleri tanıtması iyi uygulamadır. Hakemlere yorum kütüğü hazırlamaları için makul süre verilir; tasarım ekibi yazılı yanıt vermelidir, önemli konularda birkaç tur gerekebilir. Yorumların ve çözümlerin tarihleriyle kaydedildiği bir çizelge (çoğunlukla hesap tablosu) tutulması idealdir; toplantı ve telefon görüşmelerinde varılan sonuçlar da buraya yazılmalıdır. | yok | 97 |
| §10.6 | ZORUNLU | İnceleme sonunda ve mal sahibi ya da AHJ'nin istediği diğer zamanlarda hakem ekibi yazılı rapor sunar: inceleme kapsamı, yorum kütüğü ve benzetimin Prestandard'ın performans hedefleri ile kabul ölçütleri şartlarına genel uygunluğu hakkında hakemlerin mesleki görüşü. | 3 içerik kalemi | 97 |
| §10.7 | ZORUNLU (sorumluluk hükmü) | Rüzgâr yükünü ve yapının rüzgâr tepkisini belirleme sorumluluğu yalnız hesaplamalı rüzgâr benzetimini yapan rüzgâr mühendisine aittir. | yok | 98 |
| §10.7 yorum | YORUM / ÖNERİ | Hakem incelemesi benzetim ekibini mesleki sorumluluklarından kurtarmaz ve ekibin olağan kalite güvence önlemlerinin yerini tutmaz. Hakem sürecinde üretilen rapor ve belgeler yapım belgesi değildir; proje çizimlerine eklenmemeli, sözleşme belgelerinin parçası gibi görünecek biçimde çoğaltılmamalıdır. Hakem belgeleri yapı idaresinin proje dosyalarında saklanmalıdır. | yok | 98 |
| §10.8 | ZORUNLU | Sorumlu tasarımcılar ile hakemler arasındaki anlaşmazlık olağan inceleme sürecinde çözülemezse, malzemeyi inceleyip bir yol önerecek başka uzmanlar tutulur. Bu ek uzmanlar ilk hakem ekibiyle aynı şartları sağlar. | yok | 98 |
| §10.8 yorum | YORUM | Anlaşmazlıklar rüzgâr iklimi varsayımlarından, benzetimin özelliklerinden, sonuçların niteliğinden ya da Davenport rüzgâr mühendisliği zincirinin uygulanmasındaki diğer yönlerden doğabilir; zincir, benzetimin belirli yönlerini ayırıp ek bilgi istemek için yararlı bir araçtır. | yok | 98 |
| §10.9 | ZORUNLU | Hakem incelemesi tamamlandıktan sonra bina tasarımında esaslı değişiklik olursa EOR, mimari ya da yapısal tasarımdaki değişiklikleri anlatarak AHJ'yi bilgilendirir. AHJ'nin takdiriyle bu değişiklikler hakem ekibinin ek incelemesine ve AHJ onayına tabi olabilir. | yok | 98 |
| §10.9 yorum | YORUM | EOR, rüzgâr yüklerini ya da tepkisini etkileyebileceğinden makul biçimde şüphelenilen değişiklikleri AHJ'ye bildirmekle sorumludur. Esaslı değişiklik örnekleri: mimari biçim ya da kütlelendirme; yanal yük taşıyıcı sistemin boyut ve/veya düzeninde rijitliği ya da kütle dağılımını değiştiren değişiklikler; yapının kendi ya da ek sönümündeki değişiklikler. | yok | 98 |

## Okunamayan / eksik yerler

- Bölüm 9 ve 10'da okunamayan denklem ya da bozuk tablo yok.
- §9.3.3.4 kabul ölçütleri için "Bölüm 8"e gönderme yapar; Bölüm 8 yalnız Tablo 8-1'i içerir (spektrum ölçütleri tabloda Bölüm 5/6 satırlarıdır).
- §9.2.2 "near flow region" ve "far-field region" der; Tablo 8-1 ve §1.8 tanımlarındaki bölge adları "near-wall", "local flow", "approach flow", "background/far flow" biçimindedir. Olduğu gibi aktarıldı.
- Ek (appendix): metinde bulunamadı; Bölüm 10'dan sonra Kaynaklar (PDF s. 99) ve Dizin gelir.
- Hakem sayısı, lisans zorunluluğu, inceleme süreleri için sayısal şart: metinde bulunamadı.

## Sayım

Bölüm 9: içerik taşıyan 38 numaralı alt bölüm (§9.1 – §9.5.6), giriş ve yorumlarla birlikte tabloda 45 satır. Bölüm 10: 9 alt bölüm (§10.1–§10.9), §10.3 altında 7 kapsam kalemi.
PO/AC numaralı madde: yok.
