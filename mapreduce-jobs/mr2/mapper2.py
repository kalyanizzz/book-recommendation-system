#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    try:
        # Parse each line as JSON
        fields = json.loads(line.strip())
        title = fields.get("title", "Unknown Title").strip()
        score = fields.get("review/score", None)
        
        # Emit valid scores
        if title and score is not None:
            print(f"{title}\t{score}\t1")
    except Exception as e:
        # Ignore any malformed data
        continue
