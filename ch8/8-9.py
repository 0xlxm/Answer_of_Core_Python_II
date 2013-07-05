#! /usr/bin/env python

'''
Fibonacci Numbers. The Fibonacci number sequence is 1, 1, 2, 3, 5, 8, 13, 21, etc. In
other words, the next value of the sequence is the sum of the previous two values in
the sequence. Write a routine that, given N, displays the value of the Nth Fibonacci
number. For example, the first Fibonacci number is 1, the 6th is 8, and so on.
'''

def Fibonacci(num):
    i = 0
    temp1 = F1 = 1
    temp2 = F2 = 1
    while i < num - 2:
        temp1 = F1
        temp2 = F2
        F2 = F1 + F2
        F1 = temp2
        i = i+1
    return (temp1, temp2, F2)

if __name__ == '__main__':
    n = input('given N: ')
    print 'previous two is %d %d, and the %dth is %d' % (Fibonacci(n)[0], Fibonacci(n)[1], n, Fibonacci(n)[2])
