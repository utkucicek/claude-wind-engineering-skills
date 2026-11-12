# Referans: CWE ön standardı Bölüm 1, 2 ve 4 — madde tablosu

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design". Özetler kendi cümlelerimizle yazılmıştır. "PDF sayfası" PDF sayfa sırasıdır (basılı sayfa = PDF − 18).

Tür: **ZORUNLU** = metinde "shall"; **ÖNERİ** = "should" / "recommended"; **YORUM** = "Commentary" paragrafı; **BİLGİ** = tanım ya da açıklayıcı ana metin (zorunluluk kipi yok).

Bölüm 1 ve 2'de numaralı PO/AC yoktur. Bölüm 4'te 7 PO ve 7 AC vardır (PO 4-1 … 4-7; AC 4-1, 4-2, 4-3, 4-4, 4-5, 4-6a, 4-7).

## Bölüm 1 — Genel

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §1.1 | BİLGİ | Belgenin amacı: hesaplamalı yöntemle bina rüzgâr yükü belirlemenin yaygın kabulü için gereken standartlaşmayı PO ve AC'lerle sağlamak; odak, yükün güvenilir biçimde nicelenmesi. | — | 19 |
| §1.1 | BİLGİ | Yük tahmini türbülans çözen büyük girdap benzetimi (LES) gerektirir; kabul ölçütleri gövdeye oturan ağlı LES için geliştirilmiştir; duvar modelli yaklaşım melez RANS/LES ya da tüm alanda LES olabilir. | — | 19 |
| §1.1 yorum | YORUM | Yaya rüzgâr koşulları ve hava kalitesi için türbülans çözmeyen yerleşik yaklaşımlar vardır ve çoğu durumda durağan çözüm yeterlidir; türbülans çözümlü sonuç istenirse bu belgedeki yaklaşımlar yararlıdır. Rüzgârla sürüklenen yağmur, kar ve dolu ele alınmaz. | — | 19 |
| §1.2 | ZORUNLU | Hesaplamalı rüzgâr aracını kullanan kişi, rüzgâr mühendisliği uygulamalarının kuramını ve türbülansın yük tahminindeki temel önemini bilmelidir. | — | 20 |
| §1.2 | ÖNERİ | Bu altyapı yoksa belge kullanılmadan önce rüzgâr mühendisliği çevresinden uzman görüşü alınması önerilir. | — | 20 |
| §1.2 | BİLGİ | Madde gösterimi: "[Performance Objective x-x]" ve "[Acceptance Criterion x-x]"; ilk sayı bölüm, ikinci sıra numarası. Kural koyucu şartlar da PO adıyla anılır. PO iyi uygulama kılavuzudur, sonuç sağlandıkça yöntemde esneklik tanır; AC geçti/kaldı ölçütüdür. Bir PO'ya birden çok AC bağlıysa harf eklenir; her PO'nun AC'si olmayabilir. | — | 20 |
| §1.3 | BİLGİ | Belge, sonlu hacim yöntemi ve gövdeye oturan ağla uygulanan türbülans çözen benzetimlere (ör. LES) odaklanır. Gömülü sınır ve kafes Boltzmann yöntemleri daha az incelenip geçerlendiği için belgede ele alınmaz. | — | 20 |
| §1.4 | BİLGİ | Belge, bina ve diğer yapılarda rüzgâr yükü tahmini için CWE benzetimlerinin yürütülmesi, yorumlanması ve belgelenmesine ilişkin asgari şartları verir; yapı Davenport yükleme zincirini izler; kalite güvencesi, raporlama ve akran denetimi şartları da tanımlanır. | — | 20 |
| §1.4 | ZORUNLU | Belge, belirli bir uygulamaya uygunluğu konusunda yetkin rüzgâr mühendisliği görüş ve yönlendirmesi alınmadan kullanılamaz. | — | 21 |
| §1.4 yorum | YORUM | Yükleme zinciri beş halkadır: rüzgâr iklimi, arazi etkisi, aerodinamik etki, dinamik etki, ölçütler. CWE değerlendirmesi her halkayı ele almalıdır. Belirsizlik değişim katsayısı (CoV) ile ölçülür; toplam CoV ilk dört halkanın CoV'lerinin kareler toplamının kareköküyle yaklaşık bulunur ve rüzgâr hızı CoV'si dört katsayısıyla ağırlıklandırılır. | Rüzgâr hızı CoV ağırlığı: 4 | 21 |
| §1.5.1 | BİLGİ | Belge hem sinoptik (sınır tabaka profilli) hem sinoptik olmayan rüzgârların benzetim koşullarını kapsar; sinoptik olmayanlar için tam ölçek ölçümü sınırlıdır. | — | 21 |
| §1.5.1 yorum | YORUM | Hortum ve gök gürültülü fırtına profilleri için yaklaşımlar Bölüm 4–6 yorumlarında yer alır; Bölüm 7 ve sonrasında, olay benzetiminden karakteristik yüke geçişte görüş birliği sınırlı olduğu için yaklaşım yoktur. | — | 21–22 |
| §1.5.2 | BİLGİ | İklim değişikliğinin yol açacağı gelecek koşulları belirleme yöntemi belgede yer almaz. | — | 22 |
| §1.5.3 | BİLGİ | Belge bina ve eklentiler içindir; yaklaşımlar ürünler ve diğer yapılar (iletim kulesi, silo, büyük güneş paneli dizisi) için de geçerlidir; Bölüm 3–6'nın PO ve AC'leri uygulanmaya devam eder. | — | 22 |
| §1.5.4 | BİLGİ | Gerçek rüzgâr-yapı etkileşimi ve aeroelastik kararsızlık için gereken hareketli ağlı benzetime PO tanımlanmaz. Belge rijit bina modeli içindir; rezonans gibi sınırlı aeroelastik davranış aerodinamik verinin son işlemesiyle çıkarılır. | — | 22 |
| §1.5.4 yorum | YORUM | Narin ve esnek binalarda etkileşim olasılığı vardır; bu genelde rüzgâr tünelinde aeroelastik modelle, yapının ömründe görebileceği tüm olası hızlarda sınanır. | — | 22 |
| §1.5.5 | ZORUNLU | Benzetimin PO/AC'lere göre değerlendirilmesi Bölüm 4'te ele alınan araçlarla yapılır; yapay zekâ ile yük/tepki tahmini belgenin odağı dışındadır. | — | 22 |
| §1.5.5 yorum | YORUM | Yapay zekâ ağırlıkla benzetimin yerine geçen değil, tamamlayan bir araç olarak görülür: rüzgâr yönleri arasında ara değer bulma, parametrik çalışmaların vekil modeli, son işleme eniyilemesi. | — | 22 |
| §1.5.6 | BİLGİ | DAD/DED, yoğun kent dokusundaki özgün mimarili binalarda sınırlı uygulanabilir, standart tasarımlarda yararlı olabilir; belgenin odağı dışındadır. | — | 23 |
| §1.5.6 yorum | YORUM | DAD, tam ölçek izleme ya da model ölçekli tünel verisinden düzgün biçimli binaların yükünü tahmin eder; DED gerçek zamanlı veri ve çoğunlukla vekil modelleme kullanır. | — | 23 |
| §1.6 | ÖNERİ | Hangi LES kodu kullanılırsa kullanılsın analist, kodun doğrulama ve geçerleme testlerinin ayrıntılı belgesini tanımalıdır. Ticari kodlar genelde en güvenilir ve en iyi belgelenmiş olanlardır; açık kaynak, akademik ve kişisel kodlar daha az güvenilir olabilir (belgenin kendi değerlendirmesi). | — | 23 |
| §1.6 | ZORUNLU | Analist, kod sağlayıcının belgelediği kod doğrulama ve model geçerleme testlerinin koşul aralığını ve titizliğini değerlendirir. | — | 23 |
| §1.6 | ZORUNLU | Müşteri isterse bu test bilgileri, analistin yeterlilik değerlendirmesiyle birlikte sunulur. | — | 23 |
| §1.6 | ÖNERİ | Analist ya da müşteri, testlerin ilgili uygulama için yeterince ilgili olmadığı sonucuna varırsa ek test yapılıp belgelenmelidir. Bu doğrulama-geçerleme süreci belgenin kapsamı dışındadır. | — | 23 |
| §1.6 yorum | YORUM | ASME tanımları benimsenir: kod doğrulaması (modelin koda doğru işlenmesi), çözüm doğrulaması (sayısal çözümün kesin çözüm tahminine göre doğruluğu), geçerleme (sonuçların kullanım bağlamında deneysel veriyi temsil derecesi). Doğrulama ölçümle karşılaştırma içermez. Kod doğrulamasını geliştirici, çözüm doğrulamasını ve uygulamaya özgü geçerlemeyi kullanıcı yapar. CWE'de geçerleme çoğunlukla denetimli tünel deneyleriyle yapılır; temsilî veri kümesi tanımı kapsam dışıdır. | — | 23 |
| §1.7 | ZORUNLU | MWFRS, C&C ve eklenti rüzgâr yüklerinin CWE ile belirlenmesi akran denetimi gerektirir; şartlar Bölüm 10'dadır. (Metin "requires" der, "shall" değil; bağlayıcı bir gereklilik olarak yazılmıştır.) | — | 24 |

