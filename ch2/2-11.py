#! /usr/bin/env python

def print_menu():
    print '(1) get the sum of 5 numbers'
    print '(2) get the average of 5 numbers'
    print '(X) exit'

def Sum(list):
    sum_num = 0
    for i in range(5):
        sum_num += int(list[i])
    return sum_num
    
def average(sum):
    return float(sum)/5.0

sumList = []
while True:
    print_menu()
    n = raw_input('your choice: ')
    if n == '1':
        for i in range(5):
            num = raw_input('Num :')
            sumList += num
        num = Sum(sumList)
        print 'sum', num 
    elif n == '2':
       print average(num)
    else:
        break
