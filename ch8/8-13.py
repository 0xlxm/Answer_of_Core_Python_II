#! /usr/bin/env python

'''
Performance. In Section 8.5.2, we examined two basic ways of iterating over a
sequence: (1) by sequence item, and (2) via sequence index. We pointed out at the
end that the latter does not perform as well over the long haul (on my system here, a
test suite shows performance is nearly twice as bad [83% worse]). Why do you think
that is?
'''

import sys

#test_list = range(10000000)
mod_list = ['Walter', 'Nicole', 'Steven', 'Henry']
test_list = mod_list*1000000

def by_sequence_index():
    for i in range(len(test_list)):
        print test_list[i] 

def by_sequence_item():
    for i in test_list:
        print i

if sys.argv[1] == 1:
    by_sequence_index()
elif sys.argv[1] == 2:
    by_sequence_item()
else:
    print test_list
