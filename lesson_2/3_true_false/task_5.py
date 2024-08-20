#!/usr/bin/python3
"""
Со стандартного ввода подается количество денег на счете и цена курса,
который пользователь хочет купить. Выведите True, если денег достаточно, иначе — False.

Пример вывода:
True, False
"""

# Задача
"""
balance = int(input())
course_price = int(input())
"""

# Решение
balance = int(input())
course_price = int(input())
print('True' if balance >= course_price else 'False')
