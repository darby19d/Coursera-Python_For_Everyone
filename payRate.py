#inputs
hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter pay rate: ")
pay = float(rate)
#standard variables
#ot = pay * 1.5
week = 40
#calculate grossPay based on regular work week and overtime
if h > week:
    #weekWork = h - week
    #weekPay = week * pay
    #weekOt = weekWork * ot
    grossPay = (week * pay) + ((h - week) * (pay * 1.5))
else: grossPay = h * pay
print grossPay
