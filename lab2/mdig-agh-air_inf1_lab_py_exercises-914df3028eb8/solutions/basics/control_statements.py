#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Instrukcje sterujące
#
# -----------------------------------------------------------------------------


def min_pow_2(n: int) -> int:
    """Oblicz najmniejszą potęgę 2 większą od zadanej liczby naturalnej `n`.

    W implementacji użyj pętli `while`. Przyjmij, że `n` jest zawsze większe
    od 0 (nie musisz tego sprawdzać).

    Przykład: min_pow_2(5) = 8, min_pow_2(8) = 16 itd.

    :param n: liczba naturalna
    :return: najmniejszą potęgę 2 większą od zadanej liczby całkowitej `n`
    """
    pow2: int = 1
    while pow2 <= n:
        pow2 *= 2
    return pow2


def parity_str(n: int) -> str:
    """Zwróć łańcuch znaków "parzysta" jeśli `n` jest liczbą parzystą, a w przeciwym
    razie – zwróć łańcuch znaków "nieparzysta".

    W implementacji użyj wyrażenia warunkowego (ciało funkcji powinno składać się
    z jednej instrukcji!).

    Przykład: parity_str(2) => "parzysta", parity_str(3) => "nieparzysta"

    :param n: liczba, której parzystość jest badana
    :return: "parzysta" jeśli `n` jest liczbą parzystą, w przeciwym razie "nieparzysta"
    """
    return "parzysta" if n % 2 == 0 else "nieparzysta"


def plf(x: float) -> float:
    """Funkcja realizuje funkcję matematyczną:
            / 1   jeśli x < 3
    f(x) = {  1.5 jeśli x ∈ [3, 10)
            \ 4   jeśli x ≥ 10

    Przykład: plf(3) = 1.5, plf(10) = 4

    :param x: liczba rzeczywista
    :return: wartość funkcji f(x)
    """
    if x < 3:
        return 1
    elif x < 10:
        return 1.5
    else:
        return 4
