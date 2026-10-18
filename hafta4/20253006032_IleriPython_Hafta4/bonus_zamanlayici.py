"""
10 saniye boyunca her 2 saniyede tik, her 5 saniyede tak yazan program.

Neden meşgul bekleme: zamanlayici() içinde cpu sürekli perf_counter'ı kontrol
ediyor, hiç durmuyor. time.sleep() olsaydı işletim sistemi cpu'yu başka işlere
verirdi ama burada döngü sürekli dönüyor yani cpu meşgul bekliyor.
"""

from __future__ import annotations

import time
from uzay_oyunu.akis import zamanlayici


def main() -> None:
    sure = 10.0

    tik_gen = zamanlayici(2.0)
    tak_gen = zamanlayici(5.0)

    sonraki_tik = next(tik_gen)
    sonraki_tak = next(tak_gen)

    baslangic = time.perf_counter()

    while True:
        simdi = time.perf_counter() - baslangic
        if simdi >= sure:
            break
        if simdi >= sonraki_tik:
            print(f"[{simdi:.1f}s] tik")
            try:
                sonraki_tik = next(tik_gen)
            except StopIteration:
                sonraki_tik = float("inf")
        if simdi >= sonraki_tak:
            print(f"[{simdi:.1f}s] tak")
            try:
                sonraki_tak = next(tak_gen)
            except StopIteration:
                sonraki_tak = float("inf")

    print("Süre doldu.")


if __name__ == "__main__":
    main()
