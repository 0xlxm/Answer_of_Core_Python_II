
#! /usr/bin/env python

'Judge the grade of students'

import os

def Judger(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 100:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    if grade < 60:
        return 'F'

if __name__ == '__main__':
    fn = raw_input('filename that hold the greads: ')
    if os.path.exists(fn):
        f = open(fn)
        for l in f:
            print l, Judger(int(l))
    else:
        print '%s do not exist' % fn

