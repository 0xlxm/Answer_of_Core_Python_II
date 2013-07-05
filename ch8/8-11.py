#! /usr/bin/env python

'''
Text Processing. Write a program to ask the user to input a list of names, in the
format "Last Name, First Name," i.e., last name, comma, first name. Write a function
that manages the input so that when/if the user types the names in the wrong order, i.
e., "First Name Last Name," the error is corrected, and the user is notified. This
function should also keep track of the number of input mistakes. When the user is
done, sort the list, and display the sorted names in "Last Name, First Name" order.
EXAMPLE input and output (you don't have to do it this way exactly):
    % nametrack.py
    Enter total number of names: 5
    Please enter name 0: Smith, Joe
    Please enter name 1: Mary Wong
    >> Wrong format... should be Last, First.
    >> You have done this 1 time(s) already. Fixing input. . .
    Please enter name 2: Hamilton, Gerald
    Please enter name 3: Royce, Linda
    Please enter name 4: Winston Salem
    >> Wrong format... should be Last, First.
    >> You have done this 2 time(s) already. Fixing input. . .
    The sorted list (by last name) is:
    Hamilton, Gerald
    Royce, Linda
    Salem, Winston
    Smith, Joe
    Wong, Mary

'''

import re

j = 1
names = {}

pattern = re.compile('[a-zA-Z]+, [a-zA-z]+')

num = input('Enter number of names: ')
for i in xrange(num):
    name = raw_input('please enter name %d:' % i)
    if re.match(pattern, name) != None:
        name = name.split(', ')
        names[name[1]] = name[0]
    else:
        print 'Wrong format... should be Last, First. \n You have done this %d time(s) already. Fixing input. . .' % (j); j += 1
        name = name.split()
        names[name[0]] = name[1]

for l in sorted(names):
    print '%s, %s' % (names[l], l)  
