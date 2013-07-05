#! /usr/bin/env python

'''
9-8. Module Introspection. Extract module attribute information. Prompt the user for a
module name (or accept it from the command line). Then, using dir() and other builtin
functions, extract all its attributes, and display their names, types, and values.
'''

while True:
    #try:
    mn = raw_input('enter module name: ')
    if mn == 'q':
        break
    mn = __import__(mn)
    properties = dir(mn)
    for p in properties:
        print p
        if isinstance(getattr(mn, p), (int, long, float, complex, str)):
            value = getattr(mn, p)
        else:
            value = None
        print 'properties name: ', p, ',properties type:', type(p), ',properties value: ', value
    #except:
    #    print 'no such module, try again!'
    #    continue
