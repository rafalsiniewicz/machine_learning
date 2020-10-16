#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import TypeVar, Container


class Movable:
    def __init__(self, x: float, y: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy


class Vehicle(ABC, Movable):
    def __init__(self, id_: str, brand: str, *args, **kwargs) -> None:
        super().__init__(0, 0, *args, **kwargs)
        self.id = id_
        self.brand = brand

    @abstractmethod
    def max_speed(self) -> float:
        raise NotImplementedError()

    def __str__(self) -> str:
        return '{self.id} :  {self.brand}'.format(self=self)


V = TypeVar('V', bound=Vehicle)


def vehicle_collection_as_string(vehicles: Container[V]):
    return '\n'.join(map(str, vehicles))


class Car(Vehicle):
    def __init__(self, id_: str, brand: str, engine_hp: float, *args, **kwargs) -> None:
        super().__init__(id_, brand, *args, **kwargs)
        self.engine_hp = engine_hp

    def max_speed(self) -> float:
        return self.engine_hp


class Bicycle(Vehicle):
    def __init__(self, id_: str, brand: str, n_gears: int, *args, **kwargs) -> None:
        super().__init__(id_, brand, *args, **kwargs)
        self.n_gears = n_gears

    def max_speed(self) -> float:
        return self.n_gears * 3


def compute_min_travel_duration(distance: float, vehicle: Vehicle) -> float:
    return distance / vehicle.max_speed()


def compute_min_travel_duration_as_string(distance: float, vehicle: Vehicle) -> str:
    return '{0:.3f} h'.format(compute_min_travel_duration(distance, vehicle))
