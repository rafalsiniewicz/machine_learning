#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest import mock

from news_feeders import *


class TestArticle(unittest.TestCase):
    def test_init(self):
        News("", "01 Jan 2018")
        with self.assertRaises(ValueError):
            News("", "Jan 2018")
        with self.assertRaises(ValueError):
            News("", "2 Jan 2018")
        with self.assertRaises(ValueError):
            News("", "201 Jan 2018")
        with self.assertRaises(ValueError):
            News("", "01 Ja 2018")
        with self.assertRaises(ValueError):
            News("", "01 Jan 201")
        with self.assertRaises(ValueError):
            News("", "01 Jan 2018x")

    def test_pubdate(self):
        news = News("", "01 Jan 2018")
        with self.assertRaises(ValueError):
            news.pub_date = "Jan 2018"


class TestBBCNewsFeeder(unittest.TestCase):
    def test_get_feed(self):
        with open('data/bbc_rss_sample.xml', 'r') as content_file:
            bbc_rss_sample = content_file.read()
        with mock.patch('news_feeders.urllib.request.urlopen', mock.mock_open(read_data=bbc_rss_sample)):
            bbc_feeder = BBCNewsFeeder('dummy_url')
            feed = bbc_feeder.get_feed()
            self.assertEqual(2, len(feed))
            self.assertEqual("[22 Jan 2018] Some silly news", str(feed[0]))
            self.assertEqual("[22 Jan 2018] Some funny news", str(feed[1]))


if __name__ == '__main__':
    unittest.main()
