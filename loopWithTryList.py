numList = list()
while True:
    num = raw_input("Enter a number: ")
    if num == "done": break
    try:
        entry = int(num) #convert from input (string) to integer
    except:
        print "Invalid input"
        continue
    if num not in numList:
        numList.append(num)
print 'Maximum is', max(numList)
print 'Minimum is', min(numList)
