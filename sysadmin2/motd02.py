#!/usr/bin/env python
""" This is a motd type program with input

    Vern Ceder
    09/08/2010
"""

# get user's name
name = raw_input('Enter your name: ')

size = len(name)
print "Welcome to python", name
print "your name is", size, "characters long"
