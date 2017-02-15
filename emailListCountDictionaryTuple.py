name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emailDict = dict()
for line in handle: #create a dictionary with sender email addresses
    if line.startswith('From '):
        email = line.split()
        sender = email[1]
        emailDict[sender] = emailDict.get(sender,0)+1
#bigcount = None
#bigaddress = None
#for address,count in emailDict.items(): #create 2 variables and insert the highest value for the key pair
    #if bigcount is None or count > bigcount:
        #bigaddress = address
        #bigcount = count
#print bigaddress,bigcount
emailList = list()
for s,c in emailDict.items():
    emailList.append((c,s))
emailList.sort(reverse=True)
for s,c in emailList[:1]:
    print c,s
