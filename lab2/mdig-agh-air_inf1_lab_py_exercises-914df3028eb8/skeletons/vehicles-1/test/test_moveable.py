#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from vehicles import *


class TestMovable(unittest.TestCase):
    def test_init(self):
        moveable = Movable(x=1, y=2)
        self.assertEqual(1, moveable.x)
        self.assertEqual(2, moveable.y)

    def test_move(self):
        moveable = Movable(x=0, y=0)
        moveable.move(dx=1, dy=2)
        self.assertEqual(1, moveable.x)
        self.assertEqual(2, moveable.y)


class TestVehicleWithMovableMixin(unittest.TestCase):
    def test_inheritance(self):
        self.assertTrue(issubclass(Vehicle, Movable))


if __name__ == '__main__':
    unittest.main()
