#!/usr/bin/env python

import sys

#data = sys.stdin.read()

data = open(sys.argv[1]).read()
# the above is a shortened form of:
#   infile = open(sys.argv[1])
#   data = infile.read()
chars = len(data)
words = len(data.split())
lines = len(data.split('\n'))

print ("{0}   {1}   {2}".format(lines, words, chars))
#sys.stdout.write(("{0}   {1}   {2}\n".format(lines, words, chars)))
