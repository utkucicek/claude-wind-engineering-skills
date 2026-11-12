---
name: cwe-kapsam-ve-surec
description: "ASCE hesaplamalı rüzgâr mühendisliği ön standardının (Prestandard for Use of Computational Wind Engineering in Building Design, CWE) kapsamı, dışladıkları, izin verilen araçlar (LES, wall-modeled LES, hybrid RANS/LES; RANS, LBM, immersed boundary durumu), doğrulama-geçerleme (verification and validation), iki adımlı süreç (approach flow + building aerodynamics), gelen konum (incident location) ve temel tanımlar sorulduğunda ya da bir CFD rüzgâr yükü çalışmasının bu belgeye uyup uymadığı baştan denetlenecekse kullanılır."
---

# CWE ön standardı: kapsam ve süreç (Bölüm 1, 2 ve 4)

Kaynak: ASCE "Prestandard for Use of Computational Wind Engineering in Building Design", Bölüm 1 (Genel), Bölüm 2 (Süreç), Bölüm 4 (Genel benzetim şartları). Ayrıntılı madde tablosu: `referans.md`. Sayfa numaraları PDF sayfa sırasıdır (basılı sayfa = PDF sayfası − 18).

## Ne zaman kullanılır

- Bir rüzgâr yükü CFD çalışmasına başlamadan önce "bu iş belgenin kapsamında mı, hangi çözücü/yöntem kabul ediliyor?" sorusu yanıtlanacaksa.
- Mevcut bir çalışmanın (ör. RANS, LBM, gömülü sınır yöntemi, yapay zekâ vekil modeli) tasarım rüzgâr yükü için ön standarda uyup uymadığı sorulduğunda.
- "Gelen konum (incident location)", "yaklaşım akışı bölgesi (approach flow region)", "çalışma bölgesi (study region)", "yakınlık yarıçapı (radius of proximity)" gibi terimlerin anlamı gerektiğinde.
- İki adımlı sürecin (boş alan + binalı alan) nasıl kurulacağı ve iki adım arasında neyin değişebileceği sorulduğunda.
- Ayrıklaştırma mertebesi, zaman adımı/CFL, alt ızgara modeli, zaman adımı içi yakınsama ve ölçekleme/Reynolds sayısı şartları denetlenecekse.

Kullanma: hedef rüzgâr profili ve iklim modeli için `hedef-ruzgar-tanimi`; yaklaşım akışı benzetiminin ayrıntılı ölçütleri (Bölüm 5) ve bina aerodinamiği benzetimi (Bölüm 6) bu becerinin dışında.

## Belgenin amacı ve yapısı

- Amaç: rüzgâr tüneli deneylerindeki standartlaşmanın bir benzerini hesaplamalı yönteme getirmek; ana rüzgâr taşıyıcı sistem (main wind force resisting system, MWFRS), bileşen ve kaplama (components and cladding, C&C) ve eklentiler (appurtenances) için tasarımda kullanılabilir yük tahminine giden yolu başarım hedefleri ve kabul ölçütleriyle tanımlamak (§1.1).
- Belge bir "nasıl yapılır" kılavuzu değildir; kullanıcının rüzgâr mühendisliği ve türbülans altyapısı olması şarttır (§1.2).
- İki tür madde vardır: başarım hedefi (Performance Objective, PO x-y) ve kabul ölçütü (Acceptance Criterion, AC x-y). PO iyi uygulamayı tarif eder ve sonuç sağlandıkça yöntemde serbestlik tanır; AC geçti/kaldı ölçütüdür. Her PO'nun bir AC'si olmayabilir; bir PO'ya birden çok AC bağlıysa harfle ayrılır (a, b, c) (§1.2).
- Yapı Davenport rüzgâr yükleme zincirini izler: rüzgâr iklimi → arazi etkisi → aerodinamik etki → dinamik etki → ölçütler. CWE çalışması zincirin her halkasını ele almalıdır (§1.4, yorum).
- Bölüm 1 ve 2'de numaralı PO/AC yoktur; zorunluluklar düz "shall" cümleleridir. Bölüm 4'te PO 4-1 … 4-7 ve bunlara bağlı AC'ler bulunur.

