'''创建一个从单词到其出现情况的映射'''

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open('chinadaily.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])