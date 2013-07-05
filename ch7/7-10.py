#! /usr/bin/env python

def rot13(s):
    l_str = list(s)
    for i, c in enumerate(l_str):
        if 'a' <= c <= 'z':
            l_str[i] = chr((ord(c) - 97 + 13) % 26 + 97)
        elif 'A' <= c <= 'Z':
            l_str[i] = chr((ord(c) - 65 + 13) % 26 + 65)
        else:
            continue
    return ''.join([c for c in l_str])

if __name__ == '__main__':
    plain = raw_input('Enter to rot13: ')
    print 'your stringto en/decrypt was: [%s].' % plain
    print 'The rot13 string is: [%s].' % rot13(plain)
    
