# combined_mapper.py
import sys
import csv

# Read input from stdin
reader = csv.reader(sys.stdin)
header_skipped = False

for row in reader:
    if not header_skipped:
        header_skipped = True  # Skip the header row
        continue

    if len(row) == 0:  # Skip empty rows
        continue

    book_title = row[0]  # Book Title column (Index 0)
    authors = row[2]     # Authors column (Index 2)
    
    # Emit review count
    print(f"{book_title}\t1")
    # Emit author data
    print(f"{book_title}\t{authors}")
