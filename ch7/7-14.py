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

print A, B#, A|B, A&B

i = 2
while i >= 0:
    l_AorB = raw_input('Your answer of A|B: ').split()
    for j, s in enumerate(l_AorB):
        l_AorB[j] = int(s)
    if set(l_AorB) != A|B:
        print 'incrrect! try again, %d oppurate remaining.' % i
        i = i - 1
    else:
        print 'excellent'
        break
else:
    print 'answer: A|B = ', A|B
