#!/usr/bin/env python3
import sys
from collections import defaultdict

genre_count = defaultdict(int)

# Aggregate counts for each genre
for line in sys.stdin:
    genre, count = line.strip().split("\t")
    genre_count[genre] += int(count)

# Sort genres by count in descending order and take the top 20
top_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)[:20]

# Output the results
for genre, count in top_genres:
    print(f"{genre}\t{count}")
