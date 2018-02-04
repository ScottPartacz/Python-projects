# Scott Partacz 1/25/2018 ITMD 413 Lab 3
import time
#starting balance
account_bal = float(input("Enter an initial bank balance: "))
#interest rate for 12 months compunded monthly
rate = float(input("Include annual interest rate ( as a decimal )"))

count = 1
while(count <= 12):
    # start loop body     
    account_bal = account_bal + (rate / 12) * account_bal
    print("\nMonth: %2d    New Monthly bal: $%.2f" % (count,account_bal))
    count += 1
    # end loop body

    

print (" ")
print ("Scott Partacz")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
