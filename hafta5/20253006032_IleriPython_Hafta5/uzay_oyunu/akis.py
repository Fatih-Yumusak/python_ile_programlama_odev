from __future__ import annotations

import time
from functools import lru_cache
from typing import Generator, Iterator

from uzay_oyunu.dekoratorler import sure_olc


"""Görev 1 - sonsuz fibonacci üreteci"""
def fibonacci() -> Generator[int, None, None]:
    """0'dan başlayarak sonsuz fibonacci sayıları üretir."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


"""Görev 2 - yakıt azalarak 0'a iner, 0'da durur"""
def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her adımda yakıtı tuketim kadar düşürüp kalanı verir, sıfırda biter."""
    while yakit > 0:
        yakit = max(0, yakit - tuketim)
        yield yakit


"""Görev 3 - boru hattı fonksiyonları, hiçbiri dosyayı listeye okumuyor"""
def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyadan satır satır okur, boş ve # ile başlayanları atlar."""
    with open(yol, encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir


def ayristir(satirlar: Iterator[str]) -> Generator[tuple[str, str, int], None, None]:
    """Her satırı (kaynak, hedef, yakit) demetine dönüştürür."""
    for satir in satirlar:
        sol, sag = satir.split("->")
        kaynak = sol.strip()
        parcalar = sag.strip().split()
        hedef = parcalar[0]
        yakit = int(parcalar[1])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(
    kayitlar: Iterator[tuple[str, str, int]], esik: int
) -> Generator[tuple[str, str, int], None, None]:
    """Yakıtı eşikten büyük olan kayıtları geçirir, gerisini eler."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)


"""Görev 4 - lru_cache içeride tanımlanıyor ki baglantilar'ı kapanım üzerinden kullansın"""
def rota_sayaci(baglantilar: dict[str, list[str]]):
    """Verilen bağlantı haritası için önbellekli rota sayma fonksiyonu döndürür."""
    """dict içindeki listeler tuple'a çevrildi, lru_cache hashable parametre ister"""
    _bag = {k: tuple(v) for k, v in baglantilar.items()}

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Gezegenden başlayıp tam adim yolculuk yapan farklı rota sayısını döndürür."""
        if adim == 0:
            return 1
        komsular = _bag.get(gezegen, ())
        return sum(rota_sayisi(komsu, adim - 1) for komsu in komsular)

    return rota_sayisi


@sure_olc
def rota_sayisi_onbelleksiz(baglantilar: dict[str, list[str]], gezegen: str, adim: int) -> int:
    """Önbelleksiz rota sayısı, özyineleme iç fonksiyonda olduğu için süre bir kez yazılır."""
    def ic(g: str, a: int) -> int:
        if a == 0:
            return 1
        return sum(ic(k, a - 1) for k in baglantilar.get(g, []))

    return ic(gezegen, adim)


"""Bonus - meşgul bekleme ile zamanlayıcı üreteci"""
def zamanlayici(aralik: float) -> Generator[float, None, None]:
    """Her aralik saniyede bir başlangıçtan geçen süreyi üretir."""
    """
    perf_counter sürekli sorgulanıyor yani cpu hiç uyumuyor, bu meşgul bekleme
    time.sleep kullansaydık os cpu'yu başka işe verirdi ama burada kasıtlı busy-wait yapıyoruz
    """
    baslangic = time.perf_counter()
    sonraki = baslangic + aralik
    while True:
        simdi = time.perf_counter()
        if simdi >= sonraki:
            sonraki += aralik
            yield simdi - baslangic
