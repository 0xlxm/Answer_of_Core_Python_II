#! /usr/bin/env python

'Judge the leap year'

def isleap(y):
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    for y in xrange(1600, 2100):
        if isleap(y):
            print y
