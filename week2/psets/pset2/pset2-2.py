#balance = 3322
#annualInterestRate = 0.24

testbalance = balance
mir = annualInterestRate/12
x = 10
while True:
    testbalance = balance
    for i in range(1,13):
        testbalance -= x
        testbalance += testbalance *mir
    if testbalance <= 0:
        break 
    else: x += 10 
print 'Lowest Payment: ' + str(x)