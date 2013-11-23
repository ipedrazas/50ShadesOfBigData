#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

path = '../Data/txt'
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]


for txt_file in text_files:
    f = open( os.path.join(path, txt_file))
    lines = f.readlines()
    f.close()
    for line in  lines:
        words = re.split(" ", line)
        for word in words:
            if len(word) > 2:
                m = re.search(r'[a-z|A-Z]+', word)
                if m:
                    print m.group().lower() + "\t" + str(1)

