#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from basics import append


class TestAppend(unittest.TestCase):
    def test_with_custom_argument(self):
        self.assertListEqual(["X", "hi"], append(["X"]))

    def test_with_default_argument(self):
        self.assertListEqual(["hi"], append())
        self.assertListEqual(["hi"], append())


if __name__ == '__main__':
    unittest.main()
