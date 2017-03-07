import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter Location: ')
if len(address) < 1 : address = 'http://python-data.dr-chuck.net/comments_42.xml'
print 'Retreiving ', address
xmlfile = urllib.urlopen(address).read()
print 'Retreived ', len(xmlfile), ' characters'

tree = ET.fromstring(xmlfile)

countList = list()

lst = tree.findall('comments/comment')
print 'comment volume: ', len(lst)
for counts in lst:
    count = int(counts[1].text)
    countList.append(count)
print sum(countList)
