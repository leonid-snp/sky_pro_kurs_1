#!/usr/bin/python3

# Решение
items = [True, True, False, True, True, False]

for index, value in enumerate(items, start=1):
    if value:
        print(index)
