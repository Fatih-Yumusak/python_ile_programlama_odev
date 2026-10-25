# Hafta 5 - Dekoratörler

İleri Python Programlama dersi 5. hafta lab ödevi. Hafta 4'teki uzay oyunu projesine dekoratörler ve dekoratörlerle çalışan bir komut sistemi eklendi.

## Testleri çalıştırmak

```
uv run pytest
```

## Dosyalar

- `uzay_oyunu/dekoratorler.py`: sure_olc, say, log_cagri, sinirla, hafiza
- `uzay_oyunu/komutlar.py`: KOMUTLAR sözlüğü, komut dekoratörü, yardim / envanter / harita
- `uzay_oyunu/fib_sira.py`: Fibonacci için üç dekoratör sırasının çağrı sayıları
- `dekorator_sirasi.md`: sıranın neden sonucu değiştirdiği
- `tests/test_dekoratorler.py`, `tests/test_komutlar.py`

## Görev 1 - sure_olc

perf_counter ile süreyi ölçüp "ad: 0.0123 sn" biçiminde yazdırıyor, sonucu aynen döndürüyor. Hafta 4'teki önbelleksiz rota sayacı `akis.rota_sayisi_onbelleksiz` olarak eklendi ve dekoratör uygulandı. Özyineleme iç fonksiyonda, böylece süre her çağrıda değil bir kez yazılıyor. adim=20 için yaklaşık 0.9 sn sürdü.

## Görev 2 - say ve sıra

Sonuçlar 21891, 39 ve 21. Açıklama `dekorator_sirasi.md` içinde.

## Görev 3 - log_cagri

galaksi_kur ve hedef_menusu fonksiyonlarına uygulandı. Eski testler geçiyor.

## Görev 4 - komut sistemi

komut(ad, aciklama) fonksiyonu değiştirmeden (fonksiyon, aciklama) olarak kaydediyor, aynı ad ikinci kez kullanılırsa tanım anında ValueError veriyor. travel() içinde girdi komut adıysa komut çalışıp menü tekrar gösteriliyor, değilse eskisi gibi gezegen seçimi. travel() Hafta 4'teki yakıt göstergesini kullanmaya devam ediyor, yakıt bitince False döner.

## Görev 5 - sinirla

yakit_harca fonksiyonuna `@sinirla(0, 100)` uygulandı. Sınır değerleri (0 ve 100) ve aralık dışı değerler ayrı ayrı test edildi.

## Bonus - hafiza

lru_cache kullanmadan closure içindeki sözlükle çalışıyor. maxsize dolunca ilk eklenen girdi siliniyor. Sonuçlar ve çağrı sayısı lru_cache ile karşılaştırıldı.
