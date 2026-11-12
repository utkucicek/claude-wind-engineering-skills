---
name: hesap-araclari
description: Rüzgâr benzetimi denetim hesapları için hazır betik; hedef profil (log law, I_u), tıkanma oranı (blockage), kesme frekansı (cutoff frequency), boş alan (empty domain) ±%10 denetimi ve kısa kayıttan tepe değer (Gumbel peak) hesabı gerektiğinde kullanılır.
---

# Hesap araçları

Tek dosya: `ruzgar_arac.py` (Python 3, yalnız `numpy` ister). Beş alt komutu vardır; hepsi yalnız okur ve ekrana tablo basar.

## Ne zaman kullanılır

- Hesap alanının boyutunu seçerken ya da denetlerken (tıkanma).
- Boş alan koşusu bittiğinde, ölçülen profil hedefle karşılaştırılırken.
- Ağın yeterince ince olup olmadığına spektrumdan karar verirken (kesme frekansı).
- Kısa bir basınç kaydından tasarım süresindeki tepe değeri kestirirken.

## Komutlar

| Komut | Ne yapar | Ölçütün kaynağı |
|---|---|---|
| `profil --z0 --zref --uref --z ...` | Logaritmik yasayla hedef U(z) ve I_u(z) tablosu | Hedef tanımı projeye aittir; bkz. `hedef-ruzgar-tanimi` |
| `tikanma --by --h --ly --lz` | Alan oranı ≤ %3, enine ve düşey oran ≤ %17 | CWE ön standardı AC 6-8b |
| `kesme --fc --lb --u` | n·L_b/U ≥ 2 (kaplama), ≥ 1 (taşıyıcı sistem) | AC 5-2, AC 5-10 |
| `bosalan olcum.csv --z0 --zref --uref --hmax` | h_max'ın üst %75'inde U ve I_u ortalama bağıl farkı < %10 | AC 5-9 |
| `tepe seri.csv --dt --parca --hedef` | Parça uç değerlerine Gumbel, hedef süreye uzatma | Yöntem seçimi için bkz. `tasarim-ruzgar-yukleri` |

Örnek:

```bash
python ruzgar_arac.py tikanma --by 54 --h 157.6 --ly 2000 --lz 940
```

## Girdi biçimleri

- `bosalan`: başlıklı CSV, sütunlar `z,U,Iu` (m, m/s, oran). Değerler gelen konumdaki (incident location) düşey çizgiden ya da o konumdaki kutu ortalamasından alınır.
- `tepe`: tek sütunlu CSV (Cp ya da basınç), sabit zaman adımı `--dt` (s).

## Sınırlar

- Hedef profil yalnız logaritmik yasa ve I_u = 1 / ln(z / z0) ile kurulur. Proje ASCE 7, EN 1991-1-4 ya da ESDU profili tanımlıyorsa hedef sütununu o kaynaktan hesaplayıp karşılaştırmayı elle yapın.
- `bosalan` sapmayı 0,25·h_max – h_max aralığındaki ölçüm yüksekliklerinin mutlak bağıl farklarının ortalaması olarak hesaplar. Belgedeki Denklem 5-1 ve 5-2 yükseklik boyunca integraldir; denklemin alt sınırı ve mutlak değer işareti PDF'ten okunamadı, asıl belgeden doğrulayın. Ölçüm yükseklikleri eşit aralıklı değilse sonucu elle denetleyin.
- `bosalan` ölçütü ortalama sapma üzerinedir; betik tek yükseklikteki en büyük sapmayı da basar. Bunu raporda ayrıca yazın.
- `tepe` komutunda hedef süre / parça süresi oranı büyüdükçe belirsizlik artar; oran çıktıda yazılır.

## İlgili beceriler

- `bos-alan-dogrulamasi`, `hesap-alani-ve-ag`, `tasarim-ruzgar-yukleri`
