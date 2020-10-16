#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import min_max


class TestFuncArgRet(unittest.TestCase):
    def test_without_limit(self):
        result = min_max([1, 5])
        self.assertEqual(1, result.min)
        self.assertEqual(5, result.max)

    def test_with_limit(self):
        result = min_max([1, 5], upper_limit=3)
        self.assertEqual(1, result.min)
        self.assertEqual(3, result.max)

    def test_ints_and_floats(self):
        result = min_max([1, 5, 3.4])
        self.assertEqual(1, result.min)
        self.assertEqual(5, result.max)


if __name__ == '__main__':
    unittest.main()
