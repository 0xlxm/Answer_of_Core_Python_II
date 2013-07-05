#! /usr/bin/env python

'''
11-14. *Recursion. We also looked at Fibonacci numbers in Chapter 8. Rewrite your previous
       solution for calculating Fibonacci numbers (Exercise 8-9) so that it now uses recursion.
'''

def Fibonacci(a, b, n):
    return b if n <= 0 else Fibonacci(a+b, a, n-1)

if __name__ == '__main__':
    print Fibonacci(1, 1, 5)
