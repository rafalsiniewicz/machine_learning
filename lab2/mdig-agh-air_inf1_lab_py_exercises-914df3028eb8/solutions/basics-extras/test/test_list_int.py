#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import mul_if


class TestMulIf(unittest.TestCase):
    def test_all_numbers_meet_predicate(self):
        self.assertEqual(6, mul_if([1, 2, 3], lambda x: True))

    def test_some_numbers_does_not_meet_predicate(self):
        self.assertEqual(3, mul_if([1, 3, 8], lambda x: x < 5))


if __name__ == '__main__':
    unittest.main()
