#! /usr/bin/env python

'''
Prime Numbers. We presented some code in this chapter to determine a number's
largest factor or if it is prime. Turn this code into a Boolean function called isprime()
such that the input is a single value, and the result returned is true if the number is
prime and False otherwise.

example 8.1:

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % (num, count)
            break
        count -= 1
    else:
        print num, "is prime"

for eachNum in range(10, 21):
    showMaxFactor(eachNum)
'''

import math

def isprime(num):
    #count = num / 2
    count = int(math.sqrt(num))
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True

if __name__ == '__main__':
    #while True:
    #    n = input('enter a number: ')
    for n in range(2, 100):
        if isprime(n):
            print n,
    print 


