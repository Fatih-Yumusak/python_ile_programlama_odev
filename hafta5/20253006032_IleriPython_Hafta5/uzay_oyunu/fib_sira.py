from __future__ import annotations

from functools import lru_cache

from uzay_oyunu.dekoratorler import say


def uc_sayim(n: int = 20) -> tuple[int, int, int]:
    """fib(n) için üç dekoratör sırasındaki çağrı sayılarını döndürür."""

    @say
    def fib_a(k):
        return k if k < 2 else fib_a(k - 1) + fib_a(k - 2)

    @say
    @lru_cache(maxsize=None)
    def fib_b(k):
        return k if k < 2 else fib_b(k - 1) + fib_b(k - 2)

    @lru_cache(maxsize=None)
    @say
    def fib_c(k):
        return k if k < 2 else fib_c(k - 1) + fib_c(k - 2)

    fib_a(n)
    fib_b(n)
    fib_c(n)
    return fib_a.cagri, fib_b.cagri, fib_c.__wrapped__.cagri


if __name__ == "__main__":
    a, b, c = uc_sayim(20)
    print(f"Yalnızca @say             : {a}")
    print(f"@say üstte, @lru_cache altta: {b}")
    print(f"@lru_cache üstte, @say altta: {c}")
