#!/usr/bin/python
# -*- coding: utf-8 -*-

import operator
from functools import reduce
from typing import List, Any, Union, Sequence, Callable, MutableSequence, Mapping, NamedTuple, Iterable

# FIXME (skel): Zastąpić (regex) -- "return .*" => "pass"
# FIXME (skel): Usunąć pozostałe fragmenty implementacji.

def list_print() -> None:
    colors = ['red', 'green', 'blue']

    for inx, color in enumerate(colors):
        print(inx, ' -> ', color)


def remove_duplicates(elements: Iterable[Any]) -> List[Any]:
    """Usuń duplikaty z listy (bez zachowania kolejności).

    Przykład: [1, 1, 2, 2] -> [2, 1]

    Parametry:
    elements -- lista elementów, z której należy usunąć duplikaty
    """
    return list(set(elements))


# Podpowiedź typu `Num` := jeden z typów: int, float
Num = Union[int, float]


class MinMax(NamedTuple):
    min: Num
    max: Num


def min_max(numbers: Sequence[Num], upper_limit: Num = None) -> MinMax:
    """Zwróć min i max spośród przekazanych liczb (z ograniczeniem górnym).

    Parametry:
    numbers -- kolekcja liczb
    upper_limit -- maksymalna wartość największej liczby

    Typ zwracany: namedtuple (pola: min, max)
    """

    num_min = min(numbers)
    num_max = max(numbers)

    if upper_limit is not None:
        num_max = min(num_max, upper_limit)

    return MinMax(min=num_min, max=num_max)


def append(elements: MutableSequence[Any] = None) -> MutableSequence[Any]:
    """Dodaj "hi" na koniec listy.

    Wywołanie z argumentem domyślnym powinno zwrócić listę ["hi"].

    elements -- lista, do której dopisujemy
    """
    if not elements:
        elements = []

    elements.append("hi")
    return elements


def sum_values(my_dict: Mapping[Any, Num]) -> Num:
    """Zsumuj wszystkie wartości w słowniku.

    Parametry:
    my_dict -- słownik, którego wartości są sumowane
    """
    return sum(my_dict.values())


def filter_pesels_by_name_initial(persons: Mapping[str, str], name_initial: str) -> List[str]:
    """Zwróć zbiór PESEL-i osób, których imię zaczyna się zadaną literę.

    Parametry:
    persons -- baza osób {PESEL -> osoba}
    name_initial -- inicjał imienia użyty do filtrowania
    """
    pesels = []
    for pesel, name in persons.items():
        if name[0] == name_initial:
            pesels.append(pesel)
    return pesels


def repeat(f: Callable[[Num], Num]) -> List[Num]:
    """Zwróć listę wartości zwróconych przez wywołanie f()
    z argumentami 1, 3 i 5.

    Parametry:
    f -- jednoargumentowa funkcja przyjmująca i zwracająca liczbę
    """
    return [f(arg) for arg in [1, 3, 5]]


def count_if(words: Sequence[str]) -> int:
    """Zwróć liczbę słów z listy spełniających oba poniższe warunki:
    - długość słowa wynosi co najmniej 2
    - słowo zaczyna się na litetę 'a' lub jest palindromem
    """
    return sum([len(word) >= 2 and (word[0] == 'a' or word == word[::-1]) for word in words])


def mul_if(numbers: Sequence[Num], predicate: Callable[[Num], bool]) -> Num:
    """Zwróć iloczyn liczb spełniających predykat.

     Parametry:
     numbers -- kolekcja liczb
     predicate -- predykat
    """
    return reduce(operator.mul, filter(predicate, numbers), 1)


list_print()
