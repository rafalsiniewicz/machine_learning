#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Zagadnienia dodatkowe
#
# -----------------------------------------------------------------------------

from typing import List, Set, Dict, Tuple, Optional, Callable


def get_unique_letters(s: str) -> Set[str]:
    """Zwróć zbiór unikalnych liter (o ile łańcuch zawiera co najmniej 3 znaki).

    Aby otrzymać listę znaków w łańcuchu znaków, przekaż ten łańcuch jako argument
    funkcji list().

    :param s:
    :return: zbiór unikalnych liter w łańcuchu znaków, jeśli łańcuch zawiera co
        najmniej 3 znaki, inaczej zbiór pusty
    """
    pass


# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def products_to_buy(list1: ShoppingList, list2: ShoppingList) -> Set[str]:
    """Zwróć zbiór produktów, które należy kupić.

    Przyjmij, że każda z list zawiera produkty, których należy kupić co najmniej
    jedną sztukę.

    W implementacji użyj wyłącznie instrukcji `return` - zwróć sumę zbiorów
    kluczy w obu słownikach.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: zbiór produktów, które należy kupić
    """
    pass


def products_only_on_one_list(list1: ShoppingList, list2: ShoppingList) -> int:
    """Zwróć liczbę produktów, które występują tylko na jednej z list zakupowych.

    W implementacji użyj wyłącznie instrukcji `return` - zwróć różnicę symetryczną
    zbiorów kluczy w obu słownikach.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: liczba produktów, które występują tylko na jednej z list zakupowych
    """
    pass


def two_dice_rolls_combinations() -> Dict[int, Set[Tuple[int, int]]]:
    """Zwróć słownik możliwych wyników rzutu dwiema kostkami.

    Przyjmij, że kostki są znaczone - zatem (1, 2) i (2, 1) to dwa różne wyniki.

    :return: słownik zawierający mapowanie sumy oczek na zbiór kombinacji
        wyników rzutu parą kostek
    """
    pass


def append_and_sort(lst: List[str]) -> List[str]:
    """Utwórz kopię listy wejściowej, dodaj do niej element 'abc', a na koniec
        zwróć jej elementy posortowane w porządku alfabetycznym (rosnącym).
    """
    pass


def ints_to_str(lst: List[int]) -> str:
    """Sklej listę liczb (całkowitych) w jeden łańcuch znaków.

    W implementacji skorzystaj z metody str.join(), list comprehension oraz
    z funkcji wbudowanej str().

    Przykład: ints_to_str([11, 33, 50]) = '113350'

    :param lst: lista liczb całkowitych
    :return: łańcuch znaków powstały ze "sklejenia" elementów przekazanej listy
    """
    pass


def ints_to_str_max_length(lst: List[int], max_length: Optional[int] = None) -> str:
    """Sklej listę liczb w jeden łańcuch znaków o ustalonej maksymalnej długości.

    Argument domyślny dla `max_length` to None, co oznacza, że nie ma ograniczenia
    na maksymalną długość wynikowego łańcucha znaków.

    W implementacji wywołaj funkcję `ints_to_str()`.

    Przykład:
        ints_to_str_max_length([11, 33]) = '1133'
        ints_to_str_max_length([11, 33], 3) = '113'

    :param lst: lista liczb całkowitych
    :param max_length: maksymalna długość łańcucha znaków po "sklejeniu"
    :return: łańcuch znaków powstały ze "sklejenia" elementów przekazanej listy
    """
    pass


def division_guardian(x: float, y: float) -> bool:
    """Sprawdź, czy stosunek x/y jest większy niż 1.

    Implementacja powinna zawierać wyłącznie instrukcję `return`.
    W wyrażeniu logicznym skorzystaj wyłącznie z operatora AND (zastosuj
    mechanizm "short-circuting").

    :param x: liczba zmiennoprzecinkowa
    :param y: liczba zmiennoprzecinkowa
    :return: True jeśli x/y > 1 (dla y różnego od 0), False gdy y = 0 lub gdy
        x/y < 1
    """
    pass


def f_compose(f: Callable[[float], float], x0: float) -> float:
    """Zwróć wynik złożenia ("matematycznej") funkcji `f` z samą sobą (tj. f²(x)).

    :param f: funkcja R ↦ R
    :param x0: liczba rzeczywista (x0 ∈ R)
    :return: wartość f²(x0)
    """
    pass
