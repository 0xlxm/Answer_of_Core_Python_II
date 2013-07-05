#! /usr/bin/evn python

'''
i9-2. File Access. Prompt for a number N and file F, and display the first N lines of F.
'''

import os

def print_F(F, N):
    f = open(F)
    c = f.readlines()
    f.close()
    l = len(c)
    
    if N > l:
        print 'There are %d lines in all in the fle.' % l
        return

    for i in xrange(N):
        print c[i],

if __name__ == '__main__':
    F = raw_input('filename: ')
    N = input('rows want to display: ')
    if os.path.exists(F):
        print_F(F, N)
    else:
        print F, 'do not exist'

