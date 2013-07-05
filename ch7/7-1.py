#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Dictionary Methods.

''' What dictionary method would we use to combine two dictionaries together '''

def updatedict():
    dict1 = {}.fromkeys(('x', 'y'), 1)
    dict2 = {'name':'earth', 'port':'80'}

    dict1.update(dict2)
    return dict1

if __name__ == '__main__':
    print updatedict()
    print 'dict.update(dict)'
