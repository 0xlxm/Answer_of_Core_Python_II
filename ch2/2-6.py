#! /usr/bin/evn python

# my version
#var = raw_input('Input a integer:')
#
#if int(var) == 0:
#	print 'var equal zero'
#elif int(var) > 0:
#	print 'var > 0'
#else: 
#	print 'var < 0'

# answer from author:
n = int(raw_input('enter a number:'))

if n < 0:
	print 'negative'
elif n > 0:
	print 'positive'
else:
	print 'zero'
