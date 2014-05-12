#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re


class NoTextException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def _isCode(text):
    """
    Predicts if the given text is composed of code
    """

    codepieces = ['+=,' '==', 'jQuery', 'var']

    for codepiece in codepieces:
        if codepiece in text:
            return True
    return False


def _isText(text, tagname='p'):
    """
    Predicts if the given text is actual natural language
    """
    text = text.strip()
    text = re.sub(' +', ' ', text)

    if _isCode(text):
        return False

    if tagname == 'p':
        minlen = 20
        minwords = 7
    else:
        minlen = 50
        minwords = 20
    if len(text) > minlen and len(text.split()) > minwords:
        return True
    return False


def getMainContent(url):
    """
    Extracts the text main content from an URL
    """
    r = requests.get(url)
    data = r.text

    soup = BeautifulSoup(data)

    result = []
    for ptag in soup.find_all(['p', 'div']):
        if _isText(ptag.text, ptag.name):
            result.append(ptag.text)

    if result == []:
        raise Exception

    return ' '.join(result)