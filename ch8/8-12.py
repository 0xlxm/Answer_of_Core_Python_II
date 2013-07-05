#! /usr/bin/env python

'''
(Integer) Bit Operators. Write a program that takes begin and end values and prints
out a decimal, binary, octal, hexadecimal chart like the one shown below. If any of the
characters are printable ASCII characters, then print those, too. If none is, you may
omit the ASCII column header.
SAMPLE OUTPUT 1
---------------
Enter begin value: 9
Enter end value: 18
DEC BIN OCT HEX
-------------------------------
9 01001 11 9
10 01010 12 a
11 01011 13 b
12 01100 14 c
13 01101 15 d
14 01110 16 e
15 01111 17 f
16 10000 20 10
17 10001 21 11
18 10010 22 12
SAMPLE OUTPUT 2
---------------
Enter begin value: 26
Enter end value: 41
DEC BIN OCT HEX ASCII
----------------------------------------
26 011010 32 1a
27 011011 33 1b
28 011100 34 1c
29 011101 35 1d
30 011110 36 1e
31 011111 37 1f
32 100000 40 20
33 100001 41 21 !
34 100010 42 22 '
35 100011 43 23 #
36 100100 44 24 $
37 100101 45 25 %
38 100110 46 26 &
39 100111 47 27 '
40 101000 50 28 (
41 101001 51 29 )
'''

import string

values = []
ascii = {} 

def bin(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    return s

def printable():
    begin = input('Enter begin value: ')
    end = input('Enter end value: ')

    for n in xrange(begin, end + 1):
        if chr(n) in string.printable:
            ascii[n] = chr(n)
        else:
            #ascii.append('')
            continue
    ASC = '\tASCII' if len(ascii) != 0 else ''
    _num = 32 if ASC == '' else 40

    print 'DEC\tBIN\tOCT\tHEX', ASC
    print '-'*_num

    for n in xrange(begin, end + 1):
        #binary = eval(bin(n)[2:])
        print '%d\t%d\t%o\t%x\t' % (n, eval(bin(n)), n, n),
        if len(ascii) != 0 and n in ascii:
            print '%s' % repr(ascii[n])
        else:
            print

if __name__ == '__main__':
    printable()
