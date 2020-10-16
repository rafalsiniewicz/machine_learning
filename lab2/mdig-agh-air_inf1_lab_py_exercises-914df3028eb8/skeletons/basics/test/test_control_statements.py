#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from skeletons.basics.control_statements import *


class MinPow2Test(unittest.TestCase):
    def test(self):
        self.assertEqual(8, min_pow_2(5))
        self.assertEqual(16, min_pow_2(8))


class ParityStrTest(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual("parzysta", parity_str(2))

    def test_is_odd(self):
        self.assertEqual("nieparzysta", parity_str(3))


class PlfTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, plf(2.99))
        self.assertEqual(1.5, plf(3))
        self.assertEqual(4, plf(10))
