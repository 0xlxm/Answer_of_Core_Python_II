#! /usr/bin/env python

'''
10-7. Exceptions. What is the difference between Python pseudocode snippets (a) and (b)?
Answer in the context of statements A and B, which are part of both pieces of code.
(Thanks to Guido for this teaser!)
(a) try:
    statement_A
    except . . .:
        . . .
    else:
        statement_B
        (b) try:
            statement_A
            statement_B
    except . . .:
        . . .
'''

def fa():
    try:
        print 'statement_A'
    except Exception, e:
        print str(e)
    else:
        print 'statement_B'
        #open('file_do_not_exist')

def fb():
    try:
        print 'statement_A'
        print 'statement_B'
        open('file_do_not_exist')
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    fa()
    fb()
