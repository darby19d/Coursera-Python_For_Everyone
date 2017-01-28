try:
    score = raw_input("Enter Score: ")
    scoreValue = float(score)
except:
    print "enter a number between 0.0 - 1.0"
    quit()
if scoreValue > 1.0: print "enter a number between 0.0 - 1.0"
elif scoreValue >= 0.9: print "A"
elif scoreValue >= 0.8: print "B"
elif scoreValue >= 0.7: print "C"
elif scoreValue >= 0.6: print "D"
elif scoreValue < 0.6: print "F"
