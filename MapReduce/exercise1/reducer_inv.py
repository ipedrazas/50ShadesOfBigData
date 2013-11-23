#!/usr/bin/env python

import sys


previous_key = None
total = 0


def output(previous_key, total):
    # print str(float(total)/10000) + "\t###\t" + previous_key 
    print str(total) + "\t" + previous_key 

for line in  sys.stdin:
    key, value = line.split("\t", 1)
    if previous_key != key:
        if previous_key is not None:
            output(previous_key, total)
        previous_key = key
        total = 0
    total += int(value)

if previous_key is not None:
    output(previous_key, total)

# Run as python mapper.py < input.txt | sort
