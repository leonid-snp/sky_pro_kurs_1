#!/usr/bin/python3

"""
Со стандартного ввода поступает слово.
Используя цикл range и срезы, отрезайте от него всё больше и больше букв.

Пример ввода:
Океания

Пример вывода:
Океания
кеания
еания
ания
ния
ия
я
"""

# Задача
"""
word = input()
"""

# Решение
word = input()

for i in range(len(word)):
    print(word[i:])
