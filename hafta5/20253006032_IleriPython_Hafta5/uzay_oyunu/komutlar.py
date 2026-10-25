from __future__ import annotations

from uzay_oyunu.oyun import envanter_metni

KOMUTLAR: dict = {}


def komut(ad, aciklama=""):
    """Fonksiyonu değiştirmeden (fonksiyon, aciklama) olarak KOMUTLAR'a kaydeder."""
    def dekorator(fonksiyon):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten tanımlı")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon
    return dekorator


@komut("yardim", "komutları listeler")
def yardim(durum: dict) -> str:
    """Kayıtlı komutları adlarıyla ve açıklamalarıyla listeler."""
    genislik = max(len(ad) for ad in KOMUTLAR)
    satirlar = [
        f"{ad.ljust(genislik)}  {aciklama}"
        for ad, (_, aciklama) in sorted(KOMUTLAR.items())
    ]
    return "\n".join(satirlar)


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict) -> str:
    """Oyuncunun eşyalarını döndürür."""
    metin = envanter_metni(durum["credits"], durum["engines"], durum["copilot"])
    return metin or "Hiçbir eşyan yok."


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict) -> str:
    """Bulunulan gezegenden gidilebilecek gezegenleri döndürür."""
    return ", ".join(durum["baglantilar"][durum["konum"]])
