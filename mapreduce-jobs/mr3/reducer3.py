# Reducer
#!/usr/bin/env python3
import sys

# Reducer function
def reducer():
    current_user = None
    current_count = 0

    for line in sys.stdin:
        # Parse the input key-value pair (tab-separated)
        try:
            user_id, count = line.strip().split('\t')
            count = int(count)
        except ValueError:
            continue  # Skip lines with invalid counts

        # If user_id changes, emit the result for the previous user_id
        if current_user and user_id != current_user:
            print(f"{current_user}\t{current_count}")
            current_count = 0

        # Update current_user and increment count
        current_user = user_id
        current_count += count

    # Emit the final user_id
    if current_user is not None:
        print(f"{current_user}\t{current_count}")

if __name__ == "__main__":
    reducer()
