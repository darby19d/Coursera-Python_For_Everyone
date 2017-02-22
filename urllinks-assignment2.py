import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
urlCount = raw_input('Enter count: ')
urlCount = int(urlCount) + 1
urlPosition = raw_input('Enter position: ')
urlPosition = int(urlPosition) - 1
while urlCount > 0:
    print url
    urlList = list()
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        url2 = tag.get('href', None)
        if url2 in urlList: continue
        else: urlList.append(url2)
    urlCount = urlCount - 1
    url = urlList[urlPosition]
