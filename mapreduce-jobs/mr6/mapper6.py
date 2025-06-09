#!/usr/bin/env python3
import sys
import csv
import ast  # To safely parse list strings

# Read input line by line
for i, line in enumerate(sys.stdin):
    try:
        # Use csv.reader to handle structured CSV rows
        reader = csv.reader([line])
        for row in reader:
            # On the first line (header), find the index for 'authors'
            if i == 0:
                header = row
                authors_index = header.index("authors")
                continue

            # Process subsequent rows
            authors = row[authors_index]
            author = ast.literal_eval(authors)  # Convert string to list
            if isinstance(author, list):
                for genre in author:
                    print(f"{author}\t1")
    except Exception as e:
        continue
