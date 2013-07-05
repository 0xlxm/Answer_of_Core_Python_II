#! /usr/bin/env python

""" Using loops and numeric operators to get even  and odd numbers """

# no imports

def is_even(num):
    'get even or odd number'
    if num % 2 == 0:
        return True
    else:
        return False

def is_divids(num1, num2):
    'Judge if they divid'
    if num1 % num2 and num2 % num1:
        return False 
    else:
        return True

if __name__ == '__main__':
    for num in xrange(21):
        if is_even(num):
            print num, 'is even;'
        else:
            print num, 'is odd;'
    print is_divids(3, 8)
