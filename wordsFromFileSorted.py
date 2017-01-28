bookname = raw_input('Enter a file name: ')
book = open(bookname)
wordlist = list()
for line in book:
    #print line.rstrip()
    line2 = line.rstrip()
    words = line2.split()
    for words1 in words:
        #print words1
        if words1 in wordlist: continue
        wordlist.append(words1)
    #print len(wordlist)
    wordlist.sort()
print wordlist

