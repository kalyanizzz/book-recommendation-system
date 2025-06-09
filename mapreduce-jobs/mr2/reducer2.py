#!/usr/bin/env python3
import sys

current_title = None
total_score = 0.0
total_count = 0

# Store results to sort later
results = []

for line in sys.stdin:
    try:
        title, score, count = line.strip().split("\t")
        score = float(score)
        count = int(count)

        # Aggregate data for the same title
        if title == current_title:
            total_score += score
            total_count += count
        else:
            # Store the average for the previous title
            if current_title:
                avg_score = total_score / total_count
                results.append((current_title, avg_score))
            
            # Start aggregating for the new title
            current_title = title
            total_score = score
            total_count = count
    except:
        continue

# Add the last title to the results
if current_title:
    avg_score = total_score / total_count
    results.append((current_title, avg_score))

# Sort results by average score in descending order
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

# Output top books
for title, avg_score in sorted_results[:10]:  # Adjust the number for top N
    print(f"{title}\t{avg_score:.2f}")
