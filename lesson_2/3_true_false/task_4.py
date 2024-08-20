#!/usr/bin/python3
"""
Со стандартного ввода подается название файла.
Если название файла содержит .gif, выведите True. Иначе — False.

Пример вывода:
True, False
"""

# Задача
"""
filename = input()

...
"""

# Решение
filename = input()
print('True' if '.gif' in filename else 'False')
