#!/usr/bin/python
# -*- coding: utf-8 -*-

# Moduł zawierający predefiniowane ciągi
from typing import List, Generator


def fib(n: int) -> List[int]:
    """Zwróć n pierwszych elementów ciągu Fibonacciego.

    Parametry:
     n -- liczba elementów ciągu do wygenerowania
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
