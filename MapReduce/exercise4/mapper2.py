#!/usr/bin/env python


import os
import re
from textblob import TextBlob

path = '../../Data'
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]


for txt_file in text_files:
    f = open( os.path.join(path, txt_file))
    text = TextBlob(open( os.path.join(path, txt_file)).read().decode("utf-8"))
    for word in text.words:
        if len(word) > 3:
            try:
                print word.lower() + "\t" + str(1)
            except:
                pass

