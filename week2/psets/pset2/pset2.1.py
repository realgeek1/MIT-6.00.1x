#Bank account only min monthly payment paid

balance = float(input('What is the balance? '))
monthlyPaymentRate = float(input('What is the percentage of minimum monthly payment? '))
annualInterestRate = float(input('What is the APR? '))


mir = annualInterestRate/12
months = 12
paid = 0
for i in range(1,months+1):
    print('Month: ' + str(i))
    mmp = balance*monthlyPaymentRate
    print('Minimum monthly payment: ' + str(round(mmp, 2)))
    paid += mmp
    balance -= mmp
    balance += balance * mir
    print('Remaining balance: ' + str(round(balance, 2)))
print('Total paid: ' + str(round(paid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
