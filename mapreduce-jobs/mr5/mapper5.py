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
            # On the first line (header), find the index for 'categories'
            if i == 0:
                header = row
                categories_index = header.index("categories")
                continue

            # Process subsequent rows
            categories = row[categories_index]
            genres = ast.literal_eval(categories)  # Convert string to list
            if isinstance(genres, list):
                for genre in genres:
                    print(f"{genre}\t1")
    except Exception as e:
        continue
