#!/usr/bin/env python

""" execute something outside of Python
"""

import subprocess
##can do this with popen as well it's more general purpose
retcode = subprocess.call(['ls', '-l', '/home'])
print "returned", retcode

retcode = subprocess.call(['ls', '-l', '/home/nobody'])
print "returned", retcode
