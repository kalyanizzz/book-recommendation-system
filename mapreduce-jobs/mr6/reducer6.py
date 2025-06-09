#!/usr/bin/env python3
import sys
from collections import defaultdict

author_count = defaultdict(int)

# Aggregate counts for each genre
for line in sys.stdin:
    author, count = line.strip().split("\t")
    author_count[author] += int(count)

# Sort genres by count in descending order and take the top 20
top_authors = sorted(author_count.items(), key=lambda x: x[1], reverse=True)[:50]

# Output the results
for genre, count in top_authors:
    print(f"{genre}\t{count}")
