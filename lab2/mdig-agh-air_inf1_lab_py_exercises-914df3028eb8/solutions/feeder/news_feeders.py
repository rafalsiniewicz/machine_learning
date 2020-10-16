#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import List

# ---

import urllib.request
import xml.etree.ElementTree
import re


class News:
    """Nowinka.

    Atrybuty:
        title (str): tytuł nowinki
        pub_date (str): data nowinki w formacie "DD Mmm YYYY" (np. "01 Jan 2018")
            Próba ustawienia źle sformatowanej daty powinna skutkować błędem typu ValueError.
            Poprawna data składa się z ciągu:
                "<2x cyfra> <duża litera><2x mała litera> <4x cyfra>"

    Reprezentacja tekstowa:
        "[DD Mmm YYYY] <tytuł>"
    """

    # FIXME (szkielet): TODO: zaimplementuj...
    # pass

    def __init__(self, title: str, pub_date: str):
        self.title = title
        self.pub_date = pub_date

    @property
    def pub_date(self) -> str:
        return self.__pub_date

    @pub_date.setter
    def pub_date(self, pub_date: str) -> None:
        re_pubdate = r'\d{2} [A-Z][a-z]{2} \d{4}'
        if not re.fullmatch(re_pubdate, pub_date):
            raise ValueError("Incorrect date format: ", pub_date)
        self.__pub_date = pub_date

    def __str__(self) -> str:
        return '[{self.pub_date}] {self.title}'.format(self=self)


class NewsFeeder(ABC):
    """Klasa dostarczająca zestawienia nowinek ze strumienia RSS.

    Atrybuty:
        rss_url (str): URL strony zawierającej strumień RSS
    """

    def __init__(self, rss_url: str, *args, **kwargs) -> None:
        """
        Parametry:
         rss_url -- URL strony zawierającej strumień RSS
        """
        self.rss_url = rss_url

    @abstractmethod
    def get_feed(self) -> List[News]:
        """Zwróć listę artykułów ze strumienia RSS.
        """
        raise NotImplementedError


class BBCNewsFeeder(NewsFeeder):
    def __init__(self, rss_url: str, *args, **kwargs) -> None:
        super().__init__(rss_url, *args, **kwargs)

    def get_feed(self) -> List[News]:
        with urllib.request.urlopen(self.rss_url) as response:
            xml_str = response.read()

        root = xml.etree.ElementTree.fromstring(xml_str)
        channel = root.find('channel')
        articles = []
        for item in channel.findall('item'):
            title = item.find('title').text
            pub_date = self.parse_pubdate(item.find('pubDate').text)
            articles.append(News(title=title, pub_date=pub_date))
        return articles

    @classmethod
    def parse_pubdate(cls, pubdate: str) -> str:
        return pubdate[5:16]
