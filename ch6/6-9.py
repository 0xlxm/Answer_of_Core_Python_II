#! /usr/bin/env python

while True:
    try:
        minutes = input('Enter a minutes -1 to quit: ')
        if minutes < -1:
            continue
    except:
        continue
    if -1 == minutes:
        break 
    else:
        print '%d hours and %d minutes' % (minutes//60, minutes%60) 
    
