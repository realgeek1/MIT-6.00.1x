balance = 2345
annualInterestRate = 0.25

mir = annualInterestRate/12
lower = balance/12
upper = (balance * (1 + mir) ** 12) / 12
marginOfError = 0.01
minpayment = ((upper + lower) / 2)
while abs((minpayment * 12) - balance) > marginOfError:
    minpayment = (upper + lower) / 2
    
    if ((minpayment * 12) - balance) > 0:
        lower = minpayment
    else: upper = minpayment  
    
print('Lowest Payment: ' + str(minpayment))
