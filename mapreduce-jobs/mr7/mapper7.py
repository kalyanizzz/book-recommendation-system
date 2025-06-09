#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    try:
        fields = eval(line.strip())
        publisher = fields.get('publisher', 'unknown')
        score = float(fields.get('review/score', 0))
        print(f"{publisher}\t{score}\t1")
    except:
        continue
