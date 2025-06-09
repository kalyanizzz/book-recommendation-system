# reducer_most_common_words.py
import sys
from collections import Counter

# Use a Counter to count word occurrences
word_counts = Counter()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        word, count = line.split('\t')
        count = int(count)
        word_counts[word] += count
    except ValueError:
        # Log malformed lines for debugging
        print(f"WARNING: Skipping invalid line - {line}", file=sys.stderr)
        continue

# Output the top 20 most common words
for word, count in word_counts.most_common(20):
    print(f"{word}\t{count}")
