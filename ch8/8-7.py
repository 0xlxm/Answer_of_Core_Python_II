#! /usr/bin/env python

'''
Perfect Numbers. A perfect number is one whose factors (except itself) sum to itself.
For example, the factors of 6 are 1, 2, 3, and 6. Since 1 + 2 + 3 is 6, it (6) is
considered a perfect number. Write a function called isperfect() which takes a single
integer input and outputs 1 if the number is perfect and 0 otherwise.
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

def isperfectnumber(num):
    factors = []
    product = 0
    count = num / 2

    while count >= 1:
        if num % count == 0:
            factors.append(count)
        count -= 1
    for f in factors:
        product += f
    if product == num:
        print factors
        return True
    else:
        return False

if __name__ == '__main__':
    for n in xrange(2, 1001):
        if isperfectnumber(n):
            print n
