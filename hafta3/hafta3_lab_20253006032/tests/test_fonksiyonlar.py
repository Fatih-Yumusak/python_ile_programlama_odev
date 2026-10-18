# Fatih Yumuşak - 20253006032
# Görev 1 testleri - önce testleri yazdım, sonra fonksiyonları ekledim

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


# envanter_metni testleri

def test_kredi_ve_pilot_var():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"

def test_hicbir_sey_yok():
    assert envanter_metni(False, False, False) == ""

def test_sadece_kredi():
    assert envanter_metni(True, False, False) == "Sende: bol kredi"

def test_sadece_motorlar():
    assert envanter_metni(False, True, False) == "Sende: güçlü motorlar"

def test_sadece_pilot():
    assert envanter_metni(False, False, True) == "Sende: yetenekli bir pilot"

def test_hepsi_var():
    assert envanter_metni(True, True, True) == "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"

def test_donen_deger_string():
    assert isinstance(envanter_metni(True, True, True), str)


# hedef_menusu testleri

def test_iki_hedef():
    sonuc = hedef_menusu(["centauri", "sirius"])
    assert sonuc == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"

def test_tek_hedef():
    assert hedef_menusu(["mars"]) == "Nereye gitmek istersin?\n[1] mars"

def test_bos_liste():
    assert hedef_menusu([]) == "Nereye gitmek istersin?"

def test_numaralar_dogru():
    sonuc = hedef_menusu(["a", "b", "c"])
    assert "[1] a" in sonuc
    assert "[2] b" in sonuc
    assert "[3] c" in sonuc

def test_baslik_ilk_satirda():
    sonuc = hedef_menusu(["x", "y"])
    assert sonuc.startswith("Nereye gitmek istersin?")
