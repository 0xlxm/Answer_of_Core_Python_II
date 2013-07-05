#! /usr/bin/env python

'''
Factors. Write a function called getfactors() that takes a single integer as an
argument and returns a list of all its factors, including 1 and itself.
'''

def getfactors(num):
    if num == 1:
        return [1]
    factors = [1, num]
    count = num / 2
    while count > 1:
        if num % count == 0:
            factors.append(count)
        count -= 1
    factors.sort()
    return factors
if __name__ == '__main__':
    for n in xrange(1, 200):
        print n, getfactors(n)
    
