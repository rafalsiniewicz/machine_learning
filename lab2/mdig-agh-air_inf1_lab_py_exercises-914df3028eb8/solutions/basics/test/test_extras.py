#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from extras import *


class GetUniqueLettersTest(unittest.TestCase):
    def test_less_than_3_unique_letters(self):
        self.assertSetEqual(set(), get_unique_letters('ah'))

    def test_at_least_3_unique_letters(self):
        self.assertSetEqual({'k', 'a', 'y'}, get_unique_letters('kayak'))


class ProductsToBuyTest(unittest.TestCase):
    def test(self):
        list1 = {"apple": 1, "orange": 5, "eggs": 1}
        list2 = {"banana": 3, "apple": 1, "orange": 4}
        self.assertSetEqual({'apple', 'orange', 'eggs', 'banana'},
                            products_to_buy(list1, list2))


class ProductsOnlyOnOneListTest(unittest.TestCase):
    def test_disjoint_sets(self):
        list1 = {"eggs": 1}
        list2 = {"banana": 3}
        self.assertEqual(2, products_only_on_one_list(list1, list2))

    def test_overlapping_sets(self):
        list1 = {"apple": 1, "orange": 5, "eggs": 1}
        list2 = {"banana": 3, "apple": 1, "orange": 4}
        self.assertEqual(2, products_only_on_one_list(list1, list2))


class TwoDiceRollsCombinationsTest(unittest.TestCase):
    def test(self):
        self.assertDictEqual(
            {2: {(1, 1)}, 3: {(1, 2), (2, 1)}, 4: {(1, 3), (3, 1), (2, 2)}, 5: {(3, 2), (2, 3), (4, 1), (1, 4)},
             6: {(5, 1), (3, 3), (1, 5), (4, 2), (2, 4)}, 7: {(6, 1), (5, 2), (1, 6), (4, 3), (2, 5), (3, 4)},
             8: {(3, 5), (2, 6), (4, 4), (6, 2), (5, 3)}, 9: {(4, 5), (5, 4), (6, 3), (3, 6)},
             10: {(6, 4), (5, 5), (4, 6)}, 11: {(5, 6), (6, 5)}, 12: {(6, 6)}},
            two_dice_rolls_combinations()
        )


class IntsToStrTest(unittest.TestCase):
    def test_no_elements(self):
        self.assertEqual('', ints_to_str([]))

    def test_one_element(self):
        self.assertEqual('1', ints_to_str([1]))

    def test_multiple_elements(self):
        self.assertEqual('12', ints_to_str([1, 2]))


class IntsToStrMaxLengthTest(unittest.TestCase):
    def test_default_limit(self):
        self.assertEqual('12', ints_to_str_max_length([1, 2]))

    def test_limit_no_trimming(self):
        self.assertEqual('12', ints_to_str_max_length([1, 2], max_length=2))

    def test_limit_trimming(self):
        self.assertEqual('1', ints_to_str_max_length([1, 2], max_length=1))


class DivisionGuardianTest(unittest.TestCase):
    def test_y_equals_zero(self):
        self.assertFalse(division_guardian(1, 0))

    def test_x_per_y_smaller_than_1(self):
        self.assertFalse(division_guardian(1.00, 1.01))

    def test_x_per_y_greater_than_1(self):
        self.assertTrue(division_guardian(1.01, 1.00))
