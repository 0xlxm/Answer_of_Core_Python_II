#! /usr/bin/env python

'''
9-15. Copying Files. Prompt for two filenames (or better yet, use command-line arguments).
      The contents of the first file should be copied to the second file.
'''

# resolution 1,
import os

def cpfile(src, dest):
    ''' copy file from src to dest '''
    try:
        fs = open(src, 'r')
        fd = open(dest, 'w')
        slines = fs.readlines()
    except IOError, e:
        print 'Error occured,', e
    else:
        #for line in slines:
            fd.writelines(slines)
    finally:
        fs.close()
        fd.close()

def main():
    ''' main function '''
    while True:
        srcf = raw_input('Please enter the source file name: ')
        if not os.path.exists(srcf):
            print '%s doesn\'t exist, try again.' % (srcf)
            continue
        else:
            desf = raw_input('Please enter the dest file name: ')
            break

    cpfile(srcf, desf)

if __name__ == '__main__':
    main()

# resolution 2:
#import shutil
#
#src  = raw_input('enter source filename: ')
#dst  = raw_input('enter dest filename: ')

#shutil.copyfile(src, dst)
