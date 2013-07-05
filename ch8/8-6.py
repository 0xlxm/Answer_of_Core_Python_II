#! /usr/bin/env python

'''
Factors. Write a function called getfactors() that takes a single integer as an
argument and returns a list of all its factors, including 1 and itself.
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
def primelist(l):
    return [n for n in l if isprime(n)]

def getprimefactors(num):
    if num == 1:
        return [1]
    if isprime(num):
        return [num]

    factors = []
    product = 1
    count = num / 2

    while count > 1:
        if num % count == 0:
            factors.append(count)
        count -= 1
    factors = primelist(factors)
    if factors == [2]:
        return [2] * int(math.log(num, 2))
    for f in factors:
        product *= f
    if product != num:
        factors.append(int(num/product))
    #factors.sort()
    return sorted(factors)

if __name__ == '__main__':
    for n in xrange(1, 21):
        print n, getprimefactors(n)
    
