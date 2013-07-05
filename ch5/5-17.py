#! /usr/bin/env python

# Random Numbers.

'''
Read up on the random module and do the following problem:
Generate a list of a random number (1 < N <= 100) of random numbers (0 <= n <=
231-1). Then randomly select a set of these numbers (1 <= N <= 100), sort them, and
display this subset.
'''

import sys
import random

list = []
list_sort = []
N1 = random.randint(2, 100)
print 'generate', N1, 'n;'

for i in xrange(N1):
   list.append(random.randrange(2**31)) 
   print 'generate list[%d]: %d' % (i, list[i])
print list

N2 = random.randint(1, N1)
print '\nslect N2 %d numbers from list;' % N2
for i in xrange(N2):
    pos = random.randint(1, N2)
    print 'selcet list[%d]: %d' % (pos, list[pos])
    list_sort.append(list[pos]) 
print list_sort
list_sort.sort()
print list_sort
