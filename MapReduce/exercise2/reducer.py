#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


previous_key = None
total = 0


def output(previous_key, total):
    print previous_key + " \t " + str(total)

for line in  sys.stdin:
    if '\t' in line:
        key, value = line.split("\t", 1)
        if previous_key != key:
            if previous_key is not None:
                output(previous_key, total)
            previous_key = key
            total = 0
        total += int(value)

if previous_key is not None:
    output(previous_key, total)

