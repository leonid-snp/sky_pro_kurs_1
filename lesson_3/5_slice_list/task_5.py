#!/usr/bin/python3

"""
У вас есть два списка букв.
Со стандартного ввода подается число count.

Возьмите первые count букв из второго списка и добавьте к первому,
используя метод extend.
"""

# Задача
"""
letters_1 = ["A", "B", "C", "D"]
letters_2 = ["E", "F", "G", "K", "L", "M", "N"]

count = int(input())

letters_1...

# Не удаляйте код ниже, он нужен для проверки

print("".join(letters_1))
"""

# Решение
letters_1 = ["A", "B", "C", "D"]
letters_2 = ["E", "F", "G", "K", "L", "M", "N"]

count = int(input())

letters_1.extend(letters_2[:count])

# Не удаляйте код ниже, он нужен для проверки

print("".join(letters_1))
