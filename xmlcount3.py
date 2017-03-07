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
for item in lst:
    print 'Name: ', item.find('name').text
    print 'Count: ', item.find('count').text
    countList.append(int(item.find('count').text))
print 'Sum of Count: ', sum(countList)