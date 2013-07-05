#! /usr/bin/env python

'''
9-4. File Access. Write a "pager" program. Your solution should prompt for a filename, and
display the text file 25 lines at a time, pausing each time to ask the user to "press a
key to continue."
'''

import os

i = 0
fname = raw_input('filename: ')
if os.path.exists(fname):
    f = open(fname)
    # solution 1
    while True:
        try:
            for l in f:
                if i % 25 == 0 and i != 0:
                    #raw_input('press anykey to continue: ')
                    os.system('read -n 1 -p "Press any key to continue\n" > /dev/null')
                print l,
                i += 1
            f.next()
        except StopIteration, IOError:
            f.close()
            break

# solution 2
    #c = f.readlines()
    #f.close()
    #l = len(c)
    #for i in xrange(l):
    #    if i != 0 and i % 25 == 0:
    #        os.system('read -n 1 -p "Press any key to continue" > /dev/null')
    #    print c[i],
else:
    print '%s do not exist' % fname
