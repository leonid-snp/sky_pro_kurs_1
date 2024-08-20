#!/usr/bin/python3

"""
Со стандартного ввода поступает фраза, содержащая звездочки в неожиданных местах. Удалите их все.

Пример ввода:
Thi*s is *the pytho*nic wa*y

Пример вывода:
This is the pythonic way
"""

# Задача
"""
words = input()
"""

# Решение
words = input()

new_word = words.replace('*', '')
print(new_word)