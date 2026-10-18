from __future__ import annotations

from uzay_oyunu.galaksi import galaksi, komsular
from uzay_oyunu.akis import yakit_gostergesi


def yolculuk(kaynak: str, hedef: str, hiz: int = 1) -> str:
    '''Kaynaktan hedefe yolculuk yapar, bağlantı yoksa hata mesajı döner.'''
    baglanti = komsular(kaynak)
    if hedef not in baglanti:
        return f"{kaynak} → {hedef} rotası mevcut değil!"
    return f"Hız {hiz} ile {kaynak} → {hedef} yolculuğu tamamlandı."


def travel(kaynak: str, hedef: str, _gosterge: list) -> str:
    '''Yakıt göstergesinden bir değer çekerek yolculuğu gerçekleştirir.
    Yakıt biterse oyun biter.'''
    try:
        kalan = next(_gosterge[0])
        return f"{kaynak} → {hedef} yolculuğu tamamlandı. Kalan yakıt: {kalan}"
    except StopIteration:
        return "Yakıtın bitti, uzayda sürükleniyorsun…"


def oyunu_baslat() -> None:
    '''Oyunu başlatır, seyir rotasını takip eder.'''
    print("=== Uzay Oyunu Başladı ===")
    gosterge = [yakit_gostergesi(galaksi["yakit"], 5)]
    rotalar = [
        ("dünya", "sirius"),
        ("sirius", "orion"),
        ("orion", "centauri"),
        ("centauri", "orion"),
        ("orion", "sirius"),
        ("sirius", "kara_delik"),
    ]
    for kaynak, hedef in rotalar:
        print(travel(kaynak, hedef, gosterge))
