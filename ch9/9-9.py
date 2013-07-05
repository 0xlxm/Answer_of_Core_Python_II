#! /usr/bin/env python

'''
"PythonDoc." Go to the directory where your Python standard library modules are
located. Examine each .py file and determine whether a __doc__ string is available for
that module. If so, format it properly and catalog it. When your program has
completed, it should present a nice list of those modules that have documentation
strings and what they are. There should be a trailing list showing which modules do
not have documentation strings (the shame list). Extra credit: Extract documentation
for all classes and functions within the standard library modules.
'''

import os

def print_doc(libdir):
    modnames = []
    os.chdir(libdir)
    modfiles = os.listdir('.')
    for f in modfiles:
        try:
            if f.endswith('py') or os.path.isdir(f):
                f_e = os.path.splitext(f)
                mo = __import__(f_e[0])
                if '__doc__' in mo.__dict__ and mo.__dict__['__doc__'] is not None:
                    print '__doc__ of module: %s' % f_e[0]
                    print `mo.__dict__['__doc__']`,'\n'
                else:
                    modnames.append(f_e[0])
        except:
            print 'error on module %s' % f_e[0]
            continue
    print 'Following modules have no doc: '
    print modnames


libdir = '/usr/lib/python2.4/'
#libdir = raw_input('enter the path of standard library modules: ')
#if os.path.isdir(libdir):
print_doc(libdir)
#else:
#    print 'it is not a directory'

