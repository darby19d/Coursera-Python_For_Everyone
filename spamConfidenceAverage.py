# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
totalscore = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        individualscore = individualscore = line.find(':')
        individualscore = float(line[individualscore+1:])
        #print individualscore
        totalscore = totalscore + individualscore
#print totalscore
#print count
answer = totalscore / count
#print answer
print "Average spam confidence:",answer
