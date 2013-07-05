#! /usr/bin/env python

'''
11-8. Functional Programming with filter(). Use the code you created for Exercise 5-4 to
      determine leap years. Update your code so that it is a function if you have not done so
      already. Then write some code to take a list of years and return a list of only leap
      years. Then convert it to using list comprehensions.
'''

def isleap(y):
    'Judge the leap year'
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

def main():
    print 'Result from filter', filter(isleap, range(2000, 2020))
    print 'Result from filter', filter(lambda y: (y % 400 == 0 or y % 4 == 0 and y % 100 != 0), range(2000, 2020))
    print 'Result from list comprehensions', [y for y in range(2000, 2020) if isleap(y)]
    
if __name__ == '__main__':
    main()
