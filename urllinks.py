# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1: url = "http://www.py4inf.com/book.htm"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
paraList = list()
# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    tag2 = tag.get('p', soup)
    paraList.append(tag2)
print len(paraList)
