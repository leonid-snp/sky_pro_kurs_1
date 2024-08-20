#!/usr/bin/python3
"""
Со стандартного ввода подается 1 или 0.
Выведите «Дождь идет» или «Дождя нет» в зависимости от полученного значения.

Пример вывода:
Дождь идет, Дождя нет
"""

# Задача
"""
is_raining = bool(int(input()))

2_if ...
    print(...)

2_if ...
"""

# Решение
is_raining = bool(int(input()))

if is_raining:
    print('Дождь идет')

if not is_raining:
    print('Дождя нет')
