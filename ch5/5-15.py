#! /usr/bin/env python

""" Determine the greatest common divisor and least common multiple of
a pair of integers """

import sys

def GCD_LCM(N1, N2):
    'GCD & LCM'
    if N1 <= 0 or N2 <= 0:
        return 'Wrong'

    (re, tN1, tN2) = ([], N1, N2)

    if N1 < N2:
        (N1, N2) = (N2, N1)
    while N2 != 0:
        tmp = N2
        N2 = N1 % N2
        N1 = tmp 
    re += [N1, tN1 * tN2 / N1]
    return re

if __name__ == '__main__':
    num = raw_input('enter 2 non-zero numbers N1, n2: ')
    di_num = num.split()
    if len(di_num) != 2:
        print 'Wrong input'
        sys.exit()
    re = GCD_LCM(int(di_num[0]), int(di_num[1]))
    if re == 'Wrong':
        print 'Wrong input'
    else:
        print 'GCD of', di_num[0], '&', di_num[1], ':', re[0]
        print 'LCM of', di_num[0], '&', di_num[1], ':', re[1]
