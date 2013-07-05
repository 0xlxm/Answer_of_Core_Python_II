#! /usr/bin/env python

'''
11-10. Functional Programming with filter(). In the Unix file system, there are always two
       special files in each folder/directory: '.' indicates the current directory and '..'
       represents the parent directory. Given this knowledge, take a look at the
       documentation for the os.listdir() function and describe what this code snippet does:
           files = filter(lambda x: x and x[0] != '.', os.
           listdir(folder))
'''

import os

def main():
    files = filter(lambda x: x and x[0] != '.', os.listdir('.'))
    print files

if __name__ == '__main__':
    main()
