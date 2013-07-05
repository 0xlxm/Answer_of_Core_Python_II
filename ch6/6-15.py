#! /usr/bin/env python
#-*- coding:utf-8 -*-

'''
Conversion.
a.
Given a pair of dates in some recognizable standard format such as MM/DD/YY
or DD/MM/YY, determine the total number of days that fall between both dates.
b.
Given a person's birth date, determine the total number of days that person
has been alive, including all leap days.
c.
Armed with the same information from (b) above, determine the number of
days remaining until that person's next birthday.
'''

import string, time, copy

def print_menu():
    print '''
    a) calculate the days between two given dates D1 - D2;
    b) Calculate how many days have somebody lived since born
       according to his/her birthday;
    c) Calculate how many days remaining until that person's next birthday;
    q) quit
    '''

def isleapyear(y):
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

def all_days(date):
    leap_y = month_d = 0
    m_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for y in xrange(1,date[2]):
        if isleapyear(y):
            leap_y += 1
    if isleapyear(date[2]) and date[0] > 2:
        leap_y += 1
    for m in xrange(date[0] - 1):
        month_d += m_days[m]
    return date[2] * 365 + leap_y + month_d + date[1]
    
def cal():
    print_menu()
    while True:
        try:
            choice = raw_input('Your choice: ')
            #if choice != 'a' and choice != 'b' and choice != 'c' and choice != 'q':
            if choice not in 'abcq':
                print 'please input one of a,b,c,q, thanks!'
                continue
            if choice == 'q':
                break
            if choice == 'a':
                date = raw_input('Please input two date:MM/DD/YYYY - MM/DD/YYYY: ').split('-')
                date_bk = copy.deepcopy(date)
                for i in xrange(2):
                    date[i] = date[i].split('/')
                    for j in xrange(3):
                        date[i][j] = string.atoi(date[i][j])
                print 'There are %d days between %s to %s' % ((all_days(date[1]) - all_days(date[0])), date_bk[0], date_bk[1]) 
            elif choice == 'b':
                date = [None,None]
                date[0] = raw_input('Please input the birthing of him/her(MM/DD/YYYY): ').split('/')
                date[1] = list(time.localtime()[:3])
                date[0] = [string.atoi(date[0][0]), string.atoi(date[0][1]), string.atoi(date[0][2])]
                (date[1][0],date[1][1],date[1][2]) = (date[1][1],date[1][2],date[1][0])
                print 'He/she have lived for %d days!' % (all_days(date[1]) - all_days(date[0]))
            elif choice == 'c':
                date = [None,None]
                date[0] = raw_input('Please input the birthing of him/her:(MM/DD/YYYY) ').split('/')
                date[1] = list(time.localtime()[:3])
                (date[1][0],date[1][1],date[1][2]) = (date[1][1],date[1][2],date[1][0])
                date[0] = [string.atoi(date[0][0]), string.atoi(date[0][1]),date[1][2]]
                if date[0][0] < date[1][0]:
                    date[0][2] += 1
                elif date[0][0] == date[1][0]:
                    if date[0][1] < date[1][1]:
                        date[0][2] += 1
                remain_days = all_days(date[0]) - all_days(date[1])
                print 'There are remaining %d days until your next birthday!' % remain_days
                if remain_days == 0:
                    print 'so today is your birthday, Happy birthday!'
        except:
            print 'wrong input; please try again:'
            continue
          
if __name__ == '__main__':
    cal()