## Adım adım

1. **Kapsam denetimi (§2.1, §1.5).** İş bina/eklenti rüzgâr yükü mü (MWFRS, C&C, eklenti)? Aşağıdaki dışlananlardan birine giriyor mu?
   - Hareketli ağlı aeroelastik benzetim: kapsam dışı. Belge rijit bina modeli içindir; rezonans gibi sınırlı aeroelastik davranış aerodinamik verinin son işlemesiyle çıkarılır (§1.5.4).
   - İklim değişikliğine bağlı gelecek koşullar: yöntem verilmez (§1.5.2).
   - Yapay zekâ ile yük tahmini: belgenin odağı dışında; değerlendirme Bölüm 4'teki araçlarla yapılır (§1.5.5).
   - Veri tabanı destekli / veri etkin tasarım (database-assisted design, DAD; data-enabled design, DED): odak dışı (§1.5.6).
   - Rüzgârla sürüklenen yağmur, kar, dolu: ele alınmaz (§1.1 yorum).
   - Sinoptik olmayan rüzgârlar (hortum, gök gürültülü fırtına): Bölüm 4–6 yorumlarında yaklaşım var; Bölüm 7 ve sonrasında (olaydan karakteristik yüke geçiş) yöntem yok (§1.5.1 yorum).
   - Diğer yapılar ve ürünler (iletim kulesi, silo, güneş paneli dizisi): aynı yaklaşım geçerli sayılır; Bölüm 3–6'nın PO/AC'leri uygulanmaya devam eder (§1.5.3).
2. **Yetkinlik ve uzman görüşü (§1.2, §1.4).** Kullanıcının kuramsal altyapısı var mı? Belge, yetkin rüzgâr mühendisliği danışmanlığı alınmadan kullanılmamalıdır.
3. **Araç seçimi (§1.3, §4.2.1; PO 4-2, AC 4-2).** Tasarım yükü için: gövdeye oturan ağlı (body-fitted mesh) büyük girdap benzetimi (large-eddy simulation, LES). Duvar modelli LES'e (wall-modeled LES) izin vardır; bu, duvar yakınında RANS çözen melez RANS/LES ya da tüm alanda LES denklemlerini çözen biçim olabilir.
4. **Kod doğrulama-geçerleme belgesi (§1.6).** Kod sağlayıcının doğrulama ve geçerleme testlerinin kapsamını ve titizliğini değerlendir; müşteri isterse bu bilgiyi kendi yeterlilik değerlendirmenle birlikte ver.
5. **Hedef rüzgâr koşulları (Bölüm 3).** `hedef-ruzgar-tanimi` becerisiyle yön yön hedefleri çıkar.
6. **Ölçek kararı (§4.2.4; PO 4-7, AC 4-7).** Tam ölçek ya da küçültülmüş ölçek; küçültülmüşse iki adımda aynı ölçek katsayıları ve model Reynolds sayısı ≥ 11 000.
7. **Sayısal ayarlar (§4.2.2–4.2.3; PO 4-3 … 4-6).** En az ikinci mertebe uzay ve zaman ayrıklaştırması; CFL sayısını raporla; alt ızgara modeli fiziksel olarak tutarlı; zaman adımı içinde yakınsama ölçütü.
8. **Adım 1 – yaklaşım akışı benzetimi (§4.1; PO 4-1, AC 4-1).** Yapısız (boş) alanda, gelen konumda hedef rüzgâr koşullarının sağlandığını göster. Ayrıntı: Bölüm 5.
9. **Adım 2 – bina aerodinamiği benzetimi (§4.1).** Sahaya özgü bina modelini ekle. Adım 1'e göre yalnız şunlar değişebilir: yapıların eklenmesi, sınır koşulu etkisinden kaçınmak için gerekirse alanın enine ve/veya akış yönünde uzatılması, yapı çevresinde yerel ağ sıklaştırması. Ayrıntı: Bölüm 6.
10. **Akran denetimi (§1.7).** MWFRS, C&C ve eklenti yükleri için CWE kullanımı akran denetimi (peer review) gerektirir; şartlar Bölüm 10'da.

