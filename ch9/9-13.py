#! /usr/bin/env python

'''
9-13. Command-Line Arguments.
a.
What are they, and why might they be useful?
b.
Write code to display the command-line arguments which were entered.
'''

import sys

def show_cmd_arg():
    '''show the command line argument'''
    if len(sys.argv) > 0:
        print len(sys.argv), sys.argv

if __name__ == '__main__':
    show_cmd_arg()
