# mapper_most_common_words.py
import sys
import csv
import re

# List of stopwords to ignore
stopwords = set([
    "a", "the", "this", "that", "and", "is", "in", "it", "to", "of", "with", "as", 
    "for", "on", "was", "were", "there", "their", "has", "have", "had", "by", 
    "an", "be", "being", "been", "not", "are", "but", "which", "who", "whom", "how",
    "why", "you", "your", "my", "me", "we", "our", "its", "all", "any", "can", "could"
])

# Read input line by line
reader = csv.reader(sys.stdin)

# Skip the header
header_skipped = False

for row in reader:
    if not header_skipped:
        header_skipped = True  # Skip the header row
        continue

    # Ensure the row has the necessary columns
    if len(row) < 2:  # Assuming 'review/summary' is the second column
        continue

    review_summary = row[1].strip()  # Assuming 'review/summary' is the second column
    
    # Remove non-alphanumeric characters and convert to lowercase
    review_summary = re.sub(r'[^a-zA-Z\s]', '', review_summary.lower())
    
    # Split the review summary into words
    words = review_summary.split()

    # Filter out stopwords and count the remaining words
    for word in words:
        if word not in stopwords:
            print(f"{word}\t1")
