#! /usr/bin/env pyton

def countToFour1():
    for eachNum in range(5):
        print eachNum, 
    print

def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum,
    print

def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum,
    print

def main():
    for n in (2, 4, 5):
        #countToFour1(n)
        #countToFour2()
        countToFour3()

if __name__ == '__main__':
    main()

