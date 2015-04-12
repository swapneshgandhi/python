#!/usr/bin/env python

""" switch.py - simulate a switch statement
"""

def one():
    print "You chose number 1"

def two():
    print "You chose number 2"

def three():
    print "You chose number 3"

menu = {'1':one, '2':two, '3': three}

if __name__ == '__main__':
    choice = raw_input("Choose 1, 2, 3 ")
    menu[choice]()
