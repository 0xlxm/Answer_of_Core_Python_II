#! /usr/bin/env python

# a)
def findchr(string, char):
    for i,c in enumerate(string):
        if char == c:
            return i
        else:
            continue
    if i == len(string) - 1:
        return -1

# b)
def rfindchr(string, char):
    for i,c in enumerate(string[::-1]):
        if char == c:
            return len(string) - i - 1
        else:
            continue
    if i == len(string) - 1:
        return -1

# c)
def subchr(string, char, newchar):
    for i,c in enumerate(string):
        if char == c:
            return string[:i] + newchar + string[i+1:]
        else:
            continue
        if i == len(string) - 1:
            return -1
     
if __name__ == '__main__':
    print findchr('asdfasdf', 'f')
    print rfindchr('asdfasdf', 's')
    print subchr('asdfxyz', 'z', 'w')
