#! /usr/bin/env python

'''
11-2. Functions. Combine your solutions for Exercise 5-2 such that you create a combination
      function that takes the same pair of numbers and returns both their sum and product
      at the same time.
'''

def Add_multi(a, b):
    return int(a) + int(b), int(a) * int(b)

if __name__ == '__main__':
    print Add_multi(3,4)
    print Add_multi('3','4')
