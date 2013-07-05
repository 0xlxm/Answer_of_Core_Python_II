#! /usr/bin/env python

'''
11-4. Return Values. Create a complementary function to your solution for Exercise 5-13.
      Create a function that takes a total time in minutes and returns the equivalent in
      hours and minutes.
'''

def my_time(min):
    ''' min -> H:M '''
    return str(min//60) + ':' + str(min%60)

def main():
    min = input('enter the total minutes: ')
    print my_time(min)

if __name__ == '__main__':
    main()
