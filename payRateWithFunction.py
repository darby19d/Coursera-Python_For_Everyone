def computepay(h,r):
    if h <= 40: Pay = h * r
    elif h> 40: Pay = (40 * r) + ((h - 40) * (r * 1.5))
    return Pay
try:
    hrs = raw_input("Enter Hours: ")
    rate = raw_input("Enter Pay Rate: ")
    h = float(hrs)
    r = float(rate)
except:
    print "Please enter numbers only"
    quit()
p = computepay(h,r)
print "Pay",p
