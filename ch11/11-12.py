#! /usr/bin/env python
#! /usr/bin/env python

'''
11-12. Passing Functions. Write a sister function to the testit() function described in this
       chapter. Rather than testing execution for errors, timeit() will take a function object
       (along with any arguments) and time how long it takes to execute the function. Return
       the following values: function return value, time elapsed. You can use time.clock() or
       time. time(), whichever provides you with greater accuracy. (The general consensus
       is to use time.time() on POSIX and time.clock() on Win32 systems.) Note: The timeit
       () function is not related to the timeit module (introduced in Python 2.3).
'''

import time

def testit(func, *nkwargs, **kwargs):
    #print nkwargs, kwargs
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result

def timeit(func, *nkwargs, **kwargs):
    stime = time.time()
    try:
        retval = func(*nkwargs, **kwargs)
        etime = time.time()
        result = etime - stime
    except Exception, diag:
        result = (False, str(diag))
    return  result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            timeretval = timeit(eachFunc, eachVal)
            
            if retval[0]:
                print '%s(%s) = ' % (eachFunc.__name__, `eachVal`), retval[1], '; time costed: %fms.'% (timeretval * 1000000)
            else:
                print '%s(%s) = FAILED:' % (eachFunc.__name__, `eachVal`), retval[1]

if __name__ == '__main__':
    test()
