#! /usr/bin/env python

"""this is a calcutalor"""

import sys

def cal(N1, opr, N2):
    """N1 opr(+, -, *, /, %, **) N2"""
    if opr == '+':
        return N1 + N2
    elif opr == '-':
        return N1 - N2
    elif opr == '*':
        return N1 * N2
    elif opr == '/':
        return N1 / N2
    elif opr == '%':
        return N1 % N2
    elif opr == '**':
        return N1 ** N2
    else:
        return 'Wrong'

if __name__ == '__main__':
    expre = raw_input("Please input an expression like N1 opr(+, -, *, /, %, **) N2: ")
    expre_single = expre.split()
    if len(expre_single) != 3:
        print 'Wrong input'
        sys.exit()
    cal_re = cal(int(expre_single[0]),expre_single[1],int(expre_single[2]))
    if cal_re != 'Wrong':
        print expre, ' = ', cal_re
    else:
        print 'Wrong input'
