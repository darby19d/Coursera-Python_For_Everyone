# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) <1: url = "http://python-data.dr-chuck.net/comments_42.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
fileComments = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'comment:',tag.get('comments', None)
    print tag.contents[0]
    #print 'Attrs:',tag.attrs
    fileComments.append(int(tag.contents[0]))
print fileComments
print sum(fileComments)
