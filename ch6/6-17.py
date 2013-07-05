#! /usr/bin/env python
# -*- coding: utf-8 -*-

def my_pop(l):
    print l
    data = l[0]
    print data 
    l.remove(data)
    print l
    return data

if __name__ == '__main__':
    data = raw_input('Enter the data of the list to pop: ')
    l_data = eval(data)
    re = my_pop(l_data)
    print 'poped', re, '\nafter pop:', l_data
