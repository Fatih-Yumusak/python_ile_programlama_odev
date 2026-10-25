from __future__ import annotations

from functools import lru_cache

import pytest

from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla, hafiza
from uzay_oyunu.fib_sira import uc_sayim
from uzay_oyunu.akis import rota_sayisi_onbelleksiz
from uzay_oyunu.galaksi import galaksi
from uzay_oyunu.oyun import yakit_harca, hedef_menusu, galaksi_kur


class TestSureOlc:
    def test_sonuc_degismeden_doner(self, capsys):
        @sure_olc
        def topla(a, b):
            return a + b

        assert topla(2, 3) == 5

    def test_adli_argumanlar(self, capsys):
        @sure_olc
        def cikar(a, b=0):
            return a - b

        assert cikar(b=4, a=10) == 6

    def test_ad_ve_belge_korunur(self):
        @sure_olc
        def ornek():
            """belge metni"""

        assert ornek.__name__ == "ornek"
        assert ornek.__doc__ == "belge metni"

    def test_cikti_bicimi(self, capsys):
        @sure_olc
        def f():
            return 1

        f()
        cikti = capsys.readouterr().out
        assert cikti.startswith("f: ")
        assert cikti.strip().endswith(" sn")

    def test_rota_sayaci_adim_20(self, capsys):
        sonuc = rota_sayisi_onbelleksiz(galaksi["baglantilar"], "dünya", 20)
        assert sonuc > 0
        cikti = capsys.readouterr().out
        assert cikti.count("rota_sayisi_onbelleksiz:") == 1


class TestSay:
    def test_sayac_artar(self):
        @say
        def f():
            return 1

        f()
        f()
        f()
        assert f.cagri == 3

    def test_sonuc_ve_ad_korunur(self):
        @say
        def f(x):
            """belge"""
            return x * 2

        assert f(4) == 8
        assert f.__name__ == "f"
        assert f.__doc__ == "belge"

    def test_fibonacci_uc_sira(self):
        assert uc_sayim(20) == (21891, 39, 21)


class TestLogCagri:
    def test_konumsal_ve_adli(self, capsys):
        @log_cagri
        def yolculuk(kaynak, hiz=1):
            return f"{kaynak} hiz={hiz}"

        sonuc = yolculuk("orion", hiz=3)
        assert sonuc == "orion hiz=3"
        satirlar = capsys.readouterr().out.splitlines()
        assert satirlar[0] == "-> yolculuk('orion', hiz=3)"
        assert satirlar[1] == "<- yolculuk = 'orion hiz=3'"

    def test_ad_korunur(self):
        @log_cagri
        def f():
            """belge"""

        assert f.__name__ == "f"
        assert f.__doc__ == "belge"

    def test_hedef_menusu_bozulmaz(self):
        assert hedef_menusu(["a", "b"]) == "Nereye gitmek istersin?\n[1] a\n[2] b"

    def test_galaksi_kur_bozulmaz(self):
        sonuc = galaksi_kur(["a", "b"], {"a": ["b"], "b": ["a"]}, "a")
        assert sonuc["konum"] == "a"
        assert sonuc["yakit"] == 50
        with pytest.raises(ValueError):
            galaksi_kur(["a"], {"a": []}, "z")


class TestSinirla:
    def test_alt_sinir(self):
        assert yakit_harca(0) == 100

    def test_ust_sinir(self):
        assert yakit_harca(100) == 0

    def test_ornek_cikti(self):
        assert yakit_harca(30) == 70

    def test_alt_disinda(self):
        with pytest.raises(ValueError):
            yakit_harca(-1)

    def test_ust_disinda(self):
        with pytest.raises(ValueError, match="yakit_harca: 150 değeri 0-100 aralığında değil"):
            yakit_harca(150)

    def test_adli_arguman(self):
        assert yakit_harca(miktar=30) == 70
        with pytest.raises(ValueError):
            yakit_harca(miktar=150)

    def test_ad_korunur(self):
        assert yakit_harca.__name__ == "yakit_harca"
        assert "yakıt" in yakit_harca.__doc__


class TestHafiza:
    def test_lru_cache_ile_ayni_sonuc(self):
        @hafiza()
        def fib_h(n):
            return n if n < 2 else fib_h(n - 1) + fib_h(n - 2)

        @lru_cache(maxsize=None)
        def fib_l(n):
            return n if n < 2 else fib_l(n - 1) + fib_l(n - 2)

        for n in range(30):
            assert fib_h(n) == fib_l(n)

    def test_ayni_cagri_sayisi(self):
        @say
        @hafiza()
        def fib_h(n):
            return n if n < 2 else fib_h(n - 1) + fib_h(n - 2)

        @lru_cache(maxsize=None)
        @say
        def fib_l(n):
            return n if n < 2 else fib_l(n - 1) + fib_l(n - 2)

        fib_h(20)
        fib_l(20)
        assert fib_h.__wrapped__ is not None
        assert fib_l.__wrapped__.cagri == 21

    def test_hesap_bir_kez_yapilir(self):
        hesaplar = []

        @hafiza()
        def kare(x):
            hesaplar.append(x)
            return x * x

        kare(3)
        kare(3)
        assert hesaplar == [3]

    def test_maxsize_en_eskiyi_siler(self):
        hesaplar = []

        @hafiza(maxsize=2)
        def kare(x):
            hesaplar.append(x)
            return x * x

        kare(1)
        kare(2)
        kare(3)
        kare(1)
        assert hesaplar == [1, 2, 3, 1]
        kare(3)
        assert hesaplar == [1, 2, 3, 1]

    def test_ad_korunur(self):
        @hafiza()
        def f():
            """belge"""

        assert f.__name__ == "f"
        assert f.__doc__ == "belge"
