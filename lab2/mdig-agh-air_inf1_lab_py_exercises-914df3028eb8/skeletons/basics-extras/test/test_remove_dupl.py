#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        filtered = remove_duplicates(['a', 2])
        self.assertEqual(2, len(filtered))
        self.assertEqual(1, filtered.count('a'))
        self.assertEqual(1, filtered.count(2))

    def test_has_duplicates(self):
        filtered = remove_duplicates(['a', 'a', 2, 2])
        self.assertEqual(2, len(filtered))
        self.assertEqual(1, filtered.count('a'))
        self.assertEqual(1, filtered.count(2))


if __name__ == '__main__':
    unittest.main()