### §1.8 Tanımlar (PDF s. 24–26) — tümü BİLGİ

Belgede burada tanımlanmayan terimler ASCE/SEI 7-22 rüzgâr hükümlerindeki anlamıyla kullanılır.

| Terim (İngilizce) | Türkçe karşılık | Kendi cümlemizle tanım | PDF sayfası |
|---|---|---|---|
| Aerodynamic roughness length (z0) | Aerodinamik pürüzlülük uzunluğu | Tipik engel boyutuyla ilişkili yüzey pürüzlülüğü ölçüsü; hızın yükseklikle dağılımını ayarlar. | 24 |
| Aeroelastic feedback | Aeroelastik geri besleme | Cismin rüzgârdaki hareketinin, etkiyen rüzgâr yükünü değiştirmesi. | 24 |
| Aeroelastic model | Aeroelastik model | Tam ölçekli yapının rijitlik, kütle ve sönümünü benzeten model. | 24 |
| Aeroelastic structure | Aeroelastik yapı | Kendi hareketi aerodinamik kuvvetleri etkileyen esnek yapı. | 24 |
| Approach flow region | Yaklaşım akışı bölgesi | Giriş sınırından çalışma bölgesine kadar uzanan ve çalışma bölgesini de içeren ağ bölgesi. | 24 |
| Approved | Onaylı | Yetkili merci tarafından kabul edilebilir bulunan. | 24 |
| Atmospheric boundary layer (ABL) | Atmosferik sınır tabaka | Atmosferin alt kısmı; kuvvetli rüzgârda tipik 3 000–13 000 ft (1 000–4 000 m) derinlikte; hız yükseklikle artar, akış türbülanslıdır. | 24 |
| Atmospheric surface layer | Atmosferik yüzey tabakası | ABL'nin, düz ve düzgün pürüzlü arazide profilin logaritmik olduğu alt bölümü. | 24 |
| Authority Having Jurisdiction (AHJ) | Yetkili merci | Belge hükümlerini uygulama ve yaptırma sorumluluğu olan kurum ya da kişi. | 24 |
| Background region | Arka plan bölgesi | Yaklaşım akışı, yerel akış ve duvar yakını bölgelerinin kapsamadığı alan kısmı. | 24 |
| Blockage ratio | Tıkanma oranı | Model ile yakın model(ler)in akış eksenine dik düzlemdeki izdüşüm alanının kesit alanına oranı. Not: kaynak metin paydada "modelin kesiti" diyor; bu bir yazım tutarsızlığı gibi görünüyor, olduğu gibi aktarıldı. | 24 |
| Code verification | Kod doğrulaması | Kodun matematik modeli doğru uyguladığının belirlenmesi. | 24 |
| Components and cladding (C&C) | Bileşen ve kaplama | Bina kabuğu ya da eklenti/çatı üstü donanım elemanlarından MWFRS sayılmayanlar. | 24 |
| Computational domain (CD) | Hesaplama alanı | Yapı çevresindeki hava akışının benzetildiği sanal hacim. | 24 |
| Cell | Hücre | Alanın bölündüğü denetim hacmi. | 24 |
| Dynamic amplification factor (DAF) | Dinamik büyütme katsayısı | Kip uyarımından doğan atalet yükünü hesaba katmak için statik yük katsayısına uygulanan çarpan; rüzgâr hızına, yapı frekansına ve yapısal + aerodinamik sönüme bağlıdır. | 24 |
| Edge / Face | Kenar / Yüz | Yüzün sınırı / hücrenin sınırı. | 24 |
| Flexible structure | Esnek yapı | Rüzgâr tepkisinde atalet yükü etkisi önemli olan yapı. | 24 |
| Incident location | Gelen konum | Hesaplama alanında bir bina ya da topoğrafyanın eklendiği en yukarı akıştaki yer. (§4.1'de yinelenir: ikinci adımda bina ya da topoğrafya eklenecek en yukarı akış konumu; Şekil 4-1.) | 24 (ve 43) |
| Inlet boundary | Giriş sınırı | Rüzgârın alana girdiği yukarı akış kenarı. | 24 |
| Integral (macro) length scale | Tümlev uzunluk ölçeği | Sınır tabakadaki girdap/hamlelerin tipik boyutunu temsil eden uzunluk. | 25 |
| Lateral / Longitudinal / Vertical turbulence | Yanal / boyuna / düşey türbülans | Hızın ortalama rüzgâra dik yatay / ortalama rüzgâr / düşey doğrultudaki çalkantıları. | 25, 26 |
| Local flow region | Yerel akış bölgesi | İnceleme binasını ve hemen çevresini saran; çarpma, ayrılmış kayma tabakası, ayrılma kabarcığı ve iz gibi yükü etkileyen olayları yakalayan ağ bölgesi. | 25 |
| Longitudinal integral time scale | Boyuna tümlev zaman ölçeği | Rüzgâr doğrultusundaki girdapların ortalama süresi; aynı yükseklikteki tümlev uzunluk ölçeği bölü ortalama hız. | 25 |
| Main wind force resisting system (MWFRS) | Ana rüzgâr taşıyıcı sistem | Yapının tümüne destek ve denge sağlayan eleman topluluğu; genelde birden çok yüzeyden yük alır. | 25 |
| Mesh | Ağ | Alandaki hücrelerin bütünü. | 25 |
| Meshing region | Ağ bölgesi | Belirli akış özelliklerini yakalamak için çözünürlüğü ve yapısı ayarlanan alt alan; dört türü: yaklaşım akışı, yerel akış, duvar yakını, arka plan. | 25 |
| Monte Carlo simulation | Monte Carlo benzetimi | Olay dizilerinin (ör. kasırga hızları), olgunun istatistik özelliklerinden çekilerek üretilmesi. | 25 |
| Near-wall mesh | Duvar yakını ağı | Katı sınırlara (bina, arazi, zemin) bitişik, duvar etkili türbülansın çözüldüğü ya da modellendiği bölge; duvar işlemlerinin (sıklaştırma, duvar fonksiyonu, düşük Reynolds modellemesi) gerektiği kuşak. | 25 |
| Non-boundary layer flows | Sınır tabaka dışı akışlar | Atmosferik sınır tabaka özelliklerine uymayan rüzgârlar. | 25 |
| Partial turbulence simulation | Kısmi türbülans benzetimi | Türbülans spektrumunun tümünü değil, belirli yönlerini benzeten yaklaşım. | 25 |
| Product | Ürün | Binalara eklenebilen bileşenler (ör. çatı güneş panelleri) ya da çok sayıda sahada kullanılan bağımsız yapılar; çoğunlukla seri üretim. | 25 |
| Radius of proximity | Yakınlık yarıçapı | Merkezi inceleme binası olan; dışındaki açık geometri ayrıntılarının çalışma bölgesi aerodinamiğine doğrudan girişim etkisi yapmadığı dairenin yarıçapı. | 25 |
| Recognized literature | Tanınmış yazın | Hakem sürecinden geçmiş yayımlanmış araştırma ve teknik makaleler. | 25 |
| Return period (MRI) | Dönüş periyodu | Aynı türden iki olay arasındaki ortalama yıl sayısı; ortalama yinelenme aralığı. | 25 |
| Reynolds number | Reynolds sayısı | Atalet kuvvetlerinin viskoz kuvvetlere oranı: Ub·Lb/ν. | 25 |
| Rigid structure | Rijit yapı | Rüzgâr tepkisinde atalet yükü etkisi önemsiz olan bina. | 25 |
| Sand-grain roughness height | Kum tanesi pürüzlülük yüksekliği | Hesap modelinde, temsilî tam ölçek yüzeyle aynı akış direncini veren tek sıra sıkı dizilmiş eleman yüksekliği. | 25 |
| Solution verification | Çözüm doğrulaması | Belirli bir sayısal çözümün, modelin kesin çözüm tahminine göre doğruluğunun belirlenmesi. | 25 |
| Study building | İnceleme binası | Rüzgâr etkisi incelenen asıl yapı; çevre binalar ve arazi özellikleri hariç. | 25 |
| Study region | Çalışma bölgesi | İnceleme binasını, açıkça modellenen çevresini ve ilgili yakın topoğrafyayı kapsayan sınırlayıcı kutu; yaklaşım akışı bölgesini içermez. | 25 |
| Synthetic wind records | Yapay rüzgâr kayıtları | Gerçek ölçümlere istatistik olarak benzeyecek biçimde üretilmiş zaman serileri. | 26 |
| Tornado | Hortum | Zeminle temas eden, genelde fırtına bulutu tabanına bağlı dönen hava sütunu. | 26 |
| Tropical cyclone | Tropikal siklon | Tropik okyanuslarda doğan alçak basınç çevresindeki dolaşım; Amerika'da kasırga (sürekli rüzgâr 74 mi/h üstü), Asya-Pasifik'te tayfun. | 26 |
| Turbulence | Türbülans | Hız/basınçtaki rastgele çalkantılar, hamleler. | 26 |
| Up-crossing method | Yukarı geçiş yöntemi | Belirli büyüklükteki olayların ortalama yinelenme hızını hesaplayan istatistik yöntem. | 26 |
| Validation | Geçerleme | Benzetim sonuçlarının modellenen gerçek fiziksel olguyu doğru temsil ettiğinin teyidi. | 26 |
| Vortex shedding | Girdap kopması | Narin yapının iki yanından sırayla girdap kopması. | 26 |
| Wind climate model | Rüzgâr iklimi modeli | Hız ve yön istatistiklerini içeren olasılıksal iklim çalışmasının çıktısı. | 26 |

Tanımlarla ilgili notlar:
- §1.8'de "proximity model" diye bir tanım **yoktur**; yalnız "radius of proximity" tanımlıdır ve tıkanma oranında "proximate model(s)" sözü geçer.
- "Approach flow region" tanımı çalışma bölgesini "dahil" sayarken "study region" tanımı yaklaşım akışı bölgesini "içermez" der. İki tanım birlikte okunduğunda: yaklaşım akışı bölgesi çalışma bölgesini kapsar, tersi geçerli değildir. Metin bunu ayrıca açıklamaz.

### §1.9 Gösterim (PDF s. 26–27) — BİLGİ

| Simge | Anlam |
|---|---|
| B | Karakteristik bina boyutu: en küçük yatay boyut ile ortalama çatı yüksekliğinden küçük olanı |
| By | Açıkça modellenen inceleme ve çevre yapıların (ve topoğrafyanın) akış yönü izdüşümünün en büyük enine genişliği |
| f | Coriolis parametresi |
| h | Ortalama çatı yüksekliği (yapı çevresindeki ortalama zemin kotundan) |
| hav | Açıkça modellenen tüm yapıların ortalama çatı yüksekliklerinin ortalaması |
| hmax | Bina yüksekliği ile çevre binaların ortalama yüksekliğinden büyük olanı |
| hs | İnceleme binası yüksekliği (h) ile çevre binaların ortalama yüksekliğinden büyük olanı (Şekil 6-1) |
| Lb | Yapının karakteristik kesit uzunluk ölçeği |
| lCD,x,u / lCD,x,d | Hesaplama alanının yukarı akış / aşağı akış yönündeki boyu |
| lCD,y / lCD,z | Hesaplama alanının genişliği / yüksekliği |
| Lu^x, Lu^y, Lu^z | Boyuna türbülans bileşeninin x, y, z doğrultularındaki tümlev uzunluk ölçeği |
| Iu, Iv, Iw | Boyuna, yanal, düşey türbülans şiddeti |
| k | Türbülans kinetik enerjisi |
| n, nc | Frekans, kesme frekansı |
| P | Basınç |
| S | Güç spektral yoğunluğu |
| u* | Sürtünme hızı |
| u′ | Anlık türbülans çalkantısı |
| U | Ortalama hız |
| Ub | Bina ya da eklenti için uygun karakteristik hız |
| Uref, Us | zref ve zs yüksekliğindeki ortalama hız |
| u | Anlık hız (U + u′) |
| vR | R dönüş periyodu için tüm yönlü tasarım rüzgâr hızı |
| z, z0 | Zeminden yükseklik, aerodinamik pürüzlülük uzunluğu |
| zg | Gradyan yüksekliği (sınır tabakanın tepesi) |
| zref | Ortalama hızın ölçüldüğü/başvurulduğu yükseklik |
| zs | Yüzey tabakası yüksekliği; sınır tabaka yüksekliğinin yaklaşık %10'u |
| α | Ortalama hızın yükseklikle değişimi için kuvvet yasası üssü |
| κ | von Kármán sabiti |
| ν | Havanın kinematik viskozitesi |
| Alt simgeler | m: model; b: bina; g: gradyan; 0: zemin; p: prototip (tam ölçek); ref: referans; s: yüzey tabakası |

Not: hmax ve hs tanımları metinde neredeyse aynıdır; fark metinden çıkarılamıyor.

## Bölüm 2 — Hesaplamalı rüzgâr mühendisliği süreci

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| §2.1 | BİLGİ | Kapsam: bina ve eklentilerde MWFRS ile tekil yapısal eklenti / C&C rüzgâr yüklerinin CWE ile tahmini için asgari şartlar. | — | 29 |
| §2.1 | ZORUNLU | Benzetimle üretilen yükler, hesaplamalı yaklaşıma izin veren yetki alanlarında tasarım yükü olarak kullanılabilmek için belgenin başarım şartlarını sağlamalıdır. | — | 29 |
| §2.1 yorum | YORUM | CWE bu belgenin ötesinde işler de yapabilir (çok fazlı / çok türlü akış, yalnız ortalama akışın yettiği benzetimler). Belgedeki yaklaşım yaya konforu ve güvenliği için türbülanslı akışın daha güvenilir nicelenmesinde de kullanılabilir. | — | 29 |
| §2.2 | BİLGİ | Eksen takımı: sağ el kuralı; x akış yönü, y yanal, z düşey. U, V, W ortalama hızlar; u′, v′, w′ çalkantı bileşenleri. | — | 29 |
| §2.3 | BİLGİ | Şekil 2-1 belgenin düzenini ve CWE çalışmasında beklenen süreci gösteren akış şemasıdır. Şeklin içeriği düz metin kaynağında yoktur (yalnız başlık). | metinde bulunamadı | 29–30 |

## Bölüm 4 — Genel benzetim şartları

| Madde | Tür | Özet | Sayısal ölçüt | PDF sayfası |
|---|---|---|---|---|
| PO 4-1 (§4.1) | ZORUNLU | Benzetim süreci, hesaplama alanı içinde yaklaşım rüzgâr alanının doğru temsil edildiğini doğrulamalıdır. Doğru alan elde edildikten sonra bina aerodinamiği benzetimine geçilebilir. | — | 43 |
| §4.1 | ZORUNLU | Hesap iki adımlı süreçle yapılır (Şekil 4-1): Adım 1 yaklaşım akışı benzetimi, Adım 2 bina aerodinamiği benzetimi. | 2 adım | 43 |
| AC 4-1 (§4.1, Adım 1) | ZORUNLU | Yapı(lar) olmadan bir benzetim yapılarak modelin, hesaplama alanı içindeki gelen konumda hedef rüzgâr akış koşullarını doğru temsil ettiği doğrulanır. Gelen konum: ikinci adımda bina ya da topoğrafya eklenecek en yukarı akış konumu. | — | 43 |
| §4.1 (Adım 2) | ZORUNLU | Sahaya özgü bina modeli alana eklenir. Adım 1'e göre model seçimlerindeki değişiklikler şunlarla sınırlıdır: (i) yapıların eklenmesi, (ii) sınır koşullarının istenmeyen etkisinden kaçınmak için gerekirse alanın enine ve/veya akış yönünde uzatılması, (iii) yapılar çevresinde yerel ağ sıklaştırması. | — | 43 |
| §4.1 | BİLGİ | Ek şartlar: §4.2 iki adıma da uygulanır; Bölüm 5 Adım 1, Bölüm 6 Adım 2 şartlarını verir. | — | 43 |
| §4.2.1 | BİLGİ | Tepe rüzgâr yüklerinin belirlenmesinde türbülans yapılarının ve bunlara bağlı hız/basınç çalkantılarının çözülmesi önemlidir. | — | 43 |
| PO 4-2 (§4.2.1) | ZORUNLU | Benzetim yöntemi, akıştaki önemli türbülans ölçeklerinin zaman ve uzaydaki evrimini çözmelidir. | — | 44 |
| AC 4-2 (§4.2.1) | ZORUNLU | Gövdeye oturan ağ yaklaşımıyla bir LES yöntemi kullanılır. | — | 44 |
| §4.2.1 | BİLGİ (izin) | Duvar modelli LES kullanılabilir; duvar yakınında RANS çözüp biraz uzakta LES'e bağlanan melez biçim ya da tüm alanda LES denklemlerinin çözüldüğü biçim olabilir. | — | 44 |
| §4.2.1 yorum | YORUM | En yaygın ve kanıtlanmış yol sonlu hacim, gövdeye oturan ağlı LES'tir; duvar modelli LES sonuçları çeşitli bina geometrileri ve farklı kodlarla tünel ve saha deneylerine karşı geçerlenmiştir. Tekil hamle koşullarının açıkça gerektiği durumlarda (bazen yaya güvenliği, hava kalitesi) buradaki PO/AC'ler öneri olarak geçerliliğini korur. Gömülü sınır ve kafes Boltzmann yöntemleri yayım tarihinde farklı geometri ve çözücülerde tepe yük için geçerlenmemiştir; model seçimlerine duyarlılık yeterince bilinmemektedir; gömülü sınırda, sınırın ağla hizalı olmadığı yerlerde yüzey basıncının yeniden kurulması güç olabilir. | — | 44 |
| §4.2.2 | BİLGİ | Ağ çözünürlüğüne ilişkin PO/AC'ler ayrı verilir: yaklaşım akışı için Bölüm 5, bina aerodinamiği için Bölüm 6. | — | 44 |
| PO 4-3 (§4.2.2) | ZORUNLU | Uzay ayrıklaştırması ve gradyan ara değer yöntemleri, sayısal hatayı ve çözülen türbülansın sönümünü azaltacak biçimde seçilir. | — | 45 |
| AC 4-3 (§4.2.2) | ZORUNLU | Uzay ayrıklaştırma şemaları en az ikinci mertebedir. | ≥ 2. mertebe | 45 |
| PO 4-4 (§4.2.2) | ZORUNLU | Zaman ayrıklaştırması sayısal hatayı azaltacak biçimde seçilir. | — | 45 |
| AC 4-4 (§4.2.2) | ZORUNLU | Zaman ayrıklaştırması en az ikinci mertebe doğruluktadır; zaman adımı kararlılığı koruyacak ve uzayda çözülen tüm girdapların zaman evrimini çözecek biçimde seçilir; Courant-Friedrichs-Lewy (CFL) sayısı raporlanır. | ≥ 2. mertebe; CFL raporlanır (zorunlu sayısal eşik yok) | 45 |
| PO 4-5 / AC 4-5 (§4.2.2) | ZORUNLU | Alt ızgara ölçeği (SGS) modeli, çözülmeyen türbülansın çözülen akışa etkisini fiziksel olarak tutarlı biçimde temsil eder. (Metin PO ve AC'yi tek cümlede birlikte verir.) | — | 45 |
| §4.2.2 yorum – uzay | YORUM | Türbülans yapılarının aşırı sönümünü önlemek için şemalar en az ikinci mertebe olmalı; bu gerekli ama yeterli değildir. İkinci mertebe doğruluk genelde yapılı Kartezyen ya da iyi hizalı yapısız ağlarda elde edilir; düzensiz ağ ve yüksek çarpıklık doğruluğu bozar. Birçok çözücü yakınsama için birinci ve ikinci mertebeyi harmanlar; bu nedenle Bölüm 6'daki ağ bağımlılık çözümlemesi gerekir. | — | 45 |
| §4.2.2 yorum – zaman | YORUM | Çözülen girdapların zaman evrimi için CFL sayısı 1 mertebesinde olmalıdır. Örtük yöntemler daha yüksek CFL'de kararlı olabilir. Alanın büyük kısmında fazla yüksek CFL doğruluğu düşürür; yerel olarak 1'in aşılması ise maliyeti düşürürken doğru sonuç verebilir. Bölüm 5 ve 6 kabul ölçütleri sağlandıkça, bazı yerlerde CFL > 1 veren zaman adımı kullanılabilir. Not: kaynak metinde CFL tanımı "U Δx/Δt" biçiminde yazılmış; bu büyük olasılıkla dizgi hatasıdır (kaynakta görülen biçim aktarıldı, düzeltme yapılmadı). | CFL ≈ 1 (öneri, yorum) | 45 |
| §4.2.2 yorum – SGS | YORUM | Sonlu hacimde en yaygın yol doğrusal girdap viskozitesi varsayımlı alt ızgara modelidir. Ağ inceldikçe model seçiminin etkisi azalır; tepe yük ince ağ gerektirdiğinden etki sınırlıdır ve çeşitli modellerle doğru sonuç alınmıştır. Bu yüzden belirli bir alt ızgara modeli şartı konmaz; Bölüm 6'daki ağ bağımlılık çözümlemesi gereken doğruluğu göstermelidir. | — | 45 |
| PO 4-6 (§4.2.3) | ZORUNLU | Ayrıklaştırılmış denklem sistemi kararlı ve doğru bir çözüm yöntemiyle çözülür. | — | 46 |
| AC 4-6a (§4.2.3) | ZORUNLU | Zaman adımı içinde yinelemeli yordam kullanılıyorsa, bir sonraki adıma geçmeden çözümü yakınsatmak için yakınsama ölçütleri uygulanır. Yinelemesiz, doğrudan hesaplanan zaman tümlevi yöntemlerinde yineleme yakınsaması denetimi gerekmez; ancak her adımda sayısal kararlılık ve tutarlılık denetimleri yapılır: ilgili CFL koşulunun uygulanması, fiziksel sınırlılığın doğrulanması, çözümdeki zamansal değişimin izlenmesi. (Kaynakta yalnız "4-6a" görülüyor; "4-6b" metinde bulunamadı.) | Sayısal artık eşiği verilmez | 46 |
| §4.2.3 yorum | YORUM | Basınç-hız bağlaşımı kütle korunumu için esastır; PISO türü düzeltici adımlar ıraksama hatasını azaltır, çok zamana bağlı akışlarda ek düzeltici gerekebilir. Bağlaşım yapay sönüm ya da sahte salınım üretmemelidir; bunlar biçimsel olarak yakınsamış ama fiziksel olarak yanlış çözüm verebilir. Süreklilik artıklarının her adımda küçük kalması önemlidir. | — | 46 |
| §4.2.4 | BİLGİ | Benzetim tam ölçekte ya da küçültülmüş geometri ve/veya hız ölçeğinde yapılabilir. Olası ölçekleme şartları (geometrik, kinematik, dinamik benzerlik) için ASCE/SEI 49-21 §2.2'ye başvurulur. | — | 46 |
| PO 4-7 (§4.2.4) | ZORUNLU | Ölçekleme kullanılıyorsa yaklaşım akışı ve bina aerodinamiği benzetimlerinde aynı ölçek katsayıları kullanılır; böylece iki benzetimdeki uzunlukların uyumunu sağlayan benzerlik ölçütleri karşılanır. | — | 46 |
| AC 4-7 (§4.2.4) | ZORUNLU | Geometri ve hız ölçeği, model Reynolds sayısı ölçütünü sağlayacak biçimde seçilir (Denklem 4-1). Lb binanın ilgili boyutu, Ub çatı yüksekliğindeki rüzgâr hızıdır; değerler hesaplama modelindeki değerlerdir (alt simge m). | (Lb·Ub/ν)m ≥ 11 000 (boyutsuz) | 46 |
| §4.2.4 | ZORUNLU | Ölçüt sağlanamıyorsa ya da bina Reynolds bağımlılığı doğurabilecek yuvarlak/akış çizgili biçimdeyse, hem rüzgâr benzetimleri hem bina aerodinamiği benzetimleri için ek benzetimler (ör. daha yüksek Reynolds sayısında) yapılır. | — | 46 |
| §4.2.4 | ZORUNLU | Eklentilerde küçültülmüş ölçek kullanılıyorsa, sonuçların beklenen yük koşullarını temsil ettiğini ve Reynolds sayısından bağımsız olduğunu gösteren duyarlılık çalışması yapılır; Reynolds sayısı eklentiye ilişkin bir karakteristik uzunlukla (ör. eklentinin temsilî boyutu) tanımlanır. | — | 46 |
| §4.2.4 yorum | YORUM | CWE'nin ilgilendiği yüksek Reynolds sayılarında keskin kenarlı binalarda akış Reynolds sayısından bağımsızdır. Eklentilerde ilgili Reynolds sayısı eklenti yakınındaki yerel hıza dayanır ve etkiler iyi bilinmez. En iyisi tam ölçekli benzetimdir; küçültülmüş ölçekte bağımsızlık doğrulanmalıdır. Tünel yöntemleri bunu büyük model ölçeği ve kısmi türbülans benzetimiyle çözer; aynı yöntemler LES'te de kullanılabilir. | — | 47 |

## Belirsiz / kaynakta eksik noktalar

- Şekil 1-1 (yükleme zinciri), Şekil 2-1 (akış şeması) ve Şekil 4-1 (iki adımlı süreç ve gelen konum) kaynak düz metinde yalnız başlık olarak var; çizim içeriği doğrulanamadı.
- Denklem 4-1 metin çıkarımında bozuk; "Lb Ub / ν, alt simge m, ≥ 11 000" olarak okunuyor ve çevre metinle tutarlı.
- CFL tanımındaki "U Δx/Δt" yazımı (PDF s. 45) kaynakta böyle; dizgi hatası olasılığı yüksek.
- "Blockage ratio" tanımının paydası (PDF s. 24) kaynakta tutarsız yazılmış.
