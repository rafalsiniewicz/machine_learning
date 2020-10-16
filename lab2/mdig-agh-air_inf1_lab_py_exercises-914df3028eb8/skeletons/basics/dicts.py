#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Słowniki
#
# -----------------------------------------------------------------------------

from typing import Dict, Any, Tuple, Optional, Set


def dict_intro() -> None:
    """Rozgrzewka: tworzenie i wypisywanie słownika.

    Utwórz w jednej instrukcji słownik {str -> int} zawierający następujące
    pary klucz-wartość: Adam=2, Bogdan=4, Cezary=1.
    Następnie wypisz całą zawartość słownika, po jednym wpisie w każdym wierszu.

    Przykładowo (kolejność wpisów może się różnić od poniższej):
      Adam = 2
      Bogdan = 4
      Cezary = 1

    (zob. "test" w pliku test/test_dict_intro.py)
    """
    pass


# Alias `Menu` na typ `Dict[str, float]` poprawia czytelność kodu
# oraz upraszcza wprowadzanie ewentualnych zmian w programie.
Menu = Dict[str, float]


def update_price(menu: Menu, dish: str) -> None:
    """Zwiększ wartość skojarzoną z kluczem `dish` w słowniku `menu` o 50.

    :param menu: menu, które należy zaktualizować
    :param dish: danie, którego cena powinna zostać zmieniona
    """
    pass


def fix_key(dct: Dict[str, Any], incorrect_key: str, correct_key: str) -> Dict[str, Any]:
    """Skoryguj ewentualny błędny klucz w słowniku.

    Jeśli słownik `dct` zawiera błędy klucz `incorrect_key`, przepisz jego wartość
    do nowego, poprawnego klucza `correct_key` oraz usuń błędny klucz.

    W implementacji nie twórz nowego słownika "od zera".

    :param dct: słownik, który (potencjalnie) należy skorygować
    :param incorrect_key: błędny klucz (do poprawy)
    :param correct_key: poprawny klucz, który powinien zastąpić błędny klucz
    :return: poprawny słownik
    """
    pass


def update_all_prices(menu: Menu) -> None:
    """Zwiększ każdą z wartości w słowniku `menu` o 50.

    :param menu: menu, które należy zaktualizować
    """
    pass


# TODO: Zdefiniuj alias `ClassRegister` na typ umożliwiający przechowywanie
#   informacji o ocenach poszczególnych uczniów, tj. mapowanie nazwy
#   ucznia na listę ocen (będących liczbami zmiennoprzecinkowymi).
ClassRegister = None


def average_grades_1(register: ClassRegister) -> Dict[str, float]:
    """Oblicz średnią dla każdego ucznia.

    Przyjmij, że każdy uczeń ma co najmniej jedną ocenę.

    :param register: dziennik ocen
    :return: mapowanie nazwy ucznia na średnią jego ocen
    """
    pass


# [OPT]
def average_grades_2(register: ClassRegister) -> Dict[str, Optional[float]]:
    """Oblicz średnią dla każdego ucznia.

    Jeśli uczeń nie posiada ani jednej oceny, przyjmij że średnia wynosi None.

    :param register: dziennik ocen
    :return: mapowanie nazwy ucznia na średnią jego ocen (albo None, jeśli
        dany uczeń nie posiada ocen)
    """
    pass


def letters_frequencies(s: str) -> Dict[str, int]:
    """Zwróć zestawienie częstości występowania poszczególnych liter w danym słowie.

    :param s: łańcuch znaków, dla którego obliczana jest częstość wystąpień liter
    :return: mapowanie litery na częstość jej występowania
    """
    pass


def letters_frequency_2(s: str) -> Tuple[Dict[str, int], int]:
    """Zwróć zestawienie częstości występowania poszczególnych liter w danym słowie
    ORAZ liczbę unikalnych liter.

    W implemnetacji wywołaj funkcję `letters_frequencies()`.

    :param s: łańcuch znaków, dla którego obliczane są statystyki
    :return: 2-elementowa krotka złożona ze słownika częstości występowania
        poszczególnych liter oraz z liczby unikalnych liter
    """
    pass


def census(register: Dict[str, Dict[str, Any]]) -> Tuple[Dict[str, int], float]:
    """Wyznacz liczbę osób z poszczególnych państw oraz średni wiek wszystkich osób.

    Przyjmij, że rejestr zawiera dane choć jednej osoby oraz że informacje
    w słowniku są poprawne (nie ma brakujących kluczy itd.).

    :param register: spis osób w formacie {N: {'address': {'country': C}, 'age': A}
        gdzie N - nazwa osoby; C - państwo, z którego osoba pochodzi; A - wiek osoby
    :return: 2-elementowa krotka złożona ze słownika opisującego liczbę osób
        z poszczególnych państw oraz ze średniego wieku wszystkich osób
    """
    pass


# lista zakupowa - mapowanie nazwy produktu na liczbę sztuk (do kupienia)
ShoppingList = Dict[str, int]


def sum_shopping_lists(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    """Scal dwie listy zakupowe w jedną.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: scalone listy zakupowe
    """
    pass


def sum_shopping_lists_nonempty(list1: ShoppingList, list2: ShoppingList) -> ShoppingList:
    """Scal dwie listy zakupowe w jedną, z pominięciem produktów o krotności 0.

    W implementacji wywołaj funkcję `sum_shopping_lists()`.

    :param list1: pierwsza lista zakupowa
    :param list2: druga lista zakupowa
    :return: scalone listy zakupowe
    """
    pass


def filter_pesels_by_name_initial(persons: Dict[str, str], name_initial: str) -> Set[str]:
    """Zwróć zbiór PESEL-i osób, których imię zaczyna się zadaną literę.

    Implementacja powinna zawierać wyłącznie instrukcję `return`.
    W rozwiązaniu użyj set comprehension.

    :param persons: baza osób {PESEL -> osoba}
    :param name_initial: inicjał imienia użyty do filtrowania
    :return: zbiór PESEL-i osób
    """
    pass
