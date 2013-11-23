#!/usr/bin/env python


import os
import re

path = '../Data'
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

exit_lines = []

for txt_file in text_files:
    with open(os.path.join(path, txt_file), 'r') as f:
        for line in f:
            words = re.split(r"\W+", line)
            for word in words:
                if len(word) > 2:
                    exit_lines.append(word.lower() + "\t" + str(1))

exit_lines.sort(key=lambda x: x.lower())

for line in exit_lines:
    print line
