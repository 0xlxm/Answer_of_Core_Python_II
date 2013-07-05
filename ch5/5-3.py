#! /usr/bin/env python

'Judge the grade of students'

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
    for n in (90, 80, 70, 60, 0):
        print Judger(n)
