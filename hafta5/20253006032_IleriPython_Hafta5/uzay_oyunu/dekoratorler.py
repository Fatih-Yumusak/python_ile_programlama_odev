from __future__ import annotations

import time
from functools import wraps


def sure_olc(fonksiyon):
    """Fonksiyonun çalışma süresini ölçüp 'ad: 0.0123 sn' biçiminde yazdırır."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = time.perf_counter() - baslangic
        print(f"{fonksiyon.__name__}: {sure:.4f} sn")
        return sonuc
    return sarmalayici


def say(fonksiyon):
    """Çağrı sayısını fonksiyonun cagri niteliğinde tutar."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)
    sarmalayici.cagri = 0
    return sarmalayici


def log_cagri(fonksiyon):
    """Çağrıdan önce ad ve argümanları, sonra dönüş değerini yazdırır."""
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        parcalar = [repr(a) for a in args]
        parcalar += [f"{k}={v!r}" for k, v in kwargs.items()]
        print(f"-> {fonksiyon.__name__}({', '.join(parcalar)})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} = {sonuc!r}")
        return sonuc
    return sarmalayici


def sinirla(alt, ust):
    """İlk argümanın [alt, ust] aralığında olmasını zorunlu kılar."""
    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            ilk = args[0] if args else next(iter(kwargs.values()))
            if not alt <= ilk <= ust:
                raise ValueError(
                    f"{fonksiyon.__name__}: {ilk} değeri {alt}-{ust} aralığında değil"
                )
            return fonksiyon(*args, **kwargs)
        return sarmalayici
    return dekorator


def hafiza(maxsize=None):
    """lru_cache olmadan sözlükle önbellek tutar, dolunca en eski girdiyi siler."""
    def dekorator(fonksiyon):
        onbellek = {}

        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            anahtar = (args, tuple(sorted(kwargs.items())))
            if anahtar in onbellek:
                return onbellek[anahtar]
            sonuc = fonksiyon(*args, **kwargs)
            if maxsize is not None and len(onbellek) >= maxsize:
                del onbellek[next(iter(onbellek))]
            onbellek[anahtar] = sonuc
            return sonuc
        return sarmalayici
    return dekorator
