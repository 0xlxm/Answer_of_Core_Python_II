#! /usr/bin/env python

import random

def genset():
    S = set()
    len_set = random.randrange(1, 11)
    for i in xrange(len_set):
        S.add(random.randint(0, 9))

    return S 

A = genset()
B = genset()

print A, B, A|B, A&B
