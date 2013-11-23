#!/usr/bin/env python

import sys


counts = {}

for line in  sys.stdin:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


print counts
