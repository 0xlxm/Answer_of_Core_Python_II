#! /usr/bin/env python

'''
9-18. Searching Files. Obtain a byte value (0-255) and a filename. Display the number of
times that byte appears in the file.
'''

def searchar(content, char):
    '''
    search all chars in content which should the content of the file
    and return the numbers of char 
    '''
# common resolution
    #num = 0
    #sc = ''.join(content)
    #for c in sc:
    #    if c == char:
    #        num += 1

    #return num
    return len([c for l in content for c in l if c == char])

def main():
    ''' main '''
    fname = raw_input('enter the file to search: ')

    try:
        f = open(fname, 'r')
        content = f.readlines()
    except IOError, e:
        print e
    else:    
        char = raw_input('enter the char to search: ')
        print searchar(content, char)

if __name__ == '__main__':
    main()
