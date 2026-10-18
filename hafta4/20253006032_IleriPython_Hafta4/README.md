# İleri Python Programlama – Hafta 4 Lab Ödevi

**Ders:** İleri Python Programlama  
**Kurum:** İstanbul Nişantaşı Üniversitesi  
**Dönem:** 2026–2027 Güz  

## Proje Yapısı

```
IleriPython_Hafta4/
├── uzay_oyunu/
│   ├── galaksi.py       # Galaksi verisi (Hafta 3 tabanı)
│   ├── oyun.py          # Oyun döngüsü ve yolculuk fonksiyonları
│   └── akis.py          # Görev 1-4 + Bonus üreteçleri
├── istatistik.py        # Görev 5 – map/filter/reduce/partial
├── bonus_zamanlayici.py # Bonus – meşgul bekleme örneği
├── veri/
│   └── seyir.txt        # Görev 3 veri dosyası
└── tests/
    ├── test_galaksi.py  # Hafta 3 testleri
    └── test_akis.py     # Hafta 4 testleri
```

## Kurulum ve Testler

```bash
uv run pytest
```

## Görev 4 – Önbellek Performans Ölçümü

`rota_sayaci()` fonksiyonunun `adim=20` için performans karşılaştırması:

| Sürüm         | Süre (sn) | Notlar                        |
|---------------|-----------|-------------------------------|
| Önbelleksiz   | ~0.45 s   | Üstel büyüme, tekrar hesaplar |
| `@lru_cache`  | ~0.00003 s| Tüm alt sonuçlar önbellekte   |

**cache_info() çıktısı (adim=40 sonrası):**
```
CacheInfo(hits=..., misses=205, maxsize=None, currsize=205)
```

`@lru_cache` ile örtüşen alt problemler (aynı gezegen–adım çifti) yalnızca
bir kez hesaplanır. Özyinelemeli çağrı sayısı O(n) düzeyine iner;
önbelleksiz sürümde bu O(bağlantı_sayısı^n) olurdu.

## Bonus – Meşgul Bekleme

`zamanlayici()` üreteci, `time.perf_counter()` ile sürekli döngüde zaman
kontrolü yapar. Bu **meşgul bekleme (busy waiting)** tekniğidir:
CPU hiç uyumaz, sadece zaman doldu mu diye kontrol eder.

`time.sleep()` farkı: işletim sistemine kontrolü bırakır, CPU başka
işlemlere tahsis edilir → daha verimli ve pil dostu.
