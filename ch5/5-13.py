#! /usr/bin/env python

#

import sys

""" take a time period measured in hours and
minutes and return the total time in minutes only"""

def minutes(time):
    ''' return minutes of the given time '''
    di_time = time.split(':')
    if len(di_time) != 2:
        return 'Wrong'
    else:
        return int(di_time[0]) * 60 + int(di_time[1])

if __name__ == '__main__':
    time = raw_input('enter a time like (Hour:Min): ')
    re = minutes(time)
    if re == 'Wrong':
        print 'Wrong input'
        sys.exit()
    print time, 'equal', re, 'minutes'
