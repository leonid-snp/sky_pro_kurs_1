#!/usr/bin/python3

"""
У вас есть список букв алфавита, который заканчивается символом "–".

Со стандартного ввода подается номер позиции буквы.

Верните букву и следующую за ней.

А — это буква с номером 0.
"""

# Задача
"""
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 
  'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 
  'v', 'w', 'x', 'y', 'z', '-'
]

position = int(input())

print(...)
"""

# Решение
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', '-'
]

position = int(input())

print([alphabet[position], alphabet[position + 1]])
