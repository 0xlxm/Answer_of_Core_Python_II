#! /usr/asdf/env python

#i = aListSum = 0 
#aList = [2, 1, -0x92]
#aListLen = len(aList)
#
#while i < aListLen:
#	aListSum += aList[i]
#	i += 1
#print aListSum

Sum = 0
aList = []
for i in range(5):
	data = raw_input('enter a number:')
	Sum += float(data)
	aList += data
print Sum/5, aList

print sum(int(raw_input('enter a number: ')) for i in range(5))
