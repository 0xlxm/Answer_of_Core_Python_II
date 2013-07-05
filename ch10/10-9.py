#! /usr/bin/env python

'''
10-9. Improving math.sqrt(). The math module contains many functions and some constants
      for performing various mathematics-related operations. Unfortunately, this module
      does not recognize or operate on complex numbers, which is the reason why the cmath
      module was developed. Create a function, perhaps safe_sqrt(), which wraps math.sqrt
      (), but is smart enough to handle a negative parameter and return a complex number
      with the correct value back to the caller.
'''

import cmath, math

def safe_sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return cmath.sqrt(x)

def main():
    while True:
        try:
            x = input('enter a number to test safe_sqrt(Ctrl C to quit): ')
        except NameError, e:
            print str(e) + '\nplease try again!'
        except KeyboardInterrupt, e:
            print '\nCtrl + C received; exit ... '
            break
        else:
            print safe_sqrt(x)

if __name__ == '__main__':
    main()
