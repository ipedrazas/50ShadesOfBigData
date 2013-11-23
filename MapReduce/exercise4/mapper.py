#!/usr/bin/env python


import os
import re

path = '../../Data'
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]


for txt_file in text_files:
    f = open( os.path.join(path, txt_file))
    lines = f.readlines()
    f.close()
    for line in  lines:
        words = re.split(r"\W+", line)
        for word in words:
            if len(word) > 3:
                print word.lower() + "\t" + str(1)
