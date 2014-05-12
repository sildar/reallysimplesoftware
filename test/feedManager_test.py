#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
import os

# add root dir if we're on the test dir
sys.path.insert(0, os.path.dirname('..'))
# add src dir if we're on the root dir
sys.path.insert(0, os.path.dirname('./reallysimplesoftware/'))

from reallysimplesoftware import feedManager

class TestEntry(unittest.TestCase):

    def setUp(self):
        self.fakedata = {'title' : 'entrytitle',
                         'published' : '24-06-04',
                         'link' : 'http://www.fakerss.com',
                         'content' : "This is a long entry for my fake content",
        }

        self.shortdata = {'title' : 'entrytitle',
                         'published' : '24-06-04',
                         'link' : 'http://www.fakerss.com',
                         'summary' : "This is a summary of my entry",
        } 
    
    def test_fillEntry(self):
        """
        Dumb test just for setting things up
        """
        entry = feedManager.Entry(self.fakedata)
        self.assertEqual(self.fakedata['title'], entry.title)

if __name__ == '__main__':
    unittest.main()