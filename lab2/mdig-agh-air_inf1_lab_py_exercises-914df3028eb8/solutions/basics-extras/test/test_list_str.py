#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import count_if


class TestCountIf(unittest.TestCase):
    def test_too_short(self):
        self.assertEqual(0, count_if(['a']))

    def test_contains_prefix(self):
        self.assertEqual(1, count_if(['army', 'bull']))

    def test_contains_palindrome(self):
        self.assertEqual(1, count_if(['eye', 'bull']))

    def test_contains_two_correct_words(self):
        self.assertEqual(2, count_if(['eye', 'army']))


if __name__ == '__main__':
    unittest.main()
