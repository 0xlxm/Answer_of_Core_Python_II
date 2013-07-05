#! /usr/bin/env python

'''
11-13. Functional Programming with reduce() and Recursion. In Chapter 8, we looked at N
       factorial or N! as the product of all numbers from 1 to N.

       a.
        Take a minute to write a small, simple function called mult(x, y) that takes x
        and y and returns their product.
       b.
        Use the mult() function you created in part (a) along with reduce() to calculate
        factorials.
       c.
        Discard the use of mult() completely and use a lambda expression instead.
       d.
        In this chapter, we presented a recursive solution to finding N! Use the timeit
        () function you completed in the problem above and time all three versions of
        your factorial function (iterative, reduce(), and recursive). Explain any
        differences in performance, anticipated and actual.
'''

import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))

# a)
def mult(x, y):
    ''' get the product of x*y '''
    return int(x) * int(y)

# b)
def reduceA(*l):
    return reduce(mult, *l)

# c)
def replaceA(*l):
    return reduce(lambda x, y: x*y, *l)

# d)
def timeit(func, *l):
    betime = time.time()
    re = func(*l)
    endtime = time.time()
    return (func.__name__, (endtime-betime) * 10e6)

def main():
    N = 500
    l = range(1, N + 1)
    for f in (reduceA, replaceA, factorial):
        if f == factorial:
            print timeit(f, N)
        else:
            print timeit(f, l)

if __name__ == '__main__':
    main()
