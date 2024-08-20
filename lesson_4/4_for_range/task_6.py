#!/usr/bin/python3

"""
С помощью конструкции for in range() выведите список, начиная с элемента "Alpha".

Пример вывода:
Alpha
Echo
...
Foxtrot
"""

# Задача
"""
words = ["Zero", "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
"""

# Решение
words = ["Zero", "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

for i in range(1, len(words)):
    print(words[i])
