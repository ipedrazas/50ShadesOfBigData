#!/usr/bin/env python

import sys

from pymongo import Connection
from pymongo.errors import ConnectionFailure


try:
    conn = Connection(host="localhost", port=27017)
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)

db = conn['50Shades']


previous_key = None
total = 0


def output(previous_key, total):
    entry = {'w': previous_key, 'v': total}
    db.exercise4_2.insert(entry, safe=True)


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
