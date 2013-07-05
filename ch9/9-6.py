#! /usr/bin/env python

'''
9-6. File Comparison. Write a program to compare two text files. If they are different, give
the line and column numbers in the files where the first difference occurs.
'''

fn1 = raw_input('file1: ')
fn2 = raw_input('file2: ')

c1 = open(fn1).readlines()
c2 = open(fn2).readlines()

l1 = len(c1)
l2 = len(c2)

same = False
row = column = 0

for i in xrange(min(l1, l2)):
    if c1[i] == c2[i]:
        same = True
        continue
    else:
        same = False
        row = i
        minline = min(len(c1[i]), len(c2[i]))
        for j in xrange(min(len(c1[i]), len(c2[i]))):
            if c1[i][j] == c2[i][j]:
                continue
            else:
                column = j
        break

if same:
    print '%s and %s are different at row %d, column %d.' % (fn1 ,fn2, max(l1, l2), 1) 
else:
    print '%s and %s are different at row %d, column %d.' % (fn1 ,fn2, row + 1, column + 1)
