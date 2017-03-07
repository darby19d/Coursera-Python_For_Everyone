import urllib
import json

address = raw_input('Enter location: ')
if len(address) < 1: address = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving ', address
jsonFile = urllib.urlopen(address).read()
print 'Retrieved ',len(jsonFile),' characters'

info = json.loads(jsonFile)

print info[name,count]
print type(info)

#countList = list()

#for item in info:
    #print info['count']