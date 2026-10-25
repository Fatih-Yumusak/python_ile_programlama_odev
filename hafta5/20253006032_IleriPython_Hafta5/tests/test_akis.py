from __future__ import annotations

import itertools
import pytest

from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
    rota_sayaci,
)
from uzay_oyunu.galaksi import galaksi


class TestFibonacci:
    def test_ilk_uc_next(self):
        g = fibonacci()
        assert (next(g), next(g), next(g)) == (0, 1, 1)

    def test_ilk_oniki_islice(self):
        sonuc = list(itertools.islice(fibonacci(), 12))
        assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def test_yuz_den_kucuk_takewhile(self):
        sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
        assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def test_tek_kullanimlik(self):
        """Aynı üreteç tüketilince devam eden yerden devam etmeli."""
        g = fibonacci()
        ilk = list(itertools.islice(g, 5))
        ikinci = list(itertools.islice(g, 5))
        assert ilk != ikinci
        assert ikinci == [5, 8, 13, 21, 34]

    def test_yeni_uretec_sifirdan_baslar(self):
        """Her yeni fibonacci() çağrısı 0'dan başlamalı."""
        assert list(itertools.islice(fibonacci(), 3)) == [0, 1, 1]
        assert list(itertools.islice(fibonacci(), 3)) == [0, 1, 1]


class TestYakitGostergesi:
    def test_ornek_cikti(self):
        assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

    def test_tam_bolunebilir(self):
        assert list(yakit_gostergesi(20, 10)) == [10, 0]

    def test_tek_adim(self):
        assert list(yakit_gostergesi(5, 10)) == [0]

    def test_stopiteration_yakalanir(self):
        """Üretec bitince StopIteration fırlatılmalı."""
        g = yakit_gostergesi(10, 10)
        next(g)
        with pytest.raises(StopIteration):
            next(g)

    def test_dusuk_tuketim_oyun_icin(self):
        """Tüketim 5 ile 100 yakıt 20 adımda bitmeli."""
        degerler = list(yakit_gostergesi(100, 5))
        assert degerler[0] == 95
        assert degerler[-1] == 0
        assert len(degerler) == 20


SEYIR_YOLU = "veri/seyir.txt"


class TestSeyirBoruHatti:
    def test_satirlari_oku_yorum_atlama(self):
        satirlar = list(satirlari_oku(SEYIR_YOLU))
        assert all(not s.startswith("#") for s in satirlar)

    def test_satirlari_oku_bos_satir_atlama(self):
        satirlar = list(satirlari_oku(SEYIR_YOLU))
        assert all(s.strip() != "" for s in satirlar)

    def test_satirlari_oku_satir_sayisi(self):
        assert len(list(satirlari_oku(SEYIR_YOLU))) == 6

    def test_ayristir_toplam_yakit(self):
        assert sum(y for _, _, y in ayristir(satirlari_oku(SEYIR_YOLU))) == 88

    def test_ayristir_ilk_kayit(self):
        kayit = next(ayristir(satirlari_oku(SEYIR_YOLU)))
        assert kayit == ("dünya", "sirius", 12)

    def test_uzun_yolculuklar_esik_10(self):
        kayitlar = ayristir(satirlari_oku(SEYIR_YOLU))
        hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
        assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]

    def test_boru_hatti_tembel(self):
        """Üç fonksiyon da generator döndürmeli, liste değil."""
        import types
        assert isinstance(satirlari_oku(SEYIR_YOLU), types.GeneratorType)
        assert isinstance(ayristir(satirlari_oku(SEYIR_YOLU)), types.GeneratorType)
        kayitlar = ayristir(satirlari_oku(SEYIR_YOLU))
        assert isinstance(uzun_yolculuklar(kayitlar, 10), types.GeneratorType)


class TestRotaSayaci:
    def setup_method(self):
        self.say = rota_sayaci(galaksi["baglantilar"])

    def test_adim_3(self):
        assert self.say("dünya", 3) == 9

    def test_adim_10(self):
        assert self.say("dünya", 10) == 2185

    def test_adim_40(self):
        assert self.say("dünya", 40) == 16832258606399

    def test_adim_0(self):
        assert self.say("dünya", 0) == 1

    def test_onbellek_calisiyor(self):
        """Birkaç çağrı sonrası önbellekte hit olmalı."""
        self.say("dünya", 15)
        info = self.say.cache_info()
        assert info.hits > 0

    def test_once_onbelleksiz_sonra_onbellekli_hiz(self):
        """Önbellekli sürüm önbelleksizden belirgin şekilde hızlı olmalı."""
        import time

        bag = galaksi["baglantilar"]

        def rota_sayisi_saf(gezegen, adim):
            if adim == 0:
                return 1
            return sum(rota_sayisi_saf(k, adim - 1) for k in bag.get(gezegen, []))

        t0 = time.perf_counter()
        rota_sayisi_saf("dünya", 20)
        sure_saf = time.perf_counter() - t0

        say_h = rota_sayaci(bag)
        t1 = time.perf_counter()
        say_h("dünya", 20)
        sure_onb = time.perf_counter() - t1

        assert sure_onb < sure_saf


class TestIstatistik:
    def test_buyuk_harfli_map(self):
        from istatistik import buyuk_harfli_map
        assert buyuk_harfli_map() == ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]

    def test_buyuk_harfli_liste(self):
        from istatistik import buyuk_harfli_liste
        assert buyuk_harfli_liste() == ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]

    def test_cok_baglantili_filter(self):
        from istatistik import cok_baglantili_filter
        assert cok_baglantili_filter() == ["dünya", "centauri", "sirius", "orion"]

    def test_cok_baglantili_liste(self):
        from istatistik import cok_baglantili_liste
        assert cok_baglantili_liste() == ["dünya", "centauri", "sirius", "orion"]

    def test_toplam_baglanti_reduce(self):
        from istatistik import toplam_baglanti_reduce
        assert toplam_baglanti_reduce() == 10

    def test_toplam_baglanti_sum(self):
        from istatistik import toplam_baglanti_sum
        assert toplam_baglanti_sum() == 10

    def test_hizli_yolculuk_partial(self):
        from istatistik import hizli_yolculuk
        sonuc = hizli_yolculuk("dünya", "sirius")
        assert "Hız 3" in sonuc
        assert "dünya" in sonuc
        assert "sirius" in sonuc
