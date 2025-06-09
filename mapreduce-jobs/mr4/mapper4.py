#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys
import csv

csv_reader = csv.reader(sys.stdin)
headers = next(csv_reader)

title_index = headers.index('Title')
price_index = headers.index('Price')

for row in csv_reader:
    if row[title_index] and row[price_index]:
        print(f"{row[title_index]}\t{row[price_index]}")