## Akış şeması (§2.3, Şekil 2-1)

Belge, bölümler arasında yol göstermek için bir akış şeması (Şekil 2-1, PDF s. 30) verir. Şeklin içeriği kaynak düz metinde yoktur (yalnız başlığı var); kutuları uydurma. Metinden doğrulanabilen sıra, belgenin kendi yapısıdır: rüzgâr iklimi ve hedef akış koşulları (Bölüm 3) → genel benzetim şartları ve iki adımlı süreç (Bölüm 4) → yaklaşım akışı benzetimi (Bölüm 5) → bina aerodinamiği benzetimi (Bölüm 6) → genel rüzgâr etkilerinin belirlenmesi, kalite güvencesi, raporlama, akran denetimi (Bölüm 10) (§1.4, §4.1, §1.7).

## Hangi araç, hangi amaç

| Araç / yöntem | Tasarım rüzgâr yükü için durumu | Dayanak |
|---|---|---|
| Sonlu hacim, gövdeye oturan ağlı LES | Zorunlu yöntem | AC 4-2, §1.3 |
| Duvar modelli LES (melez RANS/LES dahil) | İzinli | §4.2.1, §1.1 |
| Türbülans çözmeyen (durağan) yaklaşımlar | Yük için kabul edilmez (yük tahmini türbülans çözen LES ister); yaya konforu ve hava kalitesi için başka kılavuzlarda yerleşik ve çoğunlukla yeterli | §1.1 ve yorumu |
| Gömülü sınır yöntemi (immersed boundary method) | Belgede ele alınmaz; tepe yük için farklı geometri ve çözücülerde geçerlenmemiş | §1.3, §4.2.1 yorum |
| Kafes Boltzmann yöntemi (lattice Boltzmann method, LBM) | Belgede ele alınmaz; aynı gerekçe | §1.3, §4.2.1 yorum |
| Yapay zekâ / vekil model | Odak dışı; yorumda benzetimin yerine değil, tamamlayıcı (yönler arası ara değer, parametrik vekil model, son işleme) olarak görülür | §1.5.5 |
| DAD / DED | Odak dışı; standart tasarımlarda yararlı olabilir | §1.5.6 |

Not: yaya güvenliği ya da hava kalitesinde tekil hamle koşullarını açıkça görmek gerekiyorsa buradaki PO/AC'ler öneri niteliğinde geçerliliğini korur (§4.2.1 yorum).

## Doğrulama ve geçerleme (§1.6)

- **Kod doğrulaması (code verification):** matematik modelin koda doğru işlendiğinin gösterilmesi; kod geliştiricinin işi.
- **Çözüm doğrulaması (solution verification):** belirli bir sayısal çözümün, hesaplama modelinin kesin çözüm tahminine göre doğruluğu; kullanıcının işi (uzay-zaman ayrıklaştırması, yineleme, makine hassasiyeti kaynaklı hatalar).
- **Geçerleme (validation):** model sonuçlarının, kullanım bağlamı açısından deneysel veriyi ne ölçüde temsil ettiği; uygulamaya özgü olarak genelde kullanıcı yapar; CWE'de çoğunlukla denetimli rüzgâr tüneli verisiyle.
- Doğrulama ölçüm verisiyle karşılaştırma içermez; geçerleme içerir.
- Belge bu sürecin kendisini ve geçerleme için deney veri kümesi tanımını kapsam dışı bırakır.

## Temel tanımlar (§1.8, kendi sözlerimizle)

