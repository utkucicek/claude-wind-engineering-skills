# claude-wind-engineering-skills

Rüzgâr mühendisliği için Claude becerileri: binalara gelen rüzgâr yükünün CFD (LES) ile hesabı ve rüzgâr tüneli deneyleriyle karşılaştırılması.

## Kaynaklar

| Kısaltma | Belge | Becerilerdeki kapsam |
|---|---|---|
| CWE | ASCE, *Prestandard for Use of Computational Wind Engineering in Building Design* | Bölüm 1–10'un tamamı |
| ASCE 49 | ASCE/SEI 49-21, *Wind Tunnel Testing for Buildings and Other Structures* | Bölüm 1–8 ve yorum (C1–C8) |

Beceriler bu belgelerin özetidir; metin kopyalanmamıştır ve belgelerin yerini tutmaz. Her ölçüt madde numarası ve PDF sayfa numarasıyla verilir; bağlayıcı bir işte asıl belgeye bakın.

**Uyarı.** Bu depo ASCE ile bağlantılı değildir ve belgelerin metnini içermez. Özetler yapay zekâ yardımıyla hazırlanmıştır ve hata içerebilir; tasarım kararı için belgelerin aslı esas alınmalıdır. Depodaki özetler ve betik MIT lisansıyla sunulur; ASCE belgelerinin telif hakkı ASCE'ye aittir.

## Yapı

```
skills/
  surec/      CWE'nin kapsamı, iki adımlı süreç, hedef rüzgâr tanımı
  benzetim/   boş alan doğrulaması, hesap alanı, ağ, sınır koşulları
  yukler/     basınç katsayıları, tepe değerler, tasarım yükleri
  kalite/     kalite güvencesi, rapor içeriği, hakem incelemesi
  tunel/      ASCE 49: yaklaşan akış, model ve çevre, ölçüm ve yükler
  yardimci/   hesap betiği (tıkanma, kesme frekansı, boş alan denetimi, tepe)
  deneyim/    bir projede yaşanmış hatalar (standart özeti değildir)
```

Her beceri klasöründe:

- `SKILL.md`: ne zaman kullanılır, adım adım yol, zorunlu şartlar, denetim listesi, sık yapılan hatalar.
- `referans.md`: madde madde tablo (madde, tür, özet, sayısal ölçüt, PDF sayfası) ve "metinde bulunamayanlar" listesi.

Tür sütunu: **ZORUNLU** (belgede "shall"), **ÖNERİ** ("should"), **YORUM** (commentary).

Beceri listesi için [SKILLS_INVENTORY.md](SKILLS_INVENTORY.md).

## Kurulum

Becerileri Claude Code'da kullanmak için `skills` altındaki beceri klasörlerini kişisel ya da proje beceri klasörüne kopyalayın (kategori klasörleri olmadan, her beceri kendi adıyla):

```
~/.claude/skills/<beceri-adi>/SKILL.md          (bütün projelerde)
<proje>/.claude/skills/<beceri-adi>/SKILL.md    (yalnız o projede)
```

Hesap betiği Python 3 ve `numpy` ister.

## Bilinen eksikler

- **Denklemler.** PDF'ten metin çıkarımında denklemlerin çoğu bozuk çıktı. Yapısı güvenle okunanlar düz metin olarak yazıldı; okunamayanlar `referans.md` dosyalarında "okunamadı" diye işaretli. Katsayı uydurulmadı. Gözle doğrulanması gerekenler: CWE Denklem 3-1, 3-4, 3-8…3-13, 3-16…3-19, 5-1…5-3, 6-3…6-6, 7-1…7-6.
- **Şekiller.** Şekillerin içeriği okunamadı (CWE Şekil 2-1 akış şeması, 4-1 gelen konum çizimi; ASCE 49 Şekil 1-1, C2-1…C2-3, C6-1).
- **Ağ inceltme katsayısı r'nin alt sınırı** (CWE §6.6.4) metinde ideal değerle aynı çıkıyor; bir simge düşmüş olabilir.
- **CWE Tablo 8-1**'in Bölüm 3–5 satırları tablo başlığından aktarıldı; eşikler ilgili bölümün becerisinde.
- Beceriler yazıldıktan sonra birbirine karşı satır satır denetlenmedi; yalnız biçim (ön bilgi, ad, dosya varlığı) ve bir beceri içerik olarak gözden geçirildi.

## Belgelerin açıkça söylemediği iki nokta

- **CWE, gelen konum (incident location):** çevre binalar açıkça modelleniyorsa gelen konum hedef binanın yeri değil, inceleme bölgesinin en rüzgâr üstü binasının yeridir (§1.8, PO 5-3, AC 6-7).
- **ASCE 49, profilin ölçüldüğü yer:** standart, yaklaşan akış profilinin tünelde yatay olarak nerede ve çevre modeli yerindeyken mi ölçüleceğini söylemez. Bu bilgi her tünel raporundan ayrıca alınmalıdır.
