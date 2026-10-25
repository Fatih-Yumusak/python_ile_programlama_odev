from __future__ import annotations

import json
from pathlib import Path

with open(Path(__file__).parent / "galaksi.json", encoding="utf-8") as _f:
    galaksi: dict = json.load(_f)


def gezegen_var_mi(ad: str) -> bool:
    '''Gezegenin galakside olup olmadığını döndürür.'''
    return ad in galaksi["gezegenler"]


def komsular(gezegen: str) -> list[str]:
    '''Gezegenin komşularını döndürür.'''
    return galaksi["baglantilar"].get(gezegen, [])
