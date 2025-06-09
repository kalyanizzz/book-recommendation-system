#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys

current_title = None
price_sum = 0
count = 0

for line in sys.stdin:
    title, price = line.strip().split('\t')
    price = float(price)

    if current_title == title:
        price_sum += price
        count += 1
    else:
        if current_title:
            print(f"{current_title}\t{price_sum/count:.2f}")
        current_title = title
        price_sum = price
        count = 1

if current_title:
    print(f"{current_title}\t{price_sum/count:.2f}")