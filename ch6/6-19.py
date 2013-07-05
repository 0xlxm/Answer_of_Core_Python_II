#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Multi-Column Output.

'''
Given any number of items in a sequence or other container,
display them in equally-distributed number of columns. Let the caller provide the data
and the output format. For example, if you pass in a list of 100 items destined for
three columns, display the data in the requested format. In this case, two columns
would have 33 items while the last would have 34. You can also let the user choose
horizontal or vertical sorting.
'''

d = range(100)
while True:
    c = input('input the colmn: ') 
    row = int(round(100./c))
    flag = 0

    for i in xrange(row):
        for j in xrange(c):
            try:
                print d[i + row*j],
            except:
                print '',
        print

    if 100%c < c/2.:
        for i in xrange(c - 100%c):
            print '  ',
        #for i in range(100%c)[::-1].reverse():
        for i in range(100%c)[::-1]:
            print d[100-i - 1],

