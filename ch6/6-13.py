#! /usr/bin/env python

import re
import string

def atoc(str):
    rexs = re.compile(r'-?\d+\.\d+e[+-]\d+|-?\d+e[+-]\d+|-?\d+\.\d+|-?\d+')
    real_imag = rexs.findall(str)
    return complex(string.atof(real_imag[0]), string.atof(real_imag[1]))

if __name__ == '__main__':
    str = raw_input('Enter a complex string: ')
    print atoc(str)
