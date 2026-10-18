from __future__ import annotations

from functools import reduce, partial
from uzay_oyunu.galaksi import galaksi
from uzay_oyunu.oyun import yolculuk


"""Soru A - gezegen adları büyük harf"""
def buyuk_harfli_map() -> list[str]:
    """map ile gezegen adlarını büyük harfe çevirir."""
    return list(map(str.upper, galaksi["gezegenler"]))


def buyuk_harfli_liste() -> list[str]:
    """Liste üreteci ile gezegen adlarını büyük harfe çevirir."""
    return [g.upper() for g in galaksi["gezegenler"]]


"""Soru B - en az 2 bağlantısı olanlar"""
def cok_baglantili_filter() -> list[str]:
    """filter ile en az 2 bağlantısı olan gezegenleri bulur."""
    return list(
        filter(
            lambda g: len(galaksi["baglantilar"].get(g, [])) >= 2,
            galaksi["gezegenler"],
        )
    )


def cok_baglantili_liste() -> list[str]:
    """Liste üreteci ile en az 2 bağlantısı olan gezegenleri bulur."""
    return [
        g for g in galaksi["gezegenler"]
        if len(galaksi["baglantilar"].get(g, [])) >= 2
    ]


"""Soru C - toplam bağlantı sayısı"""
def toplam_baglanti_reduce() -> int:
    """reduce ile tüm bağlantıları toplayarak genel toplamı verir."""
    return reduce(
        lambda toplam, g: toplam + len(galaksi["baglantilar"].get(g, [])),
        galaksi["gezegenler"],
        0,
    )


def toplam_baglanti_sum() -> int:
    """sum ile tüm bağlantıları toplayarak genel toplamı verir."""
    return sum(len(galaksi["baglantilar"].get(g, [])) for g in galaksi["gezegenler"])


"""
liste üreteci ve sum daha okunaklı çünkü ne istediğimiz direkt görünüyor,
map/filter/reduce daha soyut ama fonksiyonel programlamaya alışkınlar için tutarlı
"""
hizli_yolculuk = partial(yolculuk, hiz=3)
