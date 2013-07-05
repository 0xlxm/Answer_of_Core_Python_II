#! /usr/bin/env python


#for i,c in enumerate(s):
#    print i, c
#    if c == ' ':
#        s = s[0:i] + s[i+1:]
#        print s
#print s,len(s)

#s1 = ''
#for c in s:
#    if c != ' ':
#        s1 += c
#
#print s1, len(s1)

def findchar(s):
        
    isChar = False
    pos = 0
    for i,c in enumerate(s):
        if c == ' ':
            pos += 1
            continue
        else:
            return pos

if __name__ == '__main__':
    s = raw_input('enter a string with blanks: ')
    pos1 = findchar(s)
    s = s[pos1:]
    print s
    pos2 = findchar(s[::-1])
    print pos2
    s = s[:(len(s) - pos2)]
    print s, len(s)
