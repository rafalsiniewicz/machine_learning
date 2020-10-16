#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import re

from regex import *


class TestRegex(unittest.TestCase):
    def test_re_word(self):
        self.assertEqual('kXafior', re.sub(re_word(), 'X', 'kalafior'))
        self.assertEqual('Xarm', re.sub(re_word(), 'X', 'alarm'))

    def test_re_begin(self):
        self.assertEqual('kalafior', re.sub(re_begin(), 'X', 'kalafior'))
        self.assertEqual('Xarm', re.sub(re_begin(), 'X', 'alarm'))

    def test_re_end(self):
        self.assertEqual('stacja', re.sub(re_end(), 'X', 'stacja'))
        self.assertEqual('teX', re.sub(re_end(), 'X', 'test'))

    def test_re_wildchar(self):
        self.assertEqual('ala', re.sub(re_wildchar(), 'X', 'ala'))
        self.assertEqual('2 X', re.sub(re_wildchar(), 'X', '2 = 1 oraz 1'))

    def test_re_n_alnums(self):
        self.assertEqual('X i kot', re.sub(re_n_alnums(), 'X', 'pies i kot'))
        self.assertEqual('X dla X', re.sub(re_n_alnums(), 'X', 'k0dy dla mnie'))

    def test_re_binary(self):
        self.assertEqual('X', re.sub(re_binary(), 'X', '0101'))
        self.assertEqual('X9', re.sub(re_binary(), 'X', '01019'))

    def test_re_mobile(self):
        self.assertEqual('X', re.sub(re_mobile(), 'X', '601100300'))
        self.assertEqual('X', re.sub(re_mobile(), 'X', '+48601100300'))
        self.assertEqual('X', re.sub(re_mobile(), 'X', '+48 601100300'))
        self.assertEqual('X', re.sub(re_mobile(), 'X', '+48  601100300'))
        self.assertEqual('X', re.sub(re_mobile(), 'X', '+123 601100300'))
        self.assertEqual('+1 601100300', re.sub(re_mobile(), 'X', '+1 601100300'))
        self.assertEqual('+1234 601100300', re.sub(re_mobile(), 'X', '+1234 601100300'))
        self.assertEqual('6011003', re.sub(re_mobile(), 'X', '6011003'))


if __name__ == '__main__':
    unittest.main()
