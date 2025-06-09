#!/usr/bin/env python3
import sys

current_publisher = None
total_score = 0
total_count = 0

# Read input from stdin
for line in sys.stdin:
    publisher, score, count = line.strip().split("\t")
    score = float(score)
    count = int(count)

    if publisher == current_publisher:
        total_score += score
        total_count += count
    else:
        if current_publisher:
            avg_score = total_score / total_count
            print(f"{current_publisher}\t{avg_score}")
        current_publisher = publisher
        total_score = score
        total_count = count

# Output last publisher's average
if current_publisher:
    avg_score = total_score / total_count
    print(f"{current_publisher}\t{avg_score}")
