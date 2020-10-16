#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import filter_pesels_by_name_initial


class TestFilterPeselsByNameInitial(unittest.TestCase):
    def test_no_name_with_given_initial(self):
        people = {
            "0": "Adam Abacki",
            "1": "Bogdan Babacki"
        }
        self.assertListEqual([], filter_pesels_by_name_initial(people, 'C'))

    def test_one_name_with_given_initial(self):
        people = {
            "0": "Adam Abacki",
            "1": "Bogdan Babacki"
        }
        self.assertListEqual(["0"], filter_pesels_by_name_initial(people, 'A'))

    def test_multiple_names_with_given_initial(self):
        people = {
            "0": "Adam Abacki",
            "1": "Bogdan Babacki",
            "2": "Alfred Abacki"
        }
        pesels = filter_pesels_by_name_initial(people, 'A')
        self.assertEqual(2, len(pesels))
        self.assertEqual(1, pesels.count("0"))
        self.assertEqual(1, pesels.count("2"))


if __name__ == '__main__':
    unittest.main()
