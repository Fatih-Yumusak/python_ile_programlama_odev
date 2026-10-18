from __future__ import annotations

galaksi: dict = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya":      ["sirius", "centauri"],
        "sirius":     ["dünya", "orion", "kara_delik"],
        "centauri":   ["dünya", "orion"],
        "orion":      ["sirius", "centauri"],
        "kara_delik": ["sirius"],
    },
    "yakit": 100,
}


def gezegen_var_mi(ad: str) -> bool:
    '''Gezegenin galakside olup olmadığını döndürür.'''
    return ad in galaksi["gezegenler"]


def komsular(gezegen: str) -> list[str]:
    '''Gezegenin komşularını döndürür.'''
    return galaksi["baglantilar"].get(gezegen, [])
