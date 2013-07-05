#! /usr/bin/env python

for i in xrange(3):
    print 'input Num %d :' % (i + 1),
    if i == 0:
        n1 = input()
    elif i == 1:
        n2 = input()
    else:
        n3 = input()

print n1,n2,n3

if n1 >= n2:
    n1,n2 = n2,n1
    print n1,n2,n3
if n1 >= n3:
    n1,n3 = n3,n1
    print n1,n2,n3
    print 'n1 > n3'
if n2 >= n3:
    print 'n2 > n3'
    n2,n3 = n3,n2
    print n1,n2,n3

print n1,n2,n3
