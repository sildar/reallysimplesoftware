#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import sqlite3
import util

class RSSThread(object):
    """
    Represents a thread.
    """
    
    def __init__(self, url):
        self.url = url
        self.entries = []
        feed = feedparser.parse(url)
        
        self.name = feed['feed']['title']
        self.updateEntries(feed)


    def nicePrint(self):
        print(self.name)
        
        for entry in self.entries:
            if not entry.isread():
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

    def __init__(self,entry):
        self._read = False
        self.title = entry['title']
        self.published = entry['published']
        self.url = entry['link']
        if 'content' in entry:
            self.content = entry['content']
        else:
            try:
                self.content = util.getMainContent(self.url)
            except:
                self.content = entry['summary']
            

    def setread(self, isread=True):
        self._read = isread

    def isread(self):
        return self._read

    def __eq__(self, other):
        sameTitle = self.title == other.title
        sameDate = self.published == other.published
        return sameTitle and sameDate        
        


def main():
    thread = RSSThread("http://www.ogaming.tv/rss.xml")
        
    thread.nicePrint()

if __name__ == "__main__":
    main()




















