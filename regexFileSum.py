import re
name = raw_input("Enter file:")
if len(name) < 1: name = "regex_sum_331100.txt"
handle = open(name)
numberList = list()
for line in handle:
    line = line.rstrip()
    stringList = re.findall('[0-9]+' , line)
    #if len(stringList) > 0:
        #print stringList
    for item in stringList:
         item = int(item)
         numberList.append(item)
print sum(numberList)
