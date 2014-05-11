#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:date: Created on 17 April 2014
:author: Remi Bois
"""

import feedparser
import sqlite3
from reallysimplesoftware import util

class RSSThread(object):
    """
    Represents a RSS thread.
    """
    
    def __init__(self, url):
        """
        Reads a RSS feed and updates the thread entries.

        Arguments:

            url
                The URL to fetch to get the feed
        """
        self.url = url
        self.entries = []
        feed = feedparser.parse(url)
        
        self.name = feed['feed']['title']
        self.updateEntries(feed)


    def nicePrint(self):
        print(self.name)
        
        for entry in self.entries:
            if not entry.read:
                print("\t" + entry.title + '\t' + entry.published)
                print("\t\t" + str(entry.content) + "\n\n")

    def updateEntries(self, feed):
        if self.entries == None:
            self.entries = feed['entries']
        else:
            for entry in feed['entries']:
                if not entry in self.entries:
                    self.entries.append(Entry(entry))

class Entry(object):
    """
    Represents a RSS entry. A single web page.
    """

    def __init__(self, entrydata):
        """
        Stocks content of a single entry of a RSS feed.

        Arguments:

            entrydata
                The data from the RSS feed.
        """
        self.read = False
        self._fillEntry(entrydata)
        
    def _fillEntry(self, entrydata):
        self.title = entrydata['title']
        self.published = entrydata['published']
        self.url = entrydata['link']
        if 'content' in entrydata:
            self.content = entrydata['content']
        else:
            try:
                self.content = util.getMainContent(self.url)
            except:
                self.content = entrydata['summary']


    def __eq__(self, other):
        sameTitle = self.title == other.title
        sameDate = self.published == other.published
        return sameTitle and sameDate        
        


def main():
    thread = RSSThread("http://www.ogaming.tv/rss.xml")
        
    thread.nicePrint()

if __name__ == "__main__":
    main()




















