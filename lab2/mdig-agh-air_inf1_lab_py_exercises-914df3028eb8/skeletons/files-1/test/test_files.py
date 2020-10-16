#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os

from files import write_to_file


class TestFiles(unittest.TestCase):
    def test_write_to_file_when_file_does_not_exist(self):
        path = "../out/data.txt"
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        self.assertFalse(write_to_file(path))

    def test_write_to_file_when_file_exists(self):
        path = "../out/data.txt"
        with open(path, 'w'):
            pass

        self.assertTrue(write_to_file(path))


if __name__ == '__main__':
    unittest.main()
