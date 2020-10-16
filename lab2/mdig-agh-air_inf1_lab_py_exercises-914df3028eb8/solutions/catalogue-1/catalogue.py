#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy, deepcopy
from typing import Callable, Mapping, Optional


class Product:
    def __init__(self, id_: Optional[str], name: str, price: float) -> None:
        self.id = id_ if id_ is not None else self.generate_id(name)
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = min([price, 100])

    def __str__(self) -> str:
        return '{self.name} [{self.id}] : ${self.price:.2f}'.format(self=self)

    def __eq__(self, other) -> bool:
        return (self.id == other.id) and (self.name == other.name) and (self.price == other.price)

    @classmethod
    def generate_id(cls, name: str) -> str:
        """Wygeneruj ID zgodnie z regułą: usuń spacje i dodaj na koniec liczbę wszystkich znaków w nazwie.
        """
        return ''.join([c for c in name if c != ' ']) + '_' + str(len(name))


class Catalogue:
    Inventory = Mapping[str, Product]

    def __init__(self, inventory: Inventory = None) -> None:
        self.inventory = deepcopy(inventory) if inventory else {}

    def add_product(self, product: Product) -> None:
        self.inventory[product.id] = copy(product)

    def __contains__(self, id_: str) -> bool:
        return id_ in self.inventory

    def get_products_with_appropriate_price(self, predicate: Callable[[float], bool]) -> Inventory:
        return {k: v for (k, v) in self.inventory.items() if predicate(v.price)}

    def get_products_by_name_part(self, chunk: str, ignore_case: bool = False) -> Inventory:
        has_chunk = (lambda name, chunk_: chunk_.lower() in name.lower()) if ignore_case \
            else (lambda name, chunk_: chunk_ in name)
        return {k: v for (k, v) in self.inventory.items() if has_chunk(v.name, chunk)}
