#!/usr/bin/python
# -*- coding: utf-8 -*-

from news_feeders import BBCNewsFeeder

reader = BBCNewsFeeder('http://feeds.bbci.co.uk/news/world/rss.xml')

for article in reader.get_feed()[0:3]:
    print(article)
