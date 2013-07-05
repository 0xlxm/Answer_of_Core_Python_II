#! /usr/bin/env python

#i = 0
#string = raw_input('input a string:')
#
#while i < len(string):
#	print string[i]
#	i += 1
#
#for c in string:
#	print c

s = raw_input('enter a string:')

for eachChar in s:
	print eachChar

for i in range(len(s)):
	print i, s[i]

i = 0
slen = len(s)
while i < slen:
	print i, s[i]
	i += 1

for i, x in enumerate(s):
	print i, x