- **Gelen konum (incident location):** hesaplama alanında bir binanın ya da topoğrafyanın eklendiği, akışa göre en baştaki (en yukarı akıştaki) yer. §4.1 bunu "ikinci adımda bina ya da topoğrafya eklenecek en yukarı akış konumu" diye yineler. Çevre binalar açıkça modelleniyorsa bu, inceleme binasının değil, eklenen ilk cismin konumudur.
- **Yaklaşım akışı bölgesi (approach flow region):** giriş sınırından başlayıp çalışma bölgesini de içine alan ağ bölgesi.
- **Çalışma bölgesi (study region):** inceleme binasını, açıkça modellenen çevresini ve ilgili yakın topoğrafyayı saran sınırlayıcı kutu. Tanım ayrıca çalışma bölgesinin yaklaşım akışı bölgesini içermediğini söyler (iki tanım arasındaki bu gerilim için `referans.md` notuna bak).
- **İnceleme binası (study building):** rüzgâr etkisi incelenen asıl yapı; çevre binalar ve arazi dahil değil.
- **Yakınlık yarıçapı (radius of proximity):** merkezi inceleme binası olan, dışındaki geometri ayrıntılarının çalışma bölgesi aerodinamiğine doğrudan girişim etkisi yapmadığı dairenin yarıçapı. (Belge 1.8'de "proximity model" diye ayrı bir tanım vermez; yalnız tıkanma oranı tanımında "proximate model(s)" geçer.)
- **Yerel akış bölgesi (local flow region):** inceleme binası ve hemen çevresini saran; çarpma, ayrılmış kayma tabakaları, ayrılma kabarcıkları ve iz gibi yükü belirleyen olayların yakalandığı ağ bölgesi.
- **Duvar yakını ağı (near-wall mesh):** katı sınırlara bitişik, duvar etkili türbülansın çözüldüğü ya da modellendiği bölge.
- **Arka plan bölgesi (background region):** diğer üç bölgenin kapsamadığı alan.
- **Ağ bölgesi (meshing region):** dört türü vardır: yaklaşım akışı, yerel akış, duvar yakını, arka plan.
- **Hesaplama alanı (computational domain, CD):** yapı çevresindeki hava akışının benzetildiği sanal hacim.
- **Giriş sınırı (inlet boundary):** rüzgârın alana girdiği yukarı akış kenarı.
- **Tıkanma oranı (blockage ratio):** model ve yakın modellerin akış eksenine dik izdüşüm alanının kesit alanına oranı (tanım metni kaynakta bozuk görünüyor; `referans.md`).
- **Aerodinamik pürüzlülük uzunluğu (aerodynamic roughness length, z0):** tipik engel boyuyla ilişkili, hızın yükseklikle dağılımını belirleyen yüzey pürüzlülüğü ölçüsü.
- **Atmosferik sınır tabaka (atmospheric boundary layer, ABL):** kuvvetli rüzgârda tipik 1000–4000 m derinlikte, hızın yükseklikle arttığı türbülanslı alt atmosfer. **Atmosferik yüzey tabakası (atmospheric surface layer):** düz, düzgün pürüzlü arazide profilin logaritmik olduğu alt kısım.
- **Tümlev uzunluk ölçeği (integral length scale):** sınır tabakadaki türbülans girdaplarının tipik boyutunu temsil eden uzunluk.
- **Rijit yapı / esnek yapı (rigid / flexible structure):** rüzgâr tepkisinde atalet etkisi önemsiz / önemli olan yapı.
- **MWFRS, C&C, ürün (product), dönüş periyodu (return period, MRI), kum tanesi pürüzlülük yüksekliği (sand-grain roughness height)** ve diğerleri: `referans.md`.
- 1.8'de yer almayan terimler ASCE/SEI 7-22 rüzgâr hükümlerindeki anlamıyla kullanılır.

## Zorunlu şartlar

- §1.2: Kullanıcı gerekli kuramsal rüzgâr mühendisliği ve türbülans bilgisine sahip olmalı.
- §1.4: Belge, yetkin rüzgâr mühendisliği görüşü alınmadan kullanılamaz.
- §1.5.5: Değerlendirme Bölüm 4'teki araçlarla yapılır (yapay zekâ değil).
- §1.6: Analist, kod sağlayıcının belgelediği doğrulama/geçerleme testlerinin kapsam ve titizliğini değerlendirir; müşteri isterse bu bilgi ve analistin yeterlilik değerlendirmesi verilir.
- §1.7: MWFRS, C&C ve eklenti yükleri için akran denetimi gerekir (Bölüm 10).
- §2.1: Tasarım yükü sayılabilmesi için benzetim yükleri belgenin başarım şartlarını sağlamalı.
- PO 4-1 / AC 4-1 (§4.1): Yaklaşım rüzgâr alanının doğru temsil edildiği doğrulanır; iki adımlı süreç zorunlu; Adım 1 yapısız benzetimle gelen konumda hedef koşulları doğrular; Adım 2'de değişiklikler üç kalemle sınırlı.
- PO 4-2 / AC 4-2 (§4.2.1): Önemli türbülans ölçeklerinin zaman-uzay evrimi çözülür; gövdeye oturan ağlı LES kullanılır.
- PO 4-3 / AC 4-3 (§4.2.2): Uzay ayrıklaştırması en az ikinci mertebe.
- PO 4-4 / AC 4-4 (§4.2.2): Zaman ayrıklaştırması en az ikinci mertebe; zaman adımı kararlılığı ve çözülen girdapların zaman evrimini sağlar; CFL sayısı raporlanır.
- PO 4-5 / AC 4-5 (§4.2.2): Alt ızgara ölçeği (subgrid-scale, SGS) modeli fiziksel olarak tutarlı olmalı (belirli bir model dayatılmaz).
- PO 4-6 / AC 4-6a (§4.2.3): Kararlı ve doğru çözüm yöntemi; yinelemeli yöntemde zaman adımı içi yakınsama ölçütü; yinelemesiz yöntemde her adımda kararlılık ve tutarlılık denetimleri.
- PO 4-7 / AC 4-7 (§4.2.4): İki adımda aynı ölçek katsayıları; model Reynolds sayısı (Lb·Ub/ν) ≥ 11 000; sağlanamıyorsa ya da bina yuvarlak/akış çizgili biçimliyse ek benzetimler; eklentilerde küçültülmüş ölçekte Reynolds duyarlılık çalışması.

## Sık yapılan hatalar

- RANS sonucunu tasarım tepe yükü olarak sunmak. Belge yük tahmini için türbülans çözen LES ister.
- LBM ya da gömülü sınır çözücüsüyle yapılan işi "ön standarda uygun" diye nitelemek. Belge bu yöntemleri ele almaz; uygunluk iddiası kurulamaz, yalnız yöntemin kapsam dışı olduğu söylenir.
- Boş alan adımını atlamak ya da hedef profili giriş sınırında denetlemek. Denetim yeri gelen konumdur.
- Çevre binalar varken gelen konumu inceleme binasının yerinde almak. Tanım, eklenen en yukarı akıştaki bina/topoğrafyayı esas alır.
- Adım 1 ile Adım 2 arasında ağ çözünürlüğünü, sayısal şemayı, giriş üretecini ya da ölçeği değiştirmek. İzin verilen değişiklik üç kalemdir.
- Yorumdaki "CFL 1 mertebesinde olmalı" ifadesini zorunlu eşik saymak. Zorunlu olan CFL'nin raporlanmasıdır; yerel olarak 1'in aşılması, Bölüm 5–6 kabul ölçütleri sağlandıkça kabul edilir (yorum).
- Belirli bir alt ızgara modelini "zorunlu" diye yazmak. Belge model belirtmez; ağ bağımlılık çözümlemesine (Bölüm 6) gönderir.
- Doğrulama ile geçerlemeyi karıştırmak; tünel karşılaştırması geçerlemedir, ağ/zaman adımı duyarlılığı çözüm doğrulamasıdır.
- Reynolds ölçütünü tam ölçek değerleriyle hesaplamak. Ölçüt hesaplama modelindeki Lb ve Ub ile değerlendirilir.
- Rijit model sonucundan aeroelastik kararsızlık yorumu yapmak. Kapsam dışı.

## İlgili beceriler

- `hedef-ruzgar-tanimi` — Bölüm 3: rüzgâr iklimi ve hedef rüzgâr akış koşulları.
- Bölüm 5 (yaklaşım akışı benzetimi) ve Bölüm 6 (bina aerodinamiği benzetimi) becerileri — bu depodaki ilgili klasörler.
- Bölüm 10 (akran denetimi) ve raporlama becerileri.
