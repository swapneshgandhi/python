#!/usr/bin/env python
""" This is a motd type program with commandline input
    Vern Ceder
    09/08/2010
"""

import sys
from datetime import datetime

# get user's name from command line
name = sys.argv[1]

size = len(name)
print "Welcome to python", name
print "The your name is", size, "characters long"

print "The program %s was called with the following %d arguments:" % (sys.argv[0], len(sys.argv) - 1)
for arg in sys.argv[1:]:
    print "    %s" % arg
    


