#!/usr/bin/env python

import sys



for line in  sys.stdin:
    words = line.split()
    for word in words:
        print word.decode('utf-8') + "\t" + str(1)

