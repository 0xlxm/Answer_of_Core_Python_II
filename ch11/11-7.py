#! /usr/bin/env python

'''
11-7. Functional Programming with map(). Given a pair of identically sized lists, say [1, 2,
      3, ...], and ['abc', 'def', 'ghi', ...], merge both lists into a single list consisting
      of tuples of elements of each list so that our result looks like: {[(1, 'abc'), (2,
      'def'), (3, 'ghi'), ...}. (Although this problem is similar in nature to a problem in
      Chapter 6, there is no direct correlation between their solutions.) Then create another
      solution using the zip() built-in function.
'''

def my_may(l1, l2):
    return map(None, l1, l2)

def main():
    l1 = raw_input('Enter list 1: ').split()
    l2 = raw_input('Enter list 2: ').split()
    print my_may(l1, l2) 
    print zip(l1, l2)

if __name__ == '__main__':
    main()
