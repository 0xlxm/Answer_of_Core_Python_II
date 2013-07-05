#! /usr/bin/env python

'''
9-3. File Information. Prompt for a filename and display the number of lines in that text file.
'''

import os

fname = raw_input('filename: ')
if os.path.exists(fname):
    f = open(fname)
    c = f.readlines()
    f.close()
    print 'There are %d lines in %s' % (len(c), fname)
else:
    print '%s do not exist' % fname
