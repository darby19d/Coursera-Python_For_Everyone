import socket
from urlparse import urlparse
webAddress=raw_input('Enter a URL:')
if len(webAddress) < 1: webAddress = "http://data.pr4e.org/intro-short.txt"
website=urlparse(webAddress)
#print website.netloc
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((website.netloc, 80))
mysock.send('GET '+webAddress+' HTTP/1.0\n\n')
while True:
    data=mysock.recv(1024)
    if(len(data)<1):
        break
    print data;
mysock.close()
