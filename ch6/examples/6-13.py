#! /usr/bin/env python
#-*- coding: utf-8 -*-

def atoc(string):
    '''6-13 输入字符串返回复数，只能用complex不能用eval'''
    cindex = string.rfind('-')
    if cindex <= 0:
        cindex = string.rfind('+')
    if cindex >0 :
        real = float(string[0:cindex])
        compl = float(string[cindex:-1])
    return complex(real,compl)

print atoc(raw_input('Enter a complex string: '))
