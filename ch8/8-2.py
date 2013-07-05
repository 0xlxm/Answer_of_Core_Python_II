#! /usr/bin/env python

'''
Loops. Write a program to have the user input three (3) numbers: (f)rom, (t)o, and (i)
ncrement. Count from f to t in increments of i, inclusive of f and t. For example, if the
input is f == 2, t == 26, and i == 4, the program would output: 2, 6, 10, 14, 18, 22,
26.
'''

f = input('enter from: ')
t = input('enter to: ')
i = input('enter increment: ')

print 'solution 1: for'
for n in xrange(f, t+1, i):
    print n,
print '\n'

print 'solution 2: while'
while f <= t:
    print f,
    f += i
print

