#! /usr/bin/env python

""" Conversion between Fahrenheit to Celsius temperature values """

def covert(F):
    """ covert F to C """
    C = (F -32) * (5.0 / 9.0)
    return C        
if __name__ == '__main__':
    F = input('enter the Fahrenheit temperature: ')
    print covert(F)
