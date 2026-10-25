# Dekoratör sırası

fib(20) için ölçülen çağrı sayıları:

```
Yalnızca @say             : 21891
@say üstte, @lru_cache altta: 39
@lru_cache üstte, @say altta: 21
```

Dekoratörler alttan yukarı uygulanır. En üstteki dekoratörün döndürdüğü nesne fonksiyonun adına atanır, yani fib(k-1) ve fib(k-2) çağrıları önce o nesneye gider.

**Yalnızca @say (21891).** Önbellek yok, bu yüzden fib(20) için ağaçtaki her düğüm tek tek hesaplanıyor. Her çağrı say üzerinden geçtiği için hepsi sayılıyor. Çağrı sayısı 2*fib(21)-1 = 21891.

**@say üstte, @lru_cache altta (39).** Özyinelemedeki fib çağrıları say'a gidiyor, yani her çağrı sayılıyor. Ama say'ın içindeki fonksiyon lru_cache'li. Her n değeri için gerçek hesap bir kez yapılıyor, bu hesap iki çağrı daha üretiyor (fib(n-1) ve fib(n-2)). Önbellekten gelen çağrılar da say'dan geçtiği için sayılıyor. Toplam: 1 (ilk çağrı) + 19 tane iki çağrı (n=20..2 arası hesaplanırken) = 1 + 2*19 = 39.

**@lru_cache üstte, @say altta (21).** Çağrılar önce lru_cache'e gidiyor. Değer önbellekteyse say'a hiç ulaşmıyor. say sadece önbelleğin kaçırdığı yani gerçekten hesaplanan çağrıları sayıyor. fib(0)'dan fib(20)'ye 21 farklı değer var, her biri bir kez hesaplanıyor, 21. Bu durumda dışarıdaki nesne lru_cache sarmalayıcısı olduğu için sayaç `fib.__wrapped__.cagri` ile okunuyor.

Sonuç: aynı iki dekoratör ters sırada kullanılınca farklı şeyi ölçüyor. Üstteki say "fonksiyona kaç istek geldi" sayısını, alttaki say "fonksiyon gövdesi kaç kez çalıştı" sayısını veriyor.
