#!/usr/bin/env python

from subprocess import Popen, PIPE

__author__ = 'swapnesh'

with open('infile') as infile:
    with open('outfile', 'w') as outfile:
        for line in infile:
            fields = line.split('\t')
            outfile.write(','.join(fields))

fileObj = open('infile')
wFileObj = open('outfile', 'w')

for line in fileObj:
    fields = [x.strip(' ') for x in line.split(',')]
    wFileObj.write('|'.join(fields))

proc = Popen('ls -l', shell=True, stdout=PIPE)
for line in proc.stdout:
    print line

lines = [line.strip() for line in open('filename')]


def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.
    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


f = open('bigFile')
for chuck in readInChunks(f):
    pass
    # do_something(chunk) # perl -ne 's/\n//; s/abc/\n/g; print' text.txt > processed_text.txt