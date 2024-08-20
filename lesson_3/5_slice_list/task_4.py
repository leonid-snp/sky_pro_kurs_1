#!/usr/bin/python3

"""
У вас есть список букв алфавита.

Со стандартного ввода подается число num, не равное 0.

Выведите последние num элементов.
"""

# Задача
"""
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 
  'h', 'i', 'j', 'k', 'l', 'm', 'n', 
  'o', 'p', 'q', 'r', 's', 't', 'u', 
  'v', 'w', 'x', 'y', 'z'
]

num = int(input())

sliced = ...

print(sliced)
"""

# Решение
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

num = int(input())

sliced = alphabet[len(alphabet) - num:]

print(sliced)
