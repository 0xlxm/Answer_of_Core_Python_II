#! /usr/bin/evn python

'''
Text Processing. Determine the total number of vowels, consonants, and words
(separated by spaces) in a text sentence. Ignore special cases for vowels and
consonants such as "h," "y," "qu," etc. Extra credit: create code to handle those
special case.
'''

vowels = ['a', 'e', 'i', 'o', 'u']

sentence = raw_input('input a sentense: ')

len_vow = len([c for c in sentence if c in vowels])
len_con = len(sentence) - len_vow

print 'There are %d vowels and %d consonants :)' % (len_vow, len_con)
