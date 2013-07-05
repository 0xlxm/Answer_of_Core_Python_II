#! /usr/bin/env python

'''
We use safe_float() to process a set of credit card transactions given in a file and read in as
strings. A log file tracks the processing.
'''

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        try:
            ccfile = open('carddata.txt', 'r')
            txns = ccfile.readlines()
        finally:
            ccfile.close()
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
        return
    
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balence)' % (total)
    log.close()

if __name__ == '__main__':
    main()
