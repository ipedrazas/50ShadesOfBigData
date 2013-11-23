#!/usr/bin/env python


import os
import sys

from pymongo import Connection
from pymongo.errors import ConnectionFailure


path = '../Data'
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

try:
    conn = Connection(host="localhost", port=27017)
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)

db = conn['50Shades']


for txt_file in text_files:
    f = open( os.path.join(path, txt_file))
    lines = f.readlines()
    f.close()
    story = ""
    for line in  lines:
        story  += line
    entry = {'title': txt_file, 'story': story}
    db.books.insert(entry, safe=True)

