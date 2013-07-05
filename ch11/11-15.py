#! /usr/bin/env python

'''
11-15. *Recursion. Rewrite your solution to Exercise 6-5, which prints a string backwards to
       use recursion. Use recursion to print a string forward and backward.
'''

def printBack(s):
    printBack(s[1:])
    print s[0]

printBack('abcdefg')
