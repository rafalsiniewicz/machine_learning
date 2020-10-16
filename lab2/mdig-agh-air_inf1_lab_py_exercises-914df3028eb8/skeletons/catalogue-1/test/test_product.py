#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from catalogue import Product


class TestProduct(unittest.TestCase):
    def test_init(self):
        product = Product(id_="RB01", name="Robot", price=10.2)
        self.assertEqual("RB01", product.id)
        self.assertEqual("Robot", product.name)
        self.assertEqual(10.2, product.price)

    def test_str_integer_price(self):
        product = Product(id_="RB01", name="Robot", price=10)
        self.assertEqual("Robot [RB01] : $10.00", str(product))

    def test_str_fractional_price(self):
        product = Product(id_="RB01", name="Robot", price=10.2)
        self.assertEqual("Robot [RB01] : $10.20", str(product))


if __name__ == '__main__':
    unittest.main()
