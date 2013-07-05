#! /usr/bin/env python

# Home Finance

""" 
Take an opening balance and a monthly payment. Using a loop,
determine remaining balances for succeeding months, including the final payment.
"Payment 0" should just be the opening balance and schedule monthly payment
amount. The output should be in a schedule format similar to the following (the
numbers used in this example are for illustrative purposes only):
Enter opening balance:100.00
Enter monthly payment: 16.
Amount  
    Pymt# Amount Paid Remaining Balance 
    ----- ------ ---------
    0 $ 0.00 $100.00
    1 $16.13 $ 83.87
    2 $16.13 $ 67.74
    3 $16.13 $ 51.61
    4 $16.13 $ 35.48
    5 $16.13 $ 19.35
    6 $16.13 $ 3.22
    7 $ 3.22 $ 0.00
    """

import sys

def cal(re):
    tre1 = re[1]
    if re[2] < tre1:
        re[1] = re[2]
    re[0] += 1
    re[2] -= tre1
    if re[2] < 0:
        re[2] = 0
        
if __name__ == '__main__':
    balance = raw_input('Enter opening balance: ')
    payment = raw_input('Enter monthly payment: ')
    re = [int(0),float(0),float(balance)]
    print 'Pymt#    Paid    Balance'
    print '---      ------- --------'
    print "%d\t%.2f\t%.2f" % (re[0], re[1], re[2])
    re[1] = float(payment)
    while re[2] != 0:
        cal(re)
        print "%d\t%.2f\t%.2f" % (re[0], re[1], re[2])
