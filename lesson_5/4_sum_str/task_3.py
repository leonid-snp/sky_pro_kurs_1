#!/usr/bin/python3

"""
Со стандартного ввода подается последовательность 0 и 1.
На ее основе составьте строку из слов true и false.

Пример ввода:
01010

Пример вывода:
FalseTrueFalseTrueFalse
"""

# Задача
"""
sequence = input()
"""

# Решение
sequence = input()

word = ''

for number in sequence:
    if number == '0':
        word += 'False'
    else:
        word += 'True'

print(word)
