---
name: les-giris-turbulansi-ayari
description: LES'te yapay giriş türbülansı (synthetic inflow turbulence) boş alanda (empty domain) hedefi tutturmadığında, türbülans binaya gelmeden söndüğünde ya da boş alan koşusu tekrar tekrar ayarlanırken kullanılır; bir projede yaşanmış hatalar ve işe yarayan sıra.
---

# LES giriş türbülansının boş alanda ayarlanması (saha deneyimi)

Bu beceri bir standardın özeti değildir. Tek bir projede (yüksek bina, çevre binalı, LES, yapay giriş türbülansı, GPU çözücü) yaşananların kaydıdır. Sayılar o projeye aittir; yöntemi alın, sayıları kendi koşunuzda ölçün.

## Ne zaman kullanılır

- Boş alan koşusunda gelen konumda türbülans şiddeti hedefin belirgin altında ya da üstünde çıktığında.
- Giriş türbülansı dalga toplamı (sinüs modları) olarak yazıldığında.
- Koşu süresi kısa tutulmak zorunda olduğunda.

## İşe yarayan sıra

1. **Boş alan koşusunu binalı koşuyla aynı kutu, ağ, çözücü ve girişle yapın.** Bina ve çevre yalnız geometriden çıkarılır.
2. **Ölçümü kutu ortalamasıyla alın.** Tek nokta kaydı kısa sürede gürültülüdür; gelen konumda ince bir kutunun (örnek: akış yönünde ±15 m, yanal ±100 m, düşey ±6 m) hücre ortalaması daha kararlıdır.
3. **Kaybı frekans bandına göre ölçün.** Giriş modları kayıt süresine kilitliyse her mod FFT'de tek kutuya düşer; bant başına ölçülen/verilen varyans oranı doğrudan okunur.
4. **Düzeltmeyi banda göre yapın, tek çarpanla değil.** Her bandın genliğini ölçülen kaybın tersiyle çarpın; çarpanı sınırlayın (örnek: 1–2,5).
5. **Düzeltilmiş girişi yine boş alanda doğrulayın.** Binalı koşudan yapılan dolaylı kestirim yanıltır (aşağıya bakın).
6. **Kuralları sonuç görülmeden yazın:** hangi oranda sonuç geçerli, hangi oranda uyarıyla verilir, hangi oranda hükümsüz.

## Yaşanmış hatalar

| Hata | Belirti | Neden | Çare |
|---|---|---|---|
| Mod frekanslarını kısa kayda kilitlemek | Türbülans hedefin 0,37 katı | En düşük frekans 1/T'nin altındaydı; kilit, düşük frekanslı modları sırayla 1/T, 2/T, 3/T… değerlerine itti ve enerji 1–5 s periyoda yığıldı; bu dalgalar yolda söndü | En düşük frekansı 1/T alın, mod sayısını azaltın |
| Tek genel çarpanla düzeltme düşünmek | — | Kayıp banda göre çok farklıydı (oranlar 0,94 / 0,42 / 0,84 / 0,95) | Bant başına çarpan |
| Binalı koşunun yukarı akış istasyonlarından bina yerini kestirmek | Kestirim 1,2–1,3; doğrudan ölçüm 0,95 | Yukarı akıştaki büyütme bina yerine kadar taşınmıyor | Yalnız boş alan ölçümüne güvenin |
| Bekleyici betiğin günlükte eski "bitti" satırını görmesi | İki koşu aynı anda başladı | Arama satır başına ve zamana bağlanmamıştı | Yalnız kendi başlattığınız koşudan sonraki satırları arayın |
| Isınmayı kısa tutmak | İlk 20 s ile kalanın yüz ortalaması Cp farkı 0,06–0,08 | Akış oturmadan örnekleme başladı | Önceden yazılı kural: fark eşiği aşarsa ilk dilim atılır |

## Bilinmesi gerekenler

- **Türbülans akış boyunca değişir.** Aynı koşuda bina yüksekliğinde hedefe oran girişten 60 m'de 2,06, 350–500 m'de yaklaşık 1,2, gelen konumda 1,05 ölçüldü. Rüzgâr tünelinde tabla boyunca böyle bir değişim beklenmez; boş alan raporunda akış yönündeki değişimi de verin.
- **Alt kotlar ayrı davranır.** Üst yarı ±%10 içindeyken bina yüksekliğinin dörtte birinde oran 0,82 kaldı. Ortalama ölçütü geçse bile bunu raporda yazın.
- **Girişte yere yakın ters akış olabilir.** Büyütülmüş girişte yere yakın anlık hız eksiye düştü (5 m'de zamanın %6'sı). Giriş sınırının bunu nasıl ele aldığını denetleyin.
- **Kısa kayıt.** En yavaş dalga kayda bir kez sığıyorsa düşük frekans istatistiği belirsizdir; süre şartı için `bos-alan-dogrulamasi` becerisine bakın.

## Kalıcı çözüm seçenekleri

- Ön benzetim (precursor): türbülans gerçek akış çözümüdür, yolda sönmez; bir kez uzun koşu ve pürüzlülük ayarı ister.
- Daha çok modlu, kütle korunumlu yapay üreteç.
- Çözücünün ön koşu için gereken özellikleri (periyodik sınır, kaydı girişe okutma) desteklediğini önce küçük bir denemeyle doğrulayın.

## İlgili beceriler

- `bos-alan-dogrulamasi`, `hesap-araclari`, `kalite-guvencesi`
