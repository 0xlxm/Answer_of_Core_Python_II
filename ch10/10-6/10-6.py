#! /usr/bin/env python

'''
10-6. Improving open(). Create a wrapper for the open() function. When a program opens a
file successfully, a file handle will be returned. If the file open fails, rather than
generating an error, return None to the callers so that they can open files without an
exception handler.
'''

import types

def myOpen(*arg):
    ''' Encapsulate open() '''
    if len(arg) == 0:
        return None
    elif len(arg) == 1:
        name = arg[0]
        mod = 'r'
        buf = -1
    elif len(arg) == 2:
        name = arg[0]
        mod = arg[1]
        buf = -1
    elif len(arg) == 3:
        name = arg[0]
        mod = arg[1]
        buf = arg[2]
    else:
        mod = 'r'
    
    try:
        f = open(name, mod, buf)
    except Exception, e:
        #return str(e)
        return None
    else:
        return f

def main():
    name = raw_input('file to open: ')
    retVal = myOpen(name)
    if retVal == None:
        print 'open %s failed!' % name
    elif type(retVal) == types.FileType:
        print 'file %s successfully opend' % name
        print 'Content as below: \n', retVal.readlines()

        retVal.close()

if __name__ == '__main__':
    main()
