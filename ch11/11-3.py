#! /usr/bin/env python

'''
11-3. Functions. In this exercise, we will be implementing the max() and min() built-in
      functions.

      a.
          Write simple functions max2() and min2() that take two items and return the
          larger and smaller item, respectively. They should work on arbitrary Python
          objects. For example, max2(4, 8) and min2(4, 8) would each return 8 and 4,
          respectively.
      b.
          Create new functions my_max() and my_min() that use your solutions in part (a)
          to recreate max() and min(). These functions return the largest and smallest
          item of non-empty sequences, respectively. They can also take a set of
          arguments as input. Test your solutions for numbers and strings.
'''

def max2(a, b):
    if a > b:
        return a
    else:
        return b

def min2(a, b):
    if a < b:
        return a
    else:
        return b

def my_max(s):
    maxnum = s[0]
    for i in xrange(len(s) - 1):
        tmpmax = max2(s[i], s[i+1])
        if maxnum < tmpmax:
            maxnum = tmpmax
    return maxnum

def my_min(s):
    minnum = s[0]
    for i in xrange(len(s) - 1):
        tmpmin = min2(s[i], s[i+1])
        if minnum > tmpmin:
            minnum = tmpmin
    return minnum

def main():
    s = [1, 7, 2, 9, 11, 0, 99, -1]
    print my_max(s)
    print my_min(s)

if __name__ == '__main__':
    main()
