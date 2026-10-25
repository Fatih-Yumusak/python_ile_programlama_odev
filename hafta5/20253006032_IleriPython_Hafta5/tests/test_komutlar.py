from __future__ import annotations

import pytest

from uzay_oyunu import oyun
from uzay_oyunu.komutlar import KOMUTLAR, komut, yardim, envanter, harita

DURUM = {
    "konum": "sirius",
    "baglantilar": {"sirius": ["orion", "dünya", "kara_delik"]},
    "credits": True,
    "engines": False,
    "copilot": True,
}


class TestKayit:
    def test_uc_komut_kayitli(self):
        assert {"yardim", "envanter", "harita"} <= set(KOMUTLAR)

    def test_fonksiyon_degismez(self):
        fonksiyon, aciklama = KOMUTLAR["harita"]
        assert fonksiyon is harita
        assert aciklama == "gidebileceğin gezegenleri gösterir"

    def test_ayni_ad_ikinci_kez(self):
        with pytest.raises(ValueError):
            @komut("yardim")
            def baska(durum):
                return ""


class TestKomutlar:
    def test_yardim(self):
        assert yardim(DURUM) == (
            "envanter  eşyalarını gösterir\n"
            "harita    gidebileceğin gezegenleri gösterir\n"
            "yardim    komutları listeler"
        )

    def test_envanter(self):
        assert envanter(DURUM) == "Sende: bol kredi, yetenekli bir pilot"

    def test_envanter_bos(self):
        bos = {**DURUM, "credits": False, "copilot": False}
        assert envanter(bos) == "Hiçbir eşyan yok."

    def test_harita(self):
        assert harita(DURUM) == "orion, dünya, kara_delik"


class TestTravel:
    def setup_method(self):
        self.konum = oyun.galaksi["konum"]
        self.yakit = oyun.galaksi["yakit"]

    def teardown_method(self):
        oyun.galaksi["konum"] = self.konum
        oyun.galaksi["yakit"] = self.yakit

    def _girdiler(self, monkeypatch, *girdiler):
        it = iter(girdiler)
        monkeypatch.setattr("builtins.input", lambda _="": next(it))

    def test_komut_sonra_menu_tekrar(self, monkeypatch, capsys):
        menuler = []
        gercek = oyun.hedef_menusu
        monkeypatch.setattr(oyun, "hedef_menusu", lambda h: menuler.append(h) or gercek(h))
        self._girdiler(monkeypatch, "yardim", "1")
        oyun.travel()
        assert "komutları listeler" in capsys.readouterr().out
        assert len(menuler) == 2

    def test_komuttan_sonra_gezegen_secimi(self, monkeypatch):
        self._girdiler(monkeypatch, "harita", "1")
        oyun.travel()
        assert oyun.galaksi["konum"] == "sirius"

    def test_gezegen_secimi_eskisi_gibi(self, monkeypatch):
        self._girdiler(monkeypatch, "2")
        oyun.travel()
        assert oyun.galaksi["konum"] == "centauri"

    def test_gecersiz_secim(self, monkeypatch, capsys):
        self._girdiler(monkeypatch, "abc")
        oyun.travel()
        assert "Geçersiz seçim." in capsys.readouterr().out
        assert oyun.galaksi["konum"] == self.konum
