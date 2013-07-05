#! /usr/bin/env python
#
#

""" something """

import math

def print_menu():
    """print menu for choice"""
    print '(a) squares and cubes;'
    print '(b) circles and spheres.'
    choice = raw_input('Your choice: ')
    if choice == 'a':
        side = float(raw_input("input the side: "))
        print calculate('a', side)
    if choice == 'b':
        ridus = float(raw_input("input the ridus: "))
        print calculate('b', ridus)

def calculate(choice, ridus):
    """ calculate the area or and the volume """
    re = []
    if choice == 'a':
        re += [ridus * ridus]
        re += [re[0] * ridus]
        return re
    elif choice == 'b':
        re += [math.pi * ridus * ridus]
        re += [4.0/3.0 * re[0] * ridus]
        return re

if __name__ == '__main__':
    print_menu()

