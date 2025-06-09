# combined_reducer.py
import sys

book_data = {}
review_counts = {}

for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespace

    if not line:  # Skip empty lines
        continue

    try:
        title, value = line.split('\t')

        # Check if value is numeric (review count)
        if value.isdigit():
            review_counts[title] = review_counts.get(title, 0) + int(value)
        else:  # Assume it's author data
            book_data[title] = value
    except ValueError:
        # Skip malformed lines
        continue

# Output the final results
for book_title in book_data:
    count = review_counts.get(book_title, 0)
    authors = book_data[book_title]
    print(f"{book_title}\t{authors}\t{count}")
