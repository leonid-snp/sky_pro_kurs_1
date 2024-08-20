#!/usr/bin/python3

"""
У вас есть программа, в которой выводятся все слова.
Допишите программу, не удаляя ничего, так, чтобы слова короче 3 букв не выводились.
"""

# Задача
"""
words = ["int", "pk", "get", "round", "id", "if"]

for word in words: 

    # Допишите код тут

    print(word) # Не меняйте эту строку
"""

# Решение
words = ["int", "pk", "get", "round", "id", "if"]

for word in words:
    if len(word) < 3:
        continue

    print(word)  # Не меняйте эту строку
