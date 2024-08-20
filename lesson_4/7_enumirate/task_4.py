#!/usr/bin/python3

# Решение
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

for i, letter in enumerate(letters, start=1):
    if i % 2 == 0:
        print(i, letter)
