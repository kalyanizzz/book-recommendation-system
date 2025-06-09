# Mapper

#!/usr/bin/env python3
import sys

# Mapper function
def mapper():
    for line in sys.stdin:
        # Split the line into fields (assume comma-separated values)
        fields = line.strip().split(',')
        
        # Extract User_id (assume it's in the first column)
        if len(fields) > 0:
            user_id = fields[0]  # Adjust index based on input data format
            print(f"{user_id}\t1")

if __name__ == "__main__":
    mapper()
