name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emailDict = dict()
emailList = list()
for line in handle: #create a list with sender email addresses
    if line.startswith('From '):
        email = line.split()
        sender = email[1]
        emailList.append(sender)
#print emailList
for address in emailList: #add sender from list into a dictionary
    #if address not in emailDict:
        #emailDict[address] = 1
    #else:
        #emailDict[address] = emailDict[address] + 1
    emailDict[address] = emailDict.get(address,0)+1
#print emailDict
#for aaa,bbb in emailDict.items():
    #print aaa,bbb
bigcount = None
bigaddress = None
for address,count in emailDict.items(): #create 2 variables and insert the highest value for the key pair
    if bigcount is None or count > bigcount:
        bigaddress = address
        bigcount = count
print bigaddress,bigcount
