#! /usr/bin/env python

'''
9-14. Logging Results. Convert your calculator program
(Exercise 5-6) to take input from the command line, i.e.,
$ calc.py 1 + 2
Output the result only. Also, write each expression and result to a disk file. Issuing a
command of...
$ calc.py print
... will cause the entire contents of the "register tape" to be dumped to the screen and
file reset/truncated. Here is an example session:
    $ calc.py 1 + 2
    3
    $ calc.py 3 ^ 3
    27
    $ calc.py print
    1 + 2
    3
    3 ^ 3
    27
    $ calc.py print
    $
    Extra credit: Also strip out comments that begin after the first character.
'''

import os
import sys
import pickle

def Usage():
    print 'usage: ', sys.argv[0], " expression"

def dumptape(l):
    f = open('reset/truncated', 'w')
    for line in l:
        print line
        f.write(line+'\n')
    f.close() 
   
def calc(para):
    if os.path.exists('reset/truncated') and os.path.getsize('reset/truncated') > 0:
        f = open('reset/truncated')
        l = pickle.load(f)
        f.close()
    else:
        l = []
    str_ex = ''.join(para)
    if str_ex == 'print':
        dumptape(l)
    else:
        l.append(str_ex)
        str_ex = str_ex.replace('^', '**')
        val = eval(str_ex)
        print val
        l.append(`val`)
    return l

if __name__ == '__main__':
    if len(sys.argv) < 2:
        Usage()
    else:
        l = calc(sys.argv[1:])
        f = open('reset/truncated', 'w')
        pickle.dump(l, f)
        f.close()
