from __future__ import annotations

import json
from pathlib import Path

from uzay_oyunu.galaksi import komsular
from uzay_oyunu.akis import yakit_gostergesi
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler


def yolculuk(kaynak: str, hedef: str, hiz: int = 1) -> str:
    '''Kaynaktan hedefe yolculuk yapar, bağlantı yoksa hata mesajı döner.'''
    baglanti = komsular(kaynak)
    if hedef not in baglanti:
        return f"{kaynak} → {hedef} rotası mevcut değil!"
    return f"Hız {hiz} ile {kaynak} → {hedef} yolculuğu tamamlandı."


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Eldeki eşyaları metin olarak döndürür, hiçbiri yoksa boş döner."""
    esya_listesi = []
    if credits:
        esya_listesi.append("bol kredi")
    if engines:
        esya_listesi.append("güçlü motorlar")
    if copilot:
        esya_listesi.append("yetenekli bir pilot")

    if not esya_listesi:
        return ""
    return "Sende: " + ", ".join(esya_listesi)


def hedef_menusu(hedefler: list[str]) -> str:
    """Numaralı hedef menüsü metnini döndürür."""
    menu = "Nereye gitmek istersin?"
    for i in range(len(hedefler)):
        menu += f"\n[{i + 1}] {hedefler[i]}"
    return menu


def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    """Galaksi sözlüğü oluşturur. Başlangıç gezegeni yoksa ValueError fırlatır."""
    if baslangic not in gezegenler:
        raise ValueError(f"'{baslangic}' gezegeni listede yok")

    yakit = kwargs.get("yakit", 50)  # verilmezse varsayılan 50

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def _galaksiyi_yukle():
    dosya_yolu = Path(__file__).parent / "galaksi.json"
    with open(dosya_yolu, encoding="utf-8") as f:
        veri = json.load(f)
    return galaksi_kur(**veri)


# oyun durumu - global kullanmamak için liste ve sözlük kullandım
galaksi = _galaksiyi_yukle()
envanter = {"credits": True, "engines": False, "copilot": True}
_sayac = hamle_sayaci()
_son_hamle = [0]
# gösterge oyunun başında galaksideki yakıtla kuruluyor, her yolculukta bir değer çekiliyor
_gosterge = yakit_gostergesi(galaksi["yakit"], 5)


def travel() -> bool:
    '''Bir yolculuk yapar. Yakıt biterse False döner, oyun devam ediyorsa True.'''
    env = envanter_metni(
        envanter["credits"],
        envanter["engines"],
        envanter["copilot"]
    )
    if env:
        print(env)

    hedefler = galaksi["baglantilar"][galaksi["konum"]]
    if not hedefler:
        print("Gidecek yer yok!")
        return True

    print(hedef_menusu(hedefler))

    secim = input("Seçim: ").strip()
    if not secim.isdigit() or not (1 <= int(secim) <= len(hedefler)):
        print("Geçersiz seçim.")
        return True

    try:
        kalan = next(_gosterge)
    except StopIteration:
        galaksi["yakit"] = 0
        print("Yakıtın bitti, uzayda sürükleniyorsun…")
        return False

    galaksi["konum"] = hedefler[int(secim) - 1]
    galaksi["yakit"] = kalan
    hamle = _sayac()
    _son_hamle[0] = hamle
    print(f"Yeni konum: {galaksi['konum']} | Yakıt: {galaksi['yakit']} | Hamle: {hamle}")
    return True


def oyunu_bitir():
    print(f"\nOyunu {_son_hamle[0]} hamlede bitirdin!")
    print("En bağlı gezegenler:", en_bagli_gezegenler(galaksi))


if __name__ == "__main__":
    print(f"Başlangıç: {galaksi['konum']} | Yakıt: {galaksi['yakit']}")
    while travel():
        if galaksi["konum"] == "kara_delik":
            print("Kara deliğe ulaştın!")
            break
    oyunu_bitir()
