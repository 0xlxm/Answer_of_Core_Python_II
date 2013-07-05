#! /usr/bin/env python
#-*- coding: utf-8 -*-
#
#Rochambeau
#

''' Rochambeau '''

import random

def Rochambeau():
    slist = ['rock', 'paper', 'scissors']
    result = ['lose', 'win', 'tie', 'lose', 'win']
    print_menu()
    while True:
        try:
            choice = input('Your guess: ')
            if choice < 0 or choice > 3:
                continue
            elif choice == 0:
                break
            c_choice = random.randrange(3)
            print "your guess: %s \ncomputer's guess: %s \nresult:%s-%s, you %s." \
                        % (slist[choice - 1], slist[c_choice], slist[choice - 1], slist[c_choice], result[c_choice-choice + 3]) 
        except:
            continue

def print_menu():
    menu = '''
    This is a rock-paper-scisssors game between U and computer,
    please select your guess to begin the game:
    1) rock
    2) paper
    3) scisssors
    0) quit
    '''
    print menu

if __name__ == '__main__':
    Rochambeau()
