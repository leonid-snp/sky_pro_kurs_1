#!/usr/bin/python3

"""
Со стандартного ввода подаются два слова.
Определите, какое слово длиннее.

Если первое слово длиннее, выведите «первое», если второе — выведите «второе».
Если слова одинаковой длины — выведите «одинаковые».

Пример вывода:
первое
"""

# Задача
"""
word_1 = input()
word_2 = input()
"""

# Решение
word_1 = input()
word_2 = input()

if len(word_1) > len(word_2):
    print('первое')
elif len(word_1) < len(word_2):
    print('второе')
else:
    print('одинаковые')