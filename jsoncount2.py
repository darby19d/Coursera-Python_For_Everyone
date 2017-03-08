import urllib
import json

address = raw_input('Enter location: ')
if len(address) < 1: address = 'http://python-data.dr-chuck.net/comments_331106.json'
print 'Retrieving ', address
jsonFile = urllib.urlopen(address).read()
print 'Retrieved ',len(jsonFile),' characters'

info = json.loads(jsonFile)

#print info.items()
#print info['comments']
#print type(info['comments'])
#print len(info)

mylist = info['comments']

print 'Count: ',len(mylist)

newlist = list()

for items in mylist:
    #print items['count']
    newlist.append(int(items['count']))

print 'Sum: ',sum(newlist)