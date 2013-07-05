#! /usr/bin/env python

'''
9-20. Compressed Files. Write a short piece of code that will compress and decompress
gzipped or bzipped files. Confirm your solution works by using the command-line gzip
or bzip2 programs or a GUI program like PowerArchiver, StuffIt, and/or WinZip.
'''

import gzip, bz2

def menu():
    prompt = '''
(Q)uit
(C)ompress
(D)compress

Your choice: '''
    
    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
                print '\nYou picked: [%s]' % choice
                if choice not in 'cd':
                    print 'invalid option, try again'
                else:
                    chosen = True
        
    if choice == 'c': compress()
    if choice == 'd': decompress()
    if choice == 'q': done = True

def compress():
    srcfile = raw_input('enter the file you want to compress: ')
    try:
        f = open(srcfile, 'r')
    except IOError, e:
        print e
        return
    else:
        dstfile = raw_input('enter the dst file: ')
        f_c = gzip.open(dstfile, 'wb')
        f_c.writelines(f)
        f_c.close()
        f.close()

def decompress():

    pass

def main():
    pass

if __name__ == '__main__':
    main()
