---
name: tunel-yaklasan-akis
description: Rüzgâr tünelinde atmosferik sınır tabaka (atmospheric boundary layer, ABL) benzetiminin ASCE/SEI 49-21'e göre kurulması veya denetlenmesi gerektiğinde kullan; hedef ortalama hız profili (mean velocity profile), türbülans şiddeti (turbulence intensity), integral uzunluk ölçeği (integral length scale), güç spektrumu (power spectral density), pürüzlülük Reynolds sayısı, referans hız/yükseklik (Uref, zref), kısmi ABL ve kısmi türbülans benzetimi (partial turbulence simulation, PTS), topoğrafya modeli (topographic model) konularını kapsar.
---

# Tünelde yaklaşan akış (approach flow) — ASCE/SEI 49-21

Kaynak: ASCE/SEI 49-21 "Wind Tunnel Testing for Buildings and Other Structures" (2021 baskısı; 49-12'nin yerini alır). Standart metni Bölüm 1–8, yorum (commentary) Bölüm C1–C8'dir. Bu beceride "§2.3" standart metnini, "§C2.3" yorumu gösterir. Sayfa numaraları PDF sayfa sırasıdır. Ayrıntılı tablo: `referans.md`.

## Ne zaman kullanılır

- Bir tünel raporundaki sınır tabaka benzetiminin standarda uyup uymadığı sorulduğunda.
- Tünel deneyi tasarlanırken hedef profil, türbülans ve ölçek uyumu seçilirken.
- Tünel deneyini CFD'de yeniden kurmak için giriş (inlet) koşulları rapordan çıkarılırken.
- Alçak bina, büyük ölçekli ürün deneyi (kısmi ABL, PTS) veya karmaşık arazi (topoğrafya modeli) söz konusu olduğunda.

Kapsam dışı (başka beceri): model ölçeği, tıkanma, yakın çevre modeli → `tunel-model-ve-cevre`; basınç ölçümü ve yükler → `tunel-basinc-olcumu-ve-yukler`.

## Adım adım

1. **Akış türünü belirle (§2.1).** Standart yalnız nötr ısıl tabakalaşmalı (neutral thermal stratification) ABL için şart koyar; tünelde bu eş sıcaklıklı akıştır. Uzun açıklıklı köprü tabliyesi kararlılık deneylerinde nötr olmayan akışa izin vardır, gerekçesi raporda tartışılmak koşuluyla. Hortum, aşağı patlama (downburst) gibi sinoptik olmayan rüzgârlar için zorunlu şart yoktur; yalnız yorumda bir çerçeve verilir (§2.3.2, §C2.3.2).
2. **Tam ABL mi, kısmi ABL mi? (§2.3.1.1, §2.3.1.2)** Alçak binalar ve küçük yapılar için sınır tabakanın yalnız alt kısmının (atmosferik yüzey tabakası, atmospheric surface layer, ASL) benzetimine izin vardır. Tam ABL'de zref = zg (gradyan yüksekliği), yalnız ASL modellenirse zref = zs alınır (§C2.2, yorum).
3. **Hedef profili seç (§2.3.1.1 madde 1).** Ortalama hız profili tanınmış yayınlardaki (recognized literature) ABL veya kısmi ABL modelleriyle tutarlı olmalı. Standart belirli bir formülü zorunlu kılmaz. Yorum; logaritmik yasa, kuvvet yasası (power law), Harris–Deaves tam ABL profili ve kasırga için log–kuadratik profili verir, Tablo C2-1'de ASCE 7 arazi sınıflarına göre z0, 1/α, zg, zs, Iu ve xLu değerleri vardır (§C2.3.1.1).
4. **Türbülansı hedefle (§2.3.1.1 madde 2–4).** Üç hız bileşeninin türbülans şiddeti profilleri hedef ortalama hız profiliyle tutarlı olmalı. İntegral uzunluk ölçeği ve hız çalkantılarının güç spektrumu, yapının ortalama çatı yüksekliğinin %60'ı ile %100'ü arasında (veya deney amacına bağlı başka yüksekliklerde) ölçülür; hedef profille (ve uzunluk ölçeği için model ölçeğiyle) tutarlı olmalıdır.
5. **Ölçek uyumunu denetle (§2.2, Denk. 2-1…2-4).** Jensen sayısı Lb/z0 (3 katı içinde), Lb/zref, xLu/Lb (3 katı içinde veya model değeri en az 3) ve bina Reynolds sayısı (en az 11 000). Ayrıntı `tunel-model-ve-cevre` becerisinde.
6. **Pürüzlülük Reynolds sayısını denetle (§2.3.1.1 madde 5, Denk. 2-5).** u*·z0/ν en az 2,5 olmalı. u*, tünel akışı için yorumdaki Denk. C2-1 ile kestirilebilir: u* = Uref·κ / ln(zref/z0), κ = 0,4.
7. **Referans hız ve yüksekliği yerleştir (§2.3.1.1, §3.3).** Uref ve zref, yakın çevre modelinin (proximity model) ve tıkanmanın etkisini en aza indirecek yerde olmalı; seçilen Uref–zref'in hedef sınır tabaka modeliyle ilişkisi raporda açıklanmalı.
8. **Ölçek şartları sağlanamıyorsa PTS (§2.3.1.3).** §2.3.1.1'in akış ölçekleme şartları tutturulamıyorsa kısmi türbülans benzetimine izin vardır: boyutsuz spektrum n·S(n)/U² yalnız yüksek frekanslarda eşlenir (Denk. 2-6); eksik düşük frekanslı türbülansın etkisi yayınlardaki yöntem ve sınırlarla hesaba katılmalıdır.
9. **Karmaşık arazi varsa topoğrafya modeli (§2.5).** Yakın çevre modelinin kapsamını aşan veya §2.3'te tanımlanmayan akışlar doğuran arazide, sahadaki rüzgâr özellikleri topoğrafya modeliyle tünelde belirlenir: sahada ortalama hız ve türbülans profilleri, bütün yön aralığını tanımlamaya yetecek sayıda yön için ölçülür.
10. **Raporla (§1.2).** Ele alınan her rüzgâr yönü için benzetilen ve hedef profiller birlikte verilir (aşağıdaki denetim listesi).

## Profil nerede ve nasıl ölçülür — metnin söylediği ve söylemediği

Bu konu sık sorulur; standardın açıkça söyledikleri ile söylemedikleri ayrı tutulmalıdır.

Metnin söyledikleri:
- İntegral uzunluk ölçeği ve spektrum için ölçüm **yüksekliği** verilir: ortalama çatı yüksekliğinin %60–%100'ü (§2.3.1.1 madde 3–4, s. 20–21).
- Referans hız ve yükseklik, yakın çevre modeli yapılarının ve bunlara bağlı tıkanmanın etkisini en aza indirecek yerde olmalıdır (§2.3.1.1, s. 20; §3.3, s. 22).
- Yorum: referans hız tipik olarak ya (1) yüksek bina uygulamalarında benzetilen sınır tabakanın dışında kabul edilen bir yükseklikte, ya da (2) yapı yüksekliğinde, **döner tablanın rüzgâr üstünde** ölçülür; rüzgâr üstünde Pitot-statik tüp kullanılırsa boyuna basınç gradyanı düzeltmesi çoğu kez gerekir (§C3.3, s. 46).
- Yorum: yakın çevre modeli deney binasıyla birlikte döner tabla üzerinde döner; yakın çevre modeli, referans hızın ölçüldüğü yerdeki akışı etkilememelidir (§C2.4, s. 44).
- Topoğrafya modeli kullanılıyorsa profiller "deney sahasında" (test site) ölçülür (§2.5, s. 21).
- Raporda her rüzgâr yönü için benzetilen ve hedef profiller verilir (§1.2 madde 2, s. 16).

Metnin söylemedikleri (metinde bulunamadı):
- Yaklaşan akış **profilinin** (hız, türbülans, spektrum) tünelde hangi konumda ölçüleceği — döner tabla merkezi mi, yakın çevre modelinin rüzgâr üstü mü — açıkça yazılmamıştır.
- Profil ölçümü sırasında deney modelinin veya çevre binaların yerinde olup olmayacağı açıkça yazılmamıştır.
- Profil için sayısal kabul toleransı (ör. hedef profilden ±% sapma) verilmemiştir; ölçüt "tutarlı olma" (consistent) biçimindedir. Sayısal toleranslar yalnız ölçek uyumu denklemleri (2-1…2-5) içindir.

Bu yüzden bir raporu denetlerken bu bilgiler rapordan okunmalı, standarda atfedilmemelidir.

## Zorunlu şartlar (standart metni, "shall")

| Bölüm | Şart |
|---|---|
| §2.1 | Benzetim nötr tabakalaşmalı ABL içindir; köprü tabliyesi kararlılık deneylerinde nötr olmayan akış, gerekçesi raporda tartışılırsa serbesttir. |
| §2.2 | Model ölçeği yaklaşan akışın uzunluklarıyla uyumlu olmalı: Denk. 2-1 ve 2-3'ün ilk bağıntısı 3 katı içinde; (xLu/Lb)m ≥ 3 ve (Lb·Ub/ν)m ≥ 11 000 alt sınırdır. Tutmuyorsa belirsizlik ve gerekebilecek ek çalışmalar raporda tartışılır. |
| §2.3.1.1 | Uref ve zref yakın çevre modelinin ve tıkanmanın etkisi en az olacak yerde; hedef sınır tabaka modeliyle ilişkisi raporda. |
| §2.3.1.1 | Tropikal siklon rüzgârları ABL gibi benzetilir, Uref Bölüm 6'ya göre belirlenir; su üzerinden yaklaşan kasırga için Arazi Sınıfı C seçilebilir. |
| §2.3.1.1 (1) | Ortalama hız profili tanınmış yayınlardaki ABL / kısmi ABL modelleriyle tutarlı. |
| §2.3.1.1 (2) | Üç bileşenin türbülans şiddeti profilleri hedef hız profiliyle tutarlı. |
| §2.3.1.1 (3) | İntegral uzunluk ölçeği, çatı yüksekliğinin %60–%100'ünde ölçülür; hedef profil ve model ölçeğiyle tutarlı. |
| §2.3.1.1 (4) | Hız çalkantılarının güç spektrumu, aynı yükseklik aralığında ölçülür; hedef profille tutarlı. |
| §2.3.1.1 (5) | u*·z0/ν ≥ 2,5 (Denk. 2-5). |
| §2.3.1.2 | Alçak yapılar için kısmi ABL benzetimi serbesttir. |
| §2.3.1.3 | Ölçekleme şartları sağlanamazsa PTS serbesttir; eksik düşük frekans etkisi yayınlardaki yöntemlerle hesaba katılır. |
| §2.5 | Karmaşık arazide topoğrafya modeli kurulur; sahada ortalama hız ve türbülans profilleri yeterli sayıda yön için ölçülür ve §2.3.1.1 koşulları sağlanır. |
| §1.2 (2) | Rapor, her yön için benzetilen ve hedef ortalama hız profilini, boyuna türbülans şiddeti profilini, türbülans spektrumunu ve boyuna uzunluk ölçeğini içerir. |
| §1.2 | Deney koşulları standarttan sapıyorsa gerekçe raporda verilir. |

## Yorumdan öne çıkanlar (bağlayıcı değil)

- Kuvvetli rüzgâr: 10 m yükseklikte 10 m/s'den büyük hız; bu durumda mekanik türbülans ısıl tabakalaşmayı bozar (§C2.1).
- Tünelde benzetilen sınır tabaka derinliği (zg)m çoğunlukla 0,75–1,50 m; alçak bina çalışmalarında (zs)m 0,5–0,75 m'ye kadar artırılabilir (§C2.2).
- Uygulamada yaygın yol: istenen kuvvet yasası üssü elde edilene dek rüzgâr üstü zemin pürüzlülüğünü ayarlamak (§C2.2). z0 yöne göre değişebilir; her yön için en uygun sınır tabaka kullanılmalıdır (§C2.3.1.1).
- zref seçimi profili değiştirir: aynı Uref = 20 m/s için zref = 10 m yerine 600 m alınırsa 600 m'deki hız yaklaşık 1,7 kat farklı çıkar (§C2.3.1.1).
- Yanal ve düşey türbülans: Iv ≈ 0,8·Iu, Iw ≈ 0,5·Iu (ABL'nin alt kısmı). Uzunluk ölçekleri: yLu ≈ 0,3·xLu, zLu ≈ 0,5·xLu.
- xLu kestirimi yönteme duyarlıdır: zamansal korelasyon ile spektrum uydurma arasında yaklaşık %30'a varan fark; z/(2π·fm) bağıntısı 2–3 kat düşük verebilir (§C2.3.1.1).
- PTS için xLu,m/Lb,m alt sınırı araştırma konusudur; 0,7–1,5 aralığında değerler önerilmiştir (§C2.3.1.3).
- Topoğrafya modelleri 1:500–1:5 000 ölçeklerinde saha ölçümleriyle iyi uyuşur; basamak (teras) büyüklüğü dikkatle seçilmelidir: tümüyle pürüzsüz yüzey türbülansı düşük, çok büyük basamak çarpık verir (§C2.5).

## Denetim listesi (tünel raporu okurken; evet/hayır)

1. Rapor hangi baskıya (49-21) uyduğunu söylüyor mu?
2. Akışın nötr tabakalaşmalı ABL olduğu belirtilmiş mi (ya da sapmanın gerekçesi verilmiş mi)?
3. Tam ABL mi kısmi ABL mi benzetildiği yazılmış mı?
4. Hedef ortalama hız profili ve dayandığı yayın/model belirtilmiş mi?
5. Her rüzgâr yönü için benzetilen ve hedef ortalama hız profili birlikte verilmiş mi?
6. Her yön için benzetilen ve hedef boyuna türbülans şiddeti profili verilmiş mi?
7. Benzetilen ve hedef türbülans spektrumu ile boyuna integral uzunluk ölçeği verilmiş mi?
8. Uzunluk ölçeği ve spektrum çatı yüksekliğinin %60–%100'ü arasında (veya gerekçeli başka yükseklikte) ölçülmüş mü?
9. Lb/z0 model–prototip oranı 3 katı içinde mi?
10. xLu/Lb model–prototip oranı 3 katı içinde mi, ya da model değeri en az 3 mü?
11. u*·z0/ν ≥ 2,5 gösterilmiş mi?
12. Uref ve zref'in yeri ve hedef sınır tabaka modeliyle ilişkisi açıklanmış mı?
13. Referans hız ölçüm yeri yakın çevre modelinden etkilenmeyecek biçimde seçilmiş mi?
14. Profilin tünelde nerede ve hangi düzenle (model/çevre var-yok) ölçüldüğü raporda yazıyor mu? (Standart bunu şart koşmaz; CFD için gereklidir.)
15. PTS kullanıldıysa eksik düşük frekanslı türbülansın nasıl telafi edildiği ve dayandığı yayın belirtilmiş mi?
16. Topoğrafya modeli kullanıldıysa ölçeği, sahadaki profiller ve ölçüm yönleri verilmiş mi?
17. Şartlardan sapma varsa gerekçe ve belirsizlik tartışması var mı?

## CFD ile karşılaştırırken dikkat

Tünel deneyini CFD'de yeniden kurmak için rapordan alınması gerekenler:
- **Giriş profilleri:** U(z), Iu(z) (varsa Iv, Iw), xLu ve spektrum; hangi yükseklikte, hangi yön için. Standart yalnız "her yön için benzetilen ve hedef profil" ister; sayısal tablo yoksa laboratuvardan istenmelidir.
- **Profilin ölçüldüğü yer ve düzen:** Standart bunu tanımlamaz. CFD'de profilin giriş sınırında mı yoksa bina konumunda (boş tünel) mı tutturulacağı buna bağlıdır; rapordan veya laboratuvardan öğrenilmelidir.
- **Referans tanımı:** Uref'in ölçüldüğü konum ve yükseklik (sınır tabaka dışı mı, çatı yüksekliğinde döner tabla rüzgâr üstü mü) ve başka yüksekliğe dönüştürme yapıldıysa dönüşüm (§3.3, §C3.3). Katsayılar bu hızla boyutsuzlaştırılır; CFD'de aynı tanım kullanılmazsa Cp doğrudan karşılaştırılamaz.
- **z0 ve u*:** Rapor z0 veriyorsa pürüzlülük Reynolds şartı ve logaritmik profil uyumu denetlenebilir.
- **Kısmi ABL / PTS:** Tünelde eksik bırakılan düşük frekanslı türbülans sonradan çözümlemeyle eklenmişse, CFD sonucu ham tünel verisiyle değil düzeltilmiş veriyle (ya da aynı düzeltme uygulanarak) karşılaştırılmalıdır.
- **Boyuna basınç gradyanı:** Yorum, ABL'de boyuna basınç değişiminin yaklaşık sıfır olduğunu, tünelde tavan ayarıyla denetlendiğini söyler (§C2.3.1.1). CFD hesap alanında da profilin bina konumuna kadar korunup korunmadığı ayrıca denetlenmelidir.
- **Uzunluk ölçeği yöntemi:** xLu'nun korelasyonla mı spektrum uydurmayla mı bulunduğu sorulmalı; yöntem farkı %30'a varabilir.

## İlgili beceriler

- `tunel-model-ve-cevre` — ölçek, tıkanma, yakın çevre modeli, Reynolds sayısı, yön adımı.
- `tunel-basinc-olcumu-ve-yukler` — basınç ölçümü, referans basınç, tepe değer, iklimle birleştirme, rapor.
- `tunel-diger-olcumler` — kuvvet terazisi, aeroelastik model, ürünler, kar, sinoptik olmayan rüzgârlar.
