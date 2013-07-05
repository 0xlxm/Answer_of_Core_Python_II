#! /usr/bin/env python

# Creating Dictionaries.

'''
Given a pair of identically sized lists, say, [1, 2, 3,...], and
['abc', 'def', 'ghi',...], process all that list data into a single dictionary that looks
like: { 1:'abc', 2:'def', 3:'ghi',...}.
'''

def dict_a_b(a, b):
    return dict(zip(a, b))

if __name__ == '__main__':
    d1 = raw_input('enter first list: ').split()
    d2 = raw_input('enter second list: ').split()
    if len(d1) != len(d2):
        print 'length of d1 and d2 is not the same'
    else:    
        print dict_a_b(d1, d2)
