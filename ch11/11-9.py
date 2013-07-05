#! /usr/bi/env python

'''
11-9. Functional Programming with reduce(). Review the code in Section 11.7.2 that
      illustrated how to sum up a set of numbers using reduce(). Modify it to create a new
      function called average() that calculates the simple average of a set of numbers.
'''

def average(s):
    return reduce(lambda x, y: x + y, s) / float(len(s)) 

def main():
    s = frozenset((1,2,3,4,5,10))
    print average(s)

if __name__ == '__main__':
    main()
