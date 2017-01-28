name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emailDict = dict()
for line in handle:
    if line.startswith('From '):
        email = line.split()
        sender = email[5]
        hour = sender.find(':')
        hour = sender[:hour]
        emailDict[hour] = emailDict.get(hour,0)+1
#print emailDict
#for (k,v) in emailDict.items():
    #print k,v
#emailHours = sorted(emailDict.items())
#emailHours.sort()
#print emailHours
for k,v in sorted(emailDict.items()):
    print k,v
