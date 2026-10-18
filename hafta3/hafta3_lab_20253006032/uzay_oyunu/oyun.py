# Fatih Yumuşak - 20253006032
# İleri Python Programlama Hafta 3 Lab

import json
from pathlib import Path
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler


# Görev 1 - saf fonksiyonlar (print etmemeli, sadece değer döndürmeli)

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


# Görev 3 - galaksiyi json dosyasından okuyup kurma

def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    """Galaksi sözlüğü oluşturur. Başlangıç gezegeni yoksa ValueError fırlatır."""
    if baslangic not in gezegenler:
        raise ValueError(f"'{baslangic}' gezegeni listede yok")

    yakit = kwargs.get("yakit", 50)  # verilmezse varsayılan 50

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
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
_son_hamle = [0]  # tek elemanlı liste, global yazmadan içini değiştirebilmek için


def travel():
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
        return

    print(hedef_menusu(hedefler))

    secim = input("Seçim: ").strip()
    if not secim.isdigit() or not (1 <= int(secim) <= len(hedefler)):
        print("Geçersiz seçim.")
        return

    galaksi["konum"] = hedefler[int(secim) - 1]
    galaksi["yakit"] -= 10
    hamle = _sayac()
    _son_hamle[0] = hamle
    print(f"Yeni konum: {galaksi['konum']} | Yakıt: {galaksi['yakit']} | Hamle: {hamle}")


def oyunu_bitir():
    print(f"\nOyunu {_son_hamle[0]} hamlede bitirdin!")
    print("En bağlı gezegenler:", en_bagli_gezegenler(galaksi))


if __name__ == "__main__":
    print(f"Başlangıç: {galaksi['konum']} | Yakıt: {galaksi['yakit']}")
    while galaksi["yakit"] > 0:
        travel()
        if galaksi["konum"] == "kara_delik":
            print("Kara deliğe ulaştın!")
            break
    oyunu_bitir()
