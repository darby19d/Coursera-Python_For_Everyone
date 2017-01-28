# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for answer in fh:
    answer = answer.rstrip()
    #answer = fh.read()
    print answer.upper()
