#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy, deepcopy
from typing import Callable, Mapping, Iterable, Optional


class Product:
    max_name_len = 20

    def __init__(self, id_: Optional[str], name: str, price: float) -> None:
        self.id = id_ if id_ is not None else self.generate_id(name)
        self.name = name
        self.price = price


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) > self.max_name_len:
            raise ValueError("Name too long ({0} chars)".format(len(name)))
        self.__name = name

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

    @classmethod
    def from_string(cls, s: str):
        tokens = s.split(';')
        values = [token[token.find('=') + 1:] for token in tokens]
        return Product(id_=values[0], name=values[1], price=float(values[2]))


class InventoryOverflowException(Exception):
    pass


class Catalogue:
    Inventory = Mapping[str, Product]

    max_inventory_size = 2

    def __init__(self, inventory: Inventory = None) -> None:
        if inventory and len(inventory) > self.max_inventory_size:
            raise InventoryOverflowException

        self.inventory = deepcopy(inventory) if inventory else {}

    def add_product(self, product: Product) -> None:
        if len(self.inventory) == self.max_inventory_size:
            raise InventoryOverflowException
        self.inventory[product.id] = copy(product)

    def __contains__(self, id_: str) -> bool:
        return id_ in self.inventory

    def get_products_with_appropriate_price(self, predicate: Callable[[float], bool]) -> Inventory:
        return {k: v for (k, v) in self.inventory.items() if predicate(v.price)}

    def get_products_by_name_part(self, chunk: str, ignore_case: bool = False) -> Inventory:
        has_chunk = (lambda name, chunk_: chunk_.lower() in name.lower()) if ignore_case \
            else (lambda name, chunk_: chunk_ in name)
        return {k: v for (k, v) in self.inventory.items() if has_chunk(v.name, chunk)}

    def add_products(self, products: Iterable[Product]) -> int:
        n_products_added = 0
        for product in products:
            try:
                self.add_product(product)
            except InventoryOverflowException:
                print("Error when adding product: {prod_desc}\n"
                      "   Reason: inventory overflow".format(prod_desc=str(product)))
                break
            n_products_added += 1
        return n_products_added
