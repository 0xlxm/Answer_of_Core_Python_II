#! /usr/bin/env python

'integrity read and write into this python script'

import os

def write_file():
    'this function used to write to file'
    endl = os.linesep
    fc = []

    while True:
        fname = raw_input('input the filename: ')
        if os.path.exists(fname):
            print ' Error: file already exist, please try again! '
            continue
        else:
            break
    
    print 'input the content use . to quit'

    while True:
        line = raw_input('> ')
        if line == '.':
            break
        else:
            fc.append(line)

    fobj = open(fname, 'w')
    fobj.writelines('%s%s' % (cc, endl) for cc in fc)
    fobj.close()

def read_file():
    "read_file used to display the content of a specified file"
    fname = raw_input('filename to read: ')

    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** error occurs :", e
    else:
        for eachLine in fobj:
            print eachLine.strip()
    fobj.close()

def print_menu():
    print "'w' for write;"
    print "'r' for read;"
    
    choice = raw_input('your choice: ')
    if choice == 'w':
        write_file()
    elif choice == 'r':
        read_file()
    else:
        print 'invalid input'

if __name__ == '__main__':
    print write_file.__doc__
    print read_file.__doc__
    print_menu()
