#! /usr/bin/env python


'''
Factorial. The factorial of a number is defined as the product of all values from one to
that number. A shorthand for N factorial is N! where N! == factorial(N) == 1 * 2 * 3
* ... * (N-2) * (N-1) * N. So 4! == 1 * 2 * 3 * 4. Write a routine such that given N, the
value N! is returned.
'''

def Factorial(num):
    product = 1
    for n in xrange(1, num + 1):
        product *= n
    return product

if __name__ == '__main__':
    for n in xrange(1, 20):
        print '%d! = %d ' % (n, Factorial(n))
