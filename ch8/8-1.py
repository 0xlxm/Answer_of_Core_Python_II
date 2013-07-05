#! /usr/bin/env python

#

'''
Conditionals. Study the following code:
'''

def re(x):
    print 'statement A'
    if x > 0:
        print 'statement B'
        pass

    elif x < 0:
        print 'statement C'
        pass

    else:
        print 'statement D'
        pass
    print 'statement E'

#        a.
print       ' Which of the statements above (A, B, C, D, E) will be executed if x < 0?'
re(x=-1)
#       b.
print       ' Which of the statements above will be executed if x = = 0?'
re(x=0)
#        c.
print       ' Which of the statements above will be executed if x > 0?'
re(x=1)
