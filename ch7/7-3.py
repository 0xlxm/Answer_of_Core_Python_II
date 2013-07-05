#! /usr/bin/env python

# Dictionary and List Methods

'''
a.
Create a dictionary and display its keys alphabetically.
b.
Now display both the keys and values sorted in alphabetical order by the key.
c.
Same as part (b), but sorted in alphabetical order by the value. (Note: This has
no practical purpose in dictionaries or hash tables in general because most
access and ordering [if any] is based on the keys. This is merely an exercise.)
'''

# a)
dict1 = {'asdf':88, 'xxx':8999, 'qsdfas':1, (1,2):'tuple(1,2'}

key_dict1 = sorted(dict1.keys())
vale_dict1 = sorted(dict1.values())

print key_dict1

# b)
for key in  key_dict1:
    print key,dict1[key],  
print

for val in vale_dict1:
    for i in xrange(len(dict1)):
        if dict1[key_dict1[i]] == val:
            print key_dict1[i],dict1[key_dict1[i]],
        
