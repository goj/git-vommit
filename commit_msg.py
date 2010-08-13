#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

html = urllib2.urlopen('http://whatthecommit.com/').read()
print BeautifulSoup(html).find(id='content').p.string.strip()
