# Hafta 4 - Üreteçler ve functools

İleri Python Programlama dersi 4. hafta lab ödevi. Hafta 3'teki uzay oyunu projesine üreteçler, boru hattı ve önbellekli rota hesabı eklendi.

## Testleri çalıştırmak

```
uv run pytest
```

## Görev 1 - Fibonacci üreteci

Sonsuz fibonacci üreteci yazıldı. next() ile ilk üç değer, islice ile ilk 12 değer, takewhile ile 100'den küçük değerler alındı. Aynı üreteç nesnesinden ikinci islice çağrısının farklı sonuç döndürdüğü test ile gösterildi.

## Görev 2 - Yakıt göstergesi

yakit_gostergesi üreteci her adımda yakıtı tüketim kadar azaltıp kalanı veriyor, sıfıra inince duruyor. travel() fonksiyonuna bağlandı, yakıt bitince oyuncu "Yakıtın bitti, uzayda sürükleniyorsun..." mesajıyla kaybediyor.

## Görev 3 - Seyir defteri boru hattı

veri/seyir.txt okundu. satirlari_oku, ayristir ve uzun_yolculuklar olmak üzere üç üreçten oluşan bir boru hattı kuruldu. Hiçbiri dosyayı listeye okumuyor, her şey tembel çalışıyor.

## Görev 4 - Önbellekli rota sayacı

rota_sayaci fonksiyonu adim=20 için önbelleksiz çalıştırıldığında yaklaşık 0.45 saniye sürdü. lru_cache eklenince aynı hesap 0.00003 saniyede bitti çünkü daha önce hesaplanan gezegen-adım ikilisi tekrar hesaplanmıyor, önbellekten geliyor.

adim=40 sonrasında cache_info şu çıktıyı verdi:

```
CacheInfo(hits=..., misses=205, maxsize=None, currsize=205)
```

## Görev 5 - map, filter, reduce ve partial

istatistik.py içinde her soru iki farklı şekilde yanıtlandı, biri map/filter/reduce ile diğeri liste üreteci veya sum ile. Liste üreteci ve sum daha okunaklı çünkü ne istediğimiz direkt görünüyor. partial ile yolculuk fonksiyonundan hiz=3 sabit hizli_yolculuk türetildi.

## Bonus - Meşgul bekleme

zamanlayici üreteci içinde perf_counter ile sürekli zaman kontrolü yapılıyor. CPU hiç uyumuyor, sadece zaman doldu mu diye bakıyor. Buna meşgul bekleme deniyor. time.sleep kullansaydık işletim sistemi cpu'yu o süreliğine başka işlere verirdi ama burada kasıtlı olarak busy-wait kullanıldı.
