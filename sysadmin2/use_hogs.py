#!/usr/bin/env python
""" use_hogs.py - import a function from another module
"""

from hogs import get_totals
import sys

if __name__ == '__main__':
    file_rows = sys.stdin.readlines()
    user_totals = get_totals(file_rows)
    for user in user_totals:
        print "%-20s %10s" % user
