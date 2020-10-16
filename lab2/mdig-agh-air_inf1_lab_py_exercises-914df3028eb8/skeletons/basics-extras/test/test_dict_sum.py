#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import sum_values


class TestSumValues(unittest.TestCase):
    def test_logic(self):
        my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
        self.assertEqual(6, sum_values(my_dict))

    def test_empty_dict(self):
        self.assertEqual(0, sum_values({}))


if __name__ == '__main__':
    unittest.main()
