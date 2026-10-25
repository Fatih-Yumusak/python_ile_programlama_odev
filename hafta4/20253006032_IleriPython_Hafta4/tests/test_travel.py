from __future__ import annotations

from uzay_oyunu import oyun
from uzay_oyunu.akis import yakit_gostergesi


def _hazirla(monkeypatch, girdiler, yakit=100, tuketim=5):
    monkeypatch.setattr(oyun, "_gosterge", yakit_gostergesi(yakit, tuketim))
    monkeypatch.setitem(oyun.galaksi, "konum", "dünya")
    monkeypatch.setitem(oyun.galaksi, "yakit", yakit)
    it = iter(girdiler)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))


def test_yolculuk_gostergeden_yakit_ceker(monkeypatch):
    _hazirla(monkeypatch, ["1"])
    assert oyun.travel() is True
    assert oyun.galaksi["yakit"] == 95


def test_gecersiz_secim_yakit_harcamaz(monkeypatch):
    _hazirla(monkeypatch, ["x"])
    assert oyun.travel() is True
    assert oyun.galaksi["yakit"] == 100


def test_yakit_bitince_mesaj_ve_oyun_biter(monkeypatch, capsys):
    _hazirla(monkeypatch, ["1", "1"], yakit=5, tuketim=5)
    assert oyun.travel() is True
    assert oyun.galaksi["yakit"] == 0
    assert oyun.travel() is False
    assert "Yakıtın bitti, uzayda sürükleniyorsun…" in capsys.readouterr().out
