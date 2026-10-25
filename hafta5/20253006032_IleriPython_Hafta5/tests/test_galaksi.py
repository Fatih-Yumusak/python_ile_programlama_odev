"""Hafta 3 tabanı – galaksi verisi ve temel fonksiyon testleri."""

import pytest
from uzay_oyunu.galaksi import galaksi, gezegen_var_mi, komsular


def test_gezegen_listesi():
    assert "dünya" in galaksi["gezegenler"]
    assert "kara_delik" in galaksi["gezegenler"]


def test_gezegen_var_mi_true():
    assert gezegen_var_mi("sirius") is True


def test_gezegen_var_mi_false():
    assert gezegen_var_mi("mars") is False


def test_komsular_dunya():
    assert set(komsular("dünya")) == {"sirius", "centauri"}


def test_komsular_kara_delik():
    assert komsular("kara_delik") == ["sirius"]


def test_baslangic_yakiti():
    assert galaksi["yakit"] == 100
