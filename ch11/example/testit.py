#! /usr/bin/env python

def testit(func, *nkwargs, **kwargs):
    #print nkwargs, kwargs
    try:
        #retval = func( kwargs['base'], *nkwargs)
        retval = func(base= 16, *nkwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal,base= 16)
            
            if retval[0]:
                print '%s(%s) = ' % (eachFunc.__name__, `eachVal`), retval[1]
            else:
                print '%s(%s) = FAILED:' % (eachFunc.__name__, `eachVal`), retval[1]

if __name__ == '__main__':
    test()